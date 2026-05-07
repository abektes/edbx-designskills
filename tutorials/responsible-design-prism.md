# Responsible Design Prism

**The short version:** A five-axis diagnostic that tells you where your product sits on the spectrum from dark to responsible — not just overall, but separately across user relationship, information, error handling, business alignment, and usability.

---

## Who made it

The Responsible Design Prism is a framework for diagnosing a product's ethical posture across five distinct dimensions. It draws on ethical design research and principles developed in the HCI and responsible technology communities, synthesizing multiple evaluative traditions into a single spectrum-based diagnostic format.

The "prism" metaphor is intentional: just as a prism splits white light into its component colors, this method splits a product's ethical posture into its component dimensions — making visible the distinctions that a single overall rating would obscure.

---

## The problem it solves

Ethical design discussions often operate at the wrong level of abstraction. "Is this product ethical?" is rarely a useful question. A product can have an excellent user relationship model and completely opaque information practices. A product can be highly usable and deeply misaligned with the interests of the users it claims to serve.

The Responsible Design Prism fixes this by separating five axes that are often conflated. A product that scores well on usability may score badly on business alignment. A product that scores well on transparency may score badly on user relationship. The prism makes these distinctions visible and prevents teams from using strength in one area to avoid examining weakness in another.

---

## When to use it

- **For a product health check** — a structured diagnostic of where the product stands ethically right now
- **When leadership asks "are we ethical?"** — the prism gives a structured, defensible answer that goes beyond "yes" or "no"
- **When you want a baseline before making changes** — the prism gives you a current-state reading to compare future iterations against
- **When ethical concerns have been raised but the team doesn't know where to focus** — the prism points to the specific dimensions that need attention
- **For new product evaluation** — assessing a product concept before building it, to see which dimensions need the most attention from the start

---

## What it produces

The prism evaluates five axes, each rated on a spectrum from dark (manipulative/harmful) to responsible (transparent/honest):

**Axis 1 — User Relationship:** How does the product treat users? Is the relationship honest and mutual, or extractive and transactional? Are users stakeholders whose wellbeing the product serves, or are they resources the product harvests?

**Axis 2 — Information:** What does the product tell users — and not tell them — about how it works, what data it collects, and how decisions are made? Is information disclosed proactively, or hidden until required?

**Axis 3 — Error Handling:** When the product fails, makes a mistake, or causes harm, how does it respond? Does it take responsibility, make it easy to fix the error, and tell users what happened? Or does it obscure errors, make recovery difficult, and avoid accountability?

**Axis 4 — Business Alignment:** Are the product's business incentives aligned with users' interests? Does the product succeed when users succeed, or does it succeed when users fail (spending money they can't afford, staying longer than they want to, becoming dependent)?

**Axis 5 — Usability:** Is the product accessible and comprehensible to the full range of people it affects — including those with disabilities, limited digital literacy, or non-primary language contexts? Or does design complexity obscure the product's actual behavior from the users most likely to be harmed by it?

Before scoring, the prism requires two structural artifacts:

**Stakeholder & Vulnerable Population Map** — at least 3 distinct populations named (primary users, named vulnerable subgroups like minors / neurodivergent / low-income / undocumented / abuse survivors / people in crisis, secondary users / non-users affected, workers in supply chain). For each: relationship to product, specific harms likely, power asymmetry vs. operator. Without this map the scoring is abstract.

**Psychological Mechanism Audit** — for every axis scored Red or Yellow, name the *specific* psychological mechanism the design exploits. Vague claims of "manipulation" are not useful. Use precise terms: cognitive biases (default bias, loss aversion, social proof), behavioral mechanisms (variable reward schedule, streak-loss aversion, near-miss design, friction asymmetry), emotional vulnerabilities (FOMO, social anxiety, identity entanglement), developmental vulnerabilities (where minors are in scope). "It uses variable reward scheduling on the like counter to drive compulsive checking" is a mechanism; "it's manipulative" is not.

For each axis, the prism produces:
- A spectrum rating (Dark → Neutral → Responsible) referencing the named populations most affected
- Specific evidence from the product supporting that rating
- The named psychological mechanism (for Red/Yellow) being exploited
- The primary driver of any dark rating (business pressure, missing research, organizational blind spot)
- A highest-leverage intervention naming which mechanism it interrupts and which population benefits

---

## The key insight

The most revealing output of the prism is often the **Business Alignment** axis, because it's the one teams most frequently rate optimistically. "We make money when users succeed" sounds like alignment — but if the product's revenue model actually depends on users spending money compulsively, staying past healthy limits, or misunderstanding what they're paying for, the axis is dark regardless of what the team believes about their intentions.

Business Alignment is the axis where self-deception lives.

---

## How to use it with AI

Describe your product — what it does, how it makes money, what the key features are, and anything you already know about its ethical strengths and weaknesses. The AI will evaluate all five axes, rate each on the spectrum, provide evidence for each rating, and produce highest-leverage interventions for each dark axis.

---

## A quick example

**Product:** A buy-now-pay-later service integrated into e-commerce checkout.

| Axis | Rating | Primary driver of dark rating |
|---|---|---|
| User Relationship | 🔴 Dark | Users are revenue sources; the product succeeds when users carry debt |
| Information | 🟡 Neutral | APR is disclosed, but total cost of finance is not clearly shown at point of purchase |
| Error Handling | 🟡 Neutral | Missed payment handling is partially transparent; late fee structure is clear |
| Business Alignment | 🔴 Dark | Revenue from interest and late fees means the product literally profits from users failing to pay on time |
| Usability | 🟡 Neutral | Checkout integration is seamless (potentially too seamless — reduces friction that protects impulse purchases) |

**Highest-leverage interventions:**
- Business Alignment: Introduce a "total cost if you miss one payment" display at the moment of checkout decision. This doesn't change the business model, but it makes the business model's consequences visible to users before they commit.
- User Relationship: Add a "can you afford this?" soft check — a voluntary tool that helps users assess whether a purchase fits their financial situation before completing checkout. Voluntary, not paternalistic.

---

## See also

- [Digital Ethics Compass](digital-ethics-compass.md) — four-direction audit that covers overlapping territory with different framing
- [Ethicography](ethicography.md) — explains the decision history that produced the prism rating; Responsible Design Prism is the diagnosis, Ethicography is the autopsy
- [Normative Design Scheme](normative-design-scheme.md) — applies philosophical lenses to specific decisions; the prism applies a spectrum rating to the overall product
