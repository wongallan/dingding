# QA Check — Scene 04 Full Scene

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 14-17
- Target script file: `booklet/script/scene-04.md`
- Section QA files:
  - `working-files/qa/scene-04-section-01-check.md`
  - `working-files/qa/scene-04-section-02-check.md`
  - `working-files/qa/scene-04-section-03-check.md`

## Scene-Level Checks

1. Completeness check
- Section 01 lines: 24
- Section 02 lines: 46
- Section 03 lines: 25
- Scene total: 95 triplets
- Result: PASS

2. Boundary/ownership check
- Page-14 crossover was assigned to Scene 04 in Section 01.
- Scene 04 closes at page 17 (`第四幕完`); page 18 (`第五幕`) is excluded from Scene 04.
- Result: PASS

3. Continuity check
- Failed-magic classroom arc remains continuous across all three sections.
- No dropped or duplicated boundary lines detected between sections.
- Result: PASS

4. Formatting/consistency check
- All entries use strict three-line triplet format.
- Character naming aligns with `working-files/character-name-map.md`.
- Result: PASS

## Residual Risk Notes

- Page-17 song OCR is low confidence; lyric wording is conservatively normalized and tracked in section QA/extraction notes.
- Optional hardening task: targeted re-OCR on page 17 prior to final publication lock.
