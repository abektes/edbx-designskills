# Bad Design Canvas

**The short version:** A 12-category framework for stress-testing any product idea against everything that could go wrong — culturally, socially, environmentally, ethically, and everything else.

---

## Who made it

The Bad Design Canvas was created by **Matthew Manos**, a designer and educator, and is licensed under a Creative Commons CC BY-ND license. It appears as Method #09 in *Universal Methods of Ethical Design*.

The canvas was designed to be used by teams as a structured adversarial exercise — a way of deliberately looking for problems with your own work before they find you.

---

## The problem it solves

Most design teams think about what could go wrong when something breaks. The Bad Design Canvas asks a harder question: what goes wrong when everything works exactly as intended?

Products are released into complex social, cultural, and environmental systems. A food delivery app that delivers food perfectly might also exploit gig workers perfectly, create environmental waste perfectly, and erode food culture perfectly. None of those are bugs. They're features the team never considered.

The Bad Design Canvas exists because most teams don't have a framework for finding these consequences. They focus on the problem they're solving and forget to ask what new problems their solution creates.

---

## When to use it

- **Before launch** — to shape the product concept while you still can
- **Before committing to a direction** — when you're evaluating multiple ideas and want to stress-test them
- **During a design review** — when the team needs a structured "what could go wrong" conversation
- **After an incident** — to understand what the canvas would have caught if you'd run it earlier
- **Whenever a team member says "let's think about what could go wrong"** — this is the answer to that request

---

## What it produces

The canvas covers 12 consequence categories. Every product gets rated on all 12 — there is no "N/A" without explanation. The categories are:

1. **Cultural Appropriation** — is the idea borrowed from a culture you don't represent?
2. **Band-Aid** — is this a temporary fix that ignores the root cause?
3. **Unfair Control** — does this create unfair control over users?
4. **Exploitation** — does this expose or objectify the people it's meant to serve?
5. **Inefficiency** — does this create new complexity, confusion, or delay?
6. **Environmental & Social Impact** — does this use finite resources or create harsh conditions for workers?
7. **Stakeholder Abandonment** — who is this failing to consider?
8. **Decreased Safety** — does this create unsafe conditions?
9. **Inappropriate** — is this offensive in any context or culture?
10. **Boring** — is this just uninspired? (this one is lighter — a quality check, not a moral concern)
11. **Displacement** — does this replace something valuable that existed before?
12. **Inequity** — does this make existing inequalities worse?

Each category gets rated: **Significant 🔴 / Possible 🟡 / Low 🟢**

The output includes: a completed 12-cell canvas, a top-3 consequences summary, redesign recommendations for every Significant finding, a Bad Design Statement (one paragraph naming the harm, who it affects, and what to do), and a "Should we build this?" verdict.

---

## The three verdicts

At the end of a Bad Design Canvas session, the team arrives at one of three positions:

- **Ship with changes** — the significant findings are addressable; specific design changes would fix them
- **Rethink fundamentally** — the significant findings are systemic; the core concept needs to change, not just the details
- **Do not build** — the harm is inherent to what the product is, and it cannot be designed around

Most teams never arrive at "do not build" explicitly. The canvas makes it possible to say it out loud.

---

## How to use it with AI

Describe the product or service you're evaluating. If you're in early ideation, a brief description is enough. If it's an existing product, describe how it works and who uses it.

The AI will work through all 12 categories with product-specific responses — not generic observations about what products "could" do, but specific analysis of what this product, with this mechanism, in this context, actually risks.

---

## A quick example

**Product:** A food delivery app using gig workers, surge pricing, and gamified delivery streaks.

Selected findings:

- **Exploitation 🔴** — gig workers have no labor protections; surge pricing exploits users in food deserts with no alternatives; gamified streaks turn worker desperation into engagement metrics
- **Environmental & Social Impact 🔴** — no healthcare, no minimum wage guarantee, algorithmic management with no human recourse; single-use packaging at scale
- **Displacement 🔴** — replaces employed local delivery staff with gig workers earning less; replaces home cooking for time-pressed users, increasing dependency

**Bad Design Statement:** *"The most significant unintended consequence of this app is the systematic exploitation of gig workers, who are treated as disposable infrastructure rather than human stakeholders. This requires fundamental redesign of the worker relationship model — or the product should not be built in its current form."*

**Verdict: Rethink fundamentally.**

---

## See also

- [Worrystorming](worrystorming.md) — generates free-form worries that the Bad Design Canvas then systematizes
- [Anti-Heroes](anti-heroes.md) — surfaces who gets harmed; Bad Design Canvas maps the systemic categories those harms fall into
- [Inverted Behavior Model](inverted-behavior-model.md) — forecasts behavioral consequences; Bad Design Canvas maps broader social, environmental, and cultural consequences
- [Fair Patterns](fair-patterns.md) — remediates manipulative UI patterns; Bad Design Canvas remediates systemic consequences beyond the interface
