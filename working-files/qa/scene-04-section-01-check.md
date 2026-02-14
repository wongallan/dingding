# QA Check — Scene 04 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 14
- Extracted source file: `working-files/extracted/scene-04-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-04.md`

## Checks

1. Completeness check
- Extracted line IDs: 24 (`S04-SEC01-L001` to `S04-SEC01-L024`)
- Written triplets in scene section: 24
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Scene-opening chorus lines from page 14 correctly belong to Scene 04 (not Scene 03).
- Result: PASS

3. Speaker/content check
- Chorus, home dialogue, and TV broadcast sequence preserved in narrative order.
- Low-confidence OCR normalizations are explicitly tracked in extraction notes (`S04-SEC01-L015`, `S04-SEC01-L021`).
- Result: PASS (with uncertainty notes)

4. Format check
- Each written entry in `scene-04.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions, branding/header artifacts, and standalone printed numbers were excluded from triplet entries.
- Result: PASS
