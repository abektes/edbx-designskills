# Provenance — edbx-critical-interviewing

Stage B (checked against the text in `papers/pages/`, 2026-10-13). One row per
element the skill attributes to a source. Rows whose source is in
`papers/manifest.json` carry a page locator (or `web`) and a verbatim anchor,
or `not in source` where the text was read and the element is absent. Other
rows are `metadata only`, with the reason. The extracted text drops some
ligatures in other PDFs; anchors here are copied as extracted.

**Main finding:** the skill's primary source is Carspecken (1996), a book that
is not in the manifest. Two readable papers confirm that the Gray / Chivukula
group followed a "critical interview approach" citing Carspecken: Chivukula et
al. (2020) p. 3 and ref. [8] p. 11, and Gray & Chivukula (2019) cite
Carspecken as ref. [9] for field-note practice. Of the skill's protocol terms,
only "lead-off questions" appears in the papers (p. 3 of Chivukula et al.). The
back-up question, emergency question, covert categories, construct-building
probes and the four example covert categories appear in no text read.

## Sources

| Key | Citation | Stable link | Legal free copy | Licence |
|-----|----------|-------------|-----------------|---------|
| `carspecken1996critical` | Carspecken, P. F. (1996). *Critical Ethnography in Educational Research: A Theoretical and Practical Guide*. New York: Routledge. (Ebook reissue doi:10.4324/9781315021263, 2013.) | https://www.routledge.com/products/9780415904933 | No legal free copy found. A PDF is hosted on a society site (cae.americananthro.org); its permission is unknown, so I do not list it as a free copy | unknown; commercial book, no open licence found |
| `dennis2013qualitative` | Dennis, B., Carspecken, L. & Carspecken, P. F. (eds.) (2013). *Qualitative Research: A Reader in Philosophy, Core Concepts, and Practice*. New York: Peter Lang. | not looked up | No | unknown |
| `gray2016meaning` | Gray, C. M., Toombs, A. L. & McKay, C. (2016). Meaning reconstruction as an approach to analyze critical dimensions of HCI research. *CHI '16 Extended Abstracts*. | doi:10.1145/2851581.2892571 | not confirmed | ACM copyright policy |
| `chivukula2020dimensions` | Chivukula, S. S., Watkins, C. R., Manocha, R., Chen, J. & Gray, C. M. (2020). Dimensions of UX practice that shape ethical awareness. *Proc. CHI 2020*, 1–13. | doi:10.1145/3313831.3376459 | Yes: accepted manuscript at https://par.nsf.gov/biblio/10168355 ; author copy https://colingray.me/wp-content/uploads/2020/01/2020_Chivukulaetal_CHI_DimensionsThatShapeEthicalAwareness.pdf | PDF p. 1: ACM notice, personal or classroom use free, not for profit; other reuse needs permission (see Licence) |
| `gray2019ethical` | Gray, C. M. & Chivukula, S. S. (2019). Ethical mediation in UX practice. *Proc. CHI 2019*, 1–11. | doi:10.1145/3290605.3300408 | Yes: https://par.nsf.gov/biblio/10092726 | PDF p. 1: copyright held by the authors, publication rights licensed to ACM; same personal or classroom use notice (see Licence) |
| `chivukula2021identity` | Chivukula, S. S., Hasib, A., Li, Z., Chen, J. & Gray, C. M. (2021). Identity claims that underlie ethical awareness and action. *Proc. CHI 2021*. | doi:10.1145/3411764.3445375 | not checked | ACM copyright policy |
| `davoudi2025review` | Davoudi, N., Dehghan Nayeri, N., Zokaei, M. S., Fazeli, N. & Carspecken, P. F. (2025). A review on Carspecken's critical ethnography. *Qualitative Health Research*. | doi:10.1177/10497323251325472 | not confirmed (SAGE page returned 403) | unknown |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design*. Rockport Publishers, ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (commercial book) | unknown |
| `ecfr2024adverse` | 29 C.F.R. § 1607.4(D) (Uniform Guidelines on Employee Selection Procedures: adverse impact and the "four-fifths rule"). | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607/section-1607.4 | Yes (US federal regulation) | US federal regulation; no licence text on the fetched page (see Licence) |

## Table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Method "developed from Carspecken's (1996) critical ethnography framework" | `carspecken1996critical` | title | Critical Ethnography in Educational Research | metadata only: book (Routledge table of contents read in stage A). The papers confirm the group cites it: rows 12–13 |
| 2 | Interview-based data generation as one stage of the framework | `carspecken1996critical` | Ch. 10 | Dialogical Data Generation through Interviews | metadata only: book. Ch. 11 covers validity requirements for that stage |
| 3 | Focus on normative-evaluative claims alongside subjective and objective claims | `carspecken1996critical` | title | Critical Ethnography in Educational Research | metadata only: book. Three claim types (subjective, objective, normative-evaluative) are described in secondary reviews such as `davoudi2025review` (paywalled, not read) |
| 4 | "Borrows principles from semistructured interviewing"; protocol organised by "topic domains" | `chivukula2020dimensions` | not in source | collecting data through semistructured interviews with UX practitioners | Semistructured interviews are found (p. 3). "Topic domains" does not appear in the paper. Likely from the Carspecken book (unreadable) |
| 5 | Lead-off question (open, narrative, does not embed the construct) | `chivukula2020dimensions` | p. 3 | Examples of lead-off questions that prompted these ethical | The paper uses the term and gives two examples, one asking about an experience that made the practitioner uncomfortable. It does not define the lead-off question |
| 6 | Back-up question | `dennis2013qualitative` | — | Qualitative Research: A Reader in Philosophy, Core Concepts, and Practice | metadata only: book. Attribution to this reader is a stage A lead, not confirmed; the term is in no text read |
| 7 | Emergency question redirecting an observer-narrator to their own agency | `none found` | — | narrates as an observer or user rather than a practitioner | metadata only: no source found. Terms tried: emergency question, critical interview emergency, back-up question across all page text |
| 8 | Follow-up bank: descriptive, normative, evaluative probes | `carspecken1996critical` | title | Critical Ethnography in Educational Research | metadata only: book |
| 9 | Construct-building probes: mirror the participant's own value word | `carspecken1996critical` | title | Critical Ethnography in Educational Research | metadata only: book. Not in the papers (row 10) |
| 10 | Same construct-building technique, checked against the group's protocol description | `chivukula2020dimensions` | not in source | focusing on the asking why questions rather than direct questions | The paper describes asking "why" questions and probing, without any mirroring or construct-building step |
| 11 | Covert categories phrased "I want to understand X without asking Y" | `dennis2013qualitative` | — | Qualitative Research: A Reader in Philosophy, Core Concepts, and Practice | metadata only: book. Term appears in no text read |
| 12 | Covert-category idea checked against the paper's protocol | `chivukula2020dimensions` | not in source | although these terms were not generally used in the questions being asked | Closest passage: the paper says ethics and values lenses guided the probing though those words were not used in questions. No list of categories |
| 13 | The four example covert categories "from the source" (role of ethics in design, awareness of ethical role, drivers of ethical sensitivity, personal design values) | `chivukula2020dimensions` | not in source | Positionality of UX in the Enterprise | Not there. The paper reports five dimensions (Table 3, p. 9): Positionality of UX in the Enterprise, Conflicts and Balancing in Decision Making, Identified Design Activities/Practices, Self and Stakeholder Education, Futuring. None matches the four |
| 14 | Adaptation to design research: "why" questions and no a-priori definition of ethics | `chivukula2020dimensions` | p. 3 | no a priori framing or definition of ethics and values | Method section: the protocol followed a critical interview approach cited to Carspecken. 11 UX practitioners, semistructured interviews |
| 15 | Carspecken (1996) as the cited basis | `chivukula2020dimensions` | p. 11 | Critical ethnography in educational research: A theoretical and practical guide | Reference [8], cited as the basis of the critical interview approach (p. 3). Stage A's Crossref-based claim of no Carspecken entry is overturned |
| 16 | Earlier HCI use of Carspecken-style meaning reconstruction | `gray2016meaning` | — | Meaning reconstruction as an approach to analyze critical dimensions of HCI research | metadata only: paywalled |
| 17 | Same group's interviews with UX practitioners (context for the "designer values" use) | `gray2019ethical` | p. 4 | to constitute a thick record | Carspecken is cited as ref. [9] (p. 4, listed p. 10) for field-note practice (paralinguistics, thick record) in observation, not for critical interviewing. The follow-up interviews are stimulated-recall debriefs. Stage A's Crossref-based claim of no Carspecken entry is overturned |
| 18 | Same group's later interview study (identity claims) | `chivukula2021identity` | — | Identity claims that underlie ethical awareness and action | metadata only: paywalled |
| 19 | Mode 2 live interview support (flag value words, suggest mirrored probes) | `none found` | — | Flag the word as a construct-building opportunity | metadata only: no source found |
| 20 | Mode 3 post-interview analysis (value constructs, covert-category mapping, descriptive vs normative findings, values portrait) | `carspecken1996critical` | Ch. 9 | Coding Procedures Congruent with Reconstructive Analysis | metadata only: book. Closest chapter title; the skill's specific outputs are not confirmed |
| 21 | Domain-specific question bank (algorithmic, data, labor, product, policy) | `edbx addition` | — | Domain-Specific Question Bank | metadata only: edbx addition |
| 22 | Sequencing rule (impacted users before engineers before executives; frontline before policy owners) | `none found` | — | Interview impacted users before engineers | metadata only: no source found |
| 23 | Non-Obvious Harms Inventory, Pre-Interview Design Guardrails, Red-Flag/Halt Checklist | `edbx addition` | — | Non-Obvious Harms Inventory | metadata only: edbx addition (the skill itself says it is not a substitute for IRB or ethics review) |
| 24 | "4/5 / 80% rule under Title VII" | `ecfr2024adverse` | web | Adverse impact and the four-fifths rule | 29 C.F.R. § 1607.4(D). The text says a rate under four-fifths is generally regarded as evidence of adverse impact, and smaller differences can still be adverse impact. It sits in the Uniform Guidelines on Employee Selection Procedures, not in a statute; the authority line cites the Civil Rights Act of 1964 and the section does not say "Title VII" |
| 25 | GDPR Art. 22 as proxy-variable disparate-impact law | `eu2016gdpr` | web | Automated individual decision-making, including profiling | The fetched page is the article index only, so the scope of Art. 22 cannot be read. The title shows it concerns automated decision-making and profiling, not disparate impact by proxy variables |
| 26 | EU AI Act Arts. 5 and 6 as proxy-variable disparate-impact law | `none found` | — | EU GDPR Art. 22 EU AI Act Art. 5/6 | metadata only: no source found. The AI Act text is not in the manifest; the fetched EU pages only link to it |
| 27 | Book hashtags and "See Also" (Culture Co-Creation Cards, Normative Design Scheme) | `chivukula2025universal` | entry 13 | Universal Methods of Ethical Design | metadata only: book. Entry no. 13 in the book's method list |

## Licence

- **`carspecken1996critical`.** Commercial book, no open licence found.
  Paraphrasing the framework (yes). Reproducing text, chapter material or
  figures verbatim: no. Shipping a modified method (the skill's protocol) is
  fine as our own adaptation with credit. Do not link the society-hosted PDF
  as a free copy until its permission is established.
- **`dennis2013qualitative`.** Commercial book; paraphrase only. Not yet
  looked up.
- **`chivukula2020dimensions`.** Confirmed in the PDF (p. 1): copying for
  personal or classroom use is free if not for profit or commercial advantage;
  to republish or redistribute requires permission and/or a fee; © 2020
  Association for Computing Machinery. No open licence. Paraphrase and cite;
  do not reproduce text or tables.
- **`gray2019ethical`.** Confirmed in the PDF (p. 1): copyright held by the
  owner/author(s), publication rights licensed to ACM, with the same personal or
  classroom use notice. No open licence. Paraphrase and cite.
- **`gray2016meaning`, `chivukula2021identity`.** ACM copyright policy;
  not read. Cite only.
- **`davoudi2025review`.** unknown. Check SAGE access and licence before using
  anything beyond a citation.
- **`chivukula2025universal`.** Commercial book; paraphrase only.
- **`ecfr2024adverse`.** US federal regulation. The fetched page states no
  licence; federal regulations are not ordinarily subject to copyright, but
  that is general knowledge, not read on the page.
- **`eu2016gdpr`.** EU legislation; the fetched page is an index and states no
  licence.
- Nothing found forbids commercial use or modification of the method as
  paraphrased. The licence risk is only verbatim reuse of book text.

## Discrepancies

### Contradicted by the source text

1. **Four example covert categories "from the source".** The only readable
   source that describes this research use (Chivukula et al. 2020) reports five
   different dimensions (p. 9) and no covert-category list (rows 12, 13).
2. **Protocol terms attributed to the method.** The back-up question,
   emergency question, covert categories and construct-building probes appear
   in no text read. The papers that cite Carspecken describe asking "why"
   questions, with no a-priori framing, and give lead-off examples (p. 3); that
   is all. Whether the book supplies the rest is unconfirmed.
3. **Legal framing, four-fifths rule.** 29 C.F.R. § 1607.4(D) says a rate
   under four-fifths generally counts as evidence of adverse impact, and that
   smaller differences can too; it governs employee selection procedures and does
   not name Title VII in that section (row 22). SKILL.md's "4/5 / 80% rule under
   Title VII" applied to proxy variables in any ranking or matching system
   overreaches the text.
4. **GDPR Art. 22.** The page read (an index) shows only that Art. 22 is about
   automated individual decision-making and profiling (row 23); it gives no
   support for treating it as proxy-variable disparate-impact law.
5. **Stage A's "no Carspecken reference" finding was wrong.** Chivukula et al.
   2020 cite Carspecken as ref. [8] (pp. 3, 11) and Gray & Chivukula 2019 as
   ref. [9] (pp. 4, 10). The earlier note that one search summary conflicted with
   Crossref is resolved in favour of the search summary. Gray & Chivukula use it
   for field notes, not for a critical interview protocol.

### Not verifiable

6. **Method name and adapters.** "Critical Interviewing" as a named design
   method and who adapted it (SKILL.md names none) cannot be traced; the
   Chivukula / Gray group used a "critical interview approach" (p. 3) without
   naming a method called that.
7. **Internal inconsistency (no source involved).** "Critical Interviewing
   operates in five modes" but three modes are listed; Mode 1 lettered A to J
   while the Output Format shows only A to E components.
8. **Sections F to J** (domain bank, sequencing, harms inventory, guardrails,
   halt checklist) and the "minimum output" list have no source (rows 19–21);
   treat as edbx additions. The sequencing rule is stated as fact.
9. **EU AI Act Arts. 5 and 6** named without text; the AI Act is not in the
   manifest (row 24).
10. **No citation list in SKILL.md.** The only source named is "Carspecken
    (1996)" with no title, publisher or the design-research adapters.
11. **Related-skills line** ("values interview", "designer values research") is
    trigger wording, not a source claim.
