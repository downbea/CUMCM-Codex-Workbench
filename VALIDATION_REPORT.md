# 第一阶段交付包验证报告

验证日期：2026-07-24

## 验证结论

本交付包已经完成 Linux 构建环境内能够执行的静态检查、Python 单元测试、52 个算法示例批量运行、知识库索引构建与检索、比赛项目创建、冻结工件、依赖失效和图件源码检查等验证。基础 Python 闭环可运行。

第一阶段知识卡目前统一标记为 `seeded`，表示已生成并通过构建环境中的代码验证，但尚未替代用户的首次批量人工审核。只有审核通过后，才应改为 `approved` 并作为正式比赛检索证据使用。

## 已通过的自动验证

| 检查项 | 结果 |
|---|---|
| Python 源码编译检查 | 通过 |
| Workbench 单元测试 | 6/6 通过 |
| 算法模型卡 | 52 个 |
| 可运行 Python 示例 | 52/52 通过 |
| 示例运行失败数 | 0 |
| 本地知识索引 | 81 个文档成功建立 |
| 中文检索烟雾测试 | TOPSIS 查询返回 TOPSIS 为首项 |
| 比赛项目创建与状态文件 | 通过 |
| 冻结文件与哈希校验 | 通过 |
| 依赖失效传播测试 | 通过 |
| 图件 Python 源码 QA 烟雾测试 | 通过 |
| 国赛参考 Word 模板渲染 | 10 页均成功渲染并完成页面检查 |

## 已生成的关键组件

项目包含 12 个项目内 Skills、1 个轻量全局启动 Skill、Python CLI 与工具包、PowerShell 初始化及诊断脚本、Obsidian Vault、52 个算法模型卡、52 套 Python 示例、国赛项目模板、Word 参考模板、图件契约与 QA、三重审计模板、人工审核记录、决策日志和跨会话状态文件。

## 必须在用户 Windows 电脑上继续验证的内容

以下能力依赖 Windows、Microsoft Word、Codex App、Obsidian 或用户的 GitHub 登录环境，本次 Linux 构建环境无法据实宣称已经通过：

- `winget` 软件安装权限和 PowerShell 当前用户执行策略。
- Windows 版 Codex App 对项目内 Skills 与轻量全局 launcher 的发现和触发。
- Word COM 更新域、目录、交叉引用、原生 OMML 公式与 PDF 导出。
- Obsidian 社区插件的自动安装、启用和 Dataview/Templater/Kanban 页面效果。
- GitHub CLI 浏览器授权、三个私有仓库创建、Git LFS 推送与恢复。
- OCR 可选工具链、扫描表格识别和 RTX 4060 可选 GPU 路径。
- 用户指定往届国赛真题的完整端到端验收。

## Windows 首次验证命令

将三个目录放入 `D:\obsidian笔记` 后，在 PowerShell 中运行：

```powershell
cd 'D:\obsidian笔记\CUMCM-Codex-Workbench'
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\setup.ps1
.\doctor.ps1
```

`doctor.ps1` 通过后，再在 Codex App 中打开工作台目录并执行一次用户指定的往届国赛题端到端验收。
