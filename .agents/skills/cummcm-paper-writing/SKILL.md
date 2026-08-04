---
name: cummcm-paper-writing
description: Use to draft frozen subquestion sections incrementally, then reconstruct the complete CUMCM paper with grounded numbers and references.
---

# Markdown 增量论文写作与统一重构


## Mandatory operating rules

Read project state, decision log, interaction log, and the directly required artifacts before acting. Write outputs to disk and return a compact change report. Never use chat memory as the only source of project state.

Respect human gates, source traceability, relative-path configuration, Git worktree isolation, and stale-artifact propagation. Do not perform destructive operations without explicit confirmation.


## Workflow

Markdown is the only authoritative manuscript source. After each subquestion's results are confirmed and frozen, draft that section immediately. Insert only frozen numbers, figure IDs and result references. Mark dependent paragraphs stale when upstream artifacts change.

After all questions are complete, rewrite the abstract, problem analysis, model transitions, innovation, evaluation, limitations and conclusion as one coherent argument. Learn structure from papers without copying source sentences. Use numeric GB/T 7714 citations whose fields have been verified.

## Judge-facing mathematical completeness

- For a required multi-factor model, show how every named factor enters the equation or composite index and define the future horizon or scenario. A single-factor Baseline may remain for comparison but must not replace the required model.
- For an optimization problem, make the decision variables, objective function, constraints and solution method visually explicit before presenting results. Distinguish an optimization model from a deterministic allocation rule or post-hoc screening.
- For a risk-and-adjustment problem, continue beyond risk classification. State the affected region and time, quantify the adjustment, and recompute at least one post-adjustment indicator whenever the available data permit it.

## Submission-facing language

Write for judges, not for the internal delivery pipeline. Keep hashes, freeze IDs, run IDs, Git state, manifests, allowlists, byte-for-byte checks, test counts, local paths and audit workflow language in project administration files only. Do not place them in the manuscript, appendix captions or support-material instructions unless an official rule explicitly requires a specific disclosure.

Describe reproducibility in ordinary modeling language, for example by stating the data source, preprocessing method, parameter meaning and algorithm steps. Do not use phrases such as “同名文件逐字节一致”“匿名白名单构建” or “来源运行编号” in submission-facing prose.

Write like a contestant explaining a specific modeling argument, not like an auditor certifying a pipeline. Lead paragraphs with the observed phenomenon, modeling choice or numerical finding. Consolidate recurring caveats in the assumptions, limitations or evaluation section instead of repeating “本文”“当前”“不能”“不等于”“必须强调” after every result. Avoid mechanically symmetric paragraph templates and generic recommendations that could fit any city or dataset. Use concrete regions, periods, quantities and before/after effects where available. Perform a final human-style read for cadence, repetition and unnecessary defensive language; do not rely on an AI-text detector as the acceptance criterion.

## Code appendix

- Provide exactly one concise Python listing for each subquestion, normally `q1.py` through `qN.py`, and use one code block per subquestion in Markdown.
- Include only the key modeling and solution logic needed to understand that subquestion. Keep imports and small helper functions in the same listing when necessary.
- Exclude unit tests, validation scripts, CLI entry points, YAML configuration, build or packaging code, logs, manifests and version-control metadata from the paper appendix.
- Submit processed data as separate data files. In the appendix, give only a short natural-language data-file list or field description; do not paste large datasets into the manuscript.
- Keep the full engineering implementation and internal reproducibility checks outside the submission-facing appendix. If official rules require additional materials, add only the required items and obtain human approval before expanding the package.
