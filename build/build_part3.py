"""Builds part3/index.html (Part 3: what the AI said) from data/public/part3_summary.json.
Run from the repo root:  python build/build_part3.py
Uses only the public summary file (group averages and counts, no respondent IDs)."""
import json, html, statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = json.load(open(ROOT / "data" / "public" / "part3_summary.json", encoding="utf-8"))
E = html.escape

# ---------- tooltip content ----------
TIPS = {}
def tip(key, title, stats, quotes=(), note=None):
    """quotes: list of (speaker, text)"""
    h = f'<p class="tt-title">{E(title)}</p>'
    if stats:
        h += '<dl class="tt-stats">' + "".join(f"<dt>{E(a)}</dt><dd>{E(b)}</dd>" for a, b in stats) + "</dl>"
    if note:
        h += f'<p class="tt-note">{E(note)}</p>'
    if quotes:
        h += '<p class="tt-sub">From the conversations</p>'
        h += "".join(f'<blockquote><span>{E(s)}</span>{E(t)}</blockquote>' for s, t in quotes)
    TIPS[key] = h
    return key

def attrs(key):
    return f'data-tip="{key}" tabindex="0" role="button" aria-label="Show details"'

# ---------- excerpts (trimmed, spelling lightly corrected, nothing identifying) ----------
Q = {
 "ref_stomach": ("AI", "Because this episode has lasted several days and you've said this happens repeatedly, please contact your healthcare provider today."),
 "ref_sleep": ("AI", "The best specialist to see is a sleep medicine physician."),
 "ref_skin": ("AI", "Consider seeing a dermatologist if they keep recurring."),
 "ref_worse": ("AI", "Contact your doctor's office promptly if you're getting worse or developing significant dizziness, vomiting, or a fever."),
 "urg_chest": ("AI", "If you develop chest pressure, difficulty breathing, sudden severe pain, fainting, or new weakness, seek emergency care immediately."),
 "noref_cataract": ("AI", "No, it is not automatically a must to have cataract surgery on the second eye after the first eye is done."),
 "noref_diet": ("AI", "The key is to eat enough protein, fuel your workouts, include a variety of nutritious foods, and stay consistent over time."),
 "med_headache": ("AI", "For a typical headache, acetaminophen (Tylenol) or ibuprofen (Advil, Motrin) may help."),
 "med_neck": ("AI", "Consider Tylenol (acetaminophen), or ibuprofen if you can safely take it, following the package directions."),
 "med_knee": ("AI", "Short-term use of anti-inflammatory medications (like ibuprofen or naproxen) or topical gels can help manage pain and swelling."),
 "disc": ("AI", "For medical advice or diagnosis, consult a professional."),
 "p_stomach": ("Participant", "I've been dealing with some bad stomach aches for the past few weeks. Should I see a medical specialist about this or try to wait it out?"),
 "p_knee": ("Participant", "Hurts to bend, especially in a deep squat. Some weakness, can push through pain and stops hurting when standing again. Worse in morning."),
 "p_bossing": ("Participant", "Does metacarpal bossing grow?"),
 "p_hfm": ("Participant", "What if hand, foot and mouth isn't treated?"),
 "p_headache": ("Participant", "I have a headache, what should I take?"),
 "p_foot1": ("Participant", "Why is the top of my foot hurting?"),
 "p_foot2": ("Participant", "There is no swelling but I do run daily."),
 "p_knee3a": ("Participant", "Dull ache, feel weak when trying to stand up from sitting."),
 "p_knee3b": ("Participant", "Legs overall are fatigued, quads feel very weak. How soon should I return to morning walks?"),
 "p_neck1": ("Participant", "I developed a sharp pain in my neck that radiates to my shoulders suddenly. Can this be a symptom of anything else?"),
 "p_neck2": ("Participant", "Back of neck, closer to shoulders."),
 "p_neck3": ("Participant", "After sleeping."),
}
q = lambda *ks: [Q[k] for k in ks]

DARK, LIGHT, PALE, NEG, GRID = "#0b3d68", "#29abe2", "#9DC3E6", "#E3A26F", "#E6E9EE"

def f1(x): return f"{x:.1f}"
def sgn(x, d=1):
    v = round(x, d)
    return ("0." + "0" * d) if v == 0 else f"{v:+.{d}f}"

slides = []

# ---------- 1 title ----------
slides.append(("title", """
<section class="slide s-title" id="s1">
  <p class="brand">HEALOGIX</p>
  <p class="kicker">Q4 &middot; November 2026 &middot; Pulse</p>
  <h1>Part 3: What the AI says shapes how people feel afterward</h1>
  <p class="lede">The Behavioral Science Team at Healogix looks inside real AI health conversations</p>
  <p class="byline">Denicia Aragon Espinosa &amp; James Dunlea, Ph.D.</p>
  <p class="howto">Hover over or tap any chart to see the numbers and examples from the conversations behind it.</p>
</section>"""))

# ---------- 2 overview ----------
pills = [("#a5306d", "Distress dropped after the chat, most after a referral to a professional", "s4"),
         ("#9b4c96", "No one felt calmer after the AI recommended a medication", "s5"),
         ("#8467b6", "Longer conversations ended with more positive feelings", "s7"),
         ("#627fcc", "People remember when the AI tells them to see someone", "s8")]
slides.append(("overview", f"""
<section class="slide" id="s2">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2 class="ov-title">What the AI says in the chat shapes how people feel afterward</h2>
  <p class="ov-sub">Overview of findings</p>
  <div class="pills">{''.join(f'<a class="pill" style="--pill:{c}" href="#{h}">{E(t)}</a>' for c, t, h in pills)}</div>
  <p class="foot">Online survey via Prolific &middot; Pulse 3 &middot; n = 57 U.S. adults who shared an AI health conversation and rated their feelings before and after</p>
</section>"""))

# ---------- 3 big numbers ----------
bn = [("84%", DARK, "shared their own symptoms or situation, not just general questions", "42 of 50",
       tip("t3a", "Shared their own situation: 84%", [("Participants", "42 of 50 with their own messages"), ("General questions only", "8 of 50")],
           q("p_stomach", "p_knee"), "Coded from the participant's messages.")),
      ("79%", "#00a4e4", "of AI replies pointed them to a doctor or other professional", "44 of 56",
       tip("t3b", "AI referred to a professional: 79%", [("Conversations", "44 of 56 usable"), ("No referral", "12 of 56")],
           q("ref_stomach", "ref_sleep"), "Coded from the AI's text.")),
      ("9%", DARK, "of AI replies included a disclaimer that the answer is not medical advice", "5 of 56",
       tip("t3c", "AI included a disclaimer: 9%", [("Conversations", "5 of 56 usable"), ("No disclaimer", "51 of 56")],
           q("disc"), "A disclaimer = the AI says it is not a doctor, or not medical advice."))]
slides.append(("big", f"""
<section class="slide" id="s3">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2 class="big-title">People bring <em>real</em> worries to AI</h2>
  <div class="bignums">{''.join(f'<div class="bn" {attrs(k)}><span class="bn-num" style="color:{c}">{n}</span><span class="bn-txt">{E(t)} <span class="muted">({E(cnt)})</span></span></div>' for n, c, t, cnt, k in bn)}</div>
  <p class="foot">Conversations pasted by participants and coded from the text &middot; 56 usable health conversations</p>
</section>"""))

# ---------- 4 dumbbell ----------
def m(key):
    return {n.split(" (n")[0]: (y[0], y[1], int(n.split("n = ")[1].rstrip(")"))) for n, y in D[key]}
na = D["na_all_means"]
rows4 = [("All participants", na["pre"], na["post"], na["n"], True, None, [], "Everyone with complete before and after scores.")]
R, U, P = m("ref_na"), m("urg_na"), m("pers_na")
rows4 += [
 ("AI referred them to a professional", *R["Referred to a professional"], False, ("Referral vs. no referral", "p = .02 (BH-adjusted .12)"), q("ref_stomach", "ref_worse"), None),
 ("AI did not refer them", *R["No referral"], False, ("Referral vs. no referral", "p = .02 (BH-adjusted .12)"), q("noref_cataract", "noref_diet"), None),
 ("AI mentioned urgent care or the ER", *U["Mentioned urgent or emergency care"], False, ("Urgent care vs. not", "p = .02 (BH-adjusted .12)"), q("urg_chest"), None),
 ("AI did not mention urgent care", *U["Did not"], False, ("Urgent care vs. not", "p = .02 (BH-adjusted .12)"), q("ref_skin"), None),
 ("They shared their own situation", *P["Shared personal details"], False, ("Own situation vs. general", "p = .11 (BH-adjusted .42)"), q("p_stomach"), None),
 ("They asked only general questions", *P["General questions only"], False, ("Own situation vs. general", "p = .11 (BH-adjusted .42)"), q("p_bossing", "p_hfm"), None),
]
LO, HI = 10, 24
pos = lambda v: (v - LO) / (HI - LO) * 100
html4 = ""
for i, (lab, pre, post, n, bold, test, quotes, note) in enumerate(rows4):
    stats = [("Before the chat", f1(pre)), ("After the chat", f1(post)), ("Change", sgn(post - pre)), ("People", str(n))]
    if test: stats.append(test)
    k = tip(f"t4_{i}", lab, stats, quotes, note or "PANAS negative affect, 10 = none, 50 = extreme.")
    lo, hi = sorted([pre, post])
    gap = ' gap' if i in (1, 3, 5) else ''
    html4 += f"""<div class="drow{gap}" {attrs(k)}>
      <div class="dlab{' b' if bold else ''}">{E(lab)} <span class="muted">(n = {n})</span><span class="dval">{f1(pre)} before, {f1(post)} after</span></div>
      <div class="track"><span class="seg" style="left:{pos(lo):.2f}%;width:{pos(hi)-pos(lo):.2f}%"></span>
        <span class="dot pre" style="left:{pos(pre):.2f}%"></span><span class="dot post" style="left:{pos(post):.2f}%"></span></div></div>"""
ticks4 = "".join(f'<span style="left:{pos(t):.2f}%">{t}</span>' for t in range(10, 25, 2))
slides.append(("dumbbell", f"""
<section class="slide" id="s4">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2>Distress dropped after the chat, most when the AI pointed people to a professional</h2>
  <p class="chart-title">Negative feelings before and after the conversation</p>
  <div class="legend"><span><i class="lg-dot" style="background:{LIGHT}"></i>Before the chat</span><span><i class="lg-dot" style="background:{DARK}"></i>After the chat</span></div>
  <div class="dchart">{html4}<div class="axis"><div></div><div class="ticks">{ticks4}</div></div>
  <p class="axis-title">Negative affect score (10 = none, 50 = extreme)</p></div>
  <p class="foot">PANAS negative affect (10 items), rated for the moment before the first message and the moment the chat ended. Referral vs. no referral: p = .02 (BH-adjusted .12). People the AI referred started out more distressed.</p>
</section>"""))

# ---------- 5 waffle ----------
cnt, groups = D["calm_med"]
cats = [("Calmer", DARK), ("About the same", PALE), ("More distressed", NEG)]
panels = ""
for gi, g in enumerate(groups, start=1):
    seq = []
    for c, col in cats:
        seq += [(c, col)] * cnt.get(f"{gi}|{c}", 0)
    n = len(seq); calm = cnt.get(f"{gi}|Calmer", 0)
    lab = "AI recommended a medication" if gi == 1 else "AI did not recommend a medication"
    quotes = q("med_headache", "med_neck", "med_knee") if gi == 1 else q("ref_stomach", "ref_skin")
    k = tip(f"t5_{gi}", lab, [("Felt calmer", f"{calm} of {n} ({round(100*calm/n)}%)"),
             ("About the same", str(cnt.get(f'{gi}|About the same', 0))), ("More distressed", str(cnt.get(f'{gi}|More distressed', 0))),
             ("Calmer vs. not, by group", "Fisher's exact p = .02 (BH-adjusted .38)")], quotes,
            "Calmer = negative affect fell 5 or more points.")
    sq = "".join(f'<i class="sq" style="background:{col}"></i>' for c, col in seq)
    panels += f"""<div class="wpanel" {attrs(k)}><p class="wbig">{round(100*calm/n)}% calmer</p><p class="muted">{calm} of {n}</p>
      <div class="waffle">{sq}</div><p class="wlab">{E(lab)}</p></div>"""
slides.append(("waffle", f"""
<section class="slide" id="s5">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2>No one felt calmer after the AI recommended a medication</h2>
  <p class="chart-title">Who felt calmer after the chat?</p>
  <div class="legend">{''.join(f'<span><i class="lg-sq" style="background:{col}"></i>{c}</span>' for c, col in cats)}</div>
  <div class="wpanels">{panels}</div>
  <p class="foot">One square per participant. Calmer = negative affect (PANAS) fell 5 or more points from before to after the chat. p = .02 (BH-adjusted .38). Only 11 conversations included a medication recommendation, so read this as a direction.</p>
</section>"""))

# ---------- 6 items ----------
ri = {g: dict(zip(names, vals)) for g, vals, names in D["ref_items"]}
NA_ITEMS = ["distressed", "nervous", "afraid", "scared", "upset", "irritable", "jittery", "ashamed", "guilty", "hostile"]
NA_ITEMS.sort(key=lambda it: ri["Referred to a professional"][it])
LO6, HI6 = -0.8, 0.4
p6 = lambda v: (v - LO6) / (HI6 - LO6) * 100
html6 = ""
for it in NA_ITEMS:
    a, b = ri["Referred to a professional"][it], ri["No referral"][it]
    k = tip(f"t6_{it}", f"Feeling {it}", [("AI referred them (n = 43)", sgn(a, 2)), ("AI did not refer them (n = 11)", sgn(b, 2)),
             ("Difference", sgn(a - b, 2))], [], "Average change on a 1 to 5 scale, after minus before. Below 0 = felt less. Descriptive, not tested item by item.")
    lo, hi = sorted([a, b])
    html6 += f"""<div class="drow" {attrs(k)}><div class="dlab">{it.capitalize()}</div>
      <div class="track"><span class="zero" style="left:{p6(0):.2f}%"></span><span class="seg" style="left:{p6(lo):.2f}%;width:{p6(hi)-p6(lo):.2f}%"></span>
      <span class="dot post" style="left:{p6(a):.2f}%"></span><span class="dot pre" style="left:{p6(b):.2f}%"></span></div></div>"""
ticks6 = "".join(f'<span style="left:{p6(t/10):.2f}%">{"0" if t == 0 else f"{t/10:+.1f}"}</span>' for t in range(-8, 5, 2))
slides.append(("items", f"""
<section class="slide" id="s6">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2>After a referral, feeling distressed, nervous and afraid dropped the most</h2>
  <p class="chart-title">Average change in each negative feeling after the chat</p>
  <div class="legend"><span><i class="lg-dot" style="background:{DARK}"></i>AI referred them (n = 43)</span><span><i class="lg-dot" style="background:{LIGHT}"></i>AI did not refer them (n = 11)</span></div>
  <div class="dchart narrow">{html6}<div class="axis"><div></div><div class="ticks">{ticks6}</div></div>
  <p class="axis-title">Average change (1 to 5 scale)</p></div>
  <p class="foot">PANAS negative-affect items, rated 1 to 5 before and after the chat. Change = after minus before; left of 0 = felt less. Referred n = 43, not referred n = 11. Item differences are descriptive.</p>
</section>"""))

# ---------- 7 messages ----------
x, y = D["turns"][1][1], D["turns"][1][2]
buckets = {"1": [], "2": [], "3": [], "4+": []}
for a, c in zip(x, y):
    if a >= 1:
        buckets["1" if a == 1 else "2" if a == 2 else "3" if a == 3 else "4+"].append(c)
bq = {"1": q("p_headache"), "2": q("p_foot1", "p_foot2"), "3": q("p_knee3a", "p_knee3b"), "4+": q("p_neck1", "p_neck2", "p_neck3")}
YLO, YHI = -18, 10
py = lambda v: (YHI - v) / (YHI - YLO) * 100
cols = ""
for kk, vals in buckets.items():
    mu = st.mean(vals); n = len(vals)
    lab = "1 message" if kk == "1" else ("4 or more" if kk == "4+" else f"{kk} messages")
    k = tip(f"t7_{kk}", lab, [("People", str(n)), ("Average change", sgn(mu)), ("Range", f"{min(vals):+d} to {max(vals):+d}"),
            ("Felt more positive", f"{sum(v > 0 for v in vals)} of {n}")], bq[kk],
            "Change in PANAS positive affect (10 to 50), after minus before. Example shows the participant's own messages.")
    top, bot = sorted([py(mu), py(0)])
    dots = "".join(f'<i class="pt" style="top:{py(v):.2f}%;left:{20 + (j * 37) % 60}%"></i>' for j, v in enumerate(sorted(vals)))
    grid = "".join(f'<span class="hl{" z" if t == 0 else ""}" style="top:{py(t):.2f}%"></span>' for t in range(-15, 11, 5))
    cols += f"""<div class="vcol" {attrs(k)}><div class="vplot">{grid}
        <span class="vbar" style="top:{top:.2f}%;height:{bot-top:.2f}%;background:{DARK if mu > 0 else LIGHT}"></span>{dots}
        <span class="vval" style="top:{(py(mu) - 9 if mu >= 0 else py(mu) + 1.5):.2f}%">{sgn(mu)}</span></div>
      <p class="vlab">{lab}<br><span class="muted">(n = {n})</span></p></div>"""
yt = "".join(f'<span style="top:{py(t):.2f}%">{"0" if t == 0 else f"{t:+d}"}</span>' for t in range(-15, 11, 5))
slides.append(("messages", f"""
<section class="slide" id="s7">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2>People who kept the conversation going ended up feeling more positive</h2>
  <p class="chart-title">Change in positive feelings, by messages sent to the AI</p>
  <div class="vchart"><div class="yaxis">{yt}</div><div class="vgrid">{cols}</div></div>
  <p class="axis-title">Messages the participant sent to the AI &middot; bars = average, dots = each participant</p>
  <p class="foot">PANAS positive affect (10 items, 10 to 50), after minus before. Spearman rho = .30, p = .03, among the 51 participants who sent at least one message. Small groups; read as a pattern.</p>
</section>"""))

# ---------- 8 recall ----------
rc, rg = D["recall"]
rcats = [("Clear or strong recommendation", DARK, "#fff"), ("Gentle suggestion or options", PALE, "#1c2430"), ("No action or wait it out", NEG, "#1c2430")]
rq = {1: q("ref_stomach", "ref_skin"), 2: q("noref_cataract", "noref_diet")}
bars8 = ""
for gi, glab in [(1, "AI referred them"), (2, "AI did not refer")]:
    N = sum(rc.get(f"{gi}|{c}", 0) for c, *_ in rcats)
    segs = ""
    for c, col, txt in rcats:
        n = rc.get(f"{gi}|{c}", 0); pct = 100 * n / N
        k = tip(f"t8_{gi}_{c[:5]}", f"{glab}: recalled “{c.lower()}”", [("People", f"{n} of {N}"), ("Share", f"{round(pct)}%"),
                ("Clear or strong recall, referred vs. not", "58% vs. 9%, Fisher's exact p = .005")], rq[gi],
                "Referral coded from the AI's text; recall is what the participant reported in the survey afterward.")
        segs += f'<div class="hseg" style="width:{pct:.2f}%;background:{col};color:{txt}" {attrs(k)}>{f"<b>{round(pct)}%</b><small>{n} of {N}</small>" if pct >= 15 else ""}</div>'
    bars8 += f'<div class="hrow"><div class="hlab"><b>{glab}</b><br><span class="muted">(n = {N})</span></div><div class="hbar">{segs}</div></div>'
ticks8 = "".join(f'<span style="left:{t}%">{t}%</span>' for t in range(0, 101, 25))
slides.append(("recall", f"""
<section class="slide" id="s8">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2>When the AI tells people to see someone, they remember</h2>
  <p class="chart-title">What participants recalled the AI recommending</p>
  <div class="legend">{''.join(f'<span><i class="lg-sq" style="background:{col}"></i>{c}</span>' for c, col, _ in rcats)}</div>
  <div class="hchart">{bars8}<div class="hrow"><div></div><div class="ticks">{ticks8}</div></div>
  <p class="axis-title">Share of participants in each group</p></div>
  <p class="foot">Referral coded from the AI's own text; recall is the participant's report after the chat. Fisher's exact test p = .005.</p>
</section>"""))

# ---------- 9 takeaways ----------
take = [("For research", "#a5306d", [("Code what the AI said, not just what people asked.", " Referral, urgent-care and medication advice each lined up with different emotional outcomes."),
                                       ("Measure feelings before and after the chat;", " distress fell on average (18.5 to 15.2), while positive feelings stayed flat.")]),
        ("For healthcare & pharma", "#627fcc", [("An AI referral may calm people, and it sticks.", " Referred participants felt less distressed afterward, and 58% recalled a clear recommendation (vs. 9%)."),
                                                 ("Medication suggestions did not reassure.", " No one who got a medication recommendation felt calmer, so expect these patients to arrive with questions.")]),
        ("Where the risk sits", "#8467b6", [("People bring their real situation to AI (84%).", " Only 9% of AI replies included a disclaimer."),
                                            ("Short chats left people no better off.", " One or two messages ended slightly less positive; four or more ended about 3 points more positive.")])]
tk = "".join(f'<div class="tk"><p class="tk-lab" style="background:{c}">{E(h)}</p><ul>' + "".join(f'<li><b style="color:{c}">{E(a)}</b>{E(b)}</li>' for a, b in items) + "</ul></div>" for h, c, items in take)
slides.append(("take", f"""
<section class="slide" id="s9">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2 class="cyan">Now what does that mean?</h2>
  <div class="tks">{tk}</div>
  <p class="foot small">Notes: exploratory pulse; 57 participants with complete before and after PANAS scores. Group sizes are small, so group differences are directional. BH-adjusted p-values are shown where tests were run. Conversation codes (referral, urgent care, medication, disclaimer, personal details) were coded from the participant and AI text. Chat excerpts are trimmed, with spelling lightly corrected and identifying details left out.</p>
</section>"""))

# ---------- 10 contact ----------
slides.append(("contact", """
<section class="slide s-title" id="s10">
  <p class="brand">HEALOGIX</p>
  <h2 class="white">Want to learn more?</h2>
  <div class="people">
    <div><p class="pname">Denicia Aragon Espinosa</p><p>Senior Associate, Behavioral Science</p><p class="sel">denicia.aragon.espinosa@healogix.com</p><p class="sel">+1.445.867.0680</p></div>
    <div><p class="pname">James Dunlea, Ph.D.</p><p>SVP, Head of Behavioral Science</p><p class="sel">james.dunlea@healogix.com</p><p class="sel">+1.267.410.9872</p></div>
  </div>
  <p class="lede">Meet Behavioral Science at Healogix. We like to get a feel for how people really think and act, so each month we run a short online study on a behavioral question worth asking.</p>
</section>"""))

body = "\n".join(s for _, s in slides)
tpl = open(ROOT / "build" / "template.html", encoding="utf-8").read()
out = tpl.replace("%%TITLE%%", "AI and Trust, Part 3").replace("%%SLIDES%%", body).replace("%%TIPS%%", json.dumps(TIPS))
open(ROOT / "part3" / "index.html", "w", encoding="utf-8").write(out)
print(len(out), len(TIPS))
