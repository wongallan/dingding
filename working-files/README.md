# Working Files Guide

This folder supports multi-agent, iterative script translation with consistency and auditability.

## Read Order for Any New Agent

1. `../PLAN.md`
2. `scene-progress.md`
3. `character-name-map.md`
4. `place-term-glossary.md`
5. `song-style-decisions.md`
6. `ocr-batch-log.md`

## Subfolders to Create During Execution

- `ocr/` for raw OCR batch outputs
- `extracted/` for cleaned dialogue-only staged files
- `qa/` for section and scene QA reports

## Rule

If you make a translation decision that could affect later scenes, write it here first (map/glossary/decisions), then continue scene edits.
