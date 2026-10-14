# Provenance — edbx-digital-ethics-compass

Stage A draft (2026-10-13), checked in stage B (2026-10-13) against
`papers/manifest.json` and `papers/pages/`. The two DDC web sources
(`ddc2021compass`: toolkit page and "Put the Human at the Center" page;
`ddc2021principles`: Principles, Automation, Behavioral Design and Data pages)
have text and every row that cites them is checked against it. `ddc2021case`
and the book are not in the manifest, so they cannot be checked. The compass
PDFs were not fetched. Locator `web` means a web page, not a PDF page.

## Sources

| Key | Citation | Stable URL | Free legal copy? | Licence |
|---|---|---|---|---|
| `ddc2021compass` | Dansk Design Center (DDC) (2021; launch year from the case page, 2022 for the current toolkit file). *The Digital Ethics Compass: Put the Human at the Center* (heuristic checklist "Ethics Navigator" plus ethics workshop). Developed with digital strategist Peter Svarre; funded by Industriens Fond; with the Confederation of Danish Industry. Toolkit page. | https://ddc.dk/tools/toolkit-the-digital-ethics-compass/ | Yes: the toolkit page offers a free ZIP and PDFs of the compass and knowledge cards (not downloaded). Also on-page: https://ddc.dk/tools/the-digital-ethics-compass-human-at-the-center/ | Site footer: unless otherwise noted, content is under a "Creative Commons Attribution License" (version not stated). Whether the PDFs and cards carry their own terms: unknown, check. |
| `ddc2021principles` | DDC. Digital Ethics Compass section pages: Principles, Automation, Behavioral Design, Data. | https://ddc.dk/tools/the-digital-ethics-compass-principles/ ; https://ddc.dk/tools/the-digital-ethics-compass-automation/ ; https://ddc.dk/tools/the-digital-ethics-compass-behavioral-design/ ; https://ddc.dk/tools/the-digital-ethics-compass-data | Yes (web pages). | Same CC Attribution footer. |
| `ddc2021case` | DDC. Case page, Digital Ethics Compass (creators, partners, launch). | https://ddc.dk/cases/digital-ethics-compass/ | Yes. | Same CC Attribution footer. |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design*. Rockport (Quarto). ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No. | Commercial book. I could not open its table of contents (O'Reilly returned 403; the Quarto page lists no contents), so whether it has a Digital Ethics Compass entry is unconfirmed. |

Not found in the page text (stage B): "cosmos", "wheel", "rotatable", "inner
ring", the hashtags #breakmydesign and #evaluateoutcomes, the name Peter Svarre,
and Industriens Fond. Each of these was searched in all five DDC page files.

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | The Compass is a heuristic tool for companies and design teams to make ethical design decisions | `ddc2021compass` | web | help companies make the right decisions from a design ethical standpoint | confirmed on the toolkit page |
| 2 | Two parts: a heuristic question set and a workshop (skill uses only the heuristics) | `ddc2021compass` | web | The tool has two features | confirmed: the compass (heuristics) and an ethical workshop. The page also confirms an extended course of 1-3 days. The talk (1-2 h) and 1-2 day workshop formats came from the case page `ddc2021case`, which is not in the manifest, so they are unchecked |
| 3 | Orienting centre "Put the Human in the Cosmos" | `ddc2021compass` | not in source | Put the Human at the Center | discrepancy confirmed against the text: the page title and principle say "at the Center"; the word "cosmos" appears on none of the five DDC pages |
| 4 | Four categories: Data, Avoid Manipulation, Make Intentions Transparent, Automation | `ddc2021compass` | not in source | you will find the five basic principles | discrepancy confirmed against the text: the middle of the Ethics Navigator holds five principles; the outer ring holds 22 questions in three categories (data, automation, behavioral design). "Avoid manipulating" and "Make your technology understandable" are two of the five principles, not categories |
| 5 | Printable wheel with inner, middle and outer rings of increasingly specific questions | `ddc2021compass` | not in source | In the outer ring of the Ethics Navigator | discrepancy confirmed against the text: the page describes a checklist with principles in the middle and 22 questions in the outer ring, plus downloadable PDFs. No inner ring, "wheel" or "rotatable" in the text; the middle ring holds principles, not questions |
| 6 | Data heuristics: collection proportionate, can users access data | `ddc2021principles` | web | Do you give people access to their own data | confirmed (Data page, question 04). Proportionality matches question 01, "Are you collecting too many data points, and do you keep them for too long?". The page has six data questions, adding anonymisation, storage, permission and profiling |
| 7 | Data heuristics: "what happens to data if the product shuts down", "how do you share data, with whom" | `ddc2021principles` | not in source | How do you store data | discrepancy confirmed against the text: the six Data questions do not ask about shutdown or sharing. Sharing appears only inside examples (Strava, DuckDuckGo) |
| 8 | Avoid Manipulation: does the product validate users or challenge/manipulate them | `ddc2021principles` | web | Do you validate or challenge your users | confirmed (Behavioral Design page, question 06). The page also asks about negative emotions, hidden information, concentration, social need and addiction |
| 9 | Avoid Manipulation: "use people's values against them", fear/urgency/social pressure, dark patterns, habits and cognitive biases | `ddc2021principles` | web | Also known as a dark pattern where you use cunning design tricks | partly confirmed: fear and urgency (question 01, hotel "hurry to book" example), social need (04), dark patterns (02). Not in the text: "use people's values against them" and "cognitive biases" (the stage-A claim that "dark patterns" was absent is overturned) |
| 10 | Make Intentions Transparent: can users understand how the product works | `ddc2021principles` | web | let users comprehend how the solutions work and affect their lives | confirmed, under the principle "Make your technology understandable". The skill's category name is not DDC's. Business incentives visible and algorithmic-curation disclosure are not worded on the pages (Behavioral Design page mentions recommendation echo chambers only in an example) |
| 11 | Automation: users know it is automated; algorithms prejudiced; system explains itself; transparent "engine room" | `ddc2021principles` | web | Are your algorithms prejudiced | confirmed (Automation page, question 06; also 01, 04 "engine room", 05 "explain itself"). The page has 10 questions; the skill's "responsible to automate" and "challenge automated decisions" are not worded there |
| 12 | Usable from single features to whole business models | `ddc2021compass` | not in source | decisions that designers, product managers and programmers make every day | discrepancy confirmed against the text: the page frames the tool around everyday design decisions by designers, product managers and programmers, and says it matters to top management. It does not state a range from single features to business models |
| 13 | Step 0 Stakeholder & Power Map, Step 0.5 Objective Function Risk Table, Step 0.6 Non-Obvious Harms Inventory | `ddc2021compass` | not in source | all those who may be affected by your digital solution | discrepancy confirmed against the text: Steps 0, 0.5 and 0.6 are not in the source. The closest passage says the human to keep at the center includes everyone affected, not only users, which loosely supports Step 0. SKILL.md itself cites an evaluation complaint, not DDC |
| 14 | Status colours, Business Pressure Attribution, Quick Win / Strategic Fix / Requires Leadership, Compass Reading | edbx additions | n/a | Quick Win Strategic Fix Requires Leadership | metadata only: edbx addition. Not in the DDC text |
| 15 | Hashtags #breakmydesign #evaluateoutcomes | `chivukula2025universal` | n/a | hashtags breakmydesign and evaluateoutcomes | metadata only: no source found. Absent from every DDC page; possibly from the book (unverified) |
| 16 | "See Also: Design with Intent; Responsible AI Practices" | none found | n/a | See Also Design with Intent | metadata only: no source found. Neither work was looked up |
| 17 | Universal Methods of Ethical Design as the secondary compilation | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: book. Entry unconfirmed |
| 18 | Evidence Ledger | fdbx family convention | n/a | Evidence Ledger family convention from fdbx | metadata only: edbx addition. Not from the source; SKILL.md says so |

## Licence

- **`ddc2021compass` and section pages.** Site-wide "Creative Commons
  Attribution License", version unspecified (CC BY is the licence name; 4.0 is
  likely but do not assume). CC BY permits commercial use, adaptation and
  redistribution with attribution. For this repo: paraphrasing is fine;
  reproducing the DDC question wording, the five principles or the knowledge
  cards is allowed if we credit "Dansk Design Center, The Digital Ethics
  Compass", link the licence, and note changes. Shipping a modified version is
  allowed under the same terms. Caveats: "unless otherwise noted" means a given
  PDF, image or the knowledge cards may carry other terms (unknown, check the
  PDFs); the site text is in Danish and English pages exist; the DDC name and
  logo are not covered by a CC licence.
- **Stage B check.** The footer sentence on both DDC pages (in Danish) says
  that, unless stated otherwise, all content on the site is under the Creative
  Commons Attribution License; no version is given. The toolkit page also says
  the kit is free and that the compass and knowledge cards are available as PDFs
  (not fetched, so their own terms are unchecked).
- **`chivukula2025universal`.** Commercial; paraphrase only, no verbatim text
  or diagrams.
- **Blockers.** None found for commercial redistribution or modification of the
  DDC-derived content, as long as attribution is added. SKILL.md currently has
  no attribution to DDC.

## Discrepancies

### Contradicted by the source text

1. **Centre wording (row 3).** SKILL.md says "Put the Human in the Cosmos",
   repeated through the skill including the output template. DDC's title and
   principle read "Put the Human at the Center". No "cosmos" on any DDC page.
   The output template asks every report to carry the wrong phrase. (fixed in SKILL.md)

2. **Structure (rows 4, 5).** SKILL.md has an inner ring of four categories
   (Data, Avoid Manipulation, Make Intentions Transparent, Automation) with
   middle and outer rings, as a "printable, rotatable wheel". DDC's Ethics
   Navigator has five principles in the middle and 22 questions in the outer
   ring, in three categories: Automation (10), Behavioral Design (6), Data (6).
   No inner ring, wheel or rotatable form in the text. "Behavioral Design" has
   no counterpart category in the skill; "Make Intentions Transparent" has none
   in DDC (closest: the principle "Make your technology understandable"). (fixed in SKILL.md)

3. **Data questions (row 7).** Shutdown handling and "how do you share data,
   with whom" are not among DDC's six Data questions. (fixed in SKILL.md)

4. **Manipulation items (row 9).** "Use people's values against them" and
   "cognitive biases" are not in the text. Fear, urgency, social pressure and
   dark patterns are (stage A wrongly reported dark patterns as absent). (fixed in SKILL.md)

5. **Skipped DDC content.** DDC's principles "Give users control" and "Avoid
   creating inequality", and automation items on law and human rights, job-skill
   loss, risk, readiness to step in, adaptability and security (question 10:
   hacking) are not in the skill. (fixed in SKILL.md)

6. **Scale claim (row 12).** The text does not say the compass spans single
   features to business models. (fixed in SKILL.md)

7. **Steps 0, 0.5, 0.6 (row 13)** are not in the source; they are skill
   additions, as are the status colours and implementation types (row 14). (fixed in SKILL.md)

8. **Attribution.** SKILL.md names no creator, year or licence. DDC is not
   credited, and CC BY requires attribution if DDC text is reproduced. (fixed in SKILL.md)

### Not verifiable

- Authors and funders (Peter Svarre, Industriens Fond, the Confederation of
  Danish Industry), the 2021 launch year, and the talk / 1-2 day workshop
  formats: they came from the case page `ddc2021case`, which is not in the
  manifest.
- Hashtags #breakmydesign and #evaluateoutcomes (row 15), and the "See Also"
  works (row 16): no source found.
- Whether the book has a Digital Ethics Compass entry (row 17).
- Whether the compass PDFs and knowledge cards carry terms other than the
  site-wide CC Attribution footer: the PDFs were not fetched.
