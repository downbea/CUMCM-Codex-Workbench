---
name: cummcm-python-modeling
description: Use to implement approved models as reproducible Python scripts with YAML config, tests, checkpoints, outputs, and runtime metadata.
---

# Python 建模、测试、检查点与复现


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Implement only approved models. Put paths, seeds, parameters, metrics and outputs in YAML. Use `.py` scripts as authoritative execution units; notebooks are exploratory only. Save environment, config hash, data hash, Git commit, runtime, logs, metrics, figures and checkpoints.

Jobs estimated above 20 minutes or likely to saturate resources require a run proposal and approval. Long jobs must support checkpoints, pause/resume and safe interruption. Run tests and code review before result review.
