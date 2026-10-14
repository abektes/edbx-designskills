---
name: edbx-values-levers
description: Use when a designer, team lead, or design manager wants to open up values discussions in a team, identify what values are currently embedded in team practices, use constraints creatively to surface value conflicts, advocate for ethical considerations within an organization, facilitate cross-disciplinary values alignment, or understand what values their communication systems are reinforcing. Apply the Values Levers framework to surface, discuss, and build team consensus around values embedded in a design process or organizational culture. Trigger this skill for any mention of team values alignment, values in design practice, organizational culture and ethics, building consensus on ethics, soft resistance in design, advocating for ethical design internally, or when someone says "I'm trying to get my team to care about ethics." Also trigger for "Values Levers", "team values", "org ethics culture", "building consensus", "soft resistance", or "advocating for ethical design".
version: "1.0"
tags: [ethical-design, alignment]
---

# Values Levers

## Overview

Values Levers enable you to leverage practices that help you and your team discuss and build consensus around values during the design process. Values are embedded in the work environment, and there is a connection between those values and the design process. Values Levers are tools that help people open discussions about values at a design level, team level, or organizational level.

Shilton and Koepfler describe the link this way: modes of communication can enable or constrain values levers, and values levers in turn enable or constrain values-based design:
*Communication Modes → enable or constrain → Values Levers → enable or constrain → Values-Based Design Decisions*

Communication modes shape what values conversations are possible; values levers shape what decisions get made.

> **edbx adaptation:** reading this chain as a feedback loop, where decisions also shape which communication modes the team uses next, is edbx's; the papers give the chain, not a return link, and do not call it "ENABLE". The loop is here because a team's habits of communication change after what it decides.

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

Assess which of the six levers are available and applicable:

| Lever | When to Apply | How to Activate |
|---|---|---|
| **Interdisciplinary Teams** | When values discussions stay siloed in design | Bring in engineers, ethicists, legal, community reps to cross-pollinate perspectives |
| **Designing Around Constraints** | When value conflicts feel unresolvable | Impose a constraint that forces the team to confront the conflict (e.g., "design as if you can't use this data") |
| **Leader/Team Member Advocacy** | When ethical concerns aren't being raised in meetings | Identify who can champion values internally; equip them with language and framing |
| **Self-Testing** | When the team lacks empathy for affected users | Have technologists experience their own system as a non-expert or vulnerable user |
| **Gaining/Funding** | When ethics work is deprioritized due to resource constraints | Frame ethics investment as risk reduction; identify budget or headcount opportunities |
| **Navigating Institutional Mandates** | When an outside body (an ethics review board, a regulator, a funder, a platform) imposes requirements on the work | Approach the body early and treat its review as an external check that keeps values on the agenda |

> **edbx adaptation:** the "When to Apply" and "How to Activate" columns are edbx's. Shilton's 2013 article describes levers as practices observed in one research lab, to look for in other settings, not as activation recipes. The article lists six levers (the five above that Shilton and Koepfler list, plus navigating institutional mandates) and calls its list probably incomplete, so treat the list as open. In the article, Gaining/Funding worked by paying for larger, more interdisciplinary teams, regular meetings and a long-term values advocate; the risk-reduction framing is edbx's. Interdisciplinary Teams worked there by bringing in statisticians and social scientists whose questions put the data in the spotlight; adding ethicists, legal or community representatives is edbx's. Self-Testing there meant technologists seeing their own and colleagues' data in internal testing; experiencing the system as a non-expert or vulnerable user is edbx's. Imposing a constraint such as "design as if you can't use this data" is edbx's; in the article the constraint was an existing privacy commitment that leaders framed as a creative challenge.

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

Use the chain from the overview, and check whether decisions are in turn changing how the team communicates:
*Communication Modes → enable or constrain → Values Levers → enable or constrain → Values-Based Design Decisions*

---

### Step 2.5 — Surface Whose Values Are Visible (and Whose Aren't)

> **edbx adaptation:** the three tables below are not in either Shilton paper, which define a lever as a practice that opens conversations about values; they resemble stakeholder analysis in value sensitive design. They are here because a team that converges on its own values can leave non-users, vulnerable groups and downstream parties out of the room.

Before facilitating consensus, name **whose values the current process is serving** and **whose values are absent from the room**. The biggest gap in Values Levers work is when the team converges on internal values while non-user, vulnerable, and downstream-affected populations stay invisible.

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

This step widens the conversation from the team's own values to the values of everyone the design touches. Skip it and the audit stays at organizational risk level — strong on team alignment, weak on ethical depth.

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

Tie each action to the lever it activates, so the sequence shows why these actions come in this order for this lever.

---

## Output Format

Open with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title.

### Values Levers: [Team Context]

### Answer

[Two to four sentences: the answer to the question asked (decision, verdict or recommendation) and the main reason.]

### Lever Activation Plan

| Lever | Applicable? | How to Activate | Who Owns It |
|---|---|---|---|
| Interdisciplinary Teams | Yes/No | [activation guidance] | [name] |
| Designing Around Constraints | Yes/No | [activation guidance] | [name] |
| Leader/Team Member Advocacy | Yes/No | [activation guidance] | [name] |
| Self-Testing | Yes/No | [activation guidance] | [name] |
| Gaining/Funding | Yes/No | [activation guidance] | [name] |
| Navigating Institutional Mandates | Yes/No | [activation guidance] | [name] |

### Whose Values Are Visible — and Whose Aren't

(From Step 2.5 — required output, not optional. It widens the values conversation to absent stakeholders.)

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

### Evidence Ledger
| Claim used as input | Type | Basis |
|---|---|---|
| [figure, rate or fact the output relies on] | [user-supplied / sourced / assumption / unknown] | [the brief / paper or URL / why assumed] |

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

## Guardrails

- Do not recommend levers that require more authority than the user has. Match levers to role.
- Do not assume the user can change everything. Be realistic about power dynamics and organizational constraints.
- Do not treat values conversations as debates to be won. Consensus-building requires generosity.
- Do not skip the communication audit. How a team communicates shapes what values are possible.
- Do not forget soft resistance. When direct advocacy isn't safe, indirect strategies are valid.
- Do not treat the Values-Based Design Decision statement as optional. It is the concrete output that makes the conversation matter.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

## Deliverable Quality Bar

A strong Values Levers output:

- identifies 2–3 applicable levers for any team context
- matches lever recommendations to the user's actual role and authority
- activates Individual Mode when the user is an individual contributor without organizational authority
- includes a Lever Resistance Map with a named counter-move for each recommended lever
- **completes the "Whose Values Are Visible" mapping** (Step 2.5): stated/unstated values for present stakeholders, at least 3 named absent stakeholders, and a systemic-harm map covering aggregation effects, power dynamics, future discriminatory use, and non-user externalities. Without this section, the conversation stays inside the team.
- includes a communication audit with at least one existing channel and one new ritual suggestion
- produces a facilitation guide that is session-ready and runnable in under 60 minutes
- produces a 30-day action plan with week-by-week named actions, stakeholders, and deliverables for the top 2 levers
- generates a Values-Based Design Decision statement for every session
- handles power asymmetry and organizational resistance realistically
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

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
