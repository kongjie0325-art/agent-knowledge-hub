# 源材料示例：Agent 框架

> **本文展示 raw/ 源材料的保存格式。** 以 Agent 框架为例，演示 raw/ 层如何存储从外部获取的原始资料索引。

---

## 元数据

| 字段 | 值 |
|------|-----|
| **标题** | Agent 框架 |
| **类型** | 源材料索引 (Raw Source Index) |
| **分类** | capability/agent-framework |
| **来源** | kb/capability/agent-framework.md |
| **收录时间** | 2026-06-12 |
| **状态** | ✅ 已收录 |

---

## 什么是 raw/ 源材料？

raw/ 是 Agent Knowledge Hub 的"原始资料"层，遵循 Karpathy LLM Wiki 的三层架构理念：

```
kb/  →  raw/  →  wiki/
输入      处理      输出
```

- **kb/**: 从外部获取的原始数据（GitHub 仓库列表、描述等）
- **raw/**: 将 kb/ 数据整理为标准化的源材料索引
- **wiki/**: 将 raw/ 提炼为结构化的知识文章

raw/ 的核心特性：
1. **不可变性**: 只读不写，保持原始资料的完整性
2. **可追溯性**: 每个文件都标注了来源和收录时间
3. **结构化**: 统一的格式，便于 Agent 处理

---

## 源材料内容

### 概述

Agent 框架是构建 AI Agent 的核心基础设施，提供 Agent 编排、工具调用、记忆管理、多 Agent 协作等基础能力。现代 Agent 框架通常采用 ReAct (Reasoning + Acting) 模式，让 LLM 通过"思考-行动-观察"的循环来完成任务。

2025-2026 年的趋势是从单一 Agent 向多 Agent 协作演进，框架开始原生支持 Agent 间通信、角色分工和层级化编排。同时，框架也在加强与 MCP 等标准化协议的集成。

### 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 编排模式 | 单 Agent / 多 Agent / 层级化 / 流水线 |
| 工具集成 | 内置工具 / 自定义工具 / MCP 协议 / REST API |
| 记忆管理 | 短期记忆 / 长期记忆 / 工作记忆 |
| 规划能力 | ReAct / Plan-and-Execute / Tree-of-Thought |
| 多 Agent 协作 | 角色分工 / 竞争辩论 / 层级审批 |
| 可观测性 | Trace / 日志 / 评估基准 / 成本监控 |
| 安全沙箱 | 权限控制 / 代码沙箱 / 输出过滤 |

### 主流方案对比

| 方案 | Stars | 语言 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|----------|
| LangChain | 137,836 | Python | 生态最丰富 | 抽象层过多 | 快速原型 |
| AutoGen | 58,477 | Python | 多 Agent 对话原生 | 性能开销大 | 协作研究 |
| CrewAI | 52,338 | Python | 上手简单 | 灵活性不足 | 团队场景 |
| OpenAI Agents | 26,714 | Python | 设计简洁 | 生态较新 | 生产应用 |
| MetaGPT | 68,351 | Python | 多角色协作 | 复杂度高 | 软件工程 |
| Hermes Agent | 170,701 | Python | 工具链完整 | 较新 | 通用开发 |

### 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 170,701 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | The agent that grows with you |
| 137,836 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | The agent engineering platform |
| 68,351 | [geekan/MetaGPT](https://github.com/geekan/MetaGPT) | Python | The Multi-Agent Framework |
| 58,477 | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | A programming framework for agentic AI |
| 52,338 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | Framework for orchestrating role-playing agents |
| 26,714 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Python | A lightweight framework for multi-agent workflows |

### Awesome Lists

- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — AI 自主 Agent 精选列表
- [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) — AI Agents 精选资源
- [jim-schwoebel/awesome_ai_agents](https://github.com/jim-schwoebel/awesome_ai_agents) — 1500+ AI Agent 相关资源

---

## 与 wiki/ 的关系

raw/ 中的内容会被编译为 wiki/ 中的结构化文章。编译过程：

1. **提取**: 从 raw/ 中提取核心信息
2. **组织**: 按照 article-template.md 格式重新组织
3. **提炼**: 去除冗余，补充交叉引用
4. **发布**: 输出到 wiki/capability/agent-framework.md

编译后的文章：[wiki/capability/agent-framework.md](../wiki/capability/agent-framework.md)

---

## 来源

- **原始资料**: [raw/capability/agent-framework.md](../../raw/capability/agent-framework.md)
- **上游来源**: kb/capability/agent-framework.md
- **格式遵循**: references/raw-template.md
