---
name: cummcm-word-delivery
description: Use to convert the approved Markdown source into editable DOCX with native equations, update fields through Word, export PDF, and package support files.
---

# Word 原生公式、PDF 与提交包


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Convert the approved Markdown with Pandoc and the provided reference DOCX so LaTeX math becomes native editable Word equations. Use Word COM to update fields, TOC, page numbers and PDF export. Use Word-native tables where practical and preserve editable vector figures/source files.

Back up any manually adjusted Word file before regeneration. Cross-check Markdown, DOCX, PDF, code outputs, frozen numbers, figure captions and support-material filenames before packaging.

## Submission appendix and support package

- Preserve the approved Markdown rule of one subquestion per code block and one matching Python file, normally `q1.py` through `qN.py`.
- Put only key modeling code and processed data in the judge-facing support package. Exclude tests, verification utilities, CLI wrappers, YAML files, logs, manifests, Git metadata, raw Office properties, failed experiments and internal interaction records.
- Keep internal hashes, byte comparisons, allowlist reports and audit evidence under project administration or work directories. Use them for verification, but never render that engineering language into the paper or judge-facing package.
- Build the package from an explicit allowlist containing only the approved per-question code files and processed data files. Fail the package audit when unexpected files appear.
- Do not silently expand the package for convenience. If current official rules require another file, record the rule source and obtain human approval for the exception.
