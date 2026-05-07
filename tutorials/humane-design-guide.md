# Humane Design Guide

**The short version:** A six-sensitivity audit of your product against the specific ways technology is known to harm human wellbeing — drawn from the research and advocacy of the Center for Humane Technology.

---

## Who made it

The Humane Design Guide is based on the framework developed by the **Center for Humane Technology** — a nonprofit founded by Tristan Harris (former design ethicist at Google), Aza Raskin, and colleagues who work on reforming the technology industry's incentive structures around human wellbeing.

The Center's research identified six specific "human sensitivities" — aspects of human psychology and social life that technology consistently exploits in ways that harm users. The Humane Design Guide translates that research framework into a design audit tool.

---

## The problem it solves

Technology companies often claim to be making products "for users." The Center for Humane Technology's research documented the gap between that claim and what products are actually optimized for — which is typically engagement, retention, and revenue, using design mechanisms that exploit human psychological vulnerabilities.

The six sensitivities are not abstract ethical principles. They are specific, documented mechanisms through which technology causes harm: attention exploitation, social validation manipulation, habit formation and addiction, outrage amplification, anxiety and FOMO, and persuasive technology that erodes user agency.

The Humane Design Guide makes these mechanisms auditable. For each sensitivity, it asks: is your product exploiting this mechanism? How? For whom? What would need to change to stop?

---

## When to use it

- **When you're building a product that competes for user attention** — social media, news, entertainment, games, productivity tools
- **When your success metrics include time-on-app or daily active users** — these are the metrics most likely to create misalignment between business success and user wellbeing
- **When you suspect your product might be addictive but aren't sure** — the Humane Design Guide gives you a structured way to examine that suspicion
- **When user wellbeing research is absent from your team's vocabulary** — this audit introduces the framework and makes it concrete
- **When you want to audit psychological harm specifically** — other methods cover broader ethical terrain; this one focuses on human wellbeing

---

## What it produces

The audit covers six sensitivities:

1. **Attention** — Does the product compete for user attention in ways that undermine their ability to direct it toward what they actually value?

2. **Social validation** — Does the product use likes, follower counts, or social comparison to manipulate how users feel about themselves?

3. **Persuasion and manipulation** — Does the product use dark patterns, personalized targeting, or psychological techniques to influence behavior without users' awareness?

4. **Addiction and habit formation** — Does the product create compulsive behaviors? Are users using it more than they want to?

5. **Outrage and anxiety amplification** — Does the product's recommendation or content system amplify emotionally activating content because it drives more engagement?

6. **Reduction of agency and autonomy** — Does the product make decisions on behalf of users that reduce their sense of control?

For each sensitivity, the audit produces:
- A severity rating (🔴 Exploiting / 🟡 Risk present / 🟢 Managed or absent)
- A specific description of how the sensitivity is being activated
- The **named psychological mechanism** for every 🔴 and 🟡 row — using precise terms (variable reward schedule, streak-loss aversion, near-miss design, friction asymmetry, FOMO, identity entanglement, beauty-filter colorism, engagement-amplification of anxiety). Generic "manipulation" is rejected; the mechanism must be named specifically.
- **At least 2 specifically vulnerable populations** per sensitivity row, each with the mechanism of differential vulnerability — not "users" or "vulnerable groups" generically. Examples: shift workers (cognitive depletion at off-hours), adolescents (developmental peer-comparison sensitivity), people with eating disorders (Emotional sensitivity on fitness/wellness apps), women and racial minorities re: beauty filters (colorism / narrow aesthetic norms in training data), gig workers (Decision-making under forced continuity).
- **At least 3 alternatives per 🔴 sensitivity** — minimal change (smallest intervention), structural change (modifies underlying mechanic), radical reframe (challenges whether the feature should exist in this form). Each alternative is paired with a memorable principle the team can carry forward.
- A **Business Tension Statement** — the specific metric or OKR that would need to change

The method also includes:

- **Engagement-Value Paradox Check** — does the product's core success metric structurally conflict with user welfare? If so, name the paradox explicitly rather than treating it as resolvable through incremental design improvements.
- **Compound Harm / Exploitation Stack Analysis** — single-feature audits miss the most damaging pattern: features that exploit on their own become catastrophic when stacked. A streak system + push notifications + public follower count + late-night autoplay don't add up — they multiply, because each one removes a different exit ramp. The analysis identifies 2–3 multi-feature stacks where the combination is worse than the sum, and proposes at least one redesign that breaks the stack rather than fixing one feature within it.
- **Memorable Heuristics (3–5)** — specific to this product, designed to be quoted in future design reviews without re-running the analysis. Examples: *"If the metric goes up when the user feels worse, it's not a humane metric." "If a streak punishes a missed day, the streak is the punishment."*

---

## The key insight

Most product teams track engagement. Almost no product teams track user wellbeing. Those two metrics are often in tension, and designing as if they're aligned is how products end up exploiting the very people they're meant to serve.

The Humane Design Guide forces that conflict into view. It names the specific sensitivity being exploited, names who is most harmed, and names the metric that would need to change to stop the exploitation. That's the foundation for real product decisions, not just ethics theater.

---

## How to use it with AI

Describe your product — what it does, how it makes money, what the key engagement features are. The AI will work through all six sensitivities, rate each one, identify the most affected populations, name the business tensions, and generate redesign recommendations for every 🔴 finding.

---

## A quick example

**Product:** A social photo-sharing app with algorithmic feed, public follower counts, and engagement notifications.

**Sensitivity 2 — Social Validation 🔴:**
The product shows public follower counts, public like counts, and prominent engagement metrics on every post. The algorithmic feed prioritizes posts that get more engagement, which means social validation metrics directly influence content visibility.

**Most affected population:** Adolescent users, particularly girls aged 13–17, for whom social comparison and validation-seeking behavior is developmentally amplified. Also users with depression and anxiety, for whom social rejection signals have outsized psychological impact.

**Business Tension Statement:** Daily active user (DAU) metrics depend on social validation loops to drive return visits. Removing public like counts (as Instagram has tested) reduces engagement in the short term. Fixing this requires leadership-level commitment to a different success metric — possibly a user-reported wellbeing score — which has not yet appeared on the product roadmap.

**Redesign directions:**
- Remove public like counts; show only to content creator (proven intervention from Instagram's 2019 test)
- Make follower count private by default; show only to account owner
- Redesign feed ranking to include content from smaller accounts, not just high-engagement posts

---

## See also

- [Digital Ethics Compass](digital-ethics-compass.md) — four-direction audit that includes manipulation; Humane Design Guide goes deeper on psychological harm specifically
- [Motivation Matrix](motivation-matrix.md) — maps motivational mechanisms; Humane Design Guide maps the human sensitivities those mechanisms exploit
- [Inverted Behavior Model](inverted-behavior-model.md) — forecasts behavioral consequences; Humane Design Guide identifies which sensitivities are being activated to produce those behaviors
