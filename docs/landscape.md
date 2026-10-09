# Landscape: tools that overlap with Veteran Companion

Researched 2026-10-09 with web search, then checked again the same day against GitHub, claudskills.com and the official MCP registry. The registry timed out after one query, so MCP coverage is partial. Items marked **uncertain** were seen only on an aggregator or in search snippets and could not be confirmed. GitHub coverage is incomplete. Re-check before acting on any row.

## Key findings

- **No veteran Claude plugin or Agent Skill exists yet.** GitHub code search for SKILL.md files on VA disability, DD 214, CRSC and 38 CFR found none, and claudskills.com lists none. The closest Claude-native product is VeteranUnlocked, a set of free prompt packs for Claude Projects. It does not cover CRSC.
- **One AI product drafts CRSC applications, but none covers the whole claim.** Ezel.ai sells an AI-drafted CRSC application template ($99 per document). It does no Chapter 61 cap, rating-to-max or backpay math. The other CRSC tools are free month-to-month CRSC vs CRDP calculators, plus one open-source calculator on GitHub.
- **Veteran MCP servers exist but do not prepare claims.**
  - Wounded Warriors MCP: resources, CVSO finder, PACT Act matching, crisis routing.
  - VeteranHQ (official MCP registry): VA rating math, condition lookup and 38 CFR search. No CRSC.
  - Veterans' Rights BVA corpus: Board of Veterans' Appeals decision search and an accredited-representative directory.
  - Olyport VA Facilities connector.
  
  All four are integration targets.
- **Paid VA claim help is under heavy legal pressure in 2026.**
  - Veterans Guardian lost on liability in M.D.N.C. on May 20, 2026: the court found unaccredited agent activity.
  - Trajector filed Chapter 11 in July 2026, and the New York and Illinois AGs said they intend to sue.
  - GUARD VA Benefits Act (H.R. 1732) and SAFEGUARD Veterans Act (H.R. 9105 / S. 4646) would restore criminal penalties. Neither has passed.
  - PLUS for Veterans Act (H.R. 1656) would legalize paid help with a fee cap.
- **Most AI claim startups pair AI with human review.** VetClaims.ai charges $1,250 flat, uses human review, and says it does not provide representation. AI Joe and Vala use similar models. Two Stanford projects (Project Lembas, Vet's Claim) are building agentic claim guides.
- **VA is adding AI on its own side.** Its Automated Decision Support tool is expanding to more claim types, and VA says a human decides every claim. VISN 1 issued an RFI on 2026-04-03 for an AI benefits-application assistant.
- **CRSC sits outside VA's accreditation regime.** It goes to service boards under 10 U.S.C. 1413a, not VA. Any VA-claim feature falls under 38 U.S.C. 5901–5904 and 38 CFR 14.629.
- **CRSC backpay policy settled in May 2026, but litigation continues.** DoD guidance of 2026-05-14 withdrew the August 2025 and January 2026 limits, restored the statutory effective date, and told the services to re-review affected veterans. In Ploe v. United States (Fed. Cl. No. 1:25-cv-01942), class certification was still pending as of late May 2026.
- **The 2027 VA COLA takes effect December 1, 2026.** SSA announces the percentage on October 14, 2026; projections cluster around 3.6%. The CRSC skill's rate table needs an update then.

## How Veteran Companion compares

The closest tools for a retiree working a CRSC claim. "Partial" means the tool covers part of the job, as noted in the row below the table.

| Capability | Veteran Companion | Ezel.ai CRSC template | Free CRSC/CRDP calculators | VeteranHQ | VeteranUnlocked | VetClaims.ai |
|---|---|---|---|---|---|---|
| Covers CRSC | Yes | Yes | Yes | No | No | No |
| Maps evidence to the FMR combat-related criteria | Yes | Partial | No | No | No | No |
| Drafts DD 2860 pages and DD 3210 reconsideration | Yes | DD 2860 only | No | No | No | No |
| Monthly CRSC estimate | Yes | No | Yes | No | No | No |
| Chapter 61 caps | Yes | No | Partial | No | No | No |
| VA rating needed to max CRSC | Yes | No | No | No | No | No |
| Backpay after Soto | Yes | No | No | No | No | No |
| VA combined-rating math | Yes | No | Partial | Yes | No | Yes |
| VA claim preparation | No | No | No | Partial | Yes | Yes |
| Price | Free | $99 per document or $249/month | Free | Paid, 7-day trial | Free; needs Claude Pro | $1,250 flat |
| Open source, tested | Yes | No | One (stodo88) | No | No | No |
| Sends data elsewhere | No | Yes | Varies | Yes | Claude only | Yes |

Notes on "Partial":

- Ezel.ai's editor drafts a section for each combat-related category, but it does not read the veteran's records or check them against the FMR.
- Honest MOS mentions Chapter 61 but does not apply the cap. The free calculators combine ratings only to look up a VA rate.
- VeteranHQ does rating math and condition lookup, and scans decision letters on iOS. It does not draft a claim.

Veteran Companion's edge is the whole CRSC claim in one place, free and auditable. Its gaps are VA claims themselves, which it leaves to accredited help on purpose, and any lookup that needs live data.

## 1. AI-agent extensions

| Name | URL | What it is, who runs it | Price | Overlap | Role |
|---|---|---|---|---|---|
| VeteranUnlocked | veteranunlocked.com | Three Claude Project guides (Claims Builder, Care Guide, Project Setup), 30+ prompts; built by a veteran | Free; needs Claude Pro | High | Competitor, possible partner |
| Wounded Warriors MCP | warriorsfund.org/integrate; github.com/WoundedWarriors/wounded-warriors-mcp | MCP from a Texas 501(c)(3): resource directory, CVSO finder, PACT matching, crisis routing. The hosted page lists 43 tools and CC-BY 4.0; the GitHub README lists 5 tools, 11,000+ resources, MIT code and CC-BY data | Free | Medium | Integration target |
| VeteranHQ MCP (app.veteranhq/va-disability-benefits) | registry.modelcontextprotocol.io; veteranhq.app | Rating and compensation math, condition lookup, 38 CFR search; companion iOS app scans decision letters. No CRSC or CRDP | Paid app, 7-day trial | Medium | Competitor (VA side), integration target |
| Veterans' Rights BVA corpus (com.veterans-rights/bva-corpus) | mcpbundles.com/skills/veterans-rights-mcp-34aabe5090 | Search of Board of Veterans' Appeals decisions (listed as 34k vetted, 900k+ total) plus an accredited-representative directory | Unknown | Low | Integration target |
| VA Healthcare Facilities MCP (com.olyport) | glama.ai/mcp/connectors/com.olyport/va-healthcare | Facility search, detail and services | Free | Low | Integration target |
| apex-vetclaim | github.com/woadi-vector/apex-vetclaim | Hobby Slack agent using Gemini for rating triage | Open source | Medium | Reference |
| ag2-mcp-servers veteran-confirmation | GitHub | Generated MCP wrapper for VA's Veteran Confirmation API | Open source | Low | Reference |
| "Veteran Claims Assistant" GPT | robopost.app listing | Custom GPT for VA claims | ChatGPT Plus | Medium | Competitor (**uncertain**) |
| "VA Claims Navigator" GPT | robopost.app/en/toolpasta/tools/va-claims-navigator | Custom GPT on M21-1 and PTSD claims | ChatGPT Plus | Medium | Competitor (**uncertain**) |
| VADisabilityChat.com | Barchart press release, Sept 2024 | AI chatbot for VA claims | Unknown | Medium | Competitor (**uncertain** if active) |

Not found: veteran Gemini gems, or a veteran plugin in Anthropic's official marketplace (**uncertain**). Nearest non-veteran Claude skills: "managing-disability-evaluations" (psychiatric) and a healthcare "claims-appeals" skill on claudskills.com.

## 2. CRSC and CRDP tools

| Name | URL | What it is | Price | Overlap | Role |
|---|---|---|---|---|---|
| Ezel.ai CRSC Application | ezel.ai/templates/crsc-application | AI legal-forms editor that drafts each section of a CRSC application, including the combat-related categories; no cap, rating or backpay math | $99 per document or $249/month | High | Competitor (drafting) |
| stodo88/crsc-calculator | github.com/stodo88/crsc-calculator | Open-source CRSC calculator, July 2025 | Free | Medium | Reference |
| Honest MOS CRDP vs CRSC | honestmos.com/tools/crdp-crsc | Monthly comparison; mentions Chapter 61, no backpay | Free | High | Competitor (estimates) |
| VetCalc CRSC/CRDP | vetcalc.org/calculators/crsc-crdp/ | Side-by-side calculator on 2026 rates | Free | High | Competitor |
| Rank and Pay | rankandpay.org/tools/crsc-crdp-calculator/ | Recommends CRSC or CRDP | Free | High | Competitor |
| Military Transition Toolkit | militarytransitiontoolkit.com/crsc-calculator | CRSC calculator | Free | High | Competitor |
| claim.vet | claim.vet/blog/crsc-application-step-by-step/ | CRSC guides and calculators; refers users to attorneys | Free (referral fees) | Medium | Competitor (content) |
| PEB Forum calculator | pebforum.com | Community spreadsheet and estimates | Free | Medium | Referral |
| NVLSP Soto FAQ | nvlsp.org (05-2026 Soto v. U.S. Retroactive CRSC FAQ, PDF) | Plain-language guide to retroactive CRSC after Soto and the May 2026 DoD guidance | Free | Low | Skill reference, referral |
| Service CRSC boards | Army HRC, Navy/USMC Council of Review Boards, AFPC | Decide the DD 2860 | Free | n/a | Required destination |
| MOAA | moaa.org | Concurrent receipt explainers and advocacy | Free | Low | Referral |

## 3. VA claim assistance

| Name | URL | What it is | Price | Overlap | Role |
|---|---|---|---|---|---|
| VA Claims Insider | vaclaimsinsider.com | Coaching and nexus-letter network; not accredited | 6x the monthly increase | Medium | Competitor; legal-risk precedent |
| Trajector | news coverage | Unaccredited medical-evidence firm; Chapter 11 July 2026 | Contingency | Low | Cautionary example |
| Veterans Guardian | news coverage | Court found unaccredited agent activity, May 2026 | Contingency | Low | Cautionary example |
| VetClaims.ai | vetclaims.ai; ceoworld.biz 2026-08-22 | AI preparation with human review; says it does not provide representation | $1,250 flat | Medium-high | Competitor |
| AI Joe | moonshineink.com, Nov 2025 | AI claim filing; founded by Erik Menezes, ex-82nd Airborne, Truckee | Unverified | Medium | Competitor |
| Vala | techindex.law.stanford.edu/companies/vala | Legal-tech SaaS for claim workflows | B2B | Low | Possible partner |
| Project Lembas | knight-hennessy.stanford.edu/opportunities/project-lembas | Stanford Knight-Hennessy project, 2025: agentic guide that finds conditions, fills VA forms and hands off to humans | Unknown | Medium | Competitor, possible partner |
| Vet's Claim | insightintodiversity.com | Stanford CodeX hackathon project: AI claim assistant | Unknown | Low | Reference |
| VA Claims Made Easy | iOS app, April 2026 | AI record analysis, statement drafting, human reviewer | Unknown | Medium | Competitor |
| VET Mentor AI | audible.co.uk/pd/B0GK8ZVKBZ | Nexus letters and C&P exam practice avatars | Unknown | Medium | Competitor (**uncertain**) |
| AI VA Claims | producthunt.com/p/automated-veteran-affairs-claims/ai-va-claims | Automated VA claims product | Unknown | Medium | Competitor (**uncertain**) |
| Veteran AI; Seven Principles | search snippets only | AI veteran claim tools | Unknown | Unknown | **uncertain** |
| GitHub VA disability calculators | bhartman21, tiimbitz4786; darioangelreyes/VA-Claims-Agent-Demo | Hobby rating calculators (2026); the demo is a processing dashboard, not veteran-facing | Open source | Low | Reference |
| VA Automated Decision Support | nextgov.com 2026-03 | VA's internal AI for claim processing, expanding to more claim types; a human decides every claim | n/a | n/a | Context |
| VISN 1 AI benefits assistant RFI | highergov.com/contract-opportunity/va-aiassisted-benefit-application-support-rfi1804326-r-bf-re/ (2026-04-03) | VA request for information on an AI phone and web assistant for benefit applications | n/a | Medium | Watch; possible partner |
| VA Health and Benefits app | news.va.gov | Official app: claim status, evidence upload | Free | Low | Referral |
| VA.gov chatbot | va.gov/contact-us | Answers from VA.gov content | Free | Low | Referral |
| Accredited representative finder | va.gov/get-help-from-accredited-representative | Free VSO representatives; attorneys and agents may charge | Free | n/a | Primary referral |

No AI tools from DAV, VFW or the American Legion were found. Not verified: HadIt, VetLive. Military Times (2026-10-02) covers a court fight between two veterans over for-profit claims help; whether it involves any company above is **uncertain**.

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

1. **End-to-end CRSC.** Evidence mapped to the combat-related criteria, DD 2860 and DD 3210 drafting, Chapter 61 caps, the rating to max, and backpay in one place. Ezel.ai drafts the form and the calculators estimate the money, but no one does both from the veteran's own records.
2. **Claude-native, open and auditable.** VeteranUnlocked is prompts only. A skill bundle adds scripts, tests and dated rate tables.
3. **Compose existing MCPs** (Wounded Warriors for CVSO lookup and crisis routing, Veterans' Rights for BVA precedent and accredited representatives, VA Facilities) instead of rebuilding them.
4. **Hand off to free help.** Package the analysis for a VSO or CVSO instead of filing for the veteran.
5. **Retiree money questions.** CRDP vs CRSC election, SBP, CRSC's tax-free status on the 1099-R, VA waiver offsets.
6. **Re-review after the May 2026 DoD guidance.** Help veterans whose CRSC was approved with a receipt-date effective date check the corrected decision and backpay.
7. **Transition skills on open data.** O*NET crosswalk, SkillBridge, GI Bill comparison.

## Risks

- **VA accreditation (38 U.S.C. 5901, 5904; 38 CFR 14.629, 14.636).** Only accredited people may help prepare, present and prosecute VA claims. A free self-help tool the veteran runs is lower risk. Charging fees for VA-claim preparation is the conduct now losing in court. Keep VA-claim features free.
- **CRSC is a different regime.** Service boards decide it under 10 U.S.C. 1413a, so VA accreditation rules likely do not apply. No DoD rule on paid CRSC help was found (**uncertain**). Ezel.ai already charges for CRSC drafting. Advice to file with VA for a rating increase brings VA rules back in.
- **Pending law.** GUARD or SAFEGUARD would make unaccredited paid help a crime. State laws (New York, Louisiana litigation) apply too. Check them before any paid tier.
- **Accuracy and staleness.** Rates change December 1. CRSC backpay policy changed three times between August 2025 and May 2026, and Ploe is still open. Date-stamp tables and label every figure an estimate.
- **Health and personal data.** Users share DD 214s and medical records. Keep processing local and say the maintainer never sees it.
- **Unauthorized practice and medical advice.** No nexus opinions; never state a rating outcome as fact.
- **Crisis handling.** Any mental-health content must route to the Veterans Crisis Line (dial 988, then press 1).

## Sources

warriorsfund.org/integrate; github.com/WoundedWarriors/wounded-warriors-mcp; registry.modelcontextprotocol.io (search=veteran); veteranhq.app; mcpbundles.com/skills/veterans-rights-mcp-34aabe5090; glama.ai/mcp/connectors/com.olyport/va-healthcare; claudskills.com; veteranunlocked.com; ezel.ai/templates/crsc-application; github.com/stodo88/crsc-calculator; honestmos.com/tools/crdp-crsc; vetcalc.org/calculators/crsc-crdp/; rankandpay.org/tools/crsc-crdp-calculator/; claim.vet/blog/crsc-application-step-by-step/; nvlsp.org (May 2026 DoD guidance post; 05-2026 Soto FAQ); congress.gov H.R. 1732, H.R. 9105, S. 4646; policyrisk.com/legislation/HR1656; moaa.org 2026 GUARD Act articles; wgcu.org 2026-09-24 (Trajector); insurancenewsnet.com (Veterans Guardian ruling); militarytimes.com 2026-10-02; vaclaimsinsider.com/how-much-does-va-claims-insider-cost; under30ceo.com and ceoworld.biz 2026-08-22 (VetClaims.ai); knight-hennessy.stanford.edu/opportunities/project-lembas; insightintodiversity.com (Vet's Claim); nextgov.com 2026-03 (VA AI claims processing); highergov.com (VISN 1 RFI); cck-law.com (2027 COLA); law.cornell.edu/cfr/text/38/14.627; ecfr.gov 38 CFR 14.629; va.gov/get-help-from-accredited-representative; news.va.gov; dodtap.mil; onetonline.org/crosswalk/MOC/; va.gov/gi-bill-comparison-tool; hireheroesusa.org; apis.io/providers/va-gov.
