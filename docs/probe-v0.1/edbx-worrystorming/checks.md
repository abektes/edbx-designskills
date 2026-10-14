# Checks: edbx-worrystorming (written before opening any output)

Source: Chivukula & Gray (2025), Universal Methods of Ethical Design, entry 100 "Worrystorming", p. 208 (`chivukula2025universal`, provenance rows 1, 2, 7, 9, 10). This is the only source found for the method and the entry text is unreadable, so every check is `metadata only: book` and rests on stage A's description of the entry; no manifest source mentions Worrystorming. Skipped as adaptation: the eight concern categories and their guiding questions, 10-20 raw worries, 3-6 clusters of 3-5 worries, Critical / Monitor / Low Risk severity tags, Ethical Objective / Design Constraint / Test Question per cluster, Step 5 mitigations and consultees, time budgets and silent-writing rounds, the "Worrystorm Summary" sticky-note paragraph, "capstone" and "explicitly consequentialist" framing (rows 3-4, unconfirmed), hashtags, See Also, the Answer section, the Evidence Ledger, output formatting.

- D1: Starts from a divergent, brainstorm-style generation of worries (what could go wrong or concern people) about the design, written out as a list before any sorting or evaluation (rows 7, 10).
- D2: Clusters the worries into themes (rows 10).
- D3: Reframes the clustered worries as values (what each theme says people care about), not only as risks to mitigate (row 10).
- D4: Generates refined ideas or design alternatives from the reframed values (row 10).
- D5: Treats worry / ethical anxiety itself as a design resource, and points the session at large-scale dilemmas and future consequences rather than at idea generation about features (rows 7, 9).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): names a creator, origin or source for Worrystorming other than Chivukula & Gray / Universal Methods of Ethical Design as fact; says it is a version of a named other method (e.g. pre-mortem, Black Mirror Brainstorming) as fact; gives a different step sequence or step count as the published method; or presents a fixed concern-category list, severity scheme or time budget as the published method's own.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done, or misstatement present; weak = under 40%). Here 1 of 5 moves done (D1 only). M1 present in 1 of 3 (partial in a second); M2 partial in 1 of 3. Caveat: the entry text is unreadable, so the checks rest on a stage A description of the book entry (sequence worry list, clusters, values, refined ideas); the plain model does the first step well and the rest only in part.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D3 0/3: no output reframes the clustered worries as values; clusters end in a "worst-case consequence" or a priority score, e.g. the neighbourhood-app clusters never say what the community cares about underneath.
- D4 0/3 (one partial): no refined ideas generated from the reframed values; the therapy-bot output only says "map each worry to a specific mitigation" as a next step, and the school output lists generic mitigations and alternatives.
- D2 0/3 (three partial): clusters are the user's own categories (or the model's topic headings), not themes that emerge from the worry list.
- D5 0/3 (three partial): worry is treated as risk input, not as an ethical-anxiety resource; the sessions aim at harm lists, not at calibrating large-scale dilemmas.
- M1 1/3 yes, 1/3 partial: the neighbourhood-app output invents an app name ("SightLine"), a session date and participants; the school output asserts unsourced research findings.
- M2 1/3 partial: the therapy-bot output defines the method as imagining the project has already failed and working backwards (a pre-mortem), not the worry, cluster, values, ideas sequence.

What the plain model already does well:
- D1 3/3: long, concrete lists of worries across every area the prompt named, including non-obvious ones (stalking via 2-mile windows, mandatory-reporting gaps, transgender misidentification).
- Prioritisation (severity x likelihood), worst-case scenario stories and open questions for decision-makers, although these are not the method's moves.
