# Provenance — edbx-value-dams-and-flows

Stage A drafted this from web pages; stage B (2026-10-13) checked every row
against the extracted text in `papers/pages/`. One row per element the skill
attributes to a source or presents as part of the method. Locator is a PDF page
(`p. N`) or `not in source`; anchor phrase is a verbatim 3–12-word pointer.
The primary texts for this method (`miller2007value`, `friedman2017survey`,
`friedman2019value`) are not in `papers/manifest.json`, so their rows are
`metadata only`. The only manifest source that mentions the method is
`chivukula2021surveying`, a survey that lists it and cites the 2007 paper but
does not describe how dams or flows are defined.

## Contents

- Sources
- Provenance table
- Licence
- Discrepancies

## Sources

| Key | Citation | DOI / URL | Legal free copy |
|---|---|---|---|
| `miller2007value` | Miller, J. K., Friedman, B., Jancke, G. (and, per some records, Gill, B. T.). 2007. Value tensions in design: the value sensitive design, development, and appropriation of a corporation's groupware system. Proc. GROUP '07, ACM, pp. 281–290. Origin of the method. | doi:10.1145/1316624.1316668 | No. Unpaywall and Semantic Scholar both report closed access. Check vsdesign.org/pubsearch (not read). |
| `friedman2017survey` | Friedman, B., Hendry, D. G., Borning, A. 2017. A Survey of Value Sensitive Design Methods. Foundations and Trends in HCI 11(2–3): 63–125. | doi:10.1561/1100000015 | No. OpenAlex reports closed. |
| `friedman2019value` | Friedman, B., Hendry, D. G. 2019. Value Sensitive Design: Shaping Technology with Moral Imagination. MIT Press. ISBN 9780262039536. | https://mitpress.mit.edu/9780262039536/value-sensitive-design/ | No (book). |
| `chivukula2025universal` | Chivukula, S. S., Gray, C. M. 2025. Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work. Rockport Publishers (Quarto). ISBN 9780760393086 (hardcover). Secondary compilation. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (book). |
| `chivukula2021surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J., Gray, C. M. Surveying a Landscape of Ethics-Focused Design Methods (arXiv:2102.08909v2). In `papers/manifest.json`; text read. Lists Value Dams and Flows as reference [112]. | https://arxiv.org/abs/2102.08909 | Yes (arXiv). Manifest licence CC BY-NC-SA 4.0; the PDF's own first page carries a different notice (see Licence). |
| `wikipedia2026vsd` | Wikipedia, "Value sensitive design". Secondary summary used only to read the method's definition, because the primary texts are closed. Not a citable source for the skill. | https://en.wikipedia.org/wiki/Value_sensitive_design | Readable web page. |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Value Dams and Flows exists as a named ethics-focused method | `chivukula2021surveying` | p. 17 | Methods using this pattern include: Value dams and flows | Found. The survey lists it under the pattern "design artifacts, evaluating, values/evaluation results" (methods that evaluate existing artifacts); it is also listed in the phase tables on p. 19 (phases 1, 2 and 4) |
| 2 | The method originates in Miller, Friedman, Jancke, Gill 2007, a Value Sensitive Design paper | `chivukula2021surveying` | p. 30 | Value tensions in design: the value sensitive design | Found. Reference [112] gives four authors (Miller, Friedman, Jancke, Gill), GROUP '07, pp. 281–290. Settles N7 (author list) and supports D5 |
| 3 | Dams and Flows named as one of the 2007 paper's contributions | `miller2007value` | abstract (OpenAlex record) | a new method called Dams and Flows | metadata only: paywalled (doi:10.1145/1316624.1316668). The record's abstract names the method as one of the paper's three contributions |
| 4 | The method is one of the VSD methods set | `friedman2017survey` | not read | value dams and flows | metadata only: paywalled. Listing as a VSD method confirmed only via `wikipedia2026vsd`, which cites `friedman2017survey` and `friedman2019value` (book) |
| 5 | Dam = design options that stakeholders object to are removed from the design space; threshold is a small share strongly objecting | `friedman2017survey` | not read | even a small percentage of stakeholders strongly object | metadata only: paywalled. Wording read only in `wikipedia2026vsd`; unverified in any primary text. See Discrepancies N1 |
| 6 | Flow = among the options left, those many stakeholders find appealing are emphasised | `friedman2017survey` | not read | those that a substantial share of stakeholders find appealing | metadata only: paywalled. Read only in `wikipedia2026vsd`. See N2 |
| 7 | Order: dams are applied first, then flows among what remains | `friedman2017survey` | not read | Of the remaining options | metadata only: paywalled. Read only in `wikipedia2026vsd`. See N3 |
| 8 | Applies to technical features and to organisational policy | `miller2007value` | abstract (OpenAlex record) | technology and organisational policy co-evolve | metadata only: paywalled. The OpenAlex abstract says technology and organisational policy co-evolve; `wikipedia2026vsd` says policy, law, organisational practice |
| 9 | Origin case: a corporate groupware system for engineers, 18 interviews, 5,965 visitors | `miller2007value` | abstract (OpenAlex record) | groupware system for sharing software engineering knowledge | metadata only: paywalled. Not used in SKILL.md; recorded as the method's origin context. The survey reference title (p. 30) also names a corporation's groupware system |
| 10 | Hard / Soft / Weak dam strength ratings | none | not read | Hard Dam non-negotiable Soft Dam negotiable with conditions | metadata only: no source found. Searched online in stage A; not in the survey text. Appears to be an edbx addition |
| 11 | Strong / Conditional / Contested flow ratings; Contested Flow minority concern and safeguard | none | not read | Strong Flow Conditional Flow Contested Flow minority opposition present | metadata only: no source found. Conflicts with the order in row 7: an option strongly opposed by any minority would already be a dam. See N1 and the survey check in row 21 |
| 12 | Conflict Intensity Score (1–5) as stakeholder strength × structural embeddedness | none | not read | Conflict Intensity Score stakeholder strength structural embeddedness | metadata only: edbx addition |
| 13 | Power Asymmetry: who can unblock a dam and at what cost | none | not read | which stakeholder has the power to unblock | metadata only: edbx addition |
| 14 | Redesign alternative, negotiation framing, "minimum viable ethics" floor, "What Would Have to Be True" for Hard Dams | none | not read | What Would Have to Be True | metadata only: edbx addition. Stage A searched "minimum viable ethics"; an unrelated 2024 AI-governance paper appears, not this concept |
| 15 | Values Balance Statement; facilitation agenda; Dam-Flow Map table layout | none | not read | Values Balance Statement Facilitation Agenda Dam-Flow Map | metadata only: edbx addition. The map table is an edbx layout; the source is described (by the secondary summary) as a two-step analytic filter |
| 16 | Names "Dam of Disagreement" and "Flow of Consensus"; "dam redirects or holds water" gloss | `chivukula2025universal` | not read | Dam of Disagreement | metadata only: book. Not found in any readable source |
| 17 | Listed as Universal Methods of Ethical Design method 92 | `chivukula2025universal` | contents, p. 192 | 92 Value Dams and Flows | metadata only: book. Entry and page confirmed on the Google Books contents page in stage A. SKILL.md does not state the number |
| 18 | Hashtags #breakmydesign #identifyvalues #alignmyteam; "explicitly a team alignment tool" | `chivukula2025universal` | not read | #breakmydesign #identifyvalues #alignmyteam | metadata only: book. Not found online |
| 19 | See Also: Maslow Mirrored, Dichotomy Mapping | `chivukula2025universal` | not read | Maslow Mirrored Dichotomy Mapping | metadata only: book. Names are other methods in the compilation; not checked |
| 20 | Overview wording: dams are features "even if not absolutely necessary for success or appropriation" | `chivukula2025universal` | not read | not absolutely necessary for success or appropriation | metadata only: book. Probably the compilation's paraphrase of the method; not found in any readable source |
| 21 | Survey text defines no dam threshold (share of stakeholders, strength of objection) and no flow tiers | `chivukula2021surveying` | not in source | Methods using this pattern include: Value dams and flows | Confirmed against the text: all three mentions (pp. 13, 17, 19) only list the method with reference [112]; the survey never defines "dam", "flow", a majority or minority share, or a Contested Flow tier. Does not confirm or refute SKILL.md's "majority" definitions |

## Licence

None of the sources has a licence that lets this repo copy its text. The method
itself (an idea) can be paraphrased freely.

- `miller2007value` — ACM copyright (Crossref: "ACM copyright policy, version
  of record"); paywalled. Paraphrase the method: yes. Reproduce text or
  figures: no. Modified version of the method: yes, if clearly marked as an
  edbx adaptation.
- `friedman2017survey` — Now Publishers, closed access; licence not stated on
  the records read (unknown; check the publisher's terms). Paraphrase: yes.
  Reproduce text: no.
- `friedman2019value` — MIT Press book; licence unknown (copyright page not
  read), assume all rights reserved. Paraphrase: yes. Reproduce text,
  diagrams or worked examples: no.
- `chivukula2025universal` — Rockport / Quarto book; the copyright page was
  not readable, so the licence is unknown (assume all rights reserved).
  Paraphrase the method idea: yes. Reproduce its entry text, wording of the
  overview, diagrams or illustrations: no. The skill's
  overview sentences resemble a compilation paraphrase (rows 16 and 20), so
  compare them against p. 192 and reword anything close.
- `chivukula2021surveying` — now a source for rows 1, 2 and 21 (anchors only,
  no text copied). The manifest records CC BY-NC-SA 4.0 (arXiv). The PDF text
  itself (p. 1) carries a different notice: permission for personal or
  classroom use without fee, not for profit or commercial advantage, with
  rights held by the owner/author(s) and "Manuscript submitted to ACM". No
  CC licence statement appears in the page text. Either way the survey is
  non-commercial, so its prose must not be copied into a paid bundle; short
  anchors and paraphrase are fine.
- `wikipedia2026vsd` — used only to read the definition; nothing reproduced.
- No source other than the survey forbids commercial use of a paraphrase.
  Rows 16 and 20: SKILL.md's overview sentences resemble a compilation
  paraphrase; compare against p. 192 of the book before shipping.

## Discrepancies

Contradicted by the source text (read on the page):

- C1. `tutorials/value-dams-and-flows.md` says the method was "developed within
  ethical design practice" and `THIRD_PARTY_NOTICES.md` credits "Values-centred
  design practice". The survey's reference [112] (p. 30) gives the method's
  origin as a Value Sensitive Design paper (Miller, Friedman, Jancke, Gill,
  2007). Both repo files should name `miller2007value`, `friedman2017survey`,
  `friedman2019value` and, if desired, `chivukula2025universal` entry 92. (fixed in SKILL.md)

Not verifiable (no readable primary text; the SKILL.md claim and the
contrary reading both rest on a secondary summary or on nothing):

- N1. Dam definition. SKILL.md says a Dam is something "the majority of
  stakeholders would like to be excluded". The only wording found
  (`wikipedia2026vsd`, citing the paywalled survey and book) says options that
  even a small percentage of stakeholders strongly object to are removed: a
  minority veto, not a majority vote. The manifest survey text does not define
  a dam (row 21), so this stays unconfirmed. The same holds for the Hard /
  Soft / Weak dam tiers (row 10). (fixed in SKILL.md)
- N2. Flow definition. SKILL.md says "the majority of stakeholders support";
  the summary says a substantial share find the option appealing. Unconfirmed. (fixed in SKILL.md)
- N3. Order and the Contested Flow tier. In the summary's order, dams go
  first and flows are chosen from what remains, so a flow with minority
  opposition could not exist. Nothing in any readable text supports a
  Contested Flow tier, a Conditional/Strong flow scale, or the safeguard step
  and guardrail built on them (row 11); treat them as edbx additions. (fixed in SKILL.md)
- N4. SKILL.md's "navigation, not elimination" and "Do not eliminate dams"
  versus the summary's statement that dam options are removed from the design
  space (rows 5, 14). Unconfirmed. (fixed in SKILL.md)
- N5. Conflict Intensity Score, Power Asymmetry, "What Would Have to Be True",
  minimum viable ethics, negotiation framing, Values Balance Statement,
  facilitation agenda, Dam-Flow Map layout (rows 12–15): edbx additions. (fixed in SKILL.md)
- N6. "Dam of Disagreement", "Flow of Consensus", the hashtags, the "See Also"
  list and the overview sentences (rows 16, 18–20): attributed in spirit to
  the compilation, whose entry text could not be read. (fixed in SKILL.md)
- N7. SKILL.md says the method "follows five steps" but lists four (Steps 1–4).
  Internal inconsistency, not a source issue. (fixed in SKILL.md)
- N8. The `tutorials/value-dams-and-flows.md` claim that the metaphor "comes
  from hydrology" has no source. (fixed in SKILL.md)

Resolved in stage B: the author list of `miller2007value` (stage-A item
N7). The survey's reference [112] lists four authors, including Brian Gill,
as Semantic Scholar does; Crossref and OpenAlex list three.
