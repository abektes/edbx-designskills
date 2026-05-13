---
name: edbx-ethical-contract
description: Use when a team wants to formalize shared ethical commitments across disciplines, assign individual ethical responsibilities to specific roles, create a living ethics manifesto for a project, bring new team members into ethical alignment, hold all stakeholders accountable to design ethics, or escalate from informal pledges to a signed collective agreement. Facilitate the creation of an Ethical Contract — a signed, shared document that negotiates ethical objectives and responsibilities across all stakeholders in a product team. Trigger this skill for any mention of team ethics agreement, shared ethical responsibility, ethics sign-off, stakeholder ethical alignment, design manifesto, or when someone says "we need everyone on the same page about ethics, not just the design team." Also trigger for "Ethical Contract", "ethics sign-off", "ethical manifesto", "stakeholder ethics", or "team ethics agreement".
version: "1.0"
tags: [ethical-design, alignment]
---

# Ethical Contract

## Overview

Ethical Contract enables your team to negotiate, share, and sign ethical objectives for your product with all stakeholders. It creates a collaborative space that provides a source of good practices, accountability, and a place for all designers to advocate for ethical choices within the product or service.

Every stakeholder has a role in ethical design — business executives, developers, UX/designers, software businesses, and other relevant roles. Ethical Contract enables a shared responsibility to discuss ethical considerations and find a shared ethical foundation. It covers all design responsibilities for each set of contract themes and clearly states ethical responsibilities as part of the alignment cycles of all stakeholders.

The contract follows a five-step process: **Explain the ethical challenge → Define responsibilities → State shared ethical objectives → Name the design goal → Collect signatures**. The signature requirement is what makes this distinct from informal pledges — signatures create social accountability and signal that everyone has been heard.

> **Mindset check:** The contract is both binding and inspiring. It codifies ethical commitments into shared responsibility — but the design goal statement is the aspirational core that makes people *want* to sign.

## Use This Skill When

- You want to formalize shared ethical commitments across disciplines.
- You need to assign individual ethical responsibilities to specific roles.
- You are creating a living ethics manifesto for a project.
- You are onboarding new team members into ethical alignment.
- You want to hold all stakeholders accountable to design ethics.
- You are escalating from informal pledges (Pledge Works) to a signed collective agreement.

## Inputs

Provide as many of these as are available:

- A product or project context with an ethical challenge to address
- A list of stakeholders and their roles (designer, engineer, PM, legal, executive, etc.)
- Optionally: ethical concerns surfaced from prior methods (Worrystorming, Value Dams, Pledge Works)
- Optionally: existing team values or commitments to formalize
- Optionally: a specific event triggering the contract (new team member, product pivot, ethics incident)

## Workflow

Ethical Contract follows five steps.

---

### Step 1 — Explain the Ethical Challenge

Generate a clear, shared articulation of the ethical challenge:
- What is the specific ethical tension or risk in this product?
- Why does it require a formal shared commitment?
- What happens if the team doesn't address it?

**Output:** A 2–3 sentence ethical challenge statement that all stakeholders can agree on.

---

### Step 1.5 — Stakeholder Tension Map

Before assigning responsibilities, surface where stakeholders' interests structurally conflict. A contract that ignores real tensions becomes performative.

For each pair of stakeholders with opposing incentives, name the tension explicitly:
> *"[Stakeholder A] needs [X] → [Stakeholder B] needs [Y] → These goals are structurally opposed because [Z]."*

At minimum, surface:
- Business vs. user tension (e.g., "Engagement metrics reward retention → Users benefit from disengagement")
- Short-term vs. long-term tension (e.g., "Q3 growth targets → Long-term trust erosion")
- Role vs. ethics tension (e.g., "Engineer's job is to build what's specified → Ethics requires pushing back on specifications")

**Output:** A Tension Map (2–4 named tensions). Responsibilities and objectives in Steps 2–3 should address these tensions directly — not pretend they don't exist.

---

### Step 2 — Define Responsibilities

For each stakeholder role, define their specific ethical responsibility:

| Stakeholder | Role | Ethical Responsibility |
|---|---|---|
| Designer | UX/Visual | Ensure interfaces do not manipulate users |
| Engineer | Development | Implement only what the contract authorizes |
| Product Manager | Strategy | Align feature roadmap with ethical objectives |
| Legal/Compliance | Risk | Flag regulatory and rights implications |
| Executive/Leadership | Authority | Protect ethical commitments under business pressure |
| User Researcher | Evidence | Surface user concerns that inform ethical decisions |

Generate role-specific responsibility statements for the actual stakeholders provided.

**Red Line Commitments (required):** For each stakeholder, name one thing they will NOT do regardless of business pressure. Red Lines are stronger than responsibilities — a responsibility can be deprioritized, a Red Line cannot be crossed.

Example: *"Executive/Leadership Red Line: We will not approve a feature that has been flagged harmful by the ethics review, even if the business case is strong."*

---

### Step 3 — Shared Ethical Objectives

Generate 3 shared ethical objectives — specific, measurable, and agreed-upon. Vague aspirations are not contracts.

**Each objective must include all four parts:**
1. **Action** — *"We commit to [specific ethical action] in order to [protected value/outcome]."*
2. **Quantitative threshold** — a number, percentage, or named standard that would be a breach (e.g., "if disparate-impact ratio drops below 0.8 across any protected subgroup of n≥30," "if cancellation flow exceeds 3 clicks," "if model confidence drops below 0.7 on production samples")
3. **Named owner** — the role or person accountable for this commitment (not "the team")
4. **Review cadence** — when this is checked (e.g., "every sprint demo," "pre-launch + 30/90/180 days post-launch")

Aspirational verbs without thresholds and owners get rejected. "We will be fair" is not a commitment. "Engineering lead reviews fairness scorecard before every release; release blocks if disparate-impact ratio < 0.8 on any subgroup with n ≥ 30" is.

---

### Step 3.5 — Bias & Harm Audit (required before signing)

Before any contract is signed, the team must complete a structured bias and harm audit. Without this step, the contract is a values statement, not an accountability document.

**A. Harm enumeration (named, not categorized).** List concrete, specific harms this product could cause to specific populations. Do not stop at "users" — name the populations and the specific harm:

| Population (named) | Specific harm | Severity (low / med / high / catastrophic) | Reversibility |
|---|---|---|---|

Include at minimum: primary users, vulnerable subgroups (e.g., minors, neurodivergent, low-income, undocumented, abuse survivors, people in crisis), non-users affected, workers in the supply chain.

**B. Bias audit thresholds.** For any product using ranking, scoring, recommendation, or automated decisioning, define:

- **Disparate impact threshold**: the ratio at which the team agrees to halt deployment (industry standard floor: 0.8 / "four-fifths rule")
- **Subgroup minimum sample size**: the smallest n the team will accept for a fairness claim (e.g., n ≥ 30 per subgroup before claiming "no disparate impact")
- **Proxy variables identified and named**: zip code, school name, browser language, device type — anything that could carry protected-class information without naming it
- **Model confidence floor**: below which a decision must escalate to human review

**C. Gray-zone register.** Use cases that are not explicitly prohibited but the team has not consented to. List 2–4 such cases and what would have to change before they become acceptable. Example: "Selling aggregated behavior data to third parties — currently not done, would require legal review + user re-consent + ethics review board approval."

**D. Red lines (what we refuse to build, regardless of business pressure).** 3–5 concrete refusals named at feature level, not values level. Example refusals: "We will not build a feature that requires biometric data from users under 16," "We will not implement engagement-driven recommendation in mental-health-related feeds." Each red line includes the **named owner** with veto authority.

This audit becomes Section 4 of the signed contract.

---

### Step 4 — Ultimate Design Goal

Generate a single unifying design goal statement:

*"Our ultimate design goal for [product] is to [outcome] for [users], while [ethical commitment]."*

---

### Step 5 — Produce Signable Contract

Generate the complete Ethical Contract document ready for team review and signature.

---

## Output Format

### Ethical Contract

**Product:** [name]
**Date:** [date]

---

#### 1. Ethical Challenge

[2–3 sentence statement]

#### 2. Stakeholder Responsibilities

| Stakeholder | Role | Ethical Responsibility |
|---|---|---|
| [Name] | [Role] | [Specific responsibility] |

#### 3. Our Main Ethical Objectives

Each objective is a four-part commitment. No part is optional.

| # | Commitment | Quantitative threshold (breach trigger) | Named owner | Review cadence |
|---|---|---|---|---|
| 1 | "We commit to [action] in order to [protected outcome]." | [specific number / standard] | [role/name] | [when checked] |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

#### 4. Bias & Harm Audit

**Harm enumeration table** (from Step 3.5A):

| Population | Specific harm | Severity | Reversibility |
|---|---|---|---|

**Bias audit thresholds** (from Step 3.5B):
- Disparate impact threshold: [e.g., halt deployment if ratio < 0.8]
- Subgroup minimum sample size: [e.g., n ≥ 30]
- Named proxy variables to monitor: [list]
- Model confidence floor for auto-decisions: [e.g., 0.7]

**Gray-zone register** (from Step 3.5C):
| Contested use case | What would have to change to allow it |
|---|---|

**Red lines — what we refuse to build** (from Step 3.5D):
1. [Refusal 1] — Owner with veto: [role]
2. [Refusal 2] — Owner with veto: [role]
3. [Refusal 3] — Owner with veto: [role]

#### 5. Our Design Goal

"Our ultimate design goal for [product] is to [outcome] for [users], while [ethical commitment]."

#### 6. Signatures

| Name | Role | Date | Signature |
|---|---|---|---|
| [Name] | [Role] | [Date] | ____________ |

---

### Contract Renewal Triggers

This contract should be revisited when:
- [Trigger 1: e.g., major feature launch]
- [Trigger 2: e.g., new stakeholder joins]
- [Trigger 3: e.g., ethics incident]

### Commitment Risk Register

For each shared ethical objective, identify the most likely moment it breaks and what would stop it:

| Objective | Likely Failure Moment | Early Warning Signal | Protection Mechanism |
|---|---|---|---|
| [Objective 1] | [when in project lifecycle] | [observable signal before breaking] | [gate/review/escalation path] |
| [Objective 2] | [when] | [signal] | [mechanism] |
| [Objective 3] | [when] | [signal] | [mechanism] |

### Facilitation Guide

Brief session outline for the contract signing:
1. Read the ethical challenge statement together
2. Review and discuss stakeholder responsibilities
3. Refine ethical objectives as a group
4. Align on the design goal
5. Sign

## Guardrails

- Do not write generic responsibilities. Every stakeholder needs a specific ethical duty tied to their role.
- Do not exceed 3 ethical objectives. More than 3 dilutes commitment and makes the contract unwieldy.
- Do not skip the signature section. The signature is what transforms this from a document into a commitment.
- Do not make this a design-team-only exercise. Cross-disciplinary participation is essential.
- Do not treat the contract as punitive. Frame it as a shared foundation, not a compliance mechanism.
- Do not forget renewal triggers. Contracts that are never revisited become dead documents.

## Deliverable Quality Bar

A strong Ethical Contract output:

- completes all contract steps including the Stakeholder Tension Map
- names at least 2 structural stakeholder tensions before assigning responsibilities
- assigns a specific responsibility AND a Red Line to every named stakeholder
- produces exactly 3 shared ethical objectives — each with **all four parts**: action, quantitative threshold (breach trigger), named owner, review cadence. Aspirational verbs without thresholds and owners are rejected.
- completes the Bias & Harm Audit (Step 3.5): a harm enumeration table with named populations and severity, named bias-audit thresholds (disparate impact ratio, subgroup minimum n, proxy variables), a gray-zone register, and 3–5 red lines with named veto owners
- generates a single design goal statement
- includes a Commitment Risk Register with failure moments, early warning signals, and protection mechanisms for every objective
- produces a print/sign-ready document with no placeholders left unfilled
- includes contract renewal triggers
- works for teams from 2 to 20+ stakeholders

## Integration with Other EDBX Skills

- **edbx-worrystorming** surfaces ethical concerns. Ethical Contract converts the most critical concerns into shared responsibilities.
- **edbx-anotherlens** surfaces individual bias. Ethical Contract aligns those individual perspectives into collective obligations.
- **edbx-cider** surfaces exclusionary assumptions. Ethical Contract assigns responsibility for eliminating them.
- **edbx-humane-design-guide** flags sensitivity exploitation. Ethical Contract makes specific stakeholders accountable for addressing each flag.

## Hashtags

#identifyvalues #alignmyteam

## See Also

- Ethical Disclaimer
- Pledge Works
