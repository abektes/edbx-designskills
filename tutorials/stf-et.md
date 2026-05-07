# STF-ET — Ethics Toolkit: Put Values Into Action

**The short version:** A five-tool chain from Stanford for thinking rigorously about the long-term ethical futures of a technology — not just "what happens next sprint" but "what does this look like in five years, and who has been helped or harmed by then?"

---

## Who made it

The **Ethics Toolkit: Put Values Into Action** (referred to in this package as STF-ET) was developed by the **McCoy Family Center for Ethics in Society at Stanford University**, one of the leading centers for ethics in technology research in the United States. The toolkit is released under a **Creative Commons CC BY 4.0 license**, meaning it is freely usable and adaptable.

The Stanford McCoy Center works at the intersection of philosophy, policy, and technology practice. The STF-ET toolkit reflects that intersection: it is philosophically rigorous enough to identify real ethical tensions, and practical enough to be used by product teams without a philosophy background.

---

## The problem it solves

Most ethical design methods are synchronic — they examine what's happening now. STF-ET is diachronic — it examines what will happen over time.

This matters because some of the most significant harms of technology are not visible at launch. They emerge from adoption patterns, from behavioral change over time, from how different populations use the technology differently, from regulatory responses, from market consolidation, from the second-order effects of first-order decisions.

A team that only asks "is this ethical now?" will miss those futures. STF-ET gives teams a structured method for imagining futures they haven't lived yet — and evaluating them before they arrive.

---

## When to use it

- **For any technology with long-term adoption effects** — which is most technology
- **Before making an architectural decision** — platform choices, data storage choices, business model choices that are hard to reverse
- **When thinking about AI or algorithmic systems** — where behavior changes as models learn, data compounds, and adoption grows
- **When regulators or policymakers might be involved** — STF-ET helps anticipate regulatory responses
- **When you want to evaluate not just "should we build this?" but "what will the world look like if we do?"** — the method is designed for that question
- **For research teams and senior leadership** — the five-tool chain requires more time than a single-session audit, and produces richer output

---

## What it produces

STF-ET chains five tools together in sequence:

**Tool 1 — Future Story:** Write a narrative scenario set 5-10 years in the future where this technology has been widely adopted. The scenario includes specific characters, contexts, and events — not an abstract projection but a concrete story. The goal is to make the future legible enough to evaluate.

**Tool 2 — Impacts Explorer:** Systematically map the impacts of the Future Story scenario across stakeholder groups — who benefits, who is harmed, how, and how much. This is structured stakeholder impact analysis grounded in the specific future you've described.

**Tool 3 — Ethics Frame:** Apply ethical frameworks to the impacts identified. Which values are advanced? Which are violated? Which trade-offs are being made? The Ethics Frame forces explicit articulation of the normative dimensions of the scenario.

**Tool 4 — Ethics Gauge:** Rate the overall ethical quality of the future scenario. Where on the spectrum does this land — from deeply harmful to genuinely beneficial? This is a summary verdict that synthesizes the first three tools.

**Tool 5 — Weighing Options:** Given the ethical analysis, what should be done? The method generates alternative futures — paths not taken — and evaluates whether different design, policy, or governance choices would produce better outcomes. This is the action-oriented conclusion of the chain.

---

## The relationship between tools

Each tool builds on the previous one. The Future Story gives you something concrete to analyze. The Impacts Explorer gives you who is affected. The Ethics Frame gives you the normative lens. The Ethics Gauge gives you a verdict. Weighing Options gives you paths forward.

Running only Tool 1 gives you a scenario. Running all five gives you an ethical analysis and a set of actionable alternatives.

---

## How to use it with AI

Describe the technology or product you're analyzing and the time horizon you want to think about (5 years? 10 years? The long run?). Tell the AI any existing concerns you have. The AI will run all five tools in sequence — from future narrative through impact mapping, ethical framing, verdict, and alternative paths — producing a complete STF-ET analysis.

---

## A quick example

**Technology:** A large language model-powered customer service platform that replaces human agents with AI.

**Tool 1 — Future Story (2030):** Sarah works at a retail company in 2030. In 2025, her company replaced its 400-person customer service team with an AI platform. She was one of 50 retained staff who "manage" the AI — but her role is increasingly monitoring dashboards rather than helping customers. The AI handles 99.7% of contacts. When customers reach the human team, it's because the AI has failed in a way that is statistically rare but emotionally significant. Sarah spends her days handling the cases the AI made worse.

**Tool 2 — Impacts Explorer:**
- Customers with simple issues: benefit (faster, 24/7 service)
- Customers with complex, emotional, or unusual issues: harmed (AI cannot provide the judgment, empathy, or flexibility the situation requires)
- Former customer service workers (mostly lower-income, disproportionately women and people of color): harmed through job loss
- Remaining human staff: new form of work that is more stressful and less skilled
- The company: cost savings, with hidden costs in customer trust erosion for complex cases

**Tool 3 — Ethics Frame:** Consequentialist lens finds mixed overall benefit with concentrated harm on specific populations. Deontological lens finds violation of workers' right to meaningful labor and customers' right to human recourse when things go wrong. Justice lens finds that cost savings disproportionately extracted from lower-income workers.

**Tool 4 — Ethics Gauge:** Problematic. Net benefit is real but concentrated toward shareholders; net harm is concentrated toward workers who had least capacity to absorb it.

**Tool 5 — Weighing Options:** What if the company had: (a) used AI to augment agents rather than replace them, reducing workload without job loss? (b) implemented a transparent human escalation path available on first request? (c) shared productivity gains with the workforce through reduced hours rather than reduced headcount? Each path has different cost structures and different ethical profiles.

---

## See also

- [Black Mirror Brainstorming](black-mirror-brainstorming.md) — also futures-based, but uses speculative narrative more creatively; STF-ET is more structured and analytical
- [Worrystorming](worrystorming.md) — generates near-term worries; STF-ET maps long-horizon futures
- [Anti-Heroes](anti-heroes.md) — finds who is harmed now; STF-ET maps who will be harmed in the future
