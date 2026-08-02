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

## Submission-language and appendix checks

Treat the following as submission defects even when the underlying engineering evidence is valid:

- internal hashes, freeze or run identifiers, Git state, allowlist or byte-comparison language appearing in the manuscript or judge-facing attachments;
- more than one code block or more than one Python file for a single subquestion without explicit human approval;
- tests, verification CLI scripts, YAML configuration, build scripts, logs, manifests or internal audit records included in the paper appendix or judge-facing support package;
- raw rather than processed data included where the approved package scope is processed data only.

Verify that each subquestion has one concise matching code file, that the code contains the key model logic, and that the support package contains only approved per-question code and processed data. Keep detailed provenance and reproducibility evidence in internal audit reports rather than submission-facing prose.
