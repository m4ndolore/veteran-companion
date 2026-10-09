#!/usr/bin/env bash
# Build upload files for people who install by hand:
#   dist/crsc-veteran-claim-assistant.plugin     Customize > Plugins > Add > Upload plugin
#   dist/crsc-veteran-claim-assistant-skill.zip  Customize > Skills > + > Upload a skill
set -euo pipefail
cd "$(dirname "$0")"
python3 -m unittest discover -s tests -q
rm -rf dist
mkdir dist
zip -qr dist/crsc-veteran-claim-assistant.plugin .claude-plugin skills README.md PRIVACY.md LICENSE \
  -x '*/__pycache__/*' '*.DS_Store'
(cd skills && zip -qr ../dist/crsc-veteran-claim-assistant-skill.zip crsc-veteran-claim-assistant \
  -x '*/__pycache__/*' '*.DS_Store')
ls -l dist
