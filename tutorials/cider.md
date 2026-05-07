# CIDER

**The short version:** CIDER is a structured method for finding the assumptions baked into your design that exclude people — often without the team ever realizing it.

---

## Who made it

CIDER was developed by **Cynthia Bennett, Cole Gleason, Hailey L. Johnson, Franchesca Lameiro, Meredith Ringel Morris, and colleagues** at Microsoft Research and Carnegie Mellon University, published in 2022. The lead researchers include Katta Spiel and others working at the intersection of HCI, disability studies, and inclusive design.

The name is an acronym: **Critique → Imagine → Design → Expand → Repeat**

---

## The problem it solves

Every design embeds assumptions about who the user is. What device they're using. What physical abilities they have. What language they speak. What cultural context they come from. What resources they can access. What emotional state they're in.

Most of the time, these assumptions are invisible. They feel like "common sense" because they match the lived experience of the design team. The result is products that work perfectly for some people and barely work — or actively fail — for others.

CIDER doesn't just ask "is this accessible?" It asks: *what does this design assume to be true about the person using it, and what happens when that assumption is wrong?*

---

## When to use it

- **During any design review** — CIDER can be applied to any artifact at any stage
- **When your team says "this works for most users"** — "most" is the word to interrogate
- **When accessibility concerns have been raised but not addressed** — CIDER goes deeper than a checklist
- **When you're designing for a context different from your team's** — different culture, language, ability, or economic situation
- **When you want to do genuine inclusive design work** — not as a compliance exercise, but as a design practice
- **Whenever the phrase "the average user" appears in your documentation** — there is no average user

---

## What it produces

CIDER works through five stages in a loop:

1. **Critique** — examine the design for embedded assumptions. What does this interface assume about the user's ability, context, language, device, or prior knowledge? Name the assumptions explicitly.

2. **Imagine** — for each assumption, imagine a user for whom it is false. Not a hypothetical edge case, but a real person with a real context. Someone who is blind. Someone who is managing a crisis. Someone whose first language is not the language the interface is in. Someone who cannot afford a data plan.

3. **Design** — generate a design variation that works for that imagined user. This is generative, not just critical — the goal is to find what the design would need to change, not just to identify that it needs to change.

4. **Expand** — look at the new design variation and ask: does this help anyone else? Inclusive design often produces better design for everyone. A larger tap target helps people with motor impairments and also helps people in a hurry.

5. **Repeat** — go back to step one with the new design and find the next assumption. The loop continues because assumptions are layered.

The output is a **map of embedded assumptions**, a set of **design variations** that address them, and an analysis of **how those variations expand benefit** beyond the originally excluded group.

---

## The key insight

CIDER is built on the insight that exclusion is usually not intentional — it's structural. Teams don't decide to exclude people. They decide to optimize for a user who looks like their existing user base (or like themselves), and exclusion is the side effect.

The method makes that structural exclusion visible and addressable. It doesn't ask the team to feel bad about it; it asks them to fix it.

---

## How to use it with AI

Describe your product or a specific design artifact — a screen, a flow, a feature, an interface pattern. Tell the AI you want to run CIDER. It will work through the five stages, naming the assumptions in your design, imagining specific excluded users, generating design alternatives, and expanding those alternatives to show their broader benefit.

---

## A quick example

**Design artifact:** A signup form that requires a phone number for two-factor authentication.

**Critique:** This assumes the user has a personal mobile phone with a working number, that they're comfortable sharing it, that they have cellular coverage, and that the number is stable.

**Imagine:** A user at a domestic violence shelter who cannot use their real phone number (safety risk). A user without a smartphone who relies on a library computer. A user in a country where prepaid SIM cards change frequently.

**Design variation:** Add alternative 2FA methods — authenticator app, email, or a backup code system. Make phone number optional rather than required.

**Expand:** These changes help travelers with temporary SIM cards, people switching phones, anyone who prefers not to share a phone number with services, and users in contexts where phones are shared within households.

**Repeat:** The email 2FA alternative now assumes the user has a personal email address. Loop back...

---

## See also

- [Another Lens](anotherlens.md) — CIDER examines the artifact for assumptions; Another Lens examines the designer who made them
- [Anti-Heroes](anti-heroes.md) — CIDER surfaces who is excluded; Anti-Heroes maps what harm that exclusion causes
- [Humane Design Guide](humane-design-guide.md) — covers overlapping territory from a different angle; Humane Design Guide focuses on psychological harm, CIDER focuses on structural exclusion
