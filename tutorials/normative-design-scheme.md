# Normative Design Scheme

**The short version:** Applies three philosophical lenses — virtue ethics, consequentialism, and deontology — to a design decision, so you can evaluate it from intention, outcome, and duty simultaneously rather than choosing one framework and missing what the others see.

---

## Who made it

The Normative Design Scheme draws on classical ethical philosophy — specifically the three major normative theories in Western moral philosophy — and applies them to design decisions as an analytical framework. This adaptation for design practice synthesizes work in philosophy of technology, design ethics, and HCI research on how ethical theories translate into design evaluation.

The three theories used are:
- **Virtue Ethics** (Aristotle, MacIntyre) — ethics of character and intention
- **Consequentialism** (Bentham, Mill) — ethics of outcomes and welfare
- **Deontology** (Kant) — ethics of duty and universal principles

---

## The problem it solves

When designers and product managers reason about ethics, they usually default to one framework without knowing it. "Will this harm users?" is consequentialist thinking. "Would I be comfortable if this were on the front page of the New York Times?" is a rough version of deontological thinking. "Are we the kind of team that does things like this?" is virtue ethics.

Each framework reveals different things. Consequentialism finds outcomes that individual designers weren't thinking about. Deontology finds duties that can't be traded off even for good outcomes. Virtue ethics finds whether the intentions behind a decision are honest or rationalized.

Using only one lens means missing what the other two see. A decision that looks fine from a consequentialist view (net benefit to the most users) might be deeply problematic from a deontological view (violates a duty to a minority). The Normative Design Scheme makes all three lenses explicit and applies them in sequence.

---

## When to use it

- **When a design decision has a genuine ethical tension** — not every decision needs three philosophical frameworks, but some do
- **When your team is stuck in a values debate** — applying the three lenses often reveals that different team members are implicitly reasoning from different frameworks, which is why they're not converging
- **When you want to evaluate the intentions behind a decision, not just its outcomes** — virtue ethics is the lens for that
- **When you're dealing with a trade-off between majority benefit and minority harm** — this is where consequentialism and deontology diverge most sharply
- **For complex, high-stakes decisions** where a single ethical framework is clearly insufficient

---

## What it produces

Crucially, the method is *not* "apply virtue ethics, then consequentialism, then deontology in sequence." That collapses it into generic ethical analysis. Five distinctive moves keep it a methodology:

**Step 0 — Stakeholder & Power Map (shared input for all three lenses):** Before any lens is applied, enumerate every population the design touches. The three lenses must operate on the same stakeholder reality — otherwise each lens evaluates a different reality and the synthesis becomes incoherent. The map names primary users, vulnerable subgroups (specifically, e.g., adolescents / abuse survivors / undocumented users / older adults), non-consenting bystanders, workers in the supply chain, **the designers/creators themselves** (the design shapes what kind of professionals they become), and future-affected populations. Plus a power-asymmetry summary and a **Non-Obvious Harms Inventory** of at least 5 named harms beyond the heuristic categories (proxy-variable harms, aggregation, competence foreclosure, intrinsic-motivation crowd-out, attentional-architecture formation, etc.).

**Lens 1 — Virtue Ethics, with explicit Creator Impact:** What virtues does the design promote — *in users, AND in the people who build and operate it*? The Creator Impact sub-question is the move most often skipped: what kind of designer/engineer/PM does this design make us into? What habits of moral attention does it require us to cultivate or suppress? What would we be embarrassed to explain to a journalist or a child? If creators come out of the project ethically diminished, that is a Virtue lens failing regardless of what users experienced.

**Lens 2 — Consequentialism (Effect):** Outcomes for all stakeholders named in Step 0 — not "users" generically. Who benefits, who is harmed, by how much, with what probability, at scale.

**Lens 3 — Deontology (Design/Duty):** Are there duties, rights, or principles this design violates — regardless of outcomes? Are autonomy, privacy, informed consent, dignity respected?

**Universal Law Test (named output table):** The Kantian thought experiment formalized as a structured artifact. For every named design decision: if every product did this, what world results — and is it livable?

**Triad Conflict Matrix (the methodology's signature artifact):** For every design decision, a row showing where each lens lands (Virtue / Consequence / Deontology) plus alignment status — 🟢 all-aligned (highest-confidence recommendation), 🟡 two-against-one (genuine dilemma — name it honestly), 🔴 all-conflict (unresolved — requires team-level commitment, not analysis).

The output ends with a **Normative Design Statement** in prescribed form — not just "this is ethically grounded" but a closing two-part commitment: *"We commit to [specific course of action] to honor what the lenses agreed on, and to [specific course of action] to acknowledge what they did not."* A statement without that commitment closure is incomplete.

---

## The key insight

When all three lenses point in the same direction, you have a clear ethical finding. When they diverge — when something looks fine consequentially but problematic deontologically — you have a genuine ethical tension. The framework doesn't resolve that tension for you. But it makes it explicit, which is the first step toward making an honest decision about it.

Most ethical debates in design teams are actually two people talking from different frameworks without knowing it. Making the frameworks explicit often unsticks those conversations.

---

## How to use it with AI

Describe the design decision you want to evaluate and any ethical concerns you already have. The AI will produce the Stakeholder & Power Map and Non-Obvious Harms Inventory first, then apply all three lenses (with explicit Creator Impact in Lens 1), produce the Universal Law Test for every named decision, build the Triad Conflict Matrix as the signature artifact, and close with a Normative Design Statement that includes the prescribed two-part commitment. If the lenses disagree, the AI will name the dilemma honestly without artificial resolution.

---

## A quick example

**Design decision:** An e-commerce app decides to send abandoned cart notifications every 4 hours until the user completes the purchase or explicitly opts out.

**Lens 1 — Virtue Ethics (Intention):** The stated reason is "helping users complete purchases they started." The actual driver is conversion rate optimization. The team is not being dishonest, but they're not being fully honest about whose benefit they're designing for — the user who "wants to remember their cart" or the company that wants the sale. Virtue ethics flags this rationalization.

**Lens 2 — Consequentialism (Effect):** Outcomes for different users: some users benefit from reminders (forgotten carts, genuine forgetfulness). Others experience harassment (compulsive shopping behavior amplified, financial harm to users with impulse control issues, 4-hour notification loops for low-income users who abandoned the cart because they couldn't afford the item). At scale, the harm to vulnerable users is significant and predictable.

**Lens 3 — Deontology (Duty):** Users have a right to choose when and how they engage with commercial communications. A notification every 4 hours with no easy opt-out violates that right — regardless of whether the net outcome is positive. The design doesn't respect user autonomy as a principle; it treats notification tolerance as a resource to be extracted.

**Integrated verdict:** All three lenses flag this design. The virtue ethics lens finds rationalization; the consequentialist lens finds predictable harm to vulnerable users; the deontological lens finds a violation of the right to autonomy. Recommendation: reduce to one reminder, make opt-out visible and easy on the first notification, and add option to set reminder timing.

---

## See also

- [Digital Ethics Compass](digital-ethics-compass.md) — four-direction audit that is broader but less philosophically rigorous
- [Ethicography](ethicography.md) — applies ethical analysis to team decisions over time; Normative Design Scheme applies it to a single decision in depth
- [Responsible Design Prism](responsible-design-prism.md) — gives a spectrum diagnosis of where a product sits ethically; Normative Design Scheme explains the decision logic behind that position
