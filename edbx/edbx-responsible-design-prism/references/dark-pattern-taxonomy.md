# Dark Pattern Taxonomy

Reference for the Responsible Design Prism. Use precise pattern names when scoring axes.

Source: adapted from darkpatterns.org / deceptive.design taxonomy and academic literature.

---

## Deception Patterns

Patterns that hide, obscure, or falsify information.

### Bait and Switch
The user sets out to do one thing, but a different, undesirable thing happens instead. The design leads the user to expect outcome A but delivers outcome B.

### Disguised Ads
Advertisements or sponsored content that looks like neutral content, navigation, or functionality. The user cannot distinguish commercial intent from organic content.

### Hidden Costs
Extra charges, fees, or conditions that are not revealed until the user has already invested significant effort in the flow. Shipping costs added at checkout are the classic example.

### Hidden Subscription
A one-time purchase that quietly enrolls the user in a recurring subscription. The recurrence is buried in terms, fine print, or an unchecked box.

### Misleading Pricing
Prices displayed in a way that makes comparison or true cost assessment difficult — per-unit pricing that doesn't add up, crossed-out fake original prices, or "up to X% off" where the maximum discount barely exists.

### False Expectations
Visual design, copy, or layout that creates an expectation the product does not fulfill. Stock photos showing features that don't exist, or pricing that implies scope the product doesn't cover.

---

## Coercion Patterns

Patterns that make it hard to say no or easy to say yes unintentionally.

### Forced Continuity
A free trial that automatically converts to a paid subscription without explicit consent or adequate reminder. The signup is easy; the cancellation is hard.

### Roach Motel
Easy to get into a situation (sign up, subscribe, start a trial) but hard to get out. Cancellation requires phone calls, hidden pages, or navigating complex flows.

### Confirmshaming
The opt-out button is written to induce guilt or shame. "No thanks, I don't want to save money" or "No, I prefer to stay uninformed." The language implies the user is making a bad decision.

### Trick Questions
Questions worded in confusing double-negatives or unexpected logic so that the user answers against their own interest. "Don't not uncheck if you don't want to not receive updates."

### Preselection / Default Manipulation
Defaults set to maximize business value rather than user preference. Opt-in checkboxes pre-checked, extra items added to cart by default, sharing settings defaulted to public.

---

## Exploitation Patterns

Patterns that take advantage of user vulnerability, error, or cognitive limitation.

### Sneak into Basket
Adding an extra item to the shopping cart or selection without the user's explicit action. Often combined with preselection defaults.

### Urgency Fakery
False countdown timers, limited stock warnings, or "only 2 left!" messages that reset or are not genuine. Creates artificial time pressure to prevent deliberate decision-making.

### Social Proof Fakery
Fabricated or misleading social proof — "10,000 people bought this today," fake testimonials, or notification toasts for activities that didn't happen.

### Scarcity Fakery
Artificial scarcity signals — "only 1 room left!" or "selling fast" — that do not reflect actual inventory or demand.

### Exploiting Error
Taking advantage of user mistakes rather than preventing or correcting them. An accidentally selected expensive shipping option that isn't confirmed. A typo in an email address used to prevent cancellation.

---

## Manipulation Patterns

Patterns that shape user behavior without the user's awareness or consent.

### Obstruction (Hard-to-Compare)
Making it difficult to compare options by using inconsistent units, visual clutter, or buried information. Preventing informed choice.

### Visual Interference
Using color, weight, size, or animation to draw attention to the business-preferred option and away from the user-preferred option. The expensive plan is a bright button; the free option is a text link.

### Attention Capture
Design that deliberately captures and holds attention beyond what the user intended — infinite scroll, auto-play, or notifications designed to trigger re-engagement.

### Emotional Manipulation
Copy or design that exploits fear, anxiety, FOMO, or insecurity to drive action. "Your account is at risk," "Don't miss out," or shame-based messaging.

### Gamification Exploitation
Using gamification mechanics (streaks, points, badges) not to enhance genuine engagement but to create compulsive behavior patterns.

---

## Obstruction Patterns

Patterns that physically or cognitively block the user from their intended action.

### Hard-to-Cancel
Cancellation flows that require multiple steps, hidden pages, or contact with support. Often combined with retention offers that appear after the user has already decided to cancel.

### Hard-to-Delete
Account or data deletion that is more complex than account creation. Requires sending emails, waiting periods, or navigating dark pattern-filled retention flows.

### Intermediate Currency
Using virtual currency, credits, or tokens instead of real money to obscure the true cost of purchases and make spending feel less real.

### Immense Overload
Presenting terms, conditions, or privacy policies as massive walls of text that no user will read, burying important clauses in volume.

---

## How to Use This Taxonomy in the Prism

1. When scoring the **Information** axis, look for Deception patterns.
2. When scoring the **User relationship** axis, look for Exploitation and Manipulation patterns.
3. When scoring the **Error handling** axis, look for Exploiting Error and Coercion patterns.
4. When scoring the **Business alignment** axis, look for Coercion and Obstruction patterns.
5. When scoring the **Usability** axis, look for Obstruction and Visual Interference patterns.

When you identify a pattern, name it precisely in the evidence column of the Prism Audit Table. "Uses confirmshaming in the opt-out button (Coercion)" is more actionable than "feels pushy."
