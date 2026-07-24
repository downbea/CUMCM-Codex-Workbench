---
name: cummcm-final-audit
description: Use for independent model/logic, data/code/numeric consistency, and format/reference/submission compliance audits.
---

# 三重独立审计与风险分级


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Three independent audits

Run separate contexts for: model and logic; data/code/numeric consistency; format/reference/submission compliance. Each report must cite exact files/locations, evidence and severity.

`BLOCKER` must be fixed. `MAJOR` may be released only through explicit risk acceptance with rationale and scope. `MINOR` may be accepted. Do not mark final release until all blockers are cleared and all gates are recorded.
