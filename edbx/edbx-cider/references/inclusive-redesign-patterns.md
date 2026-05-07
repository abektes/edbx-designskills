# CIDER — Inclusive Redesign Patterns

Common redesign patterns organized by assumption category. Use these as prompts and inspiration during Stage D — not as a prescriptive checklist.

---

## Ability Redesign Patterns

### Multi-Modal Output
Provide information through more than one sensory channel simultaneously.
- Text alternatives for visual indicators
- Visual indicators alongside audio signals
- Haptic feedback for state changes
- Captions and transcripts for audio and video content

### Adjustable Interaction
Let users choose how they interact — do not prescribe a single input method.
- Keyboard alternatives for every mouse/touch interaction
- Voice input as an alternative to typed input
- Switch access for users who cannot use a keyboard or touch screen
- Dwell-click and eye-tracking support

### Tolerance for Imprecision
Design for imprecise input, not just perfect gestures.
- Large touch targets (minimum 44px)
- Generous timing — no auto-advancing without user initiation
- Undo and confirmation for irreversible actions
- Forgiving input parsing ("did you mean...?")

### Progressive Disclosure
Reduce cognitive and perceptual load by revealing information incrementally.
- Show one step at a time in multi-step processes
- Hide advanced options behind a progressive disclosure control
- Provide summaries before details
- Let users control the pace of information delivery

---

## Capacity Redesign Patterns

### Embedded Guidance
Build the knowledge the user needs directly into the interface.
- Inline explanations instead of separate help documentation
- Contextual tooltips that appear when a field is focused
- Plain-language labels instead of technical jargon
- Worked examples showing what a correct input looks like

### Reduced Working Memory Load
Do not force users to hold information in their head.
- Show previously entered information on confirmation screens
- Auto-populate fields where data is already known
- Provide checklists for multi-step processes
- Save progress automatically and allow resumption

### Language and Literacy Accommodation
Design for varying language proficiency and literacy levels.
- Support for multiple languages, not just English
- Plain language at or below 8th-grade reading level
- Icons paired with text labels, not icons alone
- Pictographic instructions for critical tasks

### Time Flexibility
Do not assume users have unlimited or uninterrupted time.
- No time limits on tasks, or generous time limits with easy extension
- Save-and-resume functionality for any multi-step process
- Progress indicators showing how much remains
- Allow users to skip optional steps and return later

---

## Environment Redesign Patterns

### Offline and Low-Connectivity Support
Design for intermittent or absent connectivity.
- Cache data locally and sync when connectivity returns
- Provide core functionality without requiring a network connection
- Use progressive loading that works on slow connections
- Offer SMS or USSD alternatives for critical functions

### Ambient Condition Adaptation
Design for varied lighting, noise, and physical conditions.
- High-contrast mode for bright environments (outdoors)
- Dark mode for low-light environments
- Subtitle and caption options for noisy environments
- Audio alternatives for environments where reading is difficult

### Device Flexibility
Do not assume a specific device or screen size.
- Responsive layouts that work from 320px to 4K
- Functional on older devices and operating systems
- Alternative access paths (phone, SMS, in-person) for critical services
- Print-friendly formats for tasks that can be completed on paper

### Social Context Sensitivity
Design for use in public, shared, or supervised settings.
- Privacy screens that hide sensitive information from onlookers
- Silent mode that provides full functionality without audio
- Discreet design options for services that carry stigma
- Quick-exit buttons for safety-sensitive contexts

---

## Resources Redesign Patterns

### Cost Reduction
Reduce or eliminate financial barriers to use.
- Free tiers or waived fees for essential services
- No requirement for expensive hardware or software
- Browser-based alternatives to installed applications
- Community access points for hardware-requiring services

### Alternative Identity and Verification
Do not assume specific forms of identification or documentation.
- Multiple verification options (email, phone, in-person, social proof)
- No requirement for government-issued ID where not legally necessary
- Accommodation for users without fixed addresses
- Support for shared or borrowed devices

### Social Support Integration
Design for users who rely on others for access.
- Proxy access: allow a trusted person to act on the user's behalf
- Shared accounts or family/group access models
- Assisted digital pathways with human support
- Clear delegation and permission systems

### Institutional Flexibility
Do not assume institutional backing or affiliation.
- Do not require institutional email addresses for public services
- Accept multiple forms of proof of eligibility
- Provide walk-in alternatives for people who cannot navigate digital systems
- Partner with community organizations for outreach and support

---

## Cross-Category Patterns

Some redesign patterns address assumptions across multiple categories simultaneously.

### Universal Design
Design for the widest possible range of users from the start, not as an afterthought.
- Curb cuts benefit wheelchair users, delivery workers, parents with strollers, and cyclists
- Captions benefit deaf users, non-native speakers, people in noisy rooms, and people who process text better than audio
- Plain language benefits non-native speakers, people under stress, people with low literacy, and everyone in a hurry

### Choice and Customization
Let users adapt the design to their own situation.
- User-adjustable font sizes, contrast levels, and animation preferences
- Choice of input method (type, speak, tap, point)
- Choice of output format (text, audio, visual)
- Preference persistence across sessions

### Redundant Pathways
Provide multiple ways to accomplish the same goal.
- Web, phone, in-person, and mail access for government services
- Search, browse, and ask-a-human pathways for information
- App, SMS, and email channels for notifications
- Self-service and assisted-service options

### Graceful Degradation
Ensure core functionality survives the loss of any single capability.
- Works without JavaScript (or provides fallback)
- Works without images (or provides text alternatives)
- Works without audio (or provides visual alternatives)
- Works without a mouse (or provides keyboard alternatives)

---

## How to Use These Patterns in Stage D

During Stage D brainstorming, use these patterns as prompts when ideas stall:

1. Identify which category the assumption falls into
2. Scan the relevant patterns above
3. For each pattern, ask: "How would this pattern apply to this specific design?"
4. Generate at least one concrete proposal per pattern that fits

Remember: these are patterns, not prescriptions. The best redesigns are specific to the design, the assumption, and the exclusion scenario — not generic applications of a pattern. Use the patterns to spark ideas, then make them your own.
