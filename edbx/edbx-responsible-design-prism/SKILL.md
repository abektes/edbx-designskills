---
name: edbx-responsible-design-prism
description: Use when a designer, product manager, or researcher wants to identify dark patterns in an existing product, evaluate where their design sits on the responsible/irresponsible spectrum, facilitate team self-reflection on design ethics, map business incentives against user wellbeing, generate transition paths from dark to responsible design, or answer questions about fair practice guidelines. Apply the Responsible Design Prism framework to audit, evaluate, and reframe design artifacts across the spectrum from dark patterns to responsible design. Trigger this skill for any mention of dark patterns, responsible design, design ethics audit, manipulation in UX, fair UX, ethical product design, or when someone asks "is this design ethical?". Also trigger for "responsible design prism", "dark pattern audit", "design spectrum", "fair practice", "ethical UX", or "manipulative design".
version: "1.0"
tags: [ethical-design, audit]
---

# Responsible Design Prism

## Overview

The Responsible Design Prism is a reflective evaluation framework that positions any design artifact on a spectrum from dark patterns to responsible design. It is listed as Method 79 in *Universal Methods of Ethical Design*; the primary source of the framework has not been identified. The structure below is this skill's framing. It uses a visual metaphor — two overlapping triangles forming a prism — where the left triangle represents exploitative design (dark pattern space), the right triangle represents ethical design (responsible design space), and the overlapping center is the transition and redesign zone.

The prism's three vertices, in this framing, are **User**, **Incentives**, and **Dark Pattern**. These vertices create tension: every design decision sits somewhere between treating users as means to an end and treating users as themselves. The framework makes that position explicit.

The prism is deliberately a spectrum, not a binary. Many real-world designs are likely to land in the transitional zone — not outright malicious, but not fully aligned with user wellbeing either. The value of the prism is making that position visible and navigable.

> **edbx adaptation:** the prism visual, the three vertices, the five axes and their poles, the transition zone, the four reflection prompts and the Red/Yellow/Green scoring are this skill's own framing; no source for them has been found, and they are not claimed to be a published method. They give the audit a repeatable structure. The stakeholder map (Step 1.5) and mechanism audit (Step 2.5) are also edbx additions.

> **Intent check:** This skill is diagnostic and constructive, not accusatory. Most dark patterns exist because of organizational pressure, not individual malice. The prism helps teams see where they are and find a path forward — it does not exist to shame designers.

## Use This Skill When

- You want to audit a product or feature for dark patterns before or after shipping.
- You suspect your design exploits users but cannot articulate exactly how.
- A team needs a structured, non-judgmental way to discuss design ethics.
- You need to present an ethical case for redesign to non-design stakeholders.
- You want to map business incentives against user wellbeing and find alignment.
- You are redesigning a known dark pattern and want a responsible alternative.
- You want to facilitate a team self-reflection session on design responsibility.

## Inputs

Provide as many of these as are available:

- The product, feature, or design artifact to evaluate (name + brief description)
- The business incentive or metric the design optimizes for
- The intended user and their context
- Any specific pattern or mechanism in question (e.g., confirmation dialog, pricing display, opt-out flow)
- Relevant guidelines the team follows (WCAG, platform policies, internal standards)
- Any known user complaints, confusion, or support tickets related to the feature

## The Prism — Five Spectrum Axes

In this skill, the prism evaluates every design artifact across five axes. Each axis runs from a dark pattern pole to a responsible design pole. Score each axis as **Red** (dark), **Yellow** (transitional), or **Green** (responsible).

| Axis | Dark Pattern Pole | Responsible Design Pole |
|------|-------------------|------------------------|
| User relationship | User as Means | User as Themselves |
| Information | Setting False Expectations | Transparent Communication |
| Error handling | Taking Advantage of Errors | Inform and Support Recovery |
| Business alignment | Exploitative Incentives | Fair Practice Guidelines |
| Usability | Weaponized Usability | Genuine Usability |

Full definitions for each axis are in `references/prism-axes.md`.

## Workflow

This skill has one integrated workflow with five steps. Run them in sequence.

---

### Step 1 — Intake

Gather the evaluation context:

- What is the product, feature, or artifact?
- What business incentive drives it?
- Who is the intended user?
- What specific pattern or mechanism is in question?
- What guidelines or standards apply?

If the user has not provided all of these, ask concisely. You do not need perfect information to proceed — the prism works with partial context, and gaps themselves are diagnostic.

---

### Step 1.5 — Stakeholder & Vulnerable Population Mapping (required, not optional)

Before scoring axes, enumerate every population the design touches. The prism evaluates a design's relationship to people — without naming who, the scoring becomes abstract.

Produce a table:

| Population | Relationship to product | Specific harms likely | Power asymmetry vs. operator |
|---|---|---|---|
| Primary users | (intended audience) | (named harms in plain language) | (can they exit? are they captive?) |
| Secondary users / non-users affected | (people in the user's environment, downstream parties) | | |
| Vulnerable populations (named specifically) | (e.g., minors, neurodivergent users, low-income, people in crisis, people in abusive relationships, undocumented users, people of marginalized racial/gender identity, people with disabilities — pick the ones actually relevant; do not list categories generically) | | |
| Workers / labor in the supply chain | (moderators, gig workers, etc., if applicable) | | |

If you cannot name at least 3 distinct populations with specific harms, the analysis is too abstract — go back and look harder. "Users" is not a population.

This table feeds Steps 2 and 4: every axis score must reference which populations it most affects, and every redesign pathway must name which populations benefit.

---

### Step 2 — Prism Placement

Score each of the five axes as Red, Yellow, or Green:

- **Red (dark):** The design actively exploits, deceives, or manipulates on this axis.
- **Yellow (transitional):** The design is not actively harmful but has elements that nudge toward the dark pole — often through neglect, mixed incentives, or inherited patterns.
- **Green (responsible):** The design genuinely serves the user's interests on this axis, with transparent intent and fair outcomes.

Present the results as a Prism Audit Table:

| Axis | Score | Evidence |
|------|-------|----------|
| User relationship | Red / Yellow / Green | What you observe |
| Information | Red / Yellow / Green | What you observe |
| Error handling | Red / Yellow / Green | What you observe |
| Business alignment | Red / Yellow / Green | What you observe |
| Usability | Red / Yellow / Green | What you observe |

Be specific in the evidence column. Generic observations ("could be better") are not useful — name the exact pattern or mechanism.

---

### Step 2.5 — Psychological Mechanism Audit (required for every Red or Yellow axis)

For every axis scored Red or Yellow in Step 2, name the **specific psychological mechanism** the design exploits. Vague claims of "manipulation" are not useful — name the named mechanism. Use precise terms:

- **Cognitive biases**: default bias, loss aversion, anchoring, social proof, scarcity heuristic, sunk cost, present bias
- **Behavioral mechanisms**: variable reward schedule (intermittent reinforcement), streak-loss aversion, near-miss design, autoplay/infinite scroll exploitation of attentional residue, friction asymmetry (easy in / hard out)
- **Emotional vulnerabilities**: FOMO, social anxiety / belonging needs, identity uncertainty (especially adolescents), grief / loneliness / boredom states, status threat
- **Developmental vulnerabilities** (if minors are in scope): incomplete prefrontal development affecting impulse control, peer-comparison sensitivity, identity formation pressure

Output as a table:

| Axis | Score | Mechanism named | Why it works (one sentence) | Population most affected |
|---|---|---|---|---|

If you cannot name a mechanism for a Red/Yellow score, either the score is wrong or the analysis is too shallow. "It's manipulative" is not a mechanism. "It uses variable reward scheduling on the like counter to drive compulsive checking" is a mechanism.

This audit grounds the redesign pathways in Step 4: every redesign must explain which mechanism it interrupts.

---

### Step 3 — Four Reflection Prompts

These four prompts are the heart of this skill's method. Do not reduce them to a checklist — facilitate genuine reflection on each one.

**Prompt 1 — Self-reflection: Where do you stand when you build?**
What state of mind, pressure, or assumption led to the current design? What did you optimize for? What would you have designed if user wellbeing were the only constraint?

**Prompt 2 — Organization ecology: What org pressures push toward dark patterns?**
What metrics, incentives, timelines, or leadership directives shaped the design? Where does the organization reward engagement over trust? This is not about blame — it is about understanding system dynamics.

**Prompt 3 — Transition: How can responsible design patterns help?**
For each Red or Yellow axis, what responsible design alternatives exist? What would the transitional version look like? What is the smallest meaningful shift toward the Green pole?

**Prompt 4 — Recovery: How do you find your way back to the right side?**
If the design is already shipped and causing harm, what is the recovery path? How do you reverse the pattern without destroying business value? What does the responsible version of this feature look like?

Expanded facilitation guidance is in `references/reflection-questions.md`.

---

### Step 4 — Redesign Pathways

For every Red or Yellow axis identified in Step 2, generate a redesign pathway with three components:

1. **Redesign suggestion:** A concrete alternative design that moves toward the Green pole.
2. **Business case for the ethical alternative:** Why the responsible version serves long-term business interests — retention, trust, brand, regulatory compliance, reduced support costs. See `references/business-framing.md`.
3. **Risk if left unchanged:** What happens if the dark or transitional pattern persists — user churn, reputation damage, regulatory exposure, team burnout, ethical debt.

Present pathways as a table:

| Axis | Current State | Redesign Suggestion | Business Case | Risk of Inaction |
|------|---------------|--------------------|---------------|-----------------|
| ... | Red/Yellow | ... | ... | ... |

---

### Step 5 — Output

Compile the full prism audit into a stakeholder-ready deliverable. Open it with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title. Then:

1. **Stakeholder & Vulnerable Population Map** (from Step 1.5) — populations, harms, power asymmetries
2. **Prism Audit Table** (from Step 2) — the scored five-axis evaluation
3. **Psychological Mechanism Audit** (from Step 2.5) — named mechanisms exploited by every Red/Yellow axis
4. **Spectrum Placement Summary** — one paragraph describing where the design sits on the overall spectrum and what that means
5. **Reflection Highlights** — key insights from the four prompts (not raw transcripts — synthesized takeaways)
6. **Redesign Pathway Recommendations** (from Step 4) — actionable alternatives with business justification, each naming which mechanism it interrupts and which population benefits
7. **Leadership Framing** — one paragraph suitable for presenting to non-design stakeholders, written in business language
8. **Evidence Ledger** — every figure or fact about the user's situation the output relies on, typed as below

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

A blank template is in `assets/prism-audit-template.md`.

---

## Dark Pattern Taxonomy Reference

When scoring axes, draw on the dark pattern taxonomy in `references/dark-pattern-taxonomy.md`. Its five groups are this skill's own grouping, not the deceptive.design ontology (which has 64 synthesized types in three levels). Groups:

- **Deception:** hiding information, false expectations, bait-and-switch, hidden costs
- **Coercion:** forced continuity, roach motel, confirmshaming, trick questions, preselection
- **Exploitation:** sneak into basket, urgency, social proof and scarcity fakery, exploiting error
- **Manipulation:** hard-to-compare options, visual interference, attention capture, emotional manipulation
- **Obstruction:** hard-to-cancel, hard-to-delete, intermediate currency, information overload

Use precise pattern names rather than vague accusations. "This confirmation dialog uses confirmshaming language" is more useful than "this feels manipulative."

---

## Integration with Other EDBX Skills

The Responsible Design Prism connects to other skills in the Ethical Design Box:

- **edbx-motivation-matrix:** Surfaces why users act. The Prism evaluates how design exploits or respects that motivation.
- **edbx-anotherlens:** Surfaces designer biases and assumptions. The Prism evaluates the design output those biases produce.
- **edbx-humane-design-guide:** Maps how design exploits human sensitivities. The Prism places that exploitation on a responsibility spectrum.
- **edbx-worrystorming:** Generates broad concerns about a design. The Prism helps prevent those concerns from becoming dark patterns.
- **edbx-cider:** Maps who is excluded by design. The Prism evaluates whether exclusion is deliberate (dark) or unintentional (transitional).

See `references/related-methods.md` for detailed connections and sequencing guidance.

Use the Prism as a follow-up to any of these skills to move from diagnosis to redesign.

---

## Guardrails

- Do not collapse the spectrum into a binary pass/fail. The Yellow/transitional zone is where many real products sit — it deserves honest attention, not dismissal.
- Do not skip the reflection prompts. The scoring is only useful if the team reflects on why they scored the way they did. The prompts are the method.
- Maintain a non-accusatory tone. Designers often build dark patterns under organizational pressure, not from malice. The goal is awareness and redesign, not guilt.
- Always pair a dark pattern flag with a responsible alternative. Criticism without a path forward is not constructive.
- Acknowledge system dynamics. Individual designers rarely control the incentive structures that produce dark patterns. The prism names those structures without letting individuals off the hook.
- Use precise language. Name the specific dark pattern (e.g., "roach motel"), not just the vibe (e.g., "feels sketchy").
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

## Deliverable Quality Bar

A strong Responsible Design Prism audit:

- enumerates at least 3 distinct populations in the Stakeholder Map, naming vulnerable populations specifically (not "users" generically)
- scores all five axes with specific, evidence-based observations referencing which populations are affected
- names a specific psychological mechanism for every Red or Yellow axis (e.g., "variable reward schedule," not "manipulation")
- lands on at least one Red or Yellow — if everything is Green, the audit was too gentle
- generates genuine insight from the reflection prompts, not performative answers
- produces redesign suggestions concrete enough to implement, each naming which mechanism it interrupts
- includes business framing that a product manager or executive could act on
- names specific dark patterns from the taxonomy, not vague ethical concern
- writes the leadership framing in language that does not require design literacy to understand
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

## Further Reading

- Nielsen, J. (2020). "Responsible Design." Nielsen Norman Group.
- Narayanan, A., Mathur, A., Chetty, M. & Kshirsagar, M. (2020). "Dark Patterns: Past, Present, and Future." *ACM Queue* 18(2).
- Brignull, H. (2023). "Deceptive Design Patterns." deceptive.design
- Worldwide Web Foundation (2021). "Ethical Design Framework."
