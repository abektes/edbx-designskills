# Pledge Works

**The short version:** Translates good ethical intentions into written pledges, then (an edbx addition) stress-tests each pledge against realistic business pressure to find out which ones will actually hold.

---

## Who made it

Pledge Works is a tool from ResponsibleTech.Work, published as a practical way to write pledges for better outcomes inside the processes a product team already runs (kickoffs, sprint planning, retrospectives). Its page says the tool is still under development and is seeking wider validation. Role-based pledges can draw on professional codes such as the ACM Code of Ethics.

The tool responds to a gap between good intentions and everyday product decisions: teams write ethical principles that sound good, agree to them in a kickoff meeting, and then lose them in the day-to-day. Pledge Works aims to close that gap.

---

## The problem it solves

There is an enormous gap between a team's stated values and their behavior under pressure. Teams write "we respect user privacy" in their documentation and then implement default opt-in data collection when a growth target is at risk. Teams commit to "accessible design" and then ship inaccessible features when the sprint is short.

This doesn't happen because people are dishonest. It happens because abstract commitments offer no resistance to concrete pressures. "We value privacy" doesn't tell you what to do when your VP asks you to enable location tracking for a new feature.

Pledge Works converts abstract values into specific behavioral commitments — and then forces the team to test those commitments against realistic scenarios where business pressure will push against them.

---

## When to use it

- **After establishing team values** — Pledge Works is the step that makes values actionable
- **Before a product launch** — to make sure the team's ethical commitments will survive the launch process
- **When you want commitments the team will actually keep** — not aspirational principles, but specific behavioral promises
- **When business pressure is predictable** — when you know the growth targets, the investor expectations, or the competitive dynamics that will test your commitments
- **When you want accountability** — pledges are written down and kept visible in the team's tools, creating a record that survives team turnover and individual memory

---

## What it produces

Pledge Works generates pledges in three formats:

**Simple Pledge:** A direct behavioral commitment. "We will not use location data for advertising without explicit opt-in consent." Clear, specific, testable.

**Responsible Story Pledge:** A pledge that says who is pledging, what they pledge, and why. The published tool treats the reason as optional; this skill asks for it. "We will tell users clearly when their data is shared with third parties, because users who trusted us with their data deserve to understand how it's being used." The skill requires the "because" clause because it keeps a pledge tied to a value.

**To Whom Pledge:** A pledge explicitly directed at a named group of people. "To our users who are managing debt: we will never use financial vulnerability signals to drive upsell behavior." This format makes the human stakes of the commitment concrete.

The skill adds a set of edbx operationalization fields to each pledge; they are not part of the published method, which asks for a pledge checklist of acceptance criteria. A pledge missing any field is aspiration, not commitment:

- **Quantitative success indicator** ✅ — a number, percentage, or named standard (not "we'll be more careful"). Example: "Cancellation flow ≤ 3 clicks; cancellation completion rate ≥ 90%."
- **Quantitative failure signal** ⚠️ — the threshold at which the pledge is considered broken. Example: "Disparate-impact ratio < 0.8 on any subgroup with n ≥ 30."
- **Named owner** — a role or person accountable. "The team" is not an owner.
- **Consequence for breach** — what concretely happens if the pledge is broken: "release blocks; CTO notified," "feature is rolled back within one sprint," "incident is publicly logged in our quarterly responsibility report." Without consequence, the pledge has no teeth.
- **Review cadence** — when this is checked (every sprint demo, monthly ethics review, pre-launch + 30/90/180 days post-launch).

Also added by edbx:

- **Early Warning Signal** — the leading indicator that appears *before* the pledge breaks. Not "we violated our privacy pledge" but "leadership is asking for user location data without having raised the consent design question." If the team recognizes the signal early, the pledge has a chance of surviving.
- **Pledge Stress Test** — a realistic business pressure scenario presented to each pledge. Reveals which pledges are real vs. aspirational, and produces a protective mechanism for the ones that might break.

The skill also produces two further artifacts the published method doesn't include:

- **"What We Refuse to Build" Red-Line Register** — pledges describe what we *will* do; the red-line register describes **what we refuse to do, regardless of business pressure**. 3–5 named refusals at the **feature level** (not values level), each with a **named owner with veto authority** and a consequence if the line is crossed. Example: *"We will not target behavioral ads to users under 16. Veto: Head of Trust & Safety. Consequence: PM responsible for proposal is removed; incident logged; board notified."*
- **Pledge-to-Product Traceability** — every pledge maps to a specific product decision it would or wouldn't trigger. Pledges that don't map to a feature decision are sharpened or dropped.

---

## The key insight

Most ethics frameworks tell you what to commit to. This skill's edbx additions tell you when that commitment is about to be broken, and what to do about it before it happens.

The Early Warning Signal (an edbx addition) is the skill's most useful output. It shifts the ethics conversation from "we agreed to this in principle" to "here is the specific moment when that agreement will be tested, and here is what we agreed to do when it arrives."

---

## How to use it with AI

Describe the product, the values or principles your team has agreed to, and any known business pressures or growth targets that might conflict with them. The AI will generate pledges across all three formats, produce early warning signals for each, and run a stress test against realistic business pressure scenarios with recommendations for how to protect the commitments under that pressure.

---

## A quick example

**Team context:** Health app that tracks symptoms and medication adherence. Team has stated value: "user health data is sacred and will never be monetized."

**Simple Pledge:** "We will never sell, license, or share user health data with third parties for any commercial purpose, regardless of business pressure."

**Responsible Story Pledge:** "We will tell every user clearly, in plain language, exactly what health data we store and how long we keep it, because people sharing their health struggles with our app deserve to know it won't be used against them."

**To Whom Pledge:** "To users who came to us in a health crisis: we will never use crisis moments in your data to trigger upsells or advertising."

**Early Warning Signal (for first pledge):** "A business development conversation begins about 'research partnerships' with pharmaceutical companies. If health data is described as an 'asset' in that conversation, the pledge is at risk."

**Stress Test:** "Your investor asks why you're not monetizing the most valuable health dataset you're sitting on. Three other health apps in your category sell anonymized data. Your growth targets require new revenue streams." → Which pledges would bend under this pressure? → The Simple Pledge: leadership will be tempted to reframe data sharing as "research partnership" rather than "monetization."

**Protective mechanism:** "The pledge specifically covers 'research partnerships' that generate revenue for the company. Before any such partnership is discussed with a third party, the design team requires a documented ethics review with the pledge language explicitly referenced."

---

## See also

- [Ethical Contract](ethical-contract.md) — cross-disciplinary signed commitment; Pledge Works generates the pledges that go into that contract
- [DAH Cards](dah-cards.md) — produces an ethics manifesto; Pledge Works takes specific commitments from that manifesto and stress-tests them
- [Values Levers](values-levers.md) — identifies organizational mechanisms to build ethical design culture; Pledge Works creates the specific commitments that culture needs to protect
