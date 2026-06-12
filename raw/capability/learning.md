# 学习资源

> Source: kb/capability/learning.md
> Collected: 2026-06-12
> Published: 2026-06-12

## 概述

学习资源是 AI/Agent 开发者的知识补给站，涵盖从入门教程到高级课程、从理论讲解到实战项目的全方位学习材料。高质量的学习资源通常具备以下特点：循序渐进的课程结构、可运行的代码示例、理论与实践结合、以及持续的更新维护。

2026 年的 AI 学习资源呈现几个趋势：一是"从零到一"的完整课程（如 Karpathy 的 nn-zero-to-hero）比碎片化教程更受欢迎；二是 Agent 专项课程爆发式增长，涵盖 ReAct、多 Agent、工具调用等主题；三是视频课程和交互式教程（如 Jupyter Notebook 形式）成为主流；四是中国社区（B站、知乎、掘金）贡献了大量高质量的中文学习资源。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 内容形式 | 视频课程 / 文字教程 / Jupyter Notebook / 互动课程 |
| 难度分级 | 入门（零基础）/ 中级（有编程基础）/ 高级（研究级） |
| 覆盖范围 | 基础概念 / 模型训练 / Agent 开发 / 部署运维 / 论文解读 |
| 语言 | 英文 / 中文 / 多语言 |
| 认证 | 免费 / 付费 / 证书 |
| 实践项目 | 代码示例 / 完整项目 / 作业 / 竞赛 |

## 主流方案对比

| 方案 | Stars | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|----------|
| AI Agents for Beginners | 65,811 | 微软官方，零基础友好，12 课完整课程 | 内容较浅 | AI Agent 入门 |
| Nanochat | 54,301 | Karpathy 出品，$100 训练 ChatGPT | 需要 GPU | 理解 LLM 本质 |
| NN Zero to Hero | 22,796 | Karpathy 经典，从基础到 GPT | 内容较深 | 深度学习系统学习 |
| GenAI Agents | 22,240 | Agent 技术覆盖全面 | 质量参差 | Agent 技术全景 |

## 12 周 AI Agent 学习路径

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

## 快速上手

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

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 65,811 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | Jupyter Notebook | 12 Lessons to Get Started Building AI Agents |
| 54,301 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | Python | The best ChatGPT that $100 can buy |
| 22,796 | [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | Jupyter Notebook | Neural Networks: Zero to Hero |
| 22,240 | [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | Jupyter Notebook | 50+ tutorials for Generative AI Agent techniques |
