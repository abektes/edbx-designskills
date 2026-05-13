---
name: edbx-value-dams-and-flows
description: Use when a designer or team needs to identify features that stakeholders are strongly opposed to, map the difference between what stakeholders block vs. support, balance competing disciplinary, human, and business values, navigate organizational policy conflicts, or facilitate a structured trade-off discussion. Apply the Value Dams and Flows method to map stakeholder value conflicts and consensuses in a design space, identifying which features or policies are blocked (dams) versus which can move forward (flows), and generating strategies to navigate the trade-offs. Trigger this skill for any mention of value trade-offs, stakeholder disagreement on features, blocked design decisions, competing values in a product, balancing business vs. user values, or when someone says "we can't agree on what to build because everyone has different values." Also trigger for "Value Dams and Flows", "value trade-offs", "stakeholder values", "blocked features", or "competing values".
version: "1.0"
tags: [ethical-design, alignment]
---

# Value Dams and Flows

## Overview

Value Dams and Flows help you generate features that are strongly opposed and design indicated for as a way to navigate and balance values. These trade-offs require attention to balance disciplinary, human, and business values whose trade-offs are inevitable, as there are multiple outcomes of products.

**Value Dams** are technical features or organizational policies that the majority of stakeholders would like to be excluded from the overall system, even if the features are not absolutely necessary for success or appropriation. Dams are blocking forces where stakeholder values conflict — the "Dam of Disagreement."

**Value Flows** are technical features or organizational policies that the majority of stakeholders support. Flows are the moving forces where values can proceed — the "Flow of Consensus."

The method operates at the intersection of stakeholder management and values ethics. It is explicitly a team alignment tool — the `#alignmyteam` hashtag signals its purpose. The dam/flow metaphor makes abstract value conflicts feel concrete and navigable: a dam doesn't destroy water, it redirects or holds it until the underlying concern is addressed.

> **Mindset check:** Dams are not villains — they are protecting legitimate values. The goal is navigation, not elimination. Even Hard Dams represent real values that deserve respect.

## Use This Skill When

- You need to identify features that stakeholders are strongly opposed to.
- You want to map the difference between what stakeholders block vs. support.
- You are balancing competing disciplinary, human, and business values.
- You need to navigate organizational policy conflicts.
- You are facilitating a structured trade-off discussion.
- You cannot agree on what to build because everyone has different values.

## Inputs

Provide as many of these as are available:

- A product, feature set, or design space with known or suspected value conflicts
- A list of stakeholder types involved (e.g., users, engineers, legal, business, community)
- Optionally: a specific feature or policy that is blocked or contested
- Optionally: a known disagreement between stakeholder groups
- Optionally: the organizational context (startup, enterprise, public sector, etc.)

## Workflow

Value Dams and Flows follows five steps.

---

### Step 1 — Identify Value Dams

Value Dams = features or policies that the **majority of stakeholders want excluded** from the system.

For each identified dam:
- Name the feature or policy
- Identify which stakeholders oppose it and why
- Name the underlying value being protected
- Rate the dam strength: `🔴 Hard Dam` (non-negotiable) / `🟡 Soft Dam` (negotiable with conditions) / `🟢 Weak Dam` (preference, not principle)
- **Conflict Intensity Score (1–5):** Rate: (How strongly do opposing stakeholders feel about this?) × (How structurally embedded is the conflict in the business model?). A score of 4–5 signals a dam that cannot be dissolved by good facilitation — it requires a change in incentive structure, ownership, or governance. Raw stakeholder analysis identifies conflict; this score distinguishes negotiable friction from structural incompatibility.
- **Power Asymmetry:** Identify which stakeholder has the most power to unblock this dam, and what it would cost them (politically, financially, reputationally) to do so.

---

### Step 2 — Identify Value Flows

Value Flows = features or policies that the **majority of stakeholders support**.

For each identified flow:
- Name the feature or policy
- Identify which stakeholders support it and why
- Name the underlying value being served
- Rate flow strength: `🟢 Strong Flow` (broad consensus) / `🟡 Conditional Flow` (consensus with caveats) / `🔴 Contested Flow` (minority opposition present)

---

### Step 3 — Map the Dam-Flow Landscape

Produce a structured map:

| Feature/Policy | Dam or Flow | Stakeholders Opposed | Stakeholders Supporting | Underlying Value | Strength |
|---|---|---|---|---|---|
| [Example] | DAM | [who opposes] | [who supports] | [value] | 🔴/🟡/🟢 |

---

### Step 4 — Navigate the Trade-Offs

For each **Hard Dam**, generate:
- A **redesign alternative** that honors the blocking value while preserving the business need
- A **negotiation framing**: how to discuss this trade-off without entrenching positions
- A **minimum viable ethics** position: what is the least the team must do to respect the blocking value?
- **"What Would Have to Be True":** State the conditions under which this dam would dissolve — not what the team should do, but what would have to change in the world for the stakeholder opposing this feature to accept it. This forces counterfactual thinking that surfaces root constraints raw analysis skips (e.g., "This dam dissolves only if legal counsel changes their interpretation of GDPR Art. 22, which would require a change in our data processing agreement").

For **Soft Dams**, generate:
- The **conditions under which the dam dissolves** (e.g., "acceptable if opt-in rather than default")

For **Contested Flows**, generate:
- The **minority concern** that must be addressed before proceeding
- A **safeguard** that protects the minority without blocking the majority

---

## Output Format

### Value Dams and Flows: [Product/Feature Space]

### Dam-Flow Map

| Feature/Policy | Dam or Flow | Stakeholders Opposed | Stakeholders Supporting | Underlying Value | Strength | Conflict Intensity (1–5) | Power to Unblock |
|---|---|---|---|---|---|---|---|
| [Feature 1] | DAM | [opposed] | [supporting] | [value] | 🔴 Hard / 🟡 Soft / 🟢 Weak | [score] | [who + what it costs them] |
| [Feature 2] | FLOW | [opposed] | [supporting] | [value] | 🟢 Strong / 🟡 Conditional / 🔴 Contested | — | — |

### Trade-Off Navigation

**[Hard Dam name]:**
- Redesign alternative: [option that honors blocking value]
- Negotiation framing: [how to discuss]
- Minimum viable ethics: [floor position]

**[Soft Dam name]:**
- Dissolving condition: [what makes it acceptable]

**[Contested Flow name]:**
- Minority concern: [what must be addressed]
- Safeguard: [protection for minority]

### Values Balance Statement

*"This design proceeds with [Flows] while blocking [Dams], protecting the values of [X] and [Y]."*

### Facilitation Agenda (Optional)

Session outline for stakeholder values alignment meeting:
1. Surface all features/policies under consideration
2. Map Dam and Flow positions per stakeholder group
3. Discuss Hard Dams — redesign alternatives
4. Address Contested Flows — minority safeguards
5. Align on Values Balance Statement

## Guardrails

- Do not treat majority consensus as automatically ethical. Minority values matter — that's what Contested Flows are for.
- Do not eliminate dams. The goal is navigation, not removal. Dams protect real values.
- Do not skip naming the underlying value. "Stakeholder concerns" is not specific enough.
- Do not forget Soft Dams. They are negotiable but still represent real values.
- Do not treat "minimum viable ethics" as the goal — it is the floor, not the ceiling.
- Do not make the facilitation agenda optional if there are Hard Dams. Real conflicts require real conversation.

## Deliverable Quality Bar

A strong Value Dams and Flows output:

- classifies all features/policies as Dams or Flows with strength ratings
- names underlying values explicitly for every Dam and Flow
- assigns a Conflict Intensity Score (1–5) to every Dam
- identifies which stakeholder has the power to unblock each Dam and what it would cost them
- provides a redesign alternative, negotiation framing, and "What Would Have to Be True" statement for every Hard Dam
- provides a minority concern and safeguard for every Contested Flow
- produces a Values Balance Statement every session
- is usable as a stakeholder meeting agenda

## Integration with Other EDBX Skills

- **edbx-worrystorming** generates worries. Value Dams and Flows maps which worries are blocking (dams) vs. manageable (flows).
- **edbx-responsible-design-prism** places the design on the ethical spectrum. Dams and Flows explains *why* it's stuck there.
- **edbx-motivation-matrix** maps user motivation. Dams and Flows maps *stakeholder* value positions.
- **edbx-cider** surfaces exclusionary assumptions. Dams and Flows shows whose values are creating the dam.

## Hashtags

#breakmydesign #identifyvalues #alignmyteam

## See Also

- Values Levers
- Maslow Mirrored
- Dichotomy Mapping
