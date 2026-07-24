---
name: cummcm-problem-analysis
description: Use to restate a contest problem, decompose subquestions, establish shared symbols, assumptions, and dependency-aware work plans.
---

# 赛题解析、依赖图、假设与符号


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Restate the problem without copying it. Separate shared definitions from subquestion-specific goals. Create a dependency DAG, shared data contract, symbol table, assumptions with justification and risk, and explicit inputs/outputs for Q1, Q2, Q3, etc.

Use `shared/` for common definitions and per-question directories for question-specific work. Parallelize only tasks whose dependencies are frozen or independent.
