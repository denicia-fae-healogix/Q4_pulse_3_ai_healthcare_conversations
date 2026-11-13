# Frozen goal codebooks, 2026-11-09, version v1

The locked codebooks for the survey's two open-ended goal questions (Q4 Pulse 3 health-advice study): A = what the person wanted from the chat (multi-label, with one main goal), B = whether the goal was met, the 'why not met' list and 3 extra tags. Drafted in step 14, piloted in step 16, and frozen after the researcher's pilot decisions G15-G18.

Not adopted (left as written): the pilot's proposed P1 rule wording for A6 (asking before a planned appointment) and the P2 'two goals in one sentence' wording. Only their label changes were applied (G15, G16).

- `goal_codebook.md`: the exact coding text the coders read.
- `codebook_*.csv`, `why_not_met.csv`, `extra_tags.csv`, `main_goal_rule.csv`, `codebook_examples.csv`: the same codebook as tables.
- `goal_decisions_log.csv`: every researcher decision (G1-G18).
- `SHA256SUMS.txt`: a fingerprint of each file. `python scripts/18_code-goals/18a_freeze_and_prepare.py --verify` checks nothing has changed.

The files are read-only. Do not edit them; a change needs a new dated freeze.
