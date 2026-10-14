# Checks: edbx-motivation-matrix (written before opening any output)

Source: Zhou, K., "Motivation Matrix", Design Ethically toolkit page (`zhou2026motivationmatrix`, provenance rows 1-3, 5, 6, 8-10, 18), with Chivukula et al. (2021) p. 32 for the Zhou attribution. Skipped as adaptation: the audit/manipulation framing and "deliberately provocative" tone, the design examples per type (progress bars, likes, countdowns, leaderboards, discounts), the "at least two contexts, suggest a third" rule, the formula "MOTIVATION TYPE x USE @ CONTEXT", the "[Motivation] + [Action]" cell template (action = what the design does to the user), the three ethical lenses, green/yellow/red flags, Ethical Risk Summary, Redesign Directions, Missing Contexts, the overjustification effect, Evidence Ledger, Answer section, output formatting.

- D1: Names six motivating factors: incentive, achievement, social acceptance, fear, power and growth (growth = intrinsic drive to become a better version of oneself), not five (rows 3, 5).
- D2: Builds a grid that relates the motivating factors (rows) to various users of the product in different contexts (columns) (row 6).
- D3: Each cell records the potential actions the user could take given that motivation in that context (row 8), not what the design does to the user.
- D4: Frames the purpose as predicting how a user might interact with the product, because people act on motivations that differ by context (rows 1, 2).
- D5: Says to run the exercise after empathy mapping, using insights from sponsor users (row 9).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): credits anyone other than Kat Zhou / Design Ethically (e.g. "Annabelle Zhu", "Cordelia Nodders", Fogg, Deci and Ryan, Maslow) as the method's creator; says there are five (or another number other than six) motivation types or names a different set as the method's own; gives the formula "MOTIVATION TYPE x USE @ CONTEXT" or a "[Motivation] + [Action]" cell as the published method; attributes a flag scheme (green/yellow/red), three ethical lenses or a risk summary to the method; says the method is an audit for manipulation by design.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 0 of 5 moves done. M1 present in 0 of 3 (partial in 1: the Duolingo output states hearts and league mechanics as fact); M2 present in 3 of 3.

Note on D1: the wellness prompt itself lists five types (Achievement, Social Acceptance, Fear, Power, Incentive), so that output only echoes the prompt; it is scored `no` because growth, the sixth type, is absent. The other two prompts name no types and neither output uses the six.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 0/3: the six types (incentive, achievement, social acceptance, fear, power, growth) never appear; the review-platform output uses intrinsic/extrinsic and the Duolingo output uses Self-Determination Theory (autonomy, competence, relatedness).
- D2 0/3: no matrix of motivation types against users in contexts; two outputs cross motivations with features or mechanics (wellness: "maps each core motivation against the three main product features") and one with stakeholders (partial in two).
- D3 0/3 and D4 0/3: cells hold design effects or a manipulation verdict ("Strongly manipulative"), never the actions a user could take; none frames the matrix as predicting how users will interact.
- D5 0/3: nothing on running it after empathy mapping with sponsor users.
- M2 3/3: all three call it an ethical audit or an ethics-versus-manipulation verdict ("I’ll run the Motivation Matrix as an ethical design audit"), which is the edbx framing, not the published exercise.

What the plain model already does well:
- Thorough, plausible analysis of how features exploit fear, status and reward, with vulnerable-user impacts and redesigns; no invented figures about the user's own product.
