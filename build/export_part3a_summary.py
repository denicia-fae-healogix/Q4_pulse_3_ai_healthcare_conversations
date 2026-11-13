"""Turns the private coded conversation file into the PUBLIC summary used by build_part3a.py (Part 3A: what people asked AI).

Run this on your own computer only, pointing it at the private file (it never leaves your machine):
    python build/export_part3a_summary.py "C:/path/to/05_Q4_3_conversations_wide_deid_coded_v3.csv" "C:/path/to/10_Q4_3_med_asked_vs_recommended.csv"
The second file (drug lists) is optional; it adds the drug-class counts for slide 13.

It updates data/public/part3a_summary.json, which holds counts only: no pids, no conversation text.
Keys written by other exporters (goals, med_pairs) are kept.
"""
import json, sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if len(sys.argv) not in (2, 3):
    sys.exit("Usage: python build/export_part3a_summary.py <05_Q4_3_conversations_wide_deid_coded_v3.csv> [10_Q4_3_med_asked_vs_recommended.csv]")

d = pd.read_csv(sys.argv[1], encoding="utf-8-sig")
if "coding_source_v3" not in d.columns:
    sys.exit("This file has no v3 codes. Use 05_Q4_3_conversations_wide_deid_coded_v3.csv.")
pp = d[d.coding_source_v2.notna()].copy()          # 50 people whose paste included their own messages
multi = pp[pp.n_human_turns > 1]                    # sent 2+ messages

def cnt(col, frame):
    s = frame[col].dropna()
    return [int((s == 1).sum()), int(len(s))]

# The five v2 question types (human_asks_cause = cause, serious or test result combined); slides 4, 10 and 14
ASKS = ["human_asks_cause", "human_asks_treatment", "human_asks_condition_info", "human_asks_care", "human_asks_med"]
# Slide 6: the combined measure split into three (v3)
ASKS6 = ["human_asks_what_cause", "human_asks_treatment", "human_asks_condition_info", "human_asks_care",
         "human_asks_serious", "human_asks_med", "human_asks_test_result"]
# Slide 7: health areas (v3), one conversation can count in several
TOPICS = ["topic_muscles_bones_joints", "topic_diet_fitness_weight", "topic_digestive", "topic_cold_flu_infection",
          "topic_allergy_rash", "topic_diabetes_hormones", "topic_head_nerves", "topic_eyes", "topic_mental_health_sleep",
          "topic_skin_hair", "topic_other"]
EVERYDAY = ["topic_muscles_bones_joints", "topic_diet_fitness_weight", "topic_digestive", "topic_cold_flu_infection",
            "topic_allergy_rash", "topic_skin_hair"]
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
    "asks6": {c: cnt(c, pp) for c in ASKS6},
    "n_more_than_one_kind6": int((pp[ASKS6].sum(axis=1) > 1).sum()),
    "n_cause_and_serious": int(((pp.human_asks_what_cause == 1) & (pp.human_asks_serious == 1)).sum()),
    "topics": {c: cnt(c, pp) for c in TOPICS},
    "n_two_plus_areas": int((pp[TOPICS].sum(axis=1) > 1).sum()),
    "n_everyday": int((pp[EVERYDAY].sum(axis=1) > 0).sum()),
    "followup": {c: cnt(c, multi) for c in FOLLOW},
    "referral_by_asked_cause": {"asked": referral(pp.human_asks_cause == 1),
                                "did_not_ask": referral(pp.human_asks_cause == 0)},
    # How the AI answered, on the same 50 people (Part 3A slide 9 and takeaways)
    "ai": {c: cnt(c, pp) for c in ["ai_refers_professional", "ai_urgent_care", "ai_followup_question",
                                    "ai_recommends_med", "ai_disclaimer"]},
    "ai_named_med": [int((pp.ai_n_meds > 0).sum()), int(pp.ai_n_meds.notna().sum())],
    # Of people who did NOT ask about care, how many the AI referred anyway
    "referred_without_asking_care": referral(pp.human_asks_care == 0),
    # Of chats where the AI named a drug, how many came from people who never asked about one
    "named_med_not_asked": [int(((pp.ai_n_meds > 0) & (pp.human_asks_med == 0)).sum()), int((pp.ai_n_meds > 0).sum())],
}
# Slide 13: % of people who asked about, or were recommended, each drug class (counts only)
DRUG_CLASSES = [("OTC pain relievers", "ibuprofen, Tylenol, naproxen", "ibuprofen|tylenol|acetaminophen|naproxen|diclofenac|aspirin|advil|aleve|motrin"),
                ("Antibiotics", "amoxicillin, Bactrim", "amoxicillin|bactrim|antibiotic|sulfameth"),
                ("Osteoporosis drugs", "Prolia, raloxifene, zoledronic acid", "prolia|denosumab|raloxifene|zoledronic|alendronate"),
                ("Antifungal creams", "clotrimazole", "antifungal|clotrimazole"),
                ("Weight-loss drug", "Zepbound", "zepbound|tirzepatide"),
                ("ADHD drug", "guanfacine", "guanfacine"),
                ("Antihistamines", "Benadryl, Claritin", "benadryl|claritin|diphenhydramine|loratadine"),
                ("Gas relief", "simethicone (Gas-X)", "simethicone|gas-x")]
if len(sys.argv) == 3:
    m = pd.read_csv(sys.argv[2], encoding="utf-8-sig")
    m = m[m.pid.isin(pp.pid)]
    has = lambda col, p: int(m[col].fillna("").str.lower().str.contains(p).sum())
    out["drug_classes"] = [{"class": c, "examples": ex, "asked": has("human_meds_asked", p), "recommended": has("ai_recommended_meds", p)}
                           for c, ex, p in DRUG_CLASSES]

dest = ROOT / "data" / "public" / "part3a_summary.json"
old = json.loads(dest.read_text(encoding="utf-8")) if dest.exists() else {}
old.pop("health_area", None)                         # v2 single main topic, replaced by "topics"
old.update(out)
dest.write_text(json.dumps(old, indent=1), encoding="utf-8")
print("Wrote", dest)
print(json.dumps(out, indent=1))
