# Ethical Contract

**The short version:** A cross-disciplinary signed commitment — by designers, engineers, product managers, and sometimes legal — that starts from the team's Ethical Disclaimer, agrees what each stakeholder is responsible for, and ends in three shared objectives, a design goal and signatures. The edbx version adds a tension map, red lines and a bias and harm audit.

---

## Who made it

The Ethical Contract is a tool by Jet Gispen (2017), from her *Ethics for Designers* toolkit (ethicsfordesigners.com). Her page describes it as a value negotiation with all stakeholders to find common ethical ground, in six steps, suggested at 30–45 minutes for the design team and stakeholders. It takes an **Ethical Disclaimer** (a list of the unethical situations the design could cause, from Gispen's separate Ethical Disclaimer tool) as its input. The page is marked "© Jet Gispen 2017" with no licence terms, so this tutorial paraphrases the steps.

The six steps: (1) explain the disclaimer to the stakeholders; (2) find recurring themes in it and agree a definition of each; (3) divide the unethical situations among the stakeholders and add any missed responsibilities; (4) summarise the responsibilities in three main ethical objectives; (5) update the design goal so all stakeholders agree; (6) sign to commit to the design goal and objectives.

The skill follows these six steps and adds several things of its own. Each is marked below as an edbx addition.

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

The skill works through Gispen's six steps, with extra steps marked as edbx additions:

**Step 1 — Explain the Ethical Disclaimer:** Walk the stakeholders through the unethical situations the design could cause. If you have no disclaimer, the AI drafts one from your brief and marks it as a draft to confirm. *(edbx addition: a 2–3 sentence ethical challenge statement that condenses the disclaimer.)*

**Step 1.5 — Stakeholder Tension Map (edbx addition):** Before commitments are written, surface where stakeholder interests structurally conflict. This is a diagnosis, not a negotiation. "Business needs engagement; users need to be able to disengage. These goals are structurally opposed." At least two named tensions must be identified.

**Step 2 — Recurring themes:** Collect the themes that recur in the disclaimer and agree a short definition of each for this project.

**Step 3 — Divide responsibilities:** Each stakeholder role gets a specific ethical responsibility. *(edbx addition: a Red Line per stakeholder, one thing they will not do regardless of business pressure.)*

**Step 4 — Three shared ethical objectives:** Gispen's step asks for three objectives everyone agrees on and understands. *(edbx addition: each objective has four parts, none optional.)*
1. **Action** — *"We commit to [specific ethical action] in order to [protected outcome]"*
2. **Quantitative threshold** — a number, percentage, or named standard that would constitute a breach (illustrative example: "if disparate-impact ratio drops below 0.8 across any protected subgroup of n ≥ 30"; the numbers are the team's to choose)
3. **Named owner** — the role accountable for this commitment ("the team" is not an owner)
4. **Review cadence** — when this is checked (every sprint demo, pre-launch + 30/90/180 days post-launch)

Verbs without thresholds and owners get rejected. "We will be fair" is not a commitment; "Engineering lead reviews fairness scorecard before every release; release blocks if the agreed disparate-impact ratio is breached" is.

**Step 4.5 — Bias & Harm Audit (edbx addition):** Before signing, the team completes a structured bias and harm audit. Without this, the contract is a values statement, not an accountability document. The audit includes:
- **Harm enumeration** — concrete harms named per population (primary users, vulnerable subgroups, non-users affected, workers in supply chain), with severity and reversibility
- **Bias audit thresholds** — for any product with ranking/scoring/recommendation: a disparate-impact threshold (example: 0.8, the "four-fifths rule", a rule of thumb from US employment-selection guidelines, not a general industry standard), a subgroup minimum sample size, named proxy variables (zip code, school, browser language), and a model confidence floor. All figures are examples the team replaces with its own
- **Gray-zone register** — use cases not explicitly prohibited but not consented to, with what would have to change before they become acceptable
- **Red lines** — 3–5 concrete refusals at the feature level, each with a named owner with veto authority and a consequence if breached

**Step 5 — Design goal:** Update the design goal so everyone agrees. If there is none, the skill drafts a single statement as a proposal: *"Our ultimate design goal for [product] is to [outcome] for [users], while [ethical commitment]."* *(The sentence template is an edbx addition.)*

**Step 6 — Sign:** Signatures from all participants commit them to the design goal and the objectives. *(edbx additions: a Commitment Risk Register for each objective, with the most likely failure moment, the early warning signal and the protection mechanism, plus contract renewal triggers.)*

---

## The key insight

The Commitment Risk Register, an edbx addition, is what makes this version different from a mission statement. Every team can write inspiring values. Very few teams write down the specific moment they expect to violate those values and what they'll do when that moment arrives.

The register forces that honesty. It says: "Here is when we will be tempted. Here is what temptation will look like. Here is what we have agreed to do instead." That specificity is what makes the commitment survivable under pressure.

---

## How to use it with AI

Describe your product, the key stakeholders involved, any known tensions, and existing ethical concerns. The AI will work through the six steps: the disclaimer and challenge, tension map, recurring themes, responsibilities with red lines, four-part shared objectives, bias & harm audit (with thresholds, gray-zone register, and red lines with named veto owners), design goal, and signatures with a commitment risk register. If you already have an Ethical Disclaimer, paste it in. The output is ready to be reviewed, revised, and signed by the team.

---

## A quick example

**Product:** A consumer lending app that offers short-term loans with tiered interest rates.

**Stakeholder Tension Map (invented example):**
- *Business needs high loan acceptance rates; users need to be protected from loans they can't repay.* These goals are structurally opposed. The business profits from loans; users can be harmed by them.
- *Marketing needs simplified messaging; regulatory compliance needs complete disclosure.* Simplified messaging can obscure costs that users have a legal right to understand.

**One 4-part shared objective (excerpt, invented example):**
- **Action:** We commit to refusing loans our own model assesses as high-risk for default, in order to protect users from preventable financial harm.
- **Quantitative threshold (illustrative):** Default-risk score above 0.65 → automatic decline; manual override requires CRO sign-off plus ethics review.
- **Named owner:** Head of Underwriting.
- **Review cadence:** Pre-launch + every quarterly business review.

**Bias & Harm Audit (excerpt):**
- *Harm enumeration:* "Users in financial precarity may be steered toward higher-tier products by the recommendation algorithm" (severity: high, reversibility: medium).
- *Bias thresholds (illustrative):* Disparate-impact ratio < 0.8 across any zip-code cluster or census tract triggers immediate halt of new loan issuance pending audit. Named proxy variables: zip code, employer name, device model.
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
