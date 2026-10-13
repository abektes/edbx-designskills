# Provenance: summary (stage B, 2026-10-13)

Every element the 21 skills attribute to a source is a row in
`edbx/*/references/provenance.md`: **465 rows**, and
`python3 scripts/check_provenance.py` reports 0 problems.

- **173 rows found** in the source text: a `p. N` or `web` locator and a
  verbatim anchor the checker matched on the page.
- **89 rows confirmed not in the source**: the source was read and the
  element is not there; the anchor is the closest passage, and the note says
  what the source says instead.
- **203 rows metadata only**: no readable copy in `papers/` (books,
  paywalled papers, 403 pages, toolkits not fetched, edbx additions).

Stage A (2026-10-13, web pages only) drafted the rows; stage B read the 33
sources in `papers/manifest.json` (16 PDFs, 17 web sources). A "not
verifiable" item is not evidence of an error; only a confirmed row is.

| Skill | Rows | Found | Not in source | Metadata only |
|---|---|---|---|---|
| anotherlens | 19 | 8 | 3 | 8 |
| anti-heroes | 28 | 20 | 3 | 5 |
| bad-design-canvas | 19 | 0 | 0 | 19 |
| black-mirror-brainstorming | 21 | 4 | 1 | 16 |
| cider | 21 | 13 | 5 | 3 |
| critical-interviewing | 27 | 6 | 4 | 17 |
| dah-cards | 13 | 0 | 0 | 13 |
| digital-ethics-compass | 18 | 7 | 6 | 5 |
| ethical-contract | 21 | 11 | 4 | 6 |
| ethicography | 27 | 14 | 6 | 7 |
| fair-patterns | 33 | 7 | 2 | 24 |
| humane-design-guide | 35 | 18 | 9 | 8 |
| inverted-behavior-model | 18 | 8 | 7 | 3 |
| motivation-matrix | 20 | 9 | 6 | 5 |
| normative-design-scheme | 19 | 9 | 7 | 3 |
| pledge-works | 19 | 10 | 7 | 2 |
| responsible-design-prism | 20 | 2 | 1 | 17 |
| stf-et | 21 | 8 | 10 | 3 |
| value-dams-and-flows | 21 | 2 | 1 | 18 |
| values-levers | 29 | 16 | 6 | 7 |
| worrystorming | 16 | 1 | 1 | 14 |

Weakest sourcing: bad-design-canvas and dah-cards (no readable source),
responsible-design-prism ("prism" is in no fetched source),
value-dams-and-flows and worrystorming (primary sources not fetched).

## Licences that matter for a paid, MIT-licensed bundle

| Skill | Source | What the text shows | Consequence |
|---|---|---|---|
| anti-heroes | Mehta et al. (arXiv 2405.03674) | arXiv listing CC BY-NC-SA 4.0; PDF p. 1 carries the ACM template notice | Non-commercial either way: paraphrase and cite, no card text |
| stf-et | Stanford Ethics Toolkit | No licence statement on the fetched page, only "© Stanford University" | The CC BY 4.0 that SKILL.md, `references/value-cards.md` and THIRD_PARTY_NOTICES state is **unconfirmed**: risk on the verbatim value cards and worksheets |
| humane-design-guide | CHT Design Guide worksheet | No licence line in the PDF | `references/six-sensitivities.md` is near-verbatim to the worksheet's definitions: **copying risk** |
| bad-design-canvas | Manos, *Less (Bad) Design* | Toolkit not readable; CC BY-ND unconfirmed | If ND holds, the skill's added layers must not be presented as the canvas |
| dah-cards | Design Against Humanity (2020) | No source readable; no licence found | Paraphrase only |
| ethical-contract, normative-design-scheme | Gispen, Ethics for Designers | "© Jet Gispen 2017", no terms | Paraphrase only |
| inverted-behavior-model, motivation-matrix | Zhou, Design Ethically | Copyright line only | Paraphrase only |
| cider | Oleson et al., TOCHI 2023 | Crossref says CC BY 4.0; both PDF copies carry only the ACM personal/classroom notice | Conflict: paraphrase and cite |
| several | Chivukula et al. survey (arXiv 2102.08909) | arXiv CC BY-NC-SA 4.0; PDF p. 1 personal/classroom notice | Cite only |
| digital-ethics-compass | Danish Design Center | CC Attribution footer (no version) confirmed | Fine with credit, which the skill never gives |
| pledge-works | ResponsibleTech.Work | CC BY-SA 4.0 confirmed in the footer | Copied text must stay share-alike, outside MIT files |

## Contradicted by the source text (fix in the skills)

Highest priority (legal or creator claims):

- **fair-patterns**: DSA Art. 25 has no named list of banned patterns; it
  applies to all online platforms, not only very large ones, and lets the
  Commission issue guidelines on three practices. The dark-pattern ontology
  page says nothing about fair patterns, so "maps directly" is unsupported.
- **Wrong creator**: inverted-behavior-model and motivation-matrix are Kat
  Zhou's (Design Ethically), not Fogg's or Zhu and Nodders';
  normative-design-scheme is Jet Gispen's (no credit given); ethicography is
  Chivukula, Gray and Brier ("Chuvaala" is wrong); cider has no "Horowitz";
  anotherlens is Airbnb Design and News Deeply's; digital-ethics-compass is
  the Danish Design Center's. value-dams-and-flows: the survey lists four
  authors including Gill and calls it a VSD paper.
- **ethical-contract**: the four-fifths rule is a US employment-selection
  rule of thumb (29 CFR 1607.4(D)), not an industry standard; the n>=30, 0.7
  and 3-click figures have no source.

Method misstated:

- **digital-ethics-compass**: "Center", not "Cosmos"; 5 principles and 22
  questions in 3 categories, not the skill's four-category ring.
- **ethical-contract**: 6 steps, not 5; needs an Ethical Disclaimer.
- **motivation-matrix**: six types (growth missing).
- **inverted-behavior-model**: predicts behaviour rather than designing for
  it; no worst-design or convergence step; the page's optional
  ability/ranking pass is missing.
- **normative-design-scheme**: the three ethical views are confirmed;
  Intention/Effect/Design and the five moves are not on the page.
- **ethicography**: no 2x2, no "coercion", no Design Move label, no team or
  research modes; input is transcribed sessions; Friedman's value list.
- **humane-design-guide**: five "Enabled to" wordings, the scale, the order
  and most listed patterns differ from the worksheet.
- **anti-heroes**: 12 Anti-Hero/Hero cards and 3 action cards, not 9 pairs;
  FOMO-Dealer missing; "Nickling-and-Diming"; Conceptualization is not an
  action card.
- **anotherlens**: "Unverified", not "Unjustified"; 16 questions in a flat
  list.
- **pledge-works**: the "because" clause is optional; the cycle is write,
  seek, review.
- **values-levers**: the 2013 article lists six levers and says the list is
  incomplete; "ENABLE" and the feedback loop are not in the text.
- **cider**: asks for ten or more redesigns, not 3-5.

## Stage A findings overturned or downgraded

- value-dams-and-flows: the "dam rule inverted" finding rested on a
  secondary summary; the primary paper is not fetched, so it is **not
  verifiable**, not confirmed.
- values-levers: Gaining Funding is a named lever (Shilton 2013 p. 19).
- digital-ethics-compass: dark-pattern material is on the DDC pages.
- humane-design-guide: infinite scroll is on the worksheet.
- black-mirror-brainstorming: the Netflix-style blurb is in Klassen and
  Fiesler (p. 2).
- stf-et: the phase-grouping finding came from image alt text; withdrawn.

## Edbx additions presented as the method

Most skills add steps the sources do not contain (pledge-works' required
fields, stress test and red-line register; inverted-behavior-model's
worst-design step; bad-design-canvas' severity scale and verdict;
black-mirror-brainstorming's lenses and counts; dah-cards' sorting and harm
categories; responsible-design-prism's scoring). Additions are fine; label
them as edbx adaptations, as the Evidence Ledger already is.
