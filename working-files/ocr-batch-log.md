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

- Batch ID: B03
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 5-6
- Output file: working-files/ocr/batch-03-pages-05-06.md
- Confidence notes: Page 5 end-of-scene lines recoverable with normalization; page 6 introduces Scene 2 and remains out of scope for this increment.
- Unclear lines count: 2 (speaker labels missing on two recoverable dialogue lines in page 5)
- Follow-up required: Start Scene 02 Section 01 from page 6 onward with fresh IDs and character mapping updates.

- Batch ID: B04
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 6-6
- Output file: working-files/ocr/batch-04-pages-06-06.md
- Confidence notes: Mixed-to-low OCR quality on lyric and dialogue lines; requires line-level normalization and artifact filtering.
- Unclear lines count: 5 (degraded lexical tokens normalized contextually in extraction notes)
- Follow-up required: Continue Scene 02 with next OCR batch (pages 7-8) and re-check any provisional lexical reconstructions.

- Batch ID: B05
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 7-8
- Output file: working-files/ocr/batch-05-pages-07-08.md
- Confidence notes: Mixed OCR quality with multiple split lines and one dropped speaker label; normalization required for butler-protocol dialogue and table-service segment.
- Unclear lines count: 4 (`魚水波蛋` lexeme, `貴族早餐指引` phrasing, `芬尼/麥芬尼` label variant, one imperative particle in `S02-SEC02-L021`)
- Follow-up required: Re-check pages 8-9 during Scene 02 scene-level QA for lexical confirmation and final name-label lock.

- Batch ID: B06
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 9-10
- Output file: working-files/ocr/batch-06-pages-09-10.md
- Confidence notes: Mixed-to-low OCR quality on lyric-heavy page 10; scene-level structure recoverable with conservative normalization.
- Unclear lines count: 6 (mostly lyric token degradation and one page-9 timephrase lexeme)
- Follow-up required: Carry unresolved lyric-token uncertainty to cross-scene terminology normalization if a cleaner source version becomes available.

- Batch ID: B07
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 11-12
- Output file: working-files/ocr/batch-07-pages-11-12.md
- Confidence notes: Low-to-mixed OCR quality with heavy header/noise artifacts and split speaker lines; dialogue remains recoverable with conservative normalization.
- Unclear lines count: 3 (one angle-token ambiguity resolved contextually and one page-boundary truncated line carried forward)
- Follow-up required: Reconcile carry-over line from page 12 to page 13 at start of Scene 03 Section 02 before scene-level QA.

- Batch ID: B08
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 13-14
- Output file: working-files/ocr/batch-08-pages-13-14.md
- Confidence notes: Low OCR quality on page-13 lyric cluster with heavy token corruption; dialogue skeleton recoverable using conservative normalization and continuity anchors.
- Unclear lines count: 2 (song lexemes normalized conservatively in `S03-SEC02-L010` and `S03-SEC02-L016`)
- Follow-up required: Run targeted re-OCR for page 13 with alternate settings before final lock of lyric wording, if cleaner source is available.

- Batch ID: B09
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 15-16
- Output file: working-files/ocr/batch-09-pages-15-16.md
- Confidence notes: Mixed OCR quality with frequent line fragmentation and multilingual token noise; classroom dialogue flow recoverable with conservative normalization.
- Unclear lines count: 5 (`S04-SEC02-L001`, `L007`, `L019`, `L033`, `L041` required heavier reconstruction)
- Follow-up required: Optional targeted re-OCR of pages 15-16 to harden normalized lexemes before final Scene 04 scene-level lock.
