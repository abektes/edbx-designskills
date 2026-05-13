---
name: edbx-digital-ethics-compass
description: Use when a designer, product manager, or AI practitioner wants to reflect on the ethical dimensions of data collection and use, evaluate automation and AI features for manipulation or unfairness, assess whether intentions and processes are transparent to users, apply a structured heuristic framework to data-intensive or AI-powered products, or run a broad ethical health check on a product. Apply the Digital Ethics Compass heuristics to evaluate a product or business across four ethical dimensions — Data, Avoid Manipulation, Make Intentions Transparent, and Automation — putting the human at the center of every decision. Trigger this skill for any mention of data ethics, AI ethics, automation ethics, behavioral manipulation, transparency obligations, responsible AI, or when someone asks "is our data practice ethical?" Also trigger for "Digital Ethics Compass", "data ethics audit", "AI ethics", "automation fairness", "responsible AI", or "ethical health check".
version: "1.0"
tags: [ethical-design, audit]
---

# Digital Ethics Compass

## Overview

Digital Ethics Compass guides you to reflect on your product and business development goals through heuristics relating to data, automation, and behavioral design. It acts as an ethical navigator for companies and design teams, providing heuristic questions across four categories.

The compass is a printable, rotatable wheel with "Put the Human in the Cosmos" at the center. The inner ring has four main categories: **Data**, **Avoid Manipulation**, **Make Intentions Transparent**, and **Automation**. The middle and outer rings provide increasingly specific heuristic questions for reflection.

The compass can be used to evaluate ethical decisions at every level — from individual features to entire business models. It provides a structured heuristic framework that is practical and actionable, not theoretical.

> **Mindset check:** "Put the Human in the Cosmos" is not just a slogan — it is the orienting principle for every heuristic question. If the human is not at the center, the compass reading is off.

## Use This Skill When

- You want to evaluate a product's ethical dimensions across data, manipulation, transparency, and automation.
- You are working on data-intensive or AI-powered products.
- You need to assess whether your data practices are ethical.
- You want to evaluate automation and AI features for fairness and manipulation.
- You need to check whether your intentions and processes are transparent to users.
- You want a broad ethical health check on a product.

## Inputs

Provide as many of these as are available:

- A product, service, or feature with data, automation, or behavioral design components
- Optionally: a specific category to focus on (Data / Manipulation / Transparency / Automation)
- Optionally: a business model or data practice to evaluate
- Optionally: a specific user population or context

## Workflow

The compass evaluates four categories with "Put the Human in the Cosmos" as the orienting principle throughout. Before any category is scored, the team must complete an **explicit Stakeholder Map** — without it, "Put the Human in the Cosmos" remains an abstraction.

---

### Step 0 (required): Stakeholder & Power Map

Before walking through the four categories, enumerate every population the design touches. The judges' most consistent complaint about Compass output is that stakeholder mapping stays implicit. Make it explicit. This is mandatory output, not optional.

**A. Named stakeholder enumeration (minimum 5 distinct rows; "users" alone is not a stakeholder).**

| Stakeholder | Relationship to product | Specific power they have | Specific power they lack | What they would lose if the product harmed them |
|---|---|---|---|---|
| Primary users | (intended audience) | (the levers they have — exit, complaint, switch) | (what they cannot influence — algorithm, retention, downstream sale) | |
| Vulnerable subgroups within primary users | **Name them specifically.** Pick the ones genuinely relevant: minors / neurodivergent users / users in foster care / divorced co-parents / abuse survivors / low-income / undocumented / users in non-democratic regimes / people with disabilities / users in crisis / older adults / users with limited English / users on slow connections. Do not list categories generically; pick 2–4 actually relevant. | | | |
| Non-users in the user's environment | (people scanned, photographed, talked about, profiled by association) | | | |
| Workers in the supply chain | (moderators, gig workers, annotators, support staff) | | | |
| Future-affected populations | (people in 5 years using accumulated data; people in jurisdictions where this data could be subpoenaed; the user's future self) | | | |
| Society / public infrastructure | (epistemic commons, electoral integrity, public trust, environmental load) | | | |

**B. Power asymmetry summary.** One paragraph naming the three most significant power asymmetries between the operator and any stakeholder, with reversibility (can the affected party exit / undo / contest?).

**C. Historical-justice lens.** Has any of these populations been historically harmed by similar products / data uses / systems? If so, name the specific historical pattern (e.g., redlining via address proxies, mental-health surveillance of marginalized communities, algorithmic over-policing). The historical pattern is a prior — it shifts the burden of proof toward harm rather than away from it.

This map feeds every category below. Each category's findings must reference which stakeholders are most affected by name.

---

### Step 0.5 — Objective Function Risk Table (required for any product with optimization, ranking, scoring, or recommendation)

Before walking through the four categories, name **what the product is actually optimized for** and where that objective conflicts with stakeholder values. Stated mission ≠ optimized objective. The optimized objective is what the metrics, KPIs, model losses, and incentive structures actually maximize.

| Stated objective | Optimized objective (what the system actually maximizes) | Stakeholder value this conflicts with | Drift mechanism (how the system worsens over time on this conflict) | Mitigation owner |
|---|---|---|---|---|
| e.g., "Help children learn" | Time-on-platform; recommendation CTR | Children's autonomy, balanced development, family time | Engagement-amplified content reinforcement loop; A/B testing rewards stickier content over educational content | Head of Product + Educational Lead (joint sign-off) |

If the optimized objective and the stated objective diverge, name the gap explicitly. This is the most under-named source of ethical risk in digital products.

For products without explicit optimization (e.g., simple form-based tools), state that and proceed.

### Step 0.6 — Non-Obvious Harms Inventory (required, minimum 5 named)

Beyond the heuristic categories below, name at least **5 non-obvious harms** specific to this product. The category questions catch known harm patterns; this inventory catches the harms that don't fit pre-built categories.

For each, name: the harm, the population most affected, the mechanism by which it occurs, and whether the team had previously considered it.

| Non-obvious harm | Population most affected | Mechanism | Previously considered? |
|---|---|---|---|
| 1 | | | yes / no / partially |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

Examples of non-obvious harms to scan for (use as prompts, not a checklist):
- **Inferred-data harms**: data the system creates by inference, not collection (e.g., inferring sexuality from purchase history, mood from typing speed, immigration status from language patterns)
- **Aggregation harms**: individually innocuous signals combining to re-identify or profile
- **Proxy-variable harms**: zip code → race; school name → class; device model → income
- **Competence foreclosure**: the system replaces a skill the user would otherwise develop (e.g., navigation memory, emotion recognition, written communication)
- **Intrinsic-motivation crowd-out**: gamification or extrinsic reward replaces internal motivation
- **Attentional architecture formation**: shaping how users allocate attention even when not using the product (e.g., checking compulsion, anticipation of notifications)
- **Social fabric harms**: changes to relationships, communities, or institutions caused by widespread adoption
- **Future-you harm**: actions today that constrain the user's future choices, identity, or reputation
- **Bystander harms**: harms to non-users in the user's environment (people scanned, photographed, talked-about-by-association)
- **Worker harms**: harms to people in the supply chain (moderators exposed to harmful content, gig workers under algorithmic management, annotators with poor labor conditions)

This inventory feeds into every category below — each non-obvious harm should be referenced where the relevant heuristic applies.

### Category 1: DATA

Heuristic questions:
- Do you store/use data? What data, and why?
- How do you share data? With whom, under what conditions?
- Is data collection proportionate to the service provided?
- Are users informed about how their data is used?
- Can users access, correct, or delete their data?
- Is data anonymized where personal identification is not required?
- What happens to user data if the product shuts down?

**Output:** Data ethics assessment (what is ethical, what is at risk, what needs remediation).

---

### Category 2: AVOID MANIPULATION

Heuristic questions:
- Do you use people's values against them?
- Do you exploit people's habits or cognitive biases?
- Are behavioral nudges designed to help or to exploit?
- Does the product use fear, urgency, or social pressure to drive behavior?
- Are deceptive design techniques (dark patterns) present?
- Does the product validate users or challenge/manipulate them?

**Output:** Manipulation audit (which techniques are present, which cross the line).

---

### Category 3: MAKE INTENTIONS TRANSPARENT

Heuristic questions:
- Is it transparent to people how the product works?
- Do users understand what they're agreeing to?
- Are business incentives visible to users?
- Is the product honest about its automation and AI use?
- Can users understand why they see what they see?
- Does the product disclose when content is personalized or algorithmically curated?

**Output:** Transparency gap assessment (what users don't know that they should).

---

### Category 4: AUTOMATION

Heuristic questions:
- Is your automation fair? Who does it disadvantage?
- Can the automation be applied consistently and without bias?
- Is it responsible to automate this decision?
- Can affected people challenge automated decisions?
- Does automation remove human agency in ways that matter?
- Is the automation accountable and explainable?

**Output:** Automation ethics assessment (fairness, accountability, human oversight).

---

### Synthesis

After all four categories:
- Identify the highest-risk category (most heuristics flagged)
- **For each 🔴 finding, name the exact business pressure causing it** — the metric, KPI, or incentive structure that makes this ethical failure persist. Example: "Notification flooding persists because DAU is measured by opens, not value delivered." This attribution distinguishes a compass reading from a mechanical checklist.
- Classify each finding by implementation type: `Quick Win` (fix without changing business model) / `Strategic Fix` (requires process or priority change) / `Requires Leadership` (requires changing success metrics or business model)
- Identify systemic issues (require fundamental redesign or incentive change)
- Generate a "Compass Reading": a directional statement about where the product needs to orient

---

## Output Format

### Digital Ethics Compass: [Product Name]

Center principle: **"Put the Human in the Cosmos"**

### Stakeholder & Power Map

(From Step 0 — required. Without this, every category that follows is abstract.)

| Stakeholder (named) | Relationship to product | Power they have | Power they lack | What they lose if harmed |
|---|---|---|---|---|

**Power asymmetry summary:** [one paragraph naming the 3 most significant operator/stakeholder asymmetries and their reversibility]

**Historical-justice prior:** [one paragraph naming any pattern from history where similar products/data harmed any of these populations, and why this shifts the burden of proof toward "show this won't recur"]

### Objective Function Risk Table

(From Step 0.5 — required when the product uses optimization, ranking, scoring, or recommendation.)

| Stated objective | Optimized objective | Stakeholder value in conflict | Drift mechanism | Mitigation owner |
|---|---|---|---|---|

### Non-Obvious Harms Inventory

(From Step 0.6 — required, minimum 5 named.)

| # | Non-obvious harm | Population most affected | Mechanism | Previously considered? |
|---|---|---|---|---|
| 1 | | | | yes / no / partial |
| ... | | | | |

Avoid restating Step 0 stakeholder analysis inside each category below — reference it. Each category should add new findings, not repeat upstream framing.

### Category 1: Data

| Heuristic | Status | Notes |
|---|---|---|
| Do you store/use data? | 🔴/🟡/🟢 | [assessment] |
| How do you share data? | 🔴/🟡/🟢 | [assessment] |
| Is data collection proportionate? | 🔴/🟡/🟢 | [assessment] |

### Category 2: Avoid Manipulation

| Heuristic | Status | Notes |
|---|---|---|
| [question] | 🔴/🟡/🟢 | [assessment] |

### Category 3: Make Intentions Transparent

| Heuristic | Status | Notes |
|---|---|---|
| [question] | 🔴/🟡/🟢 | [assessment] |

### Category 4: Automation

| Heuristic | Status | Notes |
|---|---|---|
| [question] | 🔴/🟡/🟢 | [assessment] |

### Business Pressure Attribution

For each 🔴 finding, name the upstream business incentive sustaining it:

| 🔴 Finding | Business Pressure Behind It | Implementation Type |
|---|---|---|
| [finding] | [metric/KPI/incentive driving this] | Quick Win / Strategic Fix / Requires Leadership |

### Priority Improvements

Ranked by (severity × implementation ease):

1. [Quick Win — what, who, how long]
2. [Strategic Fix — what needs to change organizationally]
3. [Requires Leadership — what metric or model must change, and who decides]

### Compass Reading

*"This product puts [human need X] at risk primarily through [category Y], driven by [business pressure Z]. The most urgent reorientation is [specific change], which requires [Quick Win / leadership decision / metric change]."*

## Guardrails

- Do not skip any category. All four must be evaluated every session.
- Do not mark everything as passing. Few products are ethically flawless.
- Do not treat heuristics as pass/fail checkboxes. Each requires substantive reflection.
- Do not forget the center principle. "Put the Human in the Cosmos" frames every assessment.
- Do not ignore low-risk products. The compass should affirm ethical practice too.
- Do not limit the compass to negative findings. Identify what the product does well ethically.

## Deliverable Quality Bar

A strong Digital Ethics Compass output:

- **completes the Stakeholder & Power Map** (Step 0) with at least 5 distinct named stakeholders, including specifically-named vulnerable subgroups (not generic "users"), at least one future-affected population, and a historical-justice prior. Without this map, the compass output is abstract.
- **produces an Objective Function Risk Table** (Step 0.5) for any product with optimization/ranking/scoring/recommendation, naming the gap between stated and optimized objectives, the conflicting stakeholder values, and the drift mechanism
- **produces a Non-Obvious Harms Inventory** (Step 0.6) with at least 5 named harms beyond the heuristic categories, each with named population, mechanism, and "previously considered" honesty
- evaluates all four compass categories every session, with each finding referencing which named stakeholders are most affected, **without restating Step 0 analysis** in every category
- answers every heuristic question with a substantive assessment
- provides a remediation suggestion for every 🔴 finding
- names the specific business pressure (metric, KPI, incentive) behind every 🔴 finding
- classifies every improvement as Quick Win / Strategic Fix / Requires Leadership
- produces a Compass Reading every session that includes the business pressure driver
- maintains "Put the Human in the Cosmos" framing throughout — grounded in the named humans of Step 0, not abstract humanity
- works for both data-intensive and simpler products

## Integration with Other EDBX Skills

- **edbx-humane-design-guide** maps human sensitivities. Digital Ethics Compass maps data, automation, and manipulation practices.
- **edbx-responsible-design-prism** gives a spectrum diagnosis. Compass gives a four-category detailed audit.
- **edbx-worrystorming** generates free-form concerns. Compass provides structured heuristic categories to organize them.

## Hashtags

#breakmydesign #evaluateoutcomes

## See Also

- Design with Intent
- Responsible AI Practices
