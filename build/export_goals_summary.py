"""Aggregates only (no pids, no text) for the Part 3A goal slides. Same numbers as 09b."""
import json, sys, pandas as pd
codes_f, v2_f, out_f = sys.argv[1:4]
g = pd.read_csv(codes_f); c = pd.read_csv(v2_f, encoding="utf-8-sig")
h = g[g.goal_health == 1]
TYPES = ["goal_cause", "goal_treatment", "goal_care", "goal_condition_info", "goal_med", "goal_prepare_visit", "goal_reassurance"]
s = {"N": int(len(h)),
     "types": {t: int(h[t].sum()) for t in TYPES},
     "two_plus": int((h.goal_n_types >= 2).sum()),
     "for_other": int(h.goal_for_other.sum()), "ai_easier": int(h.goal_ai_easier.sum()),
     "met": {k: int((h.goal_met == k).sum()) for k in ["Yes", "Partly", "No"]},
     "met_flags": {k: int(h[k].sum()) for k in ["goal_met_reassured", "goal_met_professional", "goal_met_acted", "goal_met_doubt"]},
     "met_by_type": {t: [int((h[h[t] == 1].goal_met == "Yes").sum()), int((h[t] == 1).sum())] for t in TYPES}}
m = h.merge(c, on="pid"); v = m[m.coding_source_v2.notna()]
PAIRS = {"goal_cause": "human_asks_cause", "goal_treatment": "human_asks_treatment", "goal_care": "human_asks_care",
         "goal_condition_info": "human_asks_condition_info", "goal_med": "human_asks_med"}
s["N_asked"] = int(len(v))
s["goal_vs_asked"] = {gk: [int(v[gk].sum()), int(v[a].sum())] for gk, a in PAIRS.items()}
main = {"cause": "human_asks_cause", "treatment": "human_asks_treatment", "care": "human_asks_care", "condition_info": "human_asks_condition_info", "medication": "human_asks_med"}
vv = v[v.goal_primary.isin(main)].copy()
vv["asked_own"] = [r[main[r.goal_primary]] for _, r in vv.iterrows()]
s["met_by_asked_own"] = {"asked": [int(((vv.asked_own == 1) & (vv.goal_met == "Yes")).sum()), int((vv.asked_own == 1).sum())],
                         "did_not_ask": [int(((vv.asked_own == 0) & (vv.goal_met == "Yes")).sum()), int((vv.asked_own == 0).sum())]}
json.dump(s, open(out_f, "w"), indent=1); print(json.dumps(s))
