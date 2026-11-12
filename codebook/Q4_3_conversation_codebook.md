# Q4 Pulse 3 conversation codebook (one row per pid)

Code from the conversation turns (HUMAN = participant, AI = chatbot). Use 1 = yes, 0 = no.
If a pid has no split turns, code from the raw paste where you can tell who said what; if the paste is
too short, unreadable, or not a health conversation, set every code to null and explain in coder_note.

## Participant (HUMAN turns, all of them)
- human_mentions_disease: participant names a specific disease, diagnosis or medical condition
  (e.g. diabetes, UTI, migraine, anxiety disorder, COVID). Symptoms alone (headache, rash, fever, pain,
  fatigue) do NOT count. A condition named only by the AI does NOT count.
- disease_terms: the condition names the participant used, lowercase, "; "-separated ("" if none).
- human_shares_personal: participant describes a specific real situation (their own or someone's
  symptoms, history, test results, medications they take, age/sex in context). 0 = only general questions.
- human_asks_med: participant asks about, or names, a specific medication or drug (Rx or OTC, brand or
  generic). Drug classes alone ("antibiotics") count only if they ask whether to take one.
- human_first_intent: main purpose of the FIRST participant message, exactly one of:
  symptom_interpretation (what is causing X / is this normal or serious),
  condition_info (learn about a disease or diagnosis),
  medication_info (dosing, side effects, interactions, which drug, how a drug works),
  care_decision (whether/where to seek care, which test or doctor),
  self_management (how to treat/manage at home, diet, exercise, lifestyle),
  other.

## AI (all AI turns, including ai_0)
- ai_meds_named: distinct specific medications the AI names (Rx or OTC), normalized to lowercase generic
  names (Advil -> ibuprofen, Tylenol -> acetaminophen), "; "-separated. Exclude drug classes
  ("antibiotics", "NSAIDs"), vitamins, supplements and herbal products (list those in ai_supplements_named).
- ai_n_meds: count of ai_meds_named (0 if none).
- ai_supplements_named: vitamins/supplements/herbals named by the AI, "; "-separated ("" if none).
- ai_recommends_med: AI suggests the participant (or the person) take or try a specific medication
  (including "you could try ibuprofen" or "ask your doctor about X"). Mentions only to explain, warn
  against, or list what a doctor might prescribe in general = 0.
- ai_refers_professional: AI advises seeing or talking to a doctor, pharmacist, nurse or other provider.
- ai_urgent_care: AI advises urgent care, the ER or 911, or lists red-flag symptoms that need urgent care.
- ai_followup_question: AI asks the participant at least one question back (to clarify or tailor).
- ai_disclaimer: AI states it is not a doctor / not medical advice / for information only.

## Also
- coder_confidence: high / medium / low (overall for this pid).
- coder_note: one short sentence on anything uncertain. Do NOT quote personal details.

## Version 2 additions: participant side (claude_llm_v2, 12 Nov 2026)
File: `05_Q4_3_conversations_wide_deid_coded_v2.csv` (all v1 columns plus the columns below).
Coded only for usable conversations with at least one participant turn (50 pids); all others are blank.
Each "asks" code looks across ALL participant turns, so one person can have several.

- human_about: who the question is about, one of self / other_person (a named or described other person,
  e.g. husband, son, daughter) / general (no specific person, e.g. "what is diabetes"). Third-person
  descriptions with no other person named are coded self (see coder_note_v2).
- human_health_area: main health area, one of pain_muscles_bones, digestive, skin_allergy (skin, hair,
  allergic reactions), cold_flu_infection, diet_fitness_weight (incl. supplements), mental_health_sleep,
  diabetes_hormones, eyes, other (chest pain, headache, fatigue, kidney or test reports, surgery recovery).
- human_asks_cause: asks what is causing something, what it could be, or whether it is normal or serious
  (incl. asking the AI to interpret a test result).
- human_asks_treatment: asks what to do, take, eat or change to treat or manage something.
- human_asks_care: asks whether or where to get care, which specialist or test, or what a visit involves.
- human_asks_condition_info: asks for general information about a condition ("what is X", "does X grow").
  (Medication questions stay in the v1 code human_asks_med.)
- human_pushback: (2+ participant turns only) corrects the AI, says it missed something, or asks it to
  reconsider ("still think it's the flu?"). Blank for one-turn chats.
- human_followup_adds_detail: (2+ turns only) a later message adds symptoms, history or context.
- human_followup_new_question: (2+ turns only) a later message asks a new or deeper question.
- human_expresses_worry: participant states worry, fear, stress, frustration or distress in their own words.
- coder_note_v2: short note on borderline calls (no quotes of personal details).
