"""Builds part3a/index.html (Part 3A: What did people ask AI?) from data/public/part3a_summary.json.
Run from the repo root:  python build/build_part3a.py
Uses only the public summary file (counts, no respondent IDs or conversation text).
To refresh the counts from the private coded file, run build/export_part3a_summary.py first, on your own computer."""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = json.load(open(ROOT / "data" / "public" / "part3a_summary.json", encoding="utf-8"))
N = D["N"]
N_MULTI = D["n_multi"]
E = html.escape
TIPS = {}

def tip(key, title, stats, quotes=(), note=None, sub="From the conversations"):
    h = f'<p class="tt-title">{E(title)}</p>'
    if stats:
        h += '<dl class="tt-stats">' + "".join(f"<dt>{E(a)}</dt><dd>{E(b)}</dd>" for a, b in stats) + "</dl>"
    if note:
        h += f'<p class="tt-note">{E(note)}</p>'
    if quotes:
        h += f'<p class="tt-sub">{E(sub)}</p>' + "".join(f'<blockquote><span>{E(s)}</span>{E(t)}</blockquote>' for s, t in quotes)
    TIPS[key] = h
    return key

attrs = lambda k: f'data-tip="{k}" tabindex="0" role="button" aria-label="Show details"'
P = lambda t: ("Participant", t)
A = lambda t: ("AI", t)
pct = lambda n, d: round(100 * n / d)
DARK, LIGHT, PALE = "#0b3d68", "#29abe2", "#9DC3E6"
EYEBROW = '<p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>'

def cnt(col):
    """(people coded 1, people coded) for one participant code, from the public summary."""
    return tuple(D["asks"][col])

def sbars(rows, prefix, note):
    """rows: (label, n, N, color, quotes). Bars show percentages only; counts live in the hover box."""
    out = ""
    for i, (lab, n, tot, col, quotes) in enumerate(rows):
        p = 100 * n / tot
        k = tip(f"{prefix}{i}", lab, [("Share", f"{round(p)}%"), ("People", f"{n} of {tot}")], quotes, note)
        out += f"""<div class="sbar" {attrs(k)}><div class="dlab{' b' if col == DARK else ''}">{E(lab)}</div>
          <div class="strack"><span class="sfill" style="width:{p:.2f}%;background:{col}"></span>
          <span class="sval" style="left:{p:.2f}%">{round(p)}%</span></div></div>"""
    return f'<div class="sbars">{out}</div>'

from prior_pulses import prior_slide
slides = []
slides.append(f"""
<section class="slide s-title" id="s1">
  <p class="brand">HEALOGIX</p>
  <p class="kicker">Q4 &middot; November 2026 &middot; Pulse</p>
  <h1>Part 3A: When people turn to AI for health advice, what do they ask?</h1>
  <p class="lede">The Healogix Behavioral Science team collected and coded real AI health chats to see what people asked, how the AI answered, and whether it met their goals.</p>
  <p class="byline">Denicia Aragon Espinosa &amp; James Dunlea, Ph.D.</p>
  <p class="howto">Hover over or tap any chart to see the numbers and examples from the conversations behind it.</p>
</section>""")
slides.append(prior_slide("s1b", "Part 3A looks inside real AI health chats, starting with what people asked. Part 3B covers what the AI said back, and how people felt afterward."))


# Overview callouts (Nov 2026 review), in the order of the slides they link to
pills = [("#a5306d", "Most people asked about an everyday complaint of their own, and nearly half wanted to know its cause", "s6"),
         ("#9b4c96", "About 3 in 10 wanted help deciding about care, but fewer than 2 in 10 asked the AI about it", "s13"),
         ("#8467b6", "People added detail as the chat went on but rarely pushed back", "s7"),
         ("#627fcc", "The AI pointed 4 in 5 people to a professional, most of whom had not asked", "s9"),
         ("#4a8fd0", "When the AI recommended a drug, it was usually OTC and unprompted", "s9b"),
         ("#2f9fd8", f"{round(100 * D['goals']['met']['Yes'] / D['goals']['N_asked'])}% said the chat met the goal they came with", "s14")]
slides.append(f"""
<section class="slide" id="s2">{EYEBROW}
  <h2 class="ov-title">What people ask AI about their health, and how the AI answers</h2>
  <p class="ov-sub">Overview of findings</p>
  <div class="pills">{''.join(f'<a class="pill" style="--pill:{c}" href="#{h}">{E(t)}</a>' for c, t, h in pills)}</div>
  <p class="foot">Online survey via Prolific &middot; Pulse 3 &middot; {N} U.S. adults whose pasted AI health conversation included their own messages</p>
</section>""")

# ---- 3 big numbers (order matches slides 4 and 5) ----
self_n = D["about"]["self"]
cause_n, _ = cnt("human_asks_cause"); med_n, _ = cnt("human_asks_med")
bn = [(f"{pct(self_n, N)}%", DARK, "asked about their own health, not someone else's or general facts",
       tip("b1", "Asked about their own health", [("Share", f"{pct(self_n, N)}%"), ("People", f"{self_n} of {N}")], [P("Why is the top of my foot hurting?"), P("There is no swelling but I do run daily.")])),
      (f"{pct(cause_n, N)}%", "#00a4e4", "asked what was causing a symptom or whether it was serious",
       tip("b2", "Asked what was causing a symptom", [("Share", f"{pct(cause_n, N)}%"), ("People", f"{cause_n} of {N}")], [P("I've been feeling unusually tired lately, even after getting a full night's sleep. What could be causing this?")])),
      (f"{pct(med_n, N)}%", DARK, "asked about a specific medication",
       tip("b3", "Asked about a specific medication", [("Share", f"{pct(med_n, N)}%"), ("People", f"{med_n} of {N}")], [P("I have a headache, what should I take?")],
           "Counts any question that names a specific drug, prescription or over the counter."))]
slides.append(f"""
<section class="slide" id="s3">{EYEBROW}
  <h2 class="big-title">People ask AI about their <em>own</em> bodies</h2>
  <div class="bignums">{''.join(f'<div class="bn" {attrs(k)}><span class="bn-num" style="color:{c}">{n}</span><span class="bn-txt">{E(t)}</span></div>' for n, c, t, k in bn)}</div>
  <p class="foot">Conversations pasted by participants and coded from their own messages &middot; n = {N} participants with at least one message of their own</p>
</section>""")

# ---- 4 who ----
who = [("self", "Themselves", DARK, [P("Why is the top of my foot hurting?")]),
       ("other_person", "Someone else, such as a partner or child", LIGHT, [P("Husband's low back started hurting yesterday.")]),
       ("general", "No one in particular (general questions)", PALE, [P("Does metacarpal bossing grow?"), P("What if hand, foot and mouth isn't treated?")])]
sqs, leg = "", ""
for code, lab, col, qs in who:
    n = D["about"][code]
    k = tip(f"w_{code}", lab, [("Share", f"{pct(n, N)}%"), ("People", f"{n} of {N}")], qs)
    leg += f'<span {attrs(k)} style="padding:4px 8px;border-radius:6px"><i class="lg-sq" style="background:{col}"></i>{E(lab)}: <b>{pct(n, N)}%</b></span>'
    sqs += "".join(f'<i class="sq" style="background:{col}" data-tip="{k}"></i>' for _ in range(n))
slides.append(f"""
<section class="slide" id="s4">{EYEBROW}
  <h2>Most people asked AI about their own health, and 1 in 10 asked on behalf of someone else</h2>
  <p class="chart-title">Who the participant's question was about</p>
  <div class="legend">{leg}</div>
  <div class="wpanels"><div class="wpanel"><div class="waffle w10">{sqs}</div><p class="muted">One square = one participant</p></div></div>
  <p class="foot">Coded from participant messages (n = {N}). Someone else = a named or described other person, such as a partner or child. No one in particular = general questions about a condition or health topic.</p>
</section>""")

# ---- 5 question types (deck slide 6): the combined cause measure split into three (v3 codes), in deck order ----
asks = [("What is causing it", "human_asks_what_cause", [P("Why is the top of my foot hurting?"), P("I have had a headache for 2 days and pain behind my eyes. What could be the problem?")]),
        ("How to treat or manage it", "human_asks_treatment", [P("My scalp is flaking and scabbing. What do I do?"), P("What can I do to alleviate knee pain and get back to normal?")]),
        ("General facts about a condition", "human_asks_condition_info", [P("What is sleep apnea?"), P("Does metacarpal bossing grow?")]),
        ("Whether or where to get care", "human_asks_care", [P("Should I see a medical specialist about this or try to wait it out?"), P("Should I schedule an appointment with a specialist?")]),
        ("Is it normal or serious", "human_asks_serious", [P("Is that typical of the medicine?")]),
        ("About a specific medication", "human_asks_med", [P("I have a headache, what should I take?"), P("How can I tell if I'm having an allergic reaction to antibiotics I started yesterday?")]),
        ("What a test result means", "human_asks_test_result", [P("At a high level, what did these tests show?")])]
rows = []
for i, (lab, col, qs) in enumerate(asks):
    n, tot = D["asks6"][col]
    rows.append((lab, n, tot, DARK if i == 0 else LIGHT, qs))
multi_kind = D["n_more_than_one_kind6"]
slides.append(f"""
<section class="slide" id="s5">{EYEBROW}
  <h2>Within those complaints, nearly half asked what was causing a symptom, and a third asked how to treat it</h2>
  <p class="chart-title">What participants asked the AI, at any point in the chat</p>
  {sbars(rows, "q", "Coded from every participant message. One person can ask more than one kind of question.")}
  <p class="axis-title">% of participants asking a given question type</p>
  <p class="foot">Coded from every participant message (n = {N}). People could ask more than one kind of question ({pct(multi_kind, N)}% did), so bars add up to more than 100%. {pct(D['n_cause_and_serious'], N)}% asked both what was causing a symptom and whether it was serious. The referral slide groups those two ({pct(D['referral_by_asked_cause']['asked'][1], N)}%); test-result questions are not included there.</p>
</section>""")

# ---- 6 health areas (deck slide 7): every area a conversation covered (v3), in deck order with Other last ----
# What people described in each area and which drugs came up: a hand summary written while coding the conversations
# (aggregate wording only). Used for the slide 7 hovers and the slide 8 table. Same text as AREA_DETAIL in 08a.
# Nov 2026 review: "Skin and hair" and "Allergies and rashes" are combined into "Skin, rashes and allergies" (10 areas).
AREAS = [("topic_muscles_bones_joints", "Muscles, bones and joints", "Knee, back, neck, shoulder and foot pain; tennis elbow; fragile bones; osteoarthritis; a bony bump on the hand", "Prolia, raloxifene", "Prolia, alendronate and other bone drugs; steroid shots; ibuprofen, naproxen, diclofenac; Tylenol"),
         ("topic_skin_rash_allergy", "Skin, rashes and allergies", "Hives and itchy bumps, facial swelling after an antibiotic, a burning drug reaction, eczema patches, scalp flaking and dandruff, hair shedding", "Bactrim, amoxicillin, an antifungal cream, Zepbound", "21 antibiotics in one chat; Benadryl, Claritin, epinephrine; antifungal creams; hydrocortisone; dandruff shampoos"),
         ("topic_diet_fitness_weight", "Diet, fitness and weight", "Weight loss, building muscle, healthy foods and protein, supplements, workouts", None, None),
         ("topic_digestive", "Stomach and digestion", "Stomach aches and cramps, diarrhea and gas, pain near the belly button, an anal fistula", None, "Gas-X; ibuprofen, naproxen, aspirin"),
         ("topic_cold_flu_infection", "Colds, flu and infections", "Fever, chills, body aches, congestion, sore throat, hand, foot and mouth disease, an abscess, a yeast skin infection", None, "Tylenol, ibuprofen, Tamiflu"),
         ("topic_diabetes_hormones", "Diabetes and hormones", "Diabetes, A1c results, hormone imbalance, PCOS, testosterone", None, "Insulin, estradiol, progesterone"),
         ("topic_head_nerves", "Head and nerves", "Headaches, vomiting, pain behind the eyes, nerve pain in the leg", None, "Tylenol, ibuprofen; gabapentin, pregabalin, duloxetine; lidocaine"),
         ("topic_eyes", "Eyes", "Double vision, blurry central vision, cataract surgery", None, None),
         ("topic_mental_health_sleep", "Mental health and sleep", "Stress and anxiety, pauses in breathing at night, a child waking at night on an ADHD drug", "Guanfacine", "Guanfacine"),
         ("topic_other", "Other (heart, lungs, kidneys, fatigue)", "Chest pain with coughing up blood, ongoing tiredness, test findings (heart, lungs, liver, kidneys), recovery after surgery", None, "Ibuprofen, naproxen")]
TOPIC = D["topics"]
bars = ""
for i, (code, lab, sym, _, _) in enumerate(AREAS):
    n, tot = TOPIC[code]; p = 100 * n / tot; col = DARK if i == 0 else LIGHT
    k = tip(f"a{i}", lab, [("Share", f"{round(p)}%"), ("People", f"{n} of {tot}")], (),
            "Symptoms people described: " + sym + ".")
    bars += f"""<div class="sbar" {attrs(k)}><div class="dlab{' b' if i == 0 else ''}">{E(lab)}</div>
      <div class="strack"><span class="sfill" style="width:{p:.2f}%;background:{col}"></span><span class="sval" style="left:{p:.2f}%">{round(p)}%</span></div></div>"""
slides.append(f"""
<section class="slide" id="s6">{EYEBROW}
  <h2>Their questions were mostly about everyday complaints, led by muscle, bone and joint pain</h2>
  <p class="chart-title">Areas of health participants asked the AI about</p>
  <div class="sbars">{bars}</div>
  <p class="axis-title">% of participants asking about each area</p>
  <p class="foot">Coded from participant messages (n = {N}). A conversation counts in every area the person asked about ({pct(D['n_two_plus_areas'], N)}% asked about two or more). Symptoms such as pain are counted under the body area they affect. {pct(D['n_everyday'], N)}% asked about an everyday complaint (muscles and bones, skin, rashes and allergies, diet, digestion, colds). Hover over a bar to see the symptoms people described.</p>
</section>""")

# ---- 6b symptoms and medications by area (deck slide 8) ----
arows = ('<div class="arow ahead"><div>Area (% of people)</div><div>Symptoms and issues people described</div><div>Medications named in the chat</div></div>')
for i, (code, lab, sym, pm, am) in enumerate(AREAS):
    n, tot = TOPIC[code]
    meds = (f'<span class="mp">Person: {E(pm)}</span>' if pm else "") + (f'<span class="mai">AI: {E(am)}</span>' if am else "")
    k = tip(f"sx{i}", lab, [("Share", f"{pct(n, tot)}%"), ("People", f"{n} of {tot}"),
                            ("Named by the person", pm or "None"), ("Named by the AI", am or "None")], (), "Symptoms people described: " + sym + ".")
    arows += (f'<div class="arow" {attrs(k)}><div><b>{E(lab)}</b><span class="apct">{pct(n, tot)}%</span></div><div>{E(sym)}</div>'
              f'<div>{meds or "<span class=mnone>None named</span>"}</div></div>')
slides.append(f"""
<section class="slide" id="s6b">{EYEBROW}
  <h2>What people described in each area, and which medications came up</h2>
  <div class="legend"><span><i class="lg-sq" style="background:{DARK}"></i>Named by the person</span><span><i class="lg-sq" style="background:#1a8cc8"></i>Named by the AI</span></div>
  <div class="atab">{arows}</div>
  <p class="foot">Coded from participant messages (n = {N}); one conversation can fall in more than one area. Medications include any drug named in the chat, whether suggested, explained or warned against; long AI lists are shortened.</p>
</section>""")

# ---- 7 follow-ups (headline behaviors first; added detail last and lighter) ----
fu = [("Asked a new question", "human_followup_new_question", DARK, [P("My scalp is flaking and scabbing. What do I do?"), P("Can you sunburn your scalp?")]),
      ("Pushed back or corrected the AI", "human_pushback", DARK, [P("Still think it's the flu?"), P("But I can run without pain, I could start and stop with no real problem.")]),
      ("Added more about their situation", "human_followup_adds_detail", PALE, [P("Why is the top of my foot hurting?"), P("There is no swelling but I do run daily.")])]
rows = [(lab, *D["followup"][col], c, qs) for lab, col, c, qs in fu]
slides.append(f"""
<section class="slide" id="s7">{EYEBROW}
  <h2>As the chats went on, people added more about their situation ({pct(*D['followup']['human_followup_adds_detail'])}%) far more often than they pushed back ({pct(*D['followup']['human_pushback'])}%)</h2>
  <p class="chart-title">Among the {N_MULTI} participants who sent a follow-up message</p>
  {sbars(rows, "f", "Coded from participant messages after the first. One person can count in more than one bar.")}
  <p class="axis-title">% of participants whose later messages did each of these</p>
  <p class="foot">Coded from participant messages after the first (n = {N_MULTI}). One person could do more than one of these, so bars add up to more than 100%. Pushed back = corrected the AI, said it missed something, or asked it to reconsider.</p>
</section>""")

# ---- 8 asked cause vs referral ----
ry, ny = D["referral_by_asked_cause"]["asked"]
rn, nn = D["referral_by_asked_cause"]["did_not_ask"]
bars = ""
for lab, r, n, qref, qno in [("Asked what was causing it or whether it was serious", ry, ny, [A("Because this episode has lasted several days and you've said this happens repeatedly, please contact your healthcare provider today."), A("Consider seeing a dermatologist if they keep recurring.")], []),
                              ("Did not ask", rn, nn, [A("The best specialist to see is a sleep medicine physician.")], [A("No, it is not automatically a must to have cataract surgery on the second eye after the first eye is done."), A("The key is to eat enough protein, fuel your workouts, include a variety of nutritious foods, and stay consistent over time.")])]:
    segs = ""
    for part, k_n, col, txt, qs in [("AI referred to a professional", r, DARK, "#fff", qref), ("AI did not refer", n - r, PALE, "#1c2430", qno)]:
        if k_n == 0: continue
        p = 100 * k_n / n
        k = tip(f"r_{lab[:5]}_{part[:6]}", f"{lab}: {part.lower()}", [("Share", f"{round(p)}%"), ("People", f"{k_n} of {n}"),
                ("Asked vs. did not ask", "Fisher's exact p < .001 (BH-adjusted .014)")], qs,
                "Question type and referral both coded from the conversation text.")
        segs += f'<div class="hseg" style="width:{p:.2f}%;background:{col};color:{txt}" {attrs(k)}><b>{round(p)}%</b></div>'
    bars += f'<div class="hrow"><div class="hlab"><b>{lab}</b><br><span class="muted">(n = {n})</span></div><div class="hbar">{segs}</div></div>'
ticks = "".join(f'<span style="left:{t}%">{t}%</span>' for t in range(0, 101, 25))
slides.append(f"""
<section class="slide" id="s8">{EYEBROW}
  <h2>Asking what was causing a symptom or whether it was serious always led to a referral, compared with about 6 in 10 times otherwise</h2>
  <p class="chart-title">How often the AI pointed people to a professional</p>
  <div class="legend"><span><i class="lg-sq" style="background:{DARK}"></i>AI referred to a professional</span><span><i class="lg-sq" style="background:{PALE}"></i>AI did not refer</span></div>
  <div class="hchart">{bars}<div class="hrow"><div></div><div class="ticks">{ticks}</div></div>
  <p class="axis-title">% of conversations</p></div>
  <p class="foot">Question type and referral both coded from the conversation text (n = {N}). Fisher's exact p &lt; .001 (BH-adjusted .014 across 20 question-by-response pairings). Questions about a test result are not counted here.</p>
</section>""")

# ---- 9 how the AI answered (same 50 people) ----
ai = D["ai"]; nm, nmt = D["ai_named_med"]
ref_n, _ = ai["ai_refers_professional"]
rwa, rwat = D["referred_without_asking_care"]
nmn, nmnt = D["named_med_not_asked"]
ai_rows = [("Pointed them to a doctor or other professional", *ai["ai_refers_professional"], DARK,
            [A("Because this episode has lasted several days and you've said this happens repeatedly, please contact your healthcare provider today."), A("Consider seeing a dermatologist if they keep recurring.")]),
           ("Asked them a question back", *ai["ai_followup_question"], LIGHT,
            [A("Did it start suddenly (after a specific twist, stub, or fall) or build up gradually over days or weeks?"), A("Are the flakes white and dry or yellow and greasy?")]),
           ("Named a specific medication", nm, nmt, DARK,
            [A("For a typical headache, acetaminophen (Tylenol) or ibuprofen (Advil, Motrin) may help."), A("Short-term use of anti-inflammatory medications (like ibuprofen or naproxen) or topical gels can help manage pain and swelling.")]),
           ("Mentioned urgent care or the ER", *ai["ai_urgent_care"], LIGHT,
            [A("If you develop chest pressure, difficulty breathing, sudden severe pain, fainting, or new weakness, seek emergency care immediately.")]),
           ("Recommended they take a medication", *ai["ai_recommends_med"], LIGHT,
            [A("Consider Tylenol (acetaminophen), or ibuprofen if you can safely take it, following the package directions.")]),
           ("Included a disclaimer (not medical advice)", *ai["ai_disclaimer"], DARK,
            [A("For medical advice or diagnosis, consult a professional.")])]
slides.append(f"""
<section class="slide" id="s9">{EYEBROW}
  <h2>The AI filled the gap by pointing 4 in 5 people to a professional, including most who never asked about care</h2>
  <p class="chart-title">What the AI did in its replies to these {N} participants</p>
  {sbars(ai_rows, "ai", "Coded from the AI's replies across the whole conversation.")}
  <p class="axis-title">% of conversations</p>
  <p class="foot">Coded from the AI's text (n = {N}). One conversation can count in several bars. Only {pct(D['asks']['human_asks_care'][0], N)}% asked whether or where to get care, yet the AI referred {pct(rwa, rwat)}% of those who did not ask. In {pct(nmn, nmnt)}% of the chats where the AI named a drug, the person had not asked about one.</p>
</section>""")


# ---- 9b medications: what people asked about vs. what the AI recommended (one row per chat) ----
MP = D["med_pairs"]; mc = MP["counts"]; otc, nrec = MP["otc_of_recommended"]
MED_NOTE = {"Asked, and got a recommendation": "The person named a drug, and the AI suggested a specific one to take, try or ask a doctor about.",
            "Asked, no recommendation": "The person named a drug; the AI explained it but did not suggest taking or trying one.",
            "Recommended without being asked": "The person described a symptom without asking about any drug; the AI suggested one anyway."}
mrows = ""
for gi, g in enumerate(MP["groups"]):
    mrows += f'<div class="mgrp">{E(g["label"])}<span>{len(g["rows"]) if gi < 2 else mc["recommended_unasked"]} people</span></div>'
    for ri, (a, b) in enumerate(g["rows"]):
        unasked = gi == 2
        k = tip(f"md{gi}{ri}", g["label"], [("They asked about" if not unasked else "They described", a), ("The AI recommended", b or "Nothing specific; it explained only")], (), MED_NOTE[g["label"]])
        mrows += (f'<div class="mpr" {attrs(k)}><div class="{"mn" if unasked else "ma"}">{E(a)}</div><div class="marr">&rarr;</div>'
                  f'<div class="{"mb" if b else "mn"}">{E(b or "Explained only")}</div></div>')
slides.append(f"""
<section class="slide" id="s9b">{EYEBROW}
  <h2>When the AI recommended a drug, it was usually OTC relief for a symptom, and {mc['recommended_unasked']} of its {nrec} recommendations were unprompted</h2>
  <div class="mpairs"><div class="mhead"><div class="mh1">What the person asked about</div><div></div><div class="mh2">What the AI recommended</div></div>{mrows}</div>
  <p class="foot">Each row is one conversation ({sum(mc[x] for x in ("asked_and_recommended", "asked_only", "recommended_unasked"))} of the {MP['N']} involved a medication question or a recommendation). Italic = the person described a symptom and did not ask about a drug. {otc} of the {nrec} recommendations were over-the-counter. Drug names as they appeared in the chat. Scalp = a sunburned scalp: the AI suggested ibuprofen or Tylenol for the pain; the anti-dandruff shampoo it also suggested for flaking is not counted as a drug.</p>
</section>""")

# ---- 9c medications by type of drug (deck slide 13) ----
DC = D["drug_classes"]; mx = max(max(d["asked"], d["recommended"]) for d in DC) * 100 / N
dv = '<div class="dvr dvh"><div>Person asked about it</div><div></div><div>AI recommended it</div></div>'
for i, d in enumerate(DC):
    pa, pr = 100 * d["asked"] / N, 100 * d["recommended"] / N
    k = tip(f"dc{i}", d["class"], [("Asked about it", f"{round(pa)}% ({d['asked']} of {N})"), ("AI recommended it", f"{round(pr)}% ({d['recommended']} of {N})")],
            (), "Examples: " + d["examples"] + ".")
    wl, wr = 80 * pa / mx, 80 * pr / mx
    left = (f'<span class="f" style="width:{wl:.1f}%"></span><b style="right:calc({wl:.1f}% + 8px)">{round(pa)}%</b>' if pa else '<b class="z" style="right:8px">0%</b>')
    right = (f'<span class="f" style="width:{wr:.1f}%"></span><b style="left:calc({wr:.1f}% + 8px)">{round(pr)}%</b>' if pr else '<b class="z" style="left:8px">0%</b>')
    dv += f'<div class="dvr" {attrs(k)}><div class="dvl">{left}</div><div class="dvmid">{E(d["class"])}<small>{E(d["examples"])}</small></div><div class="dvrt">{right}</div></div>'
slides.append(f"""
<section class="slide" id="s9c">{EYEBROW}
  <h2>People asked about prescriptions; the AI recommended over-the-counter relief</h2>
  <p class="chart-title">Asked about vs. recommended, by type of drug</p>
  <div class="dvg">{dv}</div>
  <p class="foot">% of participants (n = {N}). Asked = named a specific drug in their own messages ({pct(med_n, N)}% did). Recommended = the AI suggested they take, try or ask a doctor about a specific drug ({pct(ai['ai_recommends_med'][0], N)}%). {otc} of the {nrec} recommendations were over-the-counter, and {mc['recommended_unasked']} of the {nrec} people who got one had not asked about any medication.</p>
</section>""")

# ---- 10 takeaways ----
self_other = D["about"]["other_person"]
pb, pbt = D["followup"]["human_pushback"]
ad, adt = D["followup"]["human_followup_adds_detail"]
take = [("For research", "#a5306d", [
            ("AI chats can be a new source of patient voice.", f" In their follow-ups, {pct(ad, adt)}% of people who kept chatting added detail about their situation, so these transcripts capture symptoms and context in people's own words."),
            ("Chats show how people describe health problems in their own words.", f" People described everyday symptoms across {len(AREAS)} areas of health, most often muscles, bones and joints ({pct(D['topics']['topic_muscles_bones_joints'][0], N)}%).")]),
        ("For healthcare & pharma", "#627fcc", [
            ("AI is steering people toward care, and sometimes toward OTC drugs, usually unprompted.", f" Only {pct(D['asks']['human_asks_care'][0], N)}% asked whether or where to get care, yet the AI pointed {pct(ref_n, N)}% of people to a professional. {D['med_pairs']['counts']['recommended_unasked']} of the {D['med_pairs']['otc_of_recommended'][1]} people who got a drug recommendation had not asked about any medication, and {D['med_pairs']['otc_of_recommended'][0]} of the {D['med_pairs']['otc_of_recommended'][1]} drugs were over the counter."),
            ("“What is causing this?” is the front door.", f" {pct(D['asks6']['human_asks_what_cause'][0], N)}% asked what was causing a symptom, and only {pct(D['asks6']['human_asks_serious'][0], N)}% asked whether it was serious. Questions about cause or seriousness are also where the AI referred most reliably, so this is the moment that most shapes whether people reach an HCP.")]),
        ("Where the risk sits", "#8467b6", [
            ("AI rarely adds a disclaimer, and people rarely push back.", f" Only {pct(ai['ai_disclaimer'][0], N)}% of AI replies included a disclaimer, and only {pb} of {pbt} people who sent follow-ups questioned an answer."),
            ("Care decisions often go unasked.", f" {pct(D['goals']['goal_vs_asked']['goal_care'][0], D['goals']['N_asked'])}% hoped AI would help them decide about care, but only {pct(D['goals']['goal_vs_asked']['goal_care'][1], D['goals']['N_asked'])}% asked it outright. People who asked about their goal directly tended to say it was met more often ({pct(*D['goals']['met_by_asked_own']['asked'])}% vs. {pct(*D['goals']['met_by_asked_own']['did_not_ask'])}%), and {'1 in 10' if pct(self_other, N) == 10 else str(pct(self_other, N)) + '%'} asked on behalf of someone the AI never heard from.")])]
tk = "".join(f'<div class="tk"><p class="tk-lab" style="background:{c}">{E(h)}</p><ul>' + "".join(f'<li><b style="color:{c}">{E(a)}</b>{E(b)}</li>' for a, b in items) + "</ul></div>" for h, c, items in take)
slides.append(f"""
<section class="slide" id="s10">{EYEBROW}
  <h2 class="cyan">Now what does that mean?</h2>
  <div class="tks">{tk}</div>
  <p class="foot small">Notes: exploratory pulse; {N} participants whose pasted conversation included their own messages. Group sizes are small, so differences are directional. BH-adjusted p-values are shown where tests were run. Question types, health areas, who the question was about and follow-up behavior were coded from participant messages; referral, medication, urgent-care and disclaimer codes from the AI text; goals from the survey answers. Goal results use the same participants. Chat excerpts are trimmed, with spelling lightly corrected and identifying details left out.</p>
</section>""")


# ---- 12 to 14: the goals people set (survey C3) and whether they were met (D2) ----
G = D["goals"]; NG = G["N"]; NA_ = G["N_asked"]
SAID = "In their words (survey answer)"
# Nov 2026 review: goal_cause split into what_cause, serious and test_result so goals line up with the slide 5 question types
GOALS = [("goal_what_cause", "What is causing it", [P("I wanted to understand why I've been feeling so tired lately, even after getting a full night's sleep."), P("Finding out what's wrong with my wrist.")]),
         ("goal_treatment", "How to treat or manage it", [P("I was looking for at-home treatments to ease knee pain.")]),
         ("goal_condition_info", "General facts about a condition", [P("I wanted to learn about sleep apnea and see if it was something I might have myself.")]),
         ("goal_care", "Whether or where to get care", [P("I wanted to determine if I needed to call my doctor or just wait out whatever sickness I was coming down with.")]),
         ("goal_serious", "Is it normal or serious", [P("My goal was to understand if my symptoms were serious and what steps I should take next.")]),
         ("goal_med", "About a specific medication", [P("I wanted to see how often people are allergic to some antibiotics.")]),
         ("goal_test_result", "What a test result means", [P("To see if AI is able to explain ultrasound results.")]),
         ("goal_reassurance", "Reassurance", [P("I wanted the AI to show me different examples of what it could be, so I know it isn't a health scare.")]),
         ("goal_prepare_visit", "Prepare for a visit", [P("I wanted to get an idea before I go see a doctor.")])]
rows = []
for i, (code, lab, qs) in enumerate(GOALS):
    n = G["types"][code]; m_yes, m_n = G["met_by_type"][code]
    k = tip(f"g{i}", lab, [("Share", f"{pct(n, NG)}%"), ("People", f"{n} of {NG}"), ("Said this goal was met", f"{pct(m_yes, m_n)}% ({m_yes} of {m_n})")], qs,
            "Coded from what people wrote as their goal before the chat. One person can have several goals.", SAID)
    out_col = DARK if code in ("goal_what_cause", "goal_treatment") else LIGHT
    rows.append((lab, n, NG, out_col, k))
bars = ""
for lab, n, tot, col, k in rows:
    p = 100 * n / tot
    bars += f"""<div class="sbar" {attrs(k)}><div class="dlab{' b' if col == DARK else ''}">{E(lab)}</div>
      <div class="strack"><span class="sfill" style="width:{p:.2f}%;background:{col}"></span><span class="sval" style="left:{p:.2f}%">{round(p)}%</span></div></div>"""
slides.append(f"""
<section class="slide" id="s12">{EYEBROW}
  <h2>Half came to AI to find out what was wrong; {pct(G['types']['goal_treatment'], NG)}% wanted to know how to treat it</h2>
  <p class="chart-title">What participants said their goal was</p>
  <div class="sbars">{bars}</div>
  <p class="axis-title">% of participants with a given goal</p>
  <p class="foot">Coded from answers to &ldquo;When starting the conversation you just provided, what was your goal?&rdquo; (n = {NG} participants who described a health goal). One person can have more than one goal ({pct(G['two_plus'], NG)}% did), so bars add up to more than 100%. {pct(G['for_other'], NG)}% said the goal was about someone else, and {pct(G['ai_easier'], NG)}% said, unprompted, that AI was quicker, cheaper or easier than a search or a doctor.</p>
</section>""")

# ---- 13 goal vs. what they asked ----
# Rows match slide 5 one to one (same labels and order); the asked bar is the slide 5 bar. Goals with no matching
# question type (reassurance, preparing for a visit) show the goal bar only.
ASK_Q = {"goal_what_cause": [P("Why is the top of my foot hurting?")], "goal_treatment": [P("What can I do to alleviate knee pain and get back to normal?")],
         "goal_condition_info": [P("What is sleep apnea?")], "goal_care": [P("Should I see a medical specialist about this or try to wait it out?")],
         "goal_serious": [P("Is that typical of the medicine?")], "goal_med": [P("I have a headache, what should I take?")],
         "goal_test_result": [P("At a high level, what did these tests show?")]}
LAB = dict((c, l) for c, l, _ in GOALS); GQ = dict((c, q) for c, _, q in GOALS)
pb_ = ""
for i, (code, _, _) in enumerate(GOALS):
    strong = code == "goal_care"
    if code in G["goal_vs_asked"]:
        ng, na = G["goal_vs_asked"][code]; pg, pa = 100 * ng / NA_, 100 * na / NA_
        k = tip(f"ga{i}", LAB[code], [("Said it was their goal", f"{round(pg)}% ({ng} of {NA_})"), ("Asked it in the chat", f"{round(pa)}% ({na} of {NA_})")],
                ASK_Q[code], "Goal from the survey answer; asked from the participant's own messages in the chat.", "What the question looked like in the chat")
        ask_bar = f'<div class="strack"><span class="sfill" style="width:{pa:.2f}%;background:{DARK}"></span><span class="sval" style="left:{pa:.2f}%">{round(pa)}%</span></div>'
    else:
        ng = G["goal_only"][code]; pg = 100 * ng / NA_
        k = tip(f"ga{i}", LAB[code], [("Said it was their goal", f"{round(pg)}% ({ng} of {NA_})"), ("Asked it in the chat", "No matching question type")],
                GQ[code], "Goal from the survey answer. The chat codes have no matching question type, so there is no asked bar.", SAID)
        ask_bar = '<div class="strack" style="background:none"><span class="sval muted" style="left:0;font-weight:400">no matching question type</span></div>'
    pb_ += f"""<div class="sbar" {attrs(k)}><div class="dlab{' b' if strong else ''}">{E(LAB[code])}</div><div class="ptracks">
      <div class="strack"><span class="sfill" style="width:{pg:.2f}%;background:{LIGHT}"></span><span class="sval" style="left:{pg:.2f}%">{round(pg)}%</span></div>
      {ask_bar}</div></div>"""
cg, ca = G["goal_vs_asked"]["goal_care"]
slides.append(f"""
<section class="slide" id="s13">{EYEBROW}
  <h2>Their goals ran ahead of their questions: {pct(cg, NA_)}% wanted help deciding about care, yet only {pct(ca, NA_)}% asked for it</h2>
  <p class="chart-title">Their goal vs. what they asked the AI</p>
  <div class="legend"><span><i class="lg-sq" style="background:{LIGHT}"></i>Said it was their goal</span><span><i class="lg-sq" style="background:{DARK}"></i>Asked it in the chat</span></div>
  <div class="sbars">{pb_}</div>
  <p class="axis-title">% of participants</p>
  <p class="foot">Goals coded from the survey answer; questions coded from participants' own messages in the pasted chat (n = {NA_} participants with both). Rows match the question types on the previous slide; the last two goals have no matching question type. Treatment shows a similar gap ({pct(G['goal_vs_asked']['goal_treatment'][0], NA_)}% vs. {pct(G['goal_vs_asked']['goal_treatment'][1], NA_)}%): people often described a symptom and left the AI to suggest next steps.</p>
</section>""")

# ---- 14 was the goal met? ----
MET = [("Yes", "Yes, it was met", DARK, "#fff", [P("I took some Tylenol and laid down for a short nap. When I woke up my headache was gone.")]),
       ("Partly", "Partly", PALE, "#1c2430", [P("It gave almost too much information and I struggled to parse it.")]),
       ("No", "No", "#E3A26F", "#1c2430", [P("It didn't really have a solid answer. There was no ah-ha moment that I was hoping for.")])]
segs = ""
for code, lab, col, txt, qs in MET:
    n = G["met"][code]; p = 100 * n / NA_
    k = tip(f"m_{code}", f"Goal met? {lab}", [("Share", f"{round(p)}%"), ("People", f"{n} of {NA_}")], qs, None, SAID)
    segs += f'<div class="hseg" style="width:{p:.2f}%;background:{col};color:{txt}" {attrs(k)}><b>{round(p)}%</b></div>'
# Nov 2026 review: the unprompted reactions (reassured, doctor, acted, noted a limit) moved to Part 3B.
# The lower bars split the same 50 by whether they asked the AI about their main goal, so the groups add back to the 50.
GROUPS = [("asked", "Asked the AI about their main goal", True, [P("What kind of knee injury does this sound like?")]),
          ("did_not_ask", "Did not ask the AI about their main goal", True, []),
          ("no_match", "Main goal had no matching question type", False, [])]
grows = ""
for gk, glab, gbold, gqs in GROUPS:
    cnts = G["met_by_group"][gk]; gn = sum(cnts.values()); gsegs = ""
    for code, lab, col, txt, _ in MET:
        n = cnts[code]
        if n == 0: continue
        p = 100 * n / gn
        k = tip(f"mg_{gk}_{code}", f"{glab}: {lab.lower()}", [("Share", f"{round(p)}%"), ("People", f"{n} of {gn}")], gqs if code == "Yes" else [],
                "Main goal from the survey answer; asked from the participant's own messages in the chat." if gk != "no_match" else
                "Main goal was reassurance (3), preparing for a visit (2) or other (2), which have no matching question type.",
                "What the question looked like in the chat")
        gsegs += f'<div class="hseg" style="width:{p:.2f}%;background:{col};color:{txt}" {attrs(k)}><b>{round(p) if p >= 8 else ""}{"%" if p >= 8 else ""}</b></div>'
    grows += f'<div class="hrow"><div class="hlab">{"<b>" if gbold else ""}{E(glab)}{"</b>" if gbold else ""}<br><span class="muted">(n = {gn})</span></div><div class="hbar" style="height:52px">{gsegs}</div></div>'
ay, an_ = G["met_by_asked_own"]["asked"]; ny_, nn_ = G["met_by_asked_own"]["did_not_ask"]
nm = sum(G["met_by_group"]["no_match"].values())
slides.append(f"""
<section class="slide" id="s14">{EYEBROW}
  <h2>{pct(G['met']['Yes'], NA_)}% said the chat met their goal; people who asked about that goal outright were somewhat more satisfied ({pct(ay, an_)}% vs. {pct(ny_, nn_)}%)</h2>
  <p class="chart-title">Did the chat meet the goal they set?</p>
  <div class="legend"><span><i class="lg-sq" style="background:{DARK}"></i>Yes</span><span><i class="lg-sq" style="background:{PALE}"></i>Partly</span><span><i class="lg-sq" style="background:#E3A26F"></i>No</span></div>
  <div class="hchart"><div class="hrow"><div class="hlab"><b>All participants</b><br><span class="muted">(n = {NA_})</span></div><div class="hbar" style="height:64px">{segs}</div></div></div>
  <p class="muted" style="text-align:center;font-style:italic;margin:18px 0 6px;border-top:1px solid #e6e9ee;padding-top:12px">The same {NA_}, split by whether they asked the AI about their main goal</p>
  <div class="hchart">{grows}</div>
  <p class="foot">Coded from the survey answer on whether the goal was achieved (n = {NA_}, the same participants as the other slides). The three lower bars split the same {NA_} people. Asked vs. did not ask: Fisher's exact p = .08, BH-adjusted p = .49, so read the gap as a pattern. No matching question type = reassurance 3, preparing for a visit 2, other 2.</p>
</section>""")

slides.append("""
<section class="slide s-title" id="s11">
  <p class="brand">HEALOGIX</p>
  <h2 class="white">Want to learn more?</h2>
  <div class="people">
    <div><p class="pname">Denicia Aragon Espinosa</p><p>Senior Associate, Behavioral Science</p><p class="sel">denicia.aragon.espinosa@healogix.com</p><p class="sel">+1.445.867.0680</p></div>
    <div><p class="pname">James Dunlea, Ph.D.</p><p>SVP, Head of Behavioral Science</p><p class="sel">james.dunlea@healogix.com</p><p class="sel">+1.267.410.9872</p></div>
  </div>
  <p class="lede">Meet Behavioral Science at Healogix. We like to get a feel for how people really think and act, so each month we run a short online study on a behavioral question worth asking.</p>
  <p class="howto"><a href="../part3b/" style="color:inherit">Continue to Part 3B: What did AI say back to people? &rarr;</a></p>
</section>""")

# Slide order (Nov 2026 review, matches the Canva deck). The takeaways slide is second to last; the deck ends with
# the QR slide, the web page with the contact slide. Cut for now and kept in the code so they can come back:
# s1b (Parts 1 and 2), s3 (big numbers), s6b (symptoms by area), s9c (drugs by type), s12 (goals).
ORDER = ["s1", "s2", "s4", "s6", "s5", "s13", "s7", "s9", "s8", "s9b", "s14", "s10", "s11"]
_by_id = {s.split('id="', 1)[1].split('"', 1)[0]: s for s in slides}
slides = [_by_id[i] for i in ORDER]
_keep = "".join(slides)
TIPS = {k: v for k, v in TIPS.items() if f'data-tip="{k}"' in _keep}

tpl = open(ROOT / "build" / "template.html", encoding="utf-8").read()
out = tpl.replace("%%TITLE%%", "AI and Trust, Part 3A").replace("%%SLIDES%%", "\n".join(slides)).replace("%%TIPS%%", json.dumps(TIPS)).replace("%%NSLIDES%%", str(len(slides)))
(ROOT / "part3a").mkdir(exist_ok=True)
open(ROOT / "part3a" / "index.html", "w", encoding="utf-8").write(out)
print("Wrote part3a/index.html", len(TIPS), "tooltips")
