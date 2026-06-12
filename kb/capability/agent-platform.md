# Agent 平台

> 能力分类: Agent 平台 (Agent Platform) | 更新时间: 2026-06-12

## 概述

Agent 平台是面向生产的 Agent 开发和部署基础设施，在 Agent 框架之上提供可视化编排、监控告警、A/B 测试、版本管理、权限控制等企业级能力。与框架不同，平台关注的是"如何把 Agent 跑起来并管起来"——包括工作流编排 UI、运行时环境、部署管道、可观测性栈和团队协作功能。

当前 Agent 平台市场呈现两大流派：一是以 Dify、Flowise 为代表的低代码/无代码平台，通过拖拽式工作流降低 Agent 构建门槛；二是以 Coze、百川为代表的端到端 Agent 平台，提供从知识库管理到多渠道分发的完整闭环。2026 年的趋势是平台开始深度集成 MCP 协议，让 Agent 能够即插即用各种外部工具，同时平台也在加强 Agent 评估和安全合规能力。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 编排方式 | 可视化拖拽 / 代码优先 / 混合模式 |
| 知识库集成 | RAG 管道 / 文档解析 / 向量数据库 / 混合检索 |
| 工具生态 | 内置工具 / 自定义工具 / MCP Server / API 插件 |
| 部署方式 | SaaS / 自托管 / 混合云 / 边缘部署 |
| 可观测性 | Trace / Metrics / Logging / 成本追踪 |
| 团队协作 | 多租户 / 角色权限 / 版本控制 / 审批流 |
| 评估测试 | A/B 测试 / 评估基准 / 回归测试 / 人工标注 |
| 渠道分发 | Web / API / Slack / 飞书 / 微信 / Discord |

## 主流方案对比

| 方案 | Stars | 语言 | 架构 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|------|----------|
| Dify | 142,950 | TypeScript | 低代码工作流 | 功能最全面，知识库管理强，社区活跃 | 自托管部署复杂度中 | 企业知识库 Agent、客服 |
| Flowise | 53,145 | TypeScript | 可视化拖拽 | 开源友好，上手极快，UI 美观 | 高级功能不如 Dify | 快速原型、教育场景 |
| Langchain-Chatchat | 38,098 | Python | RAG + Agent | 中文生态好，支持国产模型 | 架构较老旧 | 中文知识库问答 |
| AgentGPT | 36,137 | TypeScript | 浏览器端 | 零部署，浏览器即用 | 功能简单，不适合生产 | 个人使用、Demo |
| OpenAgents | 4,831 | Python | 开放平台 | 学术研究导向，工具丰富 | 生产化程度低 | 研究实验 |
| Gobii Platform | 450 | Python |  workforce | 专注 workforce 场景 | 太新，社区小 | 企业自动化 |

## 选型决策树

```
需要自托管？
├── 是 → 需要低代码？
│   ├── 是 → 中文场景？
│   │   ├── 是 → Langchain-Chatchat（中文生态好）
│   │   └── 否 → Dify（功能最全）/ Flowise（最易上手）
│   └── 否 → 自建平台（基于框架 + 自定义 UI）
└── 否 → SaaS 平台
    ├── 企业知识库 → Dify Cloud
    ├── 快速验证 → AgentGPT（浏览器即用）
    └── 企业自动化 → Gobii Platform

特殊场景：
- 需要多渠道路由 → Dify（内置渠道集成）
- 纯 RAG 知识库 → Langchain-Chatchat
- 教育/演示 → Flowise（最直观的拖拽 UI）
```

## 快速上手

### Docker 部署 Dify
```bash
# 克隆并启动 Dify
git clone https://github.com/langgenius/dify.git
cd docker
cp .env.example .env
docker compose up -d
# 访问 http://localhost/install
```

### Flowise 快速启动
```bash
# 使用 npx 一键启动
npx flowise start
# 或 Docker
docker run -d --name flowise -p 3000:3000 flowiseai/flowise
# 访问 http://localhost:3000
```

### 通过 API 调用 Agent
```bash
curl -X POST http://localhost/v1/chat-messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": {},
    "query": "什么是 Agent？",
    "response_mode": "streaming",
    "user": "user-001"
  }'
```

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 142,950 | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | Production-ready platform for agentic workflow development |
| 53,145 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | TypeScript | Build AI Agents, Visually |
| 38,098 | [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | Python | 基于 Langchain 与 ChatGLM/Qwen/Llama 的 RAG 与 Agent 框架 |
| 36,137 | [reworkd/AgentGPT](https://github.com/reworkd/AgentGPT) | TypeScript | Assemble, configure, and deploy autonomous AI Agents in your browser |
| 4,831 | [xlang-ai/OpenAgents](https://github.com/xlang-ai/OpenAgents) | Python | OpenAgents: An Open Platform for Language Agents in the Wild |
| 450 | [gobii-ai/gobii-platform](https://github.com/gobii-ai/gobii-platform) | Python | Your easy to use, always-on AI workforce |

## Awesome Lists

- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - AI 自主 Agent 精选列表
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 100+ 可运行的 AI Agent & RAG 应用

## 扩展空间

> 🔲 待补充：各平台性能基准对比（并发、延迟）
> 🔲 待补充：MCP 协议在各平台中的集成现状
> 🔲 待补充：企业级安全合规特性对比（SOC2、GDPR）
> 🔲 待补充：中国市场的 Agent 平台（Coze、百川、扣子）
> 🔲 待补充：平台间的迁移成本评估
