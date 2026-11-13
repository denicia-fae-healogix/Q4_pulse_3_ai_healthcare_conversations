You are a careful qualitative coder applying a fixed codebook. You are pilot coder 1 of 3; the coders work independently. Work only from the two files named below. Do not open any other file in the project, and do not look for or read the output of any other coder.

## Files

- **Codebook:** `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\16_pilot-goal-codebooks\codebook\pilot_goal_codebook.md`. Read all of it first. Apply it exactly as written; do not invent new codes.
- **Answers:** `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\16_pilot-goal-codebooks\input\coder_1_input.txt` holds 16 survey participants' answers in a shuffled order (seed 16101). Each participant had a health conversation with an AI chatbot and then answered two open-ended survey questions:
  - **GOAL ANSWER**: what their goal for the conversation was.
  - **GOAL-MET ANSWER**: whether they felt their goal was met.
  - Each block starts with `=== CHAT <chat_id> ===` and ends with `=== END CHAT ===`.

Read the file with Python, for example:
`C:\Users\DeniciaAragon\miniconda3\python.exe -c "print(open(r'C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\16_pilot-goal-codebooks\input\coder_1_input.txt',encoding='utf-8').read())"`
If you use PowerShell, set `$env:PYTHONIOENCODING="utf-8"` first.

## What to do for each participant

1. **Goals (codebook A):** list EVERY A code that applies (multi-label), in the order the goals are stated.
2. **Main goal:** pick exactly ONE A code using the main-goal rule.
3. **Goal met (codebook B):** exactly one of `B1`, `B2`, `B3`, `B4`.
4. **Why not met (W list):** only if goal met is NOT `B1`, list every W code that applies (at least one). If goal met is `B1`, give an empty list.
5. **Tags:** for each of the 3 tags (`T-doctor`, `T-other`, `T-whyAI`) say `true` or `false`.

For the main goal, goal met, and every tag you mark `true`, record:

- `source`: `"goal"` or `"goal_met"`: which answer the quote comes from.
- `evidence`: a quote copied **exactly, character for character**, from that answer. Use one continuous stretch of 3 to 40 words, or the whole answer if shorter. Do not fix spelling, punctuation or capitals, and do not join pieces with "...".
- `confidence`: `"high"` (the codebook clearly decides it), `"medium"` (fits, but another code was close) or `"low"` (a guess).
- `unclear`: an empty string if the codebook decided the case. Otherwise start with "unclear because" and say which definitions or rules did not decide it and which other code you considered.

For goal met `B4` with a blank answer, `evidence` may be an empty string.

## Output

Write **only** valid JSON, in UTF-8, to `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\16_pilot-goal-codebooks\coders\coder_1_raw_output.json`, with this exact structure:

```json
{
  "coder": 1,
  "seed": 16101,
  "n_chats_coded": 16,
  "codings": [
    {
      "chat_id": "...",
      "goals": ["A1", "A2"],
      "main_goal": {"code": "A1", "source": "goal", "evidence": "...", "confidence": "high", "unclear": ""},
      "goal_met": {"code": "B2", "source": "goal_met", "evidence": "...", "confidence": "medium", "unclear": "unclear because ..."},
      "why_not": ["W1"],
      "tags": {
        "T-doctor": {"value": false},
        "T-other": {"value": true, "source": "goal", "evidence": "...", "confidence": "high", "unclear": ""},
        "T-whyAI": {"value": false}
      }
    }
  ],
  "codebook_feedback": "Any definitions or rules that were confusing, overlapping or missing, with chat IDs."
}
```

The main goal must be one of the codes in `goals`.

Write the file with Python's `json.dump(..., ensure_ascii=False, indent=2)`, then load it again to confirm it is valid. Check that it has exactly 16 codings, one per chat ID in the input, and that every evidence quote appears exactly in the answer you named. Fix any quote that does not. Then reply with one line: the output file path.
