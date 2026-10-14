# Checks: edbx-dah-cards (written before opening any output)

Source: ziqq rafit (2020), *Design Against Humanity (DAH)*, project page (`rafit2020design`, rows 1, 2, 5), and Chivukula & Gray (2025), *Universal Methods of Ethical Design*, Method 16 "DAH Cards" (`chivukula2025universal`, rows 3, 6, 7). Every row is `metadata only` and none of the card rules could be read as text, so these checks rest on the skill's description of the original method; row 4 (the "do to people" flip) has no source and is not used. Skipped as adaptation: the six harm categories and the 4-of-6 coverage rule, consequence mapping fields (likelihood, severity, who bears it, design awareness), microcopy Before/After rewrites, Modes 3-4 (manifesto, future vision) and the mode-selection rule, Ship-Ready Recommendation, Answer section, Evidence Ledger, output formatting.

- D1: Writes card pairs for the product's features: a black side naming the product or feature and a white side stating its problematic consequences (row 5).
- D2: Sorts the items into exactly three piles, Ethical / Unsure / Unethical, with Unsure as a real middle pile (row 6).
- D3: After sorting, runs a "What changed?" reflection: which card surprised the team, what moved pile, which assumption shifted (row 7).
- D4: Aims the exercise at exposing real-world harms of the product so the designer reflects on their own responsibility for them (row 3).
- D5: Opens a conversation about the purpose, context and role of design, not only a list of harms (row 2).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): wrong creator or origin (not ziqq rafit; or conflating it with the Behance "Design Against Humanity" Cards Against Humanity expansion), wrong name expansion, claiming the game's own card categories or rules differ from what the skill states (e.g. fixed numbers of cards or piles other than three), or attributing the six harm categories, consequence map fields, microcopy rewrites, manifesto or future vision to the published game.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 0 of 5 moves done (D4 is the closest, `yes` in 1 of 3). M1 present in 2 of 3; M2 present in 3 of 3. Caveat: no DAH rules text was readable (all provenance rows are `metadata only`), so the checks rest on the skill's description of the original method; the M2 findings are invented card decks, not contradictions of a read source.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 0/3: no black-side / white-side card pairs; the outputs invent their own decks (question prompts such as "If your product was a cult ...", principle cards such as Privacy and Transparency, provocation cards such as "The Shame Spiral").
- D2 0/3: no Ethical / Unsure / Unethical sort in any output; the audit ends "Ship with mandatory safety and ethics modifications".
- D3 0/3: no "What changed?" reflection on surprises or shifted assumptions.
- D5 0/3: no question about the purpose or role of design.
- D4 1/3 (one partial): only the manifesto output reflects on the team's own responsibility ("We are accidentally building a machine ...").
- M2 3/3: each presents an invented deck as DAH Cards ("Four cards were drawn from the DAH deck"), and one expands DAH as "Design Against Harm".
- M1 2/3: Duolingo "users report genuine anxiety ..."; manifesto output invents an app name, a six-person session and "We sell anonymised activity-pattern data to insurance partners".

What the plain model already does well:
- Broad, specific harm mapping per mechanic (streaks, hearts, notifications, shared workout alerts) with concrete mitigations and a clear ship decision.
- First-person manifesto and future vision with specific commitments, when asked.
