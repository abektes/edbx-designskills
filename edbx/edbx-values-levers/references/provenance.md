# Provenance — edbx-values-levers

Stage A drafted this from web pages; stage B (2026-10-13) checked every row
against the extracted text in `papers/pages/`. One row per element the skill
attributes to a source or presents as part of the method. Locator is a PDF page
(`p. N`, the file number in `papers/pages/<key>/`; for the Shilton preprint the
printed page number is one lower) or `not in source`; anchor phrase is a
verbatim 3–12-word pointer. Both Shilton papers are now in the manifest, so the
lever rows are checked against the text. Sources not in the manifest are
`metadata only`.

## Contents

- Sources
- Provenance table
- Licence
- Discrepancies

## Sources

| Key | Citation | DOI / URL | Legal free copy |
|---|---|---|---|
| `shilton2013values` | Shilton, K. 2013 (online 2012). Values Levers: Building Ethics into Design. Science, Technology, & Human Values 38(3): 374–397. SAGE. Primary source. In the manifest as the author preprint (text read). | doi:10.1177/0162243912436985 | Preprint at https://mith.umd.edu/wp-content/uploads/2014/11/ShiltonSTHVpreprint.pdf. Licence not stated in the text (p. 1 says only that it is a preprint of the SAGE article). |
| `shilton2013making` | Shilton, K., Koepfler, J. A. 2013. Making space for values: communication & values levers in a virtual team. Proc. C&T '13, ACM, pp. 110–119. In the manifest (text read). | doi:10.1145/2482991.2482993 | Proceedings copy; p. 1 carries an ACM notice (personal or classroom use free, not for profit or commercial advantage; other copying needs permission). |
| `wong2021tactics` | Wong, R. Y. 2021. Tactics of Soft Resistance in User Experience Professionals' Values Work. Proc. ACM Hum.-Comput. Interact. (CSCW). Not in the manifest. | doi:10.1145/3479499 | Bronze open access per OpenAlex (licence not stated). |
| `chivukula2025universal` | Chivukula, S. S., Gray, C. M. 2025. Universal Methods of Ethical Design. Rockport Publishers (Quarto). ISBN 9780760393086. Secondary compilation. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (book). |
| `friedman2019value` | Friedman, B., Hendry, D. G. 2019. Value Sensitive Design: Shaping Technology with Moral Imagination. MIT Press. Related background for stakeholder analysis. | https://mitpress.mit.edu/9780262039536/value-sensitive-design/ | No (book). |

Stage A also read the abstract on a talk page (Shilton 2013, Internet Archive,
CC BY-SA 3.0); it is no longer needed because the preprint's own abstract is
now in the manifest.

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Values lever = a practice that opens conversations about social values and builds consensus on them as design criteria | `shilton2013values` | p. 2 | practices that open new conversations about social values | Found (abstract). |
| 2 | Evidence base: ethnography of a lab (CENS) building mobile-phone software that tracks users' location and behaviour | `shilton2013values` | p. 2 | laboratory that engineered software for mobile phones | Found (abstract). A single case study; p. 24 says the conclusions will not hold for all design settings |
| 3 | Leaders and advocates can strengthen levers so ethical reflection becomes routine | `shilton2013values` | p. 2 | Laboratory leaders and advocates can enable and strengthen | Found (abstract) |
| 4 | Communication modes affect which values conversations are possible (retreats help; mediated modes limit) | `shilton2013making` | p. 1 | mediated modes of communication tend to constrain values levers | Found (abstract). Face-to-face retreats are said to encourage interdisciplinary work and discussion of moral values |
| 5 | Scenarios and demos as communication techniques that help in both modes | `shilton2013making` | p. 1 | communications techniques such as scenarios and demos | Found (abstract) |
| 6 | Lever: Interdisciplinary Teams | `shilton2013values` | p. 11 | Working on interdisciplinary teams was another design practice | Found. Also listed as the first lever in `shilton2013making` p. 3. In the source it works by turning attention to shared data, not by bringing in ethicists or legal |
| 7 | Lever: Designing Around Constraints | `shilton2013values` | p. 13 | Designing around values-based constraints helped make social values interesting | Found. In the source, privacy constraints were seen as creative challenges; the "design as if you can't use this data" exercise is not in the text (row 24) |
| 8 | Lever: Leader / Team Member Advocacy | `shilton2013making` | p. 3 | Internalizing leader and team member advocacy | Found, and the label matches. In `shilton2013values` these are two separate levers (leader advocacy p. 14; team member advocacy p. 18, the researcher's own role). The article also reports students largely denied their mentors' influence (p. 15), a caveat the skill omits |
| 9 | Lever: Self-Testing (technologists experience their own system) | `shilton2013making` | p. 3 | Experiencing self-testing: when technologists used their own systems | Found. Named "experiencing internal prototype testing" in `shilton2013values` p. 9. In the source technologists tested their own and colleagues' systems and saw their own location data; "as a non-expert or vulnerable user" is not in the text (row 25) |
| 10 | Lever: Gaining/Funding as a lever | `shilton2013values` | p. 19 | Resources and funding also encouraged practices that fostered attention to values | Found. Overturns stage-A N1 ("Gaining/Funding appears in none"): it is a named lever in both papers (`shilton2013making` p. 3, "Gaining funding"). Meaning differs from the skill; see row 23 |
| 11 | The five levers as a fixed list | `shilton2013making` | p. 3 | Values levers discovered in the first author's previous study | Found. Shilton and Koepfler list exactly these five (interdisciplinary teams, gaining funding, self-testing, leader and team member advocacy, designing around constraints). The 2013 article's conclusion (p. 25) lists six, adding navigating institutional mandates, and p. 24 calls its list incomplete (row 12) |
| 12 | Skill's list omits navigating institutional mandates and presents five as complete | `shilton2013values` | p. 24 | likely an incomplete list of values levers | Confirmed against the text. The source's institutional-mandates lever (IRB, procedural form) is dropped, and the source says the list is not exhaustive. See Discrepancies C1 |
| 13 | ENABLE model: communication modes enable levers, levers enable decisions | `shilton2013making` | p. 3 | Modes of communication can enable or constrain values levers | Found for the two links, each "enable or constrain", illustrated in a Figure 1 whose image text was not extracted. The name "ENABLE" is not in the text (row 14) |
| 14 | ENABLE as a feedback loop: decisions shape which communication modes are used next | `shilton2013making` | not in source | values levers in turn enable or constrain values-based design | Confirmed against the text: the passage gives a chain from modes to levers to design, not a return link from decisions to modes. Figure 1 could not be read as text, so a loop drawn in the figure is unchecked. See Discrepancies C2 |
| 15 | "When to Apply" and "How to Activate" columns for each lever | `shilton2013values` | not in source | this case study suggests concrete activities to examine | Confirmed against the text: levers are observed practices to look for (p. 24), not a menu of activation recipes. Activation guidance is an edbx addition |
| 16 | Lever Resistance Map (resistance points and counter-moves such as "one hour with legal", 60-minute spike, 30 minutes) | none | not read | Lever Resistance Map counter-move per lever | metadata only: edbx addition. Figures are illustrative; stage A found no source |
| 17 | Individual Mode (individual contributors use levers 3 and 4) | none | not read | Individual Mode activates a fast path | metadata only: edbx addition |
| 18 | Step 2.5 core: whose values are served, whose are absent | `shilton2013making` | p. 2 | what, and whose, values are embodied in software | Found only as background framing: the paper says questions of what and whose values a system embodies have long been controversial. The three tables and four harm types are not in either Shilton paper |
| 19 | Step 2.5 tables (stated vs unstated values, absent stakeholders, systemic / second-order harm map) | `friedman2019value` | not read | direct and indirect stakeholders | metadata only: book. Resembles VSD stakeholder analysis, not Shilton; no source found for the tables |
| 20 | Step 2.5 described as the method's "core", a values-surfacing methodology rather than a tactical influence toolkit | `shilton2013values` | not in source | practices that open new conversations about social values | Confirmed against the text: the article defines levers as practices that open conversations, and p. 25 recommends articulating and amplifying them. It does not describe a stakeholder audit. See Discrepancies C3 |
| 21 | Communication Audit of channels | `shilton2013making` | p. 4 | Table 1: Coding scheme for communication modes | Found as a basis only: the paper codes modes as face-to-face, mediated and spanning. The audit table (values reinforced, space for ethics, recommendation) is an edbx extension |
| 22 | Facilitation Guide; 30-Day Action Plan; Values-Based Design Decision Statement | none | not read | Values-Based Design Decision Statement | metadata only: edbx addition |
| 23 | Gaining/Funding activation: frame ethics investment as risk reduction, find budget or headcount | `shilton2013values` | not in source | Funding greatly affected the trajectory of projects | Confirmed against the text: funding mattered because it paid for larger teams, formal weekly meetings, leaders in the room and a long-term ethics advocate (pp. 19, 22); the source never says to frame ethics as risk reduction |
| 24 | Designing Around Constraints activation: impose a constraint such as "design as if you can't use this data" | `shilton2013values` | not in source | Unconstrained design is often boring | Confirmed against the text: the constraint was an existing commitment to privacy that leaders and the director framed as a creative challenge (p. 13); no exercise of imposing a constraint on a team is described |
| 25 | Self-Testing activation: experience the system "as a non-expert or vulnerable user" | `shilton2013values` | not in source | made the surveillance concerns concrete in a way | Confirmed against the text: students saw their own and colleagues' data during internal testing (p. 10); no vulnerable-user role-play is described |
| 26 | Soft resistance as a fallback when direct advocacy is unsafe | `wong2021tactics` | title | Tactics of Soft Resistance in User Experience Professionals' Values Work | metadata only: no source in manifest (open-access paper, not fetched). Separate work from Shilton; SKILL.md names "soft resistance" without a source |
| 27 | Listed as Universal Methods of Ethical Design method 96 | `chivukula2025universal` | contents, p. 200 | 96 Values Levers | metadata only: book. Entry and page confirmed on the Google Books contents page in stage A |
| 28 | Hashtags #identifyvalues #designresponsibility; See Also: Tactics on Soft Resistance, Pledge Works | `chivukula2025universal` | not read | #identifyvalues #designresponsibility Tactics on Soft Resistance | metadata only: book. Not found online |
| 29 | Framing: "the team culture tool", team and organisational layer | `shilton2013values` | p. 25 | pay attention to the structure of design labs | Found as partial support: the article argues for attending to lab structure and practices rather than only education or outside experts. "Culture change, not just individual audit" is the skill's own framing |

## Licence

The ideas can be paraphrased; no source here lets the repo copy its text.

- `shilton2013values` — SAGE journal article; the manifest copy is the author
  preprint, whose text states no licence (p. 1 only says it is a preprint of
  the SAGE article). Treat as all rights reserved. Paraphrase the concept:
  yes. Reproduce text or figures, or the lever descriptions verbatim: no. Ship
  a modified method: yes, labelled as an edbx adaptation. The Resistance Map,
  Step 2.5, the Communication Audit, the 30-day plan and the activation guidance
  are edbx work, not Shilton's.
- `shilton2013making` — ACM copyright. The PDF's own p. 1 notice allows copies
  for personal or classroom use only if not made or distributed for profit or
  commercial advantage, and requires permission to republish. Paraphrase: yes.
  Reproduce text: no.
- `wong2021tactics` — free to read, licence not stated (unknown). Paraphrase:
  yes. Reproduce: no.
- `chivukula2025universal` — copyright page not readable; licence unknown
  (assume all rights reserved). Paraphrase: yes. Reproduce entry text or
  diagrams: no. Compare SKILL.md wording against p. 200 of the book.
- `friedman2019value` — MIT Press book, unknown licence, assume all rights
  reserved. Paraphrase: yes.
- No source forbids commercial use of a paraphrase. The only non-commercial,
  share-alike source encountered (Chivukula et al. 2021 survey,
  arXiv:2102.08909) is not a source here; any text added from it would
  conflict with a paid bundle.

## Discrepancies

Contradicted by the source text (read on the page):

- C1. The five-lever list. SKILL.md presents five levers as the method. The
  Shilton and Koepfler paper (p. 3) does list these five, but the 2013 article
  (p. 25) lists six, including navigating institutional mandates, and says its
  list is probably incomplete (p. 24). The skill omits the sixth lever and does
  not say the list is open. (fixed in SKILL.md)
- C2. The ENABLE feedback loop. The text gives modes enabling or constraining
  levers, and levers enabling or constraining values-based design (p. 3). It
  does not say decisions determine which communication modes are used next, and
  the name "ENABLE" does not appear. The loop may be drawn in Figure 1, whose
  image was not read. (fixed in SKILL.md)
- C3. Step 2.5 as the method's "core". The article defines levers as practices
  that open conversations (p. 2); the stakeholder and harm tables are not in
  either paper. SKILL.md also says the Gaining/Funding lever is about framing
  ethics as risk reduction and the Self-Testing lever about experiencing the
  system as a vulnerable user; the text says otherwise (funding paid for larger
  teams and a long-term ethics advocate, pp. 19, 22; self-testing meant seeing
  one's own and colleagues' data, p. 10). (fixed in SKILL.md)
- C4. Meaning of "Interdisciplinary Teams" activation. The skill says to bring
  in engineers, ethicists, legal and community reps. In the source the lever
  worked by adding statisticians, social scientists and designers whose
  questions pulled attention to the data (p. 11), not by adding legal or
  community members. (fixed in SKILL.md)
- C5. `THIRD_PARTY_NOTICES.md` credits "Organisational behaviour and
  participatory design research" for Values Levers. The method's source is
  `shilton2013values` (with `shilton2013making` for the communication-mode
  link, and compilation entry 96). That repo line is inaccurate and should be
  replaced.

Overturned from stage A: N1 said the Gaining/Funding lever appears in no
readable source. It is a named lever in `shilton2013values` (p. 19) and
`shilton2013making` (p. 3). Self-Testing, Designing Around Constraints,
Interdisciplinary Teams and Leader/Team Member Advocacy are also confirmed as
named levers.

Not verifiable (no readable source):

- N1. Lever Resistance Map, its counter-moves and figures (60 minutes, 30
  minutes, "one hour with legal prevents six months"), Individual Mode, the
  30-day plan, the Decision Statement, the Facilitation Guide (rows 16, 17,
  22): edbx additions, illustrative.
- N2. Step 2.5 tables and harm types (row 19): no source found; closest is VSD
  stakeholder analysis (book not readable).
- N3. Soft resistance (row 26) comes from separate work (`wong2021tactics`)
  and a separate compilation entry; not in the manifest.
- N4. Hashtags, See Also list and entry text of compilation entry 96 (rows 27,
  28): book.
- N5. Citation hygiene: the article's DOI is 10.1177/0162243912436985; its
  online year is 2012 and its issue year is 2013. Cite as 2013 with the DOI.
  The preprint's p. 1 says "to appear ... 2012".
