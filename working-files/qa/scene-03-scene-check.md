# QA Check — Scene 03 Full Scene

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages covered: 11-14 (with page-14 crossover noted)
- Target script file: `booklet/script/scene-03.md`
- Section QA references:
  - `working-files/qa/scene-03-section-01-check.md`
  - `working-files/qa/scene-03-section-02-check.md`

## Scene-Level Checks

1. Section boundary continuity
- Verified boundary carry-over from `S03-SEC01-L041` to `S03-SEC02-L001` is explicit and complete.
- No duplicated line content at section boundary.
- Result: PASS

2. Completeness and ordering
- Combined staged lines: 63 (Section 01: 41, Section 02: 22).
- Scene script contains matching 63 triplets in sequence.
- Result: PASS

3. Terminology consistency
- Reused established butler-title and school-world phrasing consistently.
- No conflicting renderings introduced for recurring names in this scene.
- Result: PASS

4. Formatting and exclusions
- Triplet formatting is consistent throughout Scene 03.
- Stage-direction-only lines are excluded from dialogue triplets.
- Result: PASS

5. Risk notes
- Section 02 includes lyric-heavy lines reconstructed from degraded OCR tokens (`S03-SEC02-L010`, `S03-SEC02-L016`) with explicit uncertainty retained in working extraction notes.
- Page 14 clearly starts Scene 04 context; Scene 03 is treated complete up to its available continuity boundary.
