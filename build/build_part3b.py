"""Builds part3b/index.html (Part 3b: what people asked AI) from data/public/part3b_summary.json.
Run from the repo root:  python build/build_part3b.py
Uses only the public summary file (counts, no respondent IDs or conversation text).
To refresh the counts from the private coded file, run build/export_part3b_summary.py first, on your own computer."""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = json.load(open(ROOT / "data" / "public" / "part3b_summary.json", encoding="utf-8"))
N = D["N"]
N_MULTI = D["n_multi"]
E = html.escape
TIPS = {}

def tip(key, title, stats, quotes=(), note=None):
    h = f'<p class="tt-title">{E(title)}</p>'
    if stats:
        h += '<dl class="tt-stats">' + "".join(f"<dt>{E(a)}</dt><dd>{E(b)}</dd>" for a, b in stats) + "</dl>"
    if note:
        h += f'<p class="tt-note">{E(note)}</p>'
    if quotes:
        h += '<p class="tt-sub">From the conversations</p>' + "".join(f'<blockquote><span>{E(s)}</span>{E(t)}</blockquote>' for s, t in quotes)
    TIPS[key] = h
    return key

attrs = lambda k: f'data-tip="{k}" tabindex="0" role="button" aria-label="Show details"'
P = lambda t: ("Participant", t)
A = lambda t: ("AI", t)
DARK, LIGHT, PALE = "#0b3d68", "#29abe2", "#9DC3E6"
EYEBROW = '<p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>'

def cnt(col):
    """(people coded 1, people coded) for one participant code, from the public summary."""
    return tuple(D["asks"][col])

def sbars(rows, prefix, note):
    """rows: (label, n, N, color, quotes)"""
    out = ""
    for i, (lab, n, tot, col, quotes) in enumerate(rows):
        pct = 100 * n / tot
        k = tip(f"{prefix}{i}", lab, [("People", f"{n} of {tot}"), ("Share", f"{round(pct)}%")], quotes, note)
        out += f"""<div class="sbar" {attrs(k)}><div class="dlab{' b' if i == 0 else ''}">{E(lab)}</div>
          <div class="strack"><span class="sfill" style="width:{pct:.2f}%;background:{col}"></span>
          <span class="sval" style="left:{pct:.2f}%">{round(pct)}% ({n})</span></div></div>"""
    return f'<div class="sbars">{out}</div>'

slides = []
slides.append(f"""
<section class="slide s-title" id="s1">
  <p class="brand">HEALOGIX</p>
  <p class="kicker">Q4 &middot; November 2026 &middot; Pulse</p>
  <h1>Part 3b: What people ask AI about their health</h1>
  <p class="lede">The Behavioral Science Team at Healogix looks inside real AI health conversations</p>
  <p class="byline">Denicia Aragon Espinosa &amp; James Dunlea, Ph.D.</p>
  <p class="howto">Hover over or tap any chart to see the numbers and examples from the conversations behind it.</p>
</section>""")

pills = [("#a5306d", "Most people asked about their own health, not general facts", "s3"),
         ("#9b4c96", "Half asked the AI what was causing a symptom", "s4"),
         ("#8467b6", "Follow-up messages added detail; few people pushed back", "s7"),
         ("#627fcc", "Asking what was wrong always led to a referral", "s8")]
slides.append(f"""
<section class="slide" id="s2">{EYEBROW}
  <h2 class="ov-title">What people ask AI about their health, and how the AI answers</h2>
  <p class="ov-sub">Overview of findings</p>
  <div class="pills">{''.join(f'<a class="pill" style="--pill:{c}" href="#{h}">{E(t)}</a>' for c, t, h in pills)}</div>
  <p class="foot">Online survey via Prolific &middot; Pulse 3 &middot; 50 U.S. adults whose pasted AI health conversation included their own messages</p>
</section>""")

# ---- 3 big numbers ----
self_n = D["about"]["self"]
cause_n, _ = cnt("human_asks_cause"); med_n, _ = cnt("human_asks_med")
bn = [(f"{round(100*self_n/N)}%", DARK, "asked about their own health, not someone else's or general facts", f"{self_n} of {N}",
       tip("b1", "Asked about their own health", [("People", f"{self_n} of {N}")], [P("Why is the top of my foot hurting?"), P("There is no swelling but I do run daily.")])),
      (f"{round(100*cause_n/N)}%", "#00a4e4", "asked what was causing a symptom or whether it was serious", f"{cause_n} of {N}",
       tip("b2", "Asked what was causing a symptom", [("People", f"{cause_n} of {N}")], [P("I've been feeling unusually tired lately, even after getting a full night's sleep. What could be causing this?")])),
      (f"{round(100*med_n/N)}%", DARK, "asked about a specific medication", f"{med_n} of {N}",
       tip("b3", "Asked about a specific medication", [("People", f"{med_n} of {N}")], [P("I have a headache, what should I take?")],
           "Counts any question that names a specific drug, prescription or over the counter."))]
slides.append(f"""
<section class="slide" id="s3">{EYEBROW}
  <h2 class="big-title">People ask AI about their <em>own</em> bodies</h2>
  <div class="bignums">{''.join(f'<div class="bn" {attrs(k)}><span class="bn-num" style="color:{c}">{n}</span><span class="bn-txt">{E(t)} <span class="muted">({E(c2)})</span></span></div>' for n, c, t, c2, k in bn)}</div>
  <p class="foot">Conversations pasted by participants and coded from their own messages &middot; {N} usable conversations with at least one participant message</p>
</section>""")

# ---- 4 question types ----
asks = [("What is causing it, or is it serious", "human_asks_cause", [P("Why is the top of my foot hurting?"), P("I have had a headache for 2 days and pain behind my eyes. What could be the problem?")]),
        ("How to treat or manage it", "human_asks_treatment", [P("My scalp is flaking and scabbing. What do I do?"), P("What can I do to alleviate knee pain and get back to normal?")]),
        ("General facts about a condition", "human_asks_condition_info", [P("What is sleep apnea?"), P("Does metacarpal bossing grow?")]),
        ("Whether or where to get care", "human_asks_care", [P("Should I see a medical specialist about this or try to wait it out?"), P("Should I schedule an appointment with a specialist?")]),
        ("About a specific medication", "human_asks_med", [P("I have a headache, what should I take?"), P("How can I tell if I'm having an allergic reaction to antibiotics I started yesterday?")])]
rows = []
for i, (lab, col, qs) in enumerate(asks):
    n, tot = cnt(col)
    rows.append((lab, n, tot, DARK if i == 0 else LIGHT, qs))
multi_kind = D["n_more_than_one_kind"]
slides.append(f"""
<section class="slide" id="s4">{EYEBROW}
  <h2>Half of participants asked the AI what was causing their symptom</h2>
  <p class="chart-title">What participants asked the AI, at any point in the chat</p>
  {sbars(rows, "q", "Coded from every participant message. One person can ask more than one kind of question.")}
  <p class="axis-title">Share of the {N} participants</p>
  <p class="foot">Coded from every participant message in each pasted conversation (n = {N}). One person can ask more than one kind of question; {multi_kind} did.</p>
</section>""")

# ---- 5 who ----
who = [("self", "Themselves", DARK, [P("Why is the top of my foot hurting?")]),
       ("other_person", "Someone else, such as a partner or child", LIGHT, [P("Husband's low back started hurting yesterday.")]),
       ("general", "No one in particular (general facts)", PALE, [P("Does metacarpal bossing grow?"), P("What if hand, foot and mouth isn't treated?")])]
sqs, leg = "", ""
for code, lab, col, qs in who:
    n = D["about"][code]
    k = tip(f"w_{code}", lab, [("People", f"{n} of {N}"), ("Share", f"{round(100*n/N)}%")], qs)
    leg += f'<span {attrs(k)} style="padding:4px 8px;border-radius:6px"><i class="lg-sq" style="background:{col}"></i>{E(lab)}: <b>{round(100*n/N)}% ({n})</b></span>'
    sqs += "".join(f'<i class="sq" style="background:{col}" data-tip="{k}"></i>' for _ in range(n))
slides.append(f"""
<section class="slide" id="s5">{EYEBROW}
  <h2>Most people asked about themselves; 1 in 10 asked for someone else</h2>
  <p class="chart-title">Who the participant's question was about</p>
  <div class="legend">{leg}</div>
  <div class="wpanels"><div class="wpanel"><div class="waffle w10">{sqs}</div><p class="muted">One square = one participant</p></div></div>
  <p class="foot">Coded from participant messages (n = {N}). Someone else = a named or described other person, such as a partner or child. No one in particular = general questions about a condition or health fact.</p>
</section>""")

# ---- 6 health areas ----
AREAS = [("pain_muscles_bones", "Pain, muscles and bones", [P("Dull ache, feel weak when trying to stand up from sitting.")]),
         ("skin_allergy", "Skin, hair and allergies", [P("Can you sunburn your scalp?")]),
         ("diet_fitness_weight", "Diet, fitness and weight", [P("I want to discover affordable, healthy foods that will help me achieve my fitness and wellness goals.")]),
         ("digestive", "Stomach and digestion", [P("I've been dealing with some bad stomach aches for the past few weeks.")]),
         ("cold_flu_infection", "Colds, flu and infections", [P("I'm feeling a bit better today, no aches or chills. Sore throat, no runny nose. Still think it's the flu?")]),
         ("diabetes_hormones", "Diabetes and hormones", [P("Would an endocrinologist benefit me from learning why my hormones are out of whack?")]),
         ("eyes", "Eyes", [P("My eye doctor is sending me to a retina specialist. The appointment is supposed to take 3 to 4 hours. What will they do?")]),
         ("mental_health_sleep", "Mental health and sleep", [P("What is sleep apnea? I think I may have it.")]),
         ("other", "Other (chest pain, headache, test reports)", [P("Chest pain when running.")])]
rows = []
for i, (code, lab, qs) in enumerate(AREAS):
    n = D["health_area"].get(code, 0)
    rows.append((lab, n, N, PALE if code == "other" else (DARK if i == 0 else LIGHT), qs))
slides.append(f"""
<section class="slide" id="s6">{EYEBROW}
  <h2>Aches and pains topped the list of health concerns people brought to AI</h2>
  <p class="chart-title">Main health area of each conversation</p>
  {sbars(rows, "a", "One main area per conversation.")}
  <p class="axis-title">Share of the {N} participants</p>
  <p class="foot">Coded from participant messages (n = {N}), one main area per conversation. Other includes chest pain, headache, fatigue, kidney or test reports and recovery after surgery.</p>
</section>""")

# ---- 7 follow-ups ----
fu = [("Added more about their situation", "human_followup_adds_detail", DARK, [P("Why is the top of my foot hurting?"), P("There is no swelling but I do run daily.")]),
      ("Asked a new or deeper question", "human_followup_new_question", LIGHT, [P("My scalp is flaking and scabbing. What do I do?"), P("Can you sunburn your scalp?")]),
      ("Pushed back or corrected the AI", "human_pushback", PALE, [P("Still think it's the flu?"), P("But I can run without pain, I could start and stop with no real problem.")])]
rows = [(lab, *D["followup"][col], c, qs) for lab, col, c, qs in fu]
slides.append(f"""
<section class="slide" id="s7">{EYEBROW}
  <h2>When people kept going, most added detail; few pushed back</h2>
  <p class="chart-title">Among the {N_MULTI} participants who sent 2+ messages</p>
  {sbars(rows, "f", "Coded from participant messages after the first. One person can count in more than one bar.")}
  <p class="axis-title">What their later messages did</p>
  <p class="foot">Coded from participant messages after the first. Pushed back = corrected the AI, said it missed something, or asked it to reconsider. {N - N_MULTI} of {N} sent only one message.</p>
</section>""")

# ---- 8 asked cause vs referral ----
ry, ny = D["referral_by_asked_cause"]["asked"]
rn, nn = D["referral_by_asked_cause"]["did_not_ask"]
bars = ""
for lab, r, n, qref, qno in [("Asked what was causing it", ry, ny, [A("Because this episode has lasted several days and you've said this happens repeatedly, please contact your healthcare provider today."), A("Consider seeing a dermatologist if they keep recurring.")], []),
                              ("Did not ask", rn, nn, [A("The best specialist to see is a sleep medicine physician.")], [A("No, it is not automatically a must to have cataract surgery on the second eye after the first eye is done."), A("The key is to eat enough protein, fuel your workouts, include a variety of nutritious foods, and stay consistent over time.")])]:
    segs = ""
    for part, k_n, col, txt, qs in [("AI referred to a professional", r, DARK, "#fff", qref), ("AI did not refer", n - r, PALE, "#1c2430", qno)]:
        if k_n == 0: continue
        pct = 100 * k_n / n
        k = tip(f"r_{lab[:5]}_{part[:6]}", f"{lab}: {part.lower()}", [("People", f"{k_n} of {n}"), ("Share", f"{round(pct)}%"),
                ("Asked vs. did not ask", "Fisher's exact p < .001 (BH-adjusted .004)")], qs,
                "Question type and referral both coded from the conversation text.")
        segs += f'<div class="hseg" style="width:{pct:.2f}%;background:{col};color:{txt}" {attrs(k)}><b>{round(pct)}%</b><small>{k_n} of {n}</small></div>'
    bars += f'<div class="hrow"><div class="hlab"><b>{lab}</b><br><span class="muted">(n = {n})</span></div><div class="hbar">{segs}</div></div>'
ticks = "".join(f'<span style="left:{t}%">{t}%</span>' for t in range(0, 101, 25))
slides.append(f"""
<section class="slide" id="s8">{EYEBROW}
  <h2>Asking what was wrong always led to a referral</h2>
  <p class="chart-title">How often the AI pointed people to a professional</p>
  <div class="legend"><span><i class="lg-sq" style="background:{DARK}"></i>AI referred to a professional</span><span><i class="lg-sq" style="background:{PALE}"></i>AI did not refer</span></div>
  <div class="hchart">{bars}<div class="hrow"><div></div><div class="ticks">{ticks}</div></div>
  <p class="axis-title">Share of conversations</p></div>
  <p class="foot">Question type and referral both coded from the conversation text (n = {N}). Fisher's exact p &lt; .001 (BH-adjusted .004 across 20 question-by-response pairings).</p>
</section>""")

# ---- 9 takeaways ----
take = [("For research", "#a5306d", [("Code every message, not just the first.", " Most follow-ups added detail the first message left out (87%), and about half asked something new (47%)."),
                                       ("Few people ask about a drug by name;", " only 12% asked about a specific medication, even though the AI named one in 22 of 56 chats.")]),
        ("For healthcare & pharma", "#627fcc", [("Patients ask AI what is wrong first.", " Half asked what was causing a symptom, and every one of them was pointed to a professional (vs. 58% of others)."),
                                                 ("Treatment questions lean toward treatment answers.", " People who asked how to manage something got a medication suggestion more often (38% vs. 15%) and a referral less often (62% vs. 88%); neither gap was significant.")]),
        ("Where the risk sits", "#8467b6", [("People ask about their own bodies (78%),", " and 1 in 10 asks for someone else, such as a partner or child. Only 9% of AI replies included a disclaimer."),
                                            ("Few people push back.", " Only 4 of 30 multi-message chats corrected or questioned the AI's answer.")])]
tk = "".join(f'<div class="tk"><p class="tk-lab" style="background:{c}">{E(h)}</p><ul>' + "".join(f'<li><b style="color:{c}">{E(a)}</b>{E(b)}</li>' for a, b in items) + "</ul></div>" for h, c, items in take)
slides.append(f"""
<section class="slide" id="s9">{EYEBROW}
  <h2 class="cyan">Now what does that mean?</h2>
  <div class="tks">{tk}</div>
  <p class="foot small">Notes: exploratory pulse; {N} participants whose pasted conversation included their own messages. Group sizes are small, so differences are directional. BH-adjusted p-values are shown where tests were run. Question types, health area, who the question was about and follow-up behavior were coded from participant messages; referral and medication codes from the AI text. Chat excerpts are trimmed, with spelling lightly corrected and identifying details left out.</p>
</section>""")

slides.append("""
<section class="slide s-title" id="s10">
  <p class="brand">HEALOGIX</p>
  <h2 class="white">Want to learn more?</h2>
  <div class="people">
    <div><p class="pname">Denicia Aragon Espinosa</p><p>Senior Associate, Behavioral Science</p><p class="sel">denicia.aragon.espinosa@healogix.com</p><p class="sel">+1.445.867.0680</p></div>
    <div><p class="pname">James Dunlea, Ph.D.</p><p>SVP, Head of Behavioral Science</p><p class="sel">james.dunlea@healogix.com</p><p class="sel">+1.267.410.9872</p></div>
  </div>
  <p class="lede">Meet Behavioral Science at Healogix. We like to get a feel for how people really think and act, so each month we run a short online study on a behavioral question worth asking.</p>
</section>""")

tpl = open(ROOT / "build" / "template.html", encoding="utf-8").read()
out = tpl.replace("%%TITLE%%", "AI and Trust, Part 3b").replace("%%SLIDES%%", "\n".join(slides)).replace("%%TIPS%%", json.dumps(TIPS))
open(ROOT / "part3b" / "index.html", "w", encoding="utf-8").write(out)
print("Wrote part3b/index.html", len(TIPS), "tooltips")
