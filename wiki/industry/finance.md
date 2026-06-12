# 金融 AI Agent

> Sources: kb/industry/finance.md; 2026-06-12
> Raw: [finance](../../raw/industry/finance.md)

## 概述

AI Agent 在金融领域的应用正在快速扩展，涵盖量化交易、风险管理、合规审计、智能投顾、保险科技和金融数据分析等核心场景。2026 年，多 Agent 协作框架（如 TradingAgents、FinRobot）和开源金融 LLM（如 FinGPT）的成熟，正在将此前只有大型机构才能使用的交易与风控能力民主化。

金融 AI Agent 的核心价值在于：实时感知市场数据、自主推理决策、自动执行交易或风控操作，并持续从反馈中学习优化。

## 关键概念

- **量化交易**: 多 Agent 协作交易（基本面/技术面/情绪分析师）、策略回测、信号生成
- **风控管理**: 信用评分、反欺诈检测、实时监控预警、投资组合风险度量
- **合规审计**: KYC/AML 自动化、监管报告生成、合规检查
- **智能投顾**: 个性化资产配置、风险评估、投资组合再平衡
- **保险科技**: 理赔自动化、精算模型、欺诈理赔检测
- **金融数据分析**: 财务报表分析、市场情绪分析、宏观经济预测

## 核心发现

1. **TradingAgents 多 Agent 交易框架**（16k Stars），模拟真实交易公司角色分工
2. **AI Hedge Fund 概念验证**（15k Stars），15+ 专业 Agent 协作，支持本地 LLM
3. **FinRobot 开源金融 Agent 平台**（7k Stars），多模态金融数据处理
4. **FinGPT 开源金融 LLM**（7k Stars），单卡 RTX 3090 可训练，性能超越 GPT-4
5. **OpenBB 金融数据平台**，统一接入数十种数据源，支持 MCP Server

## 实践指南

### 应用场景优先级

1. **量化交易**: 多 Agent 协作交易、策略回测优化
2. **风控管理**: 信用评分、反欺诈、实时风险监控
3. **智能投顾**: 个性化资产配置、Robo-Advisor
4. **金融数据分析**: 财务报表分析、市场情绪分析

### 关键工具

```bash
# FinGPT 训练
git clone https://github.com/AI4Finance-Foundation/FinGPT.git
cd FinGPT
pip install -r requirements.txt
# 在单卡 RTX 3090 上可训练

# OpenBB 金融数据终端
pip install openbb
```

## See Also

- [Agent 框架](../capability/agent-framework.md) — 金融 Agent 的底层框架
- [推理部署](../capability/inference.md) — 金融模型的推理优化

## 更新历史

- 2026-06-12 初始编译，从 kb/industry/finance.md 提炼
