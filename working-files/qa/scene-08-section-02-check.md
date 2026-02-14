# QA Check — Scene 08 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 33-34
- Extracted source file: `working-files/extracted/scene-08-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-08.md`

## Checks

1. Completeness check
- Extracted line IDs: 48 (`S08-SEC02-L001` to `S08-SEC02-L048`)
- Written triplets in Scene 08 Section 2: 48
- Result: PASS

2. Order check
- Verified triplet sequence matches staged line IDs and page flow 33→34.
- Dialogue block (self-cooking + butler observation) precedes `早餐小心意` song block, then closing thanks line.
- Result: PASS

3. Speaker/content check
- Speaker labels retained in extraction staging and omitted from final triplets per booklet format.
- Mixed-language tokens (`Baby`, `I got this`) preserved where source style indicates code-switching.
- Result: PASS (with residual OCR uncertainty notes)

4. Format check
- Each Section 2 entry in `scene-08.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only movement/cue lines excluded from final triplets.
- Parenthetical delivery markers retained only when embedded in spoken lines.
- Result: PASS

## Residual Risk Notes

- Targeted hardening pass completed for `S08-SEC02-L030` to `S08-SEC02-L046` using batch-19 OCR recurrence.
- Wording lock applied to `S08-SEC02-L041`: `即使都不怕，共對已足。` (removed prior over-normalized `跌倒` token).
- Remaining Section 02 uncertainty is limited to one dialogue action phrasing in `S08-SEC02-L010`.
