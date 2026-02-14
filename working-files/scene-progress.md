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
- Scene 04: In progress
- Scene 05: Not started
- Scene 06: Not started
- Scene 07: Not started
- Scene 08: Not started
- Scene 09: Not started

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
