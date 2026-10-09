#!/usr/bin/env bash
# Build upload files for people who install by hand:
#   dist/veteran-companion.plugin   Customize > Plugins > Add > Upload plugin (all skills)
#   dist/<skill>-skill.zip          Customize > Skills > + > Upload a skill (one skill)
set -euo pipefail
cd "$(dirname "$0")"
python3 -m unittest discover -s tests -q
rm -rf dist
mkdir dist
zip -qr dist/veteran-companion.plugin .claude-plugin skills README.md PRIVACY.md LICENSE \
  -x '*/__pycache__/*' '*.DS_Store'
for dir in skills/*/; do
  skill=$(basename "$dir")
  (cd skills && zip -qr "../dist/${skill}-skill.zip" "$skill" -x '*/__pycache__/*' '*.DS_Store')
done
ls -l dist
