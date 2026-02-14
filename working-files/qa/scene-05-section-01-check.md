# QA Check — Scene 05 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 18
- Extracted source file: `working-files/extracted/scene-05-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-05.md`

## Checks

1. Completeness check
- Extracted line IDs: 15 (`S05-SEC01-L001` to `S05-SEC01-L015`)
- Written triplets in scene section: 15
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Transition flow preserved from camp-anxiety dialogue to classroom group recollection.
- Result: PASS

3. Speaker/content check
- Named speakers retained as staged.
- Mixed-language spoken tokens (`Oh Baby`, `Wonderful`) retained where source style indicates.
- Result: PASS (with uncertainty notes)

4. Format check
- Each entry in `scene-05.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-only movement/cue lines are excluded from triplet entries.
- One inline parenthetical action retained only where it appears inside spoken line continuity.
- Result: PASS

## Residual Risk Notes

- OCR quality is mixed on page 18 with low-confidence lexemes in `S05-SEC01-L005`, `S05-SEC01-L007`, and `S05-SEC01-L015`.
- Recommended next step: OCR next source batch (pages 19-20) and cross-check recurring phrases before scene-level lock.