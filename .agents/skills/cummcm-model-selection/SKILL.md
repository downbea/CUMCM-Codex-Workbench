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

## Task-coverage gate

Apply the task-requirement matrix before ranking candidates. A candidate cannot become the sole main model when it omits an explicitly required factor, objective, constraint, horizon or output, even if its proxy error is lower. Keep such a model as the Baseline and retain at least one task-complete candidate for the human gate.

Interpret “beginner”, “simple” or “easy to explain” as a complexity constraint, not permission to simplify away the question. Prefer simple task-complete forms: standardized multiple regression instead of a single-factor proxy when multiple factors are required; integer linear programming or finite enumeration instead of an allocation rule when optimization is required; deterministic rolling adjustment instead of risk scoring alone when actionable recommendations are required.

For a required multi-factor forecast, ensure the named factors actually enter the prediction equation or an explicitly defined composite index. Report small-sample instability and compare with a simpler Baseline, but do not relabel a current cross-sectional redistribution as a future forecast without an executable future-input scenario.

For every optimization subquestion, the candidate report must show decision variables, objective function or lexicographic objectives, constraints, parameter meanings, solution method and optimality or feasibility checks. Post-hoc reporting of cost or grid pressure does not make them optimization objectives.

For every risk-and-recommendation subquestion, require a closed loop from risk state to decision variables, adjustment rule and recalculated outcome. Prefer quantified “where, when, how much, cost and improvement” outputs over generic policy advice.
