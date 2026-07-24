---
name: cummcm-figure
description: Use for CUMCM publication-quality data figures, workflows, diagrams, source-data mapping, vector export, and visual audits.
---

# 国赛论文图件设计、生成与 QA


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Figure contract

Before plotting, write the one-sentence conclusion, evidence hierarchy, panel map, figure role, source-data mapping and export contract. A figure is a visual argument, not decoration.

Use Python only. Prefer a hero panel with subordinate evidence, restrained palettes, white backgrounds, direct labels where useful, Chinese-font fallbacks, black-and-white print readability and editable vector exports. Quantitative figures must map to clean source data and record exclusions.

Export SVG, PDF and high-resolution PNG, plus plotting script, source data and QA notes. Check final printed size, label overlap, units, legends, statistics, seeds/folds, baseline definitions and traceability. The design is adapted from a pinned Nature Skills reference but must follow CUMCM/Word constraints rather than journal-specific rules.
