# 上游参考项目

本工作台独立维护，不直接 fork 或运行时依赖下列仓库。

- `Yuan1z0825/nature-skills`：固定参考提交 `91862221b39f7ca16d52ae0e1e9cb6c2bb31a96b`。重点借鉴短路由、按需加载、图件契约、源数据追溯和确定性 QA。许可证：Apache-2.0。
- `zhnnky329/MathModeling-skills`：固定参考提交 `50a2942007a98e74cd0948b44d7cb8e4826d15c9`。重点借鉴 Gate、PoC、人类决策、冻结数字和独立审计，同时修正路径不一致、流程依赖矛盾和纯提示词状态机问题。

运行 `scripts/check-upstream.ps1` 只会生成差异报告，不会自动修改正式 Skills。
