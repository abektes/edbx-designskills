---
name: edbx-pledge-works
description: Use when a designer, team, or organization wants to articulate concrete ethical commitments for a project, translate vague values into actionable pledges, create role-based or context-specific ethical promises, hold a team accountable to ethical outcomes over time, connect everyday design decisions to larger responsible design goals, or formalize the outputs of other ethical design methods into commitments. Facilitate the writing of design pledges — Simple Pledges and Responsible Stories — that translate ethical intentions into specific, accountable commitments linked to design work. Trigger this skill for any mention of design commitments, ethical pledges, accountability in design, team ethics agreements, responsible design promises, or when someone says "we agreed this matters but we never actually committed to doing anything about it." Also trigger for "Pledge Works", "design pledge", "responsible story", "ethical commitment", or "team values agreement".
version: "1.0"
tags: [ethical-design, alignment]
---

# Pledge Works

## Overview

Pledge Works invites you to support responsible design by writing pledges that link your design work to specific goals. Many practitioners have codes or other tools to guide ethical behavior, but these can be difficult to put into practice in the context of everyday design activity.

Pledge Works bridges the gap between good intentions and everyday product decisions. The published tool describes itself as still under development and seeking wider validation. Pledges can be made at every stage of the design process. They are mechanisms to articulate goals for yourself and your design team — resulting in specific pledges for specific types of work, context-based pledges, or role-based pledges written with a specific employee's professional role in mind. Each pledge written with this skill names a value and a context.

The published implementation cycle has three elements, in this order: **Write pledges in context → Seek better outcomes → Review outcomes together**. It is ongoing, not one-and-done: pledges adapt to the scope of work and change with new learnings. A separate responsible project kickoff, where the team discusses desired outcomes, purpose and values, comes before the first round. This skill's Stage 1 does the kickoff's grounding work; Stages 2 and 3 are the first two elements; the review element is the cadence each pledge carries and the Pledge Register the team brings to it.

> **edbx adaptation:** starting the session with an outcome review, the stage numbering and the tree image (visible outcomes above, structural roots below) are edbx's own; the page orders the cycle write, seek, review and puts the kickoff outside it. They are here to give a one-sitting session a clear order.

> **Mindset check:** A pledge you can never break is not a pledge. Pledges should be specific enough to be falsifiable. In a Responsible Story, the "because" clause names the value and makes the pledge accountable, not just aspirational.

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
- Optionally: a specific stakeholder group to pledge toward (people using the product, people not using it, the planet, clients, or another group the pledge should reach)
- Optionally: a pledge type preference (Simple Pledge, Responsible Story, or To Whom format)

## Workflow

This skill runs in three stages with a structured output phase.

---

### Stage 1 — Outcome Review (project kickoff)

Surface the product's intended and unintended consequences to ground the pledge:

- What is the product intended to do for primary users?
- What unintended consequences might emerge over time?
- What values does the team want to uphold?
- What default outcomes does the team want to challenge?

If outputs from other skills are available (Worrystorming worry clusters, CIDER assumptions, Humane Design Guide flags, Value Dams), import them as pledge anchors.

---

### Stage 2 — Write Pledges in Context

Generate pledges using three formats:

> **edbx adaptation:** the fill-in sentence templates and the per-session minimums below are edbx's; the page gives example pledges and says to use wording natural to the team. They are here so a session produces a usable set quickly.

**Format A: Simple Pledge**
- Company-wide: *"We will [action] to ensure [outcome] for [stakeholder]."*
- Project-level: *"We will [specific technical or design action] to protect [value]."*
- **Minimum:** 3 simple pledges per session

**Format B: Responsible Story**
Structure:
> *"As a [role], we/I pledge to [action] to [outcome/stakeholder] because [reason/value]."*

- The page treats the reason as optional; this skill requires the "because" clause because it names the value or reason, making the pledge accountable and testable against that value
- **Minimum:** 2 responsible stories per session

**Format C: To Whom Pledge**
> *"As a [role], I pledge to [people using the product / people not using it / the planet / clients / another named group]: [pledge text]."*

- Used when the pledge needs to explicitly name a non-obvious stakeholder
- **Minimum:** 1 to-whom pledge per session

---

### Stage 3 — Seek Better Outcomes (operationalize every pledge)

> **edbx adaptation:** the five fields, the early-warning indicator and the stress test below are not part of the published method; the page asks for a pledge checklist that makes clear what upholding each pledge means (usable as acceptance criteria, not set in stone) and for challenging default outcomes with pledges. They are here to make each pledge falsifiable and to show which will bend under pressure. Write the checklist too when the team will track pledges in a backlog.

For each pledge generated, this skill requires the following five fields. A pledge without them is aspiration, not commitment.

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

> **edbx adaptation:** the red-line register is not part of the published method, which has no register of refusals or veto owners. It is here because pledges say what a team will do and a register fixes what it will not, whatever the pressure.

Pledges describe what we will do. A red-line register describes **what we refuse to do, regardless of business pressure**. This is the document with teeth.

Produce 3–5 named refusals, each at the **feature or behavior level**, not the values level. Aspirational refusals ("we will never harm users") are rejected. Concrete refusals are required; the rows below are illustrative, not sourced claims:

| Refusal (named at feature level) | Why it crosses the line | Owner with veto authority | Consequence if attempted |
|---|---|---|---|
| e.g., "We will not build a feature that targets behavioral ads to users under 16." | Developmental vulnerability + GDPR Art. 8 + COPPA + multiple recent enforcement actions. | Head of Product — explicit veto in product council. | PM responsible for proposal is removed; incident logged; board notified. |
| e.g., "We will not implement engagement-driven recommendation in mental-health-related content categories." | Engagement amplification of distressing content has direct documented harm; ethical and legal exposure. | Head of Trust & Safety. | Feature is shut down within 24 hours of detection. |
| e.g., "We will not sell, license, or share precise location data with third parties under any commercial arrangement." | Surveillance harm + recent FTC enforcement against location data brokers. | CEO + DPO joint veto. | Public disclosure required if breached. |

Each red line includes a **named owner with veto authority** (a specific role with the power to block, not just object) and a **consequence if the line is crossed**. A red line without an owner with veto power is a wish.

---

### Stage 3.6 — Pledge-to-Product Traceability (required)

> **edbx adaptation:** the traceability table is not part of the published method, which suggests only keeping pledges visible in the team's backlog or roadmap (for example a "Pledge" label or column). It is here so every pledge can be tested against a real product decision.

Pledges must map to specific product decisions. Produce a traceability table linking each pledge to the **concrete product change** it would or wouldn't trigger:

| Pledge | Specific feature / decision affected | Decision the pledge produces | Decision the pledge prevents |
|---|---|---|---|
| e.g., "We will protect gig worker pay transparency" | Driver dashboard | Show full surge-pricing breakdown including platform fee % | Hide effective hourly rate behind "earnings" label that mixes tips and base |

Every pledge in the Pledge Register gets a row here — the register and this table list the same pledges. If a pledge does not map to at least one concrete feature decision, it is too abstract to be testable: sharpen it until it does, or drop it from the register as well.

---

## Output Format

Open with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title.

### Pledge Works: [Project Name]

Brief framing of the project context and what values/concerns anchor the pledges.

### Answer

[Two to four sentences: the answer to the question asked (decision, verdict or recommendation) and the main reason.]

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

### What We Refuse to Build

| Refusal (named at feature level) | Why it crosses the line | Owner with veto authority | Consequence if attempted |
|---|---|---|---|
| [3–5 refusals] | [reason] | [named role] | [consequence] |

### Pledge-to-Product Traceability

| Pledge | Specific feature / decision affected | Decision the pledge produces | Decision the pledge prevents |
|---|---|---|---|
| [each pledge] | [feature] | [decision] | [decision] |

### Evidence Ledger
| Claim used as input | Type | Basis |
|---|---|---|
| [figure, rate or fact the output relies on] | [user-supplied / sourced / assumption / unknown] | [the brief / paper or URL / why assumed] |

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

## Guardrails

- Do not skip the "because" clause in Responsible Stories. It names the value and makes the pledge accountable.
- Do not write pledges so vague they can never be broken. A pledge you can never break is not a pledge.
- Do not treat the write, seek, review cycle as one-and-done. The Pledge Register is a living document.
- Do not only write affirming pledges. Default-challenging pledges push against business-as-usual — they are where ethical commitment lives.
- Do not limit pledges to the immediate team. The To Whom format reaches beyond primary users to non-obvious stakeholders.
- Do not forget the review cadence. Pledges without review moments are aspirations, not commitments.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.
- Do not stop to ask for more details before answering: draft the full deliverable with unknowns marked, and list the questions worth asking the user at the end.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

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
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

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
