# Veteran Companion

A Claude plugin for military veterans, retirees and their families. It helps them claim the benefits they earned, improve their quality of life after service, and plan what comes next.

Veteran Companion is a set of skills. Each skill handles one job from the veteran's own documents and tells them what it found, what it is worth, and what to do next. Claude picks the right skill from what the veteran asks.

This is a preparation aid, not legal or financial advice. Free accredited help is available from Veterans Service Organizations and NVLSP.

## Skills

| Skill | What it does | Status |
|---|---|---|
| [CRSC Veteran Claim Assistant](skills/crsc-veteran-claim-assistant/README.md) | Builds or rescues a Combat-Related Special Compensation claim (DD 2860, DD 3210) and estimates monthly CRSC, the VA rating that maxes it, and backpay | Available |

## Install

**From the Claude directory:** search for "Veteran Companion" and install it. Updates arrive automatically, including each December's VA rate change.

**Claude Code:**

```
/plugin marketplace add m4ndolore/veteran-companion
/plugin install veteran-companion
```

**Upload by hand:** download a file from the latest release.

- `veteran-companion.plugin`: in claude.ai, Customize > Plugins > Add > Upload plugin. Works on personal plans and includes every skill.
- `<skill>-skill.zip`: Customize > Skills > + > Upload a skill. Works on the Free plan. Turn on code execution under Settings > Capabilities so calculators can run.

An uploaded copy does not update itself. Download a new file after each release.

## Data handling

- Veteran Companion reads the documents you share inside the conversation, including medical, service and pay records.
- It stores nothing. It has no database, no log, and no files outside the conversation.
- It sends nothing anywhere. Its scripts use only the Python standard library, read local files, print to the screen, and make no network calls.
- It is not meant for people under 18.

Do not post drafts that contain Social Security numbers, DoD IDs or medical details in a public group.

**Privacy:** read the full [Privacy Policy](PRIVACY.md).

## Repository layout

```
.claude-plugin/
  plugin.json          plugin manifest (name, version, icon, URLs)
  marketplace.json     lets Claude Code install from this repo
  icon.png, icon.svg
skills/
  <skill-name>/
    SKILL.md           instructions Claude follows
    README.md          what the skill does and how to maintain it
    scripts/           calculators, standard library only
    data/              dated reference tables
    examples/
tests/
  <skill_name>/        tests for that skill's scripts
```

## Adding a skill

1. Create `skills/<skill-name>/` with a `SKILL.md` whose `name` matches the folder and whose `description` says when Claude should use it.
2. Keep the skill self-contained: scripts, data and examples live inside its folder, so the folder also works as a standalone skill zip.
3. Scripts use only the Python standard library and make no network calls. That keeps the [Privacy Policy](PRIVACY.md) true.
4. Put reference data that changes on a schedule in `data/` with a date in the file name, and warn when it is out of date.
5. Add tests under `tests/<skill_name>/` with an empty `__init__.py`.
6. Add a row to the Skills table above and a `README.md` in the skill folder.
7. Bump `version` in `.claude-plugin/plugin.json`.

## Development

```
python3 -m unittest discover tests     # all skill tests
claude plugin validate .               # manifest and skill frontmatter
./build.sh                             # tests, then dist/ upload files
```

## License

MIT. See [LICENSE](LICENSE).
