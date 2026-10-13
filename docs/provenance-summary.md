# Provenance stage A: summary (2026-10-13)

Stage A traced every element the 21 skills attribute to a source (408 rows in
`edbx/*/references/provenance.md`) to a primary source from web pages only,
without downloads, and recorded each source's licence. Stage B checks the
anchors on the actual pages once the sources are fetched. "Not found" below
often means the full text was not readable online (books, paywalls, 403
pages), not that the element is invented; only "contradicted" means a source
was read and says otherwise.

## Licences that matter for a paid, MIT-licensed bundle

| Skill | Source | Licence | Consequence |
|---|---|---|---|
| anti-heroes | Mehta, Chivukula, Gray, Gairola (arXiv 2405.03674; DIS 2025) | CC BY-NC-SA 4.0 (paper and deck) | **Blocks** selling verbatim card text; paraphrase and cite only |
| bad-design-canvas | Manos, Less (Bad) Design toolkit | CC BY-ND claimed, unconfirmed | Likely blocks a modified canvas; confirm terms |
| stf-et | Stanford Ethics Toolkit (Travaglianti & Both 2025) | Page shows only "© Stanford University"; the CC BY 4.0 stated in SKILL.md, `references/value-cards.md` and THIRD_PARTY_NOTICES is unconfirmed | **Possible block** on the verbatim value cards and four worksheet templates |
| dah-cards | ziqq rafit, Design Against Humanity (2020) | none stated: all rights reserved | Paraphrase only; no card text, manual or art |
| ethical-contract, normative-design-scheme | Jet Gispen, Ethics for Designers (2017) | "© Jet Gispen 2017", no terms | Paraphrase only; no worksheet reuse |
| humane-design-guide | Center for Humane Technology worksheet | site all rights reserved; guide terms unknown | Do not copy worksheet text |
| anotherlens | Airbnb Design + News Deeply (2017) | unknown (presume all rights) | Verbatim questions risky until terms are known |
| digital-ethics-compass | Danish Design Center (2021) | CC Attribution (site) | Fine with credit, which the skill never gives |
| pledge-works | ResponsibleTech.Work | CC BY-SA 4.0 | Commercial use allowed; copied text must stay share-alike, outside MIT files |
| cider | Oleson, Solomon, Perdriau & Ko (TOCHI 2023) | CC BY 4.0 | Fine with credit; do not copy Microsoft's Inclusive Activity Cards (reported CC BY-NC-ND) |

Several related papers are CC BY-NC or CC BY-NC-SA (DRS 2020 ethicography
paper, arXiv 2102.08909 survey, Cambridge 2025 fair-patterns article): cite,
never copy text.

## Factual errors to fix in the skills (contradicted by a source)

- **fair-patterns**: says the DSA bans a named list of dark patterns for very
  large platforms; Art. 25 says otherwise. Three fair-pattern names differ
  from the creators' names. Legal claim: highest priority.
- **value-dams-and-flows**: a dam is an option that even a small share of
  stakeholders strongly objects to, not one a majority opposes; this also
  undermines the "Contested Flow" tier (rests on a secondary summary; confirm
  on the primary page in stage B).
- **cider**: names "Horowitz" as an author; the authors are Oleson,
  Solomon, Perdriau and Ko.
- **ethicography**: author misspelt ("Chuvaala" for Chivukula); the 2×2
  matrix is not part of the published method.
- **motivation-matrix**: credits two co-authors the sources do not support;
  five motivation types where the source has six (Growth missing).
- **anti-heroes**: the paper has 12 role cards; the skill has 9 pairs and
  misses FOMO-Dealer; "Conceptualization" is not an action card.
- **digital-ethics-compass**: "Cosmos" should be "Center"; the source has 5
  principles and 3 question categories (22 questions), not the skill's
  structure.
- **ethical-contract**: the method has 6 steps, not 5, and needs an Ethical
  Disclaimer as input; the four-fifths rule is a US employment regulation,
  not an industry standard.
- **anotherlens**: "Unjustified" where the source says "Unverified".
- **responsible-design-prism**: its "Gray & McDowell (2019)" reading is
  Narayanan et al. (2020).

## Credit missing or wrong

- anotherlens credits only the book, never Airbnb Design / News Deeply.
- inverted-behavior-model and motivation-matrix come from Kat Zhou's Design
  Ethically toolkit; the skills credit only Fogg.
- digital-ethics-compass never credits the Danish Design Center.
- THIRD_PARTY_NOTICES.md gives a wrong origin for pledge-works,
  value-dams-and-flows and values-levers.
- responsible-design-prism has no traceable creator (Universal Methods #79);
  worrystorming's only confirmed source is the book's entry (#100, p. 208).

## Edbx additions presented as the method

Many skills add steps the sources do not contain (inverted-behavior-model's
Step 0, worst-design step and convergence check; normative-design-scheme's
five "signature" moves; bad-design-canvas's severity scale and verdict;
black-mirror-brainstorming's three lenses and counts; dah-cards' sorting and
six harm categories). Additions are fine; they should be labelled as edbx
adaptations, as the family does elsewhere, rather than read as the published
method.
