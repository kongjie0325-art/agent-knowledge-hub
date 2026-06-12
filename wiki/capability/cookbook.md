# Cookbook

> Sources: kb/capability/cookbook.md; 2026-06-12
> Raw: [cookbook](../../raw/capability/cookbook.md)

## 概述

Cookbook 是面向实践的知识库，以"食谱"（Recipe）的形式组织代码示例和教程，每个食谱解决一个具体问题。在 AI/Agent 领域，Cookbook 通常由模型厂商（OpenAI、Anthropic、Google）官方维护，展示如何使用其 API 实现常见任务。

Cookbook 与文档和教程的区别在于：Cookbook 是"即插即用"的——每个示例都是可运行的代码，开发者可以直接复制使用。2026 年，Cookbook 已经从简单的 API 调用示例进化为包含 Agent 工作流、MCP 集成、多模态应用的完整项目。

## 关键概念

- **内容形式**: Jupyter Notebook / Markdown / 代码文件
- **难度分级**: 入门 / 中级 / 高级
- **覆盖范围**: API 调用 / RAG / Agent / 多模态 / 微调
- **语言支持**: Python / TypeScript / cURL / 多语言
- **运行环境**: Google Colab / 本地 / Docker / 在线
- **可运行性**: 一键运行 / 需配置 / 需 API Key

## 核心发现

1. **OpenAI Cookbook 最权威**（73k+ Stars），覆盖最全，质量最高，仅 OpenAI API
2. **Anthropic Cookbook 含 MCP 集成**（44k+ Stars），Claude 最佳实践
3. **Gemini Cookbook 多模态示例好**（17k+ Stars），Google 生态
4. **2026 趋势**: Agent 工作流、MCP 集成、多模态应用成为 Cookbook 新方向

## 实践指南

### 选型决策树

```
使用哪个模型/平台？
├── OpenAI → OpenAI Cookbook（最权威）
├── Anthropic → Anthropic Cookbook（含 MCP 集成）
├── Google Gemini → Gemini Cookbook
├── LangChain → LangChain Cookbook
└── 多平台通用 → 从 OpenAI Cookbook 开始（概念通用）
```

### 学习路径

1. **入门**: 先跑通"Hello World"示例
2. **进阶**: 学习 RAG 和函数调用示例
3. **高级**: 研究 Agent 编排和多模态示例

### 快速上手

```bash
# OpenAI Cookbook
git clone https://github.com/openai/openai-cookbook.git
cd openai-cookbook
pip install openai jupyter
export OPENAI_API_KEY="sk-xxx"
jupyter notebook

# Anthropic Cookbook
git clone https://github.com/anthropics/anthropic-cookbook.git
cd anthropic-cookbook
pip install anthropic
export ANTHROPIC_API_KEY="sk-xxx"
```

## See Also

- [Awesome List](../capability/awesome-list.md) — Awesome List 是 Cookbook 的资源发现入口
- [学习资源](../capability/learning.md) — Cookbook 是学习资源的重要形式

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/cookbook.md 提炼
