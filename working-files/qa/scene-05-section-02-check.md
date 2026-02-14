# QA Check — Scene 05 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 19-20
- Extracted source file: `working-files/extracted/scene-05-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-05.md`

## Checks

1. Completeness check
- Extracted line IDs: 57 (`S05-SEC02-L001` to `S05-SEC02-L057`)
- Written triplets in scene section: 57
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Page-19 dialogue transition and page-20 song sequence are preserved.
- Result: PASS

3. Speaker/content check
- Speaker attributions retained in extraction staging and omitted from final script triplets per scene format.
- Mixed-language spoken tokens (`Oh Baby`) retained where source style indicates.
- Result: PASS (with uncertainty notes)

4. Format check
- Each entry in `scene-05.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-only movement/cue lines are excluded from triplet entries.
- Song heading cue (`（唱《早餐大難》）`) is excluded while lyric lines are retained.
- Result: PASS

## Residual Risk Notes

- Page-20 lyric OCR is low-confidence in several tokens; structure and sequence are stable.
- Recommended next step: process pages 21-22 and cross-check recurring culinary/song terms before scene-level lock.
