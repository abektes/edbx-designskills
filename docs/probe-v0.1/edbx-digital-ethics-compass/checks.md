# Checks: edbx-digital-ethics-compass (written before opening any output)

Source: Dansk Design Center (DDC), *The Digital Ethics Compass: Put the Human at the Center* (the "Ethics Navigator" checklist), toolkit page and the Principles, Automation, Behavioral Design and Data pages (`ddc2021compass`, `ddc2021principles`, provenance rows 1, 6, 8-11, 13; stage B checked these against the page text). The skill's own structure is contradicted by the source (rows 3-5, 7), so the D-checks use what the pages say, not the skill's four-category wheel. Skipped as adaptation: Step 0 Stakeholder & Power Map, Step 0.5 Objective Function Risk Table, Step 0.6 Non-Obvious Harms Inventory, status colours, Business Pressure Attribution, Quick Win / Strategic Fix / Requires Leadership, Compass Reading, hashtags, See Also, mindset check, Answer section, Evidence Ledger, output formatting.

- D1: Organises the questions in the source's three question categories, Data, Automation and Behavioral Design (rows 4, 5; DDC has 22 questions: Automation 10, Behavioral Design 6, Data 6).
- D2: Data: asks whether too many data points are collected and kept too long, and whether people can get access to their own data (row 6).
- D3: Automation: asks whether the algorithms are prejudiced, whether the system can explain itself, and whether the "engine room" is made visible to users (row 11).
- D4: Behavioral Design: asks whether the product validates or challenges its users, and checks for fear and urgency, social need, dark patterns and addiction (rows 8, 9).
- D5: States the principle of making the technology understandable: letting users comprehend how the solution works and affects their lives (row 10).
- D6: Treats the human to keep at the centre as everyone affected by the solution, not only the users (row 13, closest passage).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): uses the centre phrase "Put the Human in the Cosmos" (DDC says "at the Center"); calls it a wheel with inner, middle and outer rings, or a rotatable wheel; presents four categories (Data, Avoid Manipulation, Make Intentions Transparent, Automation) as DDC's; gives a wrong creator (not Dansk Design Center) or a wrong question count; or attributes shutdown / data-sharing questions, "values used against people" or "cognitive biases" questions, or Steps 0 / 0.5 / 0.6 to DDC.

## Verdict
**partial** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 3 of 6 moves done (D3, D5, D6). M1 present in 2 of 3; M2 present in 2 of 3. The prompts named the aspects to cover (data, algorithmic influence, power; who consented, who benefits), which helps D2, D3 and D6; the plain model never uses DDC's own structure.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 0/3: none uses DDC's three question categories (Data, Automation, Behavioral Design); the outputs use five invented phases, a Human / AI / Oversight framework, or the prompt's own four questions.
- D2 1/3 (two partials): collection limits and retention appear, but only the children's output also gives people a view of their own data ("a simple dashboard of their own data"); the chatbot output offers deletion only.
- D4 0/3 (two partials): no output asks whether the product validates or challenges users; the nearest are "Manipulation of motivation: Streaks, leaderboards ..." and "Over-reliance on the bot".
- M2 2/3: the children's output presents "five phases - Define, Understand, Ideate, Evaluate, Decide" as the method; the chatbot output says its recommendations use "the Human, AI, and Oversight framework".
- M1 2/3: the children's output lists data it collects (clicks, mistakes, device usage patterns) that the prompt never gave; the city output asserts "Environmental data low risk (stored for 5 years)".

What the plain model already does well:
- D5 3/3: transparency to users about how the system works ("why am I seeing this?", real-time sensor indicators, "right to know they are talking to an AI").
- D6 3/3: stakeholder maps that reach beyond users (regulators, content partners, future generations).
- D3 2/3: bias and explainability of the algorithm, with concrete controls.
