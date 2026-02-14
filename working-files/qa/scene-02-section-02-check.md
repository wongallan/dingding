# QA Check — Scene 02 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 7-8
- Extracted source file: `working-files/extracted/scene-02-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-02.md`

## Checks

1. Completeness check
- Extracted line IDs: 38 (`S02-SEC02-L001` to `S02-SEC02-L038`)
- Written triplets in scene section: 38
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Result: PASS

3. Speaker/content check
- Butler-training and breakfast-protocol exchanges preserved with normalized OCR text.
- One dropped speaker label on page 8 recovered by dialogue flow (`S02-SEC02-L029`, Yiu-Yiu).
- `芬尼/麥芬尼` treated as same role provisionally and normalized to `芬尼` pending clearer OCR.
- Result: PASS (with provisional normalization notes in extraction file)

4. Format check
- Each written entry in `scene-02.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions and audience-lighting cues excluded from triplet entries.
- Result: PASS

## Notes

- OCR confidence on pages 7-8 remains mixed; dish/item lexeme `魚水波蛋` and one honorific phrasing (`貴族早餐指引`) should be re-checked during Scene 02 scene-level QA.
