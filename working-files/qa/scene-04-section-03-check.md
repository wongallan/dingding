# QA Check — Scene 04 Section 03

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 17
- Extracted source file: `working-files/extracted/scene-04-section-03-raw-dialogue.md`
- Target script file: `booklet/script/scene-04.md`

## Checks

1. Completeness check
- Extracted line IDs: 25 (`S04-SEC03-L001` to `S04-SEC03-L025`)
- Written triplets in scene section: 25
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Narrative flow preserved from post-homework panic into lunch crisis song refrain.
- Result: PASS

3. Speaker/content check
- Speaker labels retained for named dialogue lines.
- Chorus lines grouped as `眾人（唱）` to preserve sung ensemble delivery.
- Result: PASS (with normalization notes)

4. Format check
- Each new entry in `scene-04.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions, bell cues, and movement lines are excluded from triplets.
- Result: PASS

## Hardening Pass (2026-02-14)

- Re-checked `working-files/ocr/batch-10-pages-17-18.md` against lyric lines `S04-SEC03-L016` to `S04-SEC03-L025`.
- Locked one OCR-supported wording correction:
  - `S04-SEC03-L023`: `無管家解決問題，個書包好重，點算好。`
  - → `無管家解決問題，個書包好重，落堂點算好。`
- Remaining lyric lines in this block are retained as conservative best reads under current OCR quality.

## Residual Risk Notes

- Page-17 lyric OCR remains noisy overall, but this section no longer has an open targeted hardening item.
