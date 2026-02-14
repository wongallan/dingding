# QA Check — Scene 07 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 29-30
- Extracted source file: `working-files/extracted/scene-07-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-07.md`

## Checks

1. Completeness check
- Extracted line IDs: 37 (`S07-SEC02-L001` to `S07-SEC02-L037`)
- Written triplets in Scene 07 Section 2: 37
- Result: PASS

2. Order check
- Verified triplet sequence matches staged line IDs and page flow 29→30.
- Dialogue handoff, peer-learning transition, `新節奏` song block, and scene close line remain in source order.
- Result: PASS

3. Speaker/content check
- Speaker labels retained in extraction staging and omitted from final triplets per booklet format.
- Mixed-language tokens (`Baby no... gentleman`) preserved where source style indicates code-switching.
- Result: PASS (with residual OCR uncertainty notes)

4. Format check
- Each Section 2 entry in `scene-07.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only movement/cue lines excluded from final triplets.
- Parenthetical delivery markers are retained only when embedded in spoken/sung lines.
- Result: PASS

## Residual Risk Notes

- Targeted hardening review completed for `S07-SEC02-L021`, `L025`, and `L029`; existing wording is retained as OCR-supported and stable for publication output.