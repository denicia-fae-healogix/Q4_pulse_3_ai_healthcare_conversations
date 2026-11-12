"""Turns the private coded conversation file into the PUBLIC summary used by build_part3b.py.

Run this on your own computer only, pointing it at the private file (it never leaves your machine):
    python build/export_part3b_summary.py "C:/path/to/05_Q4_3_conversations_wide_deid_coded_v2.csv"

It writes data/public/part3b_summary.json, which holds counts only: no pids, no conversation text.
"""
import json, sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if len(sys.argv) != 2:
    sys.exit("Usage: python build/export_part3b_summary.py <path to 05_Q4_3_conversations_wide_deid_coded_v2.csv>")

d = pd.read_csv(sys.argv[1], encoding="utf-8-sig")
pp = d[d.coding_source_v2.notna()].copy()          # 50 people whose paste included their own messages
multi = pp[pp.n_human_turns > 1]                    # sent 2+ messages

def cnt(col, frame):
    s = frame[col].dropna()
    return [int((s == 1).sum()), int(len(s))]

ASKS = ["human_asks_cause", "human_asks_treatment", "human_asks_condition_info", "human_asks_care", "human_asks_med"]
FOLLOW = ["human_followup_adds_detail", "human_followup_new_question", "human_pushback"]

def referral(mask):
    g = pp[mask]
    return [int((g.ai_refers_professional == 1).sum()), int(len(g))]

out = {
    "N": int(len(pp)),
    "n_multi": int(len(multi)),
    "about": {k: int((pp.human_about == k).sum()) for k in ["self", "other_person", "general"]},
    "asks": {c: cnt(c, pp) for c in ASKS},
    "n_more_than_one_kind": int((pp[ASKS].sum(axis=1) > 1).sum()),
    "health_area": {k: int(v) for k, v in pp.human_health_area.value_counts().items()},
    "followup": {c: cnt(c, multi) for c in FOLLOW},
    "referral_by_asked_cause": {"asked": referral(pp.human_asks_cause == 1),
                                "did_not_ask": referral(pp.human_asks_cause == 0)},
}
dest = ROOT / "data" / "public" / "part3b_summary.json"
dest.write_text(json.dumps(out, indent=1), encoding="utf-8")
print("Wrote", dest)
print(json.dumps(out, indent=1))
