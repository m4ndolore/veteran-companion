# CRSC Veteran Claim Assistant

A Claude plugin that helps a military retiree file a Combat-Related Special Compensation (CRSC) claim or reconsideration, and estimates what it will pay.

It works from the veteran's own documents: the VA rating decision, retirement order, PEB findings, Retiree Account Statement, and service records. It produces:

- The maximum monthly CRSC, which limit sets it (VA waiver or Chapter 61 cap), the VA rating that reaches it, and the smallest sets of conditions that get there.
- Backpay under the statutory effective date, and under the receipt-date rule.
- DD 2860 entries for each condition, typed 14.k continuation sheets, a cover memo, and an attachment list.
- For a denial, a DD 3210 reconsideration package that answers the stated reason.

The rules come from DoD 7000.14-R, Volume 7B, Chapter 63 and 38 CFR 4.25.

This is a preparation aid, not legal or financial advice. DFAS computes the actual payment. Free accredited help is available from Veterans Service Organizations and NVLSP.

## Install

**From the Claude directory:** search for "CRSC Veteran Claim Assistant" and install it. Updates arrive automatically.

**Claude Code:**

```
/plugin marketplace add m4ndolore/veteran-companion
/plugin install crsc-veteran-claim-assistant
```

**Upload by hand:** download a file from the latest release.

- `crsc-veteran-claim-assistant.plugin`: in claude.ai, Customize > Plugins > Add > Upload plugin. Works on personal plans.
- `crsc-veteran-claim-assistant-skill.zip`: Customize > Skills > + > Upload a skill. Works on the Free plan. Turn on code execution under Settings > Capabilities so the calculator can run.

An uploaded copy does not update itself. Download a new file after each December rate change.

## Use

Ask Claude something like "Help me file for CRSC" or "My CRSC claim was denied, here's the letter." Attach the documents when Claude asks for them. The VA rating decision, with every page, matters most.

## Data handling

- The plugin reads the documents you share inside the conversation, including medical and service records.
- It stores nothing. It has no database, no log, and no files outside the conversation.
- It sends nothing anywhere. The calculator is a Python script that uses only the standard library, reads a local JSON file, prints to the screen, and makes no network calls.
- It is not meant for people under 18.

Do not post drafts that contain Social Security numbers, DoD IDs or medical details in a public group.

## Yearly maintenance

VA compensation rates change every December 1. To update:

1. Copy `skills/crsc-veteran-claim-assistant/data/va_rates_2026.json` to `va_rates_<year>.json`.
2. Enter the new rates from [va.gov](https://www.va.gov/disability/compensation-rates/veteran-rates/), the new `effective` date, and `cola_from_prior_year`.
3. Run `python3 -m unittest discover tests`, then bump `version` in `.claude-plugin/plugin.json`.

The calculator uses the newest file and warns once a table is more than a year old.

Backpay rules have changed three times since 2025 (Soto v. United States, DoD guidance of Aug 2025, Jan 2026 and May 2026, and Ploe v. United States). When guidance changes, update the Backpay section of `skills/crsc-veteran-claim-assistant/SKILL.md`.

## Development

```
python3 -m unittest discover tests     # calculator tests
claude plugin validate .               # manifest and skill frontmatter
./build.sh                             # tests, then dist/ upload files
```

## License

MIT. See [LICENSE](LICENSE).
