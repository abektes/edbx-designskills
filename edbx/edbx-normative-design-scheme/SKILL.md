---
name: edbx-normative-design-scheme
description: Use when a designer wants to assess a design decision against established ethical theory, brainstorm design alternatives rooted in normative ethics, evaluate whether a product's intention, effects, and design obligations are aligned, apply philosophical ethics frameworks to concrete design problems, or explain design decisions using ethical theory language. Apply the Normative Design Scheme to evaluate design goals and generate design ideas through three normative ethical lenses — Virtue Ethics (intention), Consequentialism (effect), and Deontology (design/duty). Trigger this skill for any mention of applying ethics theories to design, design duty or obligation, consequences of design decisions, virtue in design, deontological design review, or when someone asks "what is the ethically right thing to do here?" Also trigger for "Normative Design Scheme", "ethics lenses", "virtue ethics design", "deontology design", or "consequentialism design".
version: "1.0"
tags: [ethical-design, decision]
---

# Normative Design Scheme

## Overview

Normative Design Scheme allows you to assess your design goals and brainstorm ideas based on normative ethical theories. Every design carries intentions, produces effects, and follows or breaks rules. The Normative Design Scheme makes each of those dimensions visible by applying three philosophical traditions as lenses.

The method uses a three-part normative ethical framework applied to any design decision or product. Each lens asks a different question:

- **Intention — Virtue Ethics**: What virtues does the design promote in its creators and users?
- **Effect — Consequentialism**: What outcomes does the design produce for all stakeholders?
- **Design — Deontology**: What duties and moral rules does the design follow or break?

Using the same three-part structure, you can also brainstorm ideas to build ethical design outcomes rooted in normative ethical theory. The method works in both **Assess** mode (evaluating an existing design) and **Generate** mode (brainstorming ethical alternatives from scratch).

> **Mindset check:** The three lenses are not a hierarchy. Deontology doesn't trump Consequentialism. They are three different ways of asking "is this right?" When they agree, you have a strong ethical signal. When they conflict, you have a genuine ethical dilemma that deserves acknowledgment, not artificial resolution.

## Use This Skill When

- You want to evaluate a design decision against established ethical theory.
- You are brainstorming design alternatives and want them grounded in ethical reasoning.
- You need to explain *why* a design decision is ethical or unethical in philosophically rigorous terms.
- A team is debating what the "right" thing to build is and needs a structured framework.
- You want to bridge philosophical ethics and practical design thinking.
- You are facilitating an ethics workshop and need a repeatable evaluation method.

## Inputs

Provide as many of these as are available:

- A design goal, product feature, or existing product to evaluate
- Optionally: a specific ethical tension or design decision to focus on
- Optionally: a stakeholder group whose interests should be centered
- Optionally: a mode preference — **Assess** (evaluate existing design) or **Generate** (brainstorm ethical alternatives)

## Workflow

Normative Design Scheme applies three lenses sequentially, then synthesizes across them. Crucially, the method is **not** "apply virtue ethics, then consequentialism, then deontology in sequence." That collapses the method into generic ethical analysis. The distinctive moves are:

1. A **shared stakeholder & power map** that all three lenses operate on (so the lenses are evaluating the same reality, not three different realities).
2. A **Triad Conflict Matrix** that explicitly surfaces where the lenses *disagree* — not a synthesis paragraph but a structured artifact.
3. A **Universal Law Test** as a named output, not an embedded thought experiment.
4. **Creator Impact** as an explicit dimension of the Virtue lens, not a passing aside — what kind of designers does this design make us into?
5. A **Normative Design Statement** that names alignment, names dilemma, and commits to a course of action — the signature artifact.

These five moves are what distinguishes the Normative Design Scheme from "applying three ethical theories." Without them, the output is generic ethical analysis and the method is doing no work.

---

### Step 0 — Stakeholder & Power Map (shared input for all three lenses)

Before any lens is applied, enumerate every population the design touches. The three lenses must operate on the same stakeholder reality — otherwise Virtue evaluates one set of relationships, Consequentialism evaluates another, and Deontology a third, and the synthesis becomes incoherent.

**Named stakeholder enumeration (minimum 5 distinct rows; "users" alone is not a stakeholder):**

| Stakeholder | Relationship to design | Power they have | Power they lack | What they would lose |
|---|---|---|---|---|
| Primary users | (intended audience) | (the levers — exit, complaint, switch) | (what they cannot influence) | |
| Vulnerable subgroups | (named specifically: minors / neurodivergent / low-income / undocumented / abuse survivors / people in crisis / older adults / non-dominant linguistic group / disabled users — pick 2–4 actually relevant) | | | |
| Non-users in the user's environment | (people scanned, photographed, profiled-by-association, downstream affected) | | | |
| Workers in the supply chain | (moderators, gig workers, annotators) | | | |
| The designers/creators themselves | (yes — designers are stakeholders; the design shapes what kind of professionals they become) | | | |
| Future-affected populations | (people in 5 years using accumulated data; future users of the precedent this sets) | | | |

**Power asymmetry summary:** one paragraph naming the 3 most significant power asymmetries between the operator and any stakeholder, with reversibility (can the affected party exit / undo / contest?).

**Non-Obvious Harms Inventory (required, minimum 5 named):** harms that the heuristic categories below would miss.

| # | Non-obvious harm | Population most affected | Mechanism |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

Examples to scan for: inferred-data harms (data the system creates by inference), aggregation harms, proxy-variable harms (zip code → race), competence foreclosure, intrinsic-motivation crowd-out, attentional-architecture formation, social-fabric harms, future-you harms, bystander harms, worker harms (moderator exposure, gig labor under algorithmic management).

This stakeholder map and harms inventory feed every lens below — each lens must reference the named stakeholders and at least one non-obvious harm from the inventory.

---

### Lens 1: INTENTION — Virtue Ethics

*What virtues does the design promote — in users, AND in the people who build and operate it?*

The Virtue lens has two distinct sub-questions; both are required.

**A. User-facing virtue assessment**
- What virtue does this design promote (or undermine) in its users? (autonomy, patience, honesty, generosity, attention, courage)
- Does the design encourage virtuous user behavior, or does it train the opposite (compulsion, distraction, deception, conformity, isolation)?

**B. Creator Impact (required, not optional)**
This is the move most often skipped. A design isn't only judged by what it does to users — it also shapes what kind of professionals the people who build and operate it become.

Specifically name:
- **What kind of designer/engineer/PM does this design make us into?** (e.g., "An engineer who optimizes for engagement learns to treat psychological vulnerability as a feature rather than a hazard.")
- **What habits of moral attention does this design require us to cultivate or suppress?** (Does the org reward people who raise ethical concerns, or does it reward people who hit the metric and stay quiet?)
- **What would we have to believe about our users to build this in good conscience?** Sometimes the answer reveals the move requires self-deception or contempt.
- **What would the team be embarrassed to explain to a journalist, a regulator, or their own children?** Embarrassment is moral data.

If creators come out of the project ethically diminished — more cynical, more compromised, less attentive — that is a Virtue lens failing regardless of what users experienced.

**Generative prompt:**
- "If we designed this with [virtue X] as our north star, what would we build differently?"
- "What would a caring designer add/remove from this design?"
- "What design would make our team proud to attribute their name to?"

**Output:** A virtue assessment (user-facing + creator impact) + 2 virtue-driven design ideas.

---

### Lens 2: EFFECT — Consequentialism

*What are the outcomes for all stakeholders?*

Assessment questions:
- What are the intended consequences for primary users?
- What are the unintended consequences for secondary/tertiary stakeholders?
- Does the design produce the greatest good for the greatest number?
- Which moral and social norms does the design adhere to or violate?
- What happens at scale — if 10 million people use this, what changes?

Generative prompt:
- "If we optimized purely for the best outcome for all affected, what would we build?"
- "What one change would most improve the consequence profile of this design?"

**Output:** A consequence map (positive/negative, primary/secondary stakeholders) + 2 consequence-driven design ideas.

---

### Lens 3: DESIGN — Deontology

*What are the duties and moral rules this design must follow?*

Assessment questions:
- What moral rules does this design follow or break?
- What obligations does the design have to different stakeholders?
- Does the design treat users as ends in themselves, or as means to a business goal?
- What rights does this design respect or violate? (privacy, autonomy, dignity, informed consent)
- What would a universal law version of this design look like? (Kantian test: "What if every product did this?")

Generative prompt:
- "If we had a non-negotiable duty to [obligation X], what would we change?"
- "What design features would survive the universal law test — and which would not?"

**Output:** A duty/obligation map (what the design owes to each stakeholder) + 2 duty-driven design ideas.

---

### Universal Law Test (required output, not embedded thought experiment)

The Universal Law Test is the Kantian thought experiment formalized as a structured output. Apply it to every named design decision:

| Design decision | If every product did this, what world results? | Is that world livable? | Decision verdict |
|---|---|---|---|
| e.g., "Default-on engagement-driven recommendation in mental-health content categories" | Every wellness app, every news app, every messaging app amplifies content that triggers user distress because distress drives engagement | No: the public information environment becomes net-corrosive; people who most need stability are most aggressively destabilized | Fails the test — universalizing this design produces an unlivable world |
| e.g., "Cancel flow with a confirm dialog and one click" | Every product allows users to leave with the same friction they joined | Yes — users have agency, businesses must earn retention | Passes the test |

If a design decision fails the Universal Law Test, it cannot be ethically defended on Deontological grounds — even if it passes Virtue and Consequentialist lenses, this is a Deontological red flag that requires acknowledgment.

---

### Triad Conflict Matrix (the methodology's signature artifact)

Cross-lens synthesis is not a paragraph — it is a structured matrix. For every named design decision, fill out where each lens lands:

| Decision | Virtue verdict | Consequence verdict | Deontology verdict | Triad alignment |
|---|---|---|---|---|
| | ⬆ promotes / ⬇ undermines / ↔ neutral | ⬆ net positive / ⬇ net negative / ↔ mixed | ⬆ honors duty / ⬇ violates duty / ↔ contested | All-aligned 🟢 / Two-against-one 🟡 / All-conflict 🔴 |

For every 🟡 (two-against-one) row: name the **dilemma honestly**. Example: *"Consequentialist analysis says targeted political ads increase voter information access (positive consequence); Virtue and Deontology agree the manipulation potential outweighs that gain. The dilemma is that 'better-informed voters' is a real good, but it cannot be purchased at the cost of treating voters as means rather than ends."*

For every 🔴 (all-conflict) row: do not synthesize artificially. Name it as an unresolved ethical decision the team must make explicitly, not paper over.

---

### Cross-Lens Synthesis & Commitment

After the Triad Conflict Matrix:

- Name the **strongest 🟢 alignment finding** — the design move all three lenses endorse. This is your highest-confidence ethical recommendation.
- Name the **most serious 🔴 conflict finding** — the design move with no ethical resolution. This requires team-level commitment, not analysis.
- Produce a **Normative Design Statement** in this exact form:

> "This design is grounded in [virtue X] — promoting [user virtue] in users and [creator virtue] in our team. It produces [primary consequence] for [named stakeholders] while imposing [named harm] on [named affected population]. It fulfills the duty of [obligation Z], but cannot fully reconcile its [unresolved tension]. We commit to [specific course of action] to honor what the lenses agreed on, and to [specific course of action] to acknowledge what they did not."

The closing two clauses — "we commit to X… and we commit to Y…" — are required. A Normative Design Statement that names alignment without naming what to do about the unresolved conflict is incomplete.

---

## Output Format

### Normative Design Scheme: [Design Name]

Brief framing of what was evaluated and the mode (Assess/Generate).

### Stakeholder & Power Map

(From Step 0 — required. Without this, the three lenses operate on incompatible realities.)

| Stakeholder | Relationship | Power they have | Power they lack | What they would lose |
|---|---|---|---|---|

**Power asymmetry summary:** [one paragraph]

### Non-Obvious Harms Inventory

(From Step 0 — required, minimum 5 named.)

| # | Non-obvious harm | Population | Mechanism |
|---|---|---|---|
| 1 | | | |
| ... | | | |

### Lens 1: Intention — Virtue Ethics

**User-facing virtue assessment:**
- [Finding 1]
- [Finding 2]

**Creator Impact (required):**
- What kind of designers/engineers/PMs does building this make us into?
- What habits of moral attention does it require us to cultivate or suppress?
- What would we have to believe about our users to build this in good conscience?
- What would we be embarrassed to explain to a journalist or a child?

**Design Ideas:**
1. [Virtue-driven idea]
2. [Virtue-driven idea]

### Lens 2: Effect — Consequentialism

**Assessment:**
- [Finding 1]
- [Finding 2]

**Design Ideas:**
1. [Consequence-driven idea]
2. [Consequence-driven idea]

### Lens 3: Design — Deontology

**Assessment:**
- [Finding 1]
- [Finding 2]

**Design Ideas:**
1. [Duty-driven idea]
2. [Duty-driven idea]

### Universal Law Test

| Design decision | World if universalized | Livable? | Verdict |
|---|---|---|---|

### Triad Conflict Matrix (signature artifact)

| Decision | Virtue | Consequence | Deontology | Alignment |
|---|---|---|---|---|

For every 🟡 row: name the dilemma honestly (no artificial resolution).
For every 🔴 row: name it as an unresolved ethical decision requiring team commitment.

### Cross-Lens Synthesis & Commitment

- **Strongest 🟢 alignment finding:** [highest-confidence recommendation]
- **Most serious 🔴 conflict finding:** [unresolved tension requiring commitment]

**Normative Design Statement:**

> "This design is grounded in [virtue X] — promoting [user virtue] in users and [creator virtue] in our team. It produces [primary consequence] for [named stakeholders] while imposing [named harm] on [named affected population]. It fulfills the duty of [obligation Z], but cannot fully reconcile its [unresolved tension]. We commit to [specific course of action] to honor what the lenses agreed on, and to [specific course of action] to acknowledge what they did not."

### Priority Recommendation

Based on where lenses most strongly agree: [redesign recommendation, naming which named stakeholder benefits and which non-obvious harm it mitigates].

## Guardrails

- Do not treat the three lenses as a hierarchy — they are co-equal perspectives, not ranked alternatives.
- Do not resolve genuine ethical dilemmas artificially. When lenses conflict, name the dilemma honestly.
- Do not use philosophical jargon without explanation. Every theoretical term must be explained in plain language.
- Do not skip the cross-lens synthesis. The synthesis is where the method's real power lies.
- Do not limit yourself to assessment mode — the generative prompts produce design ideas, not just critique.
- Do not assume one lens will always dominate. Different designs raise different ethical dimensions.

## Deliverable Quality Bar

A strong Normative Design Scheme output:

- **completes the Stakeholder & Power Map** (Step 0) with at least 5 distinct named stakeholders, including specifically-named vulnerable subgroups, the design team itself as a stakeholder, and future-affected populations
- **produces a Non-Obvious Harms Inventory** with at least 5 named harms beyond what the heuristic categories catch
- applies all three lenses to the design with substantive findings per lens, **referencing the named stakeholders** rather than abstract "users"
- **completes the Creator Impact analysis in Lens 1** — what kind of designers does this design make us into; what habits of moral attention it requires us to cultivate or suppress; what we'd be embarrassed to explain. Without this, the Virtue lens is incomplete.
- produces 2 design ideas per lens (6 total minimum)
- explains each philosophical term in accessible language
- **produces a Universal Law Test table** for every named design decision, naming the world that results from universalization and whether it is livable
- **produces the Triad Conflict Matrix** — the methodology's signature artifact — explicitly naming where the three lenses align (🟢), conflict two-against-one (🟡), or all-disagree (🔴). For every 🟡 and 🔴 row, the dilemma is named honestly without artificial resolution.
- produces a Normative Design Statement in the prescribed form, including the closing two-part commitment ("we commit to X… and to Y…")
- works in both Assess and Generate modes

## Integration with Other EDBX Skills

- **edbx-responsible-design-prism** places a design on an ethical spectrum. Normative Design Scheme provides the philosophical grounding to explain *why* it sits there.
- **edbx-worrystorming** surfaces ethical fears. Normative Design Scheme provides the theoretical framework to evaluate whether those fears are justified.
- **edbx-cider** surfaces exclusionary assumptions. Normative Design Scheme evaluates them through the Deontology lens (do we owe inclusion as a duty?).
- **edbx-motivation-matrix** maps user motivation. Normative Design Scheme asks whether that motivation exploits virtue, produces harm, or violates duty.
- **edbx-humane-design-guide** flags sensitivity exploitation. Normative Design Scheme provides the ethical theory to condemn or justify each sensitivity decision.

## Hashtags

#evaluateoutcomes #applyvalues #designresponsibility

## See Also

- Layers of Effect
- Envisioning Cards
- Value Voting
