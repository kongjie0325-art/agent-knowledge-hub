# Wiki Log

> 操作日志 — 仅追加，不修改历史记录。

## [2026-06-12] init | 初始化 wiki/ 目录结构
- 创建 wiki/index.md（全局索引）
- 创建 wiki/log.md（操作日志）
- 编译 10 篇能力域文章（capability/）
- 编译 4 篇行业文章（industry/）
- 来源: kb/capability/*.md, kb/industry/*.md
- 参考: Karpathy LLM Wiki 三层架构

## [2026-06-12] ingest | GitHub Top Agent Repositories
- 来源: kb/github-top-agent-repos.md
- 编译: wiki/capability/ 下 10 篇能力域文章
- 编译: wiki/industry/ 下 4 篇行业文章
- 创建 raw/ 源材料索引（14 个文件）
- 创建 references/ 模板（4 个文件）
- 创建 SKILL.md（ingest/query/lint 工作流）
- 创建 examples/ 示例文章

## [2026-06-12] raw/capability | 补全 6 个能力域源材料文件
- 重写 raw/capability/agent-framework.md（遵循 raw-template.md 格式）
- 重写 raw/capability/agent-platform.md（遵循 raw-template.md 格式）
- 重写 raw/capability/awesome-list.md（遵循 raw-template.md 格式）
- 重写 raw/capability/coding-agent.md（遵循 raw-template.md 格式）
- 重写 raw/capability/cookbook.md（遵循 raw-template.md 格式）
- 重写 raw/capability/learning.md（遵循 raw-template.md 格式）
- 来源: 从对应的 kb/capability/*.md 提取核心内容
- 格式: 元数据头 + 概述 + 核心矩阵 + 方案对比 + 决策树 + 快速上手 + 高引用仓库

## [2026-06-12] examples | 创建 3 篇示例文章
- 创建 examples/industry-example.md（医疗健康行业文章示例）
- 创建 examples/capability-example.md（MCP 能力域文章示例）
- 创建 examples/raw-example.md（Agent 框架源材料示例）
- 目的: 展示三种文章类型的编译格式，作为后续 Agent 编译的参考模板
