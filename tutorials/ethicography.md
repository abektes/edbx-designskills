# Ethicography

**The short version:** A method for analyzing your team's design decisions — not just the product — for ethical intent versus manipulation. It treats what people say in design meetings as data, maps it on a matrix, and projects where the team is heading if they keep making the same kinds of decisions.

---

## Who made it

Ethicography was developed by **Shruthi Sai Chivukula, Colin M. Gray, and Janna Brier** in a 2019 CHI paper (ACM CHI 2019, Best of CHI Honorable Mention). The method was extended in 2024 with **"Quant-Ethico: An Approach to Quantifying and Interpreting Ethical Decision Making"** (Chivukula & Gray, DRS 2024). It is grounded in critical discourse analysis and HCI ethics research.

The name combines "ethics" and "ethnography" — it is, in essence, an ethnographic study of the ethics of a design team's own decision-making process.

---

## The problem it solves

Most ethical design audits look at the product. Ethicography looks at the decisions that produced the product.

This matters because harmful products rarely result from a single bad decision. They result from a series of decisions, each of which made sense in context, that collectively produced something that harms users. Understanding the ethical quality of those decisions — not just their outcomes — is how you prevent the next harmful product.

Ethicography treats design decisions and speech acts (what people say in meetings, design crits, and Slack conversations) as data. It asks: was this decision made with honest intent to serve users, or was it a manipulation wrapped in the language of user value?

---

## When to use it

- **After a project or sprint** — as an ethical retrospective on how decisions were made
- **When a product has shipped and caused harm** — to understand where in the design process the harm was created
- **For design research or publication** — when you need a formal, citable method for analyzing ethical quality in design process
- **When you want to understand your team's ethical patterns** — who makes value-centered decisions, who rationalizes manipulative ones, and what drives each
- **When you want to prevent future harm** — not just identify current harm, by making the decision trajectory visible before it compounds

---

## What it produces

Ethicography maps every design decision or speech act onto a **2×2 matrix**:

| | Persuasion (honest influence) | Coercion (overrides user agency) |
|---|---|---|
| **Explicit** | Value-Centered (ethical) | Explicit Manipulative (harm) |
| **Implicit** | Implicit Value-Centered | Implicit Manipulative |

Each decision gets a quadrant placement, a justification, and a values impact tag (⬆️ supports a value / ⬇️ undermines a value / ↔️ neutral).

For every move, the analysis also names **at least 2 specific affected populations** (not "users" generically) — including non-users (people scanned/photographed/talked-about-by-association), workers in the supply chain (moderators exposed to harmful content, gig workers under algorithmic management, annotators), and future-affected populations (users in 5 years using accumulated data; jurisdictions where data may be subpoenaed). For each, the analysis also flags **whether their voice was in the room** when the decision was made.

When a move undermines a user value, the analysis gives a **concrete-harm example** rather than abstract framing — naming the specific UX or accessibility mechanism. For accessibility findings: name the WCAG criterion or ARIA role failure (e.g., "WCAG 2.5.5 target size violation," "missing aria-live region for async error states"). Vague "accessibility issues" is not enough.

The method also detects **Performative Ethics Moves** — the most analytically valuable finding — where a decision uses ethical language to conceal a manipulative outcome. Examples:
- A "privacy settings" page that is architecturally incapable of actually deleting data → performs transparency, achieves opacity
- A "user wellbeing mode" that reduces notifications but triggers return anxiety → performs care, achieves re-engagement
- An "informed consent" modal with a 4,000-word ToS and a single "Agree" button → performs consent, achieves compliance

The output includes an **Ethical Trajectory Narrative** — how the ethical quality of decisions evolved over the project — and a **12-Month Trajectory Forward** projection: where will this product's ethical posture be in a year if the current decision patterns continue?

---

## The key insight

The 12-Month Trajectory Forward is what distinguishes Ethicography from a retrospective audit. Most ethics audits describe where you are. Ethicography tells you where you're going.

It names the specific pattern of decisions that is driving the drift — "this team consistently codes convenience as user benefit and friction as user harm, which will produce increasingly manipulative frictionless design over time" — and identifies the inflection point where the trajectory becomes irreversible.

---

## How to use it with AI

Describe a series of design decisions that were made on a product — ideally decisions you can explain in terms of who advocated for them and why. Meeting notes, design crit outputs, documented rationale, or even your memory of the conversations all work as input. Tell the AI you want to run Ethicography.

If you're working in research mode, specify that — the AI will apply formal coding language and include methodological notes suitable for academic documentation.

---

## A quick example

**Design decisions under analysis (messaging platform feature release):**

1. *Team adds end-to-end encryption after security concerns raised* — Explicit + Persuasion (Value-Centered) — ⬆️ Privacy
2. *PM argues that read receipts should be on by default "for better conversation"* — Implicit + Coercion — ⬇️ Autonomy (the "better conversation" framing obscures that read receipts remove the ability to read privately)
3. *Design adds typing indicators with no off switch* — Implicit + Coercion — ⬇️ Autonomy
4. *Legal adds a "Your messages may be used to improve our services" disclosure deep in the settings* — **Performative Ethics Move** — performs transparency, achieves opacity

**Ethical Trajectory Narrative:** The project began with a value-centered security commitment, but subsequent decisions moved toward implicit coercion — particularly around features that create social pressure (read receipts, typing indicators) and data collection disclosure. The team has not made any explicitly manipulative decisions, but the implicit pattern is drifting toward coercion.

**12-Month Trajectory Forward:** *"If current decision patterns continue, this product will drift toward Implicit Manipulative because every feature addition has prioritized engagement over user autonomy without naming the trade-off. The inflection point will likely be the next monetization conversation, when pressure to collect behavioral data will make the existing disclosure architecture feel like a solved problem rather than a held line. The team can prevent this by requiring an explicit values impact statement on every feature spec."*

---

## See also

- [Worrystorming](worrystorming.md) — anticipatory; Ethicography is retrospective. They bracket the design process from either end.
- [Responsible Design Prism](responsible-design-prism.md) — gives a spectrum reading of the current product; Ethicography explains the decision history that got it there
- [Ethical Contract](ethical-contract.md) — Ethicography surfaces what commitments a team has violated; the contract is the mechanism that makes those commitments explicit in the first place
