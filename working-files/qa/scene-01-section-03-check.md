# QA Check — Scene 01 Section 03

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 5 (Scene 1 ending)
- Extracted source file: `working-files/extracted/scene-01-section-03-raw-dialogue.md`
- Target script file: `booklet/script/scene-01.md`

## Checks

1. Completeness check
- Extracted line IDs: 11 (`S01-SEC03-L001` to `S01-SEC03-L011`)
- Written triplets in scene section: 11
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID order.
- Result: PASS

3. Speaker check
- Recoverable speaker labels preserved; two lines flagged `[[unclear]]` in extraction due to OCR speaker-label loss.
- Result: PASS (with documented uncertainty only in working file)

4. Format check
- Each line uses strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Standalone stage directions excluded as dialogue entries.
- Parenthetical cue retained only where embedded in a spoken line.
- Result: PASS

## Notes

- Required carry-over reconciliation completed: `S01-SEC02-L051` remains an interrupted line ending with ellipsis; first recoverable continuation after interruption is tracked in `S01-SEC03-L001`.
- Terms `比卡特羅家族` / `愛叮堡榮譽` remain provisional and should be revalidated when cleaner occurrences appear.