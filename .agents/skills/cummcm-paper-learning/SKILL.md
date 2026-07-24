---
name: cummcm-paper-learning
description: Use for importing, parsing, grounding, reproducing, reviewing, and approving mathematical-modeling papers into the Obsidian knowledge vault.
---

# 论文批量学习与审核入库


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Register all PDFs and Markdown files by hash and metadata. Deduplicate before analysis. For each paper, create exact source anchors, a paper note, one or more model cards, code/reproduction tasks, writing-pattern notes, and a provenance report. Supplement only with authoritative web sources and label supplementation separately.

Run all included or generated Python examples. Preserve commands, environment, seed, data, logs, metrics and figures. Grade reproduction as `result-level`, `method-level`, `example-only`, or `failed`; never overstate reproduction.

For batches, finish all analyses into the review queue, then generate one batch review dashboard. Publish only entries explicitly approved by the user; rejected or deferred entries remain outside the formal index.
