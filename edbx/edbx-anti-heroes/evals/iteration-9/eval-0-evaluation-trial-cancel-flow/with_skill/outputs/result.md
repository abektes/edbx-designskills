This is a classic "Hotel California" pattern—easy to check in, but you can never (easily) leave. Using the **Anti-Heroes** method, we can move the conversation away from "it feels gross" to a principled critique of how these specific design choices undermine user agency and trust.

Here is your structured critique for the MossBowl design review.

### 1. Frame
*   **Design under review:** MossBowl cancellation flow (v1.0).
*   **User task:** Ending a recurring financial commitment.
*   **User emotional state:** Likely frustrated (the service didn't work for them) or anxious (trying to save money/stick to a budget).
*   **Business pressure:** High retention targets; "industry standard" dark patterns.
*   **Mode:** Evaluation & Ethical Dialogue.

---

### 2. Anti-Hero Hits

| Card | What is happening | Where | Why it is anti-user |
| :--- | :--- | :--- | :--- |
| **Trap-Setter** | Labeling the cancel path as "Plan health." | Settings Sub-page | This is linguistic obfuscation. Users look for "Subscription" or "Cancel," not "Health." It intentionally hides the exit. |
| **Empathy Manipulator** | Half-empty fridge photo + "lose your 7-day streak" copy. | Step 1 Takeover | This weaponizes loss aversion and guilt. It frames a business transaction as a personal failure of the user’s habits. |
| **Obstacle Course** | Forcing a scroll past three plan cards to find a small, grey link. | Step 2 (Discount) | This is "visual interference." It creates artificial friction to exhaust the user’s "no" until they give up and stay. |
| **Hide-and-Seek** | "No thanks, cancel anyway" is small, grey, and low-contrast. | Step 2 Footer | This violates accessibility and hierarchy. It makes the user's primary intent the least visible element on the screen. |

---

### 3. Hero Counter-moves

| Paired Card | Concrete Change | Why it restores user value |
| :--- | :--- | :--- |
| **Empowerer** | Rename the section "Subscription & Billing" and put "Cancel Plan" in plain text. | Restores symmetry. If it was easy to sign up, it should be easy to leave. |
| **Life Coach** | Replace guilt copy with: "Your recipes and history will be saved for 6 months if you decide to return." | Provides helpful, neutral information that reduces anxiety without manipulation. |
| **Unveiler** | Show the 30% discount as a clear, upfront choice alongside "Confirm Cancellation." | Respects the user’s intelligence. It’s an honest negotiation, not a trap. |
| **Fair Fighter** | Use standard button styling for "Cancel Anyway" so it’s as legible as the "Stay" button. | Acknowledges that the user has already made a decision and respects their time. |

---

### 4. Ethical Dialogue: How to talk to the Growth PM

When the PM says, "Every SaaS does it," they are citing "competitive necessity." You can pivot the conversation toward **Brand Equity** and **Long-term LTV** using these scripts:

*   **The "Ref" Script:** "I want to call a **Trap-Setter** on the 'Plan health' label. While other apps use it, it creates a 'dishonesty tax.' When users eventually find it, they feel tricked, which makes them less likely to ever resubscribe in the future."
*   **The "Streak" Script:** "The fridge photo and streak copy act as an **Empathy Manipulator**. If we have to guilt-trip users into staying, our retention data is 'dirty'—we aren't winning on value, we're winning on shame. Can we be a **Life Coach** instead and just tell them their data is safe?"
*   **The "Friction" Script:** "The small grey link is an **Obstacle Course**. It might prevent a cancellation today, but it guarantees a negative App Store review or a support ticket tomorrow. Let’s be **Fair Fighters** and make the 'cancel' button accessible."

**Follow-up question for the team:** "Do we want MossBowl to be a brand users trust to let them go, or a brand they feel they have to escape from?"

---

### 5. Necessary Friction (What is OK to keep)
You don't have to make it a "one-click-and-you're-gone" ghost town. Some friction is actually protective:

*   **The Confirmation Step:** A single "Are you sure? Your next box is scheduled for Tuesday" is helpful friction to prevent accidental clicks.
*   **The "Why" Survey:** Asking for a reason for leaving (Price, Quality, etc.) is acceptable *if* it doesn't block the exit and is easy to skip.
*   **The Save Offer:** Offering a discount is fine, as long as the "No thanks" is just as easy to tap as the "Accept" button.