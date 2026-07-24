# 第一阶段构建报告

本包包含可运行 Python 核心、12 个项目内 Skills、一个全局轻量启动 Skill、Obsidian Vault、比赛项目模板、52 个核心/国赛高频算法种子卡及对应示例、PowerShell 初始化/诊断/GitHub/Word 工具，以及图件契约、源码 QA、冻结工件、依赖失效、OCR 入口和 GB/T 7714 基础格式化工具。

## 已自动验证

- Python 包安装与单元测试。
- 52 个算法示例逐个执行并生成 `output/result.json`。
- 本地知识索引构建与检索烟雾测试。
- 赛题项目创建与状态文件生成。

## 需要在用户 Windows 电脑上验证

- `winget` 安装权限、Codex 全局 launcher 目录和 Windows 路径。
- Word COM 更新域、Pandoc 原生 OMML 公式转换与 PDF 导出。
- Obsidian 社区插件下载与启用。
- GitHub CLI 登录、私有仓库创建和 Git LFS 推送。
- OCR 工具链和 GPU 深度学习可选依赖。

这些 Windows 专属能力由 `doctor.ps1` 和端到端验收题进行最终确认，不能在当前 Linux 构建环境中声称已经通过。
