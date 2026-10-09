# Landscape: tools that overlap with Veteran Companion

Researched 2026-10-09 with web search. Items marked **uncertain** were seen only on an aggregator or could not be confirmed. GitHub coverage is incomplete. Re-check before acting on any row.

## Key findings

- **No veteran Claude plugin or Agent Skill exists yet.** The closest Claude-native product is VeteranUnlocked, a set of free prompt packs for Claude Projects. It does not cover CRSC.
- **No AI tool builds CRSC claims.** Existing CRSC tools are free month-to-month CRSC vs CRDP calculators. None found models Chapter 61 caps or backpay, or drafts a DD 2860.
- **Veteran MCP servers exist but do not prepare claims.** The Wounded Warriors MCP (43 tools: resources, CVSO finder, PACT Act matching, crisis routing) and the Olyport VA Facilities connector are integration targets.
- **Paid VA claim help is under heavy legal pressure in 2026.**
  - Veterans Guardian lost on liability in M.D.N.C. on May 20, 2026: the court found unaccredited agent activity.
  - Trajector filed Chapter 11 in July 2026, and the New York and Illinois AGs said they intend to sue.
  - GUARD VA Benefits Act (H.R. 1732) and SAFEGUARD Veterans Act (H.R. 9105 / S. 4646) would restore criminal penalties. Neither has passed.
  - PLUS for Veterans Act (H.R. 1656) would legalize paid help with a fee cap.
- **AI claim startups pair AI with accredited humans.** VetClaims.ai charges $1,250 flat and uses accredited agents; AI Joe and Vala follow similar models.
- **CRSC sits outside VA's accreditation regime.** It goes to service boards under 10 U.S.C. 1413a, not VA. Any VA-claim feature falls under 38 U.S.C. 5901–5904 and 38 CFR 14.629.
- **The 2027 VA COLA takes effect December 1, 2026.** The CRSC skill's rate table needs an update then.

## 1. AI-agent extensions

| Name | URL | What it is, who runs it | Price | Overlap | Role |
|---|---|---|---|---|---|
| VeteranUnlocked | veteranunlocked.com | Three Claude Project guides (Claims Builder, Care Guide, Project Setup), 30+ prompts; built by a veteran | Free; needs Claude Pro | High | Competitor, possible partner |
| Wounded Warriors MCP | warriorsfund.org/integrate; github.com/WoundedWarriors/wounded-warriors-mcp | Hosted MCP from a Texas 501(c)(3): 6,500+ resources, CVSO finder, PACT matching, crisis routing | Free, CC-BY 4.0 | Medium | Integration target |
| VA Healthcare Facilities MCP (com.olyport) | glama.ai/mcp/connectors/com.olyport/va-healthcare | Facility search, detail and services | Free | Low | Integration target |
| apex-vetclaim | github.com/woadi-vector/apex-vetclaim | Hobby Slack agent using Gemini for rating triage | Open source | Medium | Reference |
| ag2-mcp-servers veteran-confirmation | GitHub | Generated MCP wrapper for VA's Veteran Confirmation API | Open source | Low | Reference |
| "Veteran Claims Assistant" GPT | robopost.app listing | Custom GPT for VA claims | ChatGPT Plus | Medium | Competitor (**uncertain**) |
| VADisabilityChat.com | Barchart press release, Sept 2024 | AI chatbot for VA claims | Unknown | Medium | Competitor (**uncertain** if active) |

Not found: veteran Gemini gems, or a veteran plugin in Anthropic's official marketplace.

## 2. CRSC and CRDP tools

| Name | URL | What it is | Price | Overlap | Role |
|---|---|---|---|---|---|
| Honest MOS CRDP vs CRSC | honestmos.com/tools/crdp-crsc | Monthly comparison; mentions Chapter 61, no backpay | Free | High | Competitor (estimates) |
| VetCalc CRSC/CRDP | vetcalc.org/calculators/crsc-crdp/ | Side-by-side calculator on 2026 rates | Free | High | Competitor |
| Rank and Pay | rankandpay.org/tools/crsc-crdp-calculator/ | Recommends CRSC or CRDP | Free | High | Competitor |
| Military Transition Toolkit | militarytransitiontoolkit.com/crsc-calculator | CRSC calculator | Free | High | Competitor |
| claim.vet | claim.vet/blog/crsc-application-step-by-step/ | CRSC guides and calculators; refers users to attorneys | Free (referral fees) | Medium | Competitor (content) |
| PEB Forum calculator | pebforum.com | Community spreadsheet and estimates | Free | Medium | Referral |
| Service CRSC boards | Army HRC, Navy/USMC Council of Review Boards, AFPC | Decide the DD 2860 | Free | n/a | Required destination |
| MOAA | moaa.org | Concurrent receipt explainers and advocacy | Free | Low | Referral |

## 3. VA claim assistance

| Name | URL | What it is | Price | Overlap | Role |
|---|---|---|---|---|---|
| VA Claims Insider | vaclaimsinsider.com | Coaching and nexus-letter network; not accredited | 6x the monthly increase | Medium | Competitor; legal-risk precedent |
| Trajector | news coverage | Unaccredited medical-evidence firm; Chapter 11 July 2026 | Contingency | Low | Cautionary example |
| Veterans Guardian | news coverage | Court found unaccredited agent activity, May 2026 | Contingency | Low | Cautionary example |
| VetClaims.ai | vetclaims.ai | AI preparation plus accredited agents | $1,250 flat | Medium-high | Competitor |
| AI Joe | moonshineink.com, Nov 2025 | Army veteran founder; AI claim filing | Unverified | Medium | Competitor |
| Vala | techindex.law.stanford.edu/companies/vala | Legal-tech SaaS for claim workflows | B2B | Low | Possible partner |
| VA Claims Made Easy | iOS app, April 2026 | AI record analysis, statement drafting, human reviewer | Unknown | Medium | Competitor |
| VA Health and Benefits app | news.va.gov | Official app: claim status, evidence upload | Free | Low | Referral |
| VA.gov chatbot | va.gov/contact-us | Answers from VA.gov content | Free | Low | Referral |
| Accredited representative finder | va.gov/get-help-from-accredited-representative | Free VSO representatives; attorneys and agents may charge | Free | n/a | Primary referral |

Not verified this pass: HadIt, VetLive, NVLSP.

## 4. Transition and quality of life

| Name | URL | Run by | Price | Overlap | Role |
|---|---|---|---|---|---|
| DoD TAP portal | dodtap.mil | DoD | Free | Low | Referral |
| SkillBridge | skillbridge.osd.mil | DoD | Free | Medium (future skill) | Data source, referral |
| O*NET Military Crosswalk | onetonline.org/crosswalk/MOC/ | DOL | Free | Medium | Integration (O*NET Web Services) |
| GI Bill Comparison Tool | va.gov/gi-bill-comparison-tool | VA | Free | Low | Referral |
| PTSD Coach | App Store | VA National Center for PTSD and DoD | Free | Low | Referral |
| Hire Heroes USA | hireheroesusa.org | Nonprofit | Free | Low | Referral |
| Onward to Opportunity | Syracuse IVMF | Nonprofit | Free | Low | Referral |
| Hiring Our Heroes | US Chamber Foundation | Nonprofit | Free | Low | Referral |

## 5. Open data and APIs

| Source | URL | Notes |
|---|---|---|
| VA Lighthouse | developer.va.gov | 22+ APIs; OAuth or API key; sandbox |
| Benefits Reference Data API | developer.va.gov/explore/api/benefits-reference-data | Disability and contention lookup tables; open |
| Facilities and Forms APIs | developer.va.gov | Open; Forms returns current versions and PDF URLs |
| Veteran Confirmation; Service History and Eligibility | developer.va.gov | Confirmation is open; service history needs veteran consent |
| Benefits Claims / Intake API | developer.va.gov | For VSOs and representatives filing 526s; assume an accredited user is required (**uncertain**) |
| VA compensation rates | va.gov | Change every December 1 |
| DFAS retired pay | dfas.mil | No official CRSC calculator found |

A skill that calls an API would break the plugin's no-network promise in [PRIVACY.md](../PRIVACY.md). Use these as sources for dated data files, or update the policy first.

## Gaps Veteran Companion could fill

1. **End-to-end CRSC.** Evidence mapped to the combat-related criteria, DD 2860 drafting, Chapter 61 caps and backpay in one place. Competitors stop at the calculator.
2. **Claude-native, open and auditable.** VeteranUnlocked is prompts only. A skill bundle adds scripts, tests and dated rate tables.
3. **Compose existing MCPs** (Wounded Warriors for CVSO lookup and crisis routing, VA Facilities) instead of rebuilding them.
4. **Hand off to free help.** Package the analysis for a VSO or CVSO instead of filing for the veteran.
5. **Retiree money questions.** CRDP vs CRSC election, SBP, CRSC's tax-free status on the 1099-R, VA waiver offsets.
6. **Transition skills on open data.** O*NET crosswalk, SkillBridge, GI Bill comparison.

## Risks

- **VA accreditation (38 U.S.C. 5901, 5904; 38 CFR 14.629, 14.636).** Only accredited people may help prepare, present and prosecute VA claims. A free self-help tool the veteran runs is lower risk. Charging fees for VA-claim preparation is the conduct now losing in court. Keep VA-claim features free.
- **CRSC is a different regime.** Service boards decide it under 10 U.S.C. 1413a, so VA accreditation rules likely do not apply. No DoD rule on paid CRSC help was found (**uncertain**). Advice to file with VA for a rating increase brings VA rules back in.
- **Pending law.** GUARD or SAFEGUARD would make unaccredited paid help a crime. State laws (New York, Louisiana litigation) apply too. Check them before any paid tier.
- **Accuracy and staleness.** Rates change December 1. Date-stamp tables and label every figure an estimate.
- **Health and personal data.** Users share DD 214s and medical records. Keep processing local and say the maintainer never sees it.
- **Unauthorized practice and medical advice.** No nexus opinions; never state a rating outcome as fact.
- **Crisis handling.** Any mental-health content must route to the Veterans Crisis Line (dial 988, then press 1).

## Sources

warriorsfund.org/integrate; github.com/WoundedWarriors/wounded-warriors-mcp; glama.ai/mcp/connectors/com.olyport/va-healthcare; veteranunlocked.com; honestmos.com/tools/crdp-crsc; vetcalc.org/calculators/crsc-crdp/; rankandpay.org/tools/crsc-crdp-calculator/; claim.vet/blog/crsc-application-step-by-step/; congress.gov H.R. 1732, H.R. 9105, S. 4646; policyrisk.com/legislation/HR1656; moaa.org 2026 GUARD Act articles; wgcu.org 2026-09-24 (Trajector); insurancenewsnet.com (Veterans Guardian ruling); vaclaimsinsider.com/how-much-does-va-claims-insider-cost; under30ceo.com (VetClaims.ai); law.cornell.edu/cfr/text/38/14.627; ecfr.gov 38 CFR 14.629; va.gov/get-help-from-accredited-representative; news.va.gov; dodtap.mil; onetonline.org/crosswalk/MOC/; va.gov/gi-bill-comparison-tool; hireheroesusa.org; apis.io/providers/va-gov.
