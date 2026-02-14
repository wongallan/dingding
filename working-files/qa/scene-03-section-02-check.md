# QA Check — Scene 03 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 13-14
- Extracted source file: `working-files/extracted/scene-03-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-03.md`

## Checks

1. Completeness check
- Extracted line IDs: 20 (`S03-SEC02-L001` to `S03-SEC02-L020`)
- Written triplets in scene section: 20
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Carry-over line from prior section (`S03-SEC01-L041`) is explicitly completed as `S03-SEC02-L001`.
- Result: PASS

3. Speaker/content check
- Emergency announcement and quarantine-panic sequence preserved.
- Lyric lines with heavy OCR degradation were conservatively normalized and documented (`S03-SEC02-L010`, `S03-SEC02-L016`).
- Page 14 starts next scene context (`第四幕`); boundary-opening chorus lines are assigned to Scene 04 Section 01.
- Result: PASS (with uncertainty notes)

4. Format check
- Each written entry in `scene-03.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions, branding/header artifacts, and standalone printed numbers were excluded from triplet entries.
- Result: PASS
