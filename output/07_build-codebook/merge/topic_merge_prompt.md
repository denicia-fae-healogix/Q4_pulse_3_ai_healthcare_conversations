You are a qualitative researcher. Three independent passes each read the same 53 **first messages** that survey participants wrote to an AI chatbot about a health question. Each pass drafted a codebook of **health topics: the health subject each first message asks about. Each message gets one primary topic and an optional secondary topic**. Your job is to merge the three drafts into one draft codebook.

## Files to read (read only these)

- `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\passes\topic_pass_1_raw_output.json`
- `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\passes\topic_pass_2_raw_output.json`
- `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\passes\topic_pass_3_raw_output.json`
- `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\first_messages.csv`: every first message (columns `chat_id`, `text`). Use it to check quotes and borderline matches. The `ai_context` column is context only; never quote it.

Use Python to read them, for example `C:\Users\DeniciaAragon\miniconda3\python.exe`, and set `$env:PYTHONIOENCODING="utf-8"` in PowerShell.

## Merge rules

1. **Match codes across passes by meaning, not by name.** Two pass codes match when their definitions describe the same thing. The chats they share are useful evidence.
2. **Each pass code goes to at most one merged code.** If one pass split a code into two that another pass kept together, choose the level of detail that most passes used. Map both split codes to the merged code, and explain this in `merge_note`.
3. **Keep a merged code only if it appears in at least 2 of the 3 passes.** Put codes found in only one pass under `dropped`, with a reason. If one of them looks clearly distinct and important, set `worth_review` to true so the researcher can decide. Do not keep it.
4. Stay within this codebook's dimension: health topics: the health subject each first message asks about. Each message gets one primary topic and an optional secondary topic. There must be **no code for replying to, following up on, or reacting to the AI**.
5. For each merged code, write the clearest `definition` (1 to 3 sentences; the first sentence stands alone), `signs` (2 to 5), `closest_other` (another merged code's name), and `how_it_differs` (including how to decide between the two).
6. Give **2 or 3 example quotes from different chats**. Each one is copied exactly, character for character, from one message in `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\input\first_messages.csv`: one continuous stretch of 3 to 40 words, or the whole message if it is shorter. Prefer quotes the passes used. Check every quote against the file before you finish.
7. In `source_codes`, record the exact pass code names that map to this merged code, keyed by pass number. Use an empty list for a pass that lacked it.
8. Give the merged codes IDs T1, T2, and so on. A script will compute the chat counts and the final order from the passes, so do not count chats yourself.

## Output

Write **only** valid JSON (UTF-8) to `C:\Users\DeniciaAragon\OneDrive - Healogix\Q4_3_Pulse\output\07_build-codebook\merge\topic_merge_raw_output.json`, using `json.dump(..., ensure_ascii=False, indent=2)`, with this structure:

```json
{
  "codebook": "topic",
  "codes": [
    {
      "code": "T1",
      "name": "...",
      "definition": "...",
      "signs": ["..."],
      "closest_other": "...",
      "how_it_differs": "...",
      "examples": [{"chat_id": "...", "quote": "..."}],
      "source_codes": {"1": ["..."], "2": ["..."], "3": ["..."]},
      "merge_note": "How the pass codes were combined, and any wording choices."
    }
  ],
  "dropped": [{"pass": 1, "name": "...", "reason": "...", "worth_review": false}],
  "notes": "Overall notes for the researcher: how well the passes agreed, unclear boundaries between codes, suggestions for the pilot."
}
```

Every pass code name must appear exactly once: either in some `source_codes` list or in `dropped`. Check this, and that every quote is found verbatim, before you finish. Do not create any other files. Your final reply should be one short line confirming the file was written, with the number of merged codes.
