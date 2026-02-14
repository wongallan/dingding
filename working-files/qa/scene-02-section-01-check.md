# QA Check — Scene 02 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 6
- Extracted source file: `working-files/extracted/scene-02-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-02.md`

## Checks

1. Completeness check
- Extracted line IDs: 37 (`S02-SEC01-L001` to `S02-SEC01-L037`)
- Written triplets in scene section: 37
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Result: PASS

3. Speaker/content check
- Song lines grouped under `唱` in extraction and preserved as standalone lyric lines in script triplets.
- Dialogue lines mapped to `貝琪` / `哈娜` / `總管` with normalized wording where OCR was degraded.
- Result: PASS (with normalization notes documented in extraction file)

4. Format check
- Each written entry in `scene-02.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Scene metadata (`時間/地點/人物`), decorative headers, and stage directions excluded from triplet entries.
- Result: PASS

## Notes

- OCR confidence remains mixed on page 6; several lexical normalizations were required and are explicitly tracked per line in the extracted staging file.
- Next section should continue from page 7 with fresh `S02-SEC02-Lxxx` IDs.
