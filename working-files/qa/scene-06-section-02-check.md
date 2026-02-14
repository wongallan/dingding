# QA Check — Scene 06 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 24-25
- Extracted source file: `working-files/extracted/scene-06-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-06.md`

## Checks

1. Completeness check
- Extracted line IDs: 66 (`S06-SEC02-L001` to `S06-SEC02-L066`)
- Written triplets in scene section: 66
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence across pages 24→25.
- Knowledge-round completion, magic-round setup, two challenge rounds, and result reveal remain in source order.
- Result: PASS

3. Speaker/content check
- Speaker labels preserved in extraction staging and omitted from final script triplets per scene format.
- Song clusters are OCR-noisy; conservative normalization was used with explicit residual-risk notes.
- Result: PASS (with uncertainty notes)

4. Format check
- Each entry in `scene-06.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only lines are excluded from script triplets.
- Only spoken/sung content retained.
- Result: PASS

## Residual Risk Notes

- Targeted page-25 lyric hardening completed for `S06-SEC02-L058`, `S06-SEC02-L061`, and `S06-SEC02-L062` by OCR re-read and wording lock.
- No blocking section-level residual risk remains for these lines after hardening.
