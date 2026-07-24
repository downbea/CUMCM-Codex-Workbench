---
name: cummcm-upstream-review
description: Use only when the user explicitly asks to check nature-skills or MathModeling-skills upstream updates and produce a non-destructive migration proposal.
---

# 上游参考仓库差异检查


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Run only on explicit user request. Compare pinned and current upstream commits, summarize file-level changes, categorize useful ideas, license/dependency impact, incompatibilities and recommended migrations. Never overwrite local skills automatically. Migration requires human approval and regression tests.
