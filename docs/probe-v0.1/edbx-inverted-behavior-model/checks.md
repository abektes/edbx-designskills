# Checks: edbx-inverted-behavior-model (written before opening any output)

Source: Zhou, K., "BJ Fogg's Inverted Behavior Model", Design Ethically toolkit page (`zhou2026invertedbehavior`, provenance rows 1-3, 5, 6, 18), with Chivukula et al. (2021) p. 32 for the Zhou attribution. Skipped as adaptation: Step 0 stakeholder map, the element-level prompt definition and example list, the five motivating-factor categories, Step 2.5 Worst Possible Design, Step 2.6 Convergence Check, the behaviour taxonomy, Behavioral Cascade Model and "10M users" scale test, Step 4.5 Rationalizations Check, Redesign Directions (min 2 per red finding), Behavior Forecast Statement, hashtags/See Also, Answer section, Evidence Ledger, output formatting.

- D1: Takes Fogg's Behavior Model (behaviour happens when Motivation, Ability and a Prompt come together) as the base and states that the method inverts it: it forecasts the behaviours a product's prompts lead to instead of designing for one intended behaviour (rows 2, 3).
- D2: Starts from a list of the prompts to forecast (features or whole products) and treats them as the unit of analysis (row 5).
- D3: For each prompt writes out the motivating factors that might come into play, then predicts the behaviours they lead to, including unknown or unintended ones, as separate steps in that order (rows 1, 5).
- D4: Analyses the consequences each predicted behaviour might trigger (row 5).
- D5: Estimates the ability level (how easy or hard) of each predicted behaviour and ranks behaviours by likelihood, optionally by severity (row 6).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): credits BJ Fogg (or anyone other than Kat Zhou / Design Ethically) as creator of the Inverted Behavior Model, instead of as author of the base model; calls a worst-possible-design or convergence step the core of the method; presents categories of motivation (intrinsic/social/extrinsic/emotional/habitual), stakeholder maps, cascade models or rationalization checks as part of the published method; writes the formula as "B = M + A + P" while attributing the "+" notation to the source page; claims the method is validated or has a fixed step count other than the prompts, motivations, behaviours, consequences flow.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 1 of 5 moves done (D4 only). M1 present in 0 of 3 (partial in 1: the fridge output states sensor, barcode and camera tracking as the feature's mechanism); M2 present in 2 of 3 (yes), partial in the third.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 0/3: Fogg's Behavior Model (Motivation, Ability, Prompt) is never named; two outputs redefine the inversion as flipping each intended behaviour into a "harmful opposite" (fridge: "pathological opposite"), the third as a rational-actor question. None says it forecasts behaviour from prompts instead of designing for an intended one.
- D3 0/3: no output lists motivating factors per prompt before predicting behaviours; they jump from feature to abuse or gaming behaviour.
- D5 0/3: no ability-level estimate; only the social-savings output ranks anything (a likelihood/impact table of risks, partial), and the others do not rank behaviours.
- D2 1/3: only the productivity output works feature by feature (points, leaderboards, badges); the fridge and savings outputs organise by intended behaviour, not by prompt.

What the plain model already does well:
- D4 3/3: rich consequence analysis (stakeholder impacts, second-order effects, societal risks) for every predicted behaviour.
- Broad and plausible unintended-behaviour lists (metric gaming, coercion, data exploitation), with no invented figures and, in the savings output, assumptions labelled as assumptions.
