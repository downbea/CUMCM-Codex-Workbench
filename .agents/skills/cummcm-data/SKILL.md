---
name: cummcm-data
description: Use for contest package extraction, manifesting, OCR/table extraction, data quality audits, reversible cleaning proposals, and data freezing.
---

# 数据导入、OCR、审计、可逆清洗


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Keep `data/raw/` immutable. Extract archives safely, create manifests and hashes, inspect PDF/image/table content, and route uncertain OCR/table cells to a human correction queue.

Create a cleaning proposal before any destructive transformation. For each rule report rationale, affected rows/columns, before/after statistics, alternatives and risks. Freeze only after human approval. Record each transformation as executable code and versioned metadata so every intermediate state can be regenerated.
