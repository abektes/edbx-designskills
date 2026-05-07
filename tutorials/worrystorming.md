# Worrystorming

**The short version:** An ethical pre-mortem that turns design anxieties into design commitments — generate the worries, cluster them into themes, reframe each theme as a value, then generate concrete mitigations.

---

## Who made it

Worrystorming is **Method #100** in *Universal Methods of Ethical Design* — the final and capstone method in the book. It synthesizes the core ethical design mindset into a single practical session format.

The method is explicitly consequentialist in its orientation: it asks what happens downstream, at scale, and over time — not what the team intends, but what the design might actually do once it's out in the world. The worry-to-value reframing draws on traditions of reflective design practice and ethical pre-mortem facilitation from organizational behavior research.

---

## The problem it solves

Most product teams know when something feels risky. They just don't have a structured way to name those risks, share them across the team, or convert them into something the design can actually respond to.

The result is that ethical anxiety gets managed privately. Someone worries about the data implications and says nothing. Someone else worries about how the feature will affect lower-income users and doesn't raise it because it feels like scope creep. The concerns stay in people's heads and never become design requirements.

Worrystorming fixes this by making worry a shared, legitimate design activity — and then by doing something most risk exercises don't: converting the worry into a value commitment and a design constraint. A raw list of concerns is just anxiety. A reframed cluster is a design direction.

The method is also designed for the moment when teams feel the most pressure not to slow down. Pre-launch is exactly when Worrystorming is most valuable, and exactly when teams are most reluctant to do it.

---

## When to use it

- **Before shipping a new feature** — the classic ethical pre-mortem use case
- **At the start of a project** — to shape design direction before decisions are made
- **When the team has a nagging feeling something is wrong** — but hasn't named what
- **When stakeholders are asking "what could go wrong?"** — this is the structured answer
- **When a design is about to affect a vulnerable population** — and the team hasn't explicitly examined that
- **When a previous product caused harm** — and you want a disciplined retrospective that generates commitments, not just blame

---

## What it produces

Worrystorming runs across eight concern categories to force coverage beyond what teams naturally think about:

| Category | What it catches |
|---|---|
| 🗃️ Data & Privacy | Consent gaps, data misuse, unclear ownership |
| 🌍 Environmental | Carbon cost, infrastructure, waste |
| 👥 Community & Social | Excluded groups, disrupted social dynamics |
| 💸 Economic | Inequality widening, livelihoods threatened, who pays |
| 🔒 Safety & Harm | Failure modes, vulnerable user scenarios |
| 🧠 Psychological | Cognitive exploitation, anxiety, addiction patterns |
| ⚖️ Power & Fairness | Who controls, who is silenced, opacity beneficiaries |
| 🔮 Future Consequences | What happens at scale, in 5 years, if competitors copy this |

Most teams over-index on Data & Privacy and Safety, and systematically skip Economic, Power & Fairness, and Future Consequences — which is where the biggest ethical failures originate.

The method produces five layered outputs:

1. **Full Worry List** — 10–20 specific, sticky-note-style concerns across all eight categories
2. **Clustered Worry Themes** — 3–6 affirmatively named clusters, each with a severity tag (🔴 Critical / 🟡 Monitor / 🟢 Low Risk)
3. **For each cluster:** an Ethical Objective ("We commit to X to avoid Y"), a Design Constraint (a specific, testable requirement), and a Test Question ("How would we know if we failed at this?")
4. **Refined Mitigations** for every 🔴 Critical cluster — concrete design alternatives or protective mechanisms
5. **Worrystorm Summary** — a single paragraph naming the key ethical challenges and the values the design must uphold; specific enough to guide the next design decision

---

## The key insight

The reframing step — turning a worry into a value — is what separates Worrystorming from a standard risk register.

"We're worried users won't understand what data we're collecting" stays a worry until you reframe it: **"We commit to informed consent in plain language, because users who trust us with their data deserve to understand what they're agreeing to."** That's not a risk item to close — it's a design principle to build toward.

The method's premise is that ethical anxiety is a design resource, not a blocker. The designer who is worried about consequences is doing responsible work. Worrystorming gives that worry a structure and a productive end state.

The second key insight: the worries that are hardest to say out loud are usually the most important. If naming a concern feels uncomfortable, that's a signal — not a reason to skip it.

---

## How to use it with AI

Describe the product, feature, or design you're evaluating and what stage it's at (ideation, in-development, pre-launch, or live). Name any concerns you already have. The AI will generate a full worry list across all eight categories, cluster them into affirmatively named themes with severity ratings, reframe each cluster into an ethical objective and design constraint, produce mitigations for all critical clusters, and write a Worrystorm Summary.

If you already know where you want to focus (e.g., "I'm particularly worried about the psychological impact"), say so — the AI will cover all eight categories but give extra attention to your flagged area.

---

## A quick example

**Product:** A "spend tracker" feature inside a banking app that sends notifications whenever a user's spending approaches a self-set budget limit.

**Cluster: Psychological Pressure (🔴 Critical)**
- Worry: Notifications may trigger financial anxiety rather than financial awareness
- Worry: Users in debt may experience shame spirals when limits are breached repeatedly
- Worry: The feature benefits the bank (more engagement) while the harm falls on the user

*Ethical Objective:* "We commit to supporting financial awareness without triggering shame or anxiety, because users who are already in financial difficulty don't need their stress amplified."

*Design Constraint:* "Notifications must include one constructive next step — not just an alert. No notification may mention the overage more than once."

*Test Question:* "If we showed this feature to users currently experiencing financial stress, would they describe it as helpful or distressing?"

**Cluster: Power & Fairness (🟡 Monitor)**
- Worry: The feature only exists for users who can afford to set a budget — users with no buffer have nothing to protect
- Worry: The bank's algorithm may know about financial distress before the user does, but uses that signal for upselling rather than support

**Worrystorm Summary:**
"The core ethical tension in this feature is that financial stress is both the problem the feature tries to solve and the mechanism through which it generates engagement. The design must commit to user wellbeing as the primary metric — not notification open rates — and build explicit protections against shame-triggering communication patterns, especially for users already over their limits."

---

## See also

- [Anti-Heroes](anti-heroes.md) — finds who is currently harmed; Worrystorming asks who will be harmed if this continues at scale
- [Responsible Design Prism](responsible-design-prism.md) — diagnoses where a product currently sits; Worrystorming helps you avoid ending up on the dark side
- [Values Levers](values-levers.md) — once Worrystorming surfaces concerns, Values Levers identifies organizational mechanisms to act on them
- [Pledge Works](pledge-works.md) — takes the ethical commitments surfaced in Worrystorming and stress-tests them against business pressure
