---
name: edbx-digital-ethics-compass
description: Use when a designer, product manager, or AI practitioner wants to reflect on the ethical dimensions of data collection and use, evaluate automation and AI features for manipulation or unfairness, assess whether intentions and processes are transparent to users, apply a structured heuristic framework to data-intensive or AI-powered products, or run a broad ethical health check on a product. Apply the Digital Ethics Compass heuristics to evaluate a product against the Danish Design Center's five principles and its 22 questions in three categories — Data, Automation, and Behavioral Design — putting the human at the center of every decision. Trigger this skill for any mention of data ethics, AI ethics, automation ethics, behavioral manipulation, transparency obligations, responsible AI, or when someone asks "is our data practice ethical?" Also trigger for "Digital Ethics Compass", "data ethics audit", "AI ethics", "automation fairness", "responsible AI", or "ethical health check".
version: "1.0"
tags: [ethical-design, audit]
---

# Digital Ethics Compass

## Overview

Digital Ethics Compass, a tool by the Danish Design Center (DDC, 2021), guides you to reflect on your product and business development goals through heuristics relating to data, automation, and behavioral design. It helps companies and design teams make everyday design decisions from an ethical standpoint.

DDC publishes the compass as a checklist called the Ethics Navigator. In the middle are **five principles** of responsible digital design: **Put the Human at the Center**, **Avoid manipulating**, **Make your technology understandable**, **Avoid creating inequality**, and **Give users control**. The outer ring holds **22 questions** in three categories: **Data** (6), **Automation** (10), and **Behavioral Design** (6). This skill follows that structure. DDC also offers a facilitated ethics workshop; this skill covers the heuristic checklist only, and the workshop is not reproduced here.

Source: Dansk Design Center, *The Digital Ethics Compass* (ddc.dk/tools/toolkit-the-digital-ethics-compass/). DDC's site footer states its content is under a Creative Commons Attribution License (version not given); the question wording below is paraphrased. This skill can be applied to a single feature or to a whole product.

> **Mindset check:** "Put the Human at the Center" is not just a slogan — it is the orienting principle for every heuristic question. If the human is not at the center, the compass reading is off.

## Use This Skill When

- You want to evaluate a product's ethical dimensions across data, automation, and behavioral design.
- You are working on data-intensive or AI-powered products.
- You need to assess whether your data practices are ethical.
- You want to evaluate automation and AI features for fairness and manipulation.
- You need to check whether your technology is understandable to users and leaves them in control.
- You want a broad ethical health check on a product.

## Inputs

Provide as many of these as are available:

- A product, service, or feature with data, automation, or behavioral design components
- Optionally: a specific category to focus on (Data / Automation / Behavioral Design)
- Optionally: a business model or data practice to evaluate
- Optionally: a specific user population or context

## Workflow

The compass reads the product against five principles, then asks 22 questions in three categories, with "Put the Human at the Center" as the orienting principle throughout. DDC's own page says the human at the center is everyone your solution may affect, not only users and customers.

> **edbx adaptation:** Steps 0, 0.5 and 0.6 (Stakeholder & Power Map, Objective Function Risk Table, Non-Obvious Harms Inventory) are not part of the published compass; they are required here before any question is scored. The Stakeholder Map makes the "everyone affected" point explicit; without it, "Put the Human at the Center" remains an abstraction.

---

### Step 0 (required): Stakeholder & Power Map

Before walking through the principles and categories, enumerate every population the design touches. The judges' most consistent complaint about Compass output is that stakeholder mapping stays implicit. Make it explicit. This is mandatory output, not optional.

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

Before walking through the principles and categories, name **what the product is actually optimized for** and where that objective conflicts with stakeholder values. Stated mission ≠ optimized objective. The optimized objective is what the metrics, KPIs, model losses, and incentive structures actually maximize.

| Stated objective | Optimized objective (what the system actually maximizes) | Stakeholder value this conflicts with | Drift mechanism (how the system worsens over time on this conflict) | Mitigation owner |
|---|---|---|---|---|
| e.g., "Help children learn" | Time-on-platform; recommendation CTR | Children's autonomy, balanced development, family time | Engagement-amplified content reinforcement loop; A/B testing rewards stickier content over educational content | Head of Product + Educational Lead (joint sign-off) |

If the optimized objective and the stated objective diverge, name the gap explicitly. This is the most under-named source of ethical risk in digital products.

For products without explicit optimization (e.g., simple form-based tools), state that and proceed.

### Step 0.6 — Non-Obvious Harms Inventory (required, minimum 5 named)

Beyond the heuristic questions below, name at least **5 non-obvious harms** specific to this product. The compass questions catch known harm patterns; this inventory catches the harms that don't fit pre-built categories.

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

### Step 1: Read the product against the five principles

DDC's five principles sit in the middle of the Ethics Navigator and frame every question. For each, say in a sentence or two how the product honours or breaks it, and which named stakeholders it affects most. Keep it short: the 22 questions below carry the detail.

- **Put the Human at the Center:** does the design account for everyone it may affect, including people with disabilities, future consequences (such as overuse or harm) and control over their own data?
- **Avoid manipulating:** does the product help people decide, or does it undermine their basic urge to decide over their own lives (targeting, retargeting, behavioral design, algorithms used to steer buying)?
- **Make your technology understandable:** can ordinary people comprehend how the product works and affects their lives, with consequences explained in the interaction itself rather than in a document nobody reads?
- **Avoid creating inequality:** could the product reinforce or widen existing imbalances, for example by penalising people an algorithm misjudges?
- **Give users control:** does the product leave people with more control, not less, or a sense of losing it?

> **edbx adaptation:** extra prompts under *Make your technology understandable*: are business incentives visible to users, and is it disclosed when content is personalized or algorithmically curated? They are not among DDC's questions; they keep the transparency checks of earlier versions of this skill.

### Category 1: DATA (6 questions)

- Are you collecting more data points than you need, or keeping them longer than needed?
- Do you anonymise the data?
- How is the data stored?
- Can people access their own data?
- Have you obtained real permission to collect and process the data, with users understanding what they agree to?
- Do you tell users how they are profiled?

> **edbx adaptation:** two extra prompts, not among DDC's six Data questions: how is data shared, with whom and under what conditions; and what happens to user data if the product shuts down. Add them as extra rows if they apply.

**Output:** Data ethics assessment (what is ethical, what is at risk, what needs remediation).

---

### Category 2: AUTOMATION (10 questions)

- Do users know they are interacting with an automated solution?
- Does the automation comply with legislation and human rights?
- Does automation make people lose the abilities needed to do a job?
- Is the system transparent enough that the user can see how it works inside (the "engine room")?
- Can the system explain itself?
- Are the algorithms prejudiced?
- Is there an unnecessarily high risk in the automated system?
- Is someone in the company ready to step in when automation fails?
- Can the system adapt to changes?
- Can the system be hacked?

> **edbx adaptation:** two extra prompts, not among DDC's ten Automation questions: is it responsible to automate this decision at all, and can affected people challenge an automated decision? Add them as extra rows if they apply.

**Output:** Automation ethics assessment (fairness, accountability, human oversight, security).

---

### Category 3: BEHAVIORAL DESIGN (6 questions)

- Does the design play on negative emotions (fear, urgency)?
- Do you deliberately make it hard for users to find or understand information or functionality?
- Do you exploit users' inability to concentrate to your own advantage?
- Do you manipulate actions by exploiting people's need to be social?
- Are you trying to create addiction with cheap tricks?
- Do you validate your users or challenge them?

Deceptive design techniques (dark patterns) are covered by the second question.

**Output:** Manipulation audit (which techniques are present, which cross the line).

---

### Synthesis

> **edbx adaptation:** the synthesis below (business-pressure attribution, the Quick Win / Strategic Fix / Requires Leadership classification, the 🔴/🟡/🟢 status, and the Compass Reading) is not part of the published compass. It turns the findings into decisions and names why each failure persists.

After the principles and all three categories:
- Identify the highest-risk category (most heuristics flagged)
- **For each 🔴 finding, name the exact business pressure causing it** — the metric, KPI, or incentive structure that makes this ethical failure persist. Example: "Notification flooding persists because DAU is measured by opens, not value delivered." This attribution distinguishes a compass reading from a mechanical checklist.
- Classify each finding by implementation type: `Quick Win` (fix without changing business model) / `Strategic Fix` (requires process or priority change) / `Requires Leadership` (requires changing success metrics or business model)
- Identify systemic issues (require fundamental redesign or incentive change)
- Generate a "Compass Reading": a directional statement about where the product needs to orient

---

## Output Format

Open with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title.

### Digital Ethics Compass: [Product Name]

Center principle: **"Put the Human at the Center"**

### Answer

[Two to four sentences: the answer to the question asked (decision, verdict or recommendation) and the main reason.]

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

### Principles Reading

(From Step 1.) One row per principle, referencing the named stakeholders most affected.

| Principle | Status | Notes |
|---|---|---|
| Put the Human at the Center | 🔴/🟡/🟢 | [assessment] |
| Avoid manipulating | 🔴/🟡/🟢 | [assessment] |
| Make your technology understandable | 🔴/🟡/🟢 | [assessment] |
| Avoid creating inequality | 🔴/🟡/🟢 | [assessment] |
| Give users control | 🔴/🟡/🟢 | [assessment] |

### Category 1: Data

One row for each of the six Data questions.

| Heuristic | Status | Notes |
|---|---|---|
| Collecting more data than needed, or keeping it too long? | 🔴/🟡/🟢 | [assessment] |
| Is the data anonymised? | 🔴/🟡/🟢 | [assessment] |
| ... | 🔴/🟡/🟢 | [assessment] |

### Category 2: Automation

One row for each of the ten Automation questions.

| Heuristic | Status | Notes |
|---|---|---|
| [question] | 🔴/🟡/🟢 | [assessment] |

### Category 3: Behavioral Design

One row for each of the six Behavioral Design questions.

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

### Evidence Ledger
| Claim used as input | Type | Basis |
|---|---|---|
| [figure, rate or fact the output relies on] | [user-supplied / sourced / assumption / unknown] | [the brief / paper or URL / why assumed] |

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

## Guardrails

- Do not skip any category or principle. All five principles and all three categories must be evaluated every session.
- Do not mark everything as passing. Few products are ethically flawless.
- Do not treat heuristics as pass/fail checkboxes. Each requires substantive reflection.
- Do not forget the center principle. "Put the Human at the Center" frames every assessment.
- Do not ignore low-risk products. The compass should affirm ethical practice too.
- Do not limit the compass to negative findings. Identify what the product does well ethically.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.
- Do not stop to ask for more details before answering: draft the full deliverable with unknowns marked, and list the questions worth asking the user at the end.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

## Deliverable Quality Bar

A strong Digital Ethics Compass output:

- **completes the Stakeholder & Power Map** (Step 0) with at least 5 distinct named stakeholders, including specifically-named vulnerable subgroups (not generic "users"), at least one future-affected population, and a historical-justice prior. Without this map, the compass output is abstract.
- **produces an Objective Function Risk Table** (Step 0.5) for any product with optimization/ranking/scoring/recommendation, naming the gap between stated and optimized objectives, the conflicting stakeholder values, and the drift mechanism
- **produces a Non-Obvious Harms Inventory** (Step 0.6) with at least 5 named harms beyond the heuristic categories, each with named population, mechanism, and "previously considered" honesty
- reads the product against the five principles and evaluates all three compass categories (Data, Automation, Behavioral Design) every session, with each finding referencing which named stakeholders are most affected, **without restating Step 0 analysis** in every category
- answers every heuristic question with a substantive assessment
- provides a remediation suggestion for every 🔴 finding
- names the specific business pressure (metric, KPI, incentive) behind every 🔴 finding
- classifies every improvement as Quick Win / Strategic Fix / Requires Leadership
- produces a Compass Reading every session that includes the business pressure driver
- maintains "Put the Human at the Center" framing throughout — grounded in the named humans of Step 0, not abstract humanity
- works for both data-intensive and simpler products
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

## Integration with Other EDBX Skills

- **edbx-humane-design-guide** maps human sensitivities. Digital Ethics Compass maps data, automation, and manipulation practices.
- **edbx-responsible-design-prism** gives a spectrum diagnosis. Compass gives a detailed audit against five principles and 22 questions in three categories.
- **edbx-worrystorming** generates free-form concerns. Compass provides structured heuristic categories to organize them.

## Hashtags

#breakmydesign #evaluateoutcomes

## See Also

- Design with Intent
- Responsible AI Practices
