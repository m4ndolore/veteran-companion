#!/usr/bin/env python3
"""CRSC estimator. DoD 7000.14-R Vol 7B Ch 63 (FMR) + VA rate table.

Usage: python3 crsc_calc.py input.json      (or "-" to read stdin)
Prints: combined rating, gross CRSC, ceiling, max entitlement, rating needed
to reach the ceiling, condition combinations that reach it, and backpay.
All money is monthly USD. This is an estimate; DFAS computes the real amount.

Standard library only. Reads local files, writes stdout, makes no network calls.
VA rates load from the newest ../data/va_rates_*.json; add a new file each December.
"""
import itertools
import json
import sys
from datetime import date
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RETIREMENT_TYPES = ("longevity", "chapter61_under20", "chapter61_20plus")
COMBAT_VALUES = (True, False, "maybe")


class InputError(ValueError):
    pass


def load_rates(path=None):
    """Load a VA rate table. Default: the newest va_rates_*.json in DATA_DIR."""
    if path is None:
        files = sorted(DATA_DIR.glob("va_rates_*.json"))
        if not files:
            raise InputError(f"no va_rates_*.json in {DATA_DIR}")
        path = files[-1]
    with open(path) as f:
        t = json.load(f)
    t["rates"] = {int(k): tuple(v) for k, v in t["rates"].items()}
    t["effective"] = date.fromisoformat(t["effective"])
    return t


def add_months(d, n):
    return date(d.year + (d.month - 1 + n) // 12, (d.month - 1 + n) % 12 + 1, 1)


def months_between(start, end):
    """Whole months from start's month through end's month, inclusive."""
    return max(0, (end.year - start.year) * 12 + (end.month - start.month) + 1)


def combine(pcts):
    """38 CFR 4.25 / FMR 9.2 Table I.

    Combine highest first; each step's combined value is a whole number
    (rounded half up), and the final value rounds to the nearest 10 with 5 up.
    Example: 60, 30, 10 -> 72 -> 74.8 -> 75 -> 80.
    Returns (whole-number combined value, rounded rating).
    """
    v = 0
    for p in sorted(pcts, reverse=True):
        v = (100 * v + p * (100 - v) + 50) // 100  # integer math, half up
    return v, (v + 5) // 10 * 10 if v else 0


def va_rate(r, d, table):
    """VA monthly rate for combined rating r with dependents d (FMR 8.1.1 includes dependents)."""
    if r < 10:
        return 0.0
    a, sp, co, sc, kid, school, par, aa = table["rates"][r]
    if r < 30:
        return a
    spouse = d.get("spouse", False)
    kids_u18 = d.get("children_under_18", 0)
    kids_sch = d.get("children_in_school", 0)
    kids = kids_u18 + kids_sch
    if kids == 0:
        base = sp if spouse else a
    else:
        base = sc if spouse else co
        # base pays one child; others at their add-on rate (approximate when
        # the only children are school-age, which VA pays slightly higher)
        if kids_u18:
            extra_u18, extra_sch = kids_u18 - 1, kids_sch
        else:
            extra_u18, extra_sch = 0, kids_sch - 1
        base += extra_u18 * kid + extra_sch * school
    base += d.get("parents", 0) * par
    if spouse and d.get("spouse_aid_attendance", False):
        base += aa
    return round(base, 2)


def ceiling(inp):
    """Max CRSC allowed by FMR 8.2 (waiver) and 8.5 (Chapter 61 reduction)."""
    waiver = inp["va_waiver"]
    if inp["retirement_type"] == "longevity":
        return waiver, {"va_waiver": waiver, "note": "no Chapter 61 reduction"}
    rpb = inp["retired_pay_base"]
    remaining = max(0.0, inp["gross_retired_pay"] - waiver)
    if inp.get("multiplier_override"):
        mult = inp["multiplier_override"]
    else:
        # High-3/Final Pay: 2.5% per year, max 75%. BRS: 2.0% per year, max 60%.
        per_year, cap = (0.020, 0.60) if inp.get("brs") else (0.025, 0.75)
        mult = min(per_year * inp["years_for_cap"], cap)
    longevity = mult * rpb * inp.get("cola_factor", 1.0)
    limit = max(0.0, longevity - remaining)
    return min(waiver, limit), {"multiplier": round(mult, 4),
                                "longevity_retired_pay": round(longevity, 2),
                                "remaining_retired_pay": round(remaining, 2),
                                "chapter61_cap": round(limit, 2), "va_waiver": waiver}


def validate(inp):
    """Raise InputError with a plain message for anything the math depends on."""
    def need(key):
        if key not in inp:
            raise InputError(f"missing required field '{key}'")

    for key in ("retirement_type", "va_waiver", "conditions"):
        need(key)
    if inp["retirement_type"] not in RETIREMENT_TYPES:
        raise InputError(f"retirement_type must be one of {', '.join(RETIREMENT_TYPES)}")
    if inp["retirement_type"] != "longevity":
        for key in ("retired_pay_base", "gross_retired_pay"):
            need(key)
        if not inp.get("multiplier_override"):
            need("years_for_cap")
    for i, c in enumerate(inp["conditions"]):
        label = c.get("name", f"conditions[{i}]")
        for key in ("name", "pct"):
            if key not in c:
                raise InputError(f"{label}: missing '{key}'")
        pct = c["pct"]
        if not isinstance(pct, int) or isinstance(pct, bool) or pct % 10 or not 0 <= pct <= 100:
            raise InputError(f"{label}: pct must be 0-100 in steps of 10, got {pct!r}")
        if c.get("combat", False) not in COMBAT_VALUES:
            raise InputError(f"{label}: combat must be true, false or \"maybe\", got {c['combat']!r}")
    bp = inp.get("backpay")
    if bp:
        for key in ("effective_date", "through_date"):
            if key not in bp:
                raise InputError(f"backpay: missing '{key}'")


def backpay(bp, monthly, table):
    """Backpay through bp['through_date'], with months before the rate table's
    effective date paid at the prior year's rates."""
    end = date.fromisoformat(bp["through_date"])
    prior_factor = bp.get("prior_year_factor", 1 / (1 + table["cola_from_prior_year"]))

    def estimate(start):
        n = months_between(start, end)
        old = sum(1 for i in range(n) if add_months(start, i) < table["effective"])
        return n, old, monthly * (n - old) + monthly * prior_factor * old

    months, old, total = estimate(date.fromisoformat(bp["effective_date"]))
    out = {"months": months, "months_at_prior_rates": old,
           "monthly_used": monthly, "estimate": round(total, 2),
           "if_limited_to_receipt_date": bp.get("receipt_date")}
    if bp.get("receipt_date"):
        out["estimate_if_receipt_date_rule"] = round(
            estimate(date.fromisoformat(bp["receipt_date"]))[2], 2)
    return out


def run(inp, table=None, today=None):
    validate(inp)
    table = table or load_rates()
    today = today or date.today()
    deps = inp.get("dependents", {})
    cr_smc = inp.get("combat_related_smc", 0.0)
    ceil, parts = ceiling(inp)

    def pays(rating):
        return va_rate(rating, deps, table) + (cr_smc if rating else 0)

    cands = [c for c in inp["conditions"] if c.get("combat") in (True, "maybe")]
    whole, r = combine([c["pct"] for c in cands])
    gross = pays(r)
    out = {"rates_effective": table["effective"].isoformat(), "warnings": [],
           "combined_value": whole, "combined_rating": r,
           "gross_crsc_if_all_claimed_approved": round(gross, 2),
           "ceiling_detail": parts, "max_monthly_crsc": round(ceil, 2),
           "monthly_if_all_approved": round(min(gross, ceil), 2)}
    if today >= add_months(table["effective"], 12):
        out["warnings"].append(
            f"VA rate table is from {table['effective']:%B %Y}; a newer table is likely out. "
            f"Check {table['source']} before relying on these figures.")

    need = next((t for t in sorted(table["rates"]) if pays(t) >= ceil), None)
    out["rating_needed_to_max"] = need
    out["rate_at_needed_rating"] = round(pays(need), 2) if need else None

    combos = []
    for k in range(1, len(cands) + 1):
        for sub in itertools.combinations(cands, k):
            rr = combine([c["pct"] for c in sub])[1]
            combos.append((round(min(pays(rr), ceil), 2), rr, [c["name"] for c in sub]))
    combos.sort(key=lambda x: (-x[0], len(x[2])))
    seen, best = [], []
    for pay, rr, names in combos:
        if pay >= ceil - 0.005 and not any(s <= set(names) for s in seen):
            seen.append(set(names))
            best.append({"pays": pay, "rating": rr, "conditions": names})
    out["minimal_sets_reaching_max"] = best[:8]
    out["each_condition_alone"] = [{"name": c["name"], "rating": c["pct"],
                                    "pays": round(min(pays(c["pct"]), ceil), 2)} for c in cands]

    bp = inp.get("backpay")
    if bp:
        out["backpay"] = backpay(bp, bp.get("monthly_amount", out["monthly_if_all_approved"]), table)
    return out


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    try:
        if argv[1] == "-":
            inp = json.load(sys.stdin)
        else:
            with open(argv[1]) as f:
                inp = json.load(f)
        print(json.dumps(run(inp), indent=2))
    except (OSError, json.JSONDecodeError, InputError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
