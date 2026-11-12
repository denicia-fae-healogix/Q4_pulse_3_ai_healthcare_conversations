# Q4 Pulse 3 codebook: AI health conversations

One row per participant (`pid`). This codebook covers every variable that was coded or derived from the pasted conversations, plus the groupings built from them for the decks, web pages and the 07 report.

**Files**

| File | What it holds | Made by |
|---|---|---|
| `05_Q4_3_conversations_wide_deid.csv` | Survey answers and PANAS, plus the split conversation turns | 00 and 01 scripts |
| `05_Q4_3_conversations_wide_deid_coded.csv` | v1 codes (section 3) | LLM-assisted coding, `coding_source = claude_llm_v1` (11 Nov 2026) |
| `05_Q4_3_conversations_wide_deid_coded_v2.csv` | v1 codes plus v2 participant codes (section 4) | LLM-assisted coding, `coding_source_v2 = claude_llm_v2` (12 Nov 2026) |
| `06_Q4_3_binary-categories` output | Word-list binary codes (section 5) | 06 script |

**Value conventions.** Binary codes use 1 = yes and 0 = no. A blank (NA) means the code does not apply to that person (see each code), never "no".

---

## 1. Who is in each base

These bases explain why the n differs between slides.

| Base | n | Who | Used on |
|---|---|---|---|
| Pasted a conversation | 60 | Everyone with a paste | Coding only |
| Usable conversation | 56 | `convo_usable = 1` | 3B referral, urgent-care and medication groups (54 of these also have complete PANAS) |
| Usable, with their own messages | 50 | `convo_usable = 1` and `n_human_turns >= 1` | Every Part 3A number |
| Sent a follow-up | 30 | Usable, with 2+ participant messages | 3A follow-up slide |
| Complete PANAS before and after | 57 | All 10 items answered at both times | 3B "all participants" numbers |
| Usable, coded, complete PANAS | 54 | Both of the above | 3B referral, urgent-care and medication groups |
| Usable, own messages, complete PANAS | 48 | Usable, `n_human_turns >= 1`, complete PANAS | 3B "shared their own situation" rows and the messages slide |

Not usable (4): pids 7, 20, 40, 57 (not a health conversation, or unreadable). Usable with AI text only and no participant turns (6): pids 4, 13, 17, 33, 41, 54. Three of the 57 people with complete PANAS had a non-usable paste, which is why 57 is larger than 54.

---

## 2. Structure variables (from the 01 split script)

| Variable | Definition |
|---|---|
| `convo_text` | The full paste |
| `human_1` ... `human_13`, `ai_0` ... `ai_13` | Each turn of the conversation. `ai_0` is an AI message that came before the participant's first message |
| `*_n_words`, `*_n_chars` | Length of each turn |
| `*_notes`, `*_correction_note` | Notes from the split check |
| `n_turns` | Total turns |
| `n_human_turns` | Participant turns = messages the participant sent. Used for the 3B messages slide (1, 2, 3, 4 or more) |
| `has_ai_0` | 1 if the paste starts with an AI message |
| `human_total_words`, `ai_total_words`, `human_mean_words` | Word counts across turns |

---

## 3. Version 1 codes (`claude_llm_v1`)

Coded from the conversation turns (HUMAN = participant, AI = chatbot). If a pid has no split turns, coded from the raw paste where the speaker is clear. If the paste is too short, unreadable or not a health conversation, every code is blank and `convo_usable = 0`.

| Variable | Type | Definition |
|---|---|---|
| `convo_usable` | 0/1 | 1 = a readable health information conversation. 0 = not health related, unreadable, or the participant pasted survey questions |

### Participant side (all participant turns)

| Variable | Type | Definition |
|---|---|---|
| `human_mentions_disease` | 0/1 | Names a specific disease, diagnosis or medical condition (diabetes, UTI, migraine, COVID). Symptoms alone (headache, rash, fever, pain, fatigue) do not count. A condition named only by the AI does not count |
| `disease_terms` | text | The condition names the participant used, lowercase, "; "-separated |
| `human_shares_personal` | 0/1 | Describes a specific real situation (their own or someone else's symptoms, history, test results, medications, age or sex in context). 0 = only general questions. Shown on 3B as "shared their own situation" vs. "did not share their own situation" |
| `human_asks_med` | 0/1 | Asks about, or names, a specific medication (Rx or OTC, brand or generic). A drug class alone ("antibiotics") counts only if they ask whether to take one. Shown on 3A as "About a specific medication" |
| `human_first_intent` | category | Main purpose of the first participant message, one of: `symptom_interpretation`, `condition_info`, `medication_info`, `care_decision`, `self_management`, `other` |

### AI side (all AI turns, including `ai_0`)

| Variable | Type | Definition |
|---|---|---|
| `ai_meds_named` | text | Distinct specific medications the AI names, normalized to lowercase generic names (Advil -> ibuprofen, Zepbound -> tirzepatide), "; "-separated. Excludes drug classes, vitamins, supplements and herbals |
| `ai_n_meds` | count | Number of medications in `ai_meds_named` (0 if none) |
| `ai_supplements_named` | text | Vitamins, supplements and herbals the AI names |
| `ai_recommends_med` | 0/1 | AI suggests the person take or try a specific medication ("you could try ibuprofen", "ask your doctor about X"). Naming a drug only to explain, warn against, or list what a doctor might prescribe = 0 |
| `ai_refers_professional` | 0/1 | AI advises seeing or talking to a doctor, pharmacist, nurse or other provider |
| `ai_urgent_care` | 0/1 | AI advises urgent care, the ER or 911, or "urgent medical attention", or lists red-flag symptoms that need urgent care |
| `ai_followup_question` | 0/1 | AI asks the participant at least one clarifying question about their situation. Offers of more help ("Want me to...?") = 0 |
| `ai_disclaimer` | 0/1 | AI says it is not a doctor, not medical advice, or for information only |

### Coder fields

| Variable | Definition |
|---|---|
| `coder_confidence` | high / medium / low for the pid overall |
| `coder_note` | One short sentence on anything uncertain (no personal details quoted) |
| `coding_source` | `claude_llm_v1` |

**Rules settled across coders (v1):** vaccines are not medications; vitamins and supplements are listed separately and not counted as medications; urgent care requires explicit urgent care, ER, emergency, 911 or "urgent medical attention/help".

---

## 4. Version 2 codes, participant side (`claude_llm_v2`)

Coded only for the 50 usable conversations with at least one participant turn; blank for everyone else. Each "asks" code looks across all participant turns, so one person can have several (12 of 50 asked more than one kind).

| Variable | Type | Definition |
|---|---|---|
| `human_about` | category | Who the question is about: `self`; `other_person` (a named or described other person, such as a husband, son or daughter); `general` (no specific person, for example "what is diabetes"). Third-person descriptions with no other person named are coded `self` (see `coder_note_v2`) |
| `human_health_area` | category | Main health area, one per conversation: `pain_muscles_bones`, `digestive`, `skin_allergy` (skin, hair, allergic reactions), `cold_flu_infection`, `diet_fitness_weight` (including supplements), `mental_health_sleep`, `diabetes_hormones`, `eyes`, `other` (chest pain, headache, fatigue, kidney or test reports, surgery recovery) |
| `human_asks_cause` | 0/1 | Asks what is causing something, what it could be, or whether it is normal or serious (including asking the AI to interpret a test result) |
| `human_asks_treatment` | 0/1 | Asks what to do, take, eat or change to treat or manage something |
| `human_asks_care` | 0/1 | Asks whether or where to get care, which specialist or test, or what a visit involves |
| `human_asks_condition_info` | 0/1 | Asks for general information about a condition ("what is X", "does X grow"). Medication questions stay in `human_asks_med` |
| `human_pushback` | 0/1 | (2+ participant turns only) Corrects the AI, says it missed something, or asks it to reconsider. Blank for one-turn chats |
| `human_followup_adds_detail` | 0/1 | (2+ turns only) A later message adds symptoms, history or context |
| `human_followup_new_question` | 0/1 | (2+ turns only) A later message asks a new or deeper question |
| `human_expresses_worry` | 0/1 | States worry, fear, stress, frustration or distress in their own words |
| `coder_note_v2` | text | Short note on borderline calls |
| `coding_source_v2` | text | `claude_llm_v2` |

---

## 5. Word-list binary codes (06 script)

The 06 script builds these from the turn text with word lists (all editable in the script). They are a rule-based cross-check on the LLM codes and feed the 07 report.

| Variable | Type | Definition |
|---|---|---|
| `human_mentions_disease` (06 version) | 0/1 | Any participant turn matches the disease list (`DISEASE_TERMS`, capital-only `DISEASE_ACRONYMS`, medical suffixes such as -itis and -osis with `SUFFIX_EXCLUDE`, and head words such as "infection" or "deficiency"). Blank if the participant wrote nothing |
| `human_multi_turn` | 0/1 | More than one participant turn (`n_human_turns > 1`). Blank if no participant turns |
| `ai_multi_med` | 0/1 | AI names 2+ distinct medications. Blank if the AI named none. Medication names are normalized to generics (for example ozempic, wegovy and rybelsus -> semaglutide; mounjaro and zepbound -> tirzepatide) |
| `human_1_long` | 0/1 | First participant message is longer than the median (18.5 words). Blank if no first message |
| `human_1_n_words_coded` | count | Words in the first participant message, used for `human_1_long` |
| Audit columns | | `human_disease_terms`, `ai_med_names`, `ai_n_meds`, `ai_any_med`, `human_1_length`: the matches behind each code, for checking |

---

## 6. Groupings used on the slides and in the 07 report

These are built in the 07 and 08a/08b scripts from the codes and survey answers above.

| Grouping | Rule | Where |
|---|---|---|
| Asked more than one kind of question | 2+ of `human_asks_cause`, `_treatment`, `_condition_info`, `_care`, `human_asks_med` | 3A question-types footer (24%) |
| Everyday complaints | `human_health_area` is pain_muscles_bones, skin_allergy, diet_fitness_weight, digestive or cold_flu_infection | 3A health-topic footer (64%) |
| AI named a medication | `ai_n_meds >= 1` | 3A "How the AI answered" (40%) |
| Referred without asking about care | `ai_refers_professional = 1` among `human_asks_care = 0` | 3A footer (79%, 33 of 42) |
| Named a drug the person had not asked about | `human_asks_med = 0` among `ai_n_meds >= 1` | 3A footer (70%, 14 of 20) |
| Negative affect (distress), positive affect | Sum of the 10 PANAS negative (or positive) items, each 1 to 5, so 10 to 50. Scored only when all 10 items are answered | 3B |
| Change | After minus before | 3B |
| Felt calmer / about the same / more distressed | Negative affect fell 5+ points / changed by less than 5 / rose 5+ points | 3B waffle |
| Messages sent | `n_human_turns`: 1, 2, 3, 4 or more | 3B messages slide |
| Recalled recommendation (survey item E2, `action_ai_rec_self` or `_other`) | 5-6 = clear or strong; 3-4 = gentle suggestion or options; 1-2 = no action or wait it out | 3B recall slide |
| First-message intent (07) | symptom_interpretation; self_management; everything else = other questions | 07 |
| Topic (07, survey) | Diagnosed condition / undiagnosed symptom / general wellness or medication | 07 |
| Condition duration (07, survey) | Under a month / a month or longer | 07 |
| Prior knowledge (07, survey) | Nothing or a little / moderate or more | 07 |
| Chatbot (07, survey) | ChatGPT / other chatbot ("can't remember" left out) | 07 |

Group comparisons are tested only when every group has at least 5 people. Benjamini-Hochberg correction is applied across all 16 segments within each outcome (07) or across the 20 question-by-response pairings (3A referral slide).
