# 土木工程/建筑 AI Agent

> Sources: kb/industry/civil-engineering.md; 2026-06-12
> Raw: [civil-engineering](../../raw/industry/civil-engineering.md)

## 概述

> 行业分类: 土木工程/建筑 (Civil Engineering & Construction) | 更新时间: 2026-06-12

## 关键概念

- 1. 结构设计与分析 (Structural Design & Analysis)
- **定义**：AI Agent 辅助结构优化设计、有限元分析和 BIM 模型生成
- **技术栈**：ETABS、SAP2000、ANSYS、Revit API、生成式设计
- 2. 施工管理 (Construction Management)
- **定义**：AI Agent 优化施工进度、资源调度和现场安全管理
- **技术栈**：4D BIM、关键路径法 (CPM)、多 Agent 仿真、无人机监测
- 3. 质量检测与验收 (Quality Inspection & Acceptance)
- **定义**：AI Agent 自动化建筑缺陷检测、结构健康监测和验收报告生成
- **技术栈**：计算机视觉 (YOLO、Mask R-CNN)、点云处理、IoT 传感器
- 4. 成本与项目管理 (Cost & Project Management)
- **定义**：AI Agent 自动化工程量计算、造价估算和合同管理
- **技术栈**：BIM 5D、RPA、NLP 合同分析、预测建模
- 5. 基础设施运维 (Infrastructure O&M)
- **定义**：AI Agent 驱动桥梁、隧道、道路等基础设施的监测和养护
- **技术栈**：数字孪生、IoT 监测、预测性维护、GIS

## 核心发现

- **[garystafford/general-contractor-agent-demo](https://github.com/garystafford/general-contractor-agent-demo)** (-⭐): 总承包商 AI Agent 演示，展示施工项目管理自动化
- **[aws-samples/sample-amazon-bedrock-property-inspection-agent](https://github.com/aws-samples/sample-amazon-bedrock-property-inspection-agent)** (-⭐): 基于 Amazon Bedrock 的物业检测 Agent，自动化建筑质量检查
- **[tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents)** (-⭐): 含 EngiAI 多 Agent 工程设计框架，支持协同工程分析与设计
- **[Autodesk/revit-api](https://github.com/Autodesk/revit-api)** (3k+⭐): Revit API 开发资源，支持 BIM 自动化
- **[Bentley/iModel.js](https://github.com/Bentley/iModel.js)** (1k+⭐): Bentley iModel.js 开源 BIM 平台
- **[langgenius/dify](https://github.com/langgenius/dify)** (142k⭐): 低代码 Agent 平台
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** (138k⭐): Agent 框架
- **[microsoft/autogen](https://github.com/microsoft/autogen)** (58k⭐): 多 Agent 协作

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| - | [garystafford/general-contractor-agent-demo](https://github.com/garystafford/general-contractor-agent-demo) | - | 总承包商 AI Agent 演示，展示施工项目管理自动化 | 施工管理 |
| - | [aws-samples/sample-amazon-bedrock-property-inspection-agent](https://github.com/aws-samples/sample-amazon-bedrock-property-inspection-agent) | - | 基于 Amazon Bedrock 的物业检测 Agent，自动化建筑质量检查 | 质量检测与验收 |
| - | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | - | 含 EngiAI 多 Agent 工程设计框架，支持协同工程分析与设计 | 结构设计与分析 |

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 3k+ | [Autodesk/revit-api](https://github.com/Autodesk/revit-api) | C# | Revit API 开发资源，支持 BIM 自动化 | 结构设计与分析 |
| 1k+ | [Bentley/iModel.js](https://github.com/Bentley/iModel.js) | TypeScript | Bentley iModel.js 开源 BIM 平台 | 结构设计与分析 |

| Stars | 仓库 | 语言 | 描述 | 适用场景 |
|-------|------|------|------|----------|
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | 低代码 Agent 平台 | 项目管理 |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | Agent 框架 | 全场景 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 多 Agent 协作 | 协同设计 |

| 类别 | 技术/工具 |
|------|-----------|
| 结构设计 | ETABS, SAP2000, STAAD.Pro, ANSYS |
| BIM | Revit, ArchiCAD, Tekla Structures, iModel.js |
| 施工管理 | Procore, Autodesk Construction Cloud, Primavera P6 |
| 计算机视觉 | OpenCV, YOLO, Mask R-CNN, PCL |
| 有限元分析 | Abaqus, ANSYS, COMSOL, OpenSees |
| 能耗模拟 | EnergyPlus, OpenStudio, TRNSYS |
| AI 框架 | PyTorch, TensorFlow, LangChain |

## 实践指南

### 1. 结构设计与分析 (Structural Design & Analysis)
- **定义**：AI Agent 辅助结构优化设计、有限元分析和 BIM 模型生成
- **技术栈**：ETABS、SAP2000、ANSYS、Revit API、生成式设计
- **代表工具**：Autodesk Generative Design、Trimble Tekla、Bentley Systems AI
### 2. 施工管理 (Construction Management)
- **定义**：AI Agent 优化施工进度、资源调度和现场安全管理
- **技术栈**：4D BIM、关键路径法 (CPM)、多 Agent 仿真、无人机监测
- **代表工具**：Procore AI、Autodesk Construction Cloud、Buildots
### 3. 质量检测与验收 (Quality Inspection & Acceptance)
- **定义**：AI Agent 自动化建筑缺陷检测、结构健康监测和验收报告生成
- **技术栈**：计算机视觉 (YOLO、Mask R-CNN)、点云处理、IoT 传感器
- **代表工具**：OpenCV、PCL、AWS Panorama、Smartvid.io
### 4. 成本与项目管理 (Cost & Project Management)
- **定义**：AI Agent 自动化工程量计算、造价估算和合同管理
- **技术栈**：BIM 5D、RPA、NLP 合同分析、预测建模
- **代表工具**：CostX、Bluebeam、PlanGrid AI
### 5. 基础设施运维 (Infrastructure O&M)
- **定义**：AI Agent 驱动桥梁、隧道、道路等基础设施的监测和养护
- **技术栈**：数字孪生、IoT 监测、预测性维护、GIS
- **代表工具**：Bentley iTwin、Trimble Asset Management
### 6. 绿色建筑与可持续建造 (Green & Sustainable Construction)
- **定义**：AI Agent 优化建筑能效、碳排放和可持续材料选择
- **技术栈**：能耗模拟、LCA 分析、碳足迹计算、绿色认证
- **代表工具**：EnergyPlus、OpenStudio、One Click LCA

## Awesome Lists

- [awesome-civil-engineering](https://github.com/kaustubh-sadekar/awesome-civil-engineering) — 土木工程综合资源
- [awesome-bim](https://github.com/andrewparker/awesome-bim) — BIM 技术资源精选
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (23.1k⭐) — Agent 技能大全

## 扩展空间

> 🔲 待补充：BIM 与 AI Agent 集成工具（自动化模型检查、碰撞检测）
> 🔲 待补充：结构健康监测 Agent 平台（桥梁、隧道实时监测）
> 🔲 待补充：施工安全智能预警系统（危险行为识别、安全帽检测）
> 🔲 待补充：绿色建筑评估 AI 工具（LEED/BREEAM 自动评分）
> 🔲 待补充：土木工程规范自动审查 Agent（规范条文智能匹配）
> 🔲 待补充：3D 打印建筑 Agent（路径规划、材料优化）
> 🔲 待补充：智能建造机器人控制 Agent（砌墙、焊接、喷涂）
> 🔲 待补充：基础设施数字孪生 Agent（全生命周期管理）

## See Also

- [航空航天 AI Agent](../aerospace.md) — 相关行业 AI Agent 应用
- [农业 AI Agent](../agriculture.md) — 相关行业 AI Agent 应用
- [汽车 AI Agent](../automotive.md) — 相关行业 AI Agent 应用
- [生物学 AI Agent](../biology.md) — 相关行业 AI Agent 应用
- [化学工程 AI Agent](../chemical-engineering.md) — 相关行业 AI Agent 应用
- [Agent 框架](../../capability/agent-framework.md) — 行业 Agent 的底层框架
- [编码 Agent](../../capability/coding-agent.md) — AI 编程助手

## 来源

- kb/industry/civil-engineering.md

## 更新历史

- 2026-06-12 初始编译，从 kb/industry 提炼
