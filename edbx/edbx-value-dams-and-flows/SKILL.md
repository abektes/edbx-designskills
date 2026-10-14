---
name: edbx-value-dams-and-flows
description: Use when a designer or team needs to identify features that stakeholders are strongly opposed to, map the difference between what stakeholders block vs. support, balance competing disciplinary, human, and business values, navigate organizational policy conflicts, or facilitate a structured trade-off discussion. Apply the Value Dams and Flows method to map stakeholder value conflicts and consensuses in a design space, identifying which features or policies are blocked (dams) versus which can move forward (flows), and generating strategies to navigate the trade-offs. Trigger this skill for any mention of value trade-offs, stakeholder disagreement on features, blocked design decisions, competing values in a product, balancing business vs. user values, or when someone says "we can't agree on what to build because everyone has different values." Also trigger for "Value Dams and Flows", "value trade-offs", "stakeholder values", "blocked features", or "competing values".
version: "1.0"
tags: [ethical-design, alignment]
---

# Value Dams and Flows

## Overview

Value Dams and Flows help you generate features that are strongly opposed and design indicated for as a way to navigate and balance values. These trade-offs require attention to balance disciplinary, human, and business values whose trade-offs are inevitable, as there are multiple outcomes of products.

The method comes from the Value Sensitive Design literature: Miller, Friedman, Jancke and Gill (2007), "Value tensions in design", ACM GROUP '07, which presents Dams and Flows as a method. Friedman, Hendry and Borning's 2017 survey of Value Sensitive Design methods and Friedman and Hendry's 2019 book are cited as describing it. The 2007 paper and those two texts were not read when this skill was checked, so the definitions below are this skill's working definitions, not quotations of the method.

**Value Dams**, in this skill, are technical features or organizational policies that the majority of stakeholders would like to be excluded from the overall system, even if the features are not absolutely necessary for success or appropriation. Dams are blocking forces where stakeholder values conflict — this skill calls this the "Dam of Disagreement."

**Value Flows**, in this skill, are technical features or organizational policies that the majority of stakeholders support. Flows are the moving forces where values can proceed — this skill calls this the "Flow of Consensus."

> **edbx adaptation:** the dam and flow definitions above are unconfirmed against the primary paper. The one secondary description found reads differently: options that even a small share of stakeholders strongly object to are removed from the design space, and among the options left, those a substantial share of stakeholders find appealing are emphasised. Check the 2007 paper before quoting a definition as the method's. The names "Dam of Disagreement" and "Flow of Consensus" and the overview wording are not confirmed in any readable source.

This skill uses the method as a team alignment tool. The dam/flow metaphor makes abstract value conflicts feel concrete and navigable: a dam doesn't destroy water, it redirects or holds it until the underlying concern is addressed.

> **Mindset check:** Dams are not villains — they are protecting legitimate values. The goal is navigation, not elimination. Even Hard Dams represent real values that deserve respect.

> **edbx adaptation:** the mindset check and the navigation-not-elimination stance are this skill's own; the secondary description above speaks of removing dam options from the design space.

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

Value Dams and Flows follows four steps here.

> **edbx adaptation:** the dam strength ratings (Hard / Soft / Weak), the Conflict Intensity Score, Power Asymmetry, the flow strength ratings, the Dam-Flow Map layout, the redesign alternative, negotiation framing, "minimum viable ethics" floor and "What Would Have to Be True" statement, the Values Balance Statement and the facilitation agenda are not part of the published method, as far as could be checked. The sources found describe a two-step filter: dams out first, then flows among what remains. These additions are here so that a blocked decision ends in something a team can negotiate.

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

> **edbx adaptation:** the Contested Flow tier (and the Strong / Conditional scale) is not part of the published method, and no readable source supports it. Where dams are applied first, a feature with strong minority opposition would already be a dam; in this skill a Contested Flow is one that most stakeholders support but some oppose less than strongly enough to make it a dam. It is here so minority concerns are named and safeguarded, not lost.

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

Open with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title.

### Value Dams and Flows: [Product/Feature Space]

### Answer

[Two to four sentences: the answer to the question asked (decision, verdict or recommendation) and the main reason.]

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

### Evidence Ledger
| Claim used as input | Type | Basis |
|---|---|---|
| [figure, rate or fact the output relies on] | [user-supplied / sourced / assumption / unknown] | [the brief / paper or URL / why assumed] |

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

## Guardrails

- Do not treat majority consensus as automatically ethical. Minority values matter — that's what Contested Flows are for.
- Do not eliminate dams. The goal is navigation, not removal. Dams protect real values.
- Do not skip naming the underlying value. "Stakeholder concerns" is not specific enough.
- Do not forget Soft Dams. They are negotiable but still represent real values.
- Do not treat "minimum viable ethics" as the goal — it is the floor, not the ceiling.
- Do not make the facilitation agenda optional if there are Hard Dams. Real conflicts require real conversation.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

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
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

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
