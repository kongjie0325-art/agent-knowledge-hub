# Agent 平台

> Sources: kb/capability/agent-platform.md; 2026-06-12
> Raw: [agent-platform](../../raw/capability/agent-platform.md)

## 概述

Agent 平台是面向生产的 Agent 开发和部署基础设施，在 Agent 框架之上提供可视化编排、监控告警、A/B 测试、版本管理、权限控制等企业级能力。与框架不同，平台关注的是"如何把 Agent 跑起来并管起来"——包括工作流编排 UI、运行时环境、部署管道、可观测性栈和团队协作功能。

当前 Agent 平台市场呈现两大流派：一是以 Dify、Flowise 为代表的低代码/无代码平台，通过拖拽式工作流降低 Agent 构建门槛；二是以 Coze、百川为代表的端到端 Agent 平台，提供从知识库管理到多渠道分发的完整闭环。

## 关键概念

- **编排方式**: 可视化拖拽 / 代码优先 / 混合模式
- **知识库集成**: RAG 管道 / 文档解析 / 向量数据库 / 混合检索
- **工具生态**: 内置工具 / 自定义工具 / MCP Server / API 插件
- **部署方式**: SaaS / 自托管 / 混合云 / 边缘部署
- **可观测性**: Trace / Metrics / Logging / 成本追踪
- **团队协作**: 多租户 / 角色权限 / 版本控制 / 审批流
- **评估测试**: A/B 测试 / 评估基准 / 回归测试 / 人工标注
- **渠道分发**: Web / API / Slack / 飞书 / 微信 / Discord

## 核心发现

1. **Dify 功能最全面**（142k+ Stars），知识库管理强，适合企业知识库 Agent 和客服场景
2. **Flowise 上手极快**（53k+ Stars），开源友好，UI 美观，适合快速原型
3. **Langchain-Chatchat 中文生态好**（38k+ Stars），支持国产模型
4. **AgentGPT 零部署**（36k+ Stars），浏览器即用，适合个人使用和 Demo
5. **2026 趋势**: MCP 协议深度集成、Agent 评估和安全合规能力加强

## 实践指南

### 选型决策树

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
```

### 快速上手

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

## See Also

- [Agent 框架](../capability/agent-framework.md) — Agent 框架是平台的基础层
- [UI/前端](../capability/ui-frontend.md) — Agent 平台的前端交互层

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/agent-platform.md 提炼
