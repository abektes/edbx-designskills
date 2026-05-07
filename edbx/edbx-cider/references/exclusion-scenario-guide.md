# CIDER — Exclusion Scenario Guide

This reference helps designers write vivid, specific exclusion scenarios for Stage I (and Stage R) of CIDER.

---

## What Makes a Good Exclusion Scenario

An exclusion scenario is a short narrative that shows a specific person failing, struggling, or being humiliated because of an assumption the design makes. It is not a generalization, a statistic, or a category label. It is a story about one person in one moment.

Good scenarios have four qualities:

1. **Specific person** — A named individual with concrete characteristics
2. **Concrete setting** — A particular place, time, and circumstance
3. **Observable failure** — A task that goes wrong in a describable way
4. **Emotional texture** — What the experience feels like, not just what happens

---

## The Difference Between Generic and Specific

### Generic (avoid)

> "A visually impaired user might have difficulty with the color-coded status indicators."

Why this fails: No person. No setting. No moment. No feeling. The designer can nod at this and move on without actually imagining exclusion.

### Specific (aim for this)

> "Fatima, who has low vision from diabetic retinopathy, is checking her lab results on the patient portal during her lunch break at the hospital cafeteria. The results page uses green, yellow, and red dots to indicate normal, borderline, and critical values. Fatima cannot distinguish the yellow from the green dots. She knows one of her values is borderline but cannot tell which one. She zooms in on her phone, but the dots are only 8px and blur further at high magnification. She screenshots the page and texts it to her daughter, asking her to read the colors. Her daughter is in class and does not respond for 45 minutes. Fatima spends her entire lunch break not knowing whether her kidney function is declining."

Why this works: Named person. Specific condition. Concrete setting. Observable task failure. Emotional stakes. The designer reading this cannot help but imagine the experience.

---

## Building a Scenario: Step by Step

### Step 1: Name the Person

Choose a name and give them a brief identity. Include age, relevant condition or circumstance, and one contextual detail.

Examples:
- "Tomás, a 34-year-old construction worker with a hand injury..."
- "Priya, a 72-year-old grandmother visiting from India..."
- "Marcus, a 16-year-old student whose phone screen is cracked..."
- "Ingrid, a social worker doing home visits in rural Minnesota..."

Avoid stereotypes. Give the person dignity and specificity. They are not a symbol of their condition — they are a person with a life.

### Step 2: Place Them in Context

Where are they? What time of day? What else is happening around them? Context determines whether an assumption becomes exclusion.

- "on a crowded bus during rush hour"
- "at the kitchen counter while her toddler is crying"
- "standing at a self-checkout kiosk with a line of six people behind her"
- "in a hospital bed, groggy from medication, using a borrowed tablet"

### Step 3: Describe the Task

What are they trying to accomplish? Be specific about the goal, not just the interface.

- "trying to book an appointment for next Tuesday morning"
- "trying to find out if her test results are normal"
- "trying to complete the required safety training before her shift starts"
- "trying to submit a reimbursement form before the deadline"

### Step 4: Show the Failure

What goes wrong? Trace the interaction step by step until the person hits the wall created by the assumption.

- "She taps the dropdown but it opens a scrollable list of 200 items that she cannot search."
- "The form requires her to type a confirmation code, but the email takes 12 minutes to arrive and the code expires in 10."
- "The video autoplays with sound. She is in a library. She fumbles for the mute button but it is not visible until the video is fully loaded."
- "He selects the correct option three times but each time the form resets because he is inadvertently touching the edge of the screen with his palm."

### Step 5: Name the Feeling

What does the person experience emotionally? This is what turns a technical failure into a human one.

- "She feels embarrassed — the person behind her in line is sighing."
- "He closes the app and decides to skip the appointment. He will try again next week, or maybe not."
- "She wonders if this is deliberate — if the system is designed to make people give up."
- "He asks his 9-year-old son to help him, which makes him feel like he cannot manage his own life."

---

## Common Pitfalls

### Pitfall 1: The Demo User

Avoid scenarios that feel like accessibility demo scripts — a screen reader user navigating a form, a wheelchair user approaching a ramp. These are real scenarios, but they are also the ones every accessibility training uses. CIDER is about finding assumptions you did not already know about. Push past the obvious.

### Pitfall 2: The Statistical User

"A study found that 15% of users..." is not a scenario. It is evidence. Scenarios are about one person, not populations.

### Pitfall 3: The Solvable User

Avoid writing scenarios where the fix is obvious and trivial. If the scenario makes the designer say "just add alt text," it is too shallow. The best scenarios reveal exclusion that requires genuine redesign.

### Pitfall 4: The Pitying Gaze

Write scenarios with respect. The person in the scenario is not a victim to be pitied — they are a person encountering a design that was not built for them. The failure belongs to the design, not to the person.

---

## Scenario Length

Aim for 100–200 words. Long enough to be vivid, short enough to be readable in a workshop setting. If you find yourself writing 400 words, you are writing a case study, not a scenario — tighten it to the essential moment.

---

## Using Scenarios in Team Sessions

In team CIDER sessions, have each participant read their scenario aloud (or display it for everyone to read silently for 60 seconds). Then ask:

- "Who has encountered something similar?"
- "What did you feel hearing this?"
- "What would have to change for this person to succeed?"

The discussion after scenario sharing is often the most productive part of a CIDER session. Do not rush it.
