# Checks: edbx-anti-heroes (written before opening any output)

Source: Mehta, Chivukula, Gray and Gairola (2024), Anti-Heroes preprint, arXiv:2405.03674 (provenance rows 1-5, 8, 10, 12, 15, 17, 19, 21, all `p. N`). Skipped as adaptation: the nine-pair deck list in SKILL.md/cards.md (Hero names unconfirmed), the fourth "Conceptualization" mode, mode step procedures, "first three changes I would ship", 2-5 cards per critique, "necessary friction kept", card-spam rule, dialogue script wording, the example UI illustrations (mascots, streaks), Answer section, Evidence Ledger, formatting.

- D1: Uses the method's role-card vocabulary: names at least two Anti-Hero roles that the paper confirms as cards (Trap-Setter, Empathy Manipulator, Nickling-and-Diming, Puppeteer, FOMO-Dealer) as roles the design or designer plays.
- D2: Pairs each Anti-Hero role with a value-centred Hero counterpart role (the card is double-sided: Anti-Hero face and Hero face).
- D3: Frames the roles as the designer's intentions or stance (what role the team is playing), for reflection, not only as a catalogue of UI dark patterns, and not as a verdict that the designer is bad.
- D4: Makes the value trade-off explicit: business/shareholder (monetary) values against human/user values, as the thing the roles surface.
- D5: Gives the team a way to call out a role in discussion (raising a named card, like a referee), rather than only a written verdict.
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): wrong creators or origin (not Mehta/Chivukula/Gray et al.), a deck size or card set presented as the deck that the paper does not support (the paper has 12 role cards, and names none of Black Hat, White Hat, Adversary, Ally, Unveiler, Life Coach, Liberator, Transparent Pricer as cards), Hero names or pairings asserted as the published deck, or a claim that the method is a dark-pattern checklist/scoring framework.

## Verdict
**partial** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 2 of 5 moves done (D3, D4). M1 present in 1 of 3; M2 present in 3 of 3. Verdict written by the coordinating session from the scores after the scoring agent hit a session limit.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 0/3: no deck role is named; every output invents its own characters ("Growth Amplifier", "Engagement Vampire", "Shame Gremlin").
- D2 0/3 (2 partial): no double-sided Hero counterpart per role; at most a generic "Heroic Alternative" or a "Flipped Commitment".
- D5 0/3 (2 partial): no card-raising call-out for the team; one output gives a shared vocabulary and a red-line list instead.
- M2 3/3: all three present an invented structure (a single persona, a five-question form, an eight-villain team) as the Anti-Heroes method.
- M1 1/3: the cancel-flow output names fined companies as fact.

What the plain model already does well:
- D3 2/3 (1 partial): frames the roles as the team's own pull, not a verdict on people ("a voice we all carry").
- D4 2/3 (1 partial): names the business metric against user wellbeing explicitly.
