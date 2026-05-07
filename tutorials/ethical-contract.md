# Ethical Contract

**The short version:** A cross-disciplinary signed commitment — by designers, engineers, product managers, and sometimes legal — that names what the team is responsible for, where stakeholder interests conflict, and what the team will not do regardless of business pressure.

---

## Who made it

The Ethical Contract draws on traditions of values-centered design, responsible innovation frameworks, and cross-disciplinary ethics agreements developed in the tech industry and academic HCI research. It adapts the concept of a professional ethical code — common in medicine, law, and engineering — into a format appropriate for product design teams working under sprint-based commercial pressures.

The method is particularly influenced by participatory design traditions that treat ethical commitments as team agreements, not individual virtues.

---

## The problem it solves

Ethical intentions in product teams are usually individual and informal. A designer believes in user privacy. An engineer is uncomfortable with dark patterns. A PM wants to prioritize accessibility. These commitments exist — but they're not shared, not explicit, and not robust enough to survive a difficult stakeholder conversation or a missed quarterly target.

When business pressure arrives — and it always does — individual ethical intentions tend to bend. Not because people are dishonest, but because informal personal commitments are no match for structured organizational pressure.

The Ethical Contract makes commitments explicit, shared, and structured. It creates the conditions for a team member to say "we agreed to this" rather than "I personally feel uncomfortable with that."

---

## When to use it

- **At the start of a project** — to establish shared ethical commitments before the work is under pressure
- **When a team is working on a high-stakes product** — anything that touches health, safety, financial wellbeing, children, or vulnerable populations
- **When stakeholder interests are known to conflict** — the contract surfaces those conflicts explicitly rather than leaving them to emerge during a launch
- **When you want accountability that survives team turnover** — a written, signed contract outlies the individuals who made it
- **When leadership support for ethical design is uncertain** — the contract creates an explicit record of what the team committed to, useful when pressure comes from above

---

## What it produces

The Ethical Contract is built in five stages:

**Stage 1 — Stakeholder Tension Map:** Before any commitments are written, the method surfaces where stakeholder interests structurally conflict. This is a diagnosis, not a negotiation. "Business needs engagement; users need to be able to disengage. These goals are structurally opposed." At least two named tensions must be identified.

**Stage 2 — Shared Ethical Objectives (4 parts each, no aspirations):** Each objective is a four-part commitment, never optional:
1. **Action** — *"We commit to [specific ethical action] in order to [protected outcome]"*
2. **Quantitative threshold** — a number, percentage, or named standard that would constitute a breach (e.g., "if disparate-impact ratio drops below 0.8 across any protected subgroup of n ≥ 30")
3. **Named owner** — the role accountable for this commitment ("the team" is not an owner)
4. **Review cadence** — when this is checked (every sprint demo, pre-launch + 30/90/180 days post-launch)

Verbs without thresholds and owners get rejected. "We will be fair" is not a commitment; "Engineering lead reviews fairness scorecard before every release; release blocks if disparate-impact ratio < 0.8" is.

**Stage 3 — Bias & Harm Audit:** Before signing, the team completes a structured bias and harm audit. Without this, the contract is a values statement, not an accountability document. The audit includes:
- **Harm enumeration** — concrete harms named per population (primary users, vulnerable subgroups, non-users affected, workers in supply chain), with severity and reversibility
- **Bias audit thresholds** — for any product with ranking/scoring/recommendation: disparate-impact threshold (industry floor: 0.8 / four-fifths rule), subgroup minimum sample size, named proxy variables (zip code, school, browser language), model confidence floor
- **Gray-zone register** — use cases not explicitly prohibited but not consented to, with what would have to change before they become acceptable
- **Red lines** — 3–5 concrete refusals at the feature level, each with a named owner with veto authority and a consequence if breached

**Stage 4 — Ultimate Design Goal:** A single unifying statement: *"Our design goal for [product] is [outcome] for [users], while [ethical commitment]."*

**Stage 5 — Commitment Risk Register + Signatures:** For each objective, document the most likely failure moment, the early warning signal, and the protection mechanism. Then signatures from all participants — making it a real commitment, not just a document.

---

## The key insight

The Commitment Risk Register is what makes this method different from a mission statement. Every team can write inspiring values. Very few teams write down the specific moment they expect to violate those values and what they'll do when that moment arrives.

The register forces that honesty. It says: "Here is when we will be tempted. Here is what temptation will look like. Here is what we have agreed to do instead." That specificity is what makes the commitment survivable under pressure.

---

## How to use it with AI

Describe your product, the key stakeholders involved, any known tensions, and existing ethical concerns. The AI will work through all five stages: tension map, four-part shared objectives, bias & harm audit (with thresholds, gray-zone register, and red lines with named veto owners), ultimate design goal, and commitment risk register with signatures. The output is ready to be reviewed, revised, and signed by the team.

---

## A quick example

**Product:** A consumer lending app that offers short-term loans with tiered interest rates.

**Stakeholder Tension Map:**
- *Business needs high loan acceptance rates; users need to be protected from loans they can't repay.* These goals are structurally opposed. The business profits from loans; users can be harmed by them.
- *Marketing needs simplified messaging; regulatory compliance needs complete disclosure.* Simplified messaging can obscure costs that users have a legal right to understand.

**One 4-part shared objective (excerpt):**
- **Action:** We commit to refusing loans our own model assesses as high-risk for default, in order to protect users from preventable financial harm.
- **Quantitative threshold:** Default-risk score above 0.65 → automatic decline; manual override requires CRO sign-off plus ethics review.
- **Named owner:** Head of Underwriting.
- **Review cadence:** Pre-launch + every quarterly business review.

**Bias & Harm Audit (excerpt):**
- *Harm enumeration:* "Users in financial precarity may be steered toward higher-tier products by the recommendation algorithm" (severity: high, reversibility: medium).
- *Bias thresholds:* Disparate-impact ratio < 0.8 across any zip-code cluster or census tract triggers immediate halt of new loan issuance pending audit. Named proxy variables: zip code, employer name, device model.
- *Red lines (3 of 5):*
  1. We will not target loan products to users our model has identified as financially distressed. Veto: Head of Trust & Safety. Consequence: PM responsible for proposal is removed; incident logged.
  2. We will not implement UI patterns that obscure APR or fees. Veto: Head of Design. Consequence: feature is rolled back within one sprint.
  3. We will not change the underwriting threshold to increase approvals without independent ethics review. Veto: Chief Risk Officer. Consequence: change is reverted; audit issued to board.

**Commitment Risk Register (one entry):**
- **Commitment:** We will not approve high-risk applications.
- **Most likely moment of failure:** Q3 growth review, when approval rates fall short of target.
- **Early warning signal:** Leadership requests approval rate data alongside default rate data, but frames conversation around the former.
- **Protection mechanism:** The team lead cites this contract; threshold changes route to documented ethics review per Red Line #3.

---

## See also

- [DAH Cards](dah-cards.md) — a facilitation session that produces an ethics manifesto; the Ethical Contract is more formal and structured
- [Pledge Works](pledge-works.md) — translates commitments into specific pledges and stress-tests them; pairs naturally with the Ethical Contract's Red Lines
- [Values Levers](values-levers.md) — identifies organizational mechanisms to support ethical design culture; the contract is one artifact that culture needs
