# 首次本机验收维护报告

- 日期：2026-07-24
- 范围：首次本机验收报告中的非阻断维护项
- 工作台仓库：`CUMCM-Codex-Workbench`
- 知识库仓库：`CUMCM-Knowledge-Vault`
- 结论：维护目标全部完成，回归测试通过，可以继续使用

## 修改摘要

### 静态代码质量

使用当前虚拟环境中的 Ruff 对 `src/` 和 `tests/` 执行安全自动修复。当前 Ruff 版本共应用 37 条自动修复，完整覆盖首次验收报告中的 29 条可自动修复问题，并同时处理复检时暴露的同类导入排序、空行、未使用导入和 `datetime.UTC` 旧写法问题。

`src/cummcm_workbench/ocr.py` 中函数内单行可选导入无法由 Ruff 自动整理，已手工改为结构化 `try/except` 导入。异常类型、错误消息和公开函数签名保持不变。

修改文件：

- `src/cummcm_workbench/audit.py`
- `src/cummcm_workbench/cli.py`
- `src/cummcm_workbench/config.py`
- `src/cummcm_workbench/contest.py`
- `src/cummcm_workbench/data_audit.py`
- `src/cummcm_workbench/dependency.py`
- `src/cummcm_workbench/freeze.py`
- `src/cummcm_workbench/hashing.py`
- `src/cummcm_workbench/knowledge.py`
- `src/cummcm_workbench/logs.py`
- `src/cummcm_workbench/manifest.py`
- `src/cummcm_workbench/ocr.py`
- `src/cummcm_workbench/paper.py`
- `src/cummcm_workbench/references.py`
- `src/cummcm_workbench/state.py`
- `tests/test_dependency.py`
- `tests/test_freeze.py`
- `tests/test_knowledge.py`
- `tests/test_manifest.py`
- `tests/test_paper.py`
- `tests/test_state.py`

### SVM 示例兼容性

修改文件：

- `CUMCM-Knowledge-Vault/40-Code-Examples/svm/example.py`

修改原因：`SVC(probability=True)` 在当前 scikit-learn 中已弃用，并计划在未来版本移除。

处理方式：使用官方建议的 `CalibratedClassifierCV(SVC(...), ensemble=False)` 提供概率校准能力，保留标准化、SVC 核心参数、随机种子、五折交叉验证、ROC-AUC 指标和 `result.json` 输出结构。

行为对比：

- 修复前五折 ROC-AUC：`0.9665289256198347`
- 修复后五折 ROC-AUC：`0.9665289256198347`
- 绝对差异：`0.0`
- 原弃用警告：已消失

### 自动更新的验证产物

- `CUMCM-Knowledge-Vault/99-System/seed-example-validation.json`
- `CUMCM-Knowledge-Vault/99-System/index/knowledge.joblib`

## 回归测试结果

| 检查项 | 结果 | 证据摘要 |
|---|---|---|
| Ruff：工作台源码与测试 | PASS | `All checks passed!` |
| Ruff：SVM 示例 | PASS | `All checks passed!` |
| Python 编译检查 | PASS | `src/`、`tests/` 编译无错误 |
| 核心测试 | PASS | `6 passed` |
| 52 个算法示例 | PASS | `52/52`，失败数 `0` |
| 知识索引构建 | PASS | 成功索引 `81` 篇文档 |
| TOPSIS 中文检索 | PASS | `TOPSIS.md` 排名第 1 |
| Word 生成 | PASS | DOCX 成功生成 |
| PDF 生成 | PASS | PDF 成功导出 |
| Word 原生公式 | PASS | DOCX 内检测到 OMML `m:oMath` |
| 补丁完整性 | PASS | `git diff --check` 无错误 |

## 接口与内容保护检查

- 未修改算法原理。
- 未修改模型卡内容或目录结构。
- 未修改现有 CLI 子命令、函数签名或结果文件结构。
- 未覆盖、删除或重置任何 Git 历史或用户文件。

## 仍未解决的问题

无工作台代码级未解决问题。

测试阶段仍会出现来自第三方 `joblib` 与 NumPy 2.5 组合的 `DeprecationWarning`。该警告位于虚拟环境依赖内部，不影响当前索引读写或测试结果，也不属于本次工作台源码和 SVM 示例的维护范围。后续依赖升级时应再次核验。

Windows Git 同时提示未来签出时可能把 LF 转换为 CRLF；当前补丁完整性检查通过，文件内容和运行结果未受影响。
