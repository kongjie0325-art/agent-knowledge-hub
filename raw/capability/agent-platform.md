# Agent 平台

> Source: kb/capability/agent-platform.md
> Collected: 2026-06-12
> Published: 2026-06-12

## 概述

Agent 平台是面向生产的 Agent 开发和部署基础设施，在 Agent 框架之上提供可视化编排、监控告警、A/B 测试、版本管理、权限控制等企业级能力。与框架不同，平台关注的是"如何把 Agent 跑起来并管起来"——包括工作流编排 UI、运行时环境、部署管道、可观测性栈和团队协作功能。

当前 Agent 平台市场呈现两大流派：一是以 Dify、Flowise 为代表的低代码/无代码平台，通过拖拽式工作流降低 Agent 构建门槛；二是以 Coze、百川为代表的端到端 Agent 平台，提供从知识库管理到多渠道分发的完整闭环。2026 年的趋势是平台开始深度集成 MCP 协议，让 Agent 能够即插即用各种外部工具。

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

| 方案 | Stars | 语言 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|----------|
| Dify | 142,950 | TypeScript | 功能最全面，知识库管理强 | 自托管部署复杂度中 | 企业知识库 Agent、客服 |
| Flowise | 53,145 | TypeScript | 开源友好，上手极快，UI 美观 | 高级功能不如 Dify | 快速原型、教育场景 |
| Langchain-Chatchat | 38,098 | Python | 中文生态好，支持国产模型 | 架构较老旧 | 中文知识库问答 |
| AgentGPT | 36,137 | TypeScript | 零部署，浏览器即用 | 功能简单 | 个人使用、Demo |

## 选型决策树

```
需要自托管？
├── 是 → 需要低代码？
│   ├── 是 → 中文场景？
│   │   ├── 是 → Langchain-Chatchat
│   │   └── 否 → Dify / Flowise
│   └── 否 → 自建平台
└── 否 → SaaS 平台
    ├── 企业知识库 → Dify Cloud
    ├── 快速验证 → AgentGPT
    └── 企业自动化 → Gobii Platform
```

## 快速上手

```bash
# Docker 部署 Dify
git clone https://github.com/langgenius/dify.git
cd docker
cp .env.example .env
docker compose up -d
# 访问 http://localhost/install

# Flowise 快速启动
npx flowise start
# 或 Docker
docker run -d --name flowise -p 3000:3000 flowiseai/flowise
```

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 142,950 | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | Production-ready platform for agentic workflow development |
| 53,145 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | TypeScript | Build AI Agents, Visually |
| 38,098 | [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | Python | 基于 Langchain 的 RAG 与 Agent 框架 |
| 36,137 | [reworkd/AgentGPT](https://github.com/reworkd/AgentGPT) | TypeScript | Assemble, configure, and deploy autonomous AI Agents in your browser |
