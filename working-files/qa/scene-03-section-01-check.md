# QA Check — Scene 03 Section 01

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source pages: 11-12
- Extracted source file: `working-files/extracted/scene-03-section-01-raw-dialogue.md`
- Target script file: `booklet/script/scene-03.md`

## Checks

1. Completeness check
- Extracted line IDs: 41 (`S03-SEC01-L001` to `S03-SEC01-L041`)
- Written triplets in scene section: 41
- Result: PASS

2. Order check
- Verified triplet order follows staged line ID sequence.
- Result: PASS

3. Speaker/content check
- Butler summit code-recitation, complaint review, and procedural Q&A flow preserved in source order.
- One line is intentionally page-boundary truncated (`S03-SEC01-L041`) and marked for immediate carry-over reconciliation in next section.
- Result: PASS (with carry-over note)

4. Format check
- Each written entry in `scene-03.md` follows strict triplet format:
  - Characters
  - Sidney Lau romanization
  - English translation
- Result: PASS

5. Exclusion check
- Stage-direction-only cues and branding/header artifacts were excluded from triplet entries.
- Result: PASS
