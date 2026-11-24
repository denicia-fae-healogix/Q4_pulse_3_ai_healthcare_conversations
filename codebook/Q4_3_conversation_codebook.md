# Q4 Pulse 3 codebook: AI health conversations

One row per participant (`pid`). This codebook covers every variable that was coded or derived from the pasted conversations, plus the groupings built from them for the decks, web pages and the 07 report.

**Files**

| File | What it holds | Made by |
|---|---|---|
| `05_Q4_3_conversations_wide_deid.csv` | Survey answers and PANAS, plus the split conversation turns | 00 and 01 scripts |
| `05_Q4_3_conversations_wide_deid_coded.csv` | v1 codes (section 3) | LLM-assisted coding, `coding_source = claude_llm_v1` (11 Nov 2026) |
| `05_Q4_3_conversations_wide_deid_coded_v2.csv` | v1 codes plus v2 participant codes (section 4) | LLM-assisted coding, `coding_source_v2 = claude_llm_v2` (12 Nov 2026) |
| `05_Q4_3_conversations_wide_deid_coded_v3.csv` | v2 file plus v3 codes (section 4b). Only adds columns, so it replaces v2 in every script | LLM-assisted coding, `coding_source_v3 = claude_llm_v3` (13 Nov 2026) |
| `06_Q4_3_binary-categories` output | Word-list binary codes (section 5) | 06 script |
| `11_Q4_3_actions_coded.csv` | What people did after the chat and whether they followed the AI's advice (section 9) | LLM-assisted coding, reviewed by Denicia (24 Nov 2026) |

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
| `human_health_area` | category | (Kept for reference; the slides now use the v3 `topic_*` codes in section 4b.) Main health area, one per conversation: `pain_muscles_bones`, `digestive`, `skin_allergy` (skin, hair, allergic reactions), `cold_flu_infection`, `diet_fitness_weight` (including supplements), `mental_health_sleep`, `diabetes_hormones`, `eyes`, `other` (chest pain, headache, fatigue, kidney or test reports, surgery recovery) |
| `human_asks_cause` | 0/1 | Asks what is causing something, what it could be, or whether it is normal or serious (including asking the AI to interpret a test result). This combined measure equals 1 when any of the three v3 codes `human_asks_what_cause`, `human_asks_serious` or `human_asks_test_result` is 1 (52%). Used on 3A slide 9 and in the goals comparisons |
| `human_asks_treatment` | 0/1 | Asks what to do, take, eat or change to treat or manage something |
| `human_asks_care` | 0/1 | Asks whether or where to get care, which specialist or test, or what a visit involves |
| `human_asks_condition_info` | 0/1 | Asks for general information about a condition ("what is X", "does X grow"). Medication questions stay in `human_asks_med` |
| `human_pushback` | 0/1 | (2+ participant turns only) Corrects the AI, says it missed something, or asks it to reconsider. Blank for one-turn chats |
| `human_followup_adds_detail` | 0/1 | (2+ turns only) A later message adds symptoms, history or context |
| `human_followup_new_question` | 0/1 | (2+ turns only) A later message asks a new question (a new topic or a more specific follow-up) |
| `human_expresses_worry` | 0/1 | States worry, fear, stress, frustration or distress in their own words |
| `coder_note_v2` | text | Short note on borderline calls |
| `coding_source_v2` | text | `claude_llm_v2` |

---

## 4b. Version 3 codes, participant side (`claude_llm_v3`)

Added 13 Nov 2026 after review of the Part 3A deck. Coded for the same 50 usable conversations with at least one participant turn; blank for everyone else. Each code looks across all participant turns.

**Question types.** The combined `human_asks_cause` is split into three, because asking what is causing a symptom and asking whether it is serious are different questions. One person can have several.

| Variable | Type | Definition | Share |
|---|---|---|---|
| `human_asks_what_cause` | 0/1 | Asks what is causing a symptom or what it could be ("why is my foot hurting", "what could this be") | 46% (23) |
| `human_asks_serious` | 0/1 | Asks whether something is normal, typical, serious or worth worrying about | 12% (6) |
| `human_asks_test_result` | 0/1 | Asks the AI to explain a test result, lab value or report (for example an A1c value or a scan report) | 6% (3) |

The three together reproduce `human_asks_cause` exactly. 5 people (10%) asked both what was causing a symptom and whether it was serious.

**Health areas.** Replaces the single `human_health_area` on the slides. A conversation counts in every area the person asked about (4 people, 8%, covered two or more). Pain is a symptom, not an area, so it is counted under the body area it affects (stomach pain under digestion, nerve pain under head and nerves, chest pain under other).

| Variable | Type | Covers | Share |
|---|---|---|---|
| `topic_muscles_bones_joints` | 0/1 | Joint, back, neck and foot pain, bone density, osteoarthritis, sports injuries | 20% (10) |
| `topic_diet_fitness_weight` | 0/1 | Weight loss, diet and nutrition, exercise, supplements | 12% (6) |
| `topic_digestive` | 0/1 | Stomach pain and cramps, diarrhea, gas, bowel problems | 12% (6) |
| `topic_cold_flu_infection` | 0/1 | Colds, flu, sore throat, fever, infections (including an abscess and a yeast skin infection) | 10% (5) |
| `topic_allergy_rash` | 0/1 | Allergic and drug reactions, hives, rashes, eczema | 10% (5) |
| `topic_diabetes_hormones` | 0/1 | Diabetes and A1c, hormones, PCOS, testosterone | 10% (5) |
| `topic_head_nerves` | 0/1 | Headaches, nerve pain | 6% (3) |
| `topic_eyes` | 0/1 | Vision problems, eye surgery | 6% (3) |
| `topic_mental_health_sleep` | 0/1 | Stress, anxiety, sleep, ADHD | 6% (3) |
| `topic_skin_hair` | 0/1 | Scalp, dandruff, hair loss (not rashes or allergies) | 4% (2) |
| `topic_other` | 0/1 | Heart and lungs (chest pain), kidneys and liver, fatigue, recovery after surgery | 12% (6) |
| `topic_skin_rash_allergy` | 0/1 | Made in 08a and the web export, not stored in the coded file: 1 if `topic_skin_hair` or `topic_allergy_rash` is 1. Shown on the slides as "Skin, rashes and allergies" (Nov 2026 review; no one had both) | 14% (7) |
| `coding_source_v3` | text | `claude_llm_v3` | |

On the slides (Nov 2026 review), skin and hair and allergies and rashes are shown as one area, "Skin, rashes and allergies", so the deck and web page show 10 areas. The two original codes stay in the coded file.

Coding calls worth knowing: eczema and the yeast skin infection count under allergies and rashes (the yeast infection also under infections); the abscess counts as an infection; the A1c chat counts under diabetes and as a test-result question; chest pain counts under other.

**Area text.** The symptoms and medications listed for each area (the slide 4 hovers, and a table slide cut in the Nov 2026 review) are a hand summary written while coding (aggregate wording only). It lists any drug named in the chat, whether suggested, explained or warned against, so it differs from `ai_recommends_med` and the slide 10 drug list. The same text lives in `AREA_DETAIL` (08a) and `AREAS` (build_part3a.py).

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
| Asked more than one kind of question | 2+ of `human_asks_what_cause`, `_treatment`, `_condition_info`, `_care`, `_serious`, `human_asks_med`, `_test_result` | 3A slide 5 footer (28%) |
| Asked both cause and serious | `human_asks_what_cause = 1` and `human_asks_serious = 1` | 3A slide 5 footer (10%) |
| Asked what was causing it, or whether it was serious (combined) | `human_asks_cause = 1` (any of the three v3 cause codes) | 3A slide 9 (52%) |
| Everyday complaints | Any of `topic_muscles_bones_joints`, `topic_skin_rash_allergy`, `topic_diet_fitness_weight`, `topic_digestive`, `topic_cold_flu_infection` | 3A slide 4 footer (64%) |
| Asked about two or more areas | 2+ of the 10 areas shown | 3A slide 4 footer (8%) |
| Drug class (cut slide) | Word match in `human_meds_asked` and `ai_recommended_meds` (section 8): OTC pain relievers, antibiotics, osteoporosis drugs, antifungal creams, weight-loss drug, ADHD drug, antihistamines, gas relief | Cut in the Nov 2026 review; still in 08a |
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

Group comparisons are tested only when every group has at least 5 people. Benjamini-Hochberg correction is applied across all 16 segments within each outcome (07) or across the 20 question-by-response pairings (3A referral slide). The referral tests keep the five v2 question types, with the combined `human_asks_cause`, so the 20 pairings are unchanged.

---

## 7. Goal codes (`claude_llm_goals_v1`)

Coded from the survey question C3 (`convo_goal_oe`): "When starting the conversation you just provided, what was your goal?" File: `09_Q4_3_goals_coded.csv` (pid plus codes, no text). Coded 13 Nov 2026 for all 60 people who answered.

**Standing rule: code what the person wrote in their goal answer, not what they later typed in the chat.** The chat was read only once (pid 45) to tell what "drink" referred to. Goal types are multi-label: one person can have several.

| Variable | Type | Definition |
|---|---|---|
| `goal_cause` | 0/1 | Wanted to find out what is wrong, what is causing it, whether it is normal or serious, or what a test result means |
| `goal_treatment` | 0/1 | Wanted to know how to treat, relieve, manage or improve something (home remedies, a plan, what to take when no drug is named, supplements) |
| `goal_care` | 0/1 | Wanted to decide whether, when or where to get care (doctor, ER, urgent care, specialist, a surgery decision, where to get a vaccine) or what a visit involves |
| `goal_condition_info` | 0/1 | Wanted general knowledge about a condition or topic (how common, who it affects, outlook), not about their own symptoms specifically |
| `goal_med` | 0/1 | Asked about a specific medication or which OTC product to take. Drug classes alone, vitamins, supplements and vaccines do not count (same rules as section 3) |
| `goal_prepare_visit` | 0/1 | Wanted to get ready for a planned visit or conversation with a provider (options to discuss, organizing thoughts for a therapist, what to expect) |
| `goal_reassurance` | 0/1 | Wanted reassurance, validation, or to calm down ("so I know it isn't a health scare") |
| `goal_for_other` | 0/1 | The goal is about a specific other person (parent, child, partner, friend) |
| `goal_ai_easier` | 0/1 | Said, unprompted, that AI was quicker, cheaper, easier or less embarrassing than a search or a doctor |
| `goal_worry` | 0/1 | States worry or concern in their own words |
| `goal_health` | 0/1 | 1 = a health goal. 0 = not health related (pid 57, a school essay). Every goal chart uses `goal_health = 1` (n = 59) |
| `goal_primary` | category | The one goal the person led with: `cause`, `treatment`, `care`, `medication`, `condition_info`, `reassurance`, `prepare_visit`, `other` (vague or not a health goal) |
| `goal_n_types` | count | How many of the first seven goal types apply (0 to 7) |
| `goal_coder_confidence`, `goal_coder_note` | text | high / medium / low, and a short note on borderline calls (no quotes) |
| `goal_coding_source` | text | `claude_llm_goals_v1` |

**Was the goal met?** Coded from D2 (`convo_goal_met_oe`), asked after the chat, for all 60.

| Variable | Type | Definition |
|---|---|---|
| `goal_met` | category | `Yes` (says it was met, including "mostly" and "for the most part"), `Partly` (hedged: "partially", "sort of", "in a sense", ongoing, or met only some parts), `No` ("not really", "no", "not at all") |
| `goal_met_reassured` | 0/1 | Says they felt reassured, relieved, calmer, more confident or supported |
| `goal_met_professional` | 0/1 | Brings a doctor or other provider into what came next: saw one, plans to, will if it gets worse, or a doctor confirmed what the AI said |
| `goal_met_acted` | 0/1 | Did, or plans to do, something concrete based on the chat (bought or took something, went to the ER, sent an update, shared the advice) |
| `goal_met_doubt` | 0/1 | Notes a limit of the AI: no clear answer, too much information, it always agrees, or not enough on its own |
| `goal_met_coder_confidence`, `goal_met_coder_note` | text | Confidence and a short note on borderline calls |

The four flags only count what people volunteered, so they are floors. 09b writes `07_Q4_3_goal-met_coding.xlsx` from `goal_met` if that workbook does not exist yet, so the 07 report can use it.

**Check.** The 09b report runs a word-list cross-check on each code and lists the pids where the word list and the coder disagree. After the first review, three codes were changed (pid 17 care, pids 29 and 59 worry).

**Goal met counts (59 health goals).** Yes 50 (85%), Partly 5 (8%), No 4 (7%).

**Bases in 09b.** 59 health goals; 50 of them with a usable chat and their own messages (goal vs. what they asked); 56 with a usable chat (goal vs. how the AI answered); those with complete PANAS (goals and feelings).

---

## 8. Medications asked about vs. recommended (`claude_llm_meds_v1`)

File: `10_Q4_3_med_asked_vs_recommended.csv` (pid plus the columns below, no conversation text). Covers the 50 usable chats with the participant's own messages. Built for the Part 3A slide "Most AI drug recommendations answered a symptom, not a medication question". The 08a report checks these lists against the yes/no codes.

| Variable | Type | Definition |
|---|---|---|
| `human_meds_asked` | text | The drugs the participant named or asked about, generic name with brand in brackets, "; "-separated. Filled exactly when `human_asks_med = 1` (6 people) |
| `ai_recommended_meds` | text | The drugs the AI suggested the person take, try, or ask a doctor about, read from the AI's text. Filled exactly when `ai_recommends_med = 1` (11 people). Drugs the AI only named or explained are in `ai_meds_named`, not here |
| `med_symptom` | text | A short symptom label (headache, knee pain...) for the 8 people who got a recommendation without asking about a drug |
| `med_group` | category | `asked_and_recommended` (3), `asked_only` (3), `recommended_unasked` (8), `neither` (36) |
| `med_coding_source` | text | `claude_llm_meds_v1` |

10 of the 11 recommendations were over-the-counter (the exception: zoledronic acid, suggested as a question for the doctor).

---

## 9. What people did after the chat (`claude_llm_actions_v1`, `claude_llm_followed_ai_v1`)

**Source.** Survey question E1, open-ended: what the person did after the conversation, for themselves (`action_taken_self_oe`) or for the person they asked about (`action_taken_other_oe`). The 11a script combines the two into one answer (`action_taken_oe`, with `action_for` = self or other) and writes `11_Q4_3_actions_deid_pid_only.csv` (pid and answer only). Codes were drafted with LLM assistance and reviewed by Denicia on 24 Nov 2026. The coded file, `11_Q4_3_actions_coded.csv`, holds pid plus the codes and short coder notes, and stays private in `data/processed`.

There are two separate code sets. The action codes describe what the person said they did, read from E1 alone. The followed-the-AI's-advice code compares that answer with what the AI actually recommended in the pasted chat, so it needs the conversation and is coded only for usable chats.

### 9a. Action codes (one or more per person)

Base: 59 health answers (`act_health = 1`; pid 57, an essay, is 0 and has no codes). A person can have more than one code, so the percentages add to more than 100.

| Variable | Type | Definition | n (of 59) |
|---|---|---|---|
| `action_for` | category | `self` or `other` (who the E1 answer was about) | 45 self, 15 other (of 60) |
| `act_care_done` | 0/1 | Saw or contacted a doctor, nurse, pharmacist, PT or other professional, or got a test | 10 (17%) |
| `act_care_planned` | 0/1 | Booked or firmly plans to see a professional, or says they will go if it gets worse | 19 (32%) |
| `act_decided_no_care` | 0/1 | Decided not to see a professional (for example, the chat reassured them, or cost) | 6 (10%) |
| `act_med` | 0/1 | Took, started, stopped or changed a medication | 6 (10%) |
| `act_self_care` | 0/1 | Rest, heat or ice, diet, exercise, stretching, supplements, skincare and other home care | 19 (32%) |
| `act_avoided` | 0/1 | Stopped or avoided something (a food, an activity, a trigger) | 3 (5%) |
| `act_more_info` | 0/1 | Looked for more information (more searching, reading, another AI chat) | 5 (8%) |
| `act_shared` | 0/1 | Talked it over with or passed the information to a family member, partner or friend | 4 (7%) |
| `act_monitored` | 0/1 | Is watching the symptom or tracking it | 5 (8%) |
| `act_nothing` | 0/1 | Did nothing yet or nothing different | 17 (29%) |
| `act_any_care` | 0/1 | Derived: `act_care_done` or `act_care_planned` | 29 (49%) |
| `act_health` | 0/1 | 1 = a health answer included in the base; 0 = pid 57 | 59 |
| `act_coder_note` | text | Short note on close calls | |
| `act_coding_source` | text | `claude_llm_actions_v1` | |

**Decisions.** "Will go if it gets worse" counts as `act_care_planned` (pids 26, 41, 44, 53); pids 26 and 44 also have the code that fits what they did now (`act_nothing`, `act_decided_no_care`). "Followed the AI's advice" is not an action and is coded separately (9b). An earlier "problem went away" code was dropped because it is an outcome, not an action. Pid 1 (plans to call her insurer about her medication) is coded `act_care_planned` as the closest fit. Pid 32 said only that they listened to the AI and its advice worked; the AI's main advice was to take acetaminophen or ibuprofen for a headache, so pid 32 is coded `act_med` (inferred from their statement that they followed the advice, the one action code not read from E1 alone).

**Early results (on the 50 base, usable chat with their own messages).** People the AI referred to a professional were much more likely to see or plan to see one: 24 of 40 vs. 1 of 10 not referred (Fisher p = .011). Of the 11 people the AI recommended a medication to, 2 took one (pids 32 and 35).

### 9b. Followed the AI's advice (one per person)

Base: 56 usable chats (`convo_usable = 1`); blank for pids 7, 20, 40, 57. Coded by comparing E1 with the AI's main recommendation. A firm plan (for example, an appointment already booked) counts as following the advice; a vague "maybe if it gets worse" does not.

| Variable | Type | Values | n (of 56) |
|---|---|---|---|
| `act_followed_ai` | category | `followed`: did what the AI mainly recommended | 36 |
| | | `partly`: did some of it but not the main step (often the lighter advice without the referral) | 9 |
| | | `did_not_follow`: did not do what the AI recommended | 2 |
| | | `no_clear_advice`: the AI mainly listened or explained and gave nothing to act on | 6 |
| | | `cant_tell`: E1 or the available AI text is not enough to judge | 3 |
| `act_followed_ai_note` | text | Note on close calls (pids 1, 6, 8, 9, 23, 26, 28, 29, 30, 31, 33, 36, 46, 47, 58, 59) | |
| `act_followed_ai_source` | text | `claude_llm_followed_ai_v1` | |
| `act_reviewed` | text | Reviewer and date for both code sets | |

Of the 47 people who could be compared, 77% followed the AI's advice, 19% partly followed it and 4% did not. Everyone who partly followed or did not follow had been referred to a professional (referred 39: 28 followed, 9 partly, 2 did not; not referred 8: all followed).

**Close calls (reviewed and kept).** Pid 1 partly (plans to call her insurer, not yet the doctor); pid 9 partly (rested, but still in pain at 4 weeks without the sports doctor or PT visit the AI advised); pid 26 did not follow (the AI advised an in-person evaluation soon; she will go only if needed); pid 31 partly (the AI said go to the ER now; the friend made an appointment); pid 46 partly (used heat, but assumed it was from sleeping wrong, which the AI warned against); pid 58 followed (the AI said a second cataract surgery is not automatically needed, and she cancelled); pid 29 can't tell (the available AI text covers shot side effects, not whether it advised the flu shot); pid 6 partly and pid 8 no clear advice (the AI mainly listened or explained).
