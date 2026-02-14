# QA Check — Scene 09 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 37-38
- Extracted source file: `working-files/extracted/scene-09-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-09.md`

## Checks

1. Completeness check
- Extracted line IDs: 61 (`S09-SEC02-L001` to `S09-SEC02-L061`)
- Written triplets in Scene 09 Section 2: 61
- Result: PASS

2. Order check
- Verified triplet sequence matches staged IDs and page flow 37→38.
- Dialogue-resolution block precedes award announcements and finale song lines.
- Result: PASS

3. Speaker/content check
- Speaker labels retained in extraction staging and omitted from final triplets per booklet format.
- Stage-direction-only action lines are excluded from triplets; spoken parenthetical delivery markers are retained where part of speech.
- Result: PASS

4. Format check
- Every Section 2 entry in `scene-09.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Decorative headers, printed line numbers, and non-spoken footer/cast artifacts removed.
- `(全劇完)` is treated as stage direction and excluded from triplet payload.
- Result: PASS

## Residual Risk Notes

- Finale song pages are OCR-noisy; current text is conservative normalization preserving sequence and core semantic motifs.
