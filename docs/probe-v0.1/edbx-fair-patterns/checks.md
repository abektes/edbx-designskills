# Checks: edbx-fair-patterns (written before opening any output)

Sources: Potel-Saville & Da Rocha (2023), From Dark Patterns to Fair Patterns? (`potelsaville2023fair`, rows 1-3; abstract only, paper paywalled, so these two checks rest on metadata-only rows for a paper rather than a book); California Privacy Protection Agency Enforcement Advisory 2024-02 (`cppa2024advisory`, rows 31-32, pp. 1-2); GDPR Art. 7(3) (`eu2016gdpr`, row 19); DSA Art. 25 (`eu2022dsa`, rows 21-22). The seven fair-pattern names and their pairings (rows 4-11) are metadata-only podcast rows, so I do not check for the specific names. Skipped as adaptation: the seven named countermeasure types and the ten-row dark pattern table, Step 2.5 Root Cause Reframe, Step 2.6 jurisdiction and penalty mapping, Step 2.7 Vulnerable Population Harm Matrix, Step 3 three-colour Default Assessment, the Legal Risk x User Impact / Effort priority formula, Fair Design Statement, Copy Rewrite format, mindset note, Answer section, Evidence Ledger, hashtags, output formatting.

- D1: Does not stop at spotting the dark patterns: pairs each identified dark pattern with a concrete countermeasure interface (a "fair pattern"), moving from problem-finding to problem-solving (row 1).
- D2: Defines the fair alternative by whether it empowers the user to make a free, informed choice, and tests each redesign against that (row 3).
- D3: Symmetry in choice: agreeing and declining (or accepting and rejecting) get equal prominence and the same number of steps, with the protective path no longer than the other (row 32, pp. 1-2).
- D4: Withdrawal or cancellation must be as easy as giving consent or signing up (rows 19, 22).
- D5: Judges a pattern by its effect on users, not by the designer's or company's intent (row 31, p. 1).
- D6: Frames a dark pattern as an interface that steers users against their own interests in favour of the business's (row 16, p. 3).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example). Quoting real law or regulators is not M1.
- M2 (misstated method or sources): credits Fair Patterns to the wrong creator (for example Brignull or Gray et al. as its authors) or says it "maps to" the Gray et al. (2024) ontology; says DSA Art. 25 names pre-checked boxes, false urgency or confirmshaming as banned, or binds only very large platforms; calls the UK law the "CMA Digital Markets Act"; states the DSA 6% or GDPR 4% fine as a fixed penalty for dark patterns; presents LGPD Art. 9 as a dark-pattern rule; or presents a ten-row list as the complete taxonomy.

## Verdict
**partial** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done, or misstatement present; weak = under 40%). Here 5 of 6 moves done (D1, D2, D3, D4, D6), but invention is present and misstatement is present in all three outputs, so the verdict is capped at partial. M1 present in 2 of 3 (yes in cookie consent, partial in fast-fashion); M2 present (partial) in 3 of 3. The M2 hits are unsupported attributions, not contradictions of a readable source: no fixed penalty, creator or DSA error appears.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D5 0/3: no output says a pattern is judged by its effect rather than intent; two call the friction "intentional" or "engineered".
- Method attribution (M2, partial 3/3): outputs credit "the Fair Patterns taxonomy" or "framework" with categories and questions it is not shown to contain (cookie: "Visual asymmetry", "False hierarchy", "Consent fatigue"), or coin pattern names ("Confirmation Fog", "The Open Door"); none uses the creators' own named countermeasures.
- Invented figures (M1 2/3 at least partial): the cookie output asserts "30–70% is typical" rejection as fact; fast-fashion states how the newsletter list was populated.
- D3 2/3: the fast-fashion output gives no accept versus decline parity.

What the plain model already does well:
- D1 3/3: every dark pattern gets a concrete redesign (equal buttons, unchecked box, non-blocking carousel).
- D6 3/3 and D2 2/3 (one partial): frames the patterns as steering users toward the business's benefit and tests alternatives against genuine choice.
- D4 2/3 (one partial) and D3 2/3: cancellation no harder than sign-up, and equal prominence of choices.
