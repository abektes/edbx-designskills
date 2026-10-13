# Provenance — edbx-value-dams-and-flows

Stage A (sources and licences, no downloads). One row per element the skill
attributes to a source or presents as part of the method. Locator is a page,
section or record where the element appears; anchor phrase is a 3–12-word
pointer. Locators were confirmed only from pages read (publisher, Crossref,
OpenAlex, Semantic Scholar and Unpaywall records, the Google Books contents
page, and one Wikipedia article that summarises the method). Where the full
text was not readable the Locator is `to verify` and the anchor is marked
`(guess)`. Checked 2026-10-13. Stage B must check each `to verify` row on the
page.

## Sources

| Key | Citation | DOI / URL | Legal free copy |
|---|---|---|---|
| `miller2007value` | Miller, J. K., Friedman, B., Jancke, G. (and, per some records, Gill, B. T.). 2007. Value tensions in design: the value sensitive design, development, and appropriation of a corporation's groupware system. Proc. GROUP '07, ACM, pp. 281–290. Origin of the method. | doi:10.1145/1316624.1316668 | No. Unpaywall and Semantic Scholar both report closed access. Check vsdesign.org/pubsearch (not read). |
| `friedman2017survey` | Friedman, B., Hendry, D. G., Borning, A. 2017. A Survey of Value Sensitive Design Methods. Foundations and Trends in HCI 11(2–3): 63–125. | doi:10.1561/1100000015 | No. OpenAlex reports closed. |
| `friedman2019value` | Friedman, B., Hendry, D. G. 2019. Value Sensitive Design: Shaping Technology with Moral Imagination. MIT Press. ISBN 9780262039536. | https://mitpress.mit.edu/9780262039536/value-sensitive-design/ | No (book). |
| `chivukula2025universal` | Chivukula, S. S., Gray, C. M. 2025. Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work. Rockport Publishers (Quarto). ISBN 9780760393086 (hardcover). Secondary compilation. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (book). |
| `wikipedia2026vsd` | Wikipedia, "Value sensitive design". Secondary summary used only to read the method's definition, because the primary texts are closed. Not a citable source for the skill. | https://en.wikipedia.org/wiki/Value_sensitive_design | Readable web page. |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Value Dams and Flows as a named method for navigating value tensions among stakeholders | `miller2007value` | abstract (OpenAlex record) | a new method called Dams and Flows | metadata only: paywalled (doi:10.1145/1316624.1316668). The record's abstract names the method as one of the paper's three contributions |
| 2 | The method is one of the VSD methods set | `friedman2019value`; `friedman2017survey` | to verify | value dams and flows (guess) | metadata only: book. Listing as a VSD method confirmed via `wikipedia2026vsd`, which cites both |
| 3 | Dam = design options that stakeholders object to are removed from the design space | `friedman2017survey` | to verify | even a small percentage of stakeholders strongly object (guess) | metadata only: paywalled. Wording read only in `wikipedia2026vsd`. The threshold is a small share, not a majority. See Discrepancies D1 |
| 4 | Flow = among the options left, those many stakeholders find appealing are emphasised | `friedman2017survey` | to verify | those that a substantial share of stakeholders find appealing (guess) | metadata only: paywalled. Read only in `wikipedia2026vsd`. See D2 |
| 5 | Order: dams are applied first, then flows among what remains | `friedman2017survey` | to verify | Of the remaining options (guess) | metadata only: paywalled. Read only in `wikipedia2026vsd`. See D3 |
| 6 | Applies to technical features and to organisational policy | `friedman2017survey`; `miller2007value` | to verify | technology and social structures such as policy (guess) | metadata only: paywalled. `wikipedia2026vsd` says policy, law, organisational practice; OpenAlex abstract of `miller2007value` says technology and organisational policy co-evolve |
| 7 | Origin case: a corporate groupware system for engineers, 18 interviews, 5,965 visitors | `miller2007value` | abstract (OpenAlex record) | groupware system for sharing software engineering knowledge | metadata only: paywalled. Not used in SKILL.md; recorded as the method's origin context |
| 8 | Hard / Soft / Weak dam strength ratings | none found | — | — | not found. Searched: "value dams and flows" strength, hard dam, soft dam; Friedman Hendry Borning survey summaries |
| 9 | Strong / Conditional / Contested flow ratings; Contested Flow minority concern and safeguard | none found | — | — | not found. Same searches. Conflicts with the source's ordering; see D3 |
| 10 | Conflict Intensity Score (1–5) as stakeholder strength × structural embeddedness | none found | — | — | not found. Appears to be an edbx addition |
| 11 | Power Asymmetry: who can unblock a dam and at what cost | none found | — | — | not found. Appears to be an edbx addition |
| 12 | Redesign alternative, negotiation framing, "minimum viable ethics" floor, "What Would Have to Be True" for Hard Dams | none found | — | — | not found. Searched "minimum viable ethics" (an unrelated 2024 paper on AI governance appears, not this concept). Appears to be an edbx addition |
| 13 | Values Balance Statement; facilitation agenda; Dam-Flow Map table layout | none found | — | — | not found. The map table is an edbx layout; the source describes a two-step analytic filter |
| 14 | Names "Dam of Disagreement" and "Flow of Consensus"; "dam redirects or holds water" gloss | `chivukula2025universal` | to verify | Dam of Disagreement (guess) | metadata only: book. Not found in any readable source |
| 15 | Listed as Universal Methods of Ethical Design method 92 | `chivukula2025universal` | contents, p. 192 | 92 Value Dams and Flows | metadata only: book. Entry and page confirmed on the Google Books contents page. SKILL.md does not state the number; added for stage B |
| 16 | Hashtags #breakmydesign #identifyvalues #alignmyteam; "explicitly a team alignment tool" | `chivukula2025universal` | to verify | #alignmyteam (guess) | metadata only: book. Not found online |
| 17 | See Also: Maslow Mirrored, Dichotomy Mapping | `chivukula2025universal` | to verify | Maslow Mirrored (guess) | metadata only: book. Names are other methods in the compilation; not checked |
| 18 | Overview wording: dams are features "even if not absolutely necessary for success or appropriation" | `chivukula2025universal` | to verify | not absolutely necessary for success (guess) | metadata only: book. Probably the compilation's paraphrase of the method; not found in any readable source |

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
  overview sentences resemble a compilation paraphrase (rows 14 and 18), so
  stage B should compare them against p. 192 and reword anything close.
- `wikipedia2026vsd` — used only to read the definition; nothing reproduced.
- No source forbids commercial use. No source in the table is share-alike or
  non-commercial. The 2021 Chivukula et al. survey of ethics-focused design
  methods (arXiv:2102.08909) is CC BY-NC-SA 4.0 and is not a source here; if
  any of its text is later added, the NC and SA terms would conflict with a
  paid bundle.

## Discrepancies

Contradicted by a readable source. The wording of the method was read only in a
secondary summary (`wikipedia2026vsd`, which cites `friedman2017survey` and
`friedman2019value`), not in the primary text, so stage B must confirm each on
the primary page.

- D1. SKILL.md defines a Dam as something "the majority of stakeholders would
  like to be excluded". The summary of the method says options that even a
  small percentage of stakeholders strongly object to are removed. The source
  threshold is a minority veto; the skill's is a majority vote. This changes
  which items count as dams.
- D2. SKILL.md defines a Flow as supported by "the majority of stakeholders".
  The summary says options that a substantial share (many) of stakeholders
  find appealing. Looser threshold in the source; no majority rule.
- D3. In the source's order, dams are removed first and flows are chosen from
  what remains. A "Contested Flow" with minority opposition cannot exist
  under that order, because an option strongly opposed by even a small share
  is already a dam. The Contested Flow tier, its safeguard step and the
  guardrail built on it are edbx additions, not the method.
- D4. SKILL.md says the goal is "navigation, not elimination" and "Do not
  eliminate dams". In the source, dam options are removed from the design
  space. Navigation by redesign is reasonable, but it is not what the
  method says.
- D5. `tutorials/value-dams-and-flows.md` says the method was "developed within
  ethical design practice" and `THIRD_PARTY_NOTICES.md` credits "Values-centred
  design practice". The method comes from Value Sensitive Design (University
  of Washington), introduced in `miller2007value` (2007) and described in
  `friedman2017survey` and `friedman2019value`. Both repo files should name
  these sources and, if desired, `chivukula2025universal` entry 92.

Not found in a readable source (the full source could not be read, or no
source contains it):

- N1. Hard / Soft / Weak dam tiers and Strong / Conditional / Contested flow
  tiers (rows 8, 9).
- N2. Conflict Intensity Score (1–5), Power Asymmetry, "What Would Have to Be
  True", minimum viable ethics, negotiation framing (rows 10–12).
- N3. Values Balance Statement, facilitation agenda, Dam-Flow Map layout
  (row 13).
- N4. "Dam of Disagreement", "Flow of Consensus", the hashtags, the "See Also"
  list and the overview sentences (rows 14, 16–18): attributed in spirit to
  the compilation, whose entry text could not be read.
- N5. SKILL.md says the method "follows five steps" but lists four (Steps 1–4).
  Internal inconsistency, not a source issue.
- N6. The `tutorials/value-dams-and-flows.md` claim that the metaphor "comes
  from hydrology" has no source.
- N7. Author list of `miller2007value` differs by record: Crossref and OpenAlex
  list three (Miller, Friedman, Jancke); Semantic Scholar lists four (adds
  Brian T. Gill). Check the ACM page before writing the full citation. No
  SKILL.md claim depends on it.
