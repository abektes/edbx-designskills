---
name: edbx-pledge-works
description: Use when a designer, team, or organization wants to articulate concrete ethical commitments for a project, translate vague values into actionable pledges, create role-based or context-specific ethical promises, hold a team accountable to ethical outcomes over time, connect everyday design decisions to larger responsible design goals, or formalize the outputs of other ethical design methods into commitments. Facilitate the writing of design pledges — Simple Pledges and Responsible Stories — that translate ethical intentions into specific, accountable commitments linked to design work. Trigger this skill for any mention of design commitments, ethical pledges, accountability in design, team ethics agreements, responsible design promises, or when someone says "we agreed this matters but we never actually committed to doing anything about it." Also trigger for "Pledge Works", "design pledge", "responsible story", "ethical commitment", or "team values agreement".
version: "1.0"
tags: [ethical-design, alignment]
---

# Pledge Works

## Overview

Pledge Works invites you to support responsible design by writing pledges that link your design work to specific goals. Many practitioners have codes or other tools to guide ethical behavior, but these can be difficult to put into practice in the context of everyday design activity.

Pledge Works bridges the gap between good intentions and everyday product decisions. Pledges can be made at every stage of the design process. They are mechanisms to articulate goals for yourself and your design team — resulting in specific pledges for specific types of work, context-based pledges, or role-based pledges written with a specific employee's professional role in mind. Each pledge includes indications of a specific value and context.

The method operates on a three-stage cycle: **Review outcomes together → Write pledges in context → Seek better outcomes**. This cycle is ongoing, not one-and-done. Pledges grow over time like a tree — visible outcomes above, deep structural roots below.

> **Mindset check:** A pledge you can never break is not a pledge. Pledges should be specific enough to be falsifiable. The "because" clause in Responsible Stories names the value and makes the pledge accountable, not just aspirational.

## Use This Skill When

- You want to translate ethical intentions into specific, accountable commitments.
- A team has agreed something matters but hasn't committed to doing anything about it.
- You need role-based or context-specific ethical promises.
- You want to formalize outputs from other ethical design methods (Worrystorming, Value Dams, CIDER, etc.) into binding pledges.
- You are holding a team accountable to ethical outcomes over time.
- You want to connect everyday design decisions to larger responsible design goals.

## Inputs

Provide as many of these as are available:

- A design context, project, or product to write pledges for
- A role or team type (individual designer, cross-functional team, company-wide)
- Optionally: values or ethical concerns surfaced from other methods (Worrystorming, Value Dams, CIDER, etc.)
- Optionally: a specific stakeholder group to pledge toward (users, community, planet, future generations)
- Optionally: a pledge type preference (Simple Pledge, Responsible Story, or To Whom format)

## Workflow

Pledge Works operates in three stages with a structured output phase.

---

### Stage 1 — Review Outcomes Together

Surface the product's intended and unintended consequences to ground the pledge:

- What is the product intended to do for primary users?
- What unintended consequences might emerge over time?
- What values does the team want to uphold?
- What default outcomes does the team want to challenge?

If outputs from other skills are available (Worrystorming worry clusters, CIDER assumptions, Humane Design Guide flags, Value Dams), import them as pledge anchors.

---

### Stage 2 — Write Pledges in Context

Generate pledges using three formats:

**Format A: Simple Pledge**
- Company-wide: *"We will [action] to ensure [outcome] for [stakeholder]."*
- Project-level: *"We will [specific technical or design action] to protect [value]."*
- **Minimum:** 3 simple pledges per session

**Format B: Responsible Story**
Structure:
> *"As a [role], we/I pledge to [action] to [outcome/stakeholder] because [reason/value]."*

- The "because" clause is required — it names the value or reason, making the pledge accountable
- **Minimum:** 2 responsible stories per session

**Format C: To Whom Pledge**
> *"As a [role], I pledge to [the planet / users / future generations / community]: [pledge text]."*

- Used when the pledge needs to explicitly name a non-obvious stakeholder
- **Minimum:** 1 to-whom pledge per session

---

### Stage 3 — Seek Better Outcomes (operationalize every pledge)

For each pledge generated, the following five fields are **required**, not optional. A pledge without them is aspiration, not commitment.

- **Quantitative success indicator** ✅ — a number, percentage, or named standard (not "we'll be more careful"). Example: "Cancellation flow ≤ 3 clicks; cancellation completion rate ≥ 90%."
- **Quantitative failure signal** ⚠️ — the threshold at which the pledge is considered broken. Example: "Disparate-impact ratio < 0.8 on any subgroup with n ≥ 30."
- **Named owner** — a role or person accountable. "The team" is not an owner.
- **Consequence for breach** — what concretely happens if the pledge is broken. Examples: "release blocks; CTO notified," "feature is rolled back within one sprint," "incident is publicly logged in our quarterly responsibility report." Without a consequence, the pledge has no teeth.
- **Review cadence** — when this is checked (every sprint demo, monthly ethics review, pre-launch + 30/90/180 days post-launch).

Flag which pledges are **default-challenging** (pushing against business-as-usual) vs. **affirming** (codifying existing good practice).

**Early Warning Detection:** For each pledge, name the *leading indicator* that the commitment is about to be broken — before it actually breaks. Example: "Failure signal is launching a manipulative feature. Early warning is when leadership asks to skip the ethics review."

**Pledge Stress Test (required for all default-challenging pledges):**
Present each default-challenging pledge against a realistic business pressure scenario: *"Your Q3 growth targets are at risk. Which pledges would leadership be tempted to waive?"* For each at-risk pledge, name one protective mechanism — a process, approval gate, or escalation path that makes waiving the pledge harder than keeping it.

---

### Stage 3.5 — "What We Refuse to Build" Red-Line Register (required)

Pledges describe what we will do. A red-line register describes **what we refuse to do, regardless of business pressure**. This is the document with teeth.

Produce 3–5 named refusals, each at the **feature or behavior level**, not the values level. Aspirational refusals ("we will never harm users") are rejected. Concrete refusals (examples below) are required:

| Refusal (named at feature level) | Why it crosses the line | Owner with veto authority | Consequence if attempted |
|---|---|---|---|
| e.g., "We will not build a feature that targets behavioral ads to users under 16." | Developmental vulnerability + GDPR Art. 8 + COPPA + multiple recent enforcement actions. | Head of Product — explicit veto in product council. | PM responsible for proposal is removed; incident logged; board notified. |
| e.g., "We will not implement engagement-driven recommendation in mental-health-related content categories." | Engagement amplification of distressing content has direct documented harm; ethical and legal exposure. | Head of Trust & Safety. | Feature is shut down within 24 hours of detection. |
| e.g., "We will not sell, license, or share precise location data with third parties under any commercial arrangement." | Surveillance harm + recent FTC enforcement against location data brokers. | CEO + DPO joint veto. | Public disclosure required if breached. |

Each red line includes a **named owner with veto authority** (a specific role with the power to block, not just object) and a **consequence if the line is crossed**. A red line without an owner with veto power is a wish.

---

### Stage 3.6 — Pledge-to-Product Traceability (required)

Pledges must map to specific product decisions. Produce a traceability table linking each pledge to the **concrete product change** it would or wouldn't trigger:

| Pledge | Specific feature / decision affected | Decision the pledge produces | Decision the pledge prevents |
|---|---|---|---|
| e.g., "We will protect gig worker pay transparency" | Driver dashboard | Show full surge-pricing breakdown including platform fee % | Hide effective hourly rate behind "earnings" label that mixes tips and base |

If a pledge does not map to at least one concrete feature decision, it is too abstract to be testable. Either sharpen it or drop it.

---

## Output Format

### Pledge Works: [Project Name]

Brief framing of the project context and what values/concerns anchor the pledges.

### Stage 1 — Outcome Review
- Intended outcomes: [list]
- Unintended risks: [list]
- Values to protect: [list]
- Defaults to challenge: [list]

### Simple Pledges

1. "We will [action] to ensure [outcome] for [stakeholder]."
2. "We will [action] to protect [value]."
3. "We will [action] to ensure [outcome]."

### Responsible Stories

> As a [role], we pledge to [action] to [outcome] because [reason/value].

> As a [role], I pledge to [action] to [outcome] because [reason/value].

### To Whom Pledge

> As a [role], I pledge to [stakeholder]: [pledge text].

### Pledge Register

| Pledge | Type | Stakeholder | Value | Review Moment | Default-Challenging? | Owner |
|---|---|---|---|---|---|---|
| [Pledge 1] | Simple | [stakeholder] | [value] | [when] | Yes/No | [name] |
| [Pledge 2] | Responsible Story | [stakeholder] | [value] | [when] | Yes/No | [name] |

### Success Indicators ✅ & Failure Signals ⚠️

Per pledge: what tells you it's being kept vs. broken.

## Guardrails

- Do not skip the "because" clause in Responsible Stories. It names the value and makes the pledge accountable.
- Do not write pledges so vague they can never be broken. A pledge you can never break is not a pledge.
- Do not treat the three-stage cycle as one-and-done. The Pledge Register is a living document.
- Do not only write affirming pledges. Default-challenging pledges push against business-as-usual — they are where ethical commitment lives.
- Do not limit pledges to the immediate team. The To Whom format reaches beyond primary users to non-obvious stakeholders.
- Do not forget the review cadence. Pledges without review moments are aspirations, not commitments.

## Deliverable Quality Bar

A strong Pledge Works output:

- produces minimum 6 pledges (3 Simple + 2 Responsible Stories + 1 To Whom)
- every Responsible Story includes a "because" clause naming a value
- **every pledge has all five operationalization fields**: quantitative success indicator (with number/threshold), quantitative failure signal (with breach threshold), named owner (role/person, not "the team"), consequence for breach, and review cadence. Pledges missing any field are aspirations, not commitments.
- every default-challenging pledge has an early warning indicator distinct from the failure signal
- every default-challenging pledge has a stress test result and a named protective mechanism
- **produces a "What We Refuse to Build" red-line register** with 3–5 concrete feature-level refusals, each with a named owner with veto authority and a consequence for breach
- **produces a Pledge-to-Product traceability table** mapping each pledge to a specific product decision it would or wouldn't trigger; pledges that don't map to a feature decision are sharpened or dropped
- a Pledge Register is produced for ongoing maintenance
- accepts outputs from any other skill in the set as pledge anchors
- works at individual, team, and org-wide scope
- identifies which pledges are default-challenging vs. merely affirming

## Integration with Other EDBX Skills

- **edbx-worrystorming** surfaces ethical concerns. Pledge Works converts critical worry clusters into binding pledges.
- **edbx-cider** surfaces exclusionary assumptions. Pledge Works commits the team to eliminating them.
- **edbx-humane-design-guide** flags sensitivity exploitation. Pledge Works creates accountability to address each flag.
- **edbx-anotherlens** surfaces individual bias. Pledge Works externalizes personal commitments into team agreements.
- **edbx-responsible-design-prism** diagnoses current position. Pledge Works commits to moving toward responsible design.

## Hashtags

#alignmyteam #designresponsibility

## See Also

- Hippocratic Oath
- Ethical Contract
