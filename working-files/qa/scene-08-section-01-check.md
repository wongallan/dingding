# QA Check — Scene 08 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 31-32
- Extracted source file: `working-files/extracted/scene-08-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-08.md`

## Checks

1. Completeness check
- Extracted line IDs: 34 (`S08-SEC01-L001` to `S08-SEC01-L034`)
- Written triplets in Scene 08 Section 1: 34
- Result: PASS

2. Order check
- Verified triplet sequence matches staged line IDs and page flow 31→32.
- Opening song lines are followed by garden-observation dialogue and independence-monitoring exchange in source order.
- Result: PASS

3. Speaker/content check
- Speaker labels retained in extraction staging and omitted from final triplets per booklet format.
- Mixed-language token `Baby` is preserved where source style indicates code-switching.
- Result: PASS (with residual OCR uncertainty notes)

4. Format check
- Each Section 1 entry in `scene-08.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only movement/cue lines excluded from final triplets.
- Parenthetical delivery markers retained only when embedded in spoken dialogue.
- Result: PASS

## Residual Risk Notes

- Targeted hardening pass completed for `S08-SEC01-L009` and `S08-SEC01-L031` using `working-files/ocr/batch-18-pages-31-32.md` recurrence.
- No remaining high-impact unresolved tokens in Section 01.