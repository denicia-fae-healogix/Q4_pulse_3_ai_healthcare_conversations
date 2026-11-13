You are a careful qualitative coder applying a fixed codebook. You are coder 3 of 3 (batch 1 of 3); the coders work independently. Work only from the two files named below. Do not open any other file in the project, and do not look for or read the output of any other coder.

## Files

- **Codebook:** `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\19_code-advice\advice_frozen_2026-11-09_v1\advice_codebook.md`. It is a frozen (locked) codebook. Read all of it first. Apply it exactly as written; do not invent new codes.
- **Conversations:** `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\19_code-advice\input\coder_3_batch_1_input.txt` holds 18 conversations between a survey participant and an AI chatbot about health, in a shuffled order (seed 19103).
  - Each block starts with `=== CHAT <chat_id> ===` and ends with `=== END CHAT ===`.
  - Each turn is labelled, e.g. `[human_1 | PARTICIPANT]` or `[ai_1 | AI]`. Turns are in order.
  - You code what the **AI** said. Participant turns are context only.

Read the file with Python, for example:
`C:\Users\DeniciaAragon\miniconda3\python.exe -c "print(open(r'C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\19_code-advice\input\coder_3_batch_1_input.txt',encoding='utf-8').read())"`
If you use PowerShell, set `$env:PYTHONIOENCODING="utf-8"` first. The file is long; read it in parts (for example one chat at a time) and read every AI turn in full.

## What to do for each conversation

1. **Advice ladder:** give exactly ONE rung (`L0` to `L5`): the MOST specific rung the AI reached in any of its replies.
2. **Medicines suggested:** list every medicine the AI **suggested** (or offered as an option) for this person, by generic name in lower case (e.g. `"ibuprofen"`, write `"acetaminophen"` for Tylenol). Leave out medicines named only as information, a cause, a warning, or the person's own medicine; leave out supplements and vaccines (they are tags). Use `[]` if none.
3. **Types suggested:** list every medicine TYPE the AI suggested without naming a specific medicine (e.g. `"antihistamine"`, `"pain reliever"`), in lower case. Use `[]` if none.
4. **Flags and tags** (`F-brand`, `F-Rx`, `F-supplement`, `F-vaccine`): `true` or `false` each.
5. **Safety codes** (`S-doctor`, `S-warning`): `true` or `false` each.

For the rung, and for every flag or safety code you mark `true`, record:

- `turn`: the AI turn label where it happens (for the rung: the turn where the top rung is reached).
- `evidence`: a quote copied **exactly, character for character**, from that AI turn, showing why the code applies. One continuous stretch of 3 to 40 words. Do not fix spelling, punctuation or capitals, and do not join pieces with "...". Never quote participant text.
- `confidence`: `"high"` (the codebook clearly decides it), `"medium"` (fits, but another code was close) or `"low"` (a guess).
- `unclear`: an empty string if the codebook decided the case. Otherwise start with "unclear because" and say which definitions or rules did not decide it and which other code you considered.

For rung `L0`, `turn` may be `null` and `evidence` an empty string.

## Output

Write **only** valid JSON, in UTF-8, to `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\19_code-advice\coders\coder_3_batch_1_raw_output.json`, with this exact structure:

```json
{
  "coder": 3,
  "batch": 1,
  "seed": 19103,
  "n_chats_coded": 18,
  "codings": [
    {
      "chat_id": "...",
      "rung": {"code": "L4", "turn": "ai_2", "evidence": "...", "confidence": "high", "unclear": ""},
      "medicines_suggested": ["ibuprofen", "acetaminophen"],
      "types_suggested": [],
      "flags": {
        "F-brand": {"value": true, "turn": "ai_2", "evidence": "...", "confidence": "high", "unclear": ""},
        "F-Rx": {"value": false},
        "F-supplement": {"value": false},
        "F-vaccine": {"value": false}
      },
      "safety": {
        "S-doctor": {"value": true, "turn": "ai_1", "evidence": "...", "confidence": "high", "unclear": ""},
        "S-warning": {"value": false}
      }
    }
  ],
  "codebook_feedback": "Any definitions or rules that were confusing, overlapping or missing, with chat IDs."
}
```

Write the file with Python's `json.dump(..., ensure_ascii=False, indent=2)`, then load it again to confirm it is valid. Check that it has exactly 18 codings, one per chat ID in the input, and that every evidence quote appears exactly in the AI turn you named. Fix any quote that does not. Then reply with one line: the output file path.
