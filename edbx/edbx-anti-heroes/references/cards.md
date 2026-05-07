# Anti-Heroes Card Deck

This is the working deck used by the Anti-Heroes method. Each row pairs an **Anti-Hero** card (a manipulative designer role) with the **Hero** card that counters it (an ethical role). When you tag a design with an Anti-Hero, propose the paired Hero as the move that flips it.

The deck below is drawn from Mehta, Chivukula, Gray, et al. (2024), *Anti-heroes: an ethics-focused method for responsible designer intentions*, arXiv:2405.03674, and from the *Universal Methods of Ethical Design* method profile that depicts the deck in use. Some Anti-Hero cards in the source appear without an explicitly named Hero pair; in those cases the Hero column gives the counter-move that the source's framing implies.

## How to read this deck

- **Anti-Hero** describes the designer's role when the move is present. It does not call the human designer a bad person — it names the value-deprioritizing move embedded in the design.
- **What it does** is the manipulative behavior the user experiences.
- **Hero** is the paired ethical role.
- **What it does** for the Hero is the counter-move that restores user agency.

When critiquing, cite the specific UI element, copy line, default, or interaction that triggers the tag. Cards without cites are labels, not critique.

## The pairs

### Trap-Setter ↔ Empowerer

- **Trap-Setter:** Designs a user task flow such that the user "can't get out of it," setting a trap that enables the stakeholder's goal. Hidden cancel paths, loops back to the start, dead-end "back" buttons.
- **Empowerer:** Designs paths that enable users to make their own decisions in a task flow. Symmetric entry and exit, clear off-ramps, decisions reversible without penalty.

### Camouflager ↔ Unveiler

- **Camouflager:** Hides costs, terms, or consequences inside visual or copy noise — fine print, color-matched disclaimers, important info on a separate screen.
- **Unveiler:** Surfaces costs, terms, and consequences upfront, in the same visual weight as the call to action.

### Empathy Manipulator ↔ Life Coach

- **Empathy Manipulator:** Weaponizes the user's emotions — guilt, fear, loss aversion, social shame — to push a stakeholder-favored choice. Sad mascots, "are you sure you want to abandon your goals?" copy, streak-loss warnings.
- **Life Coach:** Gives the user honest, non-coercive information that helps them act on their own intent, including when that means leaving.

### Cynic ↔ Liberator

- **Cynic:** Treats the user as a target to be extracted from. Optimizes for short-term stakeholder metrics at the expense of trust.
- **Liberator:** Treats the user as the principal. Optimizes for the user's long-term interest even when it conflicts with short-term funnel metrics.

### Nickeling-and-Diming ↔ Transparent Pricer

- **Nickeling-and-Diming:** Splits the real cost across many small fees, surcharges, "optional" defaults, or upsell gates that appear after commitment. Users feel surprised at checkout.
- **Transparent Pricer:** States the all-in price the user will actually pay, upfront, in the same place as the offer.

### Black Hat ↔ White Hat

- **Black Hat:** Uses techniques the designer knows to be deceptive — confirmshaming, disguised ads, misdirection, urgency timers that aren't real.
- **White Hat:** Uses persuasion techniques only when they align with the user's stated goals, and discloses them honestly.

### Two-Faced ↔ Consistent Communicator

- **Two-Faced:** Says one thing in marketing, onboarding, or first-run, and behaves differently in defaults, settings, or post-signup flows. Privacy promises that contradict default toggles, trial terms that contradict in-product copy.
- **Consistent Communicator:** Keeps the message, defaults, and behavior aligned across surfaces.

### Puppeteer ↔ Liberator

- **Puppeteer:** Steers user behavior through hidden defaults, opaque algorithms, or constrained choice architectures the user cannot see or override.
- **Liberator:** Makes the steering visible, gives the user override controls, and explains what the system is doing on their behalf.

### Adversary ↔ Ally

- **Adversary:** Treats the user as an obstacle to a business outcome — adds friction precisely where the user's interest diverges from the company's.
- **Ally:** Treats the user as the customer of the design and adds friction only where it protects the user (fraud checks, irreversible actions, safety pauses).

## Cards without explicit pairs in the source

Some cards appear in the broader deck without a clearly named Hero counterpart in every printing. Use the closest Hero from above when tagging:

- **Cynic** → pair with Liberator or Life Coach depending on whether the move is structural or emotional.
- **Black Hat** → pair with White Hat (above) or Unveiler if the manipulation is informational.
- **Puppeteer** → pair with Liberator or Empowerer.

## Practical notes

- The deck is generative, not exhaustive. If a move in a real design clearly fits an Anti-Hero pattern but matches none of the named cards exactly, name the closest card and add a one-line description of the variant rather than inventing a brand-new card on the fly.
- A single design move can match more than one Anti-Hero card. That is OK — pick the card whose Hero counterpart most directly suggests the fix.
- Some patterns that look manipulative are actually required (legal warnings, fraud checks, irreversible-action confirms, age gates). Mark these as **necessary friction** rather than tagging them with an Anti-Hero card; otherwise the team will strip safety in the rewrite.

## Source

Mehta, S., Chivukula, S. S., Gray, C. M., et al. (2024). *Anti-heroes: an ethics-focused method for responsible designer intentions*. arXiv:2405.03674.

Further reading:
- Gray, C. M., Chivukula, S. S., & Lee, A. (2020). What kind of work do "asshole designers" create? Describing properties of ethical concerns on Reddit. *Proceedings of the 2020 ACM Designing Interactive Systems Conference*, 61–73.
- Gray, C. M., Chivukula, S. S., Melkey, K., & Manocha, R. (2021). Understanding "dark" design roles in computing education. *Proceedings of the ACM Conference on International Computing Education Research*, 225–238.
