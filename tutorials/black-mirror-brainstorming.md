# Black Mirror Brainstorming

**The short version:** Write the dystopian episode of your product before it writes itself. This method uses speculative fiction as a serious ethical tool — by imagining how your product could go terribly wrong, you surface the risks too uncomfortable to name in a normal meeting.

---

## Who made it

Black Mirror Brainstorming was developed by **Klassen & Fiesler (2022)** and draws on earlier speculative design work by **Mauldin (2018)** — a practitioner exercise first published in *UX Collective*. The academic study of the method is Klassen & Fiesler's "Run Wild a Little With Your Imagination: Ethical Speculation in Computing Education with Black Mirror" (ACM SIGCSE 2022). It appears in *Universal Methods of Ethical Design* as a method for using narrative imagination as an ethical risk tool.

The name references Charlie Brooker's *Black Mirror* TV series — anthology episodes that take a current technology and show what it looks like when something about it goes wrong at scale. The method borrows that structure as a facilitation technique.

---

## The problem it solves

Most ethical risk exercises ask teams to list potential problems. The problem with that approach is that it stays inside the team's existing mental model. You list the risks you can already see. The risks you can't see — the ones that require you to imagine a world you'd rather not think about — never make it to the whiteboard.

Speculative fiction does something different. It lets you inhabit a future you hope won't happen. That emotional distance — "we're just writing a story" — makes it possible to name things that would be too uncomfortable to state directly in a requirements meeting.

Black Mirror Brainstorming turns that creative distance into an ethical tool.

---

## When to use it

- **Early in product development** — before the design is committed and consequences are hypothetical
- **When your team is optimistic in ways that feel fragile** — when you sense that nobody is saying what they're actually worried about
- **For any product that involves social dynamics, data, automation, or behavior change** — these are the highest-risk categories for non-obvious futures
- **When you want to find risks that normal risk exercises miss** — the speculative format surfaces things that bullet-pointed lists don't
- **When you have a cross-functional team** — writers, engineers, designers, and researchers all contribute differently to the scenario, which is the point

---

## What it produces

The method runs in four steps:

1. **What-if brainstorm** — 8–12 one-sentence prompts of the form *"How could [actor] use [feature] to [harm]?"*, grouped under three lenses so the team doesn't stop at the most obvious harm: **Economic** (scams, predatory pricing, value flowing the wrong way), **Political** (surveillance, manipulation, regulatory capture), and **Social** (divides, isolation, pressure on minors and vulnerable groups).

2. **Three Black Mirror episodes** — the strongest what-ifs, ideally one from each lens, each developed into a short episode: a title, a protagonist and antagonist (the antagonist can be the system itself), a concrete setting, a three-act arc — the design works as intended, then starts to bend, then the harm lands on someone — and a Netflix-style pitch blurb. Three, because one episode reads as an opinion and three read as a pattern.

3. **A pitch poster** — the episode that lands hardest, rendered as a single self-contained HTML file styled like a streaming-service title card, ready to drop into a review deck.

4. **Anti-goals** — 6–10 things the team commits never to allow, each traced back to the episode that surfaced it and paired with a concrete test that would show whether it's being upheld. The 2–3 **load-bearing** anti-goals — the ones that would invalidate the whole concept if violated — are flagged for leadership before shipping.

---

## The key insight

The scenarios work best when they are *specific*. Not "a user misuses the feature" but "a 17-year-old in a rural area with limited social support uses the feature at 2am in a way that accelerates the exact harm the product was designed to prevent."

The more concrete the scenario, the more useful it is as an ethical risk signal. Generic dystopias are just anxiety. Specific dystopias are design criteria.

---

## How to use it with AI

Describe your product or feature — what it does, who uses it, what it's intended to accomplish. Ask for a Black Mirror Brainstorming session. The AI will brainstorm what-ifs across the three lenses, write three episodes, render the strongest as an HTML poster, and derive anti-goals — the things the product must be designed *against* as well as toward — each with a test.

---

## A quick example

**Product:** A mental health check-in app that tracks mood daily and gives personalized insights.

**Episode 1 — "Premium Feelings" (Economic):** Users' mood data is acquired in a company merger and used by health insurers to adjust premiums. The app that helped people track their mental health now makes them uninsurable for having bad mental health.

**Episode 2 — "Culture Fit" (Political):** Employers start asking applicants to share their app's mood data as a condition of hiring — framed as "we care about your wellbeing." Users who refuse are passed over. The app designed to destigmatize mental health creates new discrimination vectors.

**Episode 3 — "Standard of Care" (Social):** The app becomes the standard of care recommended by GPs. Users who don't use it are seen as non-compliant. The reduction in talking therapy funding accelerates because the app "covers" mental health needs. A generation of people receives algorithmic wellness advice instead of human clinical support.

**Anti-goals extracted (each with a test):**
- Mood data never leaves the company, including in a merger or sale. *Test:* the data licence and the acquisition terms both forbid transfer; deletion on change of ownership is automated. **Load-bearing.**
- No employer can see, request or verify a user's data. *Test:* there is no export format an employer could ask for, and the terms prohibit employment use.
- Success is measured by users' mental-health outcomes, not engagement. *Test:* no retention or streak metric appears in the product team's OKRs.

---

## See also

- [Worrystorming](worrystorming.md) — generates worries in a more structured, categorized format; Black Mirror Brainstorming generates them through narrative
- [STF-ET](stf-et.md) — also a futures-based method, but more analytical and structured; Black Mirror is more creative and narrative-driven
- [Anti-Heroes](anti-heroes.md) — names the manipulative moves in today's design; Black Mirror shows the world in which those moves have scaled
