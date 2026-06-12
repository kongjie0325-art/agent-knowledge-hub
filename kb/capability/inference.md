# 推理部署

> 能力分类: 推理部署 (Inference & Deployment) | 更新时间: 2026-06-12

## 概述

推理部署是 LLM 从研究走向生产的关键环节，涵盖模型推理优化、服务化部署、量化压缩、蒸馏加速等技术方向。核心挑战在于：如何在有限的 GPU 资源上实现低延迟、高吞吐的模型服务。主流技术栈包括：llama.cpp（纯 C/C++ 推理，支持 CPU 和 GPU）、vLLM（PagedAttention 技术，GPU 推理首选）、Ollama（一键本地推理）、TensorRT-LLM（NVIDIA 官方优化引擎）等。

2026 年的趋势是推理部署的"民主化"——通过量化技术（GPTQ、AWQ、GGUF），70B 参数模型可以在消费级 GPU 上运行；通过推测解码（Speculative Decoding）和 KV Cache 优化，推理速度持续提升。同时，边缘推理（在手机、IoT 设备上运行小模型）和混合云部署（敏感数据本地推理、复杂任务云端推理）也成为重要方向。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 推理引擎 | vLLM / TensorRT-LLM / llama.cpp / ONNX Runtime |
| 量化技术 | GPTQ / AWQ / GGUF / SmoothQuant / FP8 |
| 加速技术 | PagedAttention / FlashAttention / Speculative Decoding |
| 服务架构 | 单机 / 分布式 / Serverless / 边缘部署 |
| 模型格式 | Safetensors / GGUF / ONNX / TensorRT Engine |
| 批处理策略 | Continuous Batching / Static Batching / Chunked Prefill |
| GPU 支持 | NVIDIA / AMD / Apple Silicon / Intel |
| 监控 | 吞吐量 / 延迟 / GPU 利用率 / 队列深度 |

## 主流方案对比

| 方案 | Stars | 语言 | 架构 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|------|----------|
| Ollama | 172,480 | Go | 一键本地推理 | 极简使用，模型管理完善，跨平台 | 性能不如专用引擎 | 本地开发、个人使用 |
| llama.cpp | 113,427 | C++ | 纯 C/C++ 推理 | 硬件支持最广，GGUF 量化，CPU 可跑 | 新模型支持滞后 | 本地推理、边缘设备 |
| vLLM | 81,216 | Python | PagedAttention | GPU 吞吐最高，Continuous Batching | 仅 NVIDIA GPU | 生产级 GPU 推理 |
| Mistral Inference | 10,808 | Jupyter | 官方推理库 | Mistral 模型原生优化 | 仅 Mistral 系列 | Mistral 模型部署 |
| TensorRT-LLM | - | C++ | NVIDIA 优化 | NVIDIA GPU 上性能最优 | 仅 NVIDIA，配置复杂 | 企业级 NVIDIA 部署 |
| SGLang | - | Python | 结构化生成 | RadixAttention，结构化输出快 | 较新，生态待完善 | 结构化输出场景 |

## 选型决策树

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

模型大小：
- 7B 以下 → 消费级 GPU 即可（RTX 3060+）
- 13B-30B → 需要 24GB+ 显存或量化
- 70B+ → 需要多卡或 A100/H100
```

## 快速上手

### Ollama 一键推理
```bash
# 安装
curl -fsSL https://ollama.com/install.sh | sh
# 运行模型
ollama run llama3.2
# API 调用
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?"
}'
```

### vLLM 部署
```bash
# 安装
pip install vllm
# 启动 OpenAI 兼容服务
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3.2-70B \
  --tensor-parallel-size 4 \
  --dtype float16
# 调用
curl http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "meta-llama/Llama-3.2-70B", "prompt": "Hello"}'
```

### llama.cpp 本地推理
```bash
# 编译
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make -j
# 下载 GGUF 模型并运行
./main -m model-q4_k_m.gguf -n 256 -p "Hello, world!"
```

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 172,480 | [ollama/ollama](https://github.com/ollama/ollama) | Go | Run LLMs locally |
| 113,427 | [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | C++ | LLM inference in C/C++ |
| 81,216 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | Python | High-throughput and memory-efficient inference engine for LLMs |
| 10,808 | [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Jupyter Notebook | Official inference library for Mistral models |

## Awesome Lists

- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - LLM 精选列表（含推理部署）
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - AI 自主 Agent 精选列表

## 扩展空间

> 🔲 待补充：各推理引擎性能基准对比（tokens/sec、TTFT、TPS）
> 🔲 待补充：量化方案对比（精度损失 vs 速度提升）
> 🔲 待补充：分布式推理方案（张量并行、流水线并行）
> 🔲 待补充：边缘推理方案（手机、嵌入式设备）
> 🔲 待补充：推理成本优化策略（Spot 实例、模型路由）
