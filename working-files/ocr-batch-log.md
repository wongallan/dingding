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

- Batch ID: B10
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 17-18
- Output file: working-files/ocr/batch-10-pages-17-18.md
- Confidence notes: Page 17 (Scene 04 closing song) is low-confidence and lyric-fragmented; page 18 clearly starts Scene 05 with cleaner structural markers.
- Unclear lines count: 10 (mostly lyric-token corruption in Scene 04 song block)
- Follow-up required: Run targeted single-page re-OCR on page 17 to harden final lyric wording before publication lock.

- Batch ID: B11
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 19-20
- Output file: working-files/ocr/batch-11-pages-19-20.md
- Confidence notes: Mixed OCR quality; page 19 dialogue is mostly recoverable with conservative normalization, while page 20 lyric block remains token-noisy.
- Unclear lines count: 6 (three dialogue lexemes and three lyric tokens with conservative reconstruction)
- Follow-up required: Cross-check low-confidence page-20 lyric terms during Scene 05 Section 03 processing (pages 21-22) and run targeted re-OCR only if term recurrence stays unstable.

- Batch ID: B12
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 21-22
- Output file: working-files/ocr/batch-12-pages-21-22.md
- Confidence notes: Page 21 is lyric-heavy with moderate-to-low OCR confidence but stable sequence; page 22 clearly begins Scene 06 with cast/location heading and was boundary-excluded from Scene 05 conversion.
- Unclear lines count: 5 (page-21 lyric lexemes normalized conservatively in extraction notes)
- Follow-up required: Optional targeted single-page re-OCR on page 21 to harden final lyric wording before publication lock; continue primary flow with Scene 06 from page 22.

- Batch ID: B13
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 23-23
- Output file: working-files/ocr/batch-13-pages-23-23.md
- Confidence notes: Mixed OCR quality with noise around competition title lexeme and some punctuation; dialogue flow and quiz-setup structure are recoverable.
- Unclear lines count: 4 (one competition-title token cluster and three low-confidence lexical tokens in setup lines)
- Follow-up required: Validate competition-title canonical wording against later recurring mentions during Scene 06 continuation.

- Batch ID: B14
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 24-25
- Output file: working-files/ocr/batch-14-pages-24-25.md
- Confidence notes: Mixed OCR quality; quiz lines are mostly recoverable while song-heavy clusters on page 25 are noisy and require conservative normalization.
- Unclear lines count: 9 (primarily lyric-token corruption and one trailing phrase fragment in magic-round setup)
- Follow-up required: Continue Scene 06 with next section pages and schedule targeted re-OCR hardening for low-confidence page-25 lyric lines before full scene lock.

- Batch ID: B15
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 26-27
- Output file: working-files/ocr/batch-15-pages-26-27.md
- Confidence notes: Page 26 is clean boundary material (`第六幕完`) with no spoken/sung lines; page 27 begins Scene 07 with dialogue and lyric content but mixed OCR confidence.
- Unclear lines count: 8 (mostly page-27 low-confidence lyric tokens and fragmented dialogue lines)
- Follow-up required: Close Scene 06 at page 26 boundary and start Scene 07 Section 01 extraction from page 27 (continue with next page for continuity).

- Batch ID: B16
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 28-28
- Output file: working-files/ocr/batch-16-pages-28-28.md
- Confidence notes: Mixed-to-low OCR confidence; dialogue cues are recoverable and lyric lines are heavily fragmented but sequence-stable.
- Unclear lines count: 10 (mostly lyric-token corruption in `我真的試了` tail and `靜靜守候` block)
- Follow-up required: Continue Scene 07 with next OCR batch (pages 29-30) and schedule targeted lyric hardening for pages 27-28.

- Batch ID: B17
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 29-30
- Output file: working-files/ocr/batch-17-pages-29-30.md
- Confidence notes: Mixed OCR quality with recoverable dialogue and low-confidence call/response lyric tokens in `新節奏`.
- Unclear lines count: 6 (mainly lyric-fragment bracket tokens and one noun token in song block)
- Follow-up required: Optional targeted lyric hardening re-OCR for Scene 07 pages 29-30 before publication lock; continue primary flow with Scene 08 from page 31.

- Batch ID: B18
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 31-32
- Output file: working-files/ocr/batch-18-pages-31-32.md
- Confidence notes: Mixed OCR quality; opening song lines are mostly recoverable, but page-32 action/dialogue has fragmented tokens around surveillance phrasing and one mid-clause floral line.
- Unclear lines count: 5 (two high-impact normalized lines tracked as hardening candidates, plus three minor lexical fragments normalized contextually)
- Follow-up required: Continue primary flow with Scene 08 Section 02 (pages 33-34) and keep targeted hardening task for `S08-SEC01-L009` and `S08-SEC01-L031`.

- Batch ID: B19
- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Source file: reference/叮叮魔法師劇本1-38.pdf
- Page range: 33-34
- Output file: working-files/ocr/batch-19-pages-33-34.md
- Confidence notes: Mixed OCR quality with recoverable dialogue and heavily degraded lyric clusters in `早餐小心意` refrain lines.
- Unclear lines count: 10 (mostly repetitive lyric-token corruption on page 34 and one breakfast-action line on page 33)
- Follow-up required: Continue primary flow with Scene 09 from page 35; keep targeted Scene 08 lyric hardening for `S08-SEC02-L030` to `S08-SEC02-L046`.
