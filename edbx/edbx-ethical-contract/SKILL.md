---
name: edbx-ethical-contract
description: Use when a team wants to formalize shared ethical commitments across disciplines, assign individual ethical responsibilities to specific roles, create a living ethics manifesto for a project, bring new team members into ethical alignment, hold all stakeholders accountable to design ethics, or move from an informal pledge to a signed collective agreement. Facilitate the creation of an Ethical Contract — a signed, shared document that negotiates ethical objectives and responsibilities across all stakeholders in a product team. Trigger this skill for any mention of team ethics agreement, shared ethical responsibility, ethics sign-off, stakeholder ethical alignment, design manifesto, or when someone says "we need everyone on the same page about ethics, not just the design team." Also trigger for "Ethical Contract", "ethics sign-off", "ethical manifesto", "stakeholder ethics", or "team ethics agreement".
version: "1.0"
tags: [ethical-design, alignment]
---

# Ethical Contract

## Overview

Ethical Contract enables your team to negotiate, share, and sign ethical objectives for your product with all stakeholders. It creates a collaborative space that provides a source of good practices, accountability, and a place for all designers to advocate for ethical choices within the product or service.

Every stakeholder has a role in ethical design — business executives, developers, UX/designers, software businesses, and other relevant roles. Ethical Contract enables a shared responsibility to discuss ethical considerations and find a shared ethical foundation. It covers all design responsibilities for each set of contract themes and clearly states ethical responsibilities as part of the alignment cycles of all stakeholders.

The method is Jet Gispen's Ethical Contract (2017), from her *Ethics for Designers* toolkit (ethicsfordesigners.com/ethical-contract). It has **six steps**: **explain the disclaimer to the stakeholders → identify the recurring themes and define each → allocate the unethical situations and responsibilities among the stakeholders → distil three ethical objectives → align everyone on the design goal → sign**. Its input is an **Ethical Disclaimer**, a list of the unethical situations the design could cause, written before the contract (Gispen's separate Ethical Disclaimer tool). The page suggests 30–45 minutes for the session and a team of designers and stakeholders. Gispen's page carries "© Jet Gispen 2017" and states no licence terms, so the steps here are paraphrased. Signing is the last step: signatures create social accountability and signal that everyone has been heard.

> **Mindset check:** The contract is both binding and inspiring. It codifies ethical commitments into shared responsibility — but the design goal statement is the aspirational core that makes people *want* to sign.

## Use This Skill When

- You want to formalize shared ethical commitments across disciplines.
- You need to assign individual ethical responsibilities to specific roles.
- You are creating a living ethics manifesto for a project.
- You are onboarding new team members into ethical alignment.
- You want to hold all stakeholders accountable to design ethics.
- You are moving from an informal pledge to a signed collective agreement.

## Inputs

Provide as many of these as are available:

- An **Ethical Disclaimer**: the team's list of unethical situations its design could cause, ideally per stakeholder. This is the method's input.
- A product or project context with an ethical challenge to address
- A list of stakeholders and their roles (designer, engineer, PM, legal, executive, etc.)
- Optionally: ethical concerns surfaced earlier in any worry, values or pledge session
- Optionally: an existing design goal to update, and existing team values or commitments to formalize
- Optionally: a specific event triggering the contract (new team member, product pivot, ethics incident)

## Workflow

Ethical Contract follows Gispen's six steps. Two further steps (1.5 and 4.5) are edbx additions.

---

### Step 1 — Explain the Ethical Disclaimer

Walk the stakeholders through the Ethical Disclaimer: the unethical situations the design could cause. If the user supplies one, use it. If not, draft the list of situations from the brief, mark it "draft: confirm with the stakeholders", and carry on.

> **edbx adaptation:** the 2–3 sentence ethical challenge statement below is not part of the published method; it condenses the disclaimer into one shared sentence everyone can agree to, and it is what the rest of the contract refers back to.

Generate a clear, shared articulation of the ethical challenge:
- What is the specific ethical tension or risk in this product?
- Why does it require a formal shared commitment?
- What happens if the team doesn't address it?

**Output:** The disclaimer's unethical situations (supplied or drafted), plus a 2–3 sentence ethical challenge statement that all stakeholders can agree on.

---

### Step 1.5 — Stakeholder Tension Map

> **edbx adaptation:** the Tension Map is not part of the published method. A contract that ignores real tensions becomes performative, so this step surfaces where stakeholders' interests structurally conflict before responsibilities are divided.

For each pair of stakeholders with opposing incentives, name the tension explicitly:
> *"[Stakeholder A] needs [X] → [Stakeholder B] needs [Y] → These goals are structurally opposed because [Z]."*

At minimum, surface:
- Business vs. user tension (e.g., "Engagement metrics reward retention → Users benefit from disengagement")
- Short-term vs. long-term tension (e.g., "Q3 growth targets → Long-term trust erosion")
- Role vs. ethics tension (e.g., "Engineer's job is to build what's specified → Ethics requires pushing back on specifications")

**Output:** A Tension Map (2–4 named tensions). Responsibilities and objectives in Steps 3–4 should address these tensions directly — not pretend they don't exist.

---

### Step 2 — Find Recurring Themes and Define Them

Go through the unethical situations, collect the recurring ethical themes (for example fairness, privacy, manipulation, safety), and agree a short definition of each theme for this project, so that everyone means the same thing by it.

**Output:** A short list of themes, each with an agreed one-sentence definition.

---

### Step 3 — Divide Responsibilities

Divide the unethical situations among the stakeholders and add any responsibilities that were missed. For each stakeholder role, define their specific ethical responsibility:

| Stakeholder | Role | Ethical Responsibility |
|---|---|---|
| Designer | UX/Visual | Ensure interfaces do not manipulate users |
| Engineer | Development | Implement only what the contract authorizes |
| Product Manager | Strategy | Align feature roadmap with ethical objectives |
| Legal/Compliance | Risk | Flag regulatory and rights implications |
| Executive/Leadership | Authority | Protect ethical commitments under business pressure |
| User Researcher | Evidence | Surface user concerns that inform ethical decisions |

Generate role-specific responsibility statements for the actual stakeholders provided.

> **edbx adaptation:** Red Line Commitments are not part of the published method. They are here because a responsibility can be deprioritized under pressure and a Red Line cannot be crossed.

**Red Line Commitments (required):** For each stakeholder, name one thing they will NOT do regardless of business pressure.

Example: *"Executive/Leadership Red Line: We will not approve a feature that has been flagged harmful by the ethics review, even if the business case is strong."*

---

### Step 4 — Three Shared Ethical Objectives

Summarise the responsibilities in exactly 3 shared ethical objectives that everyone agrees on and understands. Vague aspirations are not contracts.

> **edbx adaptation:** the four-part form below (action, threshold, owner, cadence) is not part of the published method, which asks only for three agreed objectives. It makes each objective checkable. The numbers in the examples are illustrative only: no source sets them, so the team chooses its own.

**Each objective must include all four parts:**
1. **Action** — *"We commit to [specific ethical action] in order to [protected value/outcome]."*
2. **Quantitative threshold** — a number, percentage, or named standard that would be a breach (illustrative examples: "if the disparate-impact ratio drops below 0.8 across any protected subgroup of n≥30," "if cancellation flow exceeds 3 clicks," "if model confidence drops below 0.7 on production samples")
3. **Named owner** — the role or person accountable for this commitment (not "the team")
4. **Review cadence** — when this is checked (e.g., "every sprint demo," "pre-launch + 30/90/180 days post-launch")

Aspirational verbs without thresholds and owners get rejected. "We will be fair" is not a commitment. "Engineering lead reviews fairness scorecard before every release; release blocks if the agreed disparate-impact ratio is breached on any subgroup above the agreed minimum size" is.

---

### Step 4.5 — Bias & Harm Audit (required before signing)

> **edbx adaptation:** the Bias & Harm Audit is not part of the published method. Without it the contract is a values statement, not an accountability document, so the team completes it before signing.

**A. Harm enumeration (named, not categorized).** List concrete, specific harms this product could cause to specific populations. Do not stop at "users" — name the populations and the specific harm:

| Population (named) | Specific harm | Severity (low / med / high / catastrophic) | Reversibility |
|---|---|---|---|

Include at minimum: primary users, vulnerable subgroups (e.g., minors, neurodivergent, low-income, undocumented, abuse survivors, people in crisis), non-users affected, workers in the supply chain.

**B. Bias audit thresholds.** For any product using ranking, scoring, recommendation, or automated decisioning, define the following. All figures are illustrative examples chosen by the team; none comes from Gispen's method or from a standard for products.

- **Disparate impact threshold**: the ratio at which the team agrees to halt deployment (example: 0.8, the "four-fifths rule", a rule of thumb from US employment-selection guidelines, 29 CFR 1607.4(D), not a general industry standard)
- **Subgroup minimum sample size**: the smallest n the team will accept for a fairness claim (example: n ≥ 30 per subgroup before claiming "no disparate impact")
- **Proxy variables identified and named**: zip code, school name, browser language, device type — anything that could carry protected-class information without naming it
- **Model confidence floor**: below which a decision must escalate to human review (example: 0.7)

**C. Gray-zone register.** Use cases that are not explicitly prohibited but the team has not consented to. List 2–4 such cases and what would have to change before they become acceptable. Example: "Selling aggregated behavior data to third parties — currently not done, would require legal review + user re-consent + ethics review board approval."

**D. Red lines (what we refuse to build, regardless of business pressure).** 3–5 concrete refusals named at feature level, not values level. Example refusals: "We will not build a feature that requires biometric data from users under 16," "We will not implement engagement-driven recommendation in mental-health-related feeds." Each red line includes the **named owner** with veto authority.

This audit becomes a section of the signed contract.

---

### Step 5 — Design Goal

Update the design goal so that all stakeholders agree to it. If the user supplies an existing goal, revise it to reflect the objectives. If there is none, draft one with the template below and mark it as a proposal.

> **edbx adaptation:** the sentence template is not part of the published method; it keeps the goal to one statement that carries its ethical commitment.

*"Our ultimate design goal for [product] is to [outcome] for [users], while [ethical commitment]."*

---

### Step 6 — Sign

Generate the complete Ethical Contract document ready for team review and for everyone to sign, committing to the design goal and the ethical objectives.

---

## Output Format

Open with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title.

### Ethical Contract

**Product:** [name]
**Date:** [date of signing — leave blank when the brief gives none; never invent one]

---

#### Answer

[Two to four sentences: the answer to the question asked (decision, verdict or recommendation) and the main reason.]

#### 1. Ethical Disclaimer and Ethical Challenge

**Unethical situations (the disclaimer):** [supplied by the team, or drafted from the brief and marked "draft: confirm with the stakeholders"]

[2–3 sentence ethical challenge statement]

#### 2. Recurring Themes and Definitions

| Theme | Agreed definition for this project |
|---|---|
| [Theme] | [One-sentence definition] |

#### 3. Stakeholder Responsibilities

| Stakeholder | Role | Ethical Responsibility |
|---|---|---|
| [Name] | [Role] | [Specific responsibility] |

#### 4. Our Main Ethical Objectives

Each objective is a four-part commitment. No part is optional.

| # | Commitment | Quantitative threshold (breach trigger) | Named owner | Review cadence |
|---|---|---|---|---|
| 1 | "We commit to [action] in order to [protected outcome]." | [specific number / standard] | [role/name] | [when checked] |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

#### 5. Bias & Harm Audit

**Harm enumeration table** (from Step 4.5A):

| Population | Specific harm | Severity | Reversibility |
|---|---|---|---|

**Bias audit thresholds** (from Step 4.5B; the figures are illustrative examples):
- Disparate impact threshold: [e.g., halt deployment if ratio < 0.8]
- Subgroup minimum sample size: [e.g., n ≥ 30]
- Named proxy variables to monitor: [list]
- Model confidence floor for auto-decisions: [e.g., 0.7]

**Gray-zone register** (from Step 4.5C):
| Contested use case | What would have to change to allow it |
|---|---|

**Red lines — what we refuse to build** (from Step 4.5D):
1. [Refusal 1] — Owner with veto: [role]
2. [Refusal 2] — Owner with veto: [role]
3. [Refusal 3] — Owner with veto: [role]

#### 6. Our Design Goal

"Our ultimate design goal for [product] is to [outcome] for [users], while [ethical commitment]."

#### 7. Signatures

| Name | Role | Date | Signature |
|---|---|---|---|
| [Name] | [Role] | [Date] | ____________ |

---

> **edbx adaptation:** the Contract Renewal Triggers and the Commitment Risk Register below are not part of the published method. They keep the signed contract from becoming a dead document.

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

Brief session outline for the contract signing (Gispen's page suggests 30–45 minutes for her six steps; the edbx additions take longer):
1. Explain the ethical disclaimer and the challenge statement together
2. Agree the recurring themes and their definitions
3. Divide the situations and discuss stakeholder responsibilities
4. Agree the three ethical objectives
5. Align on the design goal
6. Sign

#### Evidence Ledger
| Claim used as input | Type | Basis |
|---|---|---|
| [figure, rate or fact the output relies on] | [user-supplied / sourced / assumption / unknown] | [the brief / paper or URL / why assumed] |

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

## Guardrails

- Do not write generic responsibilities. Every stakeholder needs a specific ethical duty tied to their role.
- Do not exceed 3 ethical objectives. More than 3 dilutes commitment and makes the contract unwieldy.
- Do not skip the signature section. The signature is what transforms this from a document into a commitment.
- Do not make this a design-team-only exercise. Cross-disciplinary participation is essential.
- Do not treat the contract as punitive. Frame it as a shared foundation, not a compliance mechanism.
- Do not forget renewal triggers. Contracts that are never revisited become dead documents.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

## Deliverable Quality Bar

A strong Ethical Contract output:

- builds on the team's Ethical Disclaimer: the unethical situations it lists, supplied or drafted from the brief and marked as a draft to confirm
- completes all six contract steps (disclaimer, themes, responsibilities, objectives, design goal, signatures), including the Stakeholder Tension Map
- names at least 2 structural stakeholder tensions before assigning responsibilities
- assigns a specific responsibility AND a Red Line to every named stakeholder
- produces exactly 3 shared ethical objectives — each with **all four parts**: action, quantitative threshold (breach trigger), named owner, review cadence. Aspirational verbs without thresholds and owners are rejected.
- completes the Bias & Harm Audit (Step 4.5): a harm enumeration table with named populations and severity, named bias-audit thresholds (disparate impact ratio, subgroup minimum n, proxy variables), a gray-zone register, and 3–5 red lines with named veto owners
- generates a single design goal statement
- includes a Commitment Risk Register with failure moments, early warning signals, and protection mechanisms for every objective
- produces a print/sign-ready document with no placeholders left unfilled
- includes contract renewal triggers
- works for teams from 2 to 20+ stakeholders
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

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
