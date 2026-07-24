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
