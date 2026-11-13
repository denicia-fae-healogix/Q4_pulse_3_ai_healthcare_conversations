# Frozen codebooks, 2026-11-05, version v3

These are the locked first-message codebooks for the Q4 Pulse 3 health-advice study. They were built in step 07 (3 LLM passes + merge + the researcher's revisions), piloted in step 08, and frozen here after the researcher approved pilot edits E6, E7 and E9 (step 07 revisions 9-12). The researcher then reverted pilot edit E8 (revisions 13-14; version 2), so emotions are not part of any request type, because emotion will go into sentiment analysis later. The Mental health and stress topic (T11) is kept. Version 3 replaces version 2 (frozen_2026-11-05_v2/): R3 and R6 are renamed and clarified around problem vs. goal (revisions 15-16). R3 is now 'How do I handle this problem, or is it safe?' and R6 is 'Help me reach a health goal', because 'what should I do' vs. 'recommendations' was confusing and 'personal' applies to all health advice. No message's label changed.

- `request_codebook.md` / `.csv`: type of request, R1-R6 (main analysis; several types per message).
- `topic_codebook.md` / `.csv`: health topic, T1-T11 (one primary topic per message).
- `topic_list_rules.md` and `07_topic_list_groups.csv`: how the descriptive topic list is counted.
- `codebook_revisions.csv`: every documented change made by the researcher.
- `SHA256SUMS.txt`: a fingerprint of each file. `python scripts/09_freeze-codebook/09_freeze_codebook.py --verify` checks nothing has changed.

The files are read-only. Do not edit them; a change needs a new dated freeze.
