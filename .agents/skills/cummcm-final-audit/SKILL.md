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

## Task-completeness and judge-recognition audit

Audit the manuscript against the task-requirement matrix before treating numerical consistency as success. Passing tests proves implementation consistency, not that the selected model answered the question.

- Mark omission of a named factor, required forecast horizon, optimization structure or requested decision output as at least `MAJOR`; use `BLOCKER` when the subquestion's central task is effectively unanswered.
- For multi-factor forecasting, verify that required factors enter the formal model and that “future” has executable inputs or a declared scenario. A single-factor redistribution of current totals cannot be presented as a complete future multi-factor forecast.
- For optimization, verify visible decision variables, objectives, constraints, solution method and feasibility/optimality evidence. Cost and grid indicators computed only after allocation do not satisfy a multi-objective optimization request.
- For risk questions requiring recommendations, verify a quantified adjustment or a defensible calculation of the minimum remedial action and at least one recalculated post-adjustment outcome. Generic monitoring, storage, expansion or policy prose alone is insufficient.
- When a central task-coverage `MAJOR` is considered for risk acceptance, state the likely contest-scoring impact and recommend reopening the model; do not let workflow approval language make the finding appear harmless.

Run a judge-facing prose pass. Flag repeated audit-like caveats, mechanically uniform paragraphs, excessive internal process language and recommendations that are not tied to the problem's places, periods or numbers. Require natural modeling prose, but do not use an automated AI-text score as proof of authorship or quality.

## Submission-language and appendix checks

Treat the following as submission defects even when the underlying engineering evidence is valid:

- internal hashes, freeze or run identifiers, Git state, allowlist or byte-comparison language appearing in the manuscript or judge-facing attachments;
- more than one code block or more than one Python file for a single subquestion without explicit human approval;
- tests, verification CLI scripts, YAML configuration, build scripts, logs, manifests or internal audit records included in the paper appendix or judge-facing support package;
- raw rather than processed data included where the approved package scope is processed data only.

Verify that each subquestion has one concise matching code file, that the code contains the key model logic, and that the support package contains only approved per-question code and processed data. Keep detailed provenance and reproducibility evidence in internal audit reports rather than submission-facing prose.
