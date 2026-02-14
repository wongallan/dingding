# QA Check — Scene 09 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 35-36
- Extracted source file: `working-files/extracted/scene-09-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-09.md`

## Checks

1. Completeness check
- Extracted line IDs: 35 (`S09-SEC01-L001` to `S09-SEC01-L035`)
- Written triplets in Scene 09 Section 1: 35
- Result: PASS

2. Order check
- Verified triplet sequence matches staged IDs and page flow 35→36.
- Ceremony setup, missing-award panic, search-method sequence, recovery/cleaning sequence, and result reveal remain in source order.
- Result: PASS

3. Speaker/content check
- Speaker labels retained in extraction staging and omitted from final triplets per booklet format.
- Embedded delivery markers and mixed-language tokens (`Stop`, `Oh…No signal…`) retained only when spoken.
- Result: PASS (with residual lexeme uncertainty)

4. Format check
- Every Section 1 entry in `scene-09.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only lines (lighting, movement, projection, prop-only cues) excluded from final triplets.
- Result: PASS

## Residual Risk Notes

- Competition-object/title lexeme remains provisional (`愛叮堡榮譽` and OCR variants) and should be finalized using cleaner recurrence in pages 37-38 before Scene 09 scene-level lock.