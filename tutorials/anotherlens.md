# Another Lens

**The short version:** Before you audit your design, audit yourself. Another Lens is a structured self-reflection method that helps you name the assumptions, experiences, and worldviews you're bringing to your work — so you can see what they're making you miss.

---

## Who made it

Another Lens comes from *Universal Methods of Ethical Design*, a practitioner-oriented book that collects ethical design methods in a format designers can actually use. It is listed as Principle #07.

The method is built on a long tradition of critical design thinking that treats the designer as part of the design — not a neutral tool who applies a process to an object. If you've heard of "positionality" in research or "designer responsibility" in HCI circles, Another Lens is the practitioner version of that idea.

---

## The problem it solves

Designers design for themselves without knowing it. Not out of selfishness — out of proximity. You know your own life. You understand your own context. Your assumptions about what "normal" looks like come from your own experience, and you import those assumptions into your work every time you make a decision.

The problem is that most designers never examine those assumptions. They audit the product for accessibility, the copy for clarity, the flow for friction — but they don't audit themselves for the invisible biases shaping those decisions in the first place.

Another Lens asks you to do that before you do anything else.

---

## When to use it

- **Before a major design decision** — when you're about to commit to a direction and haven't stopped to ask whose perspective is missing
- **When your team discussion feels one-sided** — when the same voices are confirming the same assumptions and nobody's pushing back
- **After a design mistake** — to understand not just what went wrong, but why your team didn't see it coming
- **During an inclusive design process** — when you want to be sure you're not centering your own experience as the default
- **When someone says "I'm not sure I've thought about this from enough angles"** — that's the literal trigger

---

## What it produces

Another Lens works through three lenses in sequence:

1. **Balance Your Bias** — turns the lens inward. You name the assumptions you're bringing, the decisions you made for yourself rather than your users, and the things you're holding onto that should be let go.

2. **Consider the Opposite** — turns the lens outward. You name who else is affected by this design (beyond your primary user), what the world looks like if your core assumption is wrong, and — crucially — who you're nervous to talk to about this. That nervousness is the signal.

3. **Embrace a Growth Mindset** — looks forward. You take what surfaced in the first two lenses and convert it into a learning intention and a reframe.

The session ends with a **Lens Statement**: a single sentence that fits on a sticky note, capturing what shifted during the session and what you're going to do about it.

> *"After applying Another Lens, I'm now questioning whether our budgeting model assumes financial stability as a prerequisite, and I plan to interview three gig-economy workers before the next design review."*

Crucially, Another Lens also produces a **Design Decision Spec** for the top 3 insights — concrete enough to write a sprint ticket from. Lens insight that doesn't translate to a shippable change is just a feeling. Each row includes all six fields (vague entries rejected):

| Insight | Specific design change | Measurable spec (with numbers) | Owner (role) | Sprint / release | Pass/fail criterion |

For accessibility insights, the measurable spec must reference **WCAG criteria with version** (e.g., WCAG 2.2 AA SC 2.5.5 target size; contrast ratio 4.5:1 per SC 1.4.3) — not generic "make it accessible." If a number cannot be specified yet, name the research deliverable that would produce it, with owner and deadline.

---

## The question that matters most

Buried in Lens 2 is the method's sharpest tool: *"Who's someone I'm nervous to talk to about this?"*

If you can answer that question honestly, you've found the gap in your design process. The nervousness is the signal. It means there's a perspective you've been avoiding — either because you suspect it will complicate your design, or because you genuinely don't know how to reach that person.

Another Lens won't let you skip it.

---

## How to use it with AI

Describe the design decision or product you're working on, including who your primary intended user is. Tell the AI you want to run Another Lens. It will walk you through each lens one question at a time — not all at once. The pacing is deliberate: the space between questions is where reflection actually happens.

You can run a single lens (Lens 2 alone is particularly sharp for a quick check) or all three for a full session.

---

## A quick example

A designer is building a budgeting app for "young professionals." Running Another Lens surfaces:

- **Bias named:** "I assumed users would have a stable monthly income because everyone on my team does. The entire flow is built around salary dates and predictable deposits."
- **Opposite considered:** "If that assumption is wrong, the app doesn't just fail to help gig workers — it actively makes them feel like they're failing at budgeting when the tool just doesn't fit their reality."
- **Person I'm nervous to talk to:** "My cousin who works three part-time jobs and has never used a budgeting app because 'those things aren't for people like me.'"
- **Learning intention:** "I want to understand how people with irregular income actually manage money week-to-week — not through a survey, but through conversation."

**Lens Statement:** *"After applying Another Lens, I'm now questioning whether our budgeting model assumes financial stability as a prerequisite, and I plan to interview three gig-economy workers before the next design review."*

---

## See also

- [Bad Design Canvas](bad-design-canvas.md) — Another Lens helps you see what biases you're bringing; Bad Design Canvas maps the external consequences those biases produce
- [Worrystorming](worrystorming.md) — run Another Lens first to name your lenses, then worrystorm with that self-awareness active
- [CIDER](cider.md) — Another Lens looks at the designer; CIDER looks at the assumptions embedded in the artifact itself
