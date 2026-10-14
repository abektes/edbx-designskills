# Checks: edbx-bad-design-canvas (written before opening any output)

Source: Manos, M., *Less (Bad) Design: A Toolkit For Ethical Ideation* (Bad Design Canvas) (`manos2020lessbad`); method listed as #09 in Chivukula & Gray (2025), *Universal Methods of Ethical Design* (`chivukula2025universal`). Caveat: every provenance row is `metadata only` and no toolkit text was readable, so the twelve names and guiding questions are unverified against the canvas; the checks rest on the skill's wording of the canvas (rows 3-9) and the listing's "12 principles of Bad Design" / "uncovering the new problems our solutions might generate" (rows 2-3). Skipped as adaptation: severity tags (Significant / Possible / Low), Systemic vs Addressable split and clusters, Top 3 ranking, redesign recommendations per finding, Bad Design Statement, "Should we build this?" verdict, facilitation times, silent solo fill, emoji, Answer section, Evidence Ledger, output formatting.

- D1: Fills a canvas of twelve distinct consequence categories, one response per category, instead of a free-form list of harms (rows 3-9).
- D2: Has a Band-Aid cell: asks whether the idea misses the root cause of the problem and is only a temporary fix, i.e. questions the problem the product claims to solve (rows 2, 5).
- D3: Has a Cultural Appropriation cell: asks what the idea borrows from a culture the team is not representative of (row 4).
- D4: Has a Displacement cell: asks what the idea substitutes for or replaces (people, practices, existing services) (row 8).
- D5: Has a Boring cell that treats it as a creative-quality check (is the idea uninspired or plain), not an ethical harm (row 8).
- D6: Has an Inefficiency cell: asks whether the idea creates new inefficiency, unnecessary complexity, confusion or delay (row 6).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): wrong creator (not Matthew Manos), a category count other than twelve or wrongly named categories presented as the canvas's, severity ratings / systemic-addressable split / Bad Design Statement / build verdict attributed to the source, or claims about the toolkit (licence, version, exercises) that provenance.md says it cannot confirm.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 0 of 6 moves done. M1 present in 3 of 3; M2 in 0 of 3. Caveat: all provenance rows are `metadata only`, so the twelve categories are unverified against the toolkit; the verdict rests on the skill's wording of the canvas.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 0/3: no output fills twelve consequence cells; each uses its own sections (habit tracker: twelve numbered sections such as Power Dynamics, Sensemaking Breakdown, Habituation, none of them the canvas categories).
- D2 0/3 (one partial): no one asks whether the product is a band-aid for the real problem; the energy monitor only gets near it ("personal habits (not industrial pollution or policy failures) are the root cause").
- D3 0/3: no cultural appropriation cell in any output.
- D4 0/3 (one partial): replacement or substitution is mostly absent; moderation touches it via human moderators' changed workload.
- D5 0/3: nothing treats "boring" as a creative-quality check.
- D6 0/3 (one partial): new inefficiency, complexity or delay is not examined as its own category.
- M1 3/3: each output asserts system details the prompt does not give (moderation: a public score and "millions of posts per hour"; habit tracker: "no grace period"; energy monitor: a primary user who sees each housemate's room usage).

What the plain model already does well:
- Long, specific lists of harms to affected groups (dialect speakers, anxious users, housemates, people in energy poverty), plus power-imbalance and inequity analysis, which would map to Unfair Control, Exploitation, Stakeholder Abandonment, Decreased Safety and Inequity in the canvas.
- Concrete redesign options for each harm, and no misstatement of the method (it never names a creator or category count).
