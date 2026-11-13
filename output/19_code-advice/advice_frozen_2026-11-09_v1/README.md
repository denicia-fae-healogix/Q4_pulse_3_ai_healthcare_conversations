# Frozen advice codebook, 2026-11-09, version v1

The locked codebook for how direct the AI's health advice was (Q4 Pulse 3 health-advice study): the advice ladder L0-L5 (one rung per chat, the most specific reached), the brand, prescription, supplement and vaccine flags, the 2 safety codes (said to see a doctor, gave a warning) and the medicines suggested. Drafted in step 15, piloted in step 17, and frozen after the researcher's pilot decisions V26-V29 (all 10 pilot edits approved).

- `advice_codebook.md`: the exact coding text the coders read.
- `codebook_*.csv`: the same codebook as tables.
- `advice_decisions_log.csv`: every researcher decision (V1-V29).
- `SHA256SUMS.txt`: a fingerprint of each file. `python scripts/19_code-advice/19a_freeze_and_prepare.py --verify` checks nothing has changed.

The files are read-only. Do not edit them; a change needs a new dated freeze.
