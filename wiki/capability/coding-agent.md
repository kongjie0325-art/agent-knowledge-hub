# 编码 Agent

> Sources: kb/capability/coding-agent.md; 2026-06-12
> Raw: [coding-agent](../../raw/capability/coding-agent.md)

## 概述

编码 Agent 是 AI 驱动的编程助手，能够理解代码上下文、生成代码、调试错误、重构代码库、执行代码审查，甚至自主完成完整的软件开发任务。从早期的代码补全（如 Copilot）到如今的自主编码 Agent（如 Claude Code、OpenHands），这一领域正在经历从"辅助工具"到"自主开发者"的范式转变。

现代编码 Agent 通常采用 Agentic 工作流：接收任务描述 → 分析代码库 → 制定计划 → 执行修改 → 运行测试 → 迭代修复。

## 关键概念

- **代码生成**: 函数/类/模块级别的代码生成，支持多语言
- **代码理解**: 代码库索引、依赖分析、架构理解
- **自主修复**: 根据错误输出自动迭代修复代码
- **代码审查**: 安全漏洞检测、风格检查、最佳实践建议
- **重构能力**: 大规模代码重构、技术债务清理
- **测试生成**: 单元测试、集成测试自动生成
- **沙箱执行**: 安全隔离的代码执行环境
- **多文件协调**: 跨文件修改的一致性和依赖管理

## 核心发现

1. **Claude Code 代码理解力极强**（127k+ Stars），工具链完整，自主修复能力强，依赖 Claude API
2. **OpenHands 开源全栈 Agent**（75k+ Stars），Web UI，完整的沙箱执行环境
3. **Devika 自动需求分析**（19k+ Stars），多语言支持，成熟度较低
4. **2026 趋势**: 多 Agent 协作编程（写代码 + 审查 + 测试），CI/CD 深度集成

## 实践指南

### 选型决策树

```
需要自主完成完整任务？
├── 是 → 需要最强代码理解力？
│   ├── 是 → Claude Code（终端 Agent，代码理解最强）
│   └── 否 → OpenHands（开源，Web UI，沙箱执行）
└── 否 → 只需要代码补全？
    ├── IDE 内 → GitHub Copilot / Cursor
    └── 终端内 → Aider（Git 原生配对）
```

### 快速上手

```bash
# Claude Code 安装与使用
npm install -g @anthropic-ai/claude-code
cd your-project
claude
# 自然语言描述任务，Claude Code 会自主完成

# OpenHands 部署
docker run -d --name openhands \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/.openhands:/openhands \
  -p 3000:3000 \
  ghcr.io/all-hands-ai/openhands:latest
```

## See Also

- [Agent 框架](../capability/agent-framework.md) — 编码 Agent 的底层框架
- [学习资源](../capability/learning.md) — 编程学习资源

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/coding-agent.md 提炼
