# How the topic list is counted (frozen)

Frozen 2026-11-05, version v4. Do not edit: any change needs a new dated freeze. Unit coded: the participant's FIRST REAL message to the AI. AI text shown before it is context only.

**Unit-of-analysis rule (first REAL message, analyst decision 2026-11-05).** Code the participant's first message. If that message is only a greeting, a joke or a bare one-word reply with no health content, code instead their next message that contains a health statement or question; the AI turn just before it may be shown as context only. If the chat has no later message with health content, the first message is coded as it is (request NONE, topic NONE / 'no health subject'). The chats where this applies are listed by hand in output/07_build-codebook/07_first-message_substitutions.csv. A first message that asks a real question, however short, is never replaced.

Analyst decision (2026-11-05): type of request is the main analysis; health topic is a simple descriptive list.

1. Each message counts once, under its **primary** topic (secondary topics are not counted).
2. Messages with primary topic NONE are given a short group name in `07_topic_list_groups.csv` (hand-made; for example 'Chest pain', 'Kidney, liver and blood', 'Test results (heart and chest scans)', 'No health subject').
3. A group with fewer than 2 messages is shown as **Other health subject**. 'No health subject' is always shown on its own line.
4. Percentages use all analysed first messages (excluded chats left out), so they add up to 100%.
5. T11 Mental health and stress is kept even though it is small (added by the researcher).
