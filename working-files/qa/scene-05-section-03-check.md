# QA Check — Scene 05 Section 03

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 21 (with page-22 Scene 06 boundary excluded)
- Extracted source file: `working-files/extracted/scene-05-section-03-raw-dialogue.md`
- Target script file: `booklet/script/scene-05.md`

## Checks

1. Completeness check
- Extracted line IDs: 46 (`S05-SEC03-L001` to `S05-SEC03-L046`)
- Written triplets in scene section: 46
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Song continuation, kitchen mishap, and butler re-entry beats are preserved.
- Result: PASS

3. Speaker/content check
- Speaker tags are retained in extraction staging and omitted from final script triplets per scene format.
- Mixed-language token (`Baby`) retained where present in source style.
- Result: PASS (with uncertainty notes)

4. Format check
- Each entry in `scene-05.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-only movement/cue lines are excluded from triplet entries.
- Page-22 scene heading/personnel block is excluded from Scene 05 ownership.
- Result: PASS

## Residual Risk Notes

- Page-21 lyric OCR remains low-confidence in a few lexemes; section structure and continuity are stable.
- Optional targeted single-page re-OCR can harden final lyric wording before publication lock.