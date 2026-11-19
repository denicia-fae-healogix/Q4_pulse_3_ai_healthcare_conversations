"""Aggregates only (no pids, no text) for the Part 3A goal slides. Same numbers as 09b.
Usage: python build/export_goals_summary.py <09_Q4_3_goals_coded.csv> <05_Q4_3_conversations_wide_deid_coded_v3.csv> <out.json>
then copy the printed object into the "goals" key of data/public/part3a_summary.json."""
import json, sys, pandas as pd
codes_f, v2_f, out_f = sys.argv[1:4]
g = pd.read_csv(codes_f); c = pd.read_csv(v2_f, encoding="utf-8-sig")
h = g[g.goal_health == 1]
# Nov 2026 review: goal_cause was split into goal_what_cause, goal_serious and goal_test_result (codebook section 7),
# so each goal type matches the question type of the same name on deck slide 5. Listed in the slide 5 order.
TYPES = ["goal_what_cause", "goal_treatment", "goal_condition_info", "goal_care", "goal_serious", "goal_med", "goal_test_result",
         "goal_reassurance", "goal_prepare_visit"]
s = {"N": int(len(h)),
     "types": {t: int(h[t].sum()) for t in TYPES},
     "two_plus": int((h.goal_n_types >= 2).sum()),
     "for_other": int(h.goal_for_other.sum()), "ai_easier": int(h.goal_ai_easier.sum()),
     "met": {k: int((h.goal_met == k).sum()) for k in ["Yes", "Partly", "No"]},
     "met_flags": {k: int(h[k].sum()) for k in ["goal_met_reassured", "goal_met_professional", "goal_met_acted", "goal_met_doubt"]},
     "met_by_type": {t: [int((h[h[t] == 1].goal_met == "Yes").sum()), int((h[t] == 1).sum())] for t in TYPES}}
m = h.merge(c, on="pid"); v = m[m.coding_source_v2.notna()]
PAIRS = {"goal_what_cause": "human_asks_what_cause", "goal_treatment": "human_asks_treatment", "goal_condition_info": "human_asks_condition_info",
         "goal_care": "human_asks_care", "goal_serious": "human_asks_serious", "goal_med": "human_asks_med", "goal_test_result": "human_asks_test_result"}
GOAL_ONLY = ["goal_reassurance", "goal_prepare_visit"]   # no matching question type: goal share only
s["N_asked"] = int(len(v))
# Nov 2026 review: goal-met results use the same 50 people (health goal + usable chat with own messages) as every other slide
s["met"] = {k: int((v.goal_met == k).sum()) for k in ["Yes", "Partly", "No"]}
s["met_flags"] = {k: int(v[k].sum()) for k in ["goal_met_reassured", "goal_met_professional", "goal_met_acted", "goal_met_doubt"]}
s["met_base"] = "N_asked"
s["goal_vs_asked"] = {gk: [int(v[gk].sum()), int(v[a].sum())] for gk, a in PAIRS.items()}
s["goal_only"] = {gk: int(v[gk].sum()) for gk in GOAL_ONLY}
main = {"what_cause": "human_asks_what_cause", "serious": "human_asks_serious", "test_result": "human_asks_test_result", "treatment": "human_asks_treatment", "care": "human_asks_care", "condition_info": "human_asks_condition_info", "medication": "human_asks_med"}
vv = v[v.goal_primary.isin(main)].copy()
vv["asked_own"] = [r[main[r.goal_primary]] for _, r in vv.iterrows()]
s["met_by_asked_own"] = {"asked": [int(((vv.asked_own == 1) & (vv.goal_met == "Yes")).sum()), int((vv.asked_own == 1).sum())],
                         "did_not_ask": [int(((vv.asked_own == 0) & (vv.goal_met == "Yes")).sum()), int((vv.asked_own == 0).sum())]}
# Slide 11: goal met (Yes/Partly/No) for the same 50 split three ways, so the groups add back to the 50
v = v.copy()
v["grp"] = ["no_match" if gp not in main else ("asked" if r == 1 else "did_not_ask")
            for gp, r in zip(v.goal_primary, [row[main[row.goal_primary]] if row.goal_primary in main else None for _, row in v.iterrows()])]
s["met_by_group"] = {gk: {k: int(((v.grp == gk) & (v.goal_met == k)).sum()) for k in ["Yes", "Partly", "No"]} for gk in ["asked", "did_not_ask", "no_match"]}
json.dump(s, open(out_f, "w"), indent=1); print(json.dumps(s))
