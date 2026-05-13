---
name: edbx-dah-cards
description: Use when a designer wants to stress-test a product idea or existing feature for negative impacts, explore the dark side of something they're building, ask "is this ethical?", check for unintended harms, reflect on design responsibility, define their design values, or articulate what kind of designer they want to be. Run a DAH (Design Against Humanity) Cards session to audit products and features for ethical harms, map hidden consequences, build a personal ethical manifesto, and draft a future design vision. Also trigger for phrases like "ethical review", "dark patterns audit", "design against humanity", "responsible design", "value alignment", or any moment when a team is uncomfortable with where a product is going.
version: "1.0"
tags: [ethical-design, audit]
---

# DAH Cards

## Overview

DAH — Design Against Humanity — is a reflective method that exposes designers to the real-world harms that products, features, and services can cause. Named as a provocation (a design version of Cards Against Humanity), it flips the usual design question from "what does this do for people?" to "what does this do *to* people — and to the world?"

The original method uses physical cards: the black side names a product or feature, the white side describes its problematic consequences. Designers sort cards into **Ethical**, **Unsure**, and **Unethical**, then step back and ask: *"What changed?"* — meaning: what assumptions shifted, what discomfort surfaced, what felt different than expected?

This AI-assisted version preserves that reflective spirit. It works with anything: a product concept, an existing feature, a full service, or a list of items the team is wrestling with.

> **Intent check:** This skill is explicitly critical by design — it surfaces problems and harms. Use it alongside (not instead of) conventional benefits analysis. The goal is self-aware, responsible design, not paralysis.

## Use This Skill When

- You want to audit a product or feature for ethical risks before shipping.
- You suspect something you're building has unintended negative consequences.
- A team needs a structured way to discuss design responsibility.
- You want to build or update your ethical design manifesto.
- You want to articulate a future vision of the kind of products you *do* want to make.
- You've heard "dark patterns", "addictive design", or "data exploitation" and want to check whether they apply to your work.

## Inputs

Provide as many of these as are available:

- The product, feature, service, mechanism, or object to evaluate (name + brief description)
- Who uses it and in what context
- Any known concerns, complaints, or controversies
- Business model context (how it makes money, what it optimizes for)
- Any previous ethical reviews or feedback
- The team's ethical framework leanings, if known

If you have multiple items to evaluate, list them — the sorting exercise is more useful with variety.

## Workflow

This skill has four modes. **Mode selection rule:** match modes to the user's actual ask.

- Audit / "run DAH on X" / "identify dark patterns" / "ethical review" → run **Modes 1 + 2 only**, then the Ship-Ready Recommendation. Do NOT auto-include Modes 3–4.
- "Help us write a manifesto" / "what should we commit to" → run Modes 1, 2, **3** (skip 4 unless requested).
- "What products do we want to make instead" / "future vision" → run Modes 1, 2, **4** (skip 3 unless requested).
- Explicit request for both → run all four.

Including Modes 3–4 when the user only asked for an audit dilutes actionability and is treated as padding.

---

### Mode 1: DAH Card Pairs + Consequence Mapping

**Step 1a — Generate the DAH Card Pairs (the method's signature artifact).**

Before any analysis, write out the cards. The DAH method is named for the card-pair format — every audit must produce them.

For each feature/mechanic being evaluated, write a black-side / white-side pair, **categorized by harm type**. Each card pair is tagged with one or more of the six DAH harm categories:

- **Deception** — the design hides, misrepresents, or misleads (dark patterns, false expectations, opaque defaults)
- **Coercion** — the design removes meaningful choice (forced continuity, roach motel, lock-in, hard-to-cancel)
- **Addiction** — the design exploits compulsion mechanisms (variable rewards, streak loss aversion, infinite scroll, near-miss design)
- **Surveillance** — the design monitors, profiles, or extracts beyond what the user signed up for (behavioral telemetry, inferred data, third-party sharing, retention beyond purpose)
- **Exclusion** — the design works against specific populations (accessibility failures, language/literacy gaps, economic gates, identity assumptions, algorithmic bias against subgroups)
- **Systemic** — the design contributes to harms beyond the individual user (normalization of manipulation, market homogenization, environmental load, erosion of public discourse, civilizational-scale effects)

A single mechanic can fall into multiple categories — tag every category that applies.

| Card # | Category | Black side (the design) | White side (its harm, named bluntly) |
|---|---|---|---|
| 1 | Addiction + Systemic | [Feature, mechanic, or copy as it ships] | [Concrete harm in plain language — what it does to a real person, not abstract framing] |
| 2 | Deception | ... | ... |

Write the white side in the voice of someone who has been harmed by the design, not in the voice of a designer apologizing. "Streak system that punishes you with shame copy if you miss a day" is a white-side card. "May reduce user wellbeing" is not.

Generate at least one card pair per distinct mechanic. **Coverage requirement:** the full set of cards must include at least one card in **at least 4 of the 6 categories** — if four or more categories are absent, the audit is too narrow, go back and look harder. Systemic harms are the most commonly missed category; do not skip them.

**Step 1b — Consequence Mapping (depth behind the white side).**

For each card pair, surface the full set of problematic consequences across multiple harm dimensions:

For each product or feature, surface its problematic consequences across multiple harm dimensions:

**Individual harms**
- Psychological: addiction, anxiety, distorted self-image, manipulation of behavior
- Physical: sedentary behavior, sleep disruption, sensory overload, safety risk
- Financial: exploitation of vulnerability, hidden costs, debt spirals
- Privacy: surveillance, data exploitation, loss of control over identity

**Social and relational harms**
- Relationship quality: isolation, comparison culture, social pressure
- Equity and access: who is excluded, who bears the most risk, who benefits least
- Labor: precarity, surveillance of workers, erosion of skill
- Power dynamics: concentration of control, erosion of alternatives

**Environmental and systemic harms**
- Resource consumption: energy, materials, waste
- Infrastructure dependency: lock-in, monopoly, fragility
- Cultural: homogenization, erasure of local practice, normalization of harmful behavior
- Systemic feedback: what this product makes normal, what it makes invisible

Do not only list extreme harms. Minor frictions, small erosions of trust, and quiet exclusions count too — they accumulate.

For each consequence identified, note:
- **How likely** is this harm? (common / possible / edge case)
- **How severe** is it? (inconvenient / meaningful / serious / irreversible)
- **Who bears it?** (user / non-user / worker / environment / society)
- **Does the design know about it?** (known and accepted / known and ignored / not considered)

---

### Mode 2: Ethical Sorting

Once consequences are mapped, sort the product(s) into one of three categories:

**Ethical** — The product delivers genuine value. Its harms are minor, well-understood, mitigated where possible, and clearly outweighed by benefits. The team can defend every significant design decision.

**Unsure** — The product has real benefits *and* real harms. The balance is unclear, contextual, or contested. More investigation, stakeholder input, or constraint is needed before a confident verdict.

**Unethical** — The product's harms are serious, disproportionate, poorly mitigated, or designed in deliberately. The team would struggle to defend the design publicly to those it hurts.

After sorting, ask the **"What changed?"** reflection:

- Which card surprised you? Why?
- Did anything land in a different category than you expected?
- What assumption shifted during the exercise?
- Where did team members disagree — and what does that disagreement reveal?
- Is there anything in "Ethical" that you'd quietly move to "Unsure" if you had to justify it to the people it affects?

This reflection is the heart of the method. Sorting is just the setup.

---

### Mode 3: Ethical Manifesto

> **Artifact delivery rule:** If the team has not yet completed a consequence mapping or sorting exercise, do not wait for it. State your best-estimate consequences and sorting verdict explicitly as working assumptions, then proceed directly to manifesto writing. Name the assumptions. Do not block artifact delivery on missing pre-work.

Use the sorting exercise (or your stated assumptions) as raw material for a personal or team ethical design manifesto. A manifesto is not a policy document — it's a commitment written in the first person that captures what you believe design should and should not do.

Structure:

**I/We believe design should...**
(3–5 active commitments grounded in what the sorting revealed — e.g., "make harms visible before shipping, not after")

**I/We will not...**
(2–4 explicit refusals — what design practices or outcomes you won't participate in)

**When we are unsure, we will...**
(A process commitment — how to handle the grey zone before defaulting to shipping)

**We define success as...**
(A restatement of value that includes wellbeing, not just engagement or revenue)

Keep it honest and specific. Vague manifestos feel good and change nothing. Specific ones create friction — that friction is the point.

**Microcopy Rewrite (required for each Unethical finding):**
For every item sorted Unethical, rewrite the specific UI copy, mechanic name, or on-screen framing that obscures the harm:
- **Before:** [current copy or mechanic as it appears to users]
- **After (honest version):** [what it would say if it named what it actually does]

If there is no specific copy to rewrite, identify the mechanic name and propose an honest design label (e.g., "Infinite scroll" → "Automatic content injection with no stopping point").

---

### Mode 4: Future Design Vision

Based on the Ethical and Unsure categories, draft a vision for the kinds of products you *want* to design going forward.

Structure:

**The problem with what I'm designing now**
(Honest acknowledgment of the harms identified — even in things you're proud of)

**The shift I want to make**
(What direction feels more aligned with your values — even if it's uncertain)

**Three products or features I'd want to exist**
(Concrete, specific ideas — not manifestations of goodness but actual design concepts grounded in what the audit revealed)

**What would have to change to make them viable**
(Constraints, incentives, business model shifts, or policy changes that would need to exist)

This mode works best after the sorting and reflection. The discomfort of Mode 2 is the fuel for Mode 4.

---

## Output Format

Default structure unless the user asks otherwise:

### DAH Cards Session

Brief framing of what was evaluated and the team's starting assumptions.

### DAH Card Pairs

Black-side / white-side table for every mechanic evaluated (from Mode 1, Step 1a), with each card tagged by its DAH harm categories: **Deception / Coercion / Addiction / Surveillance / Exclusion / Systemic**. This is the signature artifact — never omit it. If everything is on one row of consequence-map text, the cards weren't actually written. Coverage must span at least 4 of the 6 categories; systemic harms must be considered explicitly.

### Consequence Map

One section per product or feature evaluated. Use the harm dimensions from Mode 1. Flag each consequence with likelihood, severity, who bears it, and whether the design knows about it.

### Sorting Verdict

A table showing each item sorted into Ethical / Unsure / Unethical with a one-line rationale.

### What Changed?

Key reflections from the sorting — surprises, disagreements, shifted assumptions.

### Manifesto (if requested)

Personal or team ethical commitments in the format from Mode 3.

### Future Vision (if requested)

Design direction and concrete product concepts from Mode 4.

### Ship-Ready Recommendation

One concrete design change the team can implement in the next sprint — specific enough to write a ticket for. Not a principle, not an aspiration: a named feature modification. Example: "Replace infinite scroll with a 'Load 10 more' button after every 10 items" or "Add a session summary screen after 20 minutes with an explicit 'Keep browsing' choice."

---

## Guardrails

- Do not flatten the ethical spectrum into a binary pass/fail. The Unsure category is not a cop-out — it's the most honest place to put most real products.
- Do not assume harm only happens at the extremes. Cumulative, mundane harms (mild anxiety from notifications, slight erosion of attention) matter and should be named.
- Do not treat this exercise as a box to check. If it generates no discomfort, something is missing — real products have real trade-offs.
- Avoid using the manifesto to make the team feel better without changing anything. If commitments are made, surface what design decisions they would change.
- When evaluating your own work, apply the same scrutiny you would to a competitor's product.

## Deliverable Quality Bar

A strong DAH Cards session output:

- produces explicit DAH Card Pairs (black side = mechanic, white side = harm) for every feature evaluated, **each tagged by harm category** (Deception / Coercion / Addiction / Surveillance / Exclusion / Systemic), with coverage spanning at least 4 of the 6 categories — this is the signature artifact
- names at least 5–8 distinct consequences per product across multiple harm dimensions
- distinguishes between likely and edge-case harms without dismissing either
- lands on verdicts that feel slightly uncomfortable — if everything is Ethical, the audit was too gentle
- surfaces at least one genuine surprise or disagreement
- includes a microcopy rewrite (before/after) for every Unethical finding
- provides one ship-ready design recommendation specific enough to write a sprint ticket for
- matches mode selection to the user's actual ask — does NOT include Manifesto or Future Vision when only an audit was requested
- when Manifesto IS requested: produces commitments specific enough to create friction in future decisions
- when Future Vision IS requested: grounds the vision in the audit's findings, not abstract idealism

## Example Output (partial)

> **Product evaluated:** Infinite scroll feed, mobile social app
>
> **Consequence map (sample):**
> | Consequence | Likelihood | Severity | Who bears it | Design awareness |
> |---|---|---|---|---|
> | Compulsive checking behavior ("snacking") | Common | Meaningful | User | Known, optimized for |
> | Near-miss loss mechanics increase session length | Common | Meaningful | User | Known, optimized for |
> | Sleep disruption from late-night use | Common | Serious | User | Known, not mitigated |
> | Lower-quality social interaction vs. in-person | Possible | Meaningful | User + relationships | Not considered |
> | Algorithmic amplification of anxiety-inducing content | Common | Serious | User | Known, contested internally |
>
> **Verdict:** Unsure → leaning Unethical
>
> **Rationale:** Core mechanic is deliberately designed to override user intent (Unsure). Business model alignment with engagement over wellbeing is structural, not incidental (Unethical signal). No meaningful mitigation exists.
>
> **What changed?** "We always said infinite scroll was just a neutral UX pattern. Mapping it against sleep disruption and compulsive behavior made it feel much less neutral. The team disagreed about whether 'we didn't invent it' was a real defense."
>
> **Manifesto excerpt:**
> "We will not design for engagement when we know engagement is coming at the cost of sleep, attention, or real-world relationships. We will not call a mechanic 'neutral' when we know what it optimizes for."
