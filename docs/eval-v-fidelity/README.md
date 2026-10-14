# Eval: after the source-fidelity pass (2026-10-14)

Run 20261014T150536Z on 3644725: all 63 with-skill outputs regenerated
(DeepSeek V4 Pro via OpenRouter, $0.90); baselines from cache, except
motivation-matrix / corporate-wellness-app, whose prompt now names six
motivations (both arms saw the new prompt; $0.003). Blind pairwise judging by
Claude Sonnet subagents, seven dimensions, quote check.

## Result

- Skill preferred in **61/63** pairs (previous round 60/63), ties 0, label
  swaps 0.
- Dimension gap (skill minus baseline), all 63 / excluding the two
  question-only outputs: structure 0.29/0.34 · depth 0.87/1.00 ·
  actionability 0.68/0.82 · methodology_fidelity **2.79/2.97** (was 2.67) ·
  coverage 1.21/1.33 · nuance 0.70/0.79 · evidence_honesty 1.17/1.16.
- Structural conformance (with-skill): 92.6% new vs 92.8% for the old
  outputs on the same rubrics; baseline 4%.

## Losses: two outputs asked questions instead of answering

black-mirror-brainstorming / ai-hiring-screening and motivation-matrix /
employee-review-platform stopped to ask for details (2/63 this round vs 2/630
before). Fix: the family guardrail "Do not stop to
ask for more: draft the full output with unknowns marked and the questions
to ask" in all 21 skills. Applied in 4813132 (not yet re-measured).

## Other defect found

values-levers' Output Format never listed the Lever Resistance Map or the
30-Day Action Plan that its workflow and Quality Bar require; this round all
three outputs omitted the map (structural 80% vs 94%). Fixed in 4813132, with the same
defect in pledge-works (red-line register, traceability) and ethical-contract
(Tension Map), found by checking every rubric section pattern against each
template (not yet re-measured).
