# Provenance — edbx-ethicography

Stage B (checked against source text). Every row below either names one key
in `papers/manifest.json` and an anchor copied from the page text, or is
marked `metadata only` with the reason. Page text read: the CHI 2019 paper
(`chivukula2019ethicography`, 12 pages, read in full for the method sections,
abstract, results and discussion) and the survey paper
(`chivukula2021surveying`, pages 12, 16, 18, 19 and the reference list). The
DRS 2020 paper, the DIS 2018 abstract, the Everyday Ethics method page, the
Rockport book and Friedman and Goldschmidt are not in the manifest, so they are
not checked against text here. Locator `not in source` means the skill's
element is not in the cited source; the anchor then quotes the closest passage
and the Note says what the source actually says.

## Contents

- Sources
- Rows
- Licence
- Discrepancies

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
| 1 | The method itself: Ethicography, a method for analysing design decisions | `chivukula2019ethicography` | p. 1 | Analyzing Value Discovery in Design Decisions Through Ethicography | the paper introduces the method, which it calls a method of value discovery |
| 2 | Authorship: skill credits "Chuvaala, Gray et al." | `chivukula2019ethicography` | p. 1 | Shruthi Sai Chivukula, Colin M. Gray, and Jason A. Brier | three authors: Chivukula, Gray, Brier; see Discrepancies |
| 3 | Year: "(2019, 2024)" | `chivukula2019ethicography` | p. 1 | CHI 2019, May 4–9, 2019, Glasgow, Scotland, UK | 2019 confirmed. The paper has no 2024 edition; the survey paper's own reference list dates its draft August 2023 (arXiv v2 2022). See Discrepancies |
| 4 | Design decisions treated as data, analysed for the values shaping them | `chivukula2019ethicography` | p. 1 | identifying how values impact the designer's decision making | abstract. The data in the paper are transcribed speech acts from lab sessions |
| 5 | Method applied to UX design students in lab tasks (evidence base) | `chivukula2019ethicography` | p. 1 | design students in two lab protocol conditions | abstract; p. 3 gives eight sessions of three students each, 24 participants |
| 6 | Output identifies specific values designers considered and shows how they interact (the "ethicograph") | `chivukula2019ethicography` | p. 1 | visualizing the interplay of these values | abstract; Figure 1 on p. 5 shows one session's ethicograph |
| 7 | Speech acts (what people say in design dialogue) as the unit of analysis | `chivukula2019ethicography` | p. 4 | First, we unitized the speech acts | first of the paper's steps. Source material is the transcript of a recorded lab session (p. 4), not meeting notes |
| 8 | A value code applied to each act, capturing the participant's attitude toward a value ("intent") | `chivukula2019ethicography` | p. 4 | applied a value code to each speech act | a value code is the likely intent of the speech act, read as an attitude toward one or more values. Values adapted a priori from Friedman: ownership, privacy, accountability, freedom from bias, trust, autonomy, usability, informed consent, human welfare |
| 9 | Links between acts form the visual map; idea codes layered over the links; built on Linkography | `chivukula2019ethicography` | p. 4 | marked as the layers over the links created among the speech acts | the idea code ties an act to a problem, a solution or a decision rationale. The paper builds on critical reconstruction and linkography (p. 4); the survey, p. 18, lists Linkography as the baseline framework |
| 10 | Each decision coded as value-centered vs manipulative | `chivukula2019ethicography` | p. 4 | as being more value-centered or manipulative | the paper colour-codes each value code (the attitude in a speech act) as more value-centered or more manipulative. It is a colour layer on the ethicograph, not a two-axis placement |
| 11 | Chronological "Design Move" numbering; process moves as the unit | `chivukula2019ethicography` | not in source | identification of cognitive moves that may be resonant | the unit is the speech act. Figure 1 (p. 5) numbers speech acts along the session, but the paper never uses the label "Design Move" or "Ethical Move". "Cognitive moves" appears once, on p. 3, about lab protocols in general |
| 12 | Process-move mapping (Co-Evolving Towards Evil Design Outcomes) | `chivukula2020coevolving` | to verify | Co-Evolving Towards Evil Design Outcomes | metadata only: not in manifest, so not read at text level (DRS 2020 paper; free copy exists on the DRS Digital Library) |
| 13 | Designers' ethical sensitivity vs "dark" persuasive intent serving stakeholders | `chivukula2018dark` | abstract | dark intentions to persuade users | metadata only: paywalled (DIS 2018 Companion; abstract read in stage A at deceptive.design) |
| 14 | Persuasion-to-coercion axis | `chivukula2019ethicography` | not in source | opportunities to deepen persuasion rather than user agency | the paper discusses persuasion against user agency in its discussion (p. 9) and says nothing about coercion; the word does not occur in the paper. No axis or matrix |
| 15 | Ethicography described as a researcher-drawn value-discovery method; one of the catalogued ethics-focused methods | `chivukula2021surveying` | p. 16 | requires researchers to physically draw links that visualize | survey: mapping mechanic. It lists the method under Phase 2 (exploration, synthesis, design implications) on p. 19 |
| 16 | Skill's claim that it is a compilation entry in *Universal Methods of Ethical Design* | `chivukula2025universal` | to verify | Universal Methods of Ethical Design | metadata only: book (publisher page does not list individual methods) |
| 17 | Two modes, Team Reflection and Research Documentation | `chivukula2019ethicography` | not in source | lab, educational, and practice contexts | the paper presents one research method used on recorded lab sessions and names practice contexts only as future work (p. 10-11). No named modes and no facilitated team mode |
| 18 | 2x2 matrix Explicit/Implicit x Persuasion/Coercion with four labelled quadrants | `chivukula2019ethicography` | not in source | participants' explicit and implicit engagement with values | the paper uses explicit and implicit only about how participants engaged values (p. 3). There is no 2x2, no quadrant label and no coercion axis |
| 19 | Step 3 value families (user, designer, business, non-user, worker) and the affected-populations table | `chivukula2019ethicography` | not in source | values were adapted a priori from Friedman | the paper's value list is Friedman's (p. 4); user values that emerged in the sessions are listed on p. 5. User vs shareholder values are contrasted on p. 9. Families, worker values and the populations table are not there; they look like edbx additions |
| 20 | Performative Ethics Moves (hidden speech acts) | `edbx addition` | to verify | Performative Ethics Moves | metadata only: edbx addition (Step 3.5 of SKILL.md) |
| 21 | Step 0 check the record; Trajectory Forward 12-month projection | `edbx addition` | to verify | Trajectory Forward 12-Month Projection | metadata only: edbx addition. The paper shows value relationships over time (p. 10) but makes no forecast |
| 22 | Meeting notes, design crits and Slack as valid input | `chivukula2019ethicography` | not in source | audio of the session was transcribed and cleaned | the paper's input is audio and video of lab sessions, transcribed, with researcher memos (p. 4). Meeting notes, crits and Slack are not mentioned |
| 23 | Stated reason vs implicit motivation per move | `chivukula2019ethicography` | p. 4 | how implicit values might inform explicit design decisions | partial. Meaning reconstruction is used to see how implicit values inform explicit decisions; the paper has no per-move stated-reason and implicit-motivation fields |
| 24 | Analysis is post-hoc and longitudinal (value-laden decisions over time) | `chivukula2019ethicography` | p. 4 | value-laden decisions over time across a design process | supported. Post-hoc reflection on values inscribed in the solution is named on p. 9 |
| 25 | Ethicography is the "most analytically rigorous" method in the toolkit | `edbx addition` | to verify | most analytically rigorous method | metadata only: edbx addition. Neither paper ranks the method; the survey lists it among 63 methods (its abstract, p. 1) and ranks none of them |
| 26 | "See Also": Ethical Design Scorecards and Dichotomy Mapping | `chivukula2021surveying` | p. 19 | Dichotomy Mapping [159], Inverted Model [158] | both are separate catalogued methods in the survey (Phase 3 list); no link to Ethicography is claimed there |
| 27 | Hashtags #breakmydesign #identifyvalues | `uxp2021ethicography` | to verify | Ethicography method page hashtags | metadata only: no source found (the Everyday Ethics page, not in manifest, showed no hashtags in stage A) |

## Licence

Statements found in the PDFs are marked "in the PDF"; everything else is from
the stage A web pages or `papers/manifest.json`.

- `chivukula2019ethicography` (CHI 2019, ACM). In the PDF (p. 1): copyright
  held by the owner/author(s), publication rights licensed to ACM, with the
  standard ACM permission notice (copies for personal or classroom use are
  free; republishing or redistributing needs permission). No Creative Commons
  licence. Treat as copyrighted. Paraphrasing the method: yes. Reproducing
  text, figures or the ethicograph diagrams (Figure 1) verbatim: no, without
  permission. The method itself (an idea) is free to paraphrase.
- `chivukula2018dark` (DIS 2018 Companion, ACM). No licence stated on the page
  read in stage A; unknown, check ACM. Paraphrase only.
- `chivukula2020coevolving` (DRS 2020). CC BY-NC 4.0 per the DRS Digital Library
  page (stage A). Not in the manifest. Verbatim reuse allowed only
  non-commercially, so it blocks reproducing text or figures in a paid bundle.
- `chivukula2021surveying` (arXiv 2102.08909). The PDF text carries no licence
  line (the arXiv header and ACM reference format only); the manifest and the
  stage A arXiv abstract page give CC BY-NC-SA 4.0. Non-commercial and
  share-alike: do not paste text, tables or figures into this paid MIT repo.
  Paraphrase with citation is fine.
- `chivukula2025universal` (book, Rockport/Quarto). No licence stated on the
  publisher page; assume all rights reserved. Paraphrase only.
- `uxp2021ethicography` (Everyday Ethics microsite): no licence on the page;
  unknown. Paraphrase with citation.
- `friedman2003values`, `goldschmidt1990linkography`: not checked; assume all
  rights reserved.

Net: the repo may paraphrase Ethicography with citation. It may not reproduce
or ship modified copies of the CHI paper, the book, the survey or the DRS paper
inside the paid bundle. Two sources (DRS 2020, survey) forbid commercial use;
the survey is also share-alike.

## Discrepancies

Contradicted by the source text (read on the page):

1. Author name "Chuvaala" is wrong; the CHI 2019 paper (p. 1) gives Chivukula.
   "Chuvaala, Gray et al." also omits the third author, Brier. (fixed in SKILL.md; tutorial name corrected in this pass)
2. The coding scheme. The paper's steps (p. 4) are: unitize speech acts, apply
   a value code (colour-coded as more value-centered or manipulative), apply an
   idea code, link the acts. It has no 2x2 matrix, no explicit/implicit x
   persuasion/coercion quadrants, and the word coercion does not occur. The
   skill's Step 2 and its summary "persuasion-to-coercion axis" are not the
   method as published. (fixed in SKILL.md)
3. "Design Move number (chronological)" as the unit: the unit is the speech act
   (p. 4); the paper never uses the label Design Move or Ethical Move. (fixed in SKILL.md)
4. Input: the paper analyses transcribed audio and video of recorded lab
   sessions with 24 students (pp. 3-4). Meeting notes, design crits and Slack
   are not in the source. (fixed in SKILL.md)
5. Two modes, Team Reflection and Research Documentation: the paper describes
   one research method on lab data; practice use is future work. No facilitated
   team mode is described. (fixed in SKILL.md)
6. Step 3 value families and the affected-populations table: the paper's value
   list is Friedman's (p. 4); the skill's user, designer, business, non-user
   and worker families are not there. (fixed in SKILL.md)

Not verifiable (no readable source in the manifest):

7. The "2024" in "(2019, 2024)": no 2024 Ethicography publication appears in
   either PDF. The book is listed as published April 2025 (publisher page,
   stage A); the book is not readable.
8. Skill is an entry in *Universal Methods of Ethical Design* (book).
9. Performative Ethics Moves, Step 0 check the record, Trajectory Forward
   12-month projection and the Evidence Ledger: edbx additions (SKILL.md marks
   the ledger as one).
10. "Most analytically rigorous method in the ethical design toolkit": an
    opinion in SKILL.md; no source ranks it.
11. Hashtags #breakmydesign #identifyvalues.
12. Per-move "stated reason vs implicit motivation" fields: only partly
    supported (row 23).
