# Ding Ding Booklet Translation Plan (Cantonese Script → English Reference)

## Objective

Produce a complete English follow-along booklet for a live Cantonese children’s musical performance using the scaffold in `booklet/`.

Critical requirements:

- Include **every dialogue line** in `booklet/script/scene-01.md` through `scene-09.md` (no summaries in script files).
- Exclude stage directions from script line entries unless a line must be retained for dialogue continuity decisions.
- For songs, preserve artistic intent while staying faithful to source meaning (not purely literal translation).
- Work iteratively in small sections to reduce confusion across scenes/characters.

## Source Inventory (Current Workspace)

- `reference/叮叮魔法師劇本1-38.pdf` (large scanned PDF, ~14.8 MB)
- `reference/Ding_Wizard_01-1448x2048.jpg`
- `reference/Ding_Wizard_02-1448x2048.jpg`
- `reference/promo.txt` (marketing/context text)

## Non-Negotiable Process Constraints

1. Do **not** edit non-target scene files while processing a given section.
2. Keep an audit trail in `working-files/` before writing final booklet files.
3. Use OCR in batches (do not ingest full scanned PDF at once into context).
4. Use subagents/tools for OCR extraction to preserve main agent context window.
5. Run section-level QA before moving to next section.

---

## Workflow Overview

The work is split into three repeating phases per section:

1. **Extraction** (OCR + segmentation + speaker tagging)
2. **Conversion** (romanization + English translation)
3. **Checking** (line completeness + consistency + formatting)

Sections are processed in this granularity:

- Preferred: 2–4 PDF pages per batch
- Max: one logical mini-section of a scene at a time
- Never: an entire scene in one pass when OCR quality is uncertain

---

## Phase 0 — Setup and Shared Artifacts

Before translating any scene:

1. Initialize/refresh working files:
   - `working-files/scene-progress.md`
   - `working-files/character-name-map.md`
   - `working-files/place-term-glossary.md`
   - `working-files/song-style-decisions.md`
   - `working-files/ocr-batch-log.md`
2. Define canonical naming conventions:
   - Chinese character names (as-script)
   - Sidney Lau romanization for names
   - Approved English character names
3. Record unresolved terms under a “Needs Decision” section before continuing.

Deliverables after Phase 0:

- Stable glossary and name mapping files available on disk for all future agents.

---

## Phase 1 — Extraction (OCR + Dialogue Filtering)

### 1.1 OCR Strategy for Large Scanned PDF

Because `reference/叮叮魔法師劇本1-38.pdf` is scanned:

- Use OCR-capable tools/subagents in page batches (2–4 pages each).
- Persist each batch output to `working-files/ocr/batch-XX-pages-YY-ZZ.md`.
- For low-confidence lines, add an `[[unclear]]` marker and page reference.
- If OCR is poor, cross-check against nearby pages and available JPG assets.

### 1.2 Extraction Rules

For each OCR batch:

1. Separate dialogue from stage directions.
2. Keep spoken/sung text lines only.
3. Preserve line order exactly as performed.
4. Capture speaker labels exactly as source where possible.
5. Flag ambiguous speaker attribution in working files, not in final booklet output.
6. Remove decorative headers/logos, prop lists, and standalone printed line numbers before staging dialogue lines.

### 1.3 Section Staging File

Compile cleaned source lines into:

- `working-files/extracted/scene-0X-section-YY-raw-dialogue.md`

Required format:

- Line ID (stable): `S01-SEC02-L014`
- Page reference
- Speaker (Chinese)
- Chinese dialogue (verbatim)
- Notes (`unclear char`, `possible lyric`, etc.)

Extraction gate (must pass before conversion):

- No stage-direction lines remaining in staged dialogue file.
- No missing line-number sequence gaps unless explicitly documented.

---

## Phase 2 — Conversion (Romanization + English)

### 2.1 Romanization

For each staged line:

- Produce Sidney Lau romanization of full utterance.
- Keep proper nouns consistent with `working-files/character-name-map.md` and `working-files/place-term-glossary.md`.
- Re-check tone/segmentation on uncertain colloquial Cantonese phrasing.

### 2.2 English Translation Rules

Dialogue lines:

- Prioritize clarity for live follow-along audience.
- Preserve intent, emotional tone, and plot-critical meaning.
- Avoid over-condensing; one source line should map to one corresponding translated line block unless split is required for comprehension.

Song/lyric lines:

- Allow creative license for singability and artistic spirit.
- Still preserve semantic anchor points (who, what, emotional aim, key images).
- Document major adaptation choices in `working-files/song-style-decisions.md`.

### 2.3 Write to Target Scene File

Update `booklet/script/scene-0X.md` with strict per-line triplet format:

- Characters: …
- Sidney Lau romanization: …
- English translation: …

Do not add summaries into script files.

Conversion gate (must pass before checking):

- Every extracted line ID has a completed triplet.
- All names/places match shared glossary files.

---

## Phase 3 — Checking (Accuracy + Completeness + Consistency)

### 3.1 Intra-Section QA

For each section:

1. **Completeness check**: Count extracted lines vs written triplets.
2. **Order check**: Ensure triplets preserve source sequence.
3. **Speaker check**: Ensure speaker labels align with source intent.
4. **Format check**: Ensure template format is exactly followed.
5. **Exclusion check**: Verify stage directions are not included as dialogue entries.
6. **Scene-boundary ownership check**: If an OCR batch spans two scenes, assign each dialogue line to the correct scene file (do not leave next-scene anchor lines in prior scene output).

Log results in `working-files/qa/scene-0X-section-YY-check.md`.

### 3.2 Scene-Level QA

After all sections in a scene are done:

- Run full scene pass for terminology consistency and narrative continuity.
- Verify no duplicate or dropped lines at section boundaries.
- Mark scene status in `working-files/scene-progress.md`.

### 3.3 Cross-Scene QA

After multiple scenes:

- Compare recurring catchphrases, magical terms, relationship titles.
- Normalize approved translations globally only after confirming no context break.

---

## Iterative Execution Plan (Per Scene)

Repeat this loop for `scene-01` to `scene-09`:

1. Identify source page range(s) for next mini-section.
2. OCR only that batch via subagent/tool.
3. Save raw OCR batch file.
4. Clean and extract dialogue-only staged lines.
5. Convert to romanization + English.
6. Update target scene markdown.
7. Run section QA checks.
8. Commit status to working files.
9. Continue to next mini-section.

Recommended stop points:

- End of each mini-section
- End of each scene

At each stop point, update:

- `working-files/scene-progress.md`
- `working-files/ocr-batch-log.md`
- `working-files/song-style-decisions.md` (if songs touched)

---

## Assignment Model for Multiple Agents

Since future agents may not have prior chat history, each agent must:

1. Read first:
   - `PLAN.md`
   - `working-files/scene-progress.md`
   - `working-files/character-name-map.md`
   - `working-files/place-term-glossary.md`
   - `working-files/song-style-decisions.md`
2. Claim one scene section only.
3. Produce/update required extraction + QA logs.
4. Hand off with explicit “next unresolved items” list.

Handoff block format (append to scene progress file):

- Completed: scene, section, source pages
- Outstanding: unclear OCR lines, unresolved terms
- Decisions made: glossary/song translation choices
- Next action: exact next section/page range

---

## Quality Criteria (Definition of Done)

A scene is done when:

- Every dialogue/sung line from source for that scene is represented as a triplet.
- No stage directions are included as dialogue triplets.
- Romanization is present for every source line.
- English is readable, faithful, and context-appropriate.
- Song lines reflect both literal meaning anchors and artistic intent.
- Scene passes section-level and scene-level QA logs.

The booklet is done when:

- All `booklet/script/scene-01.md` … `scene-09.md` satisfy scene done criteria.
- `booklet/characters.md` aligns with finalized name mappings.
- `booklet/scene-synopsis.md` and `booklet/overview.md` are consistent with final script outcomes.

---

## Risk Controls and Error Prevention

- **OCR drift risk**: Keep batch sizes small and persist page references.
- **Low-confidence lyric OCR risk**: If lyric-heavy pages are heavily degraded, complete a conservative first pass with explicit `[[unclear]]` notes, then add a targeted re-OCR follow-up task (single-page, higher DPI or alternate OCR settings) before final scene lock.
- **Speaker confusion risk**: Enforce stable line IDs and section boundaries.
- **Terminology drift risk**: Update glossary before editing later scenes.
- **Lyric over-adaptation risk**: Track adaptation rationale in song decisions file.
- **Scene 08 breakfast-song OCR risk**: Pages 33-34 include repetitive low-confidence lyric tokens; track targeted hardening for `S08-SEC02-L030` to `S08-SEC02-L046` before publication lock.

---

## Current Verified Checkpoint (2026-02-14)

- Scenes 01-08: Converted and section-checked; Scene 08 closed at page 34 (`第八幕完`).
- Highest-priority production work: Start Scene 09 Section 01 from pages 35-36.
- Open hardening backlog: targeted lyric/dialogue re-OCR items tracked in `working-files/todo.md`.

## Active Follow-ups (Updated 2026-02-14)

- Scene 06 full-scene QA completed; boundary lock confirmed via page 26 (`第六幕完`, stage-direction-only).
- Keep targeted single-page re-OCR hardening task for page-25 lyric lines (`S06-SEC02-L058`, `S06-SEC02-L061`, `S06-SEC02-L062`) as publication-quality follow-up.
- Scene 07 full-scene QA completed; boundary lock confirmed via page 30 (`第七幕完`).
- Keep targeted lyric hardening task for Scene 07 low-confidence tokens (`S07-SEC01-L010`; `S07-SEC02-L021`, `L025`, `L029`) as publication-quality follow-up.
- Keep competition-title lexeme (`愛叮堡榮譽`) provisional until confirmed by cleaner recurrence in Scene 07+ pages.

## Active Open Issues (Rolling)

- Competition-title OCR noise in Scene 06 page-23 (`愛叮堡樊盃/榮譽` variants): keep provisional normalization in section output, then lock canonical term only after recurrence on clearer pages.

---

## Execution Status Snapshot (2026-02-14)

- Scenes completed: 01-07
- Current highest-priority pending task: start Scene 08 Section 01 from pages 31-32.
- Non-blocking hardening follow-ups discovered during Scene 05 close-out:
   - Optional targeted re-OCR of Scene 04 page-17 lyric block.
   - Optional targeted re-OCR of Scene 05 page-21 lyric block.

---

## Execution Updates

### 2026-02-14

- Verified highest-priority unfinished task via outputs/tracking: Scene 05 Section 01 (page 18) was not yet extracted/converted.
- Completed Scene 05 Section 01 pipeline end-to-end:
   - Extraction staged in `working-files/extracted/scene-05-section-01-raw-dialogue.md`
   - Conversion written to `booklet/script/scene-05.md`
   - Section QA logged in `working-files/qa/scene-05-section-01-check.md`
- New/active follow-up tasks discovered during execution:
   1. OCR next batch for Scene 05 continuity (`pages 19-20`) before Section 02 conversion.
   2. Re-check low-confidence tokens from Scene 05 Section 01 (`S05-SEC01-L005`, `L007`, `L015`) against next-page context.
   3. Keep Scene 04 page-17 lyric targeted re-OCR hardening as non-blocking publication-quality task.
 - Completed follow-up task: Scene 05 Section 02 (pages 19-20) OCR + extraction + conversion + section QA is now done.
 - New/active follow-up tasks after Section 02:
   1. OCR/process Scene 05 Section 03 (`pages 21-22`) and continue section loop.
   2. Cross-check conservative Section 02 lexemes (`S05-SEC02-L018`, `L028`, `L032`) against next-page recurrence.
   3. Keep Scene 04 page-17 lyric targeted re-OCR hardening as non-blocking publication-quality task.

---

## Live Execution Updates (2026-02-14)

- Scene 04 Section 03 source (page 17) is completed with conservative lyric normalization due low OCR confidence.
- New follow-up task: targeted single-page re-OCR hardening for page 17 lyric block before publication lock.
- Scene boundary confirmed: Scene 04 closes at `第四幕完` (page 17), Scene 05 starts at page 18 (`第五幕`).

---

## Active Follow-Up Queue (Discovered During Execution)

- 2026-02-14: Scene 04 Section 02 (pages 15-16) required five heavy OCR normalizations (`S04-SEC02-L001`, `L007`, `L019`, `L033`, `L041`).
- Action: run targeted re-OCR for pages 15-16 (alternate DPI/model) before final scene lock if higher-confidence source can be produced.
- **Missed lines risk**: Mandatory extracted-vs-written line count check per section.
- **Boundary bleed risk**: When one page includes a scene transition, perform immediate boundary reconciliation before locking section/scene QA.

## Active Next Task

- Process `Scene 08 / Section 01` from pages 31-32 and continue the extraction → conversion → QA loop.

## Active OCR Follow-Ups (2026-02-14)

- Scene 02 pages 7-8 produced four provisional normalizations reviewed during Scene 02 scene-level QA:
   - dish/item lexeme currently normalized as `魚水波蛋`
   - protocol phrase currently normalized as `貴族早餐指引`
   - speaker label variant `芬尼` vs `麥芬尼`
   - one imperative particle in `S02-SEC02-L021`
- Pages 9-10 did not provide clear recurrence for final lexical confirmation; keep these as explicitly tracked provisional normalizations until cleaner source evidence appears.
- Scene 03 page 12 ends with a truncated dialogue line (virus/sneezing line); treat as mandatory carry-over reconciliation at Scene 03 Section 02 start before scene-level QA.

---

## Execution Updates (Living)

- 2026-02-14: Scene 01 Section 01 completed (pages 1-2), QA passed.
- 2026-02-14: Scene 01 Section 02 completed (pages 3-4), QA passed.
- 2026-02-14: Scene 01 Section 03 completed (page 5 scene-ending lines), QA passed; page-boundary continuation from `S01-SEC02-L051` reconciled.
- Carry-over task completed: reconciled page-boundary continuation from `S01-SEC02-L051` before assigning Section 03 IDs.
- New term-validation task: verify final spellings/meaning for `比卡特羅家族` and `愛叮堡榮譽` against clearer OCR in next batch before locking global glossary.
- Scene boundary discovered: page 6 starts Scene 2 (`第二幕`), so Scene 01 extraction scope closes at page 5.
- 2026-02-14: Scene 02 Section 01 completed (page 6), extraction + conversion + section QA passed; heavy OCR normalizations documented line-by-line in staged extraction.
- 2026-02-14: Scene 02 Section 02 completed (pages 7-8), extraction + conversion + section QA passed.
- 2026-02-14: Scene 02 Section 03 completed (pages 9-10), extraction + conversion + section QA passed; lyric-heavy OCR normalized conservatively with uncertainty notes.
- 2026-02-14: Scene 02 scene-level QA completed and Scene 02 marked done (pages 6-10).
- 2026-02-14: Scene 03 Section 01 completed (pages 11-12), extraction + conversion + section QA passed; one end-of-page carry-over line explicitly tracked (`S03-SEC01-L041`).
- 2026-02-14: Scene 06 full-scene QA completed; page-26 OCR verifies `第六幕完` with no spoken/sung lines, so Scene 06 closes after Section 02.
- 2026-02-14: Scene 07 Section 01 completed (pages 27-28), extraction + conversion + section QA passed; mixed-confidence lyric blocks were normalized conservatively with residual risk notes.
- 2026-02-14: Scene 07 Section 02 completed (pages 29-30), extraction + conversion + section QA passed; `新節奏` call/response block normalized conservatively with explicit low-confidence markers.
- 2026-02-14: Scene 07 full-scene QA completed and Scene 07 marked done (pages 27-30).
- 2026-02-14: Scene 08 Section 01 completed (pages 31-32), extraction + conversion + section QA passed; opening `重新起步` song and butler-observation dialogue converted with conservative normalization for fragmented OCR tokens.
- 2026-02-14: Scene 09 Section 01 completed (pages 35-36), extraction + conversion + section QA passed; opening ceremony + search drill sequence locked with conservative normalization.

## Discovered Constraints (2026-02-14)

- RapidOCR on this PDF is workable but noisy on title/header regions; manual normalization is required before conversion.
- Page-level OCR output includes artifacts (branding text, isolated numerals, and partial props notes) that must be filtered during extraction.
- For uncertain OCR tokens, normalize only when context is strong; otherwise retain `[[unclear]]` in extracted files and defer final wording.
- Scene 02 page 6 includes dense OCR artifacts in lyric blocks and butler dialogue; prioritize adjacent-page context validation in the next batch (pages 7-8) before locking long-form lexical choices globally.
- Scene 03 pages 11-12 contain heavier line-fragmentation and mixed-script OCR drift than Scene 02; preserve conservative normalization and avoid aggressive lexical reconstruction without adjacent-page confirmation.
- Scene 07 pages 27-28 continue the same OCR drift pattern in lyric-heavy zones (`我真的試了`, `靜靜守候`); preserve sequence-first normalization and track low-confidence tokens explicitly for hardening passes.

## Newly Discovered Follow-Up Tasks (2026-02-14)

- Run targeted re-OCR hardening for Scene 07 pages 27-30 lyric clusters before publication lock.
- Resolve low-confidence addressee token in `S07-SEC01-L010` (`阿叮` provisional) when clearer recurrence appears.
- Resolve low-confidence `新節奏` bracket tokens in `S07-SEC02-L021`, `L025`, and `L029` when cleaner recurrence appears.
- Keep competition title lexeme (`愛叮堡榮譽` variants) as provisional until a cleaner recurrence in later Scene 07/08 OCR confirms canonical wording.
- Run targeted hardening re-OCR for Scene 08 page-31/32 low-confidence lines `S08-SEC01-L009` and `S08-SEC01-L031` before publication lock.
- Resolve competition-object lexeme ambiguity in Scene 09 (`愛叮堡榮譽` vs OCR variants like `榮益/樊益`) using next batch recurrence before final glossary lock.

---

## Immediate Next Action

Continue with Scene 9, Section 2:

1. OCR pages 37-38 and save batch output under `working-files/ocr/`.
2. Extract dialogue-only lines with fresh `S09-SEC02-Lxxx` IDs.
3. Convert and append triplets in `booklet/script/scene-09.md`.
4. Run section QA, then execute Scene 09 scene-level QA when remaining sections are complete.
