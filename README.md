# AI and Trust, Part 3: Inside real AI health conversations

Interactive slides from the Healogix Behavioral Science Q4 Pulse 3 (November 2026). Hover over or tap any chart to see the numbers and example excerpts from the conversations behind it.

**Live pages**

- Home: https://denicia-fae-healogix.github.io/Q4_pulse_3_ai_healthcare_conversations/
- Part 3A, What did people ask AI?: https://denicia-fae-healogix.github.io/Q4_pulse_3_ai_healthcare_conversations/part3a/
- Part 3B, What did AI say back to people?: https://denicia-fae-healogix.github.io/Q4_pulse_3_ai_healthcare_conversations/part3b/

The old `/part3/` address redirects to Part 3B.

## What is in this repo

| Folder | What it holds |
|---|---|
| `index.html` | Landing page that links to both slide sets |
| `part3a/`, `part3b/` | The interactive slide pages (built files, do not edit by hand) |
| `part3/` | Redirect from the original Part 3 address to `part3b/` |
| `data/public/` | Summary counts and averages that feed the pages. No respondent IDs, no conversation text |
| `build/` | Python scripts that turn `data/public/` into the pages, plus the shared page template |
| `scripts/` | The R and Python analysis pipeline (00 to 09b) |
| `decks/` | PDF versions of the two Canva carousels (no hover) |
| `codebook/` | How each conversation was coded (Excel workbook and Markdown copy) |

## Data privacy

This repo is public. It holds **no respondent-level data**: no Prolific IDs, no pids, no full conversations. The analysis scripts read the private files from a local project folder that is never committed (`.gitignore` blocks `.csv` and `.xlsx` files). Chat excerpts on the pages were picked by hand from everyday topics, trimmed, with spelling lightly corrected and identifying details left out.

## Rebuilding the pages

Requires Python 3.9+ (pandas only for the export step).

```bash
# Only if the coded data changed: refresh the 3A counts from the private file (run on your own computer)
# (the second file is optional; it adds the drug-class counts for slide 13)
python build/export_part3a_summary.py "C:/path/to/05_Q4_3_conversations_wide_deid_coded_v3.csv" "C:/path/to/10_Q4_3_med_asked_vs_recommended.csv"

# Only if the 3B numbers changed: knit scripts/08b_...Rmd, then copy
# output/08b_Q4_3_deck-figures-what-ai-said/part3b_summary.json into data/public/

# Rebuild both pages from data/public/
python build/build_part3a.py
python build/build_part3b.py
```

Then commit and push. GitHub Pages updates within a few minutes.

## Running the analysis scripts

Set `project_root` (R) or `PROJECT_ROOT` (Python) at the top of each script to your local project folder, which holds the private data. Run in order: `00` rename variables, `01` split conversations, `06` binary categories, `07` group comparisons, `08a` (Part 3A) and `08b` (Part 3B) deck figures and number checks, then `09a` (pulls out the goal answers for coding) and `09b` (goal results).

08a and 09b read `05_Q4_3_conversations_wide_deid_coded_v3.csv` (the v2 file plus the v3 question-type split and health areas; see section 4b of the codebook).

The 07, 08a, 08b and 09b reports have interactive charts: hovering shows the numbers and example messages or goal answers. Those examples are real excerpts, so the knitted reports stay in your local `output/` folder and never go in this repo.

## Team

Behavioral Science at Healogix: Denicia Aragon Espinosa and James Dunlea, Ph.D.
