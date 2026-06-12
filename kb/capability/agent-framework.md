# Agent 框架

> 能力分类: Agent 框架 (Agent Framework) | 更新时间: 2026-06-12

## 概述

Agent 框架是构建 AI Agent 的核心基础设施，提供 Agent 编排、工具调用、记忆管理、记忆管理、多 Agent 协作等基础能力。现代 Agent 框架通常采用 ReAct (Reasoning + Acting) 模式，让 LLM 通过"思考-行动-观察"的循环来完成任务。架构上一般包含：LLM 推理引擎、工具注册与调用、记忆系统（短期/长期）、规划器（Planner）和执行器（Executor）等核心组件。

2025-2026 年的趋势是从单一 Agent 向多 Agent 协作演进，框架开始原生支持 Agent 间通信、角色分工和层级化编排。同时，框架也在加强与 MCP (Model Context Protocol) 等标准化协议的集成，实现工具生态的互操作性。从工程角度看，生产级框架还需要提供可观测性、评估基准、安全沙箱等企业特性。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 编排模式 | 单 Agent / 多 Agent / 层级化 / 流水线 |
| 工具集成 | 内置工具 / 自定义工具 / MCP 协议 / REST API |
| 记忆管理 | 短期记忆(上下文窗口) / 长期记忆(向量DB) / 工作记忆 |
| 规划能力 | ReAct / Plan-and-Execute / Tree-of-Thought / LLM Compiler |
| 多 Agent 协作 | 角色分工 / 竞争辩论 / 层级审批 / 自由协作 |
| 可观测性 | Trace 追踪 / 日志 / 评估基准 / 成本监控 |
| 安全沙箱 | 权限控制 / 代码沙箱 / 输出过滤 / 人工审批 |
| 部署方式 | 本地 / 容器化 / Serverless / 托管服务 |

## 主流方案对比

| 方案 | Stars | 语言 | 架构 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|------|----------|
| LangChain | 137,836 | Python | 链式编排 | 生态最丰富，社区活跃，集成广泛 | 抽象层过多，学习曲线陡 | 快速原型、RAG 应用 |
| AutoGen | 58,477 | Python | 对话式多 Agent | 微软出品，多 Agent 对话原生支持 | 性能开销大，复杂编排受限 | 多 Agent 协作研究 |
| CrewAI | 52,338 | Python | 角色-任务模型 | 上手简单，角色分工直观 | 灵活性不如 LangChain | 团队协作场景 |
| OpenAI Agents | 26,714 | Python | 轻量多 Agent | 官方维护，设计简洁，Handoff 机制优雅 | 生态较新，社区资源少 | 生产级 Agent 应用 |
| Semantic Kernel | 27,996 | C# | 插件编排 | 微软生态深度集成，企业级 | 社区规模小，Python 生态弱 | .NET 企业应用 |
| MetaGPT | 68,351 | Python | 软件公司模拟 | 多角色协作，自动需求分析 | 复杂度高，实际落地案例少 | 软件工程 Agent |
| Hermes Agent | 170,701 | Python | 自我进化 | 工具链完整，技能系统丰富 | 较新，文档待完善 | 通用 Agent 开发 |
| SuperAGI | 17,541 | Python | 自主 Agent | 功能全面，GUI 管理面板 | 更新放缓，社区活跃度下降 | 自主 Agent 实验 |
| Agent-S | 11,666 | Python | 计算机操作 | OSWorld benchmark 领先 | 专注 GUI 操作，通用性受限 | 桌面自动化 |

## 选型决策树

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

特殊场景：
- 桌面/GUI 自动化 → Agent-S
- 需要自我进化能力 → Hermes Agent
- 快速验证想法 → CrewAI（最快上手）
```

## 快速上手

### LangChain 最小示例
```python
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
print(result["output"])
```

### CrewAI 最小示例
```python
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

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 170,701 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | The agent that grows with you |
| 137,836 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | The agent engineering platform |
| 68,351 | [geekan/MetaGPT](https://github.com/geekan/MetaGPT) | Python | The Multi-Agent Framework: First AI Software Company |
| 58,477 | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | A programming framework for agentic AI |
| 52,338 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | Framework for orchestrating role-playing, autonomous AI agents |
| 27,996 | [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | C# | Integrate cutting-edge LLM technology into your apps |
| 26,714 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Python | A lightweight, powerful framework for multi-agent workflows |
| 17,541 | [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | Python | SuperAGI: A dev-first open source autonomous AI agent framework |
| 11,666 | [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Python | Agent S: an open agentic framework that uses computers like a human |

## Awesome Lists

- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - AI 自主 Agent 精选列表
- [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) - AI Agents 精选资源
- [jim-schwoebel/awesome_ai_agents](https://github.com/jim-schwoebel/awesome_ai_agents) - 1500+ AI Agent 相关资源

## 扩展空间

> 🔲 待补充：垂直行业 Agent 框架（医疗、金融、法律等）
> 🔲 待补充：Agent 评估基准和 benchmark 对比
> 🔲 待补充：Agent 安全框架和对抗攻击防御
> 🔲 待补充：Agent 框架性能对比（延迟、吞吐量、成本）
> 🔲 待补充：MCP 协议在各框架中的集成方式
