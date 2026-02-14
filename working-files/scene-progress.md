# Scene Progress Tracker

Use this file as the single source of truth for what is completed, in progress, blocked, and next.

## Status Legend

- Not started
- In progress
- QA pending
- Done
- Blocked

## Scene Status

- Scene 01: Done
- Scene 02: Done
- Scene 03: Done
- Scene 04: Done
- Scene 05: Done
- Scene 06: Done
- Scene 07: Done
- Scene 08: Done
- Scene 09: Done

## Section Log (append-only)

### Entry Template

- Date:
- Agent:
- Scene/Section:
- Source pages:
- Status:
- Completed:
- Outstanding:
- Decisions made:
- Next action:

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 01 / Section 01
- Source pages: 1-2
- Status: Done
- Completed: OCR batch saved; dialogue-only extraction staged; 36 triplets written to booklet/script/scene-01.md; section QA completed.
- Outstanding: Confirm official spelling for `Dar`; continue OCR from pages 3-4 and process first song lines.
- Decisions made: Mapped `愛叮堡學院` to `Love-Ding Fort Academy`; `叮叮魔法` to `Ding Ding Magic`; retained brief parenthetical tone markers where needed for dialogue continuity.
- Next action: Process Scene 01 Section 02 from pages 3-4.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 01 / Section 02
- Source pages: 3-4
- Status: Done
- Completed: OCR batch B02 saved; dialogue-only extraction staged; 51 triplets written to booklet/script/scene-01.md; section QA completed.
- Outstanding: Reconcile `S01-SEC02-L051` (line continues on page 5); confirm final English rendering of `比卡特羅家族` and `愛叮堡榮譽` after clearer OCR context.
- Decisions made: Added new recurring character names (比比/露露/菲菲/芳花/小志) to canonical name map; retained parenthetical tone markers only when embedded in spoken text.
- Next action: Process Scene 01 Section 03 from pages 5-6 with explicit carry-over merge from previous section boundary.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 01 / Section 03
- Source pages: 5 (Scene 1 ending only)
- Status: Done
- Completed: OCR batch B03 saved; dialogue-only extraction staged; 11 triplets written to `booklet/script/scene-01.md`; section QA completed.
- Outstanding: Confirm final rendering of `比卡特羅家族` / `愛叮堡榮譽` when cleaner OCR appears in later pages.
- Decisions made: Treated `S01-SEC02-L051` as interrupted carry-over; started new IDs at `S01-SEC03-L001`; kept uncertain speaker attributions flagged in working extraction only.
- Next action: Start Scene 02 Section 01 from page 6 and establish new section boundaries.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 01 / Full Scene QA
- Source pages: 1-5
- Status: Done
- Completed: Scene-level continuity/duplicate/format checks logged in `working-files/qa/scene-01-scene-check.md`.
- Outstanding: Re-validate provisional terms (`比卡特羅家族`, `愛叮堡榮譽`) when clearer OCR occurrences are available.
- Decisions made: Scene 01 marked complete; Scene 02 starts at page 6 (`第二幕`).
- Next action: Begin Scene 02 Section 01 extraction and conversion.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 02 / Section 01
- Source pages: 6
- Status: Done
- Completed: OCR batch B04 saved for page 6; dialogue-only extraction staged with 37 lines; 37 triplets written to `booklet/script/scene-02.md`; section QA completed.
- Outstanding: Validate heavy OCR normalizations against next pages for continuity; continue Scene 02 on pages 7-8.
- Decisions made: Treated opening chorus as lyric lines with preserved repetition; normalized degraded lexemes only when contextual confidence was sufficient and logged each normalization.
- Next action: Process Scene 02 Section 02 from pages 7-8 with fresh IDs (`S02-SEC02-Lxxx`).

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 02 / Section 02
- Source pages: 7-8
- Status: Done
- Completed: OCR batch B05 saved; dialogue-only extraction staged with 38 lines; 38 triplets written to `booklet/script/scene-02.md`; section QA completed.
- Outstanding: Re-validate four provisional OCR normalizations during Scene 02 scene-level QA (`魚水波蛋`, `貴族早餐指引`, `芬尼/麥芬尼`, and one imperative particle in `S02-SEC02-L021`).
- Decisions made: Normalized dropped speaker label before `唔制呀，我想食奶凍先。` to `遙遙` by dialogue flow; normalized `麥芬尼` to `芬尼` provisionally for consistency.
- Next action: Process Scene 02 Section 03 from pages 9-10 and then run Scene 02 scene-level consistency pass.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 02 / Section 03
- Source pages: 9-10
- Status: Done
- Completed: OCR batch B06 saved; dialogue-only extraction staged with 47 lines; 47 triplets written to `booklet/script/scene-02.md`; section QA completed.
- Outstanding: Several lyric lexemes remain normalized from degraded OCR and should be cross-checked if cleaner source material appears.
- Decisions made: Grouped page-10 anthem lines under `管家合唱`; retained conservative normalization with uncertainty handled in working extraction notes.
- Next action: Run Scene 02 scene-level consistency/continuity pass and close scene status.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 02 / Full Scene QA
- Source pages: 6-10
- Status: Done
- Completed: Scene-level continuity/duplicate/format checks logged in `working-files/qa/scene-02-scene-check.md`; Scene 02 marked complete.
- Outstanding: Provisional OCR normalizations from Section 02 remain tracked in working notes due lack of clearer recurrence.
- Decisions made: Closed Scene 02 as complete within available source quality; unresolved lexical uncertainty preserved as explicit risk note rather than silently forcing novel terms.
- Next action: Start Scene 03 Section 01 extraction/conversion on next source page range.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 03 / Section 01
- Source pages: 11-12
- Status: Done
- Completed: OCR batch B07 saved; dialogue-only extraction staged with 41 lines; 41 triplets written to `booklet/script/scene-03.md`; section QA completed.
- Outstanding: `S03-SEC01-L041` is truncated at page boundary and must be reconciled immediately in Scene 03 Section 02 from page 13.
- Decisions made: Kept conservative normalization on noisy OCR tokens; retained `麥芬尼/芬尼` as the same mapped character (`Fanny`) and preserved in working notes.
- Next action: Process Scene 03 Section 02 from next source pages, beginning with carry-over completion for `S03-SEC01-L041`.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 03 / Section 02
- Source pages: 13-14
- Status: Done
- Completed: OCR batch B08 saved; dialogue-only extraction staged with 22 lines (including carry-over completion for `S03-SEC01-L041`); 22 triplets written to `booklet/script/scene-03.md`; section QA completed.
- Outstanding: Page-13 lyric cluster includes two conservatively normalized low-confidence lexemes (`S03-SEC02-L010`, `S03-SEC02-L016`) pending optional re-OCR hardening.
- Decisions made: Preserved emergency-quarantine narrative flow and butler-panic song structure while explicitly tracking uncertainty in working extraction notes.
- Next action: Run Scene 03 scene-level consistency pass and close scene status.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 03 / Full Scene QA
- Source pages: 11-14 (with page-14 Scene 04 crossover noted)
- Status: Done
- Completed: Scene-level continuity/duplicate/format checks logged in `working-files/qa/scene-03-scene-check.md`; Scene 03 marked complete.
- Outstanding: Optional targeted re-OCR of page 13 lyrics to harden two low-confidence normalized tokens.
- Decisions made: Treated page-boundary carry-over as closed and retained explicit uncertainty tracking rather than silently overfitting degraded OCR.
- Next action: Start Scene 04 Section 01 extraction/conversion from page 14 with fresh section IDs.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 04 / Section 01
- Source pages: 14
- Status: Done
- Completed: Dialogue-only extraction staged with 24 lines; 24 triplets written to `booklet/script/scene-04.md`; section QA completed.
- Outstanding: Continue Scene 04 with next source page range and run scene-level QA after all sections are complete.
- Decisions made: Reassigned page-14 opening chorus lines to Scene 04 (from prior Scene 03 boundary staging) to preserve scene ownership.
- Next action: Process Scene 04 Section 02 from the next page batch.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 04 / Section 02
- Source pages: 15-16
- Status: Done
- Completed: OCR batch B09 saved; dialogue-only extraction staged with 46 lines; 46 triplets written to `booklet/script/scene-04.md`; section QA completed in `working-files/qa/scene-04-section-02-check.md`.
- Outstanding: Heavier OCR normalizations in five lines should be hardened via optional targeted re-OCR before final Scene 04 lock.
- Decisions made: Added `柔柔（老師）` to canonical character map; retained mixed-language spoken tokens (`Baby`, `Too bad`, `Water, I need water`) where present in source style.
- Next action: Process Scene 04 Section 03 from next source page range, then run full Scene 04 scene-level QA.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 04 / Section 03
- Source pages: 17
- Status: Done
- Completed: OCR batch B10 generated (pages 17-18); dialogue-only extraction staged with 25 lines for page 17; 25 triplets written to `booklet/script/scene-04.md`; section QA completed in `working-files/qa/scene-04-section-03-check.md`.
- Outstanding: Optional targeted re-OCR for page-17 lyric block before publication lock.
- Decisions made: Closed Scene 04 at `第四幕完` on page 17; treated page 18 as Scene 05 boundary start and excluded it from Scene 04 ownership.
- Next action: Run Scene 04 full-scene QA and close scene status.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 04 / Full Scene QA
- Source pages: 14-17
- Status: Done
- Completed: Scene-level continuity/boundary/format checks logged in `working-files/qa/scene-04-scene-check.md`; Scene 04 marked complete.
- Outstanding: Optional page-17 lyric re-OCR hardening task remains tracked as non-blocking follow-up.
- Decisions made: Scene boundary ownership locked (`第四幕完` closes Scene 04, `第五幕` begins Scene 05).
- Next action: Begin Scene 05 Section 01 extraction/conversion from page 18 onward.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 05 / Section 01
- Source pages: 18
- Status: Done
- Completed: Dialogue-only extraction staged with 15 lines; 15 triplets written to `booklet/script/scene-05.md`; section QA completed in `working-files/qa/scene-05-section-01-check.md`.
- Outstanding: Three low-confidence OCR lexemes (`S05-SEC01-L005`, `L007`, `L015`) require cross-check during next batch.
- Decisions made: Preserved mixed-language spoken tokens and kept conservative normalization where OCR was degraded.
- Next action: OCR and process Scene 05 Section 02 from pages 19-20, then continue section loop.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 05 / Section 02
- Source pages: 19-20
- Status: Done
- Completed: OCR batch B11 saved; dialogue-only extraction staged with 57 lines; 57 triplets written to `booklet/script/scene-05.md`; section QA completed in `working-files/qa/scene-05-section-02-check.md`.
- Outstanding: Page-20 lyric tokens in `S05-SEC02-L049`, `L056`, and one rivalry lexeme in `L032` remain conservatively normalized pending recurrence check.
- Decisions made: Preserved mixed-language token `Oh Baby`; normalized breakfast-item terms conservatively to maintain continuity with prior scenes (`柴爾德家族` / `比卡特羅家族`).
- Next action: OCR and process Scene 05 Section 03 from pages 21-22, then run Scene 05 scene-level QA once section loop is complete.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 05 / Section 03
- Source pages: 21 (page 22 excluded as Scene 06 boundary)
- Status: Done
- Completed: OCR batch B12 saved (pages 21-22); dialogue-only extraction staged with 46 lines for page 21; 46 triplets written to `booklet/script/scene-05.md`; section QA completed in `working-files/qa/scene-05-section-03-check.md`.
- Outstanding: Several page-21 lyric lexemes remain conservatively normalized in low-confidence OCR zones (`S05-SEC03-L004`, `L013`, `L038`).
- Decisions made: Locked scene boundary at `第五幕完` on page 21 and excluded all `第六幕` setup lines on page 22 from Scene 05 ownership.
- Next action: Run Scene 05 scene-level QA and close scene status.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 05 / Full Scene QA
- Source pages: 18-21
- Status: Done
- Completed: Scene-level continuity/boundary/format checks logged in `working-files/qa/scene-05-scene-check.md`; Scene 05 marked complete.
- Outstanding: Optional targeted page-21 lyric re-OCR remains tracked as non-blocking hardening.
- Decisions made: Closed Scene 05 at page-21 `第五幕完`; Scene 06 starts at page 22 with fresh section IDs.
- Next action: Begin Scene 06 Section 01 extraction/conversion from pages 22-23.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 06 / Section 01
- Source pages: 22-23
- Status: Done
- Completed: OCR batch B13 saved for page 23; dialogue-only extraction staged with 38 lines; 38 triplets written to `booklet/script/scene-06.md`; section QA completed in `working-files/qa/scene-06-section-01-check.md`.
- Outstanding: Competition title lexeme remains OCR-noisy and provisional (`愛叮堡榮譽`) pending clearer recurrence in later pages.
- Decisions made: Included pre-curtain butler spoken lines and excluded movement/light stage-direction lines from script triplets.
- Next action: Process Scene 06 Section 02 from pages 24-25.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 06 / Section 02
- Source pages: 24-25
- Status: Done
- Completed: OCR batch B14 saved; dialogue-only extraction staged with 66 lines; 66 triplets written to `booklet/script/scene-06.md`; section QA completed in `working-files/qa/scene-06-section-02-check.md`.
- Outstanding: Three page-25 lyric lines remain low-confidence (`S06-SEC02-L058`, `L061`, `L062`) and competition-title lexeme is still provisional pending clearer recurrence.
- Decisions made: Preserved quiz and magic-round sequence exactly; applied conservative lyric normalization rather than overfitting noisy OCR.
- Next action: Process Scene 06 Section 03 from next source pages and carry forward targeted re-OCR hardening items before Scene 06 lock.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 06 / Full Scene QA
- Source pages: 22-26
- Status: Done
- Completed: Scene-level continuity/boundary/format checks logged in `working-files/qa/scene-06-scene-check.md`; verified page 26 (`working-files/ocr/batch-15-pages-26-27.md`) is stage-direction-only with `（第六幕完）`; Scene 06 marked complete.
- Outstanding: Targeted re-OCR hardening remains for low-confidence page-25 lyric lines (`S06-SEC02-L058`, `L061`, `L062`); competition-title lexeme remains provisional pending cleaner recurrence.
- Decisions made: Closed Scene 06 with no Section 03 dialogue payload; re-prioritized workflow to Scene 07 start.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 07 / Section 02
- Source pages: 29-30
- Status: Done
- Completed: OCR batch B17 saved; dialogue-only extraction staged with 37 lines; 37 triplets written to `booklet/script/scene-07.md`; section QA completed in `working-files/qa/scene-07-section-02-check.md`.
- Outstanding: Low-confidence lyric tokens remain in `S07-SEC02-L021`, `L025`, and `L029` for optional targeted hardening.
- Decisions made: Preserved mixed-language code-switching and kept conservative lyric normalization where OCR was fragmented.
- Next action: Run Scene 07 full-scene QA and close scene status.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 07 / Full Scene QA
- Source pages: 27-30
- Status: Done
- Completed: Scene-level continuity/boundary/format checks logged in `working-files/qa/scene-07-scene-check.md`; Scene 07 marked complete.
- Outstanding: Optional targeted lyric hardening re-OCR remains for pages 27-30 (`S07-SEC01-L010`; `S07-SEC02-L021`, `L025`, `L029`).
- Decisions made: Closed Scene 07 at page-30 `第七幕完`; next production priority moved to Scene 08 page 31.
- Next action: Begin Scene 08 Section 01 extraction/conversion from pages 31-32.
- Next action: Begin Scene 07 Section 01 extraction/conversion from page 27 onward.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 07 / Section 01
- Source pages: 27-28
- Status: Done
- Completed: OCR batch B16 generated for page 28; dialogue-only extraction staged with 34 lines; 34 triplets written to `booklet/script/scene-07.md`; section QA completed in `working-files/qa/scene-07-section-01-check.md`.
- Outstanding: Song-heavy lyric tokens remain low-confidence on pages 27-28 and should be targeted for hardening re-OCR in a follow-up pass.
- Decisions made: Preserved mixed-language spoken tokens (`I hate it`, `Baby`, `relax`) and applied conservative lyric normalization to maintain sequence and scene intent.
- Next action: OCR pages 29-30 and process Scene 07 Section 02.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 08 / Section 01
- Source pages: 31-32
- Status: Done
- Completed: OCR batch B18 saved; dialogue-only extraction staged with 34 lines; 34 triplets written to `booklet/script/scene-08.md`; section QA completed in `working-files/qa/scene-08-section-01-check.md`.
- Outstanding: Low-confidence fragments remain in `S08-SEC01-L009` and `S08-SEC01-L031` for targeted hardening re-OCR.
- Decisions made: Preserved opening-song motivational cadence (`重新起步`) and butler-observation comedic tone while applying conservative normalization where OCR tokens were fragmented.
- Next action: OCR pages 33-34 and process Scene 08 Section 02.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 08 / Section 02
- Source pages: 33-34
- Status: Done
- Completed: OCR batch B19 saved; dialogue-only extraction staged with 48 lines; 48 triplets written to `booklet/script/scene-08.md`; section QA completed in `working-files/qa/scene-08-section-02-check.md`.
- Outstanding: Song-heavy lines `S08-SEC02-L030` to `S08-SEC02-L046` remain conservatively normalized and are tracked for optional targeted lyric hardening re-OCR.
- Decisions made: Preserved student-to-butler care-reversal arc and `早餐小心意` warmth while maintaining conservative line-by-line normalization in low-confidence lyric clusters.
- Next action: Run Scene 08 full-scene QA and close scene status.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 08 / Full Scene QA
- Source pages: 31-34
- Status: Done
- Completed: Scene-level continuity/boundary/format checks logged in `working-files/qa/scene-08-scene-check.md`; Scene 08 marked complete.
- Outstanding: Targeted lyric hardening remains for Section 01 (`S08-SEC01-L009`, `L031`) and Section 02 (`S08-SEC02-L030` to `L046`).
- Decisions made: Scene boundary locked at page 34 `第八幕完`; next production priority moved to Scene 09 page 35.
- Next action: Begin Scene 09 Section 01 extraction/conversion from pages 35-36.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 09 / Section 01
- Source pages: 35-36
- Status: Done
- Completed: OCR batch B20 saved; dialogue-only extraction staged with 35 lines; 35 triplets written to `booklet/script/scene-09.md`; section QA completed in `working-files/qa/scene-09-section-01-check.md`.
- Outstanding: Competition object/title lexeme (`愛叮堡榮譽` variants) remains provisional and needs clearer recurrence in pages 37-38 before scene lock.
- Decisions made: Preserved non-magic problem-solving structure (`三步找法`) and conservative normalization in noisy lexeme zones while excluding stage-direction-only movement/lighting lines.
- Next action: OCR pages 37-38 and process Scene 09 Section 02.

### 2026-02-14 — Section Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 09 / Section 02
- Source pages: 37-38
- Status: Done
- Completed: OCR batch B21 saved; dialogue+song extraction staged with 61 lines; 61 triplets written to `booklet/script/scene-09.md`; section QA completed in `working-files/qa/scene-09-section-02-check.md`.
- Outstanding: Finale-song lyric cluster remains conservatively normalized from low-confidence OCR and is tracked as optional publication hardening.
- Decisions made: Locked competition object/title wording as `愛叮堡榮譽` (`Love-Ding Honor`) for Scene 09 consistency; retained sequence-first normalization for finale song refrains.
- Next action: Run Scene 09 full-scene QA and close scene status.

### 2026-02-14 — Scene-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 09 / Full Scene QA
- Source pages: 35-38
- Status: Done
- Completed: Scene-level continuity/boundary/format checks logged in `working-files/qa/scene-09-scene-check.md`; Scene 09 marked complete.
- Outstanding: Optional targeted lyric hardening for pages 37-38 remains non-blocking follow-up.
- Decisions made: Locked final scene ownership through page 38 `(全劇完)` with no cross-scene spillover.
- Next action: Run booklet-level consistency pass for `booklet/characters.md`, `booklet/scene-synopsis.md`, and `booklet/overview.md` against finalized scripts.

### 2026-02-14 — Booklet-Level Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Booklet-level consistency pass (post Scene 09)
- Source pages: Script corpus pages 1-38 (via finalized scene files)
- Status: Done
- Completed: Filled `booklet/characters.md`, `booklet/scene-synopsis.md`, and `booklet/overview.md`; aligned terminology and narrative arc references with finalized scene scripts and canonical working maps.
- Outstanding: Optional publication hardening tasks remain (targeted re-OCR items already tracked in `todo.md`).
- Decisions made: Kept `愛叮堡榮譽` as `Love-Ding Honor`; preserved existing canonical name map and did not force new renaming changes during booklet pass.
- Next action: Optional terminology hardening pass for remaining provisional lexemes if publication-level lock is required.

### 2026-02-14 — Hardening Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 08 / Section 02 targeted lyric hardening
- Source pages: 33-34
- Status: Done
- Completed: Re-checked `working-files/ocr/batch-19-pages-33-34.md` against staged extraction and script lines `S08-SEC02-L030` to `L046`; locked one wording correction in `S08-SEC02-L041` from `即使跌倒不怕，共對已足。` to `即使都不怕，共對已足。`; updated section QA and todo tracking.
- Outstanding: Scene 08 Section 01 hardening remains for `S08-SEC01-L009` and `S08-SEC01-L031`.
- Decisions made: Removed an over-normalized token (`跌倒`) where OCR recurrence did not support it.
- Next action: Continue highest-impact pending hardening task from `working-files/todo.md` (Scene 08 Section 01 lines or Scene 09 finale lyric cluster).

### 2026-02-14 — Hardening Update

- Date: 2026-02-14
- Agent: Copilot (GPT-5.3-Codex)
- Scene/Section: Scene 06 / Section 02 targeted lyric hardening
- Source pages: 25
- Status: Done
- Completed: Re-checked `working-files/ocr/batch-14-pages-24-25.md` against staged extraction and script lines `S06-SEC02-L058`, `S06-SEC02-L061`, `S06-SEC02-L062`; locked wording to `離開幫手必會失鎮定。`, `強大世界裡魔法。`, and `在哪可否來和應。`; synchronized section QA and todo tracking.
- Outstanding: Remaining hardening backlog stays in `working-files/todo.md` (Scenes 04, 05, 07, and 08).
- Decisions made: Replaced over-fragmented OCR-normalized wording with conservative but coherent lyric reads while preserving line order and song intent.
- Next action: Execute targeted lyric hardening for Scene 07 pages 27-30 lines tracked in `working-files/todo.md`.
