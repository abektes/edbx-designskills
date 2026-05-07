# Motivation Matrix

**The short version:** A grid that maps the five core human drives your product is activating — across different types of users and contexts — and surfaces where it's doing that ethically versus where it's crossing into manipulation.

---

## Who made it

The Motivation Matrix was developed by **Annabelle Zhu** and adapted for ethical design auditing by **Cordelia Nodders**, published in *Universal Methods of Ethical Design*. It draws on established motivational psychology research — achievement theory, social comparison theory, and behavioral economics — synthesized into a design-auditable format.

The matrix format was specifically designed to make motivation analysis accessible to design teams who don't have a psychology background.

---

## The problem it solves

All products activate human motivations. That's how they get used. The question is: which motivations, for which users, in what contexts — and is that ethical?

The problem is that motivation design happens constantly but is rarely examined explicitly. A designer adds a progress bar (achievement motivation), a follower count (social motivation), a countdown timer (fear of loss), a leaderboard (power/status motivation), a referral bonus (incentive motivation) — and none of these decisions are scrutinized for their ethical implications. Each seems reasonable in isolation. Together they may be creating something manipulative.

The Motivation Matrix makes the full picture visible. By mapping all five motivation types across multiple user contexts in a single table, it reveals patterns that would be invisible if you looked at each feature separately.

---

## When to use it

- **When you're auditing a product for manipulative behavioral design** — the matrix gives you a structured way to examine every motivational lever
- **When you suspect you're using fear or social pressure more than you realized** — the matrix makes it visible
- **When designing for multiple user types** — the matrix shows how the same feature affects different users very differently
- **When someone asks "are we manipulating users?"** — this method gives you a structured, honest answer
- **For any product with gamification, social features, or engagement mechanics** — these are highest-risk for motivational exploitation

---

## What it produces

The matrix has five rows (motivation types) and multiple columns (user contexts you define). Every cell gets a **[Motivation] + [Action] statement** — a specific description of what the design is doing to that user's motivation in that situation.

**The five motivation types:**
- **Achievement** — progress, mastery, completion (progress bars, badges, streaks, levels)
- **Social Acceptance** — belonging, approval, status (likes, follower counts, social proof, FOMO)
- **Fear** — avoiding loss, missing out, being left behind (warnings, countdowns, loss aversion framing)
- **Power** — control, influence, dominance (leaderboards, admin roles, exclusive access)
- **Incentive** — extrinsic reward, gain (discounts, points, cashback, referral bonuses)

Each cell is rated:
- 🟢 **Ethical** — motivation aligned with user goals; user can opt out without penalty
- 🟡 **Monitor** — potential for harm depending on context, vulnerability, or scale
- 🔴 **Manipulative** — design exploits motivation to drive behavior that primarily benefits the system, not the user; user cannot easily opt out or notice the manipulation

The output includes an **Ethical Risk Summary** (3–5 bullets on the most significant risks), **Redesign Directions** (concrete changes, not just "be less manipulative"), and a **Missing Contexts** section naming user groups not included in the analysis who should be.

---

## Why context columns matter

The same feature can be ethical for one user and manipulative for another. A "you're 80% to your goal!" progress bar is motivating for someone who freely chose that goal. For someone who was nudged into a default target, it's manufacturing pressure toward something they didn't choose.

By defining at least two or three different user contexts — "engaged user in ideal conditions," "stressed user in a difficult week," "new user who doesn't yet understand the system" — the matrix forces the team to see beyond the optimal case.

---

## How to use it with AI

Describe the product or feature and the user contexts you want to map. The AI will construct the full matrix — all five motivation types, all your defined contexts — with specific [Motivation] + [Action] statements in every cell, ethical flags, risk summary, and redesign directions. If you're not sure what contexts to use, the AI will suggest appropriate ones based on your product.

---

## A quick example

**Product:** A fitness app with daily workout goals, streaks, and a friend activity feed.

**Selected cells:**

| | New user (week 1) | Experienced user (month 6) | User in injury recovery |
|---|---|---|---|
| **Achievement** | 🟢 "Progress bar to first 7-day streak motivates completion of onboarding" | 🟡 "Streak counter incentivizes exercise through streak preservation, not health goals" | 🔴 "Streak counter creates pressure to exercise during recovery, risking re-injury" |
| **Fear** | 🟡 "Notification: 'Don't break your streak!' creates mild urgency" | 🟡 "Loss aversion around streak increases — missing one day feels high-stakes" | 🔴 "Streak loss framing converts rest (medically indicated) into failure" |
| **Social Acceptance** | 🟢 "Friend activity feed shows others working out — social proof for adoption" | 🟡 "Comparison to friends with longer streaks may create inadequacy" | 🔴 "Friend activity feed during recovery makes the user feel left behind and broken" |

**Key finding:** The product was designed for healthy, engaged users. For users in injury recovery — a predictable population for a fitness app — three out of five motivation types are actively harmful. The design has no mechanism to shift mode for this user group.

**Redesign direction:** Add a "recovery mode" that pauses streak tracking, changes the friend feed to supportive content, and shifts achievement framing from consistency to healing milestones.

---

## See also

- [Inverted Behavior Model](inverted-behavior-model.md) — maps behaviors that result from motivational activation; Motivation Matrix maps the motivational activation itself
- [Humane Design Guide](humane-design-guide.md) — maps human sensitivities being exploited; Motivation Matrix maps the motivational mechanisms doing the exploiting
- [Worrystorming](worrystorming.md) — surfaces fears users hold; Motivation Matrix shows how those fears are activated (or exploited) by the design
