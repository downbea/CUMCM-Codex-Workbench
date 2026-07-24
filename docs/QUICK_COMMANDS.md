# 快捷触发短语

这些是约定的自然语言入口，不依赖 Codex App 是否支持自定义斜杠命令。

```text
/learn-papers 学习 inbox 中的全部论文
/start-contest 创建 2026 年 A 题项目
/select-topic 分析本届全部题目并执行快速 PoC
/review-cleaning 审核当前数据清洗方案
/review-models 审核当前候选模型
/freeze-results 确认并冻结当前结果
/build-paper 生成 Markdown、Word 和 PDF
/final-audit 执行三重独立审计
/check-upstream 检查参考仓库上游更新
```

Codex 看到这些短语时，应将它们解释为调用相应项目内 Skill，而不是操作系统命令。
