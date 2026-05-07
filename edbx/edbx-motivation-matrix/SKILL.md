---
name: edbx-motivation-matrix
description: Use when a designer or researcher wants to audit a product for manipulative patterns, map user motivations across different contexts, generate ethical design criteria, evaluate products against motivational incentives, or identify dark patterns in behavioral design. Apply the Motivation Matrix method to analyze how different user motivations — Achievement, Social Acceptance, Fear, Power, and Incentive — interact with product or service contexts. Trigger this skill for any mention of motivation mapping, ethical auditing of a product, dark patterns analysis, designing for diverse user contexts, behavioral design ethics, or when someone asks "are we manipulating users?" Also trigger for "motivation matrix", "user motivation", "behavioral design", "manipulative patterns", or "what motivates our users".
metadata:
  version: "1.0"
---

# Motivation Matrix

## Overview

The Motivation Matrix maps how a product or service leverages five core user motivations across different users and contexts. It exposes where design choices exploit, nudge, or support those motivations — and where the line between helpful and manipulative gets blurry.

**Formula:** MOTIVATION TYPE × USE @ CONTEXT = MOTIVATION MATRIX

Rows are motivation types. Columns are users in specific contexts. Each cell contains a [Motivation] + [Action] statement that describes what the design is doing to that user's motivation in that situation.

The matrix is deliberately provocative. It surfaces uncomfortable truths about how products tap into human drives. That discomfort is the point — it creates the conditions for better design decisions.

> **Intent check:** This is a facilitation tool, not a moral verdict. A flagged cell does not mean the product is evil. It means the design team should look at that cell carefully and decide whether they are comfortable with what they find.

## Use This Skill When

- You want to audit a product for manipulative motivational patterns.
- You need to map how different user groups experience motivational pressure differently.
- You suspect a product leverages fear, social pressure, or extrinsic incentives in ways that may harm users.
- You want ethical design criteria grounded in how motivations actually work in your product.
- You ask "are we manipulating users?" and want an honest, structured answer.
- You are designing for diverse user contexts and need to check whose motivations are being served — and whose are being exploited.

## Inputs

Collect these before generating the matrix:

- **Product or service name** and a brief description of what it does.
- **Target users and contexts** — at least two distinct combinations (e.g., "new user onboarding" vs. "power user daily routine", or "teenager at home" vs. "professional at work"). More columns yield richer analysis.
- **Focus question** — what specifically you want to understand (e.g., "Where might our onboarding flow be pressuring users?" or "Is our gamification serving users or exploiting them?").

If context is ambiguous, ask clarifying questions before generating the matrix. The quality of the output depends on the specificity of the inputs.

## The Five Motivation Types

| Type | Core drive | What it looks like in design |
|---|---|---|
| Achievement | Progress, mastery, completion | Progress bars, badges, streaks, levels, completion metrics |
| Social Acceptance | Belonging, approval, status | Likes, shares, follower counts, social proof, FOMO indicators |
| Fear | Avoiding loss, missing out, being left behind | Warnings, countdowns, loss aversion framing, threat language |
| Power | Control, influence, dominance | Leaderboards, admin roles, exclusive access, competitive rankings |
| Incentive | Extrinsic reward, gain | Discounts, points, cashback, referral bonuses, free trials |

Full definitions with examples are in `references/motivation-types.md`.

## Workflow

### Step 1 — Intake

Gather the product description, user-context combinations, and focus question. If the user provides only one context, suggest at least one more — the matrix is most useful when contrasting different situations. Consider including:

- A primary user in an ideal context
- A primary user in a stressed or vulnerable context
- A secondary user or non-user affected by the product

Why: Single-context analysis misses edge cases. Most ethical issues appear when you compare how a product treats a motivated, resourced user versus a stressed, constrained, or unaware one.

### Step 2 — Matrix Generation

For each combination of [Motivation Type] × [User @ Context], write a cell statement using this format:

**[Motivation] + [Action]**

Example: *"Social Acceptance + The design displays a public activity streak that resets if the user skips a day, making rest feel like failure."*

Be specific. Name the design element. Describe the mechanism. Avoid vague statements like "uses social pressure." Instead, write what the pressure actually looks like on screen.

Fill the full matrix: 5 rows × however many columns you have. Do not skip cells. Blank cells are missed opportunities for insight.

### Step 3 — Ethical Analysis

Read across the completed matrix through three lenses:

**Lens 1 — Manipulative Patterns**

Which cells use fear, social pressure, or dark incentives to drive behavior the user did not choose? Look for:
- Countdowns that create artificial urgency
- Social proof that manufactures consent
- Loss aversion framing that turns neutral actions into perceived threats
- Rewards that shift intrinsic motivation to extrinsic (overjustification effect)

**Lens 2 — Underrepresented Users and Contexts**

Which users or situations are missing from the matrix? Who could be harmed by the motivational patterns you identified? Consider:
- Users with lower digital literacy
- Users in non-ideal contexts (stressed, distracted, coerced)
- Non-users affected by the product's existence
- Users from cultures where the motivational framing reads differently

**Lens 3 — Secondary User Consequences**

What happens to people who are not directly using the product but are affected by it? For example:
- A fitness app's competitive leaderboard affects non-users when participants compare themselves to friends who do not use the app.
- A gig economy platform's incentive structure affects the families of workers.

Flag each cell with one of three ratings:

| Flag | Meaning |
|---|---|
| 🟢 Ethical | The motivation is transparently aligned with user goals. The user can opt out without penalty. |
| 🟡 Monitor | The motivation has potential for harm depending on context, user vulnerability, or scale. Needs attention. |
| 🔴 Manipulative | The design exploits a motivation to drive behavior that primarily benefits the system, not the user. The user cannot easily opt out or notice the manipulation. |

Detailed flagging criteria are in `references/ethical-flags.md`.

### Step 4 — Output

Produce three deliverables:

**1. Filled Matrix Table (markdown)**

Use the template from `assets/matrix-template.md`. Each cell contains the [Motivation] + [Action] statement and its flag.

**2. Ethical Risk Summary (3–5 bullets)**

Distill the flagged cells into the most significant risks. Prioritize 🔴 cells. Name the specific design element, the motivation it exploits, and who is affected.

**3. Redesign Directions (1–3)**

For each significant risk, propose a concrete design change. Redesign directions should be actionable — not "be less manipulative" but "replace the countdown timer with a calm reminder that the user can dismiss." Reference the cell that triggered the direction.

## Output Format

### Motivation Matrix Session

Framing statement: product name, contexts chosen, focus question.

### Filled Matrix

Markdown table with 5 rows (motivation types) × N columns (user @ context). Each cell contains the [Motivation] + [Action] statement and its ethical flag.

### Ethical Risk Summary

3–5 bullets identifying the most significant risks. Reference specific cells. Name the affected users.

### Redesign Directions

1–3 concrete design changes. Each references the flagged cell that triggered it and describes what to change and why.

### Missing Contexts

List any user groups or situations that were not included but should be considered. Explain why they matter.

## Guardrails

- Do not skip cells. A blank cell is an unexamined risk.
- Do not default every cell to 🟢. If nothing is flagged, the analysis was too gentle. Real products leverage motivation in ways worth examining.
- Do not treat 🔴 as a verdict. A manipulative flag means "look at this carefully," not "this product is evil."
- Use accessible language. Explain ethical design terms inline. Avoid jargon without definition.
- Maintain a non-judgmental tone. The matrix is a conversation starter, not an accusation.
- Include secondary and underrepresented users. The matrix that only examines ideal users in ideal contexts misses the most important risks.

## Deliverable Quality Bar

A strong Motivation Matrix output:

- fills all 5 × N cells with specific, design-element-level statements
- flags at least one cell as 🔴 or 🟡 — a matrix with all greens was not honest enough
- proposes at least one concrete redesign direction
- mentions at least one secondary or underrepresented user group
- uses the [Motivation] + [Action] format consistently
- names specific UI elements, features, or mechanisms — not abstract patterns
- generates at least one insight the team did not expect

## Integration with Other EDBX Skills

The Motivation Matrix works best alongside other ethical design methods:

- **edbx-worrystorming** — surfaces fears that users hold; this skill maps how those fears might be exploited by the design. Run edbx-worrystorming first to populate the Fear row with real user concerns.
- **edbx-responsible-design-prism** — diagnoses where your design practice falls on a responsibility spectrum; this skill provides the motivation-level analysis within that diagnosis. Use the prism for macro positioning and the matrix for micro analysis.
- **edbx-humane-design-guide** — maps sensitivity exploitation broadly; this skill maps motivational exploitation specifically. The guide identifies *that* a sensitivity exists; the matrix shows *how* it manifests as a design element.
- **edbx-anotherlens** — surfaces designer biases; this skill maps how those biases manifest as motivational assumptions baked into the product. Run edbx-anotherlens first to understand whose motivations the team is centering.
- **edbx-cider** — maps user access and capability; this skill maps user motivation — why users engage. Together they answer: who can use this, and why do they?

## Further Reading

- Zhu, A. (2020). *Design Driven by Motivation.* design4good.com/book
- Nodders, C. (2020). "Motivation Matrix." In *Universal Methods of Ethical Design.*
