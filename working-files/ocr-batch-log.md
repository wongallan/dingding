# OCR Batch Log

Track all OCR extraction batches from scanned sources.

## Entry Template

- Batch ID:
- Date:
- Agent:
- Source file:
- Page range:
- Output file:
- Confidence notes:
- Unclear lines count:
- Follow-up required:

## Batches

- Batch ID: B01
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 1-2
- Output file: working-files/ocr/batch-01-pages-01-02.md
- Confidence notes: Mixed OCR quality; dialogue mostly recoverable with manual normalization. Decorative header, line numbers, and prop text created noise.
- Unclear lines count: 3 (minor lexical uncertainty, resolved contextually)
- Follow-up required: Continue with pages 3-4; apply pre-filter for branding/header and standalone line numbers.

- Batch ID: B02
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 3-4
- Output file: working-files/ocr/batch-02-pages-03-04.md
- Confidence notes: Low-to-mixed OCR quality on lyric-heavy lines; substantial normalization required for song and confrontation segment.
- Unclear lines count: 4 (competition-title nouns and one page-boundary carry-over line)
- Follow-up required: Reconcile carry-over line from page 4 into page 5 and confirm terms `比卡特羅家族` / `愛叮堡榮譽` during next batch.
