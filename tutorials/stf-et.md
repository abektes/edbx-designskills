# STF-ET — Ethics Toolkit: Put Values Into Action

**The short version:** A five-tool chain from Stanford that takes a team from exploring a piece of work, through weighing its benefits, harms and fairness, to choosing between concrete options. It starts with a story told from the future — "who has been helped or harmed by then?" — and ends in a decision.

---

## Who made it

The **Ethics Toolkit: Put Values Into Action** (referred to in this package as STF-ET) was developed by the **McCoy Family Center for Ethics in Society at Stanford University**, one of the leading centers for ethics in technology research in the United States. The toolkit is released under a **Creative Commons CC BY 4.0 license**, meaning it is freely usable and adaptable.

The Stanford McCoy Center works at the intersection of philosophy, policy, and technology practice. The STF-ET toolkit reflects that intersection: it is philosophically rigorous enough to identify real ethical tensions, and practical enough to be used by product teams without a philosophy background.

---

## The problem it solves

Most ethical design methods examine what's happening now, and stop once the problems are named. STF-ET does two things they don't: it starts from the future — a story of what the work did once it was out in the world — and it carries the analysis through to a choice between concrete options.

This matters because some of the most significant harms of technology are not visible at launch. They emerge from adoption patterns, from behavioral change over time, from how different populations use the technology differently, from regulatory responses, from market consolidation, from the second-order effects of first-order decisions.

A team that only asks "is this ethical now?" will miss those futures, and a team that stops at a list of harms still has to decide what to do. STF-ET gives a structured path from one to the other: imagine the future, evaluate it, then decide.

---

## When to use it

- **For any technology with long-term adoption effects** — which is most technology
- **Before making an architectural decision** — platform choices, data storage choices, business model choices that are hard to reverse
- **When thinking about AI or algorithmic systems** — where behavior changes as models learn, data compounds, and adoption grows
- **When you have to choose between two or more courses of action** — Weighing Options compares them and ends in a Future Direction with its rationale
- **When regulation is part of the picture** — Weighing Options makes you name regulatory changes among the obstacles, with a contingency plan for each
- **When you want to evaluate not just "should we build this?" but "what will the world look like if we do?"** — the method is designed for that question
- **At any project stage** — the full chain takes more time than a single-session audit, but you can run one tool or one phase on its own

---

## What it produces

STF-ET chains five tools together in sequence:

**Tool 1 — Future Story:** Narrate the work from the future, using a six-part story spine (adapted from Kenn Adams): the problem, the solution, its benefits, its harms, the cascading consequences, and what was done to mitigate them. Writing it as a story, honestly including what went wrong, opens reflection before anyone has to be analytically precise.

**Tool 2 — Impacts Explorer:** Map the ripple effects — direct effects, the secondary effects each one sets off, and the values each effect reinforces or undermines — with a separate pathway for each major stakeholder group, so you can see whether benefits and harms are distributed fairly.

**Tool 3 — Ethics Frame:** A single worksheet: the values driving the work, the benefits and harms from the Impacts Explorer connected to those values, and the actions that would expand the benefits and reduce the harms. It ends in a **Bottom Line** specific enough to hold someone to.

**Tool 4 — Ethics Gauge:** An at-a-glance assessment across four dimensions — *How beneficial? How harmful? How fair? How empowering?* — each with three spectra marked from − to +, plus what you'd expect to observe and what you still need to find out. It deliberately does **not** reduce ethics to a single score; the picture comes from the four dimensions together.

**Tool 5 — Weighing Options:** Compare at least two concrete courses of action on their societal impact, organizational impact, obstacles, and fit with the values from Tool 3, and end with a **Future Direction** — the choice, with its rationale spelled out.

Every run closes with a **Closing Synthesis**: the values prioritized, the trade-offs accepted, and the actions to take.

---

## The relationship between tools

Each tool feeds the next, and each hands over an explicit "carries forward" block. The Future Story gives you something concrete to analyze. The Impacts Explorer maps who is affected and which values are at stake. The Ethics Frame turns that into values, benefits, harms and actions. The Ethics Gauge checks the whole picture across four dimensions. Weighing Options turns it into a decision.

You don't have to run all five. You can enter at any tool — say, starting from an Ethics Frame your team already has — and the output states which tools ran and why the others were skipped, then still closes with the synthesis.

---

## How to use it with AI

Describe the technology or product you're analyzing, what stage it's at, any concerns you already have, and — if you're deciding — the options on the table. Ask for the full chain or for specific tools. The AI will run the tools in order, pass each one's output forward, and finish with the Closing Synthesis.

---

## A quick example

**Technology:** A large language model-powered customer service platform that replaces human agents with AI.

**Tool 1 — Future Story (told from 2030):** *Once upon a time* customers waited 40 minutes to reach anyone. *Until one day* the company replaced its 400-person support team with an AI platform, keeping 50 staff to supervise it. *And because of that* simple questions were answered instantly, day or night. *But also* customers whose problems were complex or distressing hit a wall. *In turn* the remaining staff spent their days on cases the AI had made worse, and trust eroded among the customers who mattered most. *One thing we could have done differently is* guarantee a route to a human on first request.

**Tool 2 — Impacts Explorer:**
- Customers with simple issues → faster service → *convenience* reinforced
- Customers with complex or distressing issues → no human recourse → *dignity* and *fairness* undermined
- Former support workers (mostly lower-income) → job loss → *security* undermined
- Remaining staff → monitoring dashboards instead of helping people → *meaningful work* undermined

**Tool 3 — Ethics Frame, Bottom Line:** The benefit is real but lands on the people who needed help least; the harm lands on the customers with the hardest problems and the workers least able to absorb it. Keep the platform, add a guaranteed human route, and retrain rather than cut.

**Tool 4 — Ethics Gauge:** Beneficial: + for individuals with simple issues, spread widely. Harmful: − concentrated harm on complex cases, largely preventable. Fair: − those harmed are less advantaged than those who benefit. Empowering: − customers lose the choice to reach a person.

**Tool 5 — Weighing Options:** Option A, full replacement: largest savings, highest trust and fairness cost. Option B, AI augments agents: smaller savings, keeps human recourse and jobs. **Future Direction:** Option B — the cost difference is smaller than the trust lost on the cases that matter most to customers.

**Closing Synthesis:** Values prioritized — dignity, fairness. Trade-off accepted — slower cost reduction. Actions — human escalation on first request within one quarter, owned by the Head of Support; redeploy and retrain rather than lay off.

---

## See also

- [Black Mirror Brainstorming](black-mirror-brainstorming.md) — also futures-based, but uses speculative narrative more creatively; STF-ET is more structured and analytical
- [Worrystorming](worrystorming.md) — generates worries at volume; run it first, then STF-ET structures them into an impact map and carries them through to a decision
- [Anti-Heroes](anti-heroes.md) — names manipulative moves in the design as it is now; STF-ET weighs where the work leads and what to do about it
