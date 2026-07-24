---
name: cummcm-workbench
description: Use when starting, resuming, coordinating, or auditing the CUMCM Codex Workbench. Routes knowledge-learning and contest-modeling tasks, enforces human gates, restores state from files, and delegates to specialist skills.
---

# CUMCM Workbench Orchestrator

## First action

Resolve the active mode and project from the user's request. Then read `AGENTS.md`, `config/defaults.yaml`, the active `project_state.json`, `decision_log.md`, and `interaction_log.md`. If no active project exists, offer exactly the valid creation or learning entrypoint required by the request.

## Primary modes

### Knowledge learning mode

Route paper discovery/import, PDF/Markdown parsing, exact source anchoring, method extraction, web supplementation, code execution, reproduction grading, batch review, and approved-vault publishing through `cummcm-paper-learning`.

### Contest modeling mode

Route in this dependency-aware order:

1. official-rule snapshot and contest package manifest;
2. all-problem rapid analysis and dynamically budgeted baseline PoCs;
3. human topic selection;
4. shared problem definition, symbol table, assumptions and subquestion dependency graph;
5. reversible data-audit and cleaning proposal, then human approval and frozen validated data;
6. knowledge retrieval, baseline and advanced candidates, comparable PoCs, then human model approval;
7. reproducible Python implementation and review;
8. human result confirmation and frozen numbers/figures;
9. incremental Markdown paper section drafting;
10. final cross-question restructuring, references, Word/PDF/support package;
11. three independent audits and severity-based release gate.

## Parallelism

Use independent worktrees for independent tasks. Parallelize paper analyses, candidate-model PoCs, web research, code review, and independent audits. Do not parallelize dependent subquestions as if they were unrelated. Share only frozen interfaces through files.

## Human gates

Stop and request explicit confirmation for topic selection, data cleaning freeze, main-model selection or change, long/high-resource runs, result freezing, MAJOR risk acceptance, and final release. BLOCKER findings cannot be released.

## Session recovery

At startup, produce a recovery summary containing current stage, valid frozen artifacts, stale artifacts, interrupted tasks, pending human decisions, time remaining, and the single recommended next action. Do not automatically cross a human gate during recovery.

## Logs

Append a structured entry to `interaction_log.md` for every meaningful run. Append human decisions to `decision_log.md` and machine state. Keep full raw chat out of the log; retain only concise key quotes for confirmations and risk acceptance.
