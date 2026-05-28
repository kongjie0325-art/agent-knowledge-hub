# 计算机科学 AI Agent

> 行业分类: 计算机科学 (Computer Science) | 更新时间: 2026-05-28

## 概述

AI Agent 在计算机科学领域的应用构成了整个智能体生态的技术基石。从底层大语言模型（LLM）训练与推理，到 Agent 框架、多智能体协作、工具调用和自主决策，计算机科学领域提供了支撑 AI Agent 运行的核心基础设施。该领域涵盖了模型架构设计、Agent 编排框架、强化学习对齐、推理优化以及开源模型生态等关键方向。

## 子分类

### LLM 模型与训练
- 大语言模型预训练与微调
- 模型推理优化（量化、蒸馏、KV Cache）
- 开源模型生态（Llama、Qwen、Gemma、Mistral）

### Agent 框架与编排
- 单智能体框架（LangChain、LlamaIndex）
- 多智能体协作框架（AutoGen、CrewAI）
- 工具调用与函数执行
- 规划与推理链（ReAct、CoT、ToT）

### 模型对齐与强化学习
- RLHF / DPO 对齐技术
- 奖励模型与偏好学习
- 安全对齐与红队测试

### 开源模型生态
- Transformer 架构实现
- 模型部署与服务化
- 多模态模型

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| - | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | Hermes Agent: 开源智能体框架，支持多工具调用、技能系统和跨平台消息传递 | Agent 框架与编排 |
| 100k+ | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python/TypeScript | 构建 LLM 应用的主流框架，提供链、Agent、工具集成等核心抽象 | Agent 框架与编排 |
| - | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | Microsoft 多智能体对话框架，支持多 Agent 协作完成复杂任务 | Agent 框架与编排 |
| - | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 多智能体编排框架，通过角色分工和任务委派实现团队协作 | Agent 框架与编排 |
| - | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Python | OpenAI 官方 Agent SDK，支持 handoffs、guardrails 和 tracing | Agent 框架与编排 |
| - | [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | Python | DeepSeek V3 开源大模型，MoE 架构，性能对标 GPT-4o | LLM 模型与训练 |
| 140k+ | [huggingface/transformers](https://github.com/huggingface/transformers) | Python | 最广泛使用的 Transformer 模型库，支持数千种预训练模型 | 开源模型生态 |
| - | [meta-llama/llama](https://github.com/meta-llama/llama) | Python | Meta LLaMA 系列开源大模型，推动开源 LLM 生态发展 | LLM 模型与训练 |
| - | [google-deepmind/gemma](https://github.com/google-deepmind/gemma) | Python | Google Gemma 轻量级开源模型，基于 Gemini 技术 | LLM 模型与训练 |
| - | [QwenLM/Qwen](https://github.com/QwenLM/Qwen) | Python | 阿里云 Qwen 系列大模型，支持多模态和长上下文 | LLM 模型与训练 |
| - | [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Python | Mistral AI 推理框架，高效部署 Mistral 系列模型 | LLM 模型与训练 |

## Awesome Lists

- [awesome-langchain](https://github.com/kyrolabs/awesome-langchain) - LangChain 生态精选资源
- [awesome-llm](https://github.com/Hannibal046/awesome-llm) - 大语言模型综合资源列表
- [awesome-open-gpt](https://github.com/EwingYangs/awesome-open-gpt) - 开源 GPT 相关项目汇总

## 相关资源

- [Hugging Face Hub](https://huggingface.co/models) - 开源模型托管与分享平台
- [Papers With Code](https://paperswithcode.com) - 论文与代码对应检索平台

## 扩展空间

> 🔲 待补充：Agent 评测基准（GAIA、SWE-bench、WebArena）
> 🔲 待补充：代码生成 Agent（Cursor、GitHub Copilot、Devin）
> 🔲 待补充：Agent 记忆与长期上下文管理方案
> 🔲 待补充：本地 LLM 部署工具（llama.cpp、Ollama、vLLM）
> 🔲 待补充：Agent 安全与沙箱执行环境
