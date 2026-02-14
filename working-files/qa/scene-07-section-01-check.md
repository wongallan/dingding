# QA Check — Scene 07 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 27-28
- Extracted source file: `working-files/extracted/scene-07-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-07.md`

## Checks

1. Completeness check
- Extracted line IDs: 34 (`S07-SEC01-L001` to `S07-SEC01-L034`)
- Written triplets in scene section: 34
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence across pages 27→28.
- Breakdown dialogue, `我真的試了` song block, butler restraint dialogue, and `靜靜守候` transition are preserved in source order.
- Result: PASS

3. Speaker/content check
- Speaker labels are preserved in extraction staging and omitted from final script triplets per scene format.
- Mixed-language tokens (`I hate it`, `Baby`, `relax`) are retained where present in source style.
- Result: PASS (with uncertainty notes)

4. Format check
- Each entry in `scene-07.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only movement/cue lines are excluded from script triplets.
- Only spoken/sung lines are retained.
- Result: PASS

## Residual Risk Notes

- Several lyric tokens on pages 27-28 are reconstructed conservatively from low-confidence OCR; targeted hardening review found no additional line-level wording changes needed for this section.
- `S07-SEC01-L010` addressee token is now wording-locked as `呀叮` after targeted OCR re-check.
