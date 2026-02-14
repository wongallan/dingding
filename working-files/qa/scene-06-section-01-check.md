# QA Check — Scene 06 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 22-23
- Extracted source file: `working-files/extracted/scene-06-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-06.md`

## Checks

1. Completeness check
- Extracted line IDs: 38 (`S06-SEC01-L001` to `S06-SEC01-L038`)
- Written triplets in scene section: 38
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Butler-release sequence, competition setup, and first quiz prompts remain in source order.
- Result: PASS

3. Speaker/content check
- Speaker labels preserved in extraction staging and omitted from final script triplets per scene format.
- Low-confidence lexical segments remain conservative and explicitly tracked in notes.
- Result: PASS (with uncertainty notes)

4. Format check
- Each entry in `scene-06.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only lines are excluded from script triplets.
- Entrances/light cues/crowd movement remain excluded from dialogue output.
- Result: PASS

## Residual Risk Notes

- Competition title lexeme is OCR-noisy and remains provisional (`愛叮堡榮譽`) pending further recurrence validation.