---
name: edbx-worrystorming
description: Use when a designer, product team, or researcher wants to proactively identify risks in a design before shipping, generate worry clusters around a product idea, reframe concerns as design values, map unintended consequences, or run an ethical pre-mortem on a feature or product. Facilitate a Worrystorming session to surface ethical concerns, unintended consequences, and value failures in a design or product. Trigger this skill for any mention of ethical risks, design worries, what could go wrong, unintended consequences, pre-mortem, concern mapping, value conflicts in design, or when someone says "I'm worried this design might..." Also trigger for "worrystorming", "ethical pre-mortem", "what could go wrong", "concern mapping", "risk brainstorm", or "value conflicts".
version: "1.0"
tags: [ethical-design, forecast]
---

# Worrystorming

## Overview

Worrystorming modifies traditional brainstorming by shifting focus from idea generation to calibration — identifying large-scale dilemmas and future consequences before they materialize. Instead of asking "what should we build?", it asks "what might go wrong if we build this?"

The method normalizes ethical anxiety as a design resource, not a blocker. A designer surrounded by worry clusters, with a "worry cloud" over their head, is doing the work of responsible design — not being paranoid.

The core sequence is: **generate worries → cluster into themes → reframe as values → generate refined ideas.** The reframing step is what makes this different from a standard risk register. Raw concerns become design commitments.

> **Method #100 — Worrystorming.** From *Universal Methods of Ethical Design*. Hashtags: #breakmydesign #evaluateoutcomes #identifyvalues. See also: Empathic Walkthrough · Moral Agent.

This is the final method in the book — a capstone practice that synthesizes the ethical design mindset. It is explicitly consequentialist: it asks what happens downstream, at scale, over time.

## Use This Skill When

- You want to proactively identify risks before shipping.
- You need to generate an exhaustive set of concerns about a design.
- You want to reframe those concerns into positive design values.
- A team is about to launch something and needs an ethical pre-mortem.
- Someone says "I'm worried this design might..."
- You want to map unintended consequences at scale.
- You need to surface value conflicts between business goals and user wellbeing.

## Inputs

Provide as many of these as are available:

- **The design, product, or feature** to evaluate (name + brief description)
- **Project stage** — ideation, in-development, pre-launch, or live (worries differ by stage)
- **Known concerns** — anything already worrying the team
- **Affected users and stakeholders** — who is touched by this, directly and indirectly
- **Domain of concern** (optional) — e.g., data privacy, environmental impact, community harm, algorithmic bias
- **Team context** (optional) — solo reflection, cross-functional team, stakeholder workshop

If the user provides only the product name, proceed — the method is designed to work from minimal input.

## The Eight Concern Categories

Worrystorming generates worries across eight thematic clusters. Covering all eight ensures breadth — most teams naturally focus on 2–3 and miss the rest.

| Cluster | Theme | Guiding Questions |
|---|---|---|
| 🗃️ Data & Privacy | How is user data handled? | What if data is misused? What if consent is unclear? Who owns the data? |
| 🌍 Environmental Impact | What is the ecological cost? | What is the carbon footprint? What waste does this create? What infrastructure is required? |
| 👥 Community & Social | How does this affect communities? | What communal values does this disrupt? Who is excluded? What social dynamics change? |
| 💸 Economic | Who profits and who bears the cost? | Does this widen inequality? Who is priced out? What happens to existing livelihoods? |
| 🔒 Safety & Harm | Who could be hurt? | What failure modes exist? What happens during outages? Who is vulnerable? |
| 🧠 Psychological | Does this affect mental health? | Does this exploit cognitive bias? Does it cause anxiety, shame, or addiction? What about vulnerable populations? |
| ⚖️ Power & Fairness | Who has control? | Who is silenced? Who benefits from opacity? What power asymmetries does this create? |
| 🔮 Future Consequences | What happens at scale? | What precedent does this set? What happens in 5 years? What if a competitor copies this? |

Full definitions and example worries per category are in `references/worry-cluster-taxonomy.md`.

## Workflow

This skill has one integrated workflow with six steps. Run them in sequence.

---

### Step 1 — Intake

Collect from the user:

- What is the design, product, or feature?
- What stage is it at? (ideation / in-development / pre-launch / live)
- Are there any known concerns already?
- Who are the affected users and stakeholders?

If the user has a specific focus ("I'm particularly worried about data privacy"), note it — the method will still cover all eight categories, but the flagged area gets extra attention.

---

### Step 2 — Worry Generation

Generate a raw "worry list" of 10–20 concerns across the eight categories. Write each worry as a single, specific concern — sticky-note style, one per item.

**Format:** Numbered list, one worry per line.

**Quality bar for worries:**
- Specific, not generic: "The onboarding flow collects location data without explaining why" is better than "data privacy concerns"
- Actionable: a worry someone could investigate or test
- Stakes-named: who is affected and how

**Coverage:** Aim for at least 1–2 worries per category. Most teams over-index on Data & Privacy and Safety and under-index on Economic, Power & Fairness, and Future Consequences.

If the user has provided a specific domain of concern, generate extra worries in that area, but do not skip the other categories.

---

### Step 3 — Cluster into Worry Themes

Group the raw worries into 3–6 thematic clusters. Each cluster gets:

- **A name** — affirmatively framed where possible. "Data privacy fears" becomes **"User Data Sovereignty."** "Environmental impact worries" becomes **"Ecological Responsibility."** The reframe from fear to value begins at the naming stage.
- **3–5 constituent worries** — the raw concerns that belong to this cluster
- **A severity tag:**
  - `🔴 Critical` — likely, severe, and unaddressed
  - `🟡 Monitor` — possible, moderate, or partially addressed
  - `🟢 Low Risk` — unlikely, minor, or well-mitigated

Present as grouped sections with severity tags.

---

### Step 4 — Reframe as Design Values

For each cluster, derive three artifacts:

1. **Ethical Objective:** A commitment statement: "We commit to [X] in order to avoid [Y]."
2. **Design Constraint:** A concrete requirement or rule the design must satisfy. "The product must allow users to delete all data within 30 seconds."
3. **Test Question:** "How would we know if we failed at this?" — a question that could be answered through testing, research, or audit.

The reframing step is the emotional core of the method. It converts anxiety into agency. A worry becomes a value. A fear becomes a commitment.

See `references/value-reframing-guide.md` for examples and techniques.

---

### Step 5 — Generate Refined Ideas

For each cluster tagged `🔴 Critical`:

1. **Propose 1–2 design alternatives or mitigations** — concrete enough to implement or test.
2. **Flag which original ideas are most at risk** — what aspects of the current design are undermined by this worry.
3. **Suggest who should be consulted** — affected community, legal counsel, accessibility expert, domain specialist.

This step connects the abstract worry to concrete design action.

---

### Step 6 — Output

Compile the full session into a structured deliverable:

1. **Full Worry List** — the raw 10–20 concerns (Step 2)
2. **Clustered Worry Themes** — with severity tags (Step 3)
3. **Ethical Objectives + Design Constraints + Test Questions** — the reframed values (Step 4)
4. **Refined Ideas or Mitigations** — for all 🔴 Critical clusters (Step 5)
5. **Worrystorm Summary** — a single paragraph framing the key ethical challenges and the values the design should uphold

The summary is the session's artifact. It should fit on a sticky note and be specific enough to guide the next design decision.

---

## Facilitation Notes

**Solo use:** Write each worry on a separate line. Do not self-censor. The first worries that come to mind are often the most important — and the most avoided. Use `assets/worrystorm-template.md` as a blank worksheet.

**Team use:** Give each participant 5 minutes of silent writing before group discussion. This prevents anchoring. Then share one worry per person, round-robin, until all are surfaced. Group clustering works best on a shared surface (whiteboard, Miro). See `references/facilitation-guide.md` for detailed workshop instructions.

**Time budget:**
- Quick scan: 15–20 minutes (Steps 2–3 only)
- Full session: 45–60 minutes (all steps)
- Workshop: 90 minutes (with group discussion and clustering)

---

## Integration with Other EDBX Skills

- **edbx-motivation-matrix** surfaces why users act. Worrystorming surfaces what might go wrong when those motivations are exploited.
- **edbx-responsible-design-prism** diagnoses where a design currently sits. Worrystorming helps you get ahead of ending up on the dark side.
- **edbx-anotherlens** surfaces internal biases. Worrystorming surfaces the external consequences those biases might cause.
- **edbx-humane-design-guide** maps sensitivity exploitation. Worrystorming generates the concerns that feed into sensitivity analysis.
- **edbx-cider** maps who is excluded. Worrystorming generates the worries about who is excluded.

Run Worrystorming early in a project (ideation stage) to shape the design direction, or late (pre-launch) as an ethical pre-mortem.

---

## Guardrails

- **Do not stop at the worry list.** The reframing step (Step 4) is what makes this method valuable. A list of concerns without values is just anxiety.
- **Do not dismiss low-probability worries.** High-severity, low-probability events are the ones that destroy trust when they happen.
- **Do not sanitize the output.** If a worry feels uncomfortable to name, that's the signal. The worries that are hardest to say out loud are often the most important.
- **Do not judge the designer.** Worries about a product are not accusations against its creators. The method is generative, not punitive.
- **Cover all eight categories.** Most teams naturally skip Economic, Power & Fairness, and Future Consequences. These blind spots are where the biggest ethical failures originate.
- **Treat the summary as a living document.** It should be revisited as the design evolves, not filed away.

## Deliverable Quality Bar

A strong Worrystorming session output:

- generates at least 10 specific worries across multiple categories
- clusters into 3–6 coherent, affirmatively-named themes
- produces ethical objectives that are specific enough to create design constraints
- proposes test questions that could be answered through research or audit
- generates concrete mitigations for every critical cluster
- produces a summary paragraph that names the key ethical challenges without vague platitudes

## Example Output (partial)

> **Product evaluated:** AI tool that screens CVs and ranks candidates automatically
> **Stage:** In-development
>
> **Worry List (selected):**
> 1. Training data may encode historical hiring biases against women and minorities
> 2. Qualified candidates may be rejected by an algorithm with no explanation
> 3. Candidates have no way to know they were evaluated by AI
> 4. The tool may create a false sense of objectivity ("the algorithm decided")
> 5. Disabled candidates whose CVs have non-standard formatting may be scored lower
> 6. Companies using the tool may reduce human HR headcount, concentrating power in the tool provider
> 7. Over time, the tool may train candidates to optimize for algorithm scoring rather than genuine qualifications
> 8. There is no mechanism for candidates to appeal or correct algorithmic decisions
>
> **Cluster: Algorithmic Fairness (🔴 Critical)**
> - Worry 1, 2, 4
> - Ethical Objective: "We commit to explainable, auditable decisions to avoid invisible discrimination."
> - Design Constraint: "Every rejection must include a human-readable reason and a pathway to human review."
> - Test Question: "Could a rejected candidate understand why they were rejected and challenge the decision?"
>
> **Mitigation:** Add a mandatory human review layer for all rejection decisions. Publish a quarterly bias audit comparing algorithmic outcomes across demographic groups.
>
> **Worrystorm Summary:**
> "The core ethical challenge is opacity. An AI screening tool that makes consequential decisions about people's livelihoods without explanation, appeal, or audit creates a power asymmetry that no efficiency gain justifies. The design should commit to explainability, human oversight, and continuous bias monitoring as non-negotiable constraints."
