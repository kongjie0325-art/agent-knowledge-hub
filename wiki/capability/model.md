# 基础模型

> Sources: kb/capability/model.md; 2026-06-12
> Raw: [model](../../raw/capability/model.md)

## 概述

基础模型（Foundation Model）是通过大规模预训练获得的通用 AI 模型，是 AI 生态系统的基石。这些模型通常基于 Transformer 架构，在海量文本、代码、图像等多模态数据上训练，具备强大的语言理解、推理和生成能力。

2026 年的基础模型格局呈现几个关键趋势：一是中国模型（DeepSeek、Qwen、GLM）在能力上快速追赶甚至超越部分西方模型；二是 MoE（Mixture of Experts）架构成为主流；三是多模态能力成为标配；四是小模型蒸馏技术成熟。

## 关键概念

- **模型架构**: Dense Transformer / MoE / SSM(Mamba) / 混合架构
- **模态支持**: 文本 / 图像 / 音频 / 视频 / 代码 / 多模态
- **上下文窗口**: 4K / 32K / 128K / 1M+ tokens
- **训练方式**: 预训练 / SFT / RLHF / DPO / GRPO
- **推理优化**: 量化 / 蒸馏 / 推测解码 / KV Cache
- **开源程度**: 完全开源 / 权重开源 / API 仅 / 闭源
- **许可证**: Apache 2.0 / MIT / Llama License / 商业许可

## 核心发现

1. **DeepSeek-V3 性价比极高**（103k+ Stars），MoE 架构，推理能力强，开源
2. **Llama 3/4 社区最大**（59k+ Stars），工具链最完善，中文能力相对弱
3. **Qwen 2.5 中文能力最强**，全尺寸覆盖，国际社区影响力小
4. **MoE 架构主流化**: DeepSeek-V3 等模型通过稀疏激活实现高效推理
5. **小模型蒸馏成熟**: 7B 级别模型在特定任务上接近前代 70B 模型

## 实践指南

### 选型决策树

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
```

### 快速上手

```python
# 使用 HuggingFace Transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-V3-0324",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3-0324")
inputs = tokenizer("Hello, world!", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
```

```bash
# 使用 Ollama 运行开源模型
ollama run deepseek-r1
ollama run llama3.2
ollama run qwen2.5
```

## See Also

- [推理部署](../capability/inference.md) — 基础模型的推理和部署方案
- [学习资源](../capability/learning.md) — 模型学习资源

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/model.md 提炼
