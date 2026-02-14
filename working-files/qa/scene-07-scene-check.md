# QA Check — Scene 07 Full Scene

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 27-30
- Section QA inputs:
  - `working-files/qa/scene-07-section-01-check.md`
  - `working-files/qa/scene-07-section-02-check.md`
- Boundary verification input:
  - `working-files/ocr/batch-17-pages-29-30.md`
- Target script file: `booklet/script/scene-07.md`

## Checks

1. Completeness check
- Section 01 line IDs: 34 (`S07-SEC01-L001` to `S07-SEC01-L034`)
- Section 02 line IDs: 37 (`S07-SEC02-L001` to `S07-SEC02-L037`)
- Total extracted spoken/sung lines for Scene 07: 71
- Total triplets in `scene-07.md` for Sections 1-2: 71
- Result: PASS

2. Order and continuity check
- Verified Section 01 → Section 02 sequence remains continuous and in source order.
- Emotional breakdown block, butler step-back handoff, and self-reliance song resolution are coherent with no dropped boundary lines.
- Result: PASS

3. Scene-boundary ownership check
- OCR page 30 includes explicit `（第七幕完。）` marker after final spoken line.
- `scene-07.md` includes spoken/sung lines through scene close and excludes stage-direction-only close marker.
- Result: PASS

4. Format check
- `scene-07.md` maintains strict triplet formatting for all retained lines:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions remain excluded from final triplets except parenthetical spoken delivery markers embedded in dialogue lines.
- Result: PASS

## Residual Risk Notes

- Low-confidence lyric tokens from pages 27-30 remain tracked for optional publication-hardening re-OCR (`S07-SEC01-L010`; `S07-SEC02-L021`, `L025`, `L029`).

## Scene Status Decision

- Scene 07 is marked **Done** for dialogue-line coverage and formatting gates.
- Next highest-priority production task shifts to Scene 08 Section 01 from page 31 onward.