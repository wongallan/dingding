# QA Check — Scene 06 Full Scene

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 22-26
- Section QA inputs:
  - `working-files/qa/scene-06-section-01-check.md`
  - `working-files/qa/scene-06-section-02-check.md`
- Boundary verification input:
  - `working-files/ocr/batch-15-pages-26-27.md`
- Target script file: `booklet/script/scene-06.md`

## Checks

1. Completeness check
- Section 01 line IDs: 38 (`S06-SEC01-L001` to `S06-SEC01-L038`)
- Section 02 line IDs: 66 (`S06-SEC02-L001` to `S06-SEC02-L066`)
- Total extracted spoken/sung lines for Scene 06: 104
- Total triplets in `scene-06.md` for Sections 1-2: 104
- Result: PASS

2. Order and continuity check
- Verified Section 01 → Section 02 sequence remains continuous and in source order.
- Competition setup, quiz round, magic rounds, and result reveal are coherent with no dropped boundary lines.
- Result: PASS

3. Scene-boundary ownership check
- OCR page 26 confirms only stage-direction material and explicit `（第六幕完）` marker.
- No spoken/sung dialogue lines for Scene 06 remain after Section 02 page-25 close.
- `scene-06.md` correctly excludes page-26 stage-direction-only content.
- Result: PASS

4. Format check
- `scene-06.md` maintains strict triplet formatting for all retained lines:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions remain excluded from final triplets except parenthetical spoken delivery markers embedded in dialogue lines.
- Result: PASS

## Residual Risk Notes

- Page-25 lyric lines `S06-SEC02-L058`, `L061`, and `L062` remain low-confidence and should still receive targeted re-OCR hardening before publication lock.

## Scene Status Decision

- Scene 06 is marked **Done** for dialogue-line coverage and formatting gates.
- Next highest-priority production task shifts to Scene 07 Section 01 from page 27 onward.