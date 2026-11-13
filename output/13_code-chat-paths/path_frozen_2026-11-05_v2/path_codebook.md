# Codebook: how the conversation unfolded (frozen)

Frozen 2026-11-05, version v2. Do not edit: any change needs a new dated freeze.

You code two things for each conversation. The participant's first request (column 1) is already coded and is not part of this task.

## General rules

- **The 2nd message** is the next real participant message after the turn marked CODED FIRST MESSAGE.
- **Skip thanks-only messages** (for example 'Nice', 'Ok thank you', 'Convert to PDF' on its own) and use the next real message. If nothing real follows, column 2 is M5.
- **Fragments:** if a turn starts with a thanks or task fragment (for example 'Convert to PDF') but then gives real content, ignore the fragment and code the rest of the turn.
- **One column-2 code per chat.**
- **Question wins:** if the 2nd message gives information AND asks a real new question, column 2 codes the question (M1 or M2). The information still counts for column 3.
- **Action wins:** if the 2nd message asks both to understand and what to do, code M2.
- **Answering the AI's follow-up question** counts as M3 (Shared more about themselves).
- **A question to the AI about itself** (its own experience or opinion) is M1.
- **Column 3 is coded only when column 2 is M2 or M3.** Otherwise it is empty.
- **Background information** means: age, body weight, height, activity level and regular habits, health history, other conditions, medicines, how long the problem has existed overall, other symptoms beyond the problem being asked about, and recent events or care that led up to the problem, including something that happened before it started (for example travel, 'after sleeping', a doctor visit, a referral, glasses).
- **NOT background:** the main complaint itself (for example 'my foot hurts'); describing the main problem in more detail (where it is, how it feels, how bad, when it shows up, how long each episode lasts, symptoms that are part of that problem); a symptom asked about only as a 'what if'; saying there are NO other symptoms.
- **Column 3 records the FIRST time** background information appears in any participant message, from the coded first message to the end of the chat.
- **'The AI asked'** means the AI turn just before asked the participant a real question about them or their situation, OR invited them to share more about it (for example 'If you tell me where the pain is, I can narrow it down'). This can look like a form or list with no question mark (for example asking for current weight). Headings written as questions ('What causes it?') do not count.
- Background about the person the question is about counts, even if that is a partner, child or parent.

## Column 2: what the participant did in their 2nd message

### M1. Kept asking to understand

**Definition.** The 2nd message asks a new question to understand something: what it is, why it happens, what it means, how long it lasts, how to tell, how likely.

**Include:** Questions about causes, meaning, test findings, duration, likelihood or general facts, even if background information is mentioned along the way (question wins). Questions that ask the AI about its own experience or opinion (for example survey-style questions) [P8].

**Do not include:** Questions about what to do, take, change, or whether to see a doctor or get a test (M2). Statements with no new question (M3).

**Close calls:** 'How can I tell if I have X' is understanding (M1); 'Should I get checked for X' is action (M2). If both are asked, M2 wins. Practical 'how likely' questions (for example hospital bed availability) are M1. A question to the AI about itself is M1, not M6 [P8].

**Examples:**

- "How long does the flu last"
- "Can we tell me what causes dandruff"

### M2. Then asked what to do

**Definition.** The 2nd message asks for action: what to do, take or change, whether to see a doctor or specialist, which tests to get, whether something is safe, or what to do if a new symptom appears.

**Include:** Treatment, self-care, medicines, care-seeking, tests, plans, safety and 'what if I have this symptom' questions. Wins over M1 when both are asked.

**Do not include:** Questions that only ask what something is or why (M1). Pushback on the AI's advice (M4).

**Close calls:** A message that adds information and then asks 'What should I do?' is M2 (the question wins; any background information still counts in column 3).

**Examples:**

- "Should I schedule an appointment with a specialist?"
- "What should I do?"

### M3. Shared more about themselves

**Definition.** The 2nd message mainly gives more information, with no new question: background information (age, health history, medicines, how long, other conditions or symptoms, weight, height, activity level or regular habits) and/or more description of the main problem, for themselves or the person they are asking for.

**Include:** Answers to the AI's follow-up questions; extra background offered on their own; information about a child, partner or parent they are asking for.

**Do not include:** Messages that also ask a real new question (M1 or M2). Messages saying the AI was wrong (M4). Continuing a task such as re-submitting a draft (M6).

**Close calls:** Adding a fact the AI did not know (for example the cause of their anemia) is M3, unless they say the AI got it wrong (M4). Only background information moves the chat into column 3 groups 1 to 3. More description of the main problem is M3 but is not background information for column 3.

**Examples:**

- "more like physical exhaustion"
- "For husband, he also had type 2 diabetes and smokes"

### M4. Pushed back or questioned the AI

**Definition.** The 2nd message disagrees with, corrects or challenges the AI, says it missed or misunderstood something, or asks it to check itself.

**Include:** 'You are missing?', 'that's not right', 'are you sure?', asking the AI to re-check earlier information.

**Do not include:** Simply adding new information without saying the AI was wrong (M3).

**Close calls:** If the main move is correcting the AI, code M4 even if a question follows.

**Examples:**

- "Claude, you are missing a conversation."

### M6. Continued a task

**Definition.** The 2nd message carries on a task the person started, such as re-submitting an edited version of a text for more help, without a new health question.

**Include:** Re-pasted or revised drafts, follow-up edits to a document.

**Do not include:** New questions (M1, M2), new information about themselves (M3), corrections of the AI (M4).

**Close calls:** Small label (1 chat); kept by researcher choice.

**Examples:**

- "I just went a whole week without saying anything to my family."

### M5. Stopped after one message

**Definition.** There is no real participant message after the coded first message.

**Include:** Chats that end after the AI's answer; chats where the only later messages are thanks or acknowledgements.

**Do not include:** Any later message with a question, information, pushback or a task (M1 to M4, M6).

**Close calls:** 'Nice' or 'Ok thank you' alone does not count as a 2nd message. If a turn starts with a thanks or task fragment (for example 'Convert to PDF') but then gives real content, ignore the fragment and code the rest of the turn [P7].

**Examples:**

- (no example in this data)

## Column 3: when they shared background information

### D1. With the first message

**Definition.** The coded first message already contains background information about the person the question is about (themselves or someone they care for).

**Include:** Age, body weight, height, activity level and regular habits (for example 'I run daily', 'mostly sedentary') [P1], health history, other conditions, medicines, how long the problem has existed overall [P5], other symptoms beyond the problem asked about [P6], and recent events or care that led up to it, including something that happened before it started (for example travel, 'after sleeping', a doctor visit, a referral, prism glasses) [P3].

**Do not include:** The main complaint on its own ('my foot is hurting', 'I have a tummy ache'). General or hypothetical questions. A symptom asked about only as a 'what if' [P2]. Saying there is NO other symptom ('my other symptoms are none') [P4]. How long each flare or episode lasts [P5]. The activity during which the symptom shows up ('chest pain when running') [P3]. Symptoms that are part of the problem asked about (itching and bumps when asking about hives) [P6].

**Close calls:** 'Stomach aches for the past few weeks' counts (how long). 'After travel with lots of walking' counts (event that led up to it). 'Why is my foot hurting' does not (main complaint only). 'For the past few weeks' counts (overall duration); 'only there for a few days then disappears' does not (episode length) [P5]. 'After sleeping' counts (before it started); 'hurts when I bend' does not (when it shows up) [P3]. A headache alongside neck pain counts as another symptom [P6].

**Examples:**

- "I've been dealing with some bad stomach aches for the past few weeks."
- "I want to deal with my pcos, anemia, pmdd, and high cholesterol"

### D2. After the AI asked

**Definition.** The first background information comes in a later message that answers a question the AI asked about the person, or follows an AI invitation to share more, in the turn just before.

**Include:** Replies to AI questions such as 'have you had other symptoms?', 'how did it start?', 'what are your biggest stressors?'. Replies after an AI invitation such as 'If you tell me where the pain is, I can narrow it down', because the person was primed to give that information. [L26]

**Do not include:** AI questions that are only section headings ('What happens during sleep apnea?'), which are not asking the person anything.

**Close calls:** If the AI asked but the person shares a different, unrequested piece of background, it still counts as D2 (they were prompted to say more). AI questions can look like a form with no question mark (for example a list asking for current weight); a reply to that counts as D2 [P9]. An invitation ('If you tell me X, I can...') counts as the AI asking, even without a question mark. [L26]

**Examples:**

- "And I've been to the doctor before and they gave me like a cream to put on it."
- "I do have a lot of cramping and gas between episodes."
- "For husband, he also had type 2 diabetes and smokes"

### D3. On their own later

**Definition.** The first background information comes in a later message that the AI did not ask for or invite.

**Include:** Background added without being prompted.

**Do not include:** Background given in the first message (D1), or right after an AI question about them or an AI invitation to share more (D2). [L26]

**Examples:**

- (no example in this data)

### D4. Never shared

**Definition.** No background information appears in any of their messages; they only described the main problem.

**Include:** Chats that stay on the main complaint or stay general. Chats with only 'what if' symptoms [P2] or 'no other symptoms' answers [P4].

**Do not include:** Any background information at any point (D1 to D3).

**Close calls:** Describing where the problem is, how it feels or how bad it is does not count as background (it is still Shared more about themselves in column 2).

**Examples:**

- (no example in this data)
