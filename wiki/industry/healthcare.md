# 医疗健康 AI Agent

> Sources: kb/industry/healthcare.md; 2026-06-12
> Raw: [healthcare](../../raw/industry/healthcare.md)

## 概述

AI Agent 在医疗健康领域的应用正在经历爆发式增长，涵盖诊断辅助、药物研发、健康管理、医学研究、临床决策支持和医疗信息化等多个方向。大型语言模型（LLM）与 Agent 框架的结合，使得 AI 能够执行复杂的多步骤医疗推理、整合多模态数据（影像、文本、信号），并在虚拟 EHR 环境中模拟临床工作流程。

当前医疗 AI Agent 的关键趋势包括：多模态医疗 Agent、自主科研 Agent、临床基准测试标准化、药物重定位、精准医疗、以及 FHIR/HL7 标准下的 EHR 集成。

## 关键概念

- **多模态医疗 Agent**: 整合影像、文本、基因组等多源数据进行综合诊断
- **自主科研 Agent**: 能够自主规划、执行和迭代医学研究流程
- **临床基准测试**: MedAgentBench、AgentClinic 等标准化评估框架
- **药物重定位**: 多 Agent 协作加速老药新用的发现
- **精准医学**: 结合基因组学和临床数据的个性化治疗方案推荐
- **医疗信息化**: FHIR/HL7 标准下的 EHR 集成与互操作

## 核心发现

1. **TxAgent 哈佛医学院出品**，治疗推理 AI Agent，整合工具宇宙进行临床决策
2. **HealthFlow 自进化 Agent**，具备元规划能力，支持自主医学研究
3. **MedAgentBoard NeurIPS 2025**，多 Agent 协作医疗任务基准评测平台
4. **MedAgentBench 斯坦福出品**，真实虚拟 EHR 环境基准测试
5. **AgentClinic 多模态基准**，在模拟临床环境中评估 AI 诊断能力
6. **MedRAX 胸部 X 光推理 Agent**，集成 SOTA 影像分析工具

## 实践指南

### 应用场景优先级

1. **诊断辅助**: 医学影像分析、临床决策支持、症状检查与智能分诊
2. **药物研发**: 分子设计、临床试验优化、药物相互作用预测
3. **健康管理**: 慢病管理、个性化健康建议、远程患者监测
4. **医学研究**: 文献综述、生物信息学分析、自主科研

### 关键工具

```bash
# PyHealth 医疗深度学习工具包
pip install pyhealth
# 支持临床预测建模全流程

# MedRAX 胸部 X 光推理
# 集成 SOTA 影像分析工具与多模态 LLM
```

## See Also

- [Agent 框架](../capability/agent-framework.md) — 医疗 Agent 的底层框架
- [编码 Agent](../capability/coding-agent.md) — 医学研究中的 AI 编程助手

## 更新历史

- 2026-06-12 初始编译，从 kb/industry/healthcare.md 提炼
