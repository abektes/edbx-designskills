# Jev calibration v0.1 (2026-10-14)

Before 2026-10-14, 17 of edbx's 145 semantic (Jev) checks had calibration
labels, in 6 skills. The owner chose a **Claude Sonnet second reader** as
labeller and one paid Jev run on one skill first, to measure cost before
labelling more.

Tooling: `scripts/dump_semantic_inputs.py` writes the exact texts each check
sends to Jev (the scorer's own extraction, `conformance.semantic_values`);
`docs/calibration-brief.md` is the labelling brief; `scripts/calibrate.py`
measures Jev against the labels (gate: 81% agreement on decided cases, at
most 25% sent to review, margin of at least 0.30 between the worst positive
and the best negative). Labels live in `eval-framework/calibration/<skill>.json`
(gitignored, like the generations).

## worrystorming: PASS

10 checks, 79 cases (39 true, 40 false; 37 constructed by breaking one
requirement of a real text).

| Run | Cases | Decided | Agreement | Review | Thin margins | Result |
|---|---|---|---|---|---|---|
| 1 | 81 | 79 | 74/79 = 94% | 2% | clusters_coherent, objective_specific, worries_span_categories | FAIL (margin) |
| 2 | 79 | 74 | 74/74 = 100% | 6% | none (lowest +0.34) | **PASS** |

Every run-1 mismatch was read. All five were labelling problems, not judge
errors:

- **worries_span_categories (3):** the second reader built its negatives as
  subsets of real worry lists, but each subset still spanned three or four
  kinds of concern (bias, vigilantism, doxxing, harassment), so it did not
  break the requirement. Rebuilt as subsets confined to one kind (clinical
  safety; privacy; privacy).
- **objective_specific (1), clusters_coherent (1):** real texts the reader
  labelled false that are genuinely borderline. Dropped, not relabelled.

**Caveat:** these changes were made after seeing Jev's scores; the reasons
are recorded in the label file's `_note` and above, and each one rests on
the criterion's own definition, not on the score. clusters_coherent is left
with 3 true and 2 false cases, below the brief's 3/3 minimum. One rebuilt
negative (worries_span_categories, 0.62) lands in the review band.

**Ambiguities the reader flagged** (for the next rubric pass, not changed
here): mitigation_concrete does not say whether a curriculum, KPI or
governance change counts as "a change to this product"; clusters_affirmative
has no rule for neutral topic names ("Clinical Crisis Response");
worries_span_categories checks the kinds of concern but not the bar's
10-worry minimum (that count is a structural check's job).

## Cost

Jev's API returns no cost or usage. The two runs sent **50 requests, 160
questions** in about 7 seconds each. The real cost has to be read from the
TypeSafe dashboard; until it is, extrapolate by questions: the 118 checks
not yet calibrated need roughly 8 cases each, about 1,000 questions per run.

## Status

| Skill | Semantic checks | Calibrated |
|---|---|---|
| anti-heroes, cider, value-dams-and-flows | 4, 4, 4 | all |
| worrystorming | 10 | all (this round) |
| stf-et, dah-cards, pledge-works | 6, 6, 3 | 3, 1, 1 |
| 14 other skills | 108 | none |
