You are a qualitative researcher drafting a codebook from real data. This is pass 2 of 3 independent passes. Work only from the file named below. Do not open any other file in the project, and do not look for or read the output of any other pass.

## The data

`C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\topic_pass_2_input.txt` holds 53 short texts. Each one is the **first message** that a survey participant wrote to an AI chatbot about a health question, for themselves or for someone else. The messages appear in a shuffled order (seed 7102).

- Each block starts with `=== CHAT <chat_id> ===` and ends with `=== END CHAT ===`.
- `[FIRST MESSAGE]:` is the participant's first message. **This is the only text you code.**
- In 2 blocks, a `[CONTEXT ONLY ...]` line shows AI text that came before the first message. Read it only to understand what the message is about. Never code it or quote it.
- Line breaks were lost in the survey export, so text may run together. Personal names were replaced with `[NAME]`.

Read the whole file before drafting. For example:
`C:\Users\DeniciaAragon\miniconda3\python.exe -c "print(open(r'C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\topic_pass_2_input.txt',encoding='utf-8').read())"`
If you use PowerShell, set `$env:PYTHONIOENCODING="utf-8"` first.

## What to find

Build a codebook of **health topics**: the health subject each first message asks about, such as a condition, a body system, or an area of health.

- Code the **subject only**. Do not code what kind of answer the person wanted, who the question is about, or how it was phrased. A separate codebook covers the type of request.
- No example categories are given on purpose. The topics should come from the messages themselves.
- Give every message **one primary topic**, the main subject. Add **one optional secondary topic** only if the message clearly also asks about a second subject.
- Topics should be broad enough to recur. Keep only topics that cover at least 3 different messages, counting primary and secondary. For 53 messages, roughly 5 to 8 topics is a sensible size. Do not force a number.
- If a message has no clear health subject, or its subject fits none of your topics, give it the primary topic `"NONE"` and explain why in `no_code_chats`.

For each topic, give:

1. `name`: a short, plain-language name of 1 to 5 words.
2. `definition`: 1 to 3 sentences. The first sentence must stand on its own as the definition. Say what is included and what is not.
3. `signs`: 2 to 5 concrete signs in the message, such as kinds of words, conditions, body parts or medicines.
4. `closest_other`: the name of your most similar topic, and `how_it_differs` in one or two sentences, including how to decide between them.
5. `examples`: 2 or 3 example quotes from **different chats**, each with its `chat_id`. Each quote must be copied **exactly, character for character**, from a `[FIRST MESSAGE]` line: one continuous stretch of 3 to 40 words, or the whole message if it is shorter. Do not fix spelling, punctuation or capitals, and do not join separate pieces with "...".

## Output

Write **only** valid JSON, in UTF-8, to `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\passes\topic_pass_2_raw_output.json`, with this exact structure:

```json
{
  "codebook": "topic",
  "pass": 2,
  "seed": 7102,
  "n_messages_read": 53,
  "codes": [
    {
      "name": "...",
      "definition": "...",
      "signs": ["...", "..."],
      "closest_other": "...",
      "how_it_differs": "...",
      "examples": [{"chat_id": "...", "quote": "..."}]
    }
  ],
  "assignments": [{"chat_id": "...", "primary": "<topic name or NONE>", "secondary": "<topic name or null>"}],
  "no_code_chats": [{"chat_id": "...", "reason": "..."}],
  "notes": "Anything a researcher should know: borderline calls, topics seen in only 1-2 messages, any personal identifiers you noticed."
}
```

`assignments` must hold all 53 chats exactly once. Every `primary` and `secondary` must be one of your topic names, `"NONE"` (primary only), or `null` (secondary only).

Write the file with Python's `json.dump(..., ensure_ascii=False, indent=2)`, then load it again to confirm that it is valid. Then check that:

- every quote is found exactly in the input file, inside the credited chat's first message;
- every chat appears once in `assignments`;
- every topic covers at least 3 chats.

Fix anything that fails. Do not create any other files. Your final reply should be one short line confirming that the file was written, with the number of topics.
