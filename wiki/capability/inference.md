# 推理部署

> Sources: kb/capability/inference.md; 2026-06-12
> Raw: [inference](../../raw/capability/inference.md)

## 概述

推理部署是 LLM 从研究走向生产的关键环节，涵盖模型推理优化、服务化部署、量化压缩、蒸馏加速等技术方向。核心挑战在于：如何在有限的 GPU 资源上实现低延迟、高吞吐的模型服务。

2026 年的趋势是推理部署的"民主化"——通过量化技术（GPTQ、AWQ、GGUF），70B 参数模型可以在消费级 GPU 上运行；通过推测解码（Speculative Decoding）和 KV Cache 优化，推理速度持续提升。

## 关键概念

- **推理引擎**: vLLM / TensorRT-LLM / llama.cpp / ONNX Runtime
- **量化技术**: GPTQ / AWQ / GGUF / SmoothQuant / FP8
- **加速技术**: PagedAttention / FlashAttention / Speculative Decoding
- **服务架构**: 单机 / 分布式 / Serverless / 边缘部署
- **模型格式**: Safetensors / GGUF / ONNX / TensorRT Engine
- **批处理策略**: Continuous Batching / Static Batching / Chunked Prefill
- **GPU 支持**: NVIDIA / AMD / Apple Silicon / Intel

## 核心发现

1. **Ollama 极简使用**（172k+ Stars），一键本地推理，模型管理完善，跨平台
2. **llama.cpp 硬件支持最广**（113k+ Stars），纯 C/C++ 推理，GGUF 量化，CPU 可跑
3. **vLLM GPU 吞吐最高**（81k+ Stars），PagedAttention 技术，Continuous Batching
4. **推理民主化**: 70B 模型可在消费级 GPU 上运行（量化后）
5. **边缘推理**: 手机、IoT 设备上运行小模型成为重要方向

## 实践指南

### 选型决策树

```
部署环境？
├── 本地/个人使用
│   ├── 需要最简单？ → Ollama（一键安装）
│   ├── 需要 CPU 推理？ → llama.cpp + GGUF
│   └── 需要 Apple Silicon？ → llama.cpp（Metal 支持好）
├── GPU 服务器
│   ├── NVIDIA GPU
│   │   ├── 追求极致吞吐？ → vLLM（PagedAttention）
│   │   └── 追求极致延迟？ → TensorRT-LLM
│   └── AMD GPU → llama.cpp（ROCm 支持）
└── 边缘设备
    ├── 手机 → llama.cpp + 量化小模型
    └── IoT → ONNX Runtime + 蒸馏模型
```

### 快速上手

```bash
# Ollama 一键推理
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3.2

# vLLM 部署
pip install vllm
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3.2-70B \
  --tensor-parallel-size 4

# llama.cpp 本地推理
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make -j
./main -m model-q4_k_m.gguf -n 256 -p "Hello, world!"
```

## See Also

- [基础模型](../capability/model.md) — 推理部署的模型层
- [Agent 框架](../capability/agent-framework.md) — Agent 框架使用推理引擎

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/inference.md 提炼
