# 基础模型

> 能力分类: 基础模型 (Foundation Model) | 更新时间: 2026-06-12

## 概述

基础模型（Foundation Model）是通过大规模预训练获得的通用 AI 模型，是 AI 生态系统的基石。这些模型通常基于 Transformer 架构，在海量文本、代码、图像等多模态数据上训练，具备强大的语言理解、推理和生成能力。基础模型可分为闭源（GPT-4o、Claude 3.5、Gemini 2.0）和开源（Llama、DeepSeek、Qwen、Mistral）两大阵营。

2026 年的基础模型格局呈现几个关键趋势：一是中国模型（DeepSeek、Qwen、GLM）在能力上快速追赶甚至超越部分西方模型；二是 MoE（Mixture of Experts）架构成为主流，DeepSeek-V3 等模型通过稀疏激活实现高效推理；三是多模态能力成为标配，模型原生支持文本、图像、音频、视频的理解和生成；四是小模型蒸馏技术成熟，7B 级别模型在特定任务上接近前代 70B 模型的表现。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 模型架构 | Dense Transformer / MoE / SSM(Mamba) / 混合架构 |
| 模态支持 | 文本 / 图像 / 音频 / 视频 / 代码 / 多模态 |
| 上下文窗口 | 4K / 32K / 128K / 1M+ tokens |
| 训练方式 | 预训练 / SFT / RLHF / DPO / GRPO |
| 推理优化 | 量化 / 蒸馏 / 推测解码 / KV Cache |
| 开源程度 | 完全开源 / 权重开源 / API 仅 / 闭源 |
| 许可证 | Apache 2.0 / MIT / Llama License / 商业许可 |
| 部署方式 | 本地推理 / API 调用 / 托管服务 |

## 主流方案对比

| 方案 | Stars | 语言 | 架构 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|------|----------|
| DeepSeek-V3 | 103,638 | Python | MoE | 性价比极高，推理能力强，开源 | 模型较大，部署资源要求高 | 通用推理、代码生成 |
| Llama 3/4 | 59,437 | Python | Dense/MoE | 社区最大，工具链最完善 | 中文能力相对弱 | 通用场景、微调基座 |
| Qwen 2.5 | - | Python | Dense | 中文能力最强，全尺寸覆盖 | 国际社区影响力小 | 中文应用、多模态 |
| Mistral | - | Python | Dense | 欧洲开源之光，推理效率高 | 大尺寸模型竞争力下降 | 欧洲合规场景 |
| Gemma 2 | - | Python | Dense | Google 出品，轻量级 | 模型尺寸偏小 | 轻量级应用 |
| GLM-4 | - | Python | Dense | 智谱出品，中文能力强 | 开源程度有限 | 中文企业应用 |

## 选型决策树

```
需要开源模型？
├── 是 → 中文场景为主？
│   ├── 是 → Qwen 2.5（中文最强）/ DeepSeek-V3（综合能力最强）
│   └── 否 → 需要最大社区？
│       ├── 是 → Llama 3/4（生态最完善）
│       └── 否 → Mistral（欧洲合规）/ Gemma 2（轻量）
└── 否 → 闭源 API
    ├── 最强推理 → Claude 3.5 / GPT-4o
    ├── 性价比 → DeepSeek API / Gemini 2.0 Flash
    └── 代码生成 → Claude 3.5 Sonnet / GPT-4o

模型大小选择：
- 资源受限 / 边缘 → 7B-8B 级别（Llama 3.2 8B, Qwen 2.5 7B）
- 通用场景 → 14B-70B 级别（DeepSeek-V3 671B MoE, Llama 3 70B）
- 最高性能 → 405B+ 级别（Llama 3.1 405B, GPT-4o）
```

## 快速上手

### 使用 Ollama 运行开源模型
```bash
# 运行 DeepSeek
ollama run deepseek-r1
# 运行 Llama
ollama run llama3.2
# 运行 Qwen
ollama run qwen2.5
```

### 使用 HuggingFace Transformers
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-V3-0324",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3-0324")

inputs = tokenizer("Hello, world!", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0]))
```

### 使用 vLLM 部署 API
```bash
# 部署 DeepSeek
python -m vllm.entrypoints.openai.api_server \
  --model deepseek-ai/DeepSeek-V3-0324 \
  --tensor-parallel-size 8 \
  --max-model-len 131072
```

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 103,638 | [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | Python | DeepSeek V3 model |
| 59,437 | [meta-llama/llama](https://github.com/meta-llama/llama) | Python | Inference code for Llama models |

## Awesome Lists

- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - LLM 精选列表
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - AI 自主 Agent 精选列表

## 扩展空间

> 🔲 待补充：2026 年主流模型能力排行榜（MMLU、HumanEval、GSM8K 等）
> 🔲 待补充：各模型的推理成本对比（input/output token 价格）
> 🔲 待补充：微调方案对比（LoRA / QLoRA / Full Fine-tuning）
> 🔲 待补充：MoE 模型架构详解和部署指南
> 🔲 待补充：多模态模型（视觉-语言-音频）能力矩阵
