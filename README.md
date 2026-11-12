# AI and Trust, Part 3: Inside real AI health conversations

Interactive slides from the Healogix Behavioral Science Q4 Pulse 3 (November 2026). Hover over or tap any chart to see the numbers and example excerpts from the conversations behind it.

**Live pages**

- Home: https://denicia-fae-healogix.github.io/Q4_pulse_3_ai_healthcare_conversations/
- Part 3, what the AI told people: https://denicia-fae-healogix.github.io/Q4_pulse_3_ai_healthcare_conversations/part3/
- Part 3b, what people asked the AI: https://denicia-fae-healogix.github.io/Q4_pulse_3_ai_healthcare_conversations/part3b/

## What is in this repo

| Folder | What it holds |
|---|---|
| `index.html` | Landing page that links to both slide sets |
| `part3/`, `part3b/` | The interactive slide pages (built files, do not edit by hand) |
| `data/public/` | Summary counts and averages that feed the pages. No respondent IDs, no conversation text |
| `build/` | Python scripts that turn `data/public/` into the pages, plus the shared page template |
| `scripts/` | The R and Python analysis pipeline (00 to 08b) |
| `codebook/` | How each conversation was coded |

## Data privacy

This repo is public. It holds **no respondent-level data**: no Prolific IDs, no pids, no full conversations. The analysis scripts read the private files from a local project folder that is never committed (`.gitignore` blocks `.csv` and `.xlsx` files). Chat excerpts on the pages were picked by hand from everyday topics, trimmed, with spelling lightly corrected and identifying details left out.

## Rebuilding the pages

Requires Python 3.9+ (pandas only for the export step).

```bash
# Only if the coded data changed: refresh the 3b counts from the private file (run on your own computer)
python build/export_part3b_summary.py "C:/path/to/05_Q4_3_conversations_wide_deid_coded_v2.csv"

# Rebuild both pages from data/public/
python build/build_part3.py
python build/build_part3b.py
```

Then commit and push. GitHub Pages updates within a few minutes.

## Running the analysis scripts

Set `project_root` (R) or `PROJECT_ROOT` (Python) at the top of each script to your local project folder, which holds the private data. Run in order: `00` rename variables, `01` split conversations, `06` binary categories, `07` group comparisons, `08` and `08b` deck figures and number checks.

## Team

Behavioral Science at Healogix: Denicia Aragon Espinosa and James Dunlea, Ph.D.

