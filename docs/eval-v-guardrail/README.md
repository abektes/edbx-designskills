# Eval: after the no-asking guardrail and template fixes (2026-10-15)

Run 20261015T065929Z on 4813132 (+ rubric fixes 8c84e14): all 63 with-skill
outputs regenerated (DeepSeek V4 Pro via OpenRouter, **$1.21**); baselines
from cache. Blind pairwise judging by Claude Sonnet subagents, seven
dimensions, quote check.

## Result

- Skill preferred in **62/63** pairs (fidelity round 61/63, rubric round
  60/63), ties 0, label swaps 0.
- Every dimension gap grew (skill minus baseline; fidelity round in
  brackets): structure 0.60 (0.29) · depth 1.11 (0.87) · actionability 1.00
  (0.68) · methodology_fidelity **2.90** (2.79) · coverage 1.48 (1.21) ·
  nuance 1.05 (0.70) · evidence_honesty **1.44** (1.17).
- Question-only replies: **0/63** (2/63 before the guardrail).
- Structural conformance (with-skill): 93.8% (92.6%). black-mirror 68 ->
  95%, motivation-matrix 59 -> 86%, values-levers 80 -> 86%.
- Two checks were format-bound and failed 3/3 on outputs that did the work
  (motivation-matrix cells with the motivation in the row header;
  values-levers times in bold step headings). Fixed in 8c84e14; both still
  fail 0/3 on the baseline.

## The one loss

ethicography / social-media-growth-hacks (20 vs 21, evidence_honesty 1):
Step 0 classified a brief that lists three practices as a "record", then
claimed it held seven decisions and typed the four invented ones
`user-supplied`. Fix (not yet re-measured, ~$0.06 for the skill's three
scenarios): a list of practices is outcome only; count only the moves the
brief states; never type an inferred move `user-supplied`.
