"""Tests for the CRSC calculator. Run: python3 -m unittest discover tests"""
import json
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "crsc-veteran-claim-assistant"
SCRIPT = SKILL / "scripts" / "crsc_calc.py"
EXAMPLE = SKILL / "examples" / "example_input.json"
sys.path.insert(0, str(SCRIPT.parent))

import crsc_calc as c  # noqa: E402

TABLE = c.load_rates()
IN_DATE = date(2026, 10, 1)


def example():
    return json.loads(EXAMPLE.read_text())


class CombineTest(unittest.TestCase):
    def test_table_one_rounds_each_step(self):
        # 60 + 30 = 72; 72 + 10 = 74.8 -> 75 -> 80. Exact math gives 74.8 -> 70.
        self.assertEqual(c.combine([10, 30, 60]), (75, 80))

    def test_five_rounds_up(self):
        self.assertEqual(c.combine([50, 10]), (55, 60))

    def test_common_pairs(self):
        self.assertEqual(c.combine([50, 30]), (65, 70))
        self.assertEqual(c.combine([40, 20]), (52, 50))
        self.assertEqual(c.combine([70, 50, 20, 10]), (89, 90))

    def test_empty_and_zero(self):
        self.assertEqual(c.combine([]), (0, 0))
        self.assertEqual(c.combine([0, 0]), (0, 0))

    def test_hundred(self):
        self.assertEqual(c.combine([100, 30]), (100, 100))


class RateTest(unittest.TestCase):
    def test_no_dependent_pay_below_30(self):
        self.assertEqual(c.va_rate(20, {"spouse": True}, TABLE), 356.66)

    def test_spouse_and_two_kids(self):
        self.assertEqual(c.va_rate(60, {"spouse": True, "children_under_18": 2}, TABLE), 1728.02)

    def test_zero_rating_pays_nothing(self):
        self.assertEqual(c.va_rate(0, {}, TABLE), 0.0)

    def test_table_is_complete(self):
        self.assertEqual(sorted(TABLE["rates"]), list(range(10, 101, 10)))
        for row in TABLE["rates"].values():
            self.assertEqual(len(row), len(TABLE["columns"]))


class CeilingTest(unittest.TestCase):
    def test_chapter61_under20(self):
        ceil, parts = c.ceiling(example())
        self.assertEqual(parts["longevity_retired_pay"], 3937.5)
        self.assertEqual(ceil, 1487.5)

    def test_brs_uses_two_percent(self):
        inp = dict(example(), brs=True)
        _, parts = c.ceiling(inp)
        self.assertEqual(parts["multiplier"], 0.35)

    def test_multiplier_capped_at_75(self):
        inp = dict(example(), retirement_type="chapter61_20plus", years_for_cap=34)
        _, parts = c.ceiling(inp)
        self.assertEqual(parts["multiplier"], 0.75)

    def test_longevity_limited_by_waiver_only(self):
        ceil, _ = c.ceiling({"retirement_type": "longevity", "va_waiver": 1200.0})
        self.assertEqual(ceil, 1200.0)


class RunTest(unittest.TestCase):
    def test_example(self):
        out = c.run(example(), today=IN_DATE)
        self.assertEqual(out["combined_rating"], 90)
        self.assertEqual(out["max_monthly_crsc"], 1487.5)
        self.assertEqual(out["rating_needed_to_max"], 60)
        self.assertEqual([s["conditions"] for s in out["minimal_sets_reaching_max"]],
                         [["TBI with PTSD"], ["Migraine", "Cervical spine"], ["Migraine", "Tinnitus"]])
        self.assertEqual(out["warnings"], [])

    def test_backpay(self):
        bp = c.run(example(), today=IN_DATE)["backpay"]
        self.assertEqual(bp["months"], 18)
        self.assertEqual(bp["months_at_prior_rates"], 5)
        self.assertEqual(bp["estimate"], 26572.42)
        self.assertEqual(bp["estimate_if_receipt_date_rule"], 2975.0)

    def test_receipt_date_rule_applies_prior_rates(self):
        inp = example()
        inp["backpay"]["receipt_date"] = "2025-11-01"
        bp = c.run(inp, today=IN_DATE)["backpay"]
        self.assertAlmostEqual(bp["estimate_if_receipt_date_rule"],
                               round(1487.5 * 13 + 1487.5 / 1.028, 2))

    def test_stale_table_warns(self):
        out = c.run(example(), today=date(2026, 12, 1))
        self.assertEqual(len(out["warnings"]), 1)
        self.assertIn("December 2025", out["warnings"][0])

    def test_only_true_and_maybe_are_combined(self):
        names = [x["name"] for x in c.run(example(), today=IN_DATE)["each_condition_alone"]]
        self.assertNotIn("Sleep apnea", names)


class ValidateTest(unittest.TestCase):
    def check(self, mutate, message):
        inp = example()
        mutate(inp)
        with self.assertRaises(c.InputError) as ctx:
            c.validate(inp)
        self.assertIn(message, str(ctx.exception))

    def test_bad_retirement_type(self):
        self.check(lambda i: i.update(retirement_type="medical"), "retirement_type")

    def test_missing_years(self):
        self.check(lambda i: i.pop("years_for_cap"), "years_for_cap")

    def test_pct_not_step_of_ten(self):
        self.check(lambda i: i["conditions"][0].update(pct=75), "steps of 10")

    def test_bad_combat_value(self):
        self.check(lambda i: i["conditions"][0].update(combat="yes"), "combat must be")

    def test_backpay_missing_dates(self):
        self.check(lambda i: i["backpay"].pop("through_date"), "through_date")


class CliTest(unittest.TestCase):
    def test_cli_runs_example(self):
        res = subprocess.run([sys.executable, str(SCRIPT), str(EXAMPLE)],
                             capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(res.stdout)["max_monthly_crsc"], 1487.5)

    def test_cli_reports_bad_input_without_traceback(self):
        res = subprocess.run([sys.executable, str(SCRIPT), "-"], input='{"conditions": []}',
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 1)
        self.assertTrue(res.stderr.startswith("error: missing required field"))


if __name__ == "__main__":
    unittest.main()
