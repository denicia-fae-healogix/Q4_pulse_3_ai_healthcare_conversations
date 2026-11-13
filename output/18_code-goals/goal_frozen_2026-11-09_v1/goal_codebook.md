# Codebook: conversation goal and whether it was met (frozen)

Frozen 2026-11-09, version v1. Do not edit: any change needs a new dated freeze.

Each participant answered two open-ended survey questions after their health chat with an AI: what their goal was (GOAL ANSWER) and whether it was met (GOAL-MET ANSWER). You code only from these two answers.

## General rules

- **Main-goal rule.** Code every goal the answer mentions (multi-label). Then pick ONE main goal: (1) the goal the person marks as main ("mainly", "primarily"); otherwise (2) the first goal they state, skipping sentences that only give context. (3) In "I wanted X so that Y", X is the main goal and Y is an extra goal if it is an A code. (4) Reassurance (A7) follows the same first-stated rule: if it is written first, it is the main goal. (5) If the goal answer is vague, the goal-met answer may be used to find the goal. (6) If the first goal stated names no health question ("find credible information quickly", "cut down on leg work"), skip it and use the first goal that names a health question; if it says why AI was used, add the tag "Said why they used AI".
- **Goals are multi-label:** code every A goal the answers mention. The main goal must be one of them.
- **A8 (No clear goal)** is used only when no other A code applies.
- **Goal met** is one label per participant, read from the GOAL-MET ANSWER (the goal answer may help you understand it).
- **Why not met** is coded only when goal met is NOT B1 (Yes). Give every W reason that applies; at least one.
- **Tags** are yes/no and independent of the codes above. They are coded only from the two survey answers.

## Codebook A: what they wanted from the chat (goal)

### A1. Find out what might be wrong

**Definition.** They wanted the AI to explain what was causing a symptom or change in their own body (or a family member's), suggest possible conditions, or confirm a condition they suspected, including "is this normal?".

**Include:** Why is this happening; what could it be; is it X; is this normal or typical for my symptoms; give me a rough diagnosis.

**Do not include:** General facts about a condition that is already known and not tied to working out the cause (A4). How serious it is or whether to see a doctor (A2).

**Close calls:** If the answer asks both "what is it" and "how serious is it", code both. If the condition is already known and they want to learn about it, use A4, not A1.

**Examples:**

- "I was looking for any reasons"
- "gain clarity as to the cause for a health issue my daughter has"

### A2. Decide whether to get medical care

**Definition.** They wanted help judging how serious a problem was, or whether, when or where to get medical care (doctor, specialist, urgent care, ER, calling the hospital), including whether they could handle it on their own.

**Include:** Should I see a doctor; when should I seek care; is it serious; can I handle this myself; ER or urgent care; could I see a specialist.

**Do not include:** Getting ready for an appointment or a treatment that is already planned or recommended (A6). What to take or do at home (A3).

**Close calls:** "Can I handle it myself?" is A2. "What can I do at home?" is A3. If both appear, code both.

**Examples:**

- "determine if I needed to call my doctor or just wait out"
- "To get advice on when to seek medical care"

### A3. Find out what to do about it

**Definition.** They wanted practical advice on what to do: treatments, self-care, home remedies, medicines or supplements, how to get relief, how to prevent it happening again, or whether something is safe to do.

**Include:** What should I take; home remedies; how to ease the pain; treatment options; is it safe to drink; should I get the flu vaccine; how to avoid it.

**Do not include:** A structured diet, exercise or weight plan (A5). Whether to see a doctor (A2).

**Close calls:** Asking about one medicine or supplement is A3 even if framed as a question about the product. Advice on handling a life situation linked to their health also counts here.

**Examples:**

- "trying to get an idea for what my alternative osteoporosis medication options are"
- "Looking for advice on next step."

### A4. Learn about a condition, medicine or test

**Definition.** They wanted general knowledge about a condition, a medicine, a test result or a procedure, rather than working out what is wrong with them: how it works, how common it is, what results mean.

**Include:** Explain my test or scan results; how common is this; how does this medicine affect me; tell me about this condition; general facts about how exercise or sleep works ("how exercise helps sleep").

**Do not include:** Working out the cause of their own symptoms (A1). Learning what will happen at an upcoming appointment (A6).

**Close calls:** Explaining a test result is A4 even though it is about their own body: the question is what the result means, not what is causing a symptom. Learning in general what treatments exist for a condition is A4; asking what THEY should take or do is A3.

**Examples:**

- "find answers about the particular medical condition"
- "how Zepbound was affecting my physical health, mental and body image"

### A5. Get a diet, exercise or weight plan

**Definition.** They wanted the AI to make or tailor a plan or target for eating, exercise or weight: calorie goals, meal plans, how much weight to lose, a walking schedule.

**Include:** Make me a plan; how many calories; meal plan; how much weight should I lose.

**Do not include:** One-off questions about a food or supplement (A3). General facts about exercise or sleep (A4).

**Close calls:** The word "plan" or a personal target is the main sign.

**Examples:**

- "a structured plan that'll help me make eating a little easier"
- "creating a realistic and sustainable weight loss plan"

### A6. Prepare for an appointment or a care decision

**Definition.** They wanted to get ready for care that was already planned or recommended: an upcoming appointment, what to tell or ask a clinician, what an appointment will involve, or deciding about a treatment or surgery a clinician recommended.

**Include:** Before I see the doctor; prepare for her appointment; organise my thoughts for my psychologist; decide about the surgery the physician recommended; what will they do at the appointment.

**Do not include:** Whether to get care at all (A2).

**Close calls:** If the answer says "I wanted X so that I can prepare for my appointment", X is the main goal and A6 is an extra goal.

**Examples:**

- "Wanted to get an ideal before i go see a Doctor"
- "so that, when I share them with my psychologist"

### A7. Get reassurance or emotional support

**Definition.** They said they wanted to feel reassured, calmer or validated: to hear it is not serious, to calm down, or to check their feelings were valid. Wanting to reassure or support the person the chat is about (for example a family member) also counts.

**Include:** Reassurance; make sure it isn't a health scare; calm down; check my feelings were valid.

**Do not include:** Feeling reassured as a RESULT of the chat (that belongs to the goal-met answer, not the goal).

**Close calls:** Only code A7 when wanting reassurance or support is stated as part of the goal. If reassurance is WRITTEN FIRST and a concrete question follows, A7 is the main goal because it came first. If reassurance is only the reason for a concrete request ("show me what it could be so I know it isn't a health scare"), the request is the main goal and A7 is an extra goal.

**Examples:**

- "make sure my feelings and opinions were valid"
- "wanted immediate reassurance and information"

### A8. No clear goal stated

**Definition.** Neither answer says what they wanted from the chat (only that they wanted feedback or information, or why they used AI).

**Include:** I wanted to get feedback; it was faster than searching online (and the goal-met answer does not name a goal either).

**Do not include:** Any answer that names a health question, even briefly ("Finding out what's wrong with my wrist" is A1). A vague goal answer where the goal-met answer names the goal.

**Close calls:** Only code A8 when no other A code applies. If the goal answer is vague, read the goal-met answer: if it names what they asked about, code that goal.

**Examples:**

- "I wanted to get feedback."

## Codebook B: was the goal met

### B1. Yes

**Definition.** They say the goal was achieved, or describe getting what they wanted, with no part of the goal left unmet.

**Include:** Yes; I achieved my goal; it answered my questions; I think so; yes, even though it told me to see a doctor.

**Do not include:** They name a part of their goal that was not met (B2). Hedged answers such as "mostly", "for the most part" or "in a sense" (B2).

**Close calls:** "Yes, but it told me to see a doctor" is B1 if they still say the goal was met, and the chat ALSO gets the tag "Told to see a doctor". "I think so" is B1: it is unsure wording, not a statement that only part of the goal was met. Doubts about AI in general ("it always validates me") do not change a yes.

**Examples:**

- "I do feel the goal of wanting better clarity"
- "Yes, as Claude gave me a list of medications"

### B2. Partly

**Definition.** They say the goal was only partly met, use a hedge about how much was met ("mostly", "for the most part", "in a sense"), or say yes/sort of but name a part of the goal that was not met.

**Include:** Partially; mostly achieved; for the most part; achieved in a sense; sort of, but I did not get answers; less fulfilling than I hoped.

**Do not include:** A plain yes with only a general caveat about AI or doctors (B1). A clear no (B3). A conversation that is still going on with no judgement yet (B4).

**Close calls:** Any hedge about HOW MUCH of the goal was met is B2, even if nothing is named as missing.

**Examples:**

- "I had a sort of reaching the goal as I was ok and stopped but did not get answers."
- "Yes, I feel like my goal was mostly achieved."

### B3. No

**Definition.** They say the goal was not achieved.

**Include:** No; not really; not at all.

**Do not include:** Answers that say "not as much as I hoped" but still say yes (B2).

**Close calls:** "Not really" counts as No.

**Examples:**

- "Not really."
- "No. At least not as much as I hoped."

### B4. Unclear

**Definition.** The answer does not say whether the goal was met (blank, off-topic, only describes feelings without a judgement, or says the conversation is still going on).

**Include:** Blank; answers about something else; it's a continuing conversation with progress still to make.

**Do not include:** Answers that describe a clear result ("my headache was gone") are B1 even without the word yes.

**Close calls:** Use only when no judgement can be read from the answer. An ongoing conversation is B4.

**Examples:**

- "I believe we still have progress to make"

## Why the goal was not (fully) met (only when goal met is not B1)

- **W1. No clear answer or still unsure**: The AI could not say what it was, or they were left uncertain.
- **W2. Needed a real doctor**: They say only a doctor could answer, or that they still need a doctor to check. Wondering whether to see a professional while still unsure is W1.
- **W3. Too much or hard-to-read information**: The answer was too long, too technical or hard to use.
- **W4. Still in progress**: The conversation is ongoing and the goal is not finished yet (used with Unclear).
- **W5. Hedged, nothing named as missing**: They said "mostly" or similar but did not say what was missing.
- **W6. AI could not do an extra task**: The AI could not do something extra they asked for (for example, make a PDF).

## Extra tags (yes / no)

- **T-other**: Asked on behalf of someone else (child, partner, parent, friend)
- **T-whyAI**: Said why they used AI instead of searching or a doctor (faster, cheaper, less embarrassing)
- **T-doctor**: Told to see a doctor: the person's survey answers say the AI advised them to see a doctor or seek medical care (now, or if things got worse), including suggesting they book an appointment with a professional. Calling about care that is already planned (for example calling the hospital about a bed) does not count. Only the survey answers are used, not the chat text. Their own plan or view ("I needed to see a real doctor", "I still planned to speak with his doctor") does not count.
