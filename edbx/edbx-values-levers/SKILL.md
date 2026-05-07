---
name: edbx-values-levers
description: Use when a designer, team lead, or design manager wants to open up values discussions in a team, identify what values are currently embedded in team practices, use constraints creatively to surface value conflicts, advocate for ethical considerations within an organization, facilitate cross-disciplinary values alignment, or understand what values their communication systems are reinforcing. Apply the Values Levers framework to surface, discuss, and build team consensus around values embedded in a design process or organizational culture. Trigger this skill for any mention of team values alignment, values in design practice, organizational culture and ethics, building consensus on ethics, soft resistance in design, advocating for ethical design internally, or when someone says "I'm trying to get my team to care about ethics." Also trigger for "Values Levers", "team values", "org ethics culture", "building consensus", "soft resistance", or "advocating for ethical design".
metadata:
  version: "1.0"
---

# Values Levers

## Overview

Values Levers enable you to leverage practices that help you and your team discuss and build consensus around values during the design process. Values are embedded in the work environment, and there is a connection between those values and the design process. Values Levers are tools that help people open discussions about values at a design level, team level, or organizational level.

The framework operates on a bidirectional ENABLE model:
*Communication Modes → enable → Values Levers → enable → Values-Based Design Decisions*

Communication modes shape what values conversations are possible; values levers shape what decisions get made; decisions shape what communication modes get used next. It is a feedback loop, not a linear pipeline.

Values Levers is the **team culture** tool in the ethical design toolkit. It operates at the team and organizational layer — not the individual designer or artifact layer. It addresses culture change, not just individual audit.

> **Mindset check:** Values Levers open conversations, they don't win arguments. The goal is consensus-building, not confrontation. If direct advocacy isn't safe, "soft resistance" is available as a fallback.

## Use This Skill When

- You want to open up values discussions in your team.
- You need to identify what values are currently embedded in team practices.
- You want to use constraints creatively to surface value conflicts.
- You are trying to advocate for ethical considerations within your organization.
- You need to facilitate cross-disciplinary values alignment.
- You want to understand what values your communication systems are reinforcing.
- You are trying to get your team to care about ethics.

## Inputs

Provide as many of these as are available:

- A team context or organizational situation (e.g., "startup with no ethics process", "large org with siloed teams")
- A design challenge or ongoing project where values tension exists
- **Your role and authority level** (individual contributor / team lead / design manager — this determines which levers are available to you)
- Optionally: a specific lever type to focus on
- Optionally: an existing communication mode or system to analyze (e.g., Slack, design crits, sprint retros)
- Optionally: a values conflict or ethical disagreement currently happening in the team

> **Individual Mode:** If you are an individual contributor without organizational authority, this skill activates a fast path. Rather than requiring team buy-in, it focuses on Levers 3 (Leader/Team Member Advocacy) and 4 (Self-Testing) with concrete individual actions you can take without anyone else's permission.

## Workflow

Values Levers operates in four steps.

---

### Step 1 — Values Lever Identification

Assess which of the five levers are available and applicable:

| Lever | When to Apply | How to Activate |
|---|---|---|
| **Interdisciplinary Teams** | When values discussions stay siloed in design | Bring in engineers, ethicists, legal, community reps to cross-pollinate perspectives |
| **Designing Around Constraints** | When value conflicts feel unresolvable | Impose a constraint that forces the team to confront the conflict (e.g., "design as if you can't use this data") |
| **Leader/Team Member Advocacy** | When ethical concerns aren't being raised in meetings | Identify who can champion values internally; equip them with language and framing |
| **Self-Testing** | When the team lacks empathy for affected users | Have technologists experience their own system as a non-expert or vulnerable user |
| **Gaining/Funding** | When ethics work is deprioritized due to resource constraints | Frame ethics investment as risk reduction; identify budget or headcount opportunities |

Match lever recommendations to the user's actual role and authority.

**Lever Resistance Map (required for each recommended lever):**
For each lever, name the most common organizational resistance point and a specific counter-move:

| Lever | Most Common Resistance | Counter-Move |
|---|---|---|
| Interdisciplinary Teams | "We don't have budget to include ethics/legal in sprints" | Reframe as risk reduction: "One hour with legal prevents six months of compliance work" |
| Designing Around Constraints | "Constraints slow us down" | Run as a 60-minute spike, not a process change |
| Leader/Team Member Advocacy | "Leadership doesn't want to hear ethics concerns" | Frame the concern as a business risk, not an ethics concern |
| Self-Testing | "We don't have time for dogfooding" | Attach to existing QA sprint; 30 minutes minimum |
| Gaining/Funding | "Ethics work isn't on the roadmap" | Calculate the cost of one ethics incident; compare to the cost of prevention |

**Output:** A ranked list of 2–3 most applicable levers with activation guidance and resistance counter-moves.

---

### Step 2 — Map Communication Modes

For the team's existing communication channels, assess:
- What values are currently being reinforced by how the team communicates?
- Which channels create space for values discussion (e.g., retrospectives, design crits)?
- Which channels suppress values discussion (e.g., metrics-only standups)?
- What new communication mode or ritual could enable values conversations?

Use the ENABLE bidirectional model:
*Communication Modes → enable → Values Levers → enable → Values-Based Design Decisions*

---

### Step 2.5 — Surface Whose Values Are Visible (and Whose Aren't)

Values Levers is fundamentally a **values-surfacing** methodology — not a tactical influence toolkit. Before facilitating consensus, name **whose values the current process is serving** and **whose values are absent from the room**. The biggest gap in Values Levers work is when the team converges on internal values while non-user, vulnerable, and downstream-affected populations stay invisible.

Produce three tables:

**A. Whose values are currently being served?** (Stated and unstated)

| Stakeholder | Stated values driving current decisions | Unstated values driving current decisions (e.g., risk avoidance, career safety, optionality, plausible deniability) |
|---|---|---|

**B. Whose values are absent from the conversation?** Name them specifically:

| Absent stakeholder | What they would want | How their absence shapes the design |
|---|---|---|
| e.g., users with disabilities | accessible-by-default rather than accessibility-as-feature | accessibility framed as cost, not requirement |
| e.g., people in 5 years using accumulated user data | meaningful data minimization | unbounded retention defaults |
| e.g., users in regimes where the data could be subpoenaed | data localization, encryption-in-transit, ability to delete | global single-tenant architecture |
| (continue with at least 3 specifically named groups) | | |

**C. Systemic / second-order harm map.** Even if the team's values look benign, the aggregate effect across many users may not be. Name:

- **Aggregation effects** — what becomes possible when many individuals' data combines that wasn't possible at the individual level
- **Power dynamics** — what the design hands the operator over the user, and how reversible that is
- **Future discriminatory use** — what protected-class inferences become possible once this data exists
- **Non-user externalities** — who is affected without ever opting in (people in the user's environment, people scraped into training data, etc.)

This step transforms Values Levers from "how to win an internal argument" into "how to make all relevant values visible." Skip it and the audit stays at organizational risk level — strong on team alignment, weak on ethical depth.

---

### Step 3 — Facilitate Values Consensus

Generate a facilitation plan for a team values conversation:
- Opening question to surface existing embedded values
- Constraint exercise to reveal value conflicts
- Advocacy framing: how to raise a values concern without triggering defensiveness
- Decision criteria: "Which values orientations and outcomes do our design decisions embody?"

### Step 4 — 30-Day Action Plan

For the top 2 recommended levers, generate a concrete week-by-week action sequence with named stakeholders and deliverables. Generic lever guidance produces aspiration; a 30-day plan with named actions produces change.

**Format:**
- **Week 1:** [Specific action, named stakeholder to engage, deliverable]
- **Week 2:** [Specific action, stakeholder, deliverable]
- **Week 3:** [Specific action, stakeholder, deliverable]
- **Week 4:** [Review + decision checkpoint — what success or failure looks like]

This step is the primary differentiator from raw analysis: the lever-specific strategic logic (why these actions in this sequence for this lever) cannot be generated without the Values Levers framework.

---

## Output Format

### Values Levers: [Team Context]

### Lever Activation Plan

| Lever | Applicable? | How to Activate | Who Owns It |
|---|---|---|---|
| Interdisciplinary Teams | Yes/No | [activation guidance] | [name] |
| Designing Around Constraints | Yes/No | [activation guidance] | [name] |
| Leader/Team Member Advocacy | Yes/No | [activation guidance] | [name] |
| Self-Testing | Yes/No | [activation guidance] | [name] |
| Gaining/Funding | Yes/No | [activation guidance] | [name] |

### Whose Values Are Visible — and Whose Aren't

(From Step 2.5 — required output, not optional. This is the values-surfacing core of the method.)

**A. Stated vs unstated values currently driving decisions:**

| Stakeholder | Stated values | Unstated values (risk-aversion, career safety, optionality, plausible deniability, etc.) |
|---|---|---|

**B. Absent stakeholders — named specifically (minimum 3):**

| Absent stakeholder | What they would want | How their absence shapes the design |
|---|---|---|

**C. Systemic / second-order harm map:**

- Aggregation effects: [what becomes possible at scale that wasn't possible per-individual]
- Power dynamics: [what the design hands the operator over the user, and reversibility]
- Future discriminatory use: [protected-class inferences this data enables]
- Non-user externalities: [who is affected without opting in]

### Communication Audit

| Channel | Values Reinforced | Space for Ethics? | Recommendation |
|---|---|---|---|
| [Channel 1] | [what values] | Yes/No/Partial | [change needed] |

### Facilitation Guide: Values Conversation Session

1. **Opening question:** [question to surface embedded values]
2. **Constraint exercise:** [exercise to reveal conflicts]
3. **Discussion:** [facilitation approach]
4. **Decision:** [decision criteria]

### Values-Based Design Decision Statement

*"In this project, we are choosing to prioritize [value X] over [value Y] because [reason], and this will manifest in [specific design decision]."*

## Guardrails

- Do not recommend levers that require more authority than the user has. Match levers to role.
- Do not assume the user can change everything. Be realistic about power dynamics and organizational constraints.
- Do not treat values conversations as debates to be won. Consensus-building requires generosity.
- Do not skip the communication audit. How a team communicates shapes what values are possible.
- Do not forget soft resistance. When direct advocacy isn't safe, indirect strategies are valid.
- Do not treat the Values-Based Design Decision statement as optional. It is the concrete output that makes the conversation matter.

## Deliverable Quality Bar

A strong Values Levers output:

- identifies 2–3 applicable levers for any team context
- matches lever recommendations to the user's actual role and authority
- activates Individual Mode when the user is an individual contributor without organizational authority
- includes a Lever Resistance Map with a named counter-move for each recommended lever
- **completes the "Whose Values Are Visible" mapping** (Step 2.5): stated/unstated values for present stakeholders, at least 3 named absent stakeholders, and a systemic-harm map covering aggregation effects, power dynamics, future discriminatory use, and non-user externalities. Without this section, the output is a tactical influence toolkit, not a values-surfacing methodology.
- includes a communication audit with at least one existing channel and one new ritual suggestion
- produces a facilitation guide that is session-ready and runnable in under 60 minutes
- produces a 30-day action plan with week-by-week named actions, stakeholders, and deliverables for the top 2 levers
- generates a Values-Based Design Decision statement for every session
- handles power asymmetry and organizational resistance realistically

## Integration with Other EDBX Skills

- **edbx-worrystorming** generates ethical concerns. Values Levers provides organizational mechanisms to act on them.
- **edbx-anotherlens** is individual self-reflection. Values Levers scales that to team and organizational culture.
- **edbx-cider** surfaces exclusionary assumptions in artifacts. Values Levers creates the team culture to challenge them.
- **edbx-humane-design-guide** identifies sensitivity exploitation. Values Levers builds culture to prevent it.

## Hashtags

#identifyvalues #designresponsibility

## See Also

- Tactics on Soft Resistance
- Pledge Works
