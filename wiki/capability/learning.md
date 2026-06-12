# 学习资源

> Sources: kb/capability/learning.md; 2026-06-12
> Raw: [learning](../../raw/capability/learning.md)

## 概述

学习资源是 AI/Agent 开发者的知识补给站，涵盖从入门教程到高级课程、从理论讲解到实战项目的全方位学习材料。高质量的学习资源通常具备以下特点：循序渐进的课程结构、可运行的代码示例、理论与实践结合、以及持续的更新维护。

2026 年的 AI 学习资源呈现几个趋势：一是"从零到一"的完整课程（如 Karpathy 的 nn-zero-to-hero）比碎片化教程更受欢迎；二是 Agent 专项课程爆发式增长；三是视频课程和交互式教程（如 Jupyter Notebook 形式）成为主流。

## 关键概念

- **内容形式**: 视频课程 / 文字教程 / Jupyter Notebook / 互动课程
- **难度分级**: 入门（零基础）/ 中级（有编程基础）/ 高级（研究级）
- **覆盖范围**: 基础概念 / 模型训练 / Agent 开发 / 部署运维 / 论文解读
- **语言**: 英文 / 中文 / 多语言
- **认证**: 免费 / 付费 / 证书
- **实践项目**: 代码示例 / 完整项目 / 作业 / 竞赛

## 核心发现

1. **AI Agents for Beginners 微软官方**（65k+ Stars），零基础友好，12 课完整课程
2. **Nanochat Karpathy 出品**（54k+ Stars），$100 训练 ChatGPT，理解 LLM 本质
3. **NN Zero to Hero Karpathy 经典**（22k+ Stars），从基础到 GPT，内容较深
4. **GenAI Agents 50+ 教程**（22k+ Stars），Agent 技术覆盖全面
5. **12 周学习路径**: 基础 → Agent 基础 → 工具与记忆 → 多 Agent → 生产化 → 项目实战

## 实践指南

### 12 周 AI Agent 学习路径

```
第 1-2 周：基础概念
- AI Agents for Beginners（微软，12 课）
- 了解 LLM、Prompt Engineering、RAG 基础

第 3-4 周：Agent 基础
- LangChain / CrewAI 入门
- 实现第一个 ReAct Agent

第 5-6 周：工具与记忆
- 工具调用（Function Calling）
- 记忆系统（短期 + 长期）

第 7-8 周：多 Agent
- AutoGen / CrewAI 多 Agent
- Agent 协作模式

第 9-10 周：生产化
- 部署与监控
- 安全与评估

第 11-12 周：项目实战
- 构建一个完整的 Agent 应用
- 部署到生产环境
```

### 快速上手

```bash
# 运行 Nanochat
git clone https://github.com/karpathy/nanochat.git
cd nanochat
pip install -r requirements.txt
python train.py  # 需要 GPU
python chat.py

# 使用 GenAI Agents 教程
git clone https://github.com/NirDiamant/GenAI_Agents.git
cd GenAI_Agents
jupyter notebook
```

## See Also

- [基础模型](../capability/model.md) — 学习资源的核心主题
- [编码 Agent](../capability/coding-agent.md) — 编程学习资源
- [Awesome List](../capability/awesome-list.md) — 学习资源的发现入口

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/learning.md 提炼
