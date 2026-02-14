# QA Check — Scene 01 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 3-4
- Extracted source file: `working-files/extracted/scene-01-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-01.md`

## Checks

1. Completeness check
- Extracted line IDs: 51 (`S01-SEC02-L001` to `S01-SEC02-L051`)
- Written triplets in scene section: 51
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID order.
- Result: PASS

3. Speaker check
- Speaker labels preserved/normalized: 眾人 / 比比 / 達爾 / 露露 / 遙遙 / 安娜 / 菲菲 / 芳花 / 小志.
- Result: PASS

4. Format check
- Each line uses strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Standalone stage directions excluded as dialogue entries.
- Parenthetical tone/action markers retained only where embedded in spoken lines.
- Result: PASS

## Notes

- OCR quality on pages 3-4 is noisy; several lines were manually normalized and consolidated where OCR split lyric fragments.
- `S01-SEC02-L051` is intentionally marked incomplete because source text continues onto page 5; boundary reconciliation is required at start of Section 03.
- Term spellings `比卡特羅家族` and `愛叮堡榮譽` remain provisional pending clearer OCR in next batch.
