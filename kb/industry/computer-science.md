# 计算机科学 AI Agent

> 行业分类: 计算机科学 (Computer Science) | 更新时间: 2026-06-12

## 概述

AI Agent 在计算机科学领域的应用构成了整个智能体生态的技术基石。从底层大语言模型（LLM）训练与推理，到 Agent 框架、多智能体协作、工具调用和自主决策，计算机科学领域提供了支撑 AI Agent 运行的核心基础设施。该领域涵盖了模型架构设计、Agent 编排框架、强化学习对齐、推理优化以及开源模型生态等关键方向。

2026 年，计算机科学 AI Agent 的关键趋势包括：**Agent 框架成熟化**——LangChain、AutoGen、CrewAI 等框架已形成稳定的生态；**推理优化**——KV Cache、投机解码 (Speculative Decoding)、量化技术使 Agent 响应速度大幅提升；**多模态 Agent**——整合文本、图像、音频、视频的统一 Agent 成为标准；**Agent 工程化**——从原型到生产部署的工程化工具链（可观测性、评估、安全）日益完善。

## 子分类

### 1. LLM 模型与训练 (LLM Models & Training)
- **定义**：大语言模型预训练、微调、推理优化和开源模型生态
- **技术栈**：Transformer、LoRA/QLoRA、Flash Attention、vLLM、llama.cpp
- **代表工具**：Llama 3/4、Qwen 2.5、Gemma 3、DeepSeek-V3、Mistral

### 2. Agent 框架与编排 (Agent Frameworks & Orchestration)
- **定义**：单智能体和多智能体框架、工具调用、规划与推理链
- **技术栈**：LangChain、LlamaIndex、AutoGen、CrewAI、Semantic Kernel
- **代表工具**：LangGraph、OpenAI Agents SDK、Google ADK、Anthropic MCP

### 3. 模型对齐与强化学习 (Alignment & RL)
- **定义**：RLHF/DPO 对齐技术、奖励模型和安全对齐
- **技术栈**：PPO、DPO、KTO、Constitutional AI、红队测试
- **代表工具**：TRL (HuggingFace)、OpenRLHF、Anthropic 对齐研究

### 4. 推理优化 (Inference Optimization)
- **定义**：模型推理加速、量化和部署优化
- **技术栈**：GPTQ/AWQ 量化、TensorRT-LLM、SGLang、投机解码
- **代表工具**：vLLM、TensorRT-LLM、Ollama、SGLang

### 5. 多智能体系统 (Multi-Agent Systems)
- **定义**：多 Agent 协作、通信和博弈
- **技术栈**：博弈论、共识算法、Agent 通信协议 (A2A)
- **代表工具**：AutoGen、CrewAI、MetaGPT、Camel

### 6. Agent 工程化 (Agent Engineering)
- **定义**：Agent 开发、测试、部署和监控的工程化实践
- **技术栈**：LangSmith、Langfuse、评估框架、可观测性
- **代表工具**：LangSmith、Langfuse、Helicone、AgentOps

## 高引用仓库

### Agent 框架

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 100k+ | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python/TypeScript | 构建 LLM 应用的主流框架，提供链、Agent、工具集成等核心抽象 | Agent 框架与编排 |
| 170k | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | Hermes Agent: 开源智能体框架，支持多工具调用、技能系统和跨平台消息传递 | Agent 框架与编排 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | Microsoft 多智能体对话框架，支持多 Agent 协作完成复杂任务 | 多智能体系统 |
| 52k | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 多智能体编排框架，通过角色分工和任务委派实现团队协作 | 多智能体系统 |
| - | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Python | OpenAI 官方 Agent SDK，支持 handoffs、guardrails 和 tracing | Agent 框架与编排 |
| - | [google/adk-python](https://github.com/google/adk-python) | Python | Google Agent Development Kit，支持多 Agent 工作流 | Agent 框架与编排 |

### LLM 模型

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 140k | [huggingface/transformers](https://github.com/huggingface/transformers) | Python | 最广泛使用的 Transformer 模型库，支持数千种预训练模型 | LLM 模型与训练 |
| - | [meta-llama/llama](https://github.com/meta-llama/llama) | Python | Meta LLaMA 系列开源大模型，推动开源 LLM 生态发展 | LLM 模型与训练 |
| - | [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | Python | DeepSeek V3 开源大模型，MoE 架构，性能对标 GPT-4o | LLM 模型与训练 |
| - | [QwenLM/Qwen](https://github.com/QwenLM/Qwen) | Python | 阿里云 Qwen 系列大模型，支持多模态和长上下文 | LLM 模型与训练 |
| - | [google-deepmind/gemma](https://github.com/google-deepmind/gemma) | Python | Google Gemma 轻量级开源模型，基于 Gemini 技术 | LLM 模型与训练 |

### 推理优化

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 25k+ | [vllm-project/vllm](https://github.com/vllm-project/vllm) | Python | vLLM 高性能 LLM 推理引擎 | 推理优化 |
| 15k+ | [SGLang-project/sglang](https://github.com/SGLang-project/sglang) | Python | SGLang 高性能 LLM 推理框架 | 推理优化 |
| 10k+ | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | C++ | llama.cpp 本地 LLM 推理引擎 | 推理优化 |

### 对齐与安全

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 10k+ | [huggingface/trl](https://github.com/huggingface/trl) | Python | HuggingFace TRL 强化学习训练库 | 模型对齐 |
| 5k+ | [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | Python | OpenRLHF 开源 RLHF 训练框架 | 模型对齐 |

## 技术栈全景

| 类别 | 技术/工具 |
|------|-----------|
| 模型训练 | PyTorch, JAX, FSDP, DeepSpeed |
| 微调 | LoRA, QLoRA, PEFT, TRL |
| 推理 | vLLM, TensorRT-LLM, llama.cpp, Ollama |
| Agent 框架 | LangChain, AutoGen, CrewAI, Semantic Kernel |
| 工具协议 | MCP (Model Context Protocol), A2A |
| 评估 | LangSmith, Langfuse, AgentOps, Braintrust |
| 向量数据库 | Chroma, Milvus, Pinecone, Weaviate |

## 实施路径

1. **学习基础**：掌握 Transformer 架构和 LLM 基本原理
2. **框架选型**：根据场景选择 Agent 框架（LangChain / AutoGen / CrewAI）
3. **工具集成**：通过 MCP 或自定义工具扩展 Agent 能力
4. **原型开发**：构建最小可行 Agent，验证核心工作流
5. **评估优化**：建立评估基准，优化 Agent 性能和成本
6. **生产部署**：集成可观测性和安全机制，部署到生产环境
7. **持续迭代**：根据用户反馈和数据持续改进 Agent

## Awesome Lists

- [awesome-langchain](https://github.com/kyrolabs/awesome-langchain) — LangChain 生态精选资源
- [awesome-llm](https://github.com/Hannibal046/awesome-llm) — 大语言模型综合资源列表
- [awesome-open-gpt](https://github.com/EwingYangs/awesome-open-gpt) — 开源 GPT 相关项目汇总
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — AI Agent 精选列表
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (23.1k⭐) — Agent 技能大全

## 扩展空间

> 🔲 待补充：Agent 评测基准（GAIA、SWE-bench、WebArena、AgentBench）
> 🔲 待补充：代码生成 Agent（Cursor、GitHub Copilot、Devin、Claude Code）
> 🔲 待补充：Agent 记忆与长期上下文管理方案
> 🔲 待补充：本地 LLM 部署工具（llama.cpp、Ollama、vLLM）
> 🔲 待补充：Agent 安全与沙箱执行环境
> 🔲 待补充：Agent 可观测性和监控工具
> 🔲 待补充：Agent 通信协议（A2A、ACP）
> 🔲 待补充：Agent 技能市场与共享生态
