# Provenance — edbx-ethicography

Stage A (sources and licences, no downloads). One row per method element the
skill attributes to a source. Locator and anchor are filled only where I read
the page (landing page, abstract, repository record). Where I could not read
the full text, Locator is `to verify` and the anchor is a guess marked
`(guess)`. No PDF was fetched; the full text of the CHI 2019 paper was not
read, so every claim about its internals is unconfirmed until stage B.

Pages read: PAR (NSF Public Access Repository) record 10092725 (CHI 2019
paper), PAR record 10190994 and the DRS Digital Library page (DRS 2020 paper),
the Deceptive Patterns page for the DIS 2018 paper, the UXP2 corpus page, the
arXiv abstract and ar5iv HTML of the 2021/2022 survey paper, the Quarto/Rockport
book page, the Purdue e-Pubs record for the Chivukula dissertation, and the
Everyday Ethics method page for Ethicography (the best readable description of
the method's steps).
The ACM DL page (403) and ResearchGate (403) could not be read.

## Sources

| Key | Citation | DOI / URL | Legal free copy |
|---|---|---|---|
| `chivukula2019ethicography` | Chivukula, S. S., Gray, C. M., & Brier, J. A. (2019). Analyzing Value Discovery in Design Decisions Through Ethicography. CHI '19, Paper 77, pp. 1-12. ACM. | doi:10.1145/3290605.3300307; PAR record https://par.nsf.gov/biblio/10092725 | Yes: accepted manuscript on PAR (record above, labelled "Free Publicly Accessible Full Text", NSF award 1657310); author preprint linked from https://darkpatterns.uxp2.com/?p=764 |
| `chivukula2018dark` | Chivukula, S. S., Brier, J., & Gray, C. M. (2018). Dark intentions or persuasion? UX designers' activation of stakeholder and user values. DIS '18 Companion. | doi:10.1145/3197391.3205417; https://deceptive.design/articles/dark-intentions-or-persuasion-ux-designers-activation-of-stakeholder-and-user-values | Not confirmed; ACM page not readable. Check PAR |
| `chivukula2020coevolving` | Chivukula, S. S., & Gray, C. M. (2020). Co-Evolving Towards Evil Design Outcomes: Mapping Problem and Solution Process Moves. DRS 2020. | doi:10.21606/drs.2020.107; https://dl.designresearchsociety.org/drs-conference-papers/drs2020/researchpapers/2 | Yes: PDF on the DRS Digital Library page; also PAR 10190994 |
| `chivukula2021surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J., & Gray, C. M. Surveying the Landscape of Ethics-Focused Design Methods (arXiv v1 2021-02-17, v2 2022-08-26; published in ACM Journal on Responsible Computing, 2024 per the UXP2 lab page). | arXiv:2102.08909 (https://arxiv.org/abs/2102.08909) | Yes: arXiv |
| `chivukula2025universal` | Chivukula, S. S., & Gray, C. M. Universal Methods of Ethical Design: 100 Ways to Apply Ethically Centered Design Practices. Rockport Publishers (Quarto), listed as published 1 April 2025. ISBN 9780760393086 (hardcover), 9780760393093 (eBook). | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (commercial book) |
| `uxp2021ethicography` | Design Ethically / Everyday Ethics microsite, "Ethicography" method page (method credited to Sai Shruthi Chivukula; page published by Thomas Carlock, 9 April 2021; cites the CHI 2019 paper). | https://everydayethics.uxp2.com/methods/ethicography/ | Yes: free web page |
| `friedman2003values` | Friedman, B., & Kahn, P. H., Jr. (2003). Human values, ethics, and design. In *The Human-Computer Interaction Handbook*, pp. 1223-1248. Lawrence Erlbaum. (Cited by the method page as the a priori value list.) | not looked up | No (book chapter) |
| `goldschmidt1990linkography` | Goldschmidt, G. (1990). Linkography: assessing design productivity (the relational analysis method Ethicography extends; year given by a search summary, not a page I read). | not looked up | to verify |

## Rows

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The method itself: Ethicography, a method for analysing design decisions | `chivukula2019ethicography` | abstract | Analyzing Value Discovery in Design Decisions Through Ethicography | free copy: https://par.nsf.gov/biblio/10092725 |
| 2 | Authorship: skill credits "Chuvaala, Gray et al." | `chivukula2019ethicography` | title page / PAR record | Chivukula, Gray, Brier | free copy: https://par.nsf.gov/biblio/10092725. Authors are Chivukula, Gray, Brier; see Discrepancies |
| 3 | Year: "(2019, 2024)" | `chivukula2019ethicography` | PAR record | published May 4, 2019 | free copy: https://par.nsf.gov/biblio/10092725. 2019 confirmed; 2024 see Discrepancies |
| 4 | Design decisions treated as data, analysed for the values shaping them | `chivukula2019ethicography` | abstract | how values shape designers' decisions | free copy: https://par.nsf.gov/biblio/10092725 |
| 5 | Method applied to UX design students in lab tasks (evidence base) | `chivukula2019ethicography` | abstract | UX design students in two lab protocol conditions | free copy: https://par.nsf.gov/biblio/10092725 |
| 6 | Output identifies specific values designers considered and shows how they interact (the "ethicograph") | `chivukula2019ethicography` | abstract | visualizing the interplay of these values | free copy: https://par.nsf.gov/biblio/10092725 |
| 7 | Speech acts (what people say in design dialogue) as the unit of analysis | `uxp2021ethicography` | Steps, step 1 | Unitize the speech acts | toolkit page: https://everydayethics.uxp2.com/methods/ethicography/ . Source material there is "a design activity or a conversation among designers" |
| 8 | A value code applied to each act, capturing the participant's attitude toward a value ("intent") | `uxp2021ethicography` | Steps, step 2 | value code to each speech act | toolkit page. Values drawn a priori from `friedman2003values` (e.g. privacy, autonomy, trust, informed consent, human welfare) |
| 9 | Links between acts form the visual map; idea codes layered over the links | `uxp2021ethicography`; `goldschmidt1990linkography` | Steps, steps 3-4 | Form the links | toolkit page. Survey paper (row 14) says Linkography was the baseline framework; Goldschmidt entry to verify |
| 10 | Each decision coded as value-centered vs manipulative | `chivukula2019ethicography` | to verify | value-centered or manipulative (guess) | free copy: https://par.nsf.gov/biblio/10092725 . Seen only in a search-result summary of the full text (colour coding of designers' attitudes); the toolkit page does not mention it |
| 11 | Chronological "Design Move" numbering; process moves as the unit | `chivukula2020coevolving` | abstract | mapping process moves | free copy: https://dl.designresearchsociety.org/drs-conference-papers/drs2020/researchpapers/2 . That paper maps process moves by sequence analysis; whether the CHI paper numbers "Design Moves" is unread |
| 12 | Designers' ethical sensitivity vs "dark" persuasive intent serving stakeholders | `chivukula2018dark` | abstract | dark intentions to persuade users | metadata only: paywalled (abstract read at https://deceptive.design/articles/dark-intentions-or-persuasion-ux-designers-activation-of-stakeholder-and-user-values) |
| 13 | Persuasion-to-coercion axis | `chivukula2018dark` | to verify | persuade users (guess) | metadata only: paywalled. The abstract speaks of persuasion and dark intentions, not coercion as an axis |
| 14 | Ethicography described as a researcher-drawn value-discovery method; one of the catalogued ethics-focused methods | `chivukula2021surveying` | design-process mapping, Phase 2 | requires researchers to physically draw links | free copy: https://arxiv.org/abs/2102.08909 . Read in the ar5iv HTML rendering |
| 15 | Skill's claim that it is a compilation entry in *Universal Methods of Ethical Design* | `chivukula2025universal` | to verify | Ethicography (guess) | metadata only: book. The publisher page does not list individual methods |
| 16 | Two modes, Team Reflection and Research Documentation | `uxp2021ethicography` | Materials/Participants | An individual or a team | toolkit page: the page says participants can be an individual or a team, nothing about two named modes. Otherwise not found; searches: "Ethicography team reflection", "Ethicography facilitated" |
| 17 | 2x2 matrix Explicit/Implicit x Persuasion/Coercion with four labelled quadrants | none found | to verify | | not found in any readable source. Search terms: "Ethicography explicit implicit persuasion coercion" |
| 18 | Step 3 value families (user, designer, business, non-user, worker) and the affected-populations table | `friedman2003values` | to verify | | metadata only: book chapter. The method page lists a different a priori value set (Friedman); the skill's families and population table look like edbx additions |
| 19 | Performative Ethics Moves (hidden speech acts) | none found | to verify | | not found; looks like an edbx addition |
| 20 | Hashtags (#breakmydesign, #identifyvalues) and "See Also" (Ethical Design Scorecards, Dichotomy Mapping) | `uxp2021ethicography` | to verify | | toolkit page: the site lists Ethical Design Scorecards and Dichotomy Mapping as separate methods (https://everydayethics.uxp2.com/methods), so the See Also names exist; the page shows no hashtags |

## Licence

- `chivukula2019ethicography` (CHI 2019, ACM). The PAR page states no licence or
  rights statement. The accepted manuscript is free to read as a public-access
  copy funded by NSF; the ACM version's licence is unknown (page not readable;
  check the ACM rights line). Treat as copyrighted. Paraphrasing the method:
  yes. Reproducing text, figures or the ethicograph diagrams verbatim: no,
  without permission. Shipping a modified version of the paper: no. The method
  itself (an idea) is free to paraphrase.
- `chivukula2018dark` (DIS 2018 Companion, ACM). No licence stated on the page I
  read; unknown, check ACM. Paraphrase only.
- `chivukula2020coevolving` (DRS 2020). CC BY-NC 4.0 per the DRS Digital Library
  page. Paraphrase: yes. Verbatim reuse and adaptation are allowed only
  non-commercially, so this blocks reproducing text or figures in a paid bundle.
  Attribution required.
- `chivukula2021surveying` (arXiv 2102.08909). CC BY-NC-SA 4.0 per the arXiv
  abstract page. Non-commercial and share-alike: do not paste its text,
  tables or figures into this paid MIT repo. Paraphrase with citation is fine.
- `chivukula2025universal` (book, Rockport/Quarto). No licence stated on the
  publisher page; a commercial book, so assume all rights reserved and check
  the imprint page. Do not reproduce its method text, card or sidebar content.
  Paraphrase only.
- `uxp2021ethicography` (Everyday Ethics microsite): no licence or copyright
  notice on the page (only a theme credit); unknown. Paraphrase with citation;
  do not copy its step text verbatim.
- `friedman2003values` (book chapter): not checked; assume all rights reserved.
  The list of values is a factual list and may be named with citation.
- `goldschmidt1990linkography`: not checked; unknown.

Net: the repo may paraphrase Ethicography with citation. It may not reproduce
or ship modified copies of the CHI paper, the book, the survey or the DRS paper
inside the paid bundle. Two sources (DRS 2020, survey) forbid commercial use;
the survey is also share-alike.

## Discrepancies

Contradicted by the source (I read the source and it says otherwise):

1. Author name "Chuvaala" is wrong. The PAR record, UXP2 corpus page and
   Quarto book page give Chivukula (Shruthi Sai Chivukula).
2. "Chuvaala, Gray et al." omits the third author and misorders the credit.
   The CHI 2019 authors are Chivukula, Gray and Brier (Jason A. Brier).
3. The coding scheme. The method page describes four steps: unitize speech
   acts, apply a value code (the participant's attitude toward a value from
   Friedman's list), apply an idea code, form links. It names no 2x2 matrix, no
   explicit/implicit axis and no persuasion/coercion axis; the skill's four
   quadrants and its Step 2 are not the method as described there.
4. "Design Move number (chronological)" as the unit: the method page's unit is
   the speech act and the links between acts, not numbered moves.

Not found in a readable source (I could not read the full text, or the readable
pages say nothing):

5. The "2024" in "(2019, 2024)": no Ethicography publication from 2024 found.
   The book is listed as published 1 April 2025; the 2024 date may refer to the
   ACM JRC version of the survey paper, which only lists Ethicography.
6. The 2x2 matrix and "persuasion-to-coercion axis": the DIS 2018 abstract
   uses persuasion and dark intentions only; a search summary of the CHI paper
   mentions value-centered vs manipulative colour coding, unread.
7. The two modes, Team Reflection and Research Documentation. The survey paper
   describes Ethicography as a method where researchers draw links; a
   facilitated team mode is unsupported (the method page allows individual or
   team participants).
8. Meeting notes, crits and Slack as input: the method page names "a design
   activity or a conversation among designers"; the lab-study abstracts name
   lab protocol data. Chat logs are not mentioned.
9. The "stated reason vs implicit motivation" split per move.
10. Step 3 value categories (user, designer, business, non-user, worker values)
    and the affected-populations table; Step 3.5 Performative Ethics Moves; Step
    0 record check; Trajectory Forward 12-month projection (the skill itself
    marks the Evidence Ledger as an edbx adaptation). Treat all as edbx
    additions unless stage B finds them in the book.
11. "Most analytically rigorous method in the ethical design toolkit": no
    source ranks it; it is an opinion in SKILL.md.
12. The method's output as a "map on a persuasion-to-coercion axis": the CHI
    abstract and the method page describe a visualization of linked value
    codes, not a matrix.
13. "Uses the designer as an ethical lens" and the Mindset check: not found in
    a readable source.
