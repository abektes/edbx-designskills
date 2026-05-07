# DAH Cards — Design Against Humanity

**The short version:** A card-based team session that maps the harms your design could cause — and ends with a signed ethics manifesto the team commits to.

---

## Who made it

DAH Cards — **Design Against Humanity** — is a design ethics facilitation method whose name is a deliberate echo of the card game *Cards Against Humanity*. The method takes the provocative, uncomfortable energy of that game and applies it to ethical design work: the goal is to surface things a team might not otherwise say out loud.

The method draws on participatory design traditions and values-centered design research, adapted into a card-facilitated workshop format for cross-functional product teams.

---

## The problem it solves

Most ethical design conversations happen in the abstract. "We should consider privacy." "Let's think about vulnerable users." "We need to be responsible." These conversations feel productive in the moment and produce very little.

DAH Cards forces the conversation to get specific. The cards are designed to be uncomfortable. They name actual harms — manipulation, exploitation, exclusion, surveillance — in direct language. When a team sits with a card that says "Your product makes users feel stupid," the conversation changes from abstract values alignment to concrete design reckoning.

The method also produces an artifact: a written, signed manifesto that captures what the team agreed to and what they committed against. That artifact can be revisited when business pressure pushes toward the harms the team named.

---

## When to use it

- **At the start of a project** — to set ethical guardrails before the design is built
- **Before a launch** — to surface concerns that haven't been named and get explicit commitments
- **When team values are fuzzy** — when you suspect people have different standards but no one has compared notes
- **When the team includes non-designers** — engineers, product managers, executives — who need a structured entry point into ethical design conversation
- **When you want a signed artifact** — something the team can point to later when pressure to compromise builds
- **When you want to name harms directly** — not euphemize them into "risks" or "considerations"

---

## What it produces

A DAH Cards session produces three core artifacts (with two optional ones depending on what was asked):

**1. DAH Card Pairs (the signature artifact).** Black side / white side cards for every mechanic evaluated. Black side = the design as it ships ("Streak system that resets if you miss a day"); white side = the harm in plain language, in the voice of someone who's been harmed by it ("App that punishes you with shame copy on a bad mental-health day"). Each card pair is **categorized by harm type** using six DAH harm categories: **Deception / Coercion / Addiction / Surveillance / Exclusion / Systemic**. A single mechanic can fall into multiple categories — tag every category that applies. Coverage must span at least 4 of the 6 categories (systemic harms are the most commonly missed and must be considered explicitly).

**2. Consequence Map** — depth behind the white side. Harms across individual / social / environmental / systemic dimensions, with likelihood, severity, who bears the harm, and whether the design knows about it.

**3. Sorting Verdict + Reflection** — each item sorted Ethical / Unsure / Unethical with a one-line rationale, plus the "What changed?" reflection (which surprises emerged, where the team disagreed, what assumptions shifted).

For each Unethical finding the method produces **microcopy rewrites** (before/after) and a **ship-ready recommendation** specific enough to write a sprint ticket from.

**Mode selection.** Two further artifacts are *opt-in*, not auto-included:
- **Manifesto** — produced when the user explicitly asks for one ("write a manifesto," "what should we commit to")
- **Future Vision** — produced when the user asks for one ("what products do we want to make instead")

When only an audit was requested, the AI runs Modes 1 + 2 and the Ship-Ready Recommendation. Including Manifesto and Future Vision when not asked dilutes actionability and is treated as padding.

---

## The key insight

The cards work because they bypass the politeness that typically suppresses hard conversations in design reviews. When someone plays a card, they're not accusing their colleague — they're engaging with the prompt the card presents. That structure gives permission to name things that would otherwise stay unspoken.

The manifesto works because it's a commitment device. Writing something down and signing it is meaningfully different from agreeing to it verbally in a meeting. When business pressure arrives — and it will — the manifesto is something you can point to.

---

## How to use it with AI

Describe your product or feature. The AI will proceed directly to the consequence mapping and manifesto — you don't need to have already run a card session. If you haven't done the harm mapping yet, the AI will make its best-estimate analysis with stated assumptions, then produce the manifesto from that foundation. You can review and revise the assumptions rather than waiting for a workshop to happen first.

---

## A quick example

**Product:** A social platform with a recommendation algorithm that surfaces increasingly extreme content to maximize engagement.

**DAH Card Pairs (excerpt):**

| Card # | Categories | Black side (the design) | White side (the harm) |
|---|---|---|---|
| 1 | Addiction + Systemic | Engagement-maximizing recommendation feed | App that learns your worst impulses faster than your best ones, then keeps showing you more of them |
| 2 | Surveillance + Deception | "Personalization" without disclosure of training signals | Profile inferred from your scroll patterns that you never saw, never consented to, and can't correct |
| 3 | Exclusion | Engagement-amplified content excludes anything quiet, slow, or non-emotional | Voices of people who don't perform for the algorithm get systematically buried |
| 4 | Systemic | Outrage-amplification at population scale | Public discourse degraded for non-users who never opted in to this platform |

**Consequence Map (excerpt):**
- **Radicalization pathway** (Critical) — algorithm optimizes for engagement; outrage drives more engagement than nuance; users incrementally exposed to more extreme content over time
- **Mental health harm** (Critical) — same mechanism amplifies body image, crisis, and harm content for vulnerable users
- **Advertiser-harm misalignment** (Moderate) — brands appear next to content they'd never choose; platform profits; brands bear reputational risk

**Microcopy rewrite (for engagement metric display):**
- Before: "You've been active for 3 hours 🔥"
- After: "You've been scrolling for 3 hours. Ready to take a break?"

**Ethics Manifesto excerpt:**
- *We commit to measuring platform health by user-reported wellbeing, not by time-on-site.*
- *We will not optimize for engagement metrics that our own research shows increase anxiety or radicalization.*
- *We are responsible to: users who trust us with their attention, families of users, communities affected by content spread.*

---

## See also

- [Pledge Works](pledge-works.md) — DAH Cards produces a manifesto; Pledge Works takes specific commitments and stress-tests them against business pressure
- [Ethical Contract](ethical-contract.md) — DAH Cards is a facilitation session; Ethical Contract is a formal cross-disciplinary agreement
- [Worrystorming](worrystorming.md) — generates worries the DAH Cards session can then examine through the card framework
