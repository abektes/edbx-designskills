# Eval: after the rubric and defect pass, one sample per scenario

Run on 0d314a1 (defect pass) with the rubrics at 4637569 (2026-10-13). All 63
with-skill outputs regenerated (DeepSeek V4 Pro via OpenRouter, $1.32); the
method-named baseline came from cache. Blind pairwise judging by Claude Sonnet
subagents with the seven-dimension rubric and the label-swap quote check.

## Result

- Skill preferred in **60/63** pairs (previous round 61/63), ties 0, label
  swaps 0. Flat within one-sample noise: the pass made edbx more measurable,
  not measurably better on the A/B.
- Dimension gap (skill minus baseline): structure_format +0.43 ·
  depth_specificity +1.16 · actionability +1.13 · methodology_fidelity +2.67 ·
  coverage_completeness +1.19 · ethical_nuance +0.90 · evidence_honesty +1.25
  (was +1.49).
- Structural conformance on the new 94%-coverage rubrics: skill 1085/1147
  (94.6%), baseline 62/1060 (5.8%). The previous outputs score 95.4% on the
  same rubrics.

## What the defect pass changed (same rubrics, old vs new outputs)

- Fixed as intended: anotherlens 'When' not invented 0/3 -> 3/3, concerns
  mapped in Synthesis 0/3 -> 2/3, ethicography move sources 0/3 -> 3/3,
  positive practices 1/3 -> 3/3. anotherlens elderly-telemedicine
  evidence_honesty 2 -> 5 in the A/B.
- Outputs with `sourced` rows lacking a URL: 5 -> 3 (still not zero).
- Six rubric checks turned out to accept only one output format and went
  3/3 -> 0/3 or 1/3 when outputs switched to tables or lists; fixed in
  893b3d3 and 4637569 before the numbers above.

## Losses

- ethicography / wellness-score-postmortem (tie on score, baseline picked):
  the trace rests on invented actors, decisions and "confirming documents"
  presented as sources, despite the reconstructed marking. accessibility-debt
  is still evidence_honesty 2. Wording has not fixed this skill: it asks for
  a decision history the brief does not hold. Next: when the brief has no
  record, the deliverable should be a record request plus labelled
  hypotheses, not a full trace.
- anti-heroes / ethical-dialogue-default-data-sharing (-0.14): the baseline
  gave the timed facilitation script the user asked for.
- worrystorming / school-facial-recognition (-0.57): leaked scratch work and
  broken cross-references (generation slip).

Data: `judging/` (Sonnet verdicts and tally).

## Re-test: ethicography with a record check (f2e6dc0)

Step 0 now classifies the brief as Record or Outcome only; with outcome only
the skill codes just the stated moves and lists the rest as Hypotheses to
Check. Three outputs regenerated ($0.05), judged blind
(`judging-ethicography-record/`).

- Skill preferred **3/3**, 0 label swaps. evidence_honesty 4, 5, 5 (baseline
  3, 1, 2); the two scenarios stuck at 2 for two rounds are fixed. Coverage
  dipped once (accessibility-debt 3 vs 4), the expected cost of not
  inventing a history. Structural 48/48.
