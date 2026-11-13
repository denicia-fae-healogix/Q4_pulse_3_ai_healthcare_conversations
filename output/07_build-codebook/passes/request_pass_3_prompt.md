You are a qualitative researcher drafting a codebook from real data. This is pass 3 of 3 independent passes. Work only from the file named below. Do not open any other file in the project, and do not look for or read the output of any other pass.

## The data

`C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\request_pass_3_input.txt` holds 53 short texts. Each one is the **first message** that a survey participant wrote to an AI chatbot about a health question, for themselves or for someone else. The messages appear in a shuffled order (seed 7203).

- Each block starts with `=== CHAT <chat_id> ===` and ends with `=== END CHAT ===`.
- `[FIRST MESSAGE]:` is the participant's first message. **This is the only text you code.**
- In 2 blocks, a `[CONTEXT ONLY ...]` line shows AI text that came before the first message. Read it only to understand the message. Never code it or quote it.
- Line breaks were lost in the survey export, so text may run together. Personal names were replaced with `[NAME]`.

Read the whole file before drafting. For example:
`C:\Users\DeniciaAragon\miniconda3\python.exe -c "print(open(r'C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\request_pass_3_input.txt',encoding='utf-8').read())"`
If you use PowerShell, set `$env:PYTHONIOENCODING="utf-8"` first.

## What to find

Build a codebook of **types of request**: what the participant wanted the AI to give them in this first message, that is, the kind of help or answer they were after.

- Code the **kind of help wanted**, not the health subject. The same type of request can be about any illness, symptom or medicine, and must not be split by subject. A separate codebook covers health topics.
- **Do not create a code for replying to, following up on, or reacting to the AI.** We are studying what people asked for at the start. If a message continues an earlier exchange, code what it asks for.
- No example categories are given on purpose. The types should come from the messages themselves.
- A message can show **more than one** type of request. Code every type that is clearly there.
- A type should recur: keep only types seen in at least 3 different messages. For 53 messages, roughly 5 to 8 types is a sensible size. Do not force a number.
- List any messages that fit none of your types, such as a greeting with no request, in `no_code_chats` with a reason.

For each type of request, give:

1. `name`: a short, plain-language name of 2 to 6 words.
2. `definition`: 1 to 3 sentences. The first sentence must stand on its own as the definition.
3. `signs`: 2 to 5 concrete signs in the message, such as typical phrasings or question forms.
4. `closest_other`: the name of your most similar type, and `how_it_differs` in one or two sentences, including how to decide between them.
5. `examples`: 2 or 3 example quotes from **different chats**, each with its `chat_id`. Each quote must be copied **exactly, character for character**, from a `[FIRST MESSAGE]` line: one continuous stretch of 3 to 40 words, or the whole message if it is shorter. Do not fix spelling, punctuation or capitals, and do not join separate pieces with "...".
6. `chat_ids`: every chat that shows this type. `n_chats` must equal the length of this list.

## Output

Write **only** valid JSON, in UTF-8, to `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\passes\request_pass_3_raw_output.json`, with this exact structure:

```json
{
  "codebook": "request",
  "pass": 3,
  "seed": 7203,
  "n_messages_read": 53,
  "codes": [
    {
      "name": "...",
      "definition": "...",
      "signs": ["...", "..."],
      "closest_other": "...",
      "how_it_differs": "...",
      "examples": [{"chat_id": "...", "quote": "..."}],
      "chat_ids": ["...", "..."],
      "n_chats": 0
    }
  ],
  "no_code_chats": [{"chat_id": "...", "reason": "..."}],
  "notes": "Anything a researcher should know: borderline calls, types seen in only 1-2 messages, any personal identifiers you noticed."
}
```

Every one of the 53 chats must appear in at least one code's `chat_ids` or in `no_code_chats`, and not in both.

Write the file with Python's `json.dump(..., ensure_ascii=False, indent=2)`, then load it again to confirm that it is valid. Then check that:

- every quote is found exactly in the input file, inside the credited chat's first message;
- every `chat_id` exists;
- every chat is covered.

Fix anything that fails. Do not create any other files. Your final reply should be one short line confirming that the file was written, with the number of types.
