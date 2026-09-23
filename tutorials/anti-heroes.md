# Anti-Heroes

**The short version:** A card deck that names the manipulative moves a design can make — the Trap-Setter, the Camouflager, the Empathy Manipulator — and pairs each one with the Hero move that undoes it.

---

## Who made it

Anti-Heroes was developed by Shikha Mehta, Shruthi Sai Chivukula, Colin M. Gray, and Ritika Gairola. The work was published as a preprint in 2024 (arXiv:2405.03674) and formally as a full paper in the Proceedings of the 2025 ACM Designing Interactive Systems Conference (DIS 2025). It comes out of ongoing academic work on ethical design methods and designer intentions.

The name is about roles, not people. An Anti-Hero card describes the role a *design* plays when it works against its user — it does not call the designer a bad person. Every Anti-Hero has a Hero: the ethical role that counters it.

---

## The problem it solves

Most teams can feel when a design is off — the cancel flow that loops back to the start, the fee that only appears at checkout, the sad mascot that guilts you into staying. What they lack is a shared, respectful way to say so. "This seems gross" starts an argument; it doesn't change the design.

Anti-Heroes gives the team that vocabulary. "This is a Trap-Setter — once you're in, the off-ramp is hidden" names the specific move, points at the specific screen, and comes with its own fix: "the Empowerer version would put cancel one tap from the account page." The value trade-off becomes visible, so the team can choose differently.

---

## When to use it

- **In a design review** — when something feels manipulative and you want to name the exact move instead of arguing about vibes
- **Before shipping a flow with money, subscriptions, consent, or cancellation in it** — the places where manipulative moves hide most often
- **When a team meeting needs to call out a move without finger-pointing** — cards work like a referee's call: about the play, not the player
- **When shaping a new concept** — use Hero cards as prompts, and stress-test each idea against the Anti-Hero it could slide into under business pressure
- **When reviewing competitors or industry trends** — to name patterns you want to avoid

---

## What it produces

**The deck — nine Anti-Hero ↔ Hero pairs:**

| Anti-Hero | What the design does | Hero | The counter-move |
|---|---|---|---|
| Trap-Setter | Makes a flow the user can't get out of | Empowerer | Symmetric entry and exit, reversible decisions |
| Camouflager | Hides costs or terms in visual or copy noise | Unveiler | Puts costs and terms upfront, as visible as the call to action |
| Empathy Manipulator | Uses guilt, fear or shame to push a choice | Life Coach | Honest information that helps the user act on their own intent |
| Cynic | Treats the user as something to extract from | Liberator | Optimizes for the user's long-term interest |
| Nickeling-and-Diming | Splits the real cost into small fees that appear late | Transparent Pricer | States the all-in price upfront |
| Black Hat | Uses techniques known to deceive — fake timers, disguised ads | White Hat | Persuades only toward the user's own goals, openly |
| Two-Faced | Promises one thing in marketing, does another in defaults | Consistent Communicator | Keeps message, defaults and behavior aligned |
| Puppeteer | Steers through hidden defaults or opaque algorithms | Liberator | Makes the steering visible and overridable |
| Adversary | Adds friction exactly where the user's interest diverges from the company's | Ally | Adds friction only where it protects the user |

**Four ways to use it**, all sharing the same cards:

1. **Evaluation** — critique an existing design: tag each suspicious element with an Anti-Hero card, cite the exact screen or copy line, and name the Hero move that flips it
2. **Reverse brainstorming** — design the worst possible version on purpose with 2–4 cards, then turn each worst move into a Hero move and a guardrail
3. **Conceptualization** — use Hero cards as creative prompts for a new concept, then make the Anti-Hero slide hard or impossible
4. **Ethical dialogue** — candidate cards and ready-to-say scripts for a meeting ("I want to call a Trap-Setter on this — can we look at the cancel flow together?")

Every run also marks **necessary friction** — fraud checks, legal warnings, confirmations before irreversible actions — so the team doesn't strip safety in the rewrite.

---

## The key insight

Every Anti-Hero comes with its fix. The method doesn't stop at "this is manipulative"; the paired Hero card says what the non-manipulative version does. That pairing is what turns critique into a design change.

The shared deck matters too. A card name only works as a team vocabulary if everyone means the same card — which is why the method uses the deck's names, not new ones invented on the spot.

---

## How to use it with AI

Describe or paste the design — a flow, a screenshot description, the copy — along with what the user is trying to do and the business pressure behind it. Say which mode you want, or let the AI infer it. The AI will pick the 2–5 cards that actually fit, cite the specific moment that triggers each, pair every Anti-Hero with a concrete Hero move, and flag any friction that should stay.

---

## A quick example

**Design:** A meditation app's subscription cancel flow. "Cancel" lives under Settings → Account → Manage plan. Tapping it shows a sad mascot and "Are you sure you want to abandon your calm?", then offers a 50% discount, then asks for a reason, then confirms.

**Anti-Heroes found:**

- **Trap-Setter** — four screens to leave, one tap to join. → **Empowerer:** cancel is one tap from the account page, with the discount offered once, beside it, not in front of it.
- **Empathy Manipulator** — "abandon your calm" and the sad mascot turn leaving into a personal failure. → **Life Coach:** "Your subscription ends on 12 May. Your saved sessions stay available to download."

**Necessary friction:** a final confirmation before cancelling is fine — cancelling is a real decision. Keep it, just make it one screen.

---

## See also

- [Fair Patterns](fair-patterns.md) — names the same moves as dark-pattern types, with the statutes they break; Anti-Heroes gives the team the words to raise them
- [DAH Cards](dah-cards.md) — another card-based critique, organized by harm category rather than designer role
- [Humane Design Guide](humane-design-guide.md) — goes deeper on the psychological mechanisms an Empathy Manipulator exploits
