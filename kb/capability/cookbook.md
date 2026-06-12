# Cookbook

> 能力分类: Cookbook (Cookbooks) | 更新时间: 2026-06-12

## 概述

Cookbook 是面向实践的知识库，以"食谱"（Recipe）的形式组织代码示例和教程，每个食谱解决一个具体问题。在 AI/Agent 领域，Cookbook 通常由模型厂商（OpenAI、Anthropic、Google）官方维护，展示如何使用其 API 实现常见任务：从基础的文本生成、函数调用，到复杂的 RAG 管道、Agent 编排、多模态应用。

Cookbook 与文档（Documentation）和教程（Tutorial）的区别在于：Cookbook 是"即插即用"的——每个示例都是可运行的代码，开发者可以直接复制使用，然后根据自己的需求修改。高质量的 Cookbook 通常包含：完整的可运行代码、预期输出、常见问题解答、以及进阶变体。2026 年，Cookbook 已经从简单的 API 调用示例进化为包含 Agent 工作流、MCP 集成、多模态应用的完整项目。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 内容形式 | Jupyter Notebook / Markdown / 代码文件 |
| 难度分级 | 入门 / 中级 / 高级 |
| 覆盖范围 | API 调用 / RAG / Agent / 多模态 / 微调 |
| 语言支持 | Python / TypeScript / cURL / 多语言 |
| 运行环境 | Google Colab / 本地 / Docker / 在线 |
| 更新频率 | 随 API 版本更新 / 社区贡献 |
| 可运行性 | 一键运行 / 需配置 / 需 API Key |

## 主流方案对比

| 方案 | Stars | 语言 | 架构 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|------|----------|
| OpenAI Cookbook | 73,819 | Jupyter | 官方示例 | 最权威，覆盖最全，质量最高 | 仅 OpenAI API | OpenAI API 学习 |
| Anthropic Cookbook | 44,487 | Jupyter | 官方示例 | Claude 最佳实践，含 MCP 集成 | 仅 Anthropic API | Claude API 学习 |
| Gemini Cookbook | 17,307 | Jupyter | 官方示例 | Google 生态，多模态示例好 | 仅 Google API | Gemini API 学习 |
| LangChain Cookbook | - | Python | 社区示例 | 框架集成示例多 | 质量参差不齐 | LangChain 学习 |
| Llama Cookbook | - | Python | Meta 官方 | Llama 模型专用 | 覆盖面有限 | Llama 微调/部署 |

## 选型决策树

```
使用哪个模型/平台？
├── OpenAI → OpenAI Cookbook（最权威）
├── Anthropic → Anthropic Cookbook（含 MCP 集成）
├── Google Gemini → Gemini Cookbook
├── LangChain → LangChain Cookbook
└── 多平台通用 → 从 OpenAI Cookbook 开始（概念通用）

学习路径：
1. 入门：先跑通"Hello World"示例
2. 进阶：学习 RAG 和函数调用示例
3. 高级：研究 Agent 编排和多模态示例
```

## 快速上手

### OpenAI Cookbook 使用
```bash
# 克隆仓库
git clone https://github.com/openai/openai-cookbook.git
cd openai-cookbook

# 安装依赖
pip install openai jupyter

# 设置 API Key
export OPENAI_API_KEY="sk-xxx"

# 启动 Jupyter
jupyter notebook
# 浏览 examples/ 目录下的示例
```

### 运行一个简单示例
```python
# 最小 OpenAI API 调用
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### Anthropic Cookbook 使用
```bash
git clone https://github.com/anthropics/anthropic-cookbook.git
cd anthropic-cookbook
pip install anthropic
# 设置 API Key
export ANTHROPIC_API_KEY="sk-xxx"
# 浏览 notebooks/ 目录
```

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 73,819 | [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Jupyter Notebook | Examples and guides for using the OpenAI API |
| 44,487 | [anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | Jupyter Notebook | Notebooks/recipes showcasing effective ways of using Claude |
| 17,307 | [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | Jupyter Notebook | Examples and guides for using the Gemini API |

## Awesome Lists

- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 100+ 可运行的 AI Agent & RAG 应用
- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - LLM 精选列表

## 扩展空间

> 🔲 待补充：各 Cookbook 的示例分类和数量统计
> 🔲 待补充：开源模型（Llama、DeepSeek、Qwen）的 Cookbook
> 🔲 待补充：Agent 专项 Cookbook（ReAct、多 Agent、工具调用）
> 🔲 待补充：中文 Cookbook 资源
> 🔲 待补充：Cookbook 示例的可运行性验证状态
