# Cookbook

> Source: kb/capability/cookbook.md
> Collected: 2026-06-12
> Published: 2026-06-12

## 概述

Cookbook 是面向实践的知识库，以"食谱"（Recipe）的形式组织代码示例和教程，每个食谱解决一个具体问题。在 AI/Agent 领域，Cookbook 通常由模型厂商（OpenAI、Anthropic、Google）官方维护，展示如何使用其 API 实现常见任务：从基础的文本生成、函数调用，到复杂的 RAG 管道、Agent 编排、多模态应用。

Cookbook 与文档和教程的区别在于：Cookbook 是"即插即用"的——每个示例都是可运行的代码，开发者可以直接复制使用。高质量的 Cookbook 通常包含：完整的可运行代码、预期输出、常见问题解答、以及进阶变体。2026 年，Cookbook 已经从简单的 API 调用示例进化为包含 Agent 工作流、MCP 集成、多模态应用的完整项目。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 内容形式 | Jupyter Notebook / Markdown / 代码文件 |
| 难度分级 | 入门 / 中级 / 高级 |
| 覆盖范围 | API 调用 / RAG / Agent / 多模态 / 微调 |
| 语言支持 | Python / TypeScript / cURL / 多语言 |
| 运行环境 | Google Colab / 本地 / Docker / 在线 |
| 可运行性 | 一键运行 / 需配置 / 需 API Key |

## 主流方案对比

| 方案 | Stars | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|----------|
| OpenAI Cookbook | 73,819 | 最权威，覆盖最全，质量最高 | 仅 OpenAI API | OpenAI API 学习 |
| Anthropic Cookbook | 44,487 | Claude 最佳实践，含 MCP 集成 | 仅 Anthropic API | Claude API 学习 |
| Gemini Cookbook | 17,307 | Google 生态，多模态示例好 | 仅 Google API | Gemini API 学习 |

## 学习路径

1. **入门**: 先跑通"Hello World"示例
2. **进阶**: 学习 RAG 和函数调用示例
3. **高级**: 研究 Agent 编排和多模态示例

## 快速上手

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

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 73,819 | [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Jupyter Notebook | Examples and guides for using the OpenAI API |
| 44,487 | [anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | Jupyter Notebook | Notebooks/recipes showcasing effective ways of using Claude |
| 17,307 | [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | Jupyter Notebook | Examples and guides for using the Gemini API |
