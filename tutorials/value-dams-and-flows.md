# Value Dams and Flows

**The short version:** A method for mapping what your stakeholders agree on, what they don't, and why — so you can navigate disagreements rather than pretending they don't exist.

---

## Who made it

Value Dams and Flows is a stakeholder values alignment method developed within ethical design practice to address a specific problem: design teams often know their stakeholders have different values, but lack a structured way to surface those differences, map them, and navigate them.

The dam/flow metaphor comes from hydrology. Value Flows move forward with broad support. Value Dams are blocking forces where stakeholder values conflict — the water isn't destroyed, it's held. The goal of the method is not to remove the dam but to understand it well enough to navigate around it, dissolve the conditions that created it, or respect the legitimate value it's protecting.

---

## The problem it solves

Stakeholder disagreements in design feel personal. Someone is blocking a feature. Someone's being unreasonable. Someone doesn't understand the user needs. Someone is too focused on business metrics.

In reality, these disagreements are almost always values disagreements. The legal team isn't blocking the feature to be difficult — they're protecting the company from regulatory risk. The ethics team isn't asking for slower timelines out of caution — they're protecting users from harm. The business team isn't being cynical — they're operating under real financial constraints.

Value Dams and Flows treats these conflicts as legitimate values disagreements, not personality conflicts. It maps them, names the underlying value each stakeholder is protecting, and generates navigation strategies — including what would have to change in the world for the blocking value to be addressed.

---

## When to use it

- **When a design decision is blocked** — and you want to understand *why* (the value) rather than just *that* (the disagreement)
- **When you're preparing for a stakeholder meeting** — to anticipate where the conflicts will be and how to navigate them
- **When your team can't agree on what to build** — because everyone has different values and nobody has named that explicitly
- **For complex products with multiple stakeholder groups** — the method scales to large, cross-disciplinary teams
- **When you want to find what everyone agrees on** — and start there, rather than starting with the conflicts

---

## What it produces

**Value Dams** — features or policies that the majority of stakeholders want excluded:
- Each dam is classified by strength: **Hard Dam 🔴** (non-negotiable), **Soft Dam 🟡** (negotiable with conditions), **Weak Dam 🟢** (preference, not principle)
- Each dam gets a **Conflict Intensity Score (1–5)**: how strongly do opposing stakeholders feel, multiplied by how structurally embedded is the conflict in the business model? A score of 4–5 signals a dam that can't be dissolved by good facilitation — it requires structural change.
- Each dam gets a **Power Asymmetry analysis**: which stakeholder has the most power to unblock this dam, and what would it cost them (politically, financially, reputationally) to do so?

**Value Flows** — features or policies that the majority of stakeholders support:
- Each flow is classified by strength: **Strong Flow 🟢** (broad consensus), **Conditional Flow 🟡** (with caveats), **Contested Flow 🔴** (minority opposition present)

For every Hard Dam, the method generates:
- A **redesign alternative** that honors the blocking value while preserving the business need
- A **negotiation framing** — how to discuss the trade-off without entrenching positions
- A **"What Would Have to Be True"** counterfactual — what conditions would have to change in the world for the blocking stakeholder to accept the feature?

The **"What Would Have to Be True"** question is the method's most powerful tool. It forces counterfactual thinking that surfaces the real root constraint — often a regulatory interpretation, a technical limitation, or an organizational incentive structure — rather than the surface-level disagreement.

---

## The key insight

Most stakeholder conflicts feel like personality conflicts but are actually structural conflicts. Two stakeholders are not disagreeing because they don't understand each other. They're disagreeing because their organizations have different incentive structures, risk tolerances, or accountability frameworks.

"What Would Have to Be True" surfaces the structural conditions that would need to change — which is the beginning of a real solution, not a negotiation theater.

---

## How to use it with AI

Describe the product or feature space with known or suspected value conflicts. Name the stakeholders involved and any specific disagreements you already know about. The AI will map all dams and flows, rate their strength and conflict intensity, analyze power dynamics, and generate navigation strategies for every hard dam — including redesign alternatives and "What Would Have to Be True" counterfactuals.

---

## A quick example

**Product:** A healthcare app that wants to add an AI-powered symptom checker.

**Dams identified:**

| Feature | Dam Type | Opposing Stakeholder | Underlying Value | Conflict Intensity |
|---|---|---|---|---|
| AI symptom checker with no human review | 🔴 Hard Dam | Medical/Legal | Patient safety, liability | 5 (structurally embedded in medical regulation) |
| Storing symptom data for model improvement | 🟡 Soft Dam | Privacy/Data team | User data minimization | 3 (negotiable with consent framework) |
| Presenting AI confidence percentages to users | 🟢 Weak Dam | UX team | Clear communication | 1 (preference, not principle) |

**For the Hard Dam (AI symptom checker, no human review):**

*Redesign alternative:* AI as triage, not diagnosis. The AI recommends a care pathway (self-care / contact GP / go to A&E) rather than providing a diagnosis or confidence score. Human clinical decision-making is preserved for anything beyond triage.

*"What Would Have to Be True":* This dam dissolves only if a new regulatory framework for AI-assisted diagnosis is established and the AI model achieves clinical-grade accuracy validated by an independent body — neither of which is true today.

**Flows identified:** Personalized medication reminders, appointment booking integration, health record access — all have broad stakeholder support with minor implementation variations.

**Values Balance Statement:** *"This design proceeds with AI triage, appointment booking, and medication support while blocking AI diagnosis, protecting the values of patient safety and clinical accountability."*

---

## See also

- [Values Levers](values-levers.md) — identifies organizational mechanisms to act on the values conflicts that dams surface
- [Ethical Contract](ethical-contract.md) — formalizes the consensus points (flows) and the red lines (hard dams) into a signed commitment
- [Worrystorming](worrystorming.md) — generates worries that can be categorized as dams or flows
