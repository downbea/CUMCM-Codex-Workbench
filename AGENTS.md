# CUMCM-Codex-Workbench Agent Rules

## Governing workflow

When a task concerns mathematical modeling, paper learning, a CUMCM contest, data analysis, modeling code, figures, paper drafting, Word/PDF generation, or submission audit, first read `.agents/skills/cummcm-workbench/SKILL.md`.

Treat Markdown/YAML/JSON files on disk as the authoritative project memory. Do not rely on the chat history when a project state, decision log, audit report, frozen result, or knowledge card exists on disk.

## Hard gates

Never bypass these gates:

- destructive file or Git operations require explicit human confirmation;
- data cleaning must be proposed, compared, and approved before freezing;
- final model selection requires human confirmation and remains reopenable;
- jobs expected to exceed 20 minutes or heavily occupy GPU/RAM require approval;
- final numeric results must be confirmed before freezing and paper insertion;
- BLOCKER audit findings cannot be force-released;
- all official-rule checks must prefer current official sources.

## File discipline

Use relative paths in code and YAML. Do not hard-code `D:\obsidian笔记` inside Python modules. Resolve paths from `config/local.yaml`, environment variables, or command arguments.

Do not edit files under `data/raw/` or `data/validated/` directly. All data corrections must be encoded in scripts or cleaning rules.

Do not let specialist agents modify the main branch directly. Use isolated worktrees or task branches and merge only after tests and a change report.

## Source and evidence discipline

For paper-derived knowledge, attach exact page, section, equation, figure, table, or Markdown heading anchors. Distinguish source-derived statements, web supplementation, and agent inference.

For web research, prioritize government, official statistical sources, professional associations, universities, primary papers, and official software documentation. Blogs and forum posts may only serve as discovery leads.

## Output discipline

Every meaningful action must update `interaction_log.md`; every human decision must update `decision_log.md` and the machine-readable state file. Generated results must include configuration hash, data hash, code commit, random seed, and runtime metadata.
