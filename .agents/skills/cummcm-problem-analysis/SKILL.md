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

Create a task-requirement matrix before generating model candidates. For every subquestion, record:

- mandatory action verbs such as analyze, predict, optimize, evaluate and recommend;
- explicitly required factors, objectives, constraints, horizons, scenarios and output forms;
- upstream inputs and downstream consumers;
- the evidence needed to declare each requirement answered.

Classify these as task-coverage requirements, not optional model features. If data cannot support one literally, define the closest defensible interpretation and flag the residual gap for human approval; do not silently drop it.

Use `shared/` for common definitions and per-question directories for question-specific work. Parallelize only tasks whose dependencies are frozen or independent.
