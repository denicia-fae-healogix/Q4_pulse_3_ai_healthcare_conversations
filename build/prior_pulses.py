"""The 'What we found in Parts 1 and 2' slide shared by the Part 3A and 3B pages.
Numbers are from the published August 2026 (Part 1) and October 2026 (Part 2) Healogix pulses."""

PART1 = ("Part 1", "August 2026", "184 U.S. adults", "#a5306d", [
    ("65%", "had used AI to look up health information, most often about symptoms and possible diagnoses (81% of those users)."),
    ("71% vs. 56%", "Women used AI for health more than men, and more often turned to AI first for emotional support (51% vs. 26%)."),
    ("59% vs. 47%", "Men more often told their provider what they had found with AI."),
])
PART2 = ("Part 2", "October 2026", "64 U.S. adults from our August and September pulses", "#627fcc", [
    ("39%", "would go to an AI chatbot before any person with a worrying health question; 61% had used AI for emotional support."),
    ("70% to 53%", "For a worrying question, asking family fell from 70% to 53% and a close friend from 56% to 44%; AI fell only from 84% to 78%."),
    ("58%", "of those who would go to AI first said the top reason was asking without feeling like a burden. People still rated their own doctor favorably, including on trust (PDRQ-9)."),
])

def prior_slide(slide_id, this_part):
    def card(part):
        name, when, who, color, rows = part
        items = "".join(f'<li><b style="color:{color}">{num}</b> {txt}</li>' for num, txt in rows)
        return (f'<div class="prev-card" style="border-top-color:{color}"><p class="prev-tag" style="color:{color}">{name} &middot; {when}</p>'
                f'<p class="prev-who">{who}</p><ul>{items}</ul></div>')
    return f"""
<section class="slide" id="{slide_id}">
  <p class="eyebrow">Healogix &middot; Q4 &middot; November 2026 &middot; Pulse</p>
  <h2>What we found in Parts 1 and 2</h2>
  <div class="prev-grid">{card(PART1)}{card(PART2)}</div>
  <p class="prev-next">{this_part}</p>
  <p class="foot">Online surveys via Prolific. Part 2 re-surveyed people from the earlier pulses.</p>
</section>"""
