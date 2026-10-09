# CRSC Veteran Claim Assistant

Part of [Veteran Companion](../../README.md). Helps a military retiree file a Combat-Related Special Compensation (CRSC) claim or reconsideration, and estimates what it will pay.

It works from the veteran's own documents: the VA rating decision, retirement order, PEB findings, Retiree Account Statement, and service records. It produces:

- The maximum monthly CRSC, which limit sets it (VA waiver or Chapter 61 cap), the VA rating that reaches it, and the smallest sets of conditions that get there.
- Backpay under the statutory effective date, and under the receipt-date rule.
- DD 2860 entries for each condition, typed 14.k continuation sheets, a cover memo, and an attachment list.
- For a denial, a DD 3210 reconsideration package that answers the stated reason.

The rules come from DoD 7000.14-R, Volume 7B, Chapter 63 and 38 CFR 4.25. CRSC claims go to the veteran's service CRSC board, not to VA. DFAS computes the actual payment.

## Use

Ask Claude something like "Help me file for CRSC" or "My CRSC claim was denied, here's the letter." Attach the documents when Claude asks for them. The VA rating decision, with every page, matters most.

## Files

| Path | Purpose |
|---|---|
| `SKILL.md` | Workflow, evidence rules, forms, filing addresses, money rules |
| `scripts/crsc_calc.py` | CRSC, ceiling, rating-to-max and backpay calculator |
| `data/va_rates_<year>.json` | VA compensation rate table |
| `examples/example_input.json` | Calculator input example |

Tests are in `tests/crsc_veteran_claim_assistant/`.

## Yearly maintenance

VA compensation rates change every December 1. To update:

1. Copy `data/va_rates_2026.json` to `va_rates_<year>.json`.
2. Enter the new rates from [va.gov](https://www.va.gov/disability/compensation-rates/veteran-rates/), the new `effective` date, and `cola_from_prior_year`.
3. Run `python3 -m unittest discover tests`, then bump `version` in `.claude-plugin/plugin.json`.

The calculator uses the newest file and warns once a table is more than a year old.

Backpay rules have changed three times since 2025 (Soto v. United States, DoD guidance of Aug 2025, Jan 2026 and May 2026, and Ploe v. United States). When guidance changes, update the Backpay section of `SKILL.md`.
