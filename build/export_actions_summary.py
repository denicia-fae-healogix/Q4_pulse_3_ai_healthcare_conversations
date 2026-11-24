"""Aggregates only (no pids, no text) for the Part 3B "what happened next" slides (codebook section 9).
Usage: python build/export_actions_summary.py <11_Q4_3_actions_coded.csv> <05_Q4_3_conversations_wide_deid_coded_v3.csv> <part3b_summary.json>
Writes the "after_chat" key into data/public/part3b_summary.json.
Base: the 50 with a usable chat and their own messages (the Part 3A base). Following the AI's advice: the 42 of them
whose advice could be compared (no_clear_advice and cant_tell left out)."""
import json, sys, pandas as pd
codes_f, v3_f, out_f = sys.argv[1:4]
a = pd.read_csv(codes_f); c = pd.read_csv(v3_f, encoding="utf-8-sig")[["pid", "convo_usable", "n_human_turns", "ai_refers_professional"]]
b = a.merge(c, on="pid"); b = b[(b.convo_usable == 1) & (b.n_human_turns >= 1)].copy()
def main(r):   # each person counted once, by the biggest step they took
    if r.act_care_done: return "done"
    if r.act_care_planned: return "planned"
    if r.act_med or r.act_self_care or r.act_avoided or r.act_monitored: return "own"
    if r.act_more_info or r.act_shared or r.act_decided_no_care: return "info_or_no_care"
    return "nothing"
b["main"] = b.apply(main, axis=1)
CODES = ["care_done", "care_planned", "decided_no_care", "self_care", "med", "monitored", "avoided", "more_info", "shared", "nothing"]
s = {"N": int(len(b)),
     "main": {k: int((b.main == k).sum()) for k in ["done", "planned", "own", "info_or_no_care", "nothing"]},
     "mentions": {k: int(b["act_" + k].sum()) for k in CODES}}
# medication recommended by the AI vs. took one
v = pd.read_csv(v3_f, encoding="utf-8-sig")[["pid", "ai_recommends_med"]]; bm = b.merge(v, on="pid")
s["med_rec_took"] = [int(bm[bm.ai_recommends_med == 1].act_med.sum()), int((bm.ai_recommends_med == 1).sum())]
# decision tree: referral -> followed the AI's advice -> main action (3 groups)
k = b[b.act_followed_ai.isin(["followed", "partly", "did_not_follow"])].copy()
k["ref"] = k.ai_refers_professional.map({1: "referred", 0: "not_referred"})
k["act3"] = k.main.map({"done": "care", "planned": "care", "own": "own"}).fillna("nothing_or_other")
s["tree_N"] = int(len(k)); s["tree_left_out"] = int(len(b) - len(k))
s["tree"] = {f"{r}|{f}|{x}": int(n) for (r, f, x), n in k.groupby(["ref", "act_followed_ai", "act3"]).size().items()}
d = json.load(open(out_f, encoding="utf-8")); d["after_chat"] = s
json.dump(d, open(out_f, "w", encoding="utf-8"), indent=1); print(json.dumps(s, indent=1))
