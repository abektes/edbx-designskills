# Provenance — edbx-pledge-works

Stage A draft (2026-10-13). One row per method element the skill attributes to
a source. Locator and anchor are what could be confirmed from web pages read in
this pass (no files downloaded). Where a page could not confirm an element,
Locator says `to verify` and the anchor is a guess marked `(guess)`. Stage B
checks each anchor on the page.

## Sources

| Key | Full citation | URL | Free copy | Licence |
|---|---|---|---|---|
| `responsibletech2022pledge` | ResponsibleTech.Work (team, individuals not named). *Pledge Works* (tool page; undated, still "under development"; the companion blog post is dated 2022-03-01). | https://responsibletech.work/tools/development/pledge-works/ | yes, web page | CC BY-SA 4.0 (site-wide statement on the pages read) |
| `responsibletech2022writing` | ResponsibleTech.Work team (2022-03-01). "Pledge Works: writing pledges for better outcomes". Blog post. | https://responsibletech.work/blog/2022/3/1/pledge-works-writing-pledges-for-better-outcomes/ | yes, web page | CC BY-SA 4.0 |
| `responsibletechndtoolbox` | ResponsibleTech.Work (n.d.). *Pledge Toolbox* (Ethical Solar System, Ethics Tree; "still under development"). | https://responsibletech.work/tools/business/pledge-toolbox/ | yes, web page | CC BY-SA 4.0 |
| `hartley2025pledge` | Hartley, D. (2025). Pledge Works case study: the startup (carbon offset company). The Public Good. Describes Pledge Works as "a ResponsibleTech.Work collaboration". | https://www.the-public-good.com/ethics/pledge-works/case-study-startup | yes, web page | "© Daniel Hartley 2025. All rights reserved" (site footer); no licence stated for the method |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work*. Rockport Publishers (Quarto Group), 1 April 2025. ISBN 9780760393086 (hardcover), 9780760393093 (ebook). Lists Pledge Works as method 71. | https://www.quarto.com/books/9780760393086/universal-methods-of-ethical-design ; method list: https://universalmethodsofethicaldesign.com/resources/ | no | unknown (commercial book; copyright statement not read; check the imprint page) |

The book is a secondary compilation. Its resources page lists "Pledge Works" as
method 71 with no creator credited and no link; the primary source is the
ResponsibleTech.Work page.

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Pledge Works as a method for writing pledges that bridge good intentions and everyday product decisions | `responsibletech2022pledge` | Overview | write pledges for better outcomes | toolkit page. Page calls it a modular tool, "still under development" |
| 2 | Pledges link design work to specific goals and carry a value and a context | `responsibletech2022pledge` | formula graphic (alt text) | values + context = pledges | toolkit page |
| 3 | Pledges can be made at every stage of the process; context-based pledges (scope of work: project, epic, sprint) | `responsibletech2022pledge` | Pledge types | context-based pledges | toolkit page. Blog: pledges "at every step of your existing processes" (`responsibletech2022writing`) |
| 4 | Role-based pledges written from a professional role | `responsibletech2022pledge` | Pledge types | role-based pledges | toolkit page. Page names the ACM Code of Ethics as one source of role-based pledges |
| 5 | Format A, Simple Pledge | `responsibletech2022pledge` | Pledge formats | simple pledges | toolkit page. Page defines it as a plain promise of how to act responsibly. The two "We will [action] to ensure/protect…" templates are not on the page (row 13) |
| 6 | Format B, Responsible Story ("As a [role], we pledge to [action]… because [reason]") | `responsibletech2022pledge` | Pledge formats | responsible stories | toolkit page. Modelled on user stories: WHO, PLEDGE, optional REASON. The "because" clause is optional on the page; SKILL.md makes it required (see Discrepancies) |
| 7 | Format C, To Whom Pledge (names the stakeholder: users, non-users, planet, future generations, community) | `responsibletech2022pledge` | Pledge formats | To WHOM pledges | toolkit page. Page says it extends responsible stories and names audiences such as people using the product, people not using it, the planet, clients. "Future generations" and "community" are not on the page |
| 8 | Three-stage cycle: Review outcomes → Write pledges in context → Seek better outcomes | `responsibletech2022pledge` | Process steps | write pledges, seek better outcomes, review outcomes | toolkit page. Page describes a repeating cycle of those three, plus a "responsible project kickoff" stage. Cycle order on the page starts at write pledges |
| 9 | Review outcomes together (including compromises and unintended consequences; cross-functional) | `responsibletech2022pledge` | Process steps, review step | review outcomes together | toolkit page. Page says reviews can be added to existing retrospectives and pledges updated |
| 10 | Pledges grow like a tree: visible outcomes above, structural roots below | `responsibletech2022pledge` | not found on page | (guess) the pledges grow like a tree | not found. The page does not use a tree metaphor. The related Pledge Toolbox page lists an "Ethics Tree" tool (`responsibletechndtoolbox`); content of that tool not read |
| 11 | Pledges can be sourced from other methods (worry sessions, assumption audits, etc.) | `responsibletech2022pledge` | Sources of pledges | outcomes from Consequence Scanning | toolkit page. Page names Consequence Scanning, company values, professional codes, the Sustainable Web Manifesto. It does not name the family's other methods |
| 12 | Pledge checklists / acceptance criteria that show what upholding a pledge means (nearest source analogue of "success indicator") | `responsibletech2022pledge` | Pledge formats | pledge checklists | toolkit page. Page: usable as acceptance criteria in Trello or Jira, "not fixed". No quantitative thresholds, owner, consequence or cadence on the page |
| 13 | Stage 2 templates: company-wide / project-level Simple Pledge wording; minimums of 3 simple, 2 responsible stories, 1 to-whom per session | `responsibletech2022pledge` | to verify | (guess) We will [action] to ensure | not found. Page example: "We will ensure people's anonymity on votes both in the UI and on the API." No session minimums anywhere read |
| 14 | Stage 3 five required fields: success indicator, failure signal, named owner, consequence for breach, review cadence | none | n/a | n/a | not found. edbx addition, not in any page read |
| 15 | Early-warning indicator per pledge; Pledge Stress Test against business pressure | none | n/a | n/a | not found. edbx addition |
| 16 | "What We Refuse to Build" red-line register with veto owners | none | n/a | n/a | not found. edbx addition. Worked examples in the table (under-16 ad targeting, location data) are illustrative and carry no source |
| 17 | Pledge-to-Product traceability table | none | n/a | n/a | not found. edbx addition. Page says pledges stay "visible in backlogs and roadmaps" (`responsibletech2022pledge`), which is the nearest idea |
| 18 | Evidence Ledger | none | n/a | n/a | already declared in SKILL.md as a family convention from fdbx, not part of the source method |
| 19 | Method catalogued as a book entry; hashtags `#alignmyteam #designresponsibility`; See Also: Hippocratic Oath, Ethical Contract | `chivukula2025universal` | method 71 (list only) | Pledge Works | metadata only: book. Hashtags and See Also could not be checked; the resources page gives the name only |

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

### Contradicted by the source (I read the page and it says otherwise)

1. **"Because" clause is required.** SKILL.md (Format B, Guardrails, Quality Bar) says every Responsible Story must have a "because" clause. The source page defines the format as WHO, PLEDGE and an optional REASON (`responsibletech2022pledge`). The requirement is the skill's own rule, not the method's.
2. **Repo attribution.** `THIRD_PARTY_NOTICES.md` credits Pledge Works to "Professional ethics codes (medicine, law, engineering)". The method is a ResponsibleTech.Work collaboration (`responsibletech2022pledge`, `hartley2025pledge`) and is listed as method 71 in `chivukula2025universal`. The page mentions professional codes only as one source of role-based pledges (ACM Code of Ethics is named; medicine, law and engineering are not). This is in the notices file, not SKILL.md; the file should be corrected.
3. **Cycle order.** SKILL.md puts "Review outcomes together" first. The page lists write pledges, seek better outcomes, review outcomes as the cycle, with a project kickoff stage before it. Treated as a cycle the two are compatible; as a first step it is not what the page says.

### Not found in a readable source (could not confirm; the full source was not read or the page is silent)

4. Tree metaphor ("grow over time like a tree"): absent from the tool page and the blog post. The Pledge Toolbox has an "Ethics Tree" whose content was not read.
5. Session minimums (3 simple, 2 responsible stories, 1 to-whom) and the Format A/B/C sentence templates: no page read gives them.
6. The five operationalisation fields, early-warning indicator, stress test, red-line register, traceability table, and the three worked red-line examples: no page read contains them. They are presented as part of the method in the Overview, Stage 3, 3.5, 3.6 and the Quality Bar, but the source is silent. SKILL.md labels only the Evidence Ledger as an edbx adaptation.
7. "Hashtags" and "See Also" lines, the "Many practitioners have codes…" framing, and the "tree" paragraph probably come from the book entry (method 71), which could not be read (book, not free).
8. "To Whom" audiences "future generations" and "community": the page names users, non-users, planet and clients.
9. The method's year: the tool page is undated; 2022 is taken from the companion blog post. The source describes itself as "still under development" and "seeking broader validation", which SKILL.md does not mention.
