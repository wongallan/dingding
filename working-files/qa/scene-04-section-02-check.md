# QA Check — Scene 04 Section 02

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 15-16
- Extracted source file: `working-files/extracted/scene-04-section-02-raw-dialogue.md`
- Target script file: `booklet/script/scene-04.md`

## Checks

1. Completeness check
- Extracted line IDs: 46 (`S04-SEC02-L001` to `S04-SEC02-L046`)
- Written triplets in scene section: 46
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Page transition from 15 to 16 is preserved without dropped boundary lines.
- Result: PASS

3. Speaker/content check
- Speaker attributions preserved for class-entry dialogue blocks and teacher announcements.
- Mixed-language exclamations (`Baby`, `Too bad`, `Water, I need water`) retained where present in source style.
- Result: PASS (with normalization notes)

4. Format check
- Each new entry in `scene-04.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage directions and movement cues remain excluded from triplet entries.
- One offstage call (`書外聲`) retained as spoken line for continuity.
- Result: PASS

## Residual Risk Notes

- OCR quality for pages 15-16 is low-to-mixed; five lines required heavier normalization (`S04-SEC02-L001`, `L007`, `L019`, `L033`, `L041`).
- Recommend optional targeted re-OCR before final lock if a higher-confidence text source becomes available.
