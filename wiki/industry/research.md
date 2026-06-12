# 科研 AI Agent

> Sources: kb/industry/research.md; 2026-06-12
> Raw: [research](../../raw/industry/research.md)

## 概述

> 行业分类: 科研 (Scientific Research) | 更新时间: 2026-06-12

## 关键概念

- 1. 文献综述与知识管理
- 自动检索、阅读和综合大量科学文献，生成结构化综述
- 关键技术栈：RAG、向量数据库
- 2. 实验设计与数据分析
- AI 辅助实验方案规划、假设生成和统计分析
- 关键技术栈：贝叶斯优化、AutoML、因果推断
- 3. 科学计算与模拟
- 利用 Agent 编排复杂的科学计算工作流
- 关键技术栈：HPC 调度、容器化
- 4. 论文写作与学术出版
- AI 辅助论文撰写、图表生成、同行评审回复
- 关键技术栈：LaTeX 生成、学术 NLP、引用管理
- 5. 跨学科研究 Agent
- 整合生物学、化学、物理学、计算机科学等多学科知识
- 关键技术栈：知识图谱、多模态 LLM、工具调用

## 核心发现

- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** (2.7k forks⭐): 138个科学技能，含物理/化学/生物/材料等多学科
- **[HICAI-ZJU/SciToolAgent](https://github.com/HICAI-ZJU/SciToolAgent)** (-⭐): 科学工具知识图谱驱动 Agent
- **[mrkingsleyobi/synapseflow](https://github.com/mrkingsleyobi/synapseflow)** (-⭐): 66-Agent 编排的 AI 研究助手
- **[InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills)** (-⭐): 科学研究 Agent 技能精选列表
- **[handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools)** (-⭐): 自动化研究工具精选（含 AI-Scientist, ARIS）
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** (170k⭐): 通用 Agent 框架
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** (138k⭐): 最流行的 LLM 应用框架
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** (127k⭐): AI 编码助手
- **[microsoft/autogen](https://github.com/microsoft/autogen)** (58k⭐): 多 Agent 协作框架
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** (52k⭐): 多角色 Agent 框架

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 2.7k forks | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 138个科学技能，含物理/化学/生物/材料等多学科 | 跨学科研究 Agent |
| - | [HICAI-ZJU/SciToolAgent](https://github.com/HICAI-ZJU/SciToolAgent) | Python | 科学工具知识图谱驱动 Agent | 跨学科研究 Agent |
| - | [mrkingsleyobi/synapseflow](https://github.com/mrkingsleyobi/synapseflow) | Python | 66-Agent 编排的 AI 研究助手 | 实验设计与数据分析 |
| - | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | Markdown | 科学研究 Agent 技能精选列表 | 跨学科研究 Agent |
| - | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | Markdown | 自动化研究工具精选（含 AI-Scientist, ARIS） | 实验设计与数据分析 |

| Stars | 仓库 | 语言 | 描述 | 适用场景 |
|-------|------|------|------|----------|
| 170k | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 通用 Agent 框架 | 跨学科研究 Agent |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | 最流行的 LLM 应用框架 | 通用 |
| 127k | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Python | AI 编码助手 | 科学计算与模拟 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 多 Agent 协作框架 | 跨学科研究 Agent |
| 52k | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 多角色 Agent 框架 | 跨学科研究 Agent |

## 实践指南

### 1. 文献综述与知识管理
- 自动检索、阅读和综合大量科学文献，生成结构化综述
- 关键技术栈：RAG、向量数据库（Pinecone/Chroma）、LLM 摘要
- 代表性工具：Semantic Scholar API、Elicit、Consensus、Aries
### 2. 实验设计与数据分析
- AI 辅助实验方案规划、假设生成和统计分析
- 关键技术栈：贝叶斯优化、AutoML、因果推断
- 代表性工具：AI-Scientist、OpenAI Codex for Science、Jupyter Agent
### 3. 科学计算与模拟
- 利用 Agent 编排复杂的科学计算工作流（CFD、MD、DFT 等）
- 关键技术栈：HPC 调度、容器化（Docker/Singularity）、工作流引擎
- 代表性工具：SimScale SDK、PyAEDT、ASE（原子模拟环境）
### 4. 论文写作与学术出版
- AI 辅助论文撰写、图表生成、同行评审回复
- 关键技术栈：LaTeX 生成、学术 NLP、引用管理
- 代表性工具：Paperpal、Writefull、Academic Writer Agent
### 5. 跨学科研究 Agent
- 整合生物学、化学、物理学、计算机科学等多学科知识
- 关键技术栈：知识图谱、多模态 LLM、工具调用
- 代表性工具：SciToolAgent、K-Dense-AI Scientific Skills
### 6. 开放科学与可复现性
- 自动化实验记录、数据管理和可复现性验证
- 关键技术栈：数据版本控制（DVC）、MLflow、开放数据标准
- 代表性工具：DVC、Open Science Framework、Zenodo API

## Awesome Lists

- [awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) (1.6k⭐) - AI for Science 综合精选
- [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) - 科学 Agent 技能大全
- [Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) - 自动化研究工具精选
- [Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) - 科学研究 Agent 技能精选
- [labclaw/awesome-physical-ai-for-science](https://github.com/labclaw/awesome-physical-ai-for-science) - 物理 AI for Science 精选
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (23.1k⭐) - 精选 Agent 技能大全

## 扩展空间

> 🔲 待补充：自主科研 Agent 框架（AI-Scientist、AutoResearchClaw）
> 🔲 待补充：科学实验数据管理与可复现性工具
> 🔲 待补充：跨学科知识图谱构建工具
> 🔲 待补充：科研伦理与 AI 治理框架
> 🔲 待补充：HPC 集成与大规模模拟 Agent
> 🔲 待补充：科研写作与学术出版 Agent 工具链

## See Also

- [航空航天 AI Agent](../aerospace.md) — 相关行业 AI Agent 应用
- [农业 AI Agent](../agriculture.md) — 相关行业 AI Agent 应用
- [汽车 AI Agent](../automotive.md) — 相关行业 AI Agent 应用
- [生物学 AI Agent](../biology.md) — 相关行业 AI Agent 应用
- [化学工程 AI Agent](../chemical-engineering.md) — 相关行业 AI Agent 应用
- [Agent 框架](../../capability/agent-framework.md) — 行业 Agent 的底层框架
- [编码 Agent](../../capability/coding-agent.md) — AI 编程助手

## 来源

- kb/industry/research.md

## 更新历史

- 2026-06-12 初始编译，从 kb/industry 提炼
