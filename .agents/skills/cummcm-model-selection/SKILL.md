---
name: cummcm-model-selection
description: Use to retrieve knowledge, generate baseline and advanced candidate models, run comparable PoCs, and wait for human model approval.
---

# 基线优先的模型候选与 PoC


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Retrieve candidate knowledge through metadata, keyword, vector-like TF-IDF and Obsidian link expansion. Always establish a simple Baseline first. Compare advanced models on identical data, splits and metrics. Require repeated validation for stochastic or complex models and report average, variability, runtime and explanation cost.

A complex model becomes a main-model candidate only when its gain is stable and practically meaningful. Present candidates and rejected alternatives with evidence, then stop for human approval. The user may reopen and modify this choice at any time; propagate staleness to downstream artifacts.
