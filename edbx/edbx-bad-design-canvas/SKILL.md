---
name: edbx-bad-design-canvas
description: Use when a designer wants to stress-test a product idea for unintended negative consequences before launch, question whether a solution addresses root causes or applies band-aids, identify who is being harmed or excluded by a design, evaluate a product across cultural, social, environmental, and safety implications, or run a structured pre-launch bad design audit across 12 consequence categories. Apply the Bad Design Canvas to systematically uncover the unintended negative consequences a product or service might generate — from cultural appropriation and inequity to environmental impact and exploitation. Trigger this skill for any mention of unintended consequences, pre-launch ethical review, who does this harm, stress-testing a design, bad design audit, break my design, or when someone says "let's think about what could go wrong with this product." Also trigger for "bad design canvas", "consequence mapping", "negative impact audit", "12 consequence categories", or "what harm does this cause."
version: "1.0"
tags: [ethical-design, audit]
---

# Bad Design Canvas

## Overview

This skill evaluates a product or service for potential or unintended "bad" consequences. It is about uncovering the new problems our "solutions" might generate, questioning our own perception of the problems we seek to solve in the first place.

Products and services have a range of impacts when released into real-use contexts and society. However, it is difficult to identify potentially "bad" impacts or unintended consequences. This skill works through a structured 12-category taxonomy so that a team looks at its idea from many angles of potential harm.

This skill is adversarial by design: it asks designers to argue against their own work. This is not pessimism; it is responsible design practice.

> **Method #09 — Bad Design Canvas.** From *Universal Methods of Ethical Design*. Hashtags: #breakmydesign #evaluateoutcomes. See also: Ethics Canvas · Judgment Call.
>
> Canvas credit: Matthew Manos, licensed under Creative Commons CC BY-ND license. Source: gum.co/baddesign
>
> **Licence:** the canvas, its twelve categories and their guiding questions are Matthew Manos's work under CC BY-ND. They are not covered by this repository's MIT License, and modified versions may not be redistributed. See [THIRD_PARTY_NOTICES.md](https://github.com/abektes/edbx-designskills/blob/main/THIRD_PARTY_NOTICES.md).

The core sequence is: **intake the idea → fill all 12 consequence cells → summarize severity → redesign against the worst findings → produce a consequence statement.**

## Use This Skill When

- You want to stress-test a product idea for negative consequences before launch.
- You need to question whether a solution addresses root causes or applies band-aids.
- You want to identify who is being harmed or excluded by a design.
- You need to evaluate a product's cultural, social, environmental, and safety implications.
- A team is about to ship something and needs a structured "bad design" audit.
- Someone says "let's think about what could go wrong with this product."
- You want a comprehensive "nothing escapes" consequence review.
- You need to convert identified harms into concrete redesign actions.

## Inputs

Provide as many of these as are available:

- **The product, service, or design concept** to evaluate (name + brief description)
- **The target community or user population** — who is this for?
- **The problem the product claims to solve** — what is it trying to fix?
- **A specific consequence category to focus on** (optional — all 12 are covered regardless)
- **Launch stage** (optional) — pre-launch ideation, live product review, or post-incident retrospective

If the user provides only the product name, proceed — the skill works from minimal input.

## The Twelve Consequence Categories

This skill uses 12 categories of potential negative consequence. Covering all 12 reduces the chance that a kind of harm is missed; it is easy to focus on two or three and overlook the rest.

| # | Category | Guiding Question |
|---|---|---|
| 1 | 🌍 Cultural Appropriation | In what way(s) is the idea borrowed from a culture you or your team are not representative of? |
| 2 | 🩹 Band-Aid | In what way(s) is the idea failing to recognize the root cause of the problem, instead serving as a temporary solution? |
| 3 | 🔒 Unfair Control | In what way(s) is the idea leading to unfair control over the user/customer? |
| 4 | ⚠️ Exploitation | In what way(s) does the new idea inappropriately expose or objectify the community it aims to serve? |
| 5 | 🔄 Inefficiency | In what way(s) is the idea creating new inefficiencies, unnecessary complexity, confusion, or delay? |
| 6 | 🌱 Environmental & Social Impact | In what way(s) is the idea using resources from finite sources or at risk of creating harsh conditions for workers? |
| 7 | 👥 Stakeholder Abandonment | In what way(s) does the idea fail to consider or address important stakeholders? |
| 8 | 🛡️ Decreased Safety | In what way(s) is the idea creating, or contributing to, unsafe conditions? |
| 9 | 🚫 Inappropriate | In what way(s) is the idea generally offensive or inappropriate? |
| 10 | 😐 Boring | In what way(s) is the idea the last, plain boring? |
| 11 | 🏠 Displacement | In what way(s) is the idea contributing to substitution or replacement? |
| 12 | ⚖️ Inequity | In what way(s) is the idea contributing to inequity? |

Full definitions, probing questions, and example responses for each category are in `references/twelve-categories.md`.

## Workflow

This skill has one integrated workflow with five steps. Run them in sequence.

---

### Step 1 — Intake

Collect from the user:

- What is the product or service idea?
- What problem does it claim to solve?
- Who is the intended community or user?
- Are there any known concerns already?
- What stage is it at? (pre-launch ideation / live product review / post-incident retrospective)

If the user provides only the product name and description, proceed. The skill works from minimal input.

---

### Step 2 — Complete the 12-Cell Canvas

For each of the 12 consequence categories, generate a specific response to the guiding question. Each response should be:

- **Specific to the product provided** — not generic observations
- **Honest and unflinching** — the point is to find the bad, not defend the design
- **Graduated by severity:**
  - `🔴 Significant` — likely, severe, and unaddressed
  - `🟡 Possible` — possible, moderate, or partially addressed
  - `🟢 Low/None` — unlikely, minor, or well-mitigated

  > **edbx adaptation:** the three-level severity scale (and `references/severity-assessment-guide.md`) is not part of the published canvas. It is here so the designer can rank findings and decide which ones need a redesign.

For each cell, provide:

1. The consequence category name and emoji
2. The guiding question (repeated for clarity)
3. A specific response grounded in the product being evaluated
4. The severity tag

**Coverage:** All 12 cells must be answered. There is no "N/A" without justification. If a category genuinely does not apply, explain why and rate it 🟢 with a brief justification.

**Tone variation for Cell 10 (Boring):** This category is intentionally lighter — it is a creative quality check, not a moral concern. Treat it with a lighter, more playful tone. A boring product is not unethical; it is just uninspired.

See `references/twelve-categories.md` for probing questions that help generate specific responses for each category.
See `references/severity-assessment-guide.md` for guidance on rating severity.

---

### Step 3 — Consequence Summary

After all 12 cells are complete:

1. **Count:** How many cells are `🔴 Significant`?
2. **Top 3:** Identify and rank the three most serious consequences
3. **Systemic vs. Addressable:** For each `🔴` finding, classify whether it is:
   - **Systemic** — requires fundamental redesign of the product concept
   - **Addressable** — can be mitigated through specific design changes without rethinking the core concept
4. **Consequence clusters:** Identify categories that reinforce each other (e.g., Exploitation + Unfair Control + Inequity often appear together)

> **edbx adaptation:** the systemic/addressable split and the consequence clusters are not part of the published canvas. They turn a list of findings into a decision about how far to redesign.

See `references/systemic-vs-addressable.md` for detailed classification guidance.

---

### Step 4 — Redesign Recommendations

> **edbx adaptation:** this redesign step is not part of the published canvas. It makes sure every serious finding ends in an action.

For each `🔴 Significant` consequence:

1. **Name one concrete design change** that would reduce or eliminate the harm
2. **Name one stakeholder** who should be involved in addressing it
3. **Ask the hard question:** "Does this consequence suggest the product should not be built at all?"

For consequences classified as **Systemic**, the redesign recommendation should address the root cause, not just the symptom. If a Band-Aid consequence is identified as systemic, the recommendation should question whether the product is solving the right problem.

---

### Step 5 — Output

Compile the full session into a structured deliverable. Open it with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title. Then:

1. **Complete 12-Cell Bad Design Canvas** — all cells answered with severity tags
2. **Top 3 Consequence Summary** — ranked list of the most serious findings
3. **Redesign Recommendations** — for every `🔴` finding
4. **Bad Design Statement** — a single declarative paragraph:

> *"The most significant unintended consequence of [product] is [X], which harms [stakeholder Y] by [mechanism Z]. This requires [redesign action]."*

   > **edbx adaptation:** the Bad Design Statement template and the build verdict below are not part of the published canvas. They give the session a decision to hand to the team.

5. **"Should we build this?" Verdict** (optional but recommended):
   - **Ship with changes** — 🔴 findings are addressable and redesign is feasible
   - **Rethink fundamentally** — 🔴 findings are systemic and the core concept needs revision
   - **Do not build** — the product causes harm that cannot be designed around
6. **Evidence Ledger** — every figure or fact about the user's situation the output relies on, typed as below

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

---

## Facilitation Notes

**Solo use:** Work through all 12 cells systematically. Do not skip categories. The categories you want to skip are often the ones with the most important findings. Use `assets/bad-design-canvas-template.md` as a blank worksheet.

**Team use:** Give each participant 5 minutes to silently fill the canvas individually before sharing. Then compare canvases — the differences between individual responses are where the richest discussion happens. Group clustering works best on a shared surface (whiteboard, Miro).

> **edbx adaptation:** the silent individual fill and the time budgets below are not part of the published canvas. They are rules of thumb for planning a session.

**Time budget:**
- Quick scan: 20–30 minutes (Steps 2–3 only, reduced responses)
- Full session: 60–90 minutes (all steps, thorough canvas)
- Workshop: 2 hours (with group discussion and redesign brainstorming)

**Stage-specific guidance:**
- **Pre-launch ideation:** Use to shape the concept before committing to a direction
- **Live product review:** Use to audit an existing product and identify harms already occurring
- **Post-incident retrospective:** Use to understand what went wrong and what the canvas would have caught

---

## Integration with Other EDBX Skills

- **edbx-worrystorming** generates free-form worries; Bad Design Canvas provides the 12-category taxonomy to organize and stress-test them systematically.
- **edbx-inverted-behavior-model** forecasts behavioral consequences; Bad Design Canvas maps the broader social, environmental, and cultural consequences.
- **edbx-humane-design-guide** maps sensitivity exploitation across 6 categories; Bad Design Canvas maps a broader 12-category consequence spectrum.
- **edbx-fair-patterns** remediates dark UI patterns; Bad Design Canvas remediates systemic design consequences beyond the interface.
- **edbx-cider** surfaces exclusionary assumptions; Bad Design Canvas maps how those assumptions lead to inequity, exploitation, and stakeholder abandonment.
- **edbx-normative-design-scheme** applies ethical theory lenses; Bad Design Canvas provides the concrete consequence taxonomy those lenses should evaluate.
- **edbx-pledge-works** formalizes commitments; Bad Design Canvas `🔴` findings are natural inputs for what to pledge against.
- **edbx-anotherlens** surfaces designer biases; Bad Design Canvas reveals the external consequences those biases produce.

See `references/related-methods.md` for detailed connections and sequencing guidance.

Run Bad Design Canvas early in a project to shape concept direction, or late as a comprehensive pre-launch audit.

---

## Guardrails

- **Do not skip categories.** All 12 cells must be answered. The categories you resist are often the most revealing.
- **Do not defend the design.** The canvas is an adversarial tool. Its job is to break the design, not protect it.
- **Do not sanitize the output.** If a finding feels uncomfortable to name, that is the signal. The hardest consequences to articulate are often the most important.
- **Do not judge the designer.** Bad consequences in a design are not accusations against its creators. The method is generative, not punitive.
- **Treat "Boring" differently.** It is a creative quality check, not a moral judgment. Keep the tone lighter for this cell.
- **Address every `🔴` finding.** A significant consequence without a redesign recommendation is an incomplete canvas.
- **Use the Bad Design Statement as a decision artifact.** It should be specific enough to guide the next design decision or stop the project.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.
- Do not stop to ask for more details before answering: draft the full deliverable with unknowns marked, and list the questions worth asking the user at the end.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

## Deliverable Quality Bar

A strong Bad Design Canvas session output:

- answers all 12 cells with product-specific responses (not generic observations)
- rates every cell with a justified severity tag
- identifies and ranks the top 3 most serious consequences
- classifies every `🔴` finding as systemic or addressable
- proposes a concrete redesign action for every `🔴` finding
- produces a Bad Design Statement that names the harm, the stakeholder, and the action
- includes a "should we build this?" verdict grounded in the evidence
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

## Example Output (partial)

> **Product evaluated:** A food delivery app that uses gig workers, surge pricing, and gamified delivery streaks
> **Stage:** Pre-launch ideation
>
> **Cell 4: EXPLOITATION ⚠️ — 🔴 Significant**
> The app commercializes both gig workers and hungry users. Workers have no labor protections, benefits, or stability — they are the product being sold to restaurants. Surge pricing exploits users in food deserts who have no alternative. The gamified delivery streaks turn worker desperation into engagement metrics.
>
> **Cell 6: ENVIRONMENTAL & SOCIAL IMPACT 🌱 — 🔴 Significant**
> Gig worker conditions constitute harsh labor conditions: no healthcare, no minimum wage guarantees, algorithmic management with no human recourse. At scale, this creates a precarious workforce. Single-use packaging from every order adds environmental cost.
>
> **Cell 11: DISPLACEMENT 🏠 — 🔴 Significant**
> The app displaces local restaurant delivery infrastructure, replacing employed delivery staff with gig workers who earn less. It displaces cooking as a daily practice for time-pressed users, increasing dependency on delivered food.
>
> **Top 3 Consequences:**
> 1. Exploitation — workers and users are commodified
> 2. Environmental & Social Impact — gig precarity at scale
> 3. Displacement — local infrastructure and food culture eroded
>
> **Bad Design Statement:**
> "The most significant unintended consequence of this food delivery app is the systematic exploitation of gig workers, who are treated as disposable infrastructure rather than human stakeholders, which harms workers by removing labor protections, fair wages, and stability. This requires fundamental redesign of the worker relationship model — or the product should not be built in its current form."
>
> **Verdict: Rethink fundamentally** — the core business model (gig labor + surge pricing) generates systemic exploitation that cannot be designed around without changing what the product is.
