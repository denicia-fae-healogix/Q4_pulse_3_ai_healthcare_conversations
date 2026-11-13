You are a careful qualitative coder applying a fixed codebook. You are pilot coder 2 of 3; the coders work independently. Work only from the two files named below. Do not open any other file in the project, and do not look for or read the output of any other coder.

## Files

- **Codebook:** `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\08_pilot-codebook\codebook\pilot_codebook.md`. Read all of it first. Apply it exactly as written; do not invent new codes.
- **Messages:** `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\08_pilot-codebook\input\coder_2_input.txt` holds 12 first messages that survey participants wrote to an AI chatbot about health, in a shuffled order (seed 8102).
  - Each block starts with `=== CHAT <chat_id> ===` and ends with `=== END CHAT ===`.
  - `[FIRST MESSAGE]:` is the participant's message. **This is the only text you code.**
  - A `[CONTEXT ONLY ...]` line shows AI text that came before the message. Use it only to understand the message. Never code it or quote it.

Read the files with Python, for example:
`C:\Users\DeniciaAragon\miniconda3\python.exe -c "print(open(r'C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\08_pilot-codebook\input\coder_2_input.txt',encoding='utf-8').read())"`
If you use PowerShell, set `$env:PYTHONIOENCODING="utf-8"` first.

## What to do for each message

Apply **both** codebooks.

1. **Health topic:** exactly one `primary` topic code (`T1`, `T2`, ... or `"NONE"`), and an optional `secondary` topic code (or `null`).
2. **Type of request:** every request code that applies (`R1`, `R2`, ...). If none applies, give an empty list and say why in `request_none_reason`.

For every code you give (primary, secondary and each request code), record:

- `evidence`: a quote copied **exactly, character for character**, from the `[FIRST MESSAGE]` that shows why the code applies. Use one continuous stretch of 3 to 40 words, or the whole message if it is shorter. Do not fix spelling, punctuation or capitals, and do not join pieces with "...".
- `confidence`: `"high"` (the definition clearly decides it), `"medium"` (fits, but another code was close) or `"low"` (a guess between codes).
- `unclear`: an empty string if the codebook decided the case. Otherwise, start with "unclear because" and say which definitions or rules did not decide it, and which other code you considered.

For a `"NONE"` primary topic, give `evidence` as an empty string and explain in `unclear` or `none_reason` why no topic fits.

## Output

Write **only** valid JSON, in UTF-8, to `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\08_pilot-codebook\coders\coder_2_raw_output.json`, with this exact structure:

```json
{
  "coder": 2,
  "seed": 8102,
  "n_messages_coded": 12,
  "codings": [
    {
      "chat_id": "...",
      "topic": {
        "primary":   {"code": "T1", "evidence": "...", "confidence": "high", "unclear": ""},
        "secondary": null,
        "none_reason": ""
      },
      "request": {
        "codes": [{"code": "R1", "evidence": "...", "confidence": "medium", "unclear": "unclear because ..."}],
        "request_none_reason": ""
      }
    }
  ],
  "codebook_feedback": "Any definitions or rules that were confusing, overlapping or missing, with chat IDs."
}
```

`secondary` is either `null` or an object with the same four fields as `primary`.

Write the file with Python's `json.dump(..., ensure_ascii=False, indent=2)`, then load it again to confirm it is valid. Then check that:

- all 12 chats appear exactly once in `codings`;
- every code is a code from the codebook;
- every `evidence` quote is found exactly in that chat's `[FIRST MESSAGE]`.

Fix anything that fails. Do not create any other files. Your final reply should be one short line confirming that the file was written.
