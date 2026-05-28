# 医疗健康 AI Agent

> 行业分类: 医疗健康 (Healthcare) | 更新时间: 2026-05-28

## 概述

AI Agent 在医疗健康领域的应用正在经历爆发式增长，涵盖诊断辅助、药物研发、健康管理、医学研究、临床决策支持和医疗信息化等多个方向。大型语言模型（LLM）与 Agent 框架的结合，使得 AI 能够执行复杂的多步骤医疗推理、整合多模态数据（影像、文本、信号），并在虚拟 EHR 环境中模拟临床工作流程。

当前医疗 AI Agent 的关键趋势包括：
- **多模态医疗 Agent**：整合影像、文本、基因组等多源数据进行综合诊断
- **自主科研 Agent**：能够自主规划、执行和迭代医学研究流程
- **临床基准测试**：MedAgentBench、AgentClinic 等标准化评估框架的出现
- **药物重定位**：多 Agent 协作加速老药新用的发现
- **精准医学**：结合基因组学和临床数据的个性化治疗方案推荐
- **医疗信息化**：FHIR/HL7 标准下的 EHR 集成与互操作

## 子分类

### 1. 诊断辅助
- 医学影像分析（X-ray、CT、MRI、病理切片）
- 临床决策支持系统（CDSS）
- 症状检查与智能分诊
- 多模态诊断 Agent（影像 + 文本 + 实验室数据）

### 2. 药物研发
- 分子设计与药物生成
- 临床试验优化与设计
- 药物相互作用预测
- 药物重定位（Drug Repurposing）
- ADMET 预测与药代动力学建模

### 3. 健康管理
- 慢病管理与监测
- 个性化健康建议
- 心理健康筛查与干预
- 可穿戴设备数据整合
- 远程患者监测（RPM）

### 4. 医学研究
- 文献综述与知识综合
- 生物信息学分析
- 基因组学与蛋白质组学
- 自主科研 Agent
- 多 Agent 协作研究

### 5. 临床基准与评估
- 虚拟 EHR 环境仿真
- 临床推理能力评估
- 多 Agent 协作基准
- 医学 VQA（视觉问答）评估
- 医疗 Agent 安全性与可信度评测

### 6. 医疗信息化与互操作
- EHR/EMR 系统集成
- FHIR/HL7 标准支持
- 临床数据标准化
- 医疗 NLP 与文本挖掘
- 医院信息系统（HIS）智能化

## 高引用仓库

### 医疗专用 Agent

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 11,666 | [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Python | Agent S: 开放式 Agentic 框架，像人类一样操作计算机（OSWorld 基准） | 诊断辅助 |
| - | [mims-harvard/TxAgent](https://github.com/mims-harvard/TxAgent) | Python | 哈佛医学院出品，治疗推理 AI Agent，整合工具宇宙进行临床决策 | 诊断辅助 |
| - | [yhzhu99/HealthFlow](https://github.com/yhzhu99/HealthFlow) | Python | 自进化 AI Agent，具备元规划能力，支持自主医学研究 | 医学研究 |
| - | [yhzhu99/MedAgentBoard](https://github.com/yhzhu99/MedAgentBoard) | Python | NeurIPS 2025，多 Agent 协作医疗任务基准评测平台 | 临床基准与评估 |
| - | [stanfordmlgroup/MedAgentBench](https://github.com/stanfordmlgroup/MedAgentBench) | Python | 斯坦福出品，真实虚拟 EHR 环境，用于基准测试医疗 LLM Agent | 临床基准与评估 |
| - | [gersteinlab/medagents-benchmark](https://github.com/gersteinlab/medagents-benchmark) | Python | 耶鲁出品，评估思维模型和 Agent 框架在复杂医学推理中的表现 | 临床基准与评估 |
| - | [samuelschmidgall/agentclinic](https://github.com/samuelschmidgall/agentclinic) | Python | 多模态 Agent 基准，在模拟临床环境中评估 AI 诊断能力 | 临床基准与评估 |
| - | [bowang-lab/MedRAX](https://github.com/bowang-lab/MedRAX) | Python | 胸部 X 光医学推理 Agent，集成 SOTA 影像分析工具与多模态 LLM | 诊断辅助 |
| - | [sunlabuiuc/PyHealth](https://github.com/sunlabuiuc/PyHealth) | Python | 医疗深度学习工具包，支持临床预测建模全流程 | 医疗信息化与互操作 |
| - | [ncbi-nlp/Clinical-Tool-Learning](https://github.com/ncbi-nlp/Clinical-Tool-Learning) | Python | AgentMD: 自主整理和应用临床计算器的 LLM Agent | 临床决策支持 |
| - | [pharmbio/repuragent](https://github.com/pharmbio/repuragent) | Python | 多 Agent 药物重定位系统，自主规划和执行药物发现工作流 | 药物研发 |

### 科学研究 Agent 技能

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 2.7k  forks | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 138 个科学技能，含临床研究/精准医学/生物信息学 21+ 技能 | 医学研究 |
| - | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | Markdown | 科学研究 Agent 技能精选列表 | 医学研究 |
| - | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | Markdown | 自动化研究工具精选（含 AI-Scientist, AutoResearchClaw, ARIS） | 医学研究 |
| - | [mrkingsleyobi/synapseflow](https://github.com/mrkingsleyobi/synapseflow) | Python | 66-Agent 编排的 AI 研究助手 | 医学研究 |
| - | [HICAI-ZJU/SciToolAgent](https://github.com/HICAI-ZJU/SciToolAgent) | Python | 科学工具知识图谱驱动的 Agent | 医学研究 |

### 通用 Agent 框架

| Stars | 仓库 | 语言 | 描述 | 适用场景 |
|-------|------|------|------|----------|
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | 开源 LLM 应用开发平台，支持医疗应用快速搭建 | 医疗信息化 |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | 最流行的 LLM 应用框架，广泛用于医疗 Agent 构建 | 通用 |
| 138k | [open-webui/open-webui](https://github.com/open-webui/open-webui) | Svelte | 开源 AI 交互界面，可集成医疗 LLM 应用 | 医疗信息化 |
| 127k | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Rust | Claude Code: 终端 AI 编程助手，支持医疗代码开发 | 医学研究 |
| 77k | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | TypeScript | 开源 LLM 聊天框架，可定制医疗对话 Agent | 健康管理 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 微软多 Agent 框架，支持医疗多 Agent 协作场景 | 临床决策支持 |
| 53k | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | TypeScript | 低代码 LLM 流程构建器，快速搭建医疗工作流 | 医疗信息化 |
| 52k | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 多 Agent 协作框架，适用于医疗团队模拟 | 临床决策支持 |
| 23.1k | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Markdown | 精选 Agent 技能列表，含医疗领域技能 | 通用 |

## Awesome Lists

### 医疗健康专用
- [AgenticHealthAI/Awesome-AI-Agents-for-Healthcare](https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare) - 医疗 AI Agent 精选列表（含 TxAgent、HealthFlow、MedAgentsBench 等）
- [AIM-Research-Lab/Awesome-AI-Agents-Medicine](https://github.com/AIM-Research-Lab/Awesome-AI-Agents-Medicine) - 医学 AI Agent 资源（含 MMedAgent 等多模态医疗 Agent）
- [yczhou001/Awesome-Medical-LLM-Agent](https://github.com/yczhou001/Awesome-Medical-LLM-Agent) - 从医疗 LLM 到通用医疗 Agent 的综合调查与资源
- [FreedomIntelligence/Awesome-LLM-Patient-Simulators](https://github.com/FreedomIntelligence/Awesome-LLM-Patient-Simulators) - LLM 患者模拟器论文集合

### 科学研究相关
- [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) (1.6k⭐) - AI for Science 综合精选
- [Webioinfo01/Awesome-AI-Meets-Biology](https://github.com/Webioinfo01/Awesome-AI-Meets-Biology) - AI 与生物学交叉应用综述
- [labclaw/awesome-physical-ai-for-science](https://github.com/labclaw/awesome-physical-ai-for-science) - 物理 AI for Science 精选
- [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) - 自动化研究工具精选

### 通用 Agent
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (23.1k⭐) - 精选 Agent 技能大全
- [luo-junyu/Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) (2.7k⭐) - LLM Agent 研究论文综合收集

## 相关资源

- [BEHAVIOR-1K](https://github.com/StanfordVL/BEHAVIOR-1K) - 1000 项日常活动模拟基准（可用于医疗场景模拟）
- [google/fhir](https://github.com/google/fhir) (940⭐) - Google FHIR 标准实现，医疗数据互操作
- [hapifhir/hapi-fhir](https://github.com/hapifhir/hapi-fhir) (2.3k⭐) - Java FHIR 服务器与客户端库
- [medplum/medplum](https://github.com/medplum/medplum) (2.3k⭐) - 开源 FHIR 服务器，支持医疗应用开发
- [openemr/openemr](https://github.com/openemr/openemr) (3.9k⭐) - 开源电子病历系统
- [frappe/erpnext](https://github.com/frappe/erpnext) - 开源 ERP 系统（含医疗模块）
- [metriport/metriport](https://github.com/metriport/metriport) (731⭐) - 医疗数据 API 集成平台
- [baeseongsu/awesome-machine-learning-for-healthcare](https://github.com/baeseongsu/awesome-machine-learning-for-healthcare) - 医疗机器学习研究精选
- [ai-in-health/medllmspracticalguide](https://github.com/ai-in-health/medllmspracticalguide) - 医疗 LLM 实践指南（Nature 论文配套）
- [richard-peng-xia/awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) - 医学成像多模态学习资源

## 扩展空间

> 🔲 待补充：FDA 合规与医疗 AI 监管工具
> 🔲 待补充：医疗数据隐私和安全工具（HIPAA 合规）
> 🔲 待补充：远程医疗 Agent 平台
> 🔲 待补充：医疗影像专用 Agent（病理、放射、超声）
> 🔲 待补充：基因组学分析 Agent 工具链
> 🔲 待补充：医疗 NLP 与临床文本挖掘工具
> 🔲 待补充：心理健康 AI Agent 与数字疗法
> 🔲 待补充：手术机器人与 AI 辅助手术规划
> 🔲 待补充：医疗知识图谱构建与推理 Agent
> 🔲 待补充：临床试验患者匹配 Agent
