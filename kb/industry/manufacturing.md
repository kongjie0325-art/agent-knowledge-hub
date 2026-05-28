# 制造业 AI Agent

> 行业分类: 制造业 (Manufacturing) | 更新时间: 2026-05-28

## 概述

AI Agent 在制造业的应用正在推动第四次工业革命（工业 4.0）的深入发展，涵盖质量控制、供应链优化、预测性维护、生产调度、工艺优化、安全监控等多个核心方向。通过将大语言模型（LLM）与工业物联网（IoT）、数字孪生（Digital Twin）、机器人流程自动化（RPA）等技术深度融合，AI Agent 正在重塑制造业的运营模式。

制造业 AI Agent 的核心价值在于：
- **自主决策**：Agent 可根据实时传感器数据自动调整生产参数，减少人工干预
- **多 Agent 协作**：多个 Agent 协同完成从原材料采购到成品交付的全流程管理
- **知识沉淀**：将老师傅的经验编码为 Agent 可执行的知识库，解决制造业人才断层问题
- **弹性响应**：面对供应链中断、设备故障等突发事件，Agent 可快速重构生产计划

## 子分类

### 1. 质量控制与检测
- 基于计算机视觉的缺陷检测 Agent
- 统计过程控制（SPC）自动化
- 质量根因分析（RCA）Agent
- 多模态质检（视觉 + 声学 + 振动信号融合）

### 2. 预测性维护
- 设备健康状态实时监控与预警
- 基于振动、温度、声信号的故障预测
- 维护计划自动编排与备件库存联动
- 数字孪生驱动的设备寿命预测

### 3. 供应链优化
- 需求预测与智能补货 Agent
- 供应商风险评估与管理
- 物流路线优化与仓储调度
- 端到端供应链可视化与异常处理

### 4. 生产调度与排程
- 多约束条件下的生产排程优化
- 动态重调度（应对紧急插单、设备故障）
- 人机协作任务分配
- 能耗优化与绿色生产调度

### 5. 工艺优化与研发
- 产品参数自动调优（配方优化、工艺窗口探索）
- 新材料研发 Agent（分子模拟、性能预测）
- 制造执行系统（MES）Agent 化
- 工业知识图谱构建与推理

### 6. 安全监控与合规
- 工业环境安全监控 Agent
- 工人行为安全检测（PPE 佩戴、危险区域闯入）
- 环保排放监控与合规报告自动生成
- 工业网络安全威胁检测与响应

## 高引用仓库

### 制造业专属仓库

| Stars | 仓库 | 描述 | 子分类 |
|-------|------|------|--------|
| 87 | [ARUNAGIRINATHAN-K/awesome-ai-agents-2026](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026) | 2026 AI Agent 精选列表，含制造业分类，收录制造场景 Agent 资源 | 综合 |
| - | [mallahyari/ml-practical-usecases](https://github.com/mallahyari/ml-practical-usecases) | 650+ ML 系统设计案例，含制造业预测性维护、质量预测等场景 | 质量控制与检测 |
| - | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | 500+ AI Agent 项目集合，含制造业用例（缺陷检测、产线优化等） | 综合 |

### 通用 Agent 框架（适用于制造业）

| Stars | 仓库 | 描述 | 子分类 |
|-------|------|------|--------|
| 170k | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 通用 Agent 框架，支持多工具调用、技能系统，可用于构建制造流程 Agent | 综合 |
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | 低代码 Agent 平台，制造企业可快速构建质检、排程等场景 Agent | 综合 |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Agent 框架，可用于制造流程 Agent 编排（从原料到成品的全流程） | 生产调度与排程 |
| 138k | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 自托管 AI 界面，可用于制造监控大屏、车间操作终端 | 安全监控与合规 |
| 127k | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 代码生成 Agent，可用于制造软件（MES/SCADA/PLC 编程辅助） | 工艺优化与研发 |
| 75k | [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | 自主编程 Agent，可自动化制造系统开发与维护 | 工艺优化与研发 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | 多 Agent 协作框架，可用于生产线多工位协调、供应链多方协同 | 生产调度与排程 |
| 53k | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 低代码 Agent 构建工具，制造企业可无代码搭建质检、告警 Agent | 质量控制与检测 |
| 52k | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 多角色 Agent 框架，可用于制造团队管理（生产、品控、物流协同） | 供应链优化 |
| 23.1k | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Agent 技能大全，含工业场景可用的工具调用模板与最佳实践 | 综合 |

## Awesome Lists

- [ARUNAGIRINATHAN-K/awesome-ai-agents-2026](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026) - 2026 AI Agent 精选列表，含制造业分类
- [mallahyari/ml-practical-usecases](https://github.com/mallahyari/ml-practical-usecases) - 650+ ML 实践案例，覆盖制造场景
- [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) - 500+ AI Agent 项目，含大量制造用例
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) - Agent 技能大全

## 扩展空间

> 🔲 待补充：制造业专属 Agent 框架（如工业数字孪生 Agent、MES Agent）
> 🔲 待补充：行业数据集和基准（如缺陷检测数据集、设备故障预测基准）
> 🔲 待补充：行业合规工具（ISO 9001 质量管理、IATF 16949 汽车行业合规 Agent）
> 🔲 待补充：行业解决方案平台（西门子 MindSphere Agent、GE Predix Agent 集成）
> 🔲 待补充：边缘计算 Agent（工厂端侧部署的轻量级 Agent）
> 🔲 待补充：OPC UA / MQTT 等工业协议 Agent 集成方案
