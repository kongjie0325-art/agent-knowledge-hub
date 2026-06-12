# 学习资源

> 能力分类: 学习资源 (Learning Resources) | 更新时间: 2026-06-12

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
| 更新频率 | 持续更新 / 一次性 / 定期更新 |
| 认证 | 免费 / 付费 / 证书 |
| 实践项目 | 代码示例 / 完整项目 / 作业 / 竞赛 |

## 主流方案对比

| 方案 | Stars | 语言 | 架构 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|------|----------|
| AI Agents for Beginners | 65,811 | Jupyter | 12 课教程 | 微软官方，零基础友好，完整课程 | 内容较浅 | AI Agent 入门 |
| Nanochat | 54,301 | Python | 极简实现 | Karpathy 出品，$100 训练 ChatGPT | 需要 GPU | 理解 LLM 本质 |
| NN Zero to Hero | 22,796 | Jupyter | 系列课程 | Karpathy 经典，从基础到 GPT | 内容较深 | 深度学习系统学习 |
| GenAI Agents | 22,240 | Jupyter | 50+ 教程 | Agent 技术覆盖全面 | 质量参差 | Agent 技术全景 |
| Learn AI Engineering | 5,642 | - | 资源合集 | 从零学 AI/LLMs，免费资源 | 非结构化 | 自学路径规划 |
| Complete Agentic AI | 5,156 | Jupyter | 完整课程 | Agentic AI 工程全流程 | 较新，待验证 | Agent 工程实践 |
| AI Agents Masterclass | 3,406 | Python | 项目代码 | 实战项目驱动 | 文档较少 | 项目实战 |

## 选型决策树

```
目标？
├── 零基础入门 AI Agent
│   └── AI Agents for Beginners（微软官方，12 课）
├── 理解 LLM 本质
│   ├── 理论 → NN Zero to Hero（Karpathy 经典）
│   └── 实践 → Nanochat（$100 训练 ChatGPT）
├── 学习 Agent 开发
│   ├── 全面覆盖 → GenAI Agents（50+ 教程）
│   └── 工程实践 → Complete Agentic AI
└── 自学路径规划
    └── Learn AI Engineering（免费资源合集）

学习方式偏好：
- 视频学习 → YouTube（Karpathy、AI Explained）
- 文字教程 → GitHub README + Jupyter Notebook
- 互动学习 → Kaggle Notebooks / Google Colab
- 项目实战 → AI Agents Masterclass
```

## 快速上手

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

### 运行 Nanochat
```bash
git clone https://github.com/karpathy/nanochat.git
cd nanochat
pip install -r requirements.txt
# 训练（需要 GPU）
python train.py
# 推理
python chat.py
```

### 使用 GenAI Agents 教程
```bash
git clone https://github.com/NirDiamant/GenAI_Agents.git
cd GenAI_Agents
pip install -r requirements.txt
# 浏览 tutorials/ 目录
jupyter notebook
```

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 65,811 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | Jupyter Notebook | 12 Lessons to Get Started Building AI Agents |
| 54,301 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | Python | The best ChatGPT that $100 can buy |
| 22,796 | [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | Jupyter Notebook | Neural Networks: Zero to Hero |
| 22,240 | [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | Jupyter Notebook | 50+ tutorials for Generative AI Agent techniques |
| 5,642 | [ashishps1/learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering) | - | Learn AI and LLMs from scratch using free resources |
| 5,156 | [ed-donner/agents](https://github.com/ed-donner/agents) | Jupyter Notebook | Repo for the Complete Agentic AI Engineering Course |
| 3,406 | [coleam00/ai-agents-masterclass](https://github.com/coleam00/ai-agents-masterclass) | Python | AI Agents Masterclass code |

## Awesome Lists

- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - AI 自主 Agent 精选列表
- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - LLM 精选列表
- [ashishps1/learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering) - AI 学习资源合集

## 扩展空间

> 🔲 待补充：中文学习资源精选（B站、知乎、掘金等）
> 🔲 待补充：各课程的难度评级和时间估算
> 🔲 待补充：AI Agent 专项认证和考试
> 🔲 待补充：论文阅读清单（Agent 领域经典论文）
> 🔲 待补充：社区学习小组和讨论渠道
