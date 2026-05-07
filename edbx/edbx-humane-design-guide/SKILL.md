---
name: edbx-humane-design-guide
description: Use when a designer, researcher, or product manager wants to audit how a product exploits human vulnerabilities, identify where design harms attention or emotional wellbeing, surface dark patterns around addiction or deception, generate opportunity areas for more humane product design, or evaluate against Center for Humane Technology principles. Apply the Humane Design Guide framework to evaluate a product or feature against six human sensitivities — Attention, Emotional, Sensemaking, Decision-making, Social Reasoning, and Group Dynamics — and generate humane design alternatives. Trigger this skill for any mention of humane technology, attention exploitation, addictive design, emotional harm in UX, filter bubbles, dark patterns in social products, or when someone asks "is this product respecting its users?" Also trigger for "humane design", "human sensitivities", "attention design", "digital wellbeing", "center for humane technology", or "humane design guide".
metadata:
  version: "1.0"
---

# Humane Design Guide

## Overview

The Humane Design Guide evaluates products against six human sensitivities that digital technology can exploit: attention, emotional state, sensemaking, decision-making, social reasoning, and group dynamics. It was developed by the Center for Humane Technology as a practical worksheet for design teams.

The method is structured around a simple idea: technology can take advantage of how humans think and feel, making people act in ways they would not otherwise choose. The guide makes those exploitation patterns visible and replaces them with humane alternatives framed as what users are *enabled to* do.

> **Method #47 — Humane Design Guide.** From *Universal Methods of Ethical Design*. Source: Center for Humane Technology — humanetech.com. Hashtags: #breakmydesign #evaluateoutcomes. See also: Maslow Mirrored · Well-Being Design Cards.

The worksheet is the primary output artifact. This skill produces a filled worksheet equivalent — six rows (one per sensitivity), four columns per row — every time it runs.

## Use This Skill When

- You want to audit a product or feature for humane design violations.
- You suspect the product exploits attention, emotion, or decision-making.
- A team needs a structured sensitivity-by-sensitivity evaluation.
- You want to generate "Enabled to..." improvement opportunities.
- You are evaluating against Center for Humane Technology principles.
- Someone asks "is this product respecting its users?"

## Inputs

Provide as many of these as are available:

- **Product or feature** name and description
- **Value proposition** — what the product claims to offer users
- **Measures of success** — how the organization measures performance (DAU, session time, notification CTR, etc.). These often reveal exploitation intent — engagement metrics can signal where the product optimizes for extraction over wellbeing.
- **Known concerns** or complaints
- **A specific sensitivity to focus on** (optional — by default, all six are assessed)

## The Six Human Sensitivities

Each sensitivity describes a human capacity that can be inhibited or supported by design.

| Sensitivity | Definition | Inhibited When... | Supported When... → Enabled to... |
|---|---|---|---|
| **Attention** | How and where we focus | Fragmented, driven, overwhelmed | Find focus and peace |
| **Emotional** | What we feel in our body and health | Overwhelmed, afraid, stressed | Process and adapt |
| **Sensemaking** | How we integrate sense with knowledge | Fear-based, out of context, misleading | Find truth and clarity |
| **Decision-making** | How we align actions with intentions | Agency not supported or requested | Act with agency and control |
| **Social Reasoning** | How we navigate relationships | Status, self-image manipulated | Connect meaningfully |
| **Group Dynamics** | How we navigate groups and shared understanding | Excluded, divided, managed through fear | Build strong communities |

Full definitions, inhibition states, and support states are in `references/six-sensitivities.md`.

## Workflow

This skill has one integrated workflow. Run all four steps in sequence.

---

### Step 1 — Intake

Collect from the user:

- The product or feature name and description
- The value proposition (what it claims to do for users)
- Current measures of success (metrics, KPIs, optimization targets)
- Any known concerns

Pay attention to the measures of success. Metrics like "average session time," "notification click-through rate," or "daily streaks maintained" often indicate that the product optimizes for extraction rather than wellbeing. Flag these explicitly when they appear.

If the user has not provided a value proposition or measures of success, ask concisely before proceeding. You need at least the product description to run a meaningful audit.

---

### Step 2 — Sensitivity Audit

For each of the six sensitivities, assess four dimensions:

**1. Current State:** How does the product currently engage or exploit this sensitivity? Map against known exploitation patterns:

- **Attention:** infinite scroll, nudging, notification flooding, sensory overload, autoplay
- **Emotional:** currency of likes, aspirational filters, fear-based framing, shame mechanics
- **Sensemaking:** filter bubbles, misleading labels, information as noise, out-of-context framing, algorithmic amplification
- **Decision-making:** dark patterns, removing agency, forced choices, hidden defaults, confirmshaming
- **Social Reasoning:** status manipulation, self-image exploitation, social comparison, FOMO mechanics
- **Group Dynamics:** polarizing algorithms, exclusion mechanics, fear-based division, us-vs-them framing

The full exploitation pattern library is in `references/exploitation-pattern-library.md`.

**2. What's at Risk:** Name the human harm. Be specific — not "users might feel bad" but "users lose capacity to self-regulate attention during evening hours, leading to sleep disruption."

**3. Opportunity Level:** Score as:
- `🔴 High` — the product actively exploits this sensitivity
- `🟡 Medium` — the product touches this sensitivity with some risk
- `🟢 Low` — the product respects this sensitivity well

**4. Improvement Opportunity:** Frame using the "Enabled to..." format:
- Attention → *Enabled to find focus and peace*
- Emotional → *Enabled to process and adapt*
- Sensemaking → *Enabled to find truth and clarity*
- Decision-making → *Enabled to act with agency and control*
- Social Reasoning → *Enabled to connect meaningfully*
- Group Dynamics → *Enabled to build strong communities*

**5. Named Psychological Mechanism (required for every 🔴 and 🟡 row):** Naming "manipulation" is not enough. Name the **specific psychological mechanism** the design exploits, using precise terminology. If you cannot name a mechanism, the diagnosis is too shallow.

Use these named-mechanism categories:

- **Cognitive biases:** default bias, loss aversion, anchoring, social proof, scarcity heuristic, sunk-cost fallacy, present bias, availability heuristic
- **Behavioral mechanisms:** variable reward schedule (intermittent reinforcement), streak-loss aversion, near-miss design, autoplay/infinite-scroll exploiting attentional residue, friction asymmetry (easy in / hard out), cognitive depletion (late-night decisions)
- **Emotional vulnerabilities:** FOMO, social anxiety / belonging needs, identity entanglement, status threat, grief / loneliness / boredom states
- **Developmental vulnerabilities** (when minors are in scope): incomplete prefrontal development, peer-comparison sensitivity in adolescence, identity formation pressure
- **Algorithmic-bias mechanisms:** engagement amplification of anxiety-provoking content, Elo-style scoring carrying historical participation bias, beauty-filter colorism amplifying narrow aesthetic norms, ranking systems converting demographic proxies into "merit"

Generic "feels manipulative" is not a mechanism. "Variable reward schedule on the like counter producing checking compulsion" is.

**6. Differential Impact (required, multi-population):** For each sensitivity, name **at least 2 specifically-vulnerable populations** that experience this harm most acutely — not "all users." For each, name the mechanism of differential vulnerability.

Examples: adolescents (developmental peer-comparison sensitivity); shift workers (cognitive depletion at off-hours); people with eating disorders (Emotional sensitivity on fitness/wellness/beauty apps); women and racial minorities re: beauty filters (colorism / narrow aesthetic norms baked into training data); gig workers (Decision-making under forced continuity, no negotiating power); elderly users with low digital literacy (Sensemaking under algorithmic curation); users with anxiety disorders (engagement-amplified anxiety content); low-income users (default-bias on opt-out paid features).

Present the audit as a filled worksheet table:

| Sensitivity | Current State | What's at Risk | Level | Named Mechanism (specific) | Most Affected Populations (≥2 named, with mechanism of differential harm) | Enabled to... |
|---|---|---|---|---|---|---|
| Attention | ... | ... | 🔴/🟡/🟢 | e.g., "infinite scroll exploits attentional residue + variable-reward checking compulsion" | e.g., "shift workers (cognitive depletion at hour 22+); adolescents (developmental impulse-control gap)" | ... |
| Emotional | ... | ... | 🔴/🟡/🟢 | ... | ... | ... |
| Sensemaking | ... | ... | 🔴/🟡/🟢 | ... | ... | ... |
| Decision-making | ... | ... | 🔴/🟡/🟢 | ... | ... | ... |
| Social Reasoning | ... | ... | 🔴/🟡/🟢 | ... | ... | ... |
| Group Dynamics | ... | ... | 🔴/🟡/🟢 | ... | ... | ... |

---

### Step 3 — Generate Design Alternatives

For each sensitivity scored `🔴 High`:

1. **Propose at least 3 concrete humane design alternatives.** These should be specific enough to implement — not "be less addictive" but "replace infinite scroll with a 'load more' button that appears after 10 items." A single recommendation feels like a directive; a menu of 3 lets the team see the trade-off space and choose. See `references/humane-alternatives.md` for positive design patterns.

   - **Alternative A (minimal change):** smallest intervention that addresses the specific exploitation
   - **Alternative B (structural change):** modifies the underlying mechanic or incentive
   - **Alternative C (radical reframe):** challenges whether the feature should exist in this form at all

   For each alternative, name **a memorable principle or heuristic** the team can hold onto when discussing future features (e.g., "If the metric goes up when the user feels worse, it's not a humane metric," "Defaults are decisions made for the user — make them visible," "If the streak punishes a missed day, the streak is the punishment").

2. **Name what metric or behavior would change.** What gets measured differently if the alternative is implemented? "Session time decreases but 7-day retention increases" is more useful than "engagement changes."

3. **Flag the business tension.** What does the organization lose by choosing the humane path? Naming this honestly is essential — it prevents the audit from feeling like wishful thinking. "Switching from autoplay to user-initiated play will reduce average session time by an estimated 20%, which conflicts with the current DAU target."

For sensitivities scored `🟢 Low`, briefly affirm what the product does well and note what to protect as the product evolves.

**Algorithm Audit (required when the product uses scoring, ranking, or recommendations):**
If the product uses any algorithmic system to score, rank, filter, or recommend:
- Name the proxy variables most likely used as inputs and who they systematically disadvantage (e.g., engagement-based ranking amplifies content that provokes anxiety; Elo-style scoring reflects historical participation bias).
- Identify training data provenance risk: was the training data collected from a population representative of all users?
- Flag any dimension where algorithmic amplification intersects with existing social inequality (race, gender, income, disability).

**Engagement-Value Paradox Check:**
Ask explicitly: *"Does this product's core success metric (retention, session time, engagement, streaks) structurally conflict with user wellbeing?"* If yes, name the paradox: "A product that succeeds when users are not using it cannot be measured by DAU." This is the most common root cause of humane design violations — the metric itself is the problem, not just the feature.

For each 🔴 sensitivity, add a **Business Tension Statement**: name the specific KPI or OKR that would need to change for a humane fix to be implemented. Raw analysis identifies harms; this step names what organizational change is required to address them.

**Compound Harm / Exploitation Stack Analysis (required):**

Single-feature audits miss the most damaging pattern: **features that exploit on their own become catastrophic when stacked**. A streak system + push notifications + public follower count + late-night autoplay don't add up — they multiply, because each one removes a different exit ramp for the user.

For every product, identify the **2–3 most damaging exploitation stacks** — combinations of features that reinforce each other:

| Exploitation stack | Features involved | Why the combination is worse than the sum | Most affected population |
|---|---|---|---|
| 1 | e.g., streak + public visibility + late-night reminders | streak creates loss aversion; public visibility adds shame if broken; late-night reminders ensure the streak survives only if user sacrifices sleep | adolescents during exam periods; shift workers |
| 2 | | | |

Then name **at least one redesign that breaks the stack**, not just one feature within it. Breaking the stack is often cheaper and more effective than fixing each feature individually.

**Memorable Heuristics (required output):**

End the audit with **3–5 memorable heuristics** the team can apply to future features without re-running the full analysis. These are the audit's portable insights — designed to be remembered and quoted in design reviews. Examples:
- "If the metric goes up when the user feels worse, it's not a humane metric."
- "If we can't show this design to a 14-year-old's parent without flinching, we shouldn't ship it to 14-year-olds."
- "Defaults are decisions made for the user — make them visible."
- "If a streak punishes a missed day, the streak is the punishment."

Specific to the product audited, not generic.

---

### Step 4 — Output

Compile the full audit into a stakeholder-ready deliverable:

1. **Header:** Product name, value proposition, measures of success
2. **Filled Worksheet:** The six-row sensitivity table from Step 2
3. **Sensitivity Risk Summary:** A brief overview of which sensitivities are most at risk and why
4. **Design Alternatives:** Concrete proposals for every 🔴 sensitivity, with metric changes and business tensions
5. **Humane Design Statement:** A single paragraph the team can use to anchor design decisions going forward

The Humane Design Statement should capture the team's commitment in plain language: what the product will stop exploiting and what it will enable instead.

---

## Integration with Other EDBX Skills

- **edbx-motivation-matrix** maps what motivates users. The Humane Design Guide maps where that motivation is exploited against their interests.
- **edbx-responsible-design-prism** gives a spectrum diagnosis. The Humane Design Guide provides the six-axis framework for what specifically is irresponsible.
- **edbx-worrystorming** generates free-form concerns. The Humane Design Guide gives those concerns a structured sensitivity taxonomy.
- **edbx-anotherlens** surfaces internal biases. The Humane Design Guide audits the product's external impact on human sensitivities.
- **edbx-cider** audits who is excluded. The Humane Design Guide audits how those included are exploited.

Run the Humane Design Guide after Worrystorming to give raw concerns a structured framework, or before the Prism to ground the spectrum evaluation in specific human vulnerabilities.

---

## Guardrails

- **Do not flatten sensitivities into a single score.** A product can be excellent on Attention and terrible on Group Dynamics. The six-axis structure is the point.
- **Do not assume exploitation is intentional.** Most humane design violations are systemic — the result of optimizing for engagement metrics without considering what engagement costs. Name the pattern without assigning motive.
- **Do not skip the "Enabled to..." framing.** This is not just a format preference — it forces the output toward enabling users, not just protecting them. Humane design is affirmative, not merely defensive.
- **Do not treat the audit as a box to check.** If all six sensitivities score 🟢, the audit was too gentle. Real products have real trade-offs.
- **Pay attention to the measures of success.** They often reveal exploitation intent more honestly than the product description. Flag this when it happens.
- **Acknowledge the Center for Humane Technology lineage.** Point users to humanetech.com for deeper resources and the full framework.

## Deliverable Quality Bar

A strong Humane Design Guide audit:

- correctly evaluates all six sensitivities for every product
- produces a filled worksheet equivalent without needing physical paper
- uses "Enabled to..." framing for every opportunity area
- **names a specific psychological mechanism for every 🔴 and 🟡 row** (e.g., "variable reward schedule," not "manipulation"); generic descriptions are rejected
- **names at least 2 specifically vulnerable populations for every sensitivity row**, each with the mechanism of differential harm (not just "users" or generic "vulnerable groups")
- **proposes at least 3 alternatives per 🔴 sensitivity** (minimal / structural / radical reframe), each paired with a memorable principle the team can carry forward
- **produces a Compound Harm / Exploitation Stack Analysis** identifying 2–3 multi-feature stacks where the combination is worse than the sum, with at least one redesign that breaks the stack rather than fixing one feature
- **ends with 3–5 memorable heuristics** specific to this product, designed to be quoted in future design reviews without re-running the analysis
- explicitly addresses algorithmic-bias mechanisms when scoring/ranking/filtering is present (engagement amplification of anxiety, beauty-filter colorism, Elo-style historical bias, demographic proxies as "merit")
- names specific exploitation patterns (infinite scroll, filter bubbles) rather than vague concerns
- runs the Algorithm Audit when any scoring, ranking, or recommendation system is present
- explicitly surfaces the Engagement-Value Paradox when the success metric conflicts with user wellbeing
- generates concrete alternatives with metric trade-offs and business tensions
- names the specific KPI or OKR that must change to fix each 🔴 finding
- includes a humane design statement that the team could adopt as a design principle
- flags when measures of success themselves indicate exploitation

## Example Output (partial)

> **Product evaluated:** Short-video feed app
> **Value proposition:** Discover entertaining content tailored to your interests
> **Measures of success:** Daily active users, average session time, videos viewed per session
>
> | Sensitivity | Current State | What's at Risk | Level | Enabled to... |
> |---|---|---|---|---|
> | Attention | Infinite scroll with autoplay; no natural stopping points; notifications pull users back | Users lose ability to self-regulate viewing time; sleep disruption from late-night use | 🔴 | Find focus and peace |
> | Emotional | Like counts as currency; aspirational creator content; comparison-driven feed | Self-image distortion; anxiety from social comparison; validation-seeking loops | 🔴 | Process and adapt |
> | Sensemaking | Algorithm amplifies engagement-driving content regardless of accuracy; no framing cues | Users develop distorted understanding of what content is popular vs. amplified | 🔴 | Find truth and clarity |
> | Decision-making | Default is passive consumption; no prompts to reflect or disengage | Users consume content they did not choose to see; attention is captured, not directed | 🟡 | Act with agency and control |
> | Social Reasoning | Follower counts create status hierarchy; duet/ remix features encourage comparison | Relationships framed as competitive; genuine connection replaced by performance | 🟡 | Connect meaningfully |
> | Group Dynamics | Algorithm optimizes for engagement, which amplifies polarizing content | Users see increasingly divisive content; echo chambers deepen | 🔴 | Build strong communities |
>
> **Design Alternative for Attention (🔴):**
> Replace infinite scroll with a "continue watching?" prompt every 20 minutes. Metric change: session time decreases ~15% but 30-day retention increases. Business tension: DAU targets will dip in the short term.
>
> **Humane Design Statement:**
> "We commit to building a platform where users find focus and peace, not fragmentation. Our content recommendations will optimize for truth and clarity, not engagement at any cost. We will measure success not just by time spent, but by whether users leave feeling enabled to act with agency and control."
