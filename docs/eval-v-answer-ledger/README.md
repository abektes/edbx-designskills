# Eval: Answer first and Evidence Ledger, one sample per scenario

Run after commit 80d5e07 "Answer first and an Evidence Ledger in every skill"
(2026-10-12). Only the with-skill arm was regenerated (63 outputs, DeepSeek V4
Pro via OpenRouter, $1.24); the baseline arm, told the published method by
name, came from cache. Pairs were judged blind by Claude Sonnet subagents (in
session, no API cost) with the seven-dimension rubric and the quote check
against label swaps (`scripts/judge_pairs.py`, ported from cdbx). This is the
first edbx eval whose harness, scenarios and verdicts are all in version
control; RESULTS.md describes an earlier one whose harness was lost.

## Result

- Skill preferred in **61/63** pairs, ties 0, label swaps 0.
- Mean score gap per dimension (skill minus baseline, 1-5 scale):
  structure_format +0.59 · depth_specificity +1.19 · actionability +0.92 ·
  methodology_fidelity +2.75 · coverage_completeness +1.32 · ethical_nuance
  +0.95 · evidence_honesty +1.49.
- Structural conformance (code checks, semantic checks not run): skill
  367/381 (96%), baseline 17/339 (5%). answer_first 33/33, Evidence Ledger
  present 33/33, ledger types valid 32/33 (only 11 of 21 skills have a rubric).

## The two losses: the ledger labels invention, it does not stop it

- anotherlens / elderly-telemedicine (delta -0.57): the skill output followed
  the lenses but fabricated prototype details about the user's product.
- ethicography / accessibility-debt (delta -0.29): the skill output invented
  incidents and quotes about the user's company and disclosed this only in its
  closing ledger. The same output is the one ledger-type failure above.

Ethicography is an ethnographic method: with no fieldwork in the brief, the
model fills the gap with quotes. Next fix: when the brief has no field data,
the skill should plan the fieldwork and mark findings as hypotheses, never
write observations or quotes.

One sample per scenario: read the box-level rate, not per-skill counts.

Data: `judging/` (Sonnet verdicts and tally).

## Re-test after the anti-invention fix (a789fb2, 2026-10-13)

Only anotherlens and ethicography regenerated (6 outputs, $0.03), judged
blind against the same cached baselines (`judging-fix-invention/`).

- Skill preferred **6/6** (was 4/6 for these two skills), 0 label swaps.
- Coverage of the concerns the user named rose (anotherlens
  elderly-telemedicine: coverage 5 vs 4; was 3 vs 5).
- **Invention is reduced, not gone.** evidence_honesty is still 2 (baseline
  4) in the same two scenarios: elderly-telemedicine still invents some
  product details, accessibility-debt still invents incidents that the ledger
  only partly offsets. social-media-growth-hacks shows the intended behaviour
  (evidence 4 vs 1, "honest about reconstruction").
- Next: one sample per scenario cannot separate wording from luck; when
  edbx is re-run after the defect pass, read these two scenarios first.
