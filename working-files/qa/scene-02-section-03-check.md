# QA Check — Scene 02 Section 03

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 9-10
- Extracted source file: `working-files/extracted/scene-02-section-03-raw-dialogue.md`
- Target script file: `booklet/script/scene-02.md`

## Checks

1. Completeness check
- Extracted line IDs: 47 (`S02-SEC03-L001` to `S02-SEC03-L047`)
- Written triplets in scene section: 47
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Result: PASS

3. Speaker/content check
- Dar/O-Miu-Nei breakfast dialogue, Bibi table-service exchanges, and butler-anthem sequence are preserved in source order.
- OCR remained noisy on several lyric lexemes; uncertain tokens were normalized conservatively and noted in extraction file.
- Result: PASS (with normalization notes)

4. Format check
- Each written entry in `scene-02.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only cues were excluded from triplet entries.
- Result: PASS
