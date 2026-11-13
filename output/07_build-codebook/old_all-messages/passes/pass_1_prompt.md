You are a qualitative researcher drafting a codebook from real conversations. This is pass 1 of 3 independent passes. Work only from the file named below. Do not open any other file in the project, and do not look for or read the output of any other pass.

## The data

`C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\pass_1_chats.txt` holds 53 conversations. In each one, a survey participant pasted a conversation they had had with an AI chatbot about a health question, for themselves or for someone else. The survey asked them to paste their most recent health conversation, including at least one message they wrote. The chats appear in a shuffled order (seed 7001).

- Each chat starts with `=== CHAT <chat_id> (...) ===` and ends with `=== END CHAT ===`.
- `[Participant, message n]:` lines are what the participant wrote. `[AI]:` lines are the chatbot's replies.
- Line breaks were lost when the survey was exported, so text may run together.
- Long AI replies are shortened, and the cut is marked `[... N words of the AI reply left out ...]`.

The file is about 225 KB. Read all of it before you start drafting. To read it in pieces, run Python, for example:
`C:\Users\DeniciaAragon\miniconda3\python.exe -c "t=open(r'C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\pass_1_chats.txt',encoding='utf-8').read(); print(t[0:40000])"`
and step through the file 40,000 characters at a time. If you use PowerShell, set `$env:PYTHONIOENCODING="utf-8"` first.

## What to find

Identify the **prompting approaches** that recur across these chats. A prompting approach is **what the participant was trying to get from the AI and how they went about getting it**: what they shared about themselves, how they framed their requests, and how they followed up on the replies.

- Find **approaches, not topics**. Questions about different illnesses, symptoms or medicines must not become separate codes just because the subject differs.
- No example categories are given on purpose. The approaches should come from the chats themselves.
- Code **only what participants wrote**. Read the AI replies as context, because a follow-up message often only makes sense next to the reply it answers.
- A chat can show more than one approach.
- An approach should **recur**: keep only approaches seen in at least 3 different chats. For 53 chats, roughly 5 to 8 approaches is a sensible size, but do not force or merge codes to reach that number.
- List any chats that fit none of your approaches.

For each approach, give:

1. `name`: a short, plain-language name of 2 to 6 words.
2. `definition`: 1 to 3 sentences. The first sentence must stand on its own as the definition.
3. `signs`: 2 to 5 concrete signs of the approach in participants' messages.
4. `closest_other`: the name of your most similar approach, and `how_it_differs` in one or two sentences.
5. `examples`: 2 or 3 example quotes from **different chats**, each with its `chat_id`. Each quote must be copied **exactly, character for character**, from a single `[Participant, message n]` line: one continuous stretch of 5 to 40 words. Never quote the AI. Do not fix spelling, punctuation or capitals, and do not join separate pieces with "...".
6. `chat_ids`: every chat that shows this approach. `n_chats` must equal the length of this list.

## Output

Write **only** valid JSON, in UTF-8, to `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\passes\pass_1_raw_output.json`, with this exact structure:

```json
{
  "pass": 1,
  "seed": 7001,
  "n_chats_read": 53,
  "approaches": [
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
  "no_approach_chats": [{"chat_id": "...", "reason": "..."}],
  "notes": "Anything a researcher should know: borderline calls, approaches you saw in only 1-2 chats, any personal identifiers you noticed."
}
```

Write the file with Python's `json.dump(..., ensure_ascii=False, indent=2)`, which makes sure quotes inside the text are escaped. Then load it again to confirm that it is valid. Then check that every quote is found exactly in the input file and every `chat_id` exists, and fix anything that fails. Do not create any other files. Your final reply should be one short line confirming that the file was written, with the number of approaches.
