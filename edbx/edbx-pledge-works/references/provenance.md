# Provenance — edbx-pledge-works

Stage B (2026-10-13). One row per method element the skill attributes to a
source. For the one manifest source (`responsibletech2022pledge`, html, one
page, `papers/pages/responsibletech2022pledge/001.txt`) every anchor is copied
verbatim from that page; Locator `web` means found, `not in source` means the
page was read and the element is absent (the anchor is the closest passage).
Sources not in `papers/manifest.json` were not fetched and are marked
`metadata only`.

## Sources

| Key | Full citation | URL | Free copy | Licence |
|---|---|---|---|---|
| `responsibletech2022pledge` | ResponsibleTech.Work (team, individuals not named). *Pledge Works* (tool page; undated, still "under development"; the companion blog post is dated 2022-03-01). | https://responsibletech.work/tools/development/pledge-works/ | yes, web page | CC BY-SA 4.0 (site-wide statement on the pages read) |
| `responsibletech2022writing` (not in manifest; not fetched) | ResponsibleTech.Work team (2022-03-01). "Pledge Works: writing pledges for better outcomes". Blog post. | https://responsibletech.work/blog/2022/3/1/pledge-works-writing-pledges-for-better-outcomes/ | yes, web page | CC BY-SA 4.0 |
| `responsibletechndtoolbox` (not in manifest; not fetched) | ResponsibleTech.Work (n.d.). *Pledge Toolbox* (Ethical Solar System, Ethics Tree; "still under development"). | https://responsibletech.work/tools/business/pledge-toolbox/ | yes, web page | CC BY-SA 4.0 |
| `hartley2025pledge` (not in manifest; not fetched) | Hartley, D. (2025). Pledge Works case study: the startup (carbon offset company). The Public Good. Describes Pledge Works as "a ResponsibleTech.Work collaboration". | https://www.the-public-good.com/ethics/pledge-works/case-study-startup | yes, web page | "© Daniel Hartley 2025. All rights reserved" (site footer); no licence stated for the method |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work*. Rockport Publishers (Quarto Group), 1 April 2025. ISBN 9780760393086 (hardcover), 9780760393093 (ebook). Lists Pledge Works as method 71. | https://www.quarto.com/books/9780760393086/universal-methods-of-ethical-design ; method list: https://universalmethodsofethicaldesign.com/resources/ | no | unknown (commercial book; copyright statement not read; check the imprint page) |

The book is a secondary compilation. Its resources page lists "Pledge Works" as
method 71 with no creator credited and no link; the primary source is the
ResponsibleTech.Work page.

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Pledge Works as a method for writing pledges that bridge good intentions and everyday product decisions | `responsibletech2022pledge` | web | write pledges for better outcomes | Page: a tool to bridge the gap between good intentions and everyday product decisions; modular, "still under development", seeking broader validation |
| 2 | Pledges link design work to specific goals and carry a value and a context ("values + context = pledges" formula) | `responsibletech2022pledge` | not in source | commitments to yourself, your team, your customers | The extracted page text contains no values + context formula (stage A saw it as graphic alt text; not in the text). The page defines pledges as promises to seek better outcomes in context and says values and principles can be reflected at each level of granularity |
| 3 | Pledges can be made at every stage of the process; context-based pledges (scope of work: project, epic, sprint) | `responsibletech2022pledge` | web | written to fit a specific context or scope of work | Page: pledges are written at every step of existing processes, in cascading levels of granularity. Confirmed |
| 4 | Role-based pledges written from a professional role | `responsibletech2022pledge` | web | written from the perspective of a person's role | Page names the ACM Code of Ethics and communities of practice as inputs. Confirmed |
| 5 | Format A, Simple Pledge | `responsibletech2022pledge` | web | a pledge is a promise of how you intend to act responsibly | Page's company-level and project-level examples are "We pledge to respect people..." and "We will ensure people's anonymity on votes...". The "We will [action] to ensure/protect" templates are the skill's own (row 13) |
| 6 | Format B, Responsible Story ("As a [role], we pledge to [action]... because [reason]") | `responsibletech2022pledge` | web | declaration of WHO is making the pledge, the PLEDGE itself | Page: WHO, PLEDGE and an optional REASON, modelled on user stories. SKILL.md makes the "because" clause required (see Discrepancies) |
| 7 | Format C, To Whom Pledge (names the stakeholder: users, non-users, planet, future generations, community) | `responsibletech2022pledge` | web | To WHOM Pledges: an extension to the responsible story type | Page's audiences are people using the product, people not using it, the planet and clients. "Community" is not an audience on the page; "future generations" appears only inside the planet example's reason clause |
| 8 | Three-stage cycle: Review outcomes -> Write pledges in context -> Seek better outcomes | `responsibletech2022pledge` | web | The Pledge Works implementation cycle has three main elements | Page lists the elements in the order write pledges in context, seek better outcomes, review outcomes together. The kickoff is a separate section ("Responsible Project Kickoff"), not a fourth element of the cycle. The skill's starting point (review first) is not on the page |
| 9 | Review outcomes together (including compromises and unintended consequences; cross-functional) | `responsibletech2022pledge` | web | reviewing outcomes and pledges as a team | Page: be surprised by unintended consequences, make compromises that break pledges; include a cross-functional team; add the review to regular retrospectives. Confirmed |
| 10 | Pledges grow like a tree: visible outcomes above, structural roots below | `responsibletech2022pledge` | not in source | pledges adapt to your scope of work and change | The page has no tree metaphor. Closest passage: pledges adapt to scope of work and change with new learnings |
| 11 | Pledges can be sourced from other methods (worry sessions, assumption audits, etc.) | `responsibletech2022pledge` | web | outcomes from Consequence Scanning sessions or other ethical tools | Page lists ResponsibleTech.Work pledges, the Sustainable Web Manifesto, company values, professional codes and Consequence Scanning. It names no worry-session or assumption-audit method |
| 12 | Pledge checklists / acceptance criteria that show what upholding a pledge means | `responsibletech2022pledge` | web | pledge checklist that makes it clear what upholding each pledge means | Page: usable as acceptance criteria and "not set in stone". No numeric thresholds, owner, consequence or cadence |
| 13 | Stage 2 templates: company-wide / project-level Simple Pledge wording; minimums of 3 simple, 2 responsible stories, 1 to-whom per session | `responsibletech2022pledge` | not in source | ensure people's anonymity on votes both in the UI | Page has example pledges only. No fill-in templates and no per-session minimums |
| 14 | Stage 3 five required fields: success indicator, failure signal, named owner, consequence for breach, review cadence | `responsibletech2022pledge` | not in source | How will we know if we're upholding each pledge | Closest passage is a question to answer while writing pledges. The page asks for a checklist, not five fields. SKILL.md presents the fields as part of the method |
| 15 | Early-warning indicator per pledge; Pledge Stress Test against business pressure | `responsibletech2022pledge` | not in source | use the pledges to challenge the default outcome and explore alternatives | Page has no early-warning indicator or stress test. Closest idea is challenging default outcomes with pledges |
| 16 | "What We Refuse to Build" red-line register with veto owners | `responsibletech2022pledge` | not in source | Challenge user stories or tasks that break pledges | Page has no red-line register or veto owner. The worked red-line examples carry no source |
| 17 | Pledge-to-Product traceability table | `responsibletech2022pledge` | not in source | keep relevant pledges visible in whatever tool you use | Page suggests a "Pledge" label or column in Trello/Jira backlogs and roadmaps. It does not describe a traceability table mapping pledges to product changes |
| 18 | Evidence Ledger | none | n/a | the Evidence Ledger is a family convention from fdbx | metadata only: edbx addition. SKILL.md itself labels it a family convention, not part of the source method |
| 19 | Method catalogued as a book entry; hashtags `#alignmyteam #designresponsibility`; See Also: Hippocratic Oath, Ethical Contract | `chivukula2025universal` | method 71 (list only) | Universal Methods of Ethical Design | metadata only: book. Hashtags and See Also could not be checked; the resources page gives the name only |

## Licence

- **`responsibletech2022pledge`, `responsibletech2022writing`, `responsibletechndtoolbox` (CC BY-SA 4.0).** Stated on every ResponsibleTech.Work page read ("Creative Commons Attribution-ShareAlike 4.0 International"). Commercial use and modification are both allowed, with attribution, a licence link, and a note of changes. ShareAlike applies to adaptations of the licensed text. For this repo:
  - Paraphrasing the method (formats, cycle, the values + context idea): yes. Ideas are not covered; credit the source.
  - Reproducing page text, example pledges or the four diagrams verbatim, or adapting them closely: allowed only under CC BY-SA 4.0 with attribution; the adapted portion must then be shared under CC BY-SA 4.0 (or a compatible licence), not MIT. Keep such text out of the MIT-licensed skill files, or mark it and add a notice. The skill currently reuses only short names ("Simple Pledge", "Responsible Story", "To Whom"), and the example "pledge" sentences are the skill's own.
  - Shipping a modified version in a paid bundle: allowed under CC BY-SA for the licensed portion. Nothing found forbids commercial use. The share-alike condition is the one to flag; the MIT licence cannot be applied to copied portions.
  - Whether the CC licence covers the images (formula, process, kickoff, implementation-cycle graphics) was not stated separately; assume the site-wide licence and check the repository (github.com/ResponsibleTechWork/RespTechWork-website) before copying any diagram.
- **`hartley2025pledge`.** "All rights reserved" notice on the case-study site; no licence for the method. Do not copy the case study text, its decision-matrix formula or its spreadsheet.
- **`chivukula2025universal`.** Licence unknown; commercial book, so assume nothing may be reproduced beyond the name and number. Check the imprint page. Do not reproduce its entry text, diagrams or sidenotes.
- Nothing found blocks commercial redistribution. The one restrictive condition is CC BY-SA share-alike on any copied or closely adapted ResponsibleTech.Work material.

## Discrepancies

### Contradicted by the source text (read on the page `responsibletech2022pledge`)

1. **"Because" clause is required.** SKILL.md (Format B, Guardrails, Quality Bar) requires it. The page defines a responsible story as WHO, PLEDGE and an optional REASON (row 6).
2. **Cycle order and shape.** SKILL.md starts the cycle at "Review outcomes together". The page lists write pledges in context, seek better outcomes, review outcomes together, and treats the project kickoff as a separate section (row 8).
3. **Repo attribution.** `THIRD_PARTY_NOTICES.md` credits Pledge Works to professional ethics codes (medicine, law, engineering). The page presents Pledge Works as ResponsibleTech.Work's own tool and mentions professional codes only as a source for role-based pledges, naming the ACM Code of Ethics. This sits in the notices file, not SKILL.md, which should be corrected.
4. **Tree metaphor** (row 10): absent from the page.
5. **Session minimums and Format A/B/C sentence templates** (row 13): absent. The page gives example pledges only.
6. **Five operationalisation fields, early-warning indicator, stress test, red-line register with veto owners, traceability table** (rows 14-17): absent from the page, yet SKILL.md presents them as method stages (Stage 3, 3.5, 3.6, Quality Bar). Only the Evidence Ledger is labelled an edbx adaptation.
7. **To Whom audiences** (row 7): "community" is not on the page; "future generations" appears only in an example reason.
8. **Values + context formula** (row 2): not in the extracted page text.
9. **Year and status.** The page is undated. It calls itself "still under development" and "seeking broader validation in different contexts"; SKILL.md mentions neither.

### Not verifiable (no readable source)

10. "Hashtags" and "See Also" lines and the framing sentences that probably come from the book entry (method 71, a commercial book).
11. The `responsibletech2022writing` blog post (dated 2022-03-01), the Pledge Toolbox page (including its "Ethics Tree") and the Hartley case study were not fetched, so the 2022 date and anything on those pages cannot be checked here.

### Licence statement found in the fetched page

The footer states that the ResponsibleTech.Work site content is under a Creative Commons Attribution-ShareAlike 4.0 International licence. This confirms the stage A licence entry for the page text.
