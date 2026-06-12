# Agent 框架

> Sources: kb/capability/agent-framework.md; 2026-06-12
> Raw: [agent-framework](../../raw/capability/agent-framework.md)

## 概述

Agent 框架是构建 AI Agent 的核心基础设施，提供 Agent 编排、工具调用、记忆管理、多 Agent 协作等基础能力。现代 Agent 框架通常采用 ReAct (Reasoning + Acting) 模式，让 LLM 通过"思考-行动-观察"的循环来完成任务。架构上一般包含：LLM 推理引擎、工具注册与调用、记忆系统（短期/长期）、规划器（Planner）和执行器（Executor）等核心组件。

2025-2026 年的趋势是从单一 Agent 向多 Agent 协作演进，框架开始原生支持 Agent 间通信、角色分工和层级化编排。同时，框架也在加强与 MCP (Model Context Protocol) 等标准化协议的集成，实现工具生态的互操作性。

## 关键概念

- **ReAct 模式**: 推理（Reasoning）+ 行动（Acting）的循环，是当前 Agent 框架的核心范式
- **编排模式**: 单 Agent / 多 Agent / 层级化 / 流水线
- **工具集成**: 内置工具 / 自定义工具 / MCP 协议 / REST API
- **记忆管理**: 短期记忆（上下文窗口）/ 长期记忆（向量DB）/ 工作记忆
- **规划能力**: ReAct / Plan-and-Execute / Tree-of-Thought / LLM Compiler
- **多 Agent 协作**: 角色分工 / 竞争辩论 / 层级审批 / 自由协作
- **可观测性**: Trace 追踪 / 日志 / 评估基准 / 成本监控
- **安全沙箱**: 权限控制 / 代码沙箱 / 输出过滤 / 人工审批

## 核心发现

1. **LangChain 生态最丰富**（137k+ Stars），适合快速原型和 RAG 应用，但抽象层过多
2. **AutoGen 多 Agent 对话原生**（58k+ Stars），微软出品，适合多 Agent 协作研究
3. **CrewAI 上手最简单**（52k+ Stars），角色-任务模型直观，适合团队协作场景
4. **OpenAI Agents 设计简洁**（26k+ Stars），Handoff 机制优雅，适合生产级应用
5. **MetaGPT 软件公司模拟**（68k+ Stars），多角色协作，自动需求分析
6. **Hermes Agent 工具链完整**（170k+ Stars），技能系统丰富，支持自我进化

## 实践指南

### 选型决策树

```
需要多 Agent 协作？
├── 是 → 需要对话式交互？
│   ├── 是 → AutoGen（微软生态）/ CrewAI（简单角色分工）
│   └── 否 → OpenAI Agents（Handoff 机制）/ MetaGPT（软件团队）
└── 否 → 需要丰富工具生态？
    ├── 是 → LangChain（最大生态）/ Hermes Agent（完整工具链）
    └── 否 → 企业 .NET 环境？
        ├── 是 → Semantic Kernel
        └── 否 → OpenAI Agents（轻量简洁）
```

### 快速上手

```python
# LangChain 最小示例
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """搜索互联网"""
    return f"Results for: {query}"

llm = ChatOpenAI(model="gpt-4o")
agent = create_react_agent(llm, [search], prompt="You are a helpful assistant")
executor = AgentExecutor(agent=agent, tools=[search])
result = executor.invoke({"input": "What's the weather in Tokyo?"})
```

```python
# CrewAI 最小示例
from crewai import Agent, Task, Crew

researcher = Agent(
    role="Research Analyst",
    goal="Find the latest AI trends",
    backstory="You are an expert research analyst"
)
task = Task(
    description="Research top 5 AI trends in 2026",
    expected_output="A list of 5 trends with brief descriptions",
    agent=researcher
)
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()
```

## See Also

- [Agent 平台](../capability/agent-platform.md) — Agent 框架之上的生产化平台
- [编码 Agent](../capability/coding-agent.md) — 面向代码开发的专项 Agent
- [MCP 生态](../capability/mcp.md) — Agent 工具集成的标准化协议

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/agent-framework.md 提炼
