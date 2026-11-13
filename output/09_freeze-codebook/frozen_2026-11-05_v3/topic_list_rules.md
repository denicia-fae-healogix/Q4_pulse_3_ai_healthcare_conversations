# How the topic list is counted (frozen)

Frozen 2026-11-05, version v3. Do not edit: any change needs a new dated freeze. Unit coded: the participant's FIRST message to the AI. AI text shown before it is context only.

Analyst decision (2026-11-05): type of request is the main analysis; health topic is a simple descriptive list.

1. Each message counts once, under its **primary** topic (secondary topics are not counted).
2. Messages with primary topic NONE are given a short group name in `07_topic_list_groups.csv` (hand-made; for example 'Chest pain', 'Kidney, liver and blood', 'No health subject').
3. A group with fewer than 2 messages is shown as **Other health subject**. 'No health subject' is always shown on its own line.
4. Percentages use all analysed first messages (excluded chats left out), so they add up to 100%.
5. T11 Mental health and stress is kept even though it is small (added by the researcher).
