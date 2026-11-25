"""Aggregates only (no pids, no text) for the Part 3B "when people asked this, what did the AI say?" chart (codebook section 10).
Usage: python build/export_ask_vs_ai_summary.py <12_Q4_3_ai_response_coded.csv> <05_Q4_3_conversations_wide_deid_coded_v3.csv> <part3b_summary.json>
Writes the "ask_vs_ai" key. Base: the 50 with a usable chat and their own messages (the Part 3A base)."""
import json, sys, pandas as pd
codes_f, v3_f, out_f = sys.argv[1:4]
a = pd.read_csv(codes_f); c = pd.read_csv(v3_f, encoding="utf-8-sig")
b = c.merge(a, on="pid"); b = b[(b.convo_usable == 1) & (b.n_human_turns >= 1)]
Q = [("human_asks_what_cause", "What is causing it"), ("human_asks_treatment", "How to treat it"), ("human_asks_condition_info", "About a condition"),
     ("human_asks_care", "Whether or where to get care"), ("human_asks_serious", "Whether it is serious"), ("human_asks_med", "About a medication"),
     ("human_asks_test_result", "What a test result means")]
A = [("ai_causes", "Gave possible causes"), ("ai_info", "Explained the condition"), ("ai_serious", "Said whether it was serious"), ("ai_self", "Suggested self-care steps"),
     ("ai_recommends_med", "Recommended a medication"), ("ai_refers_professional", "Referred to a professional"), ("ai_urgent_care", "Flagged urgent or ER care"),
     ("ai_test", "Interpreted a test result")]
MATCH = {0: [0], 1: [3, 4], 2: [1], 3: [5], 4: [2], 5: [4], 6: [7]}   # row index -> matching column indices
s = {"N": int(len(b)), "cols": [l for _, l in A], "match": MATCH,
     "rows": [{"label": l, "n": int((b[q] == 1).sum()), "cells": [int(b.loc[b[q] == 1, k].sum()) for k, _ in A]} for q, l in Q],
     "all": [int(b[k].sum()) for k, _ in A]}
d = json.load(open(out_f, encoding="utf-8")); d["ask_vs_ai"] = s
json.dump(d, open(out_f, "w", encoding="utf-8"), indent=1); print(json.dumps(s))
