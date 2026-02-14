# QA Check — Scene 08 (Full Scene)

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 31-34
- Target script file: `booklet/script/scene-08.md`
- Section QA inputs:
  - `working-files/qa/scene-08-section-01-check.md`
  - `working-files/qa/scene-08-section-02-check.md`

## Scene-Level Checks

1. Section completeness roll-up
- Section 01 extracted lines: 34
- Section 02 extracted lines: 48
- Total extracted lines represented in script: 82
- Result: PASS

2. Boundary ownership check
- Opening song + butler observation lines (pages 31-32) retained in Scene 08 Section 01.
- Breakfast-preparation arc + `早餐小心意` + curtain close (pages 33-34) retained in Scene 08 Section 02.
- Scene closed at `第八幕完` on page 34; no spill into Scene 09.
- Result: PASS

3. Order/continuity check
- Section handoff preserves narrative arc: encouragement reset → independent practice → children care for butlers.
- No duplicate triplets at section boundary and no dropped handoff lines detected.
- Result: PASS

4. Format/consistency check
- All entries follow triplet format (`Characters`, `Sidney Lau romanization`, `English translation`).
- Character naming and recurring terms are consistent with current shared maps and scene style.
- Result: PASS

## Residual Risk Notes

- Section 01 targeted hardening completed for `S08-SEC01-L009` and `S08-SEC01-L031` via batch-18 recurrence verification.
- Section 02 targeted lyric hardening already completed for `S08-SEC02-L030` to `S08-SEC02-L046`; one minor low-confidence phrasing remains in `S08-SEC02-L010` as optional polish.

## Scene Status

- Scene 08 status: Done
- Next primary action: Begin Scene 09 Section 01 from pages 35-36.
