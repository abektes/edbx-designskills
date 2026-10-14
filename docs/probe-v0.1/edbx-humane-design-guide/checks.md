# Checks: edbx-humane-design-guide (written before opening any output)

Source: Center for Humane Technology, Humane Design Guide, a two-sheet worksheet (`cht2020designguide`, provenance rows 1, 3-12, 19, 21-24; the PDF text was read in stage B). Skipped as adaptation: the skill's "Enabled to ..." wordings, listing Attention first, the four-column table (current state, what's at risk, level, improvement), three-colour level, named psychological mechanisms, Differential Impact by population, Alternatives A/B/C, Business Tension, Algorithm Audit, Exploitation Stack Analysis, Memorable Heuristics, the Engagement-Value Paradox aphorism, "Method #47", hashtags, Answer section, Evidence Ledger, output formatting.

- D1: Opens by capturing the product or feature, its value proposition and its measure of success (row 19).
- D2: Structures the analysis around the six human sensitivities, naming all six: Emotional, Attention, Sensemaking, Decision-making, Social Reasoning, Group Dynamics (row 4).
- D3: For each sensitivity, separates the ways the product inhibits it from the ways it could support it (the sheet's "inhibited when" and "supported when" columns) (rows 11, 12).
- D4: Ranks the sensitivities by opportunity to improve, on a High to Low scale and as an ordered 1-6 ranking (row 21).
- D5: Checks whether the product's success criteria are in tension with any of the sensitivities, and whether they need to shift (row 23).
- D6: Closes with an action statement for how the product can support or elevate the sensitivities (rows 22, 24).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): wrong number or names of sensitivities, or a sensitivity added or dropped; credits named individuals as authors of the guide (the sources name none) or a different organisation; presents the skill's own columns, "Enabled to" lines or exploitation lists as the worksheet's; says the worksheet states people are made to act against their own choice; calls it "Method #47" or a book entry; or claims it is validated.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 0 of 6 moves done (D5 is `yes` in one output only). M1 present in 1 of 3 (partial in a second); M2 present in 2 of 3 (partial in the third).

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D2 0/3: none of the outputs uses the six sensitivities; each substitutes its own list (news: "Attention, Agency, Emotional Well-being, Cognitive Autonomy, Social Impact, Time Well Spent"; dating: agency, transparency, cognitive liberty).
- D1 0/3 (2 partial): no intake of product, value proposition and measure of success as the sheet frames it.
- D3 0/3 (3 partial): inhibit versus support is split per feature, not per sensitivity.
- D4 0/3 (2 partial): no ranking of sensitivities by opportunity to improve; features get severity or verdicts instead.
- D5 1/3: only the news output calls out its success metric as the root problem; dating examines no metric, and teen swaps metrics without testing the original against the sensitivities.
- D6 0/3 (3 partial): recommendation lists, not a closing action statement.
- Misstatement (M2 2/3 yes): outputs present their own principles or "lenses" as the Guide's ("We applied the Humane Design Guide's core lenses"); dating states a typical swipe quota "(commonly 25–50)" as fact.

What the plain model already does well:
- Detailed feature-level critique with named psychological mechanisms and concrete redesigns; the news output ties the exploitation back to the "time spent reading" metric.
- Attention and emotional vulnerabilities appear in all three, although not as the sheet's named sensitivities.
