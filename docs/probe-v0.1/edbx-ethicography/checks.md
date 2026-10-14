# Checks: edbx-ethicography (written before opening any output)

Source: Chivukula, Gray & Brier (2019), Analyzing Value Discovery in Design Decisions Through Ethicography, CHI '19 (`chivukula2019ethicography`, provenance rows 1-10, 23-24), with the survey paper `chivukula2021surveying` (row 15). Skipped as adaptation: Step 0 check-the-record, the 2x2 Explicit/Implicit x Persuasion/Coercion matrix, "Design Move" numbering and Ethical Moves Inventory, value families (user, designer, business, non-user, worker), the required affected-populations table, concrete-harm examples, Performative Ethics Moves (hidden speech acts), Trajectory Forward 12-month projection, Team Reflection / Research Documentation modes, meeting notes / crits / Slack as input, Answer section, Evidence Ledger, hashtags, output formatting.

- D1: Breaks the design record into discrete units, one per statement or utterance in the design dialogue (speech acts), rather than analysing the project as a whole (row 7).
- D2: Assigns each unit a value code: which value(s) it shows an attitude toward (for example privacy, trust, autonomy, accountability, informed consent, freedom from bias, human welfare) (row 8).
- D3: Marks each unit's value stance as more value-centered or more manipulative (row 10).
- D4: Links the units to one another to draw a map of how decisions and values relate, the ethicograph, so the interplay of values is visible (rows 6, 9).
- D5: Layers an idea code on the units, tagging each as a problem, a solution or a decision rationale (row 9).
- D6: Reads implicit values behind explicit decisions and follows value-laden decisions across the sequence of the process over time (rows 23, 24).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): wrong creator (for example "Chuvaala" or a missing or different author such as Friedman or Goldschmidt as the creator), presents an Explicit/Implicit x Persuasion/Coercion 2x2 or "Design Move" labels as the published method, says the paper analyses meeting notes, crits or Slack, claims two named modes or a forecast step come from the source, claims a 2024 paper, calls it the most rigorous ethics method, or claims it is validated in professional practice (the source is a lab study of 24 students).

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 2 of 6 moves done (D2 and D6, both at decision level, not speech-act level). M1 present in 1 of 3 (partial in a second); M2 present in 1 of 3.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 0/3 (2 partial): the unit is a project stage or a decision (wellness: "Decision Trace" table), never a speech act from a design dialogue.
- D3 0/3 (2 partial): no unit is marked value-centered versus manipulative; every unit is simply called a failure.
- D4 0/3: no links between units, so no map of how values interact; findings sit in tables and lists.
- D5 0/3: no problem / solution / rationale tagging of units.
- Invention and misstatement: the growth-phase output states unprovided details as "we did" facts (an 18-month runway, a greyed skip button); the wellness output redefines ethicography as treating a feature "as a moral artifact".

What the plain model already does well:
- D2 2/3 (one partial): names the value at stake for each decision (accessibility: "Ethical Principle Violated"; wellness: "Value that won").
- D6 3/3: contrasts stated reasons with implicit motives and follows how small trade-offs compound across the process.
