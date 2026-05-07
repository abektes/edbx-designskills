# Ethical Flags — How to Identify Manipulative vs. Ethical Patterns

Use this reference when assigning flags to matrix cells. Each flag represents a judgment about the relationship between the design element and the user's agency.

---

## Flag Definitions

### 🟢 Ethical

The design supports the user's own goals transparently. The user can understand, control, and opt out of the motivational mechanism without penalty.

**Criteria (all must apply):**
- The user chose to engage with this motivational mechanism, or it is easy to understand and dismiss.
- The motivation aligns with the user's stated or reasonably inferred goals.
- The user can opt out without losing core product value.
- The mechanism is honest — it does not misrepresent urgency, scarcity, social proof, or consequences.
- The user is not penalized (explicitly or implicitly) for ignoring the motivational cue.

**Example:** A habit tracker that displays a streak but lets the user pause it, reset it, or hide it without losing any functionality.

---

### 🟡 Monitor

The design has the potential to cause harm depending on context, user vulnerability, or scale. It is not clearly manipulative, but it deserves scrutiny.

**Criteria (any one is sufficient to trigger a yellow flag):**
- The motivational mechanism is borderline persuasive — it nudges behavior in a direction the user might not have chosen autonomously.
- Harm is contextual: it depends on who the user is (age, vulnerability, cultural context) or what situation they are in (stressed, distracted, time-pressured).
- The opt-out exists but is hard to find, requires effort, or comes with a social penalty.
- The motivation is transparent to some users but not to others (e.g., sophisticated users understand the game; new users do not).
- The design uses real data but frames it in a way that amplifies emotional response beyond what the data warrants.
- Scale changes the ethics: acceptable for 100 users, potentially harmful for 10 million.

**Example:** A fitness app that shows a leaderboard. For motivated, informed users this is competition they chose. For new users who do not know how to hide it, it creates anxiety about being at the bottom.

**What to do with 🟡 flags:**
- Document the condition under which the pattern becomes harmful.
- Identify who is most vulnerable.
- Propose a design change that addresses the vulnerability without removing the feature for users who benefit.

---

### 🔴 Manipulative

The design exploits a motivation to drive behavior that primarily benefits the system, not the user. The user cannot easily opt out, notice the manipulation, or make a free choice.

**Criteria (any one is sufficient to trigger a red flag):**
- The design creates a problem (anxiety, fear, social pressure) and then offers the product as the solution.
- The user cannot opt out without significant penalty — loss of data, loss of social connections, loss of investment (sunk cost).
- The motivational mechanism is hidden or disguised. The user does not realize they are being influenced.
- The design uses deception: fake scarcity, artificial urgency, manufactured social proof.
- The primary beneficiary of the behavior change is the platform, not the user. The user's actual goals are secondary.
- The mechanism targets a known vulnerability (addiction, anxiety, loneliness, financial insecurity) and exploits it.

**Example:** A social platform that sends notifications like "3 people are looking at your profile right now!" when no one is actually looking at the profile. The notification exploits social anxiety to drive engagement.

**What to do with 🔴 flags:**
- Treat as a design defect, not a feature to optimize.
- Propose a specific redesign that removes the manipulation while preserving the underlying user need (if there is one).
- If the manipulation is structural (tied to the business model), name that explicitly. A redesign that does not address the incentive is cosmetic.

---

## Common Patterns by Motivation Type

| Motivation | Common 🟡 pattern | Common 🔴 pattern |
|---|---|---|
| Achievement | Streaks that cannot be paused | Endless levels with no completion state |
| Social Acceptance | Activity made public by default | Fake social proof or inflated engagement signals |
| Fear | Real deadlines with excessive visual urgency | Manufactured urgency (countdowns that reset) |
| Power | Public rankings with no opt-out | Pay-to-win mechanics that exploit status anxiety |
| Incentive | Complex loyalty programs with unclear value | Hidden auto-subscription buried in "free" offers |

---

## Decision Heuristic

When unsure how to flag a cell, ask these three questions in order:

1. **Who benefits most from this behavior change?** If the answer is "the platform," lean toward 🔴.
2. **Can the user understand what is happening and choose differently?** If the answer is "no, not easily," lean toward 🔴.
3. **Would the design team be comfortable explaining this mechanism publicly to the affected users?** If the answer is "no," it is at least 🟡.

If all three answers are favorable, the cell is 🟢.

---

## Tone Note

Flagging a cell is not a moral judgment on the designers. Products accumulate manipulative patterns incrementally — no single decision creates them. The purpose of flagging is to create visibility, not blame. Use flags to start conversations, not end them.
