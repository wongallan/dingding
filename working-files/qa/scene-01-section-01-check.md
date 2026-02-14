# QA Check — Scene 01 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 1-2
- Extracted source file: `working-files/extracted/scene-01-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-01.md`

## Checks

1. Completeness check
- Extracted line IDs: 36 (`S01-SEC01-L001` to `S01-SEC01-L036`)
- Written triplets in scene section: 36
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID order.
- Result: PASS

3. Speaker check
- Speaker labels preserved: 總管 / 遙遙 / 安娜 / 達爾 / 遙、安、達.
- Result: PASS

4. Format check
- Each line uses strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions excluded as standalone entries.
- Two short parenthetical tone markers retained inside spoken lines for continuity.
- Result: PASS

## Notes

- OCR noise from logo/header and standalone numbers was filtered manually.
- Continue next section with the same filter rule before conversion.
