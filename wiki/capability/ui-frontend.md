# UI/前端

> Sources: kb/capability/ui-frontend.md; 2026-06-12
> Raw: [ui-frontend](../../raw/capability/ui-frontend.md)

## 概述

UI/前端领域为 AI 应用提供用户交互界面，涵盖聊天界面、Agent 可视化、工作流编排 UI、模型管理面板等方向。在 AI Agent 生态中，前端不仅是用户对话的窗口，更是 Agent 行为的可视化面板——展示 Agent 的思考过程、工具调用链、多 Agent 协作状态等。

当前 AI 前端的核心技术栈以 React/Next.js 和 Vue 为主，TypeScript 已成为标配。2026 年的趋势是：流式输出（Streaming）成为 Agent 对话的标配体验；Agent 可视化（展示思考链、工具调用、多 Agent 协作图）成为差异化竞争力。

## 关键概念

- **对话界面**: 流式输出 / Markdown 渲染 / 代码高亮 / 多模态展示
- **Agent 可视化**: 思考链展示 / 工具调用图 / 多 Agent 协作视图
- **工作流 UI**: 拖拽编排 / 节点编辑 / 实时预览 / 调试面板
- **模型管理**: 模型切换 / 参数调节 / 用量统计 / 成本追踪
- **技术栈**: React / Vue / Svelte / Next.js / Nuxt
- **组件库**: shadcn/ui / Ant Design / Radix UI / Tailwind
- **AI SDK**: Vercel AI SDK / LangChain UI / Chainlit

## 核心发现

1. **Open WebUI 功能最全**（138k+ Stars），支持多模型后端，自托管
2. **LobeChat UI 美观**（77k+ Stars），插件系统，多模型支持
3. **Vercel AI SDK 流式输出最佳实践**，需自建 UI
4. **Chainlit Python 原生**，快速构建 AI 对话，前端定制受限
5. **2026 趋势**: WebGPU 浏览器端推理、Agent 可视化、移动端 AI 应用

## 实践指南

### 选型决策树

```
使用场景？
├── 个人 AI 对话界面
│   ├── 需要多模型支持？ → Open WebUI（最全）/ LobeChat（最美）
│   └── 需要插件生态？ → LobeChat（插件系统完善）
├── 开发 AI 应用
│   ├── Python 为主 → Chainlit（最快上手）
│   ├── React/Next.js → Vercel AI SDK（流式输出最佳）
│   └── 需要工作流 UI → Dify Frontend
└── ML 模型演示
    └── Gradio（5 分钟出 Demo）
```

### 快速上手

```bash
# Open WebUI 部署
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main

# LobeChat 部署
docker run -d -p 3210:3210 \
  -e OPENAI_API_KEY=sk-xxx \
  --name lobe-chat lobehub/lobe-chat
```

```typescript
// Vercel AI SDK 最小示例
import { openai } from "@ai-sdk/openai";
import { streamText } from "ai";

const result = streamText({
  model: openai("gpt-4o"),
  messages: [{ role: "user", content: "Hello!" }],
});
for await (const chunk of result.textStream) {
  // 流式输出到前端
}
```

## See Also

- [Agent 平台](../capability/agent-platform.md) — Agent 平台的前端层
- [推理部署](../capability/inference.md) — 前端连接的推理后端

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/ui-frontend.md 提炼
