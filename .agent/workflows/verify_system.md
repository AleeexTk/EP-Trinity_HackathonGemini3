---
description: How to verify the integrity and coherence of the Trinity Core system.
---

1. Ensure you are in the project root directory.
2. Run the absolute cleanup to ensure no Cyrillic strings are breaking the formal logic.
// turbo
3. `python absolute_cleanup.py`
4. Run the one-click demo script to verify all triangles (BLACK, GOLD, RED, GREEN) and the Evolution Protocol.
// turbo
5. `python start_hackathon_demo.py`
6. Check the output for "SYSTEM READY FOR HACKATHON SUBMISSION."
7. Verify that a new report has been generated in `_logs/` (or the root if `_logs` is not reachable).
8. Compare the newly generated coherence score with the one in `last_evolution.json`.
