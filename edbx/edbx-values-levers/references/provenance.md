# Provenance — edbx-values-levers

Stage A (sources and licences, no downloads). One row per element the skill
attributes to a source or presents as part of the method. Locator is a page,
section or record where the element appears; anchor phrase is a 3–12-word
pointer. Locators were confirmed only from pages read (Crossref and
Semantic Scholar records, the EUSSET and Internet Archive pages, the Google
Books contents page, an OpenAlex record). The SAGE, ACM, ResearchGate and
Springer pages returned errors or login redirects, so the article's full text
and section headings were not read. Where the full text was not readable the
Locator is `to verify` and the anchor is marked `(guess)`. Checked 2026-10-13.
Stage B must check each `to verify` row on the page.

## Sources

| Key | Citation | DOI / URL | Legal free copy |
|---|---|---|---|
| `shilton2013values` | Shilton, K. 2013 (online 2012). Values Levers: Building Ethics into Design. Science, Technology, & Human Values 38(3): 374–397. SAGE. Primary source. | doi:10.1177/0162243912436985 (verified in Crossref; two other DOIs suggested by search summaries do not resolve) | Probably yes: an author preprint is listed at https://mith.umd.edu/wp-content/uploads/2014/11/ShiltonSTHVpreprint.pdf (PDF, not fetched under the no-download rule; re-use terms not stated). The journal version is paywalled. |
| `shilton2013making` | Shilton, K., Koepfler, J. A. 2013. Making space for values: communication & values levers in a virtual team. Proc. C&T '13, ACM, pp. 110–119. | doi:10.1145/2482991.2482993; landing page https://dl.eusset.eu/handle/20.500.12015/2607 | Probably yes: the EUSSET digital library and the conference proceedings host a PDF (https://www.iisi.de/wp-content/uploads/2018/07/ct2013_proceedings_s3-4_shilton_koepfler.pdf); not fetched. |
| `shilton2013talk` | Shilton, K. 2013. "Finding Values Levers: Building Ethics into Emerging Technologies" (talk, Maryland Institute for Technology in the Humanities, 16 Apr 2013). | https://archive.org/details/dd_2013_04_16 | Yes: video, CC BY-SA 3.0 per the Internet Archive page. |
| `wong2021tactics` | Wong, R. Y. 2021. Tactics of Soft Resistance in User Experience Professionals' Values Work. Proc. ACM Hum.-Comput. Interact. (CSCW). | doi:10.1145/3479499 | Yes, bronze open access per OpenAlex (free to read; licence not stated). |
| `chivukula2025universal` | Chivukula, S. S., Gray, C. M. 2025. Universal Methods of Ethical Design. Rockport Publishers (Quarto). ISBN 9780760393086. Secondary compilation. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (book). |
| `friedman2019value` | Friedman, B., Hendry, D. G. 2019. Value Sensitive Design: Shaping Technology with Moral Imagination. MIT Press. Related background for stakeholder analysis, row 14. | https://mitpress.mit.edu/9780262039536/value-sensitive-design/ | No (book). |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Values lever = a practice that opens conversations about social values and builds consensus on them as design criteria | `shilton2013values` | abstract | open new conversations about social values | free copy: https://mith.umd.edu/wp-content/uploads/2014/11/ShiltonSTHVpreprint.pdf (abstract wording read on the talk page, `shilton2013talk`; journal page paywalled) |
| 2 | Evidence base: ethnography of a lab building mobile-phone software that tracks users' location and behaviour | `shilton2013values` | abstract | laboratory that engineered software for mobile phones | free copy: preprint URL in row 1. Wording read on `shilton2013talk` and in search summaries of the abstract |
| 3 | Leaders and advocates can strengthen levers so ethical reflection becomes routine | `shilton2013values` | abstract | lab leaders and advocates can enable | free copy: preprint URL in row 1 |
| 4 | Communication modes affect which values conversations are possible (retreats help; mediated modes limit; scenarios and demos help) | `shilton2013making` | abstract | practices which encourage discussion of values during design | free copy: https://dl.eusset.eu/handle/20.500.12015/2607 (abstract read; PDF not fetched) |
| 5 | Lever: Interdisciplinary Teams | `shilton2013values` | to verify | working across disciplinary barriers (guess) | free copy: preprint URL in row 1. Reported in search summaries of later papers (e.g. doi:10.1007/s11948-020-00250-0, not opened); the exact lever name in Shilton 2013 is unconfirmed |
| 6 | Lever: Designing Around Constraints | `shilton2013values` | to verify | designing around technical and policy constraints (guess) | free copy: preprint URL in row 1. Same status as row 5 |
| 7 | Lever: Leader / Team Member Advocacy | `shilton2013values` | abstract | lab leaders and advocates | free copy: preprint URL in row 1. The abstract supports leader and advocate roles; the skill's label is not confirmed |
| 8 | Lever: Self-Testing (technologists experience their own system) | `shilton2013values` | to verify | testing new systems on themselves (guess) | free copy: preprint URL in row 1. Same status as row 5 |
| 9 | Lever: Gaining/Funding (ethics framed as risk reduction, budget) | none found | — | — | not found. Searched: Shilton values levers funding; "gaining" lever; lever lists in secondary papers. Lists seen in search summaries instead mention team diversity |
| 10 | Five levers as a fixed list with "When to Apply" and "How to Activate" columns | `shilton2013values` | to verify | values levers (guess) | free copy: preprint URL in row 1. The levers are described as practices observed in the lab; the activation guidance is an edbx addition |
| 11 | ENABLE model: communication modes → enable → levers → enable → decisions, a feedback loop | `shilton2013making` | abstract | which communication modes support or limit values levers | free copy: https://dl.eusset.eu/handle/20.500.12015/2607. The abstract supports modes affecting levers; the name "ENABLE", the third arrow and the loop are not found |
| 12 | Lever Resistance Map (resistance points and counter-moves such as "one hour with legal", 60-minute spike, 30 minutes) | none found | — | — | not found. Appears to be an edbx addition; the figures are illustrative |
| 13 | Individual Mode (individual contributors use levers 3 and 4) | none found | — | — | not found. Appears to be an edbx addition |
| 14 | Step 2.5: whose values are served, whose are absent, systemic and second-order harm map | `friedman2019value` | to verify | direct and indirect stakeholders (guess) | metadata only: book. The absent-stakeholder idea resembles VSD stakeholder analysis, not Shilton; the three tables and four harm types are not found in either |
| 15 | Communication Audit of channels; Facilitation Guide; 30-Day Action Plan; Values-Based Design Decision Statement | none found | — | — | not found. The audit extends row 4; the other items are edbx additions |
| 16 | Soft resistance as a fallback when direct advocacy is unsafe | `wong2021tactics` | title | Tactics of Soft Resistance in User Experience Professionals' Values Work | free copy: https://dl.acm.org/doi/pdf/10.1145/3479499 (bronze open access per OpenAlex; not fetched). Separate work from Shilton; SKILL.md names "soft resistance" without a source |
| 17 | Listed as Universal Methods of Ethical Design method 96 | `chivukula2025universal` | contents, p. 200 | 96 Values Levers | metadata only: book. Entry and page confirmed on the Google Books contents page |
| 18 | Hashtags #identifyvalues #designresponsibility; See Also: Tactics on Soft Resistance, Pledge Works | `chivukula2025universal` | to verify | #identifyvalues (guess) | metadata only: book. Not found online |
| 19 | Framing: "the team culture tool", "culture change, not just individual audit" | none found | — | — | not found. Skill's own framing |

## Licence

The ideas can be paraphrased; no source here lets the repo copy its text.

- `shilton2013values` — SAGE journal article, paywalled; Crossref lists a SAGE
  text-and-data-mining licence only. The author preprint on the MITH site has
  no stated terms (unknown; check the preprint's first page). Paraphrase the
  concept: yes. Reproduce text or figures, or the article's lever
  descriptions verbatim: no. Ship a modified method: yes, labelled as an edbx
  adaptation. The five-lever table and the Resistance Map are edbx work, not
  Shilton's.
- `shilton2013making` — ACM copyright; the EUSSET page says "item-specific
  license agreed upon to submission" and the licence file was empty. Unknown.
  Paraphrase: yes. Reproduce text: no.
- `shilton2013talk` — Internet Archive lists CC BY-SA 3.0 for the talk video.
  Not reproduced here. If its wording were reused, attribution and
  share-alike would apply to that reused material.
- `wong2021tactics` — free to read, licence not stated (unknown). Paraphrase:
  yes. Reproduce: no.
- `chivukula2025universal` — copyright page not readable; licence unknown
  (assume all rights reserved). Paraphrase: yes. Reproduce entry text or
  diagrams: no. Stage B should compare SKILL.md wording against p. 200.
- `friedman2019value` — MIT Press book, unknown licence, assume all rights
  reserved. Paraphrase: yes.
- No source forbids commercial use of a paraphrase. The only non-commercial,
  share-alike source encountered (Chivukula et al. 2021 survey, CC BY-NC-SA 4.0,
  arXiv:2102.08909) is not a source here; any text added from it would
  conflict with a paid bundle.

## Discrepancies

Contradicted by the source (read the source and it says otherwise): none found.
No readable page states anything that conflicts with SKILL.md directly. The
article body was not readable, so absence of a contradiction is weak.

Not found in a readable source (the full source could not be read, or no
source contains it):

- N1. The five-lever list (rows 5–10). Secondary summaries seen in search
  results name interdisciplinary work, designing around constraints,
  self-testing, team diversity and leader advocacy. "Gaining/Funding" appears
  in none of them. Treat that lever as an edbx addition until the article is
  checked.
- N2. The ENABLE model name, its bidirectional shape and the third arrow
  (row 11). The Shilton–Koepfler abstract supports only that communication
  modes support or limit levers.
- N3. The Lever Resistance Map, its counter-moves and its figures (60 minutes,
  30 minutes, "one hour with legal prevents six months"), Individual Mode, the
  30-day plan, and the Decision Statement (rows 12, 13, 15). All illustrative
  or edbx additions.
- N4. Step 2.5 (stated vs unstated values, absent stakeholders, systemic harm
  map) is closer to VSD stakeholder analysis than to Shilton (row 14). The
  skill calls it the method's "core"; Shilton's abstract describes levers as
  practices that open conversations, not a stakeholder audit.
- N5. SKILL.md frames Values Levers as "tools" a facilitator activates. The
  abstract describes practices observed in a lab that leaders can strengthen.
  Not a contradiction, but a change of emphasis.
- N6. Soft resistance is not part of Shilton's method; it comes from separate
  work (`wong2021tactics`) and from a separate entry in the compilation.
- N7. `THIRD_PARTY_NOTICES.md` credits "Organisational behaviour and
  participatory design research" for Values Levers. The method's source is
  `shilton2013values` (and compilation entry 96). That repo line is
  inaccurate and should be replaced.
- N8. Citation hygiene: the article's DOI is 10.1177/0162243912436985; its
  online year is 2012 and its issue year is 2013. Cite as 2013 with the
  DOI; search summaries produced wrong DOIs.
