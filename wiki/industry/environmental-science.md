# 环境科学 AI Agent

> Sources: kb/industry/environmental-science.md; 2026-06-12
> Raw: [environmental-science](../../raw/industry/environmental-science.md)

## 概述

> 行业分类: 环境科学 (Environmental Science) | 更新时间: 2026-06-12

## 关键概念

- 1. 气候与气象
- 气候模型分析、天气预报辅助、气候变化影响评估
- 关键技术栈：数值天气预报
- 2. 污染监测
- 空气质量监测、水质检测分析、土壤污染评估
- 关键技术栈：遥感图像分析、时序预测、IoT 传感器网络
- 3. 生态保护
- 生物多样性监测、栖息地评估、入侵物种检测
- 关键技术栈：计算机视觉
- 4. 可持续发展
- 碳排放追踪、可再生能源优化、环境影响评估
- 关键技术栈：LCA 分析、能源系统优化、碳核算模型
- 5. 地理空间分析
- GIS 数据处理、空间建模、土地利用变化检测
- 关键技术栈：GeoPandas、Rasterio、Google Earth Engine、PostGIS

## 核心发现

- **[ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science)** (-⭐): AI for Science 综合列表（含环境科学）
- **[labclaw/awesome-physical-ai-for-science](https://github.com/labclaw/awesome-physical-ai-for-science)** (-⭐): 物理 AI for Science 精选
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** (-⭐): 138个科学技能（含地理空间科学）
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** (138k⭐): Agent 框架，可用于构建环境分析 Agent
- **[langgenius/dify](https://github.com/langgenius/dify)** (142k⭐): 低代码 Agent 平台，可快速构建环境监测 Agent
- **[microsoft/autogen](https://github.com/microsoft/autogen)** (58k⭐): 多 Agent 协作，适合多源数据融合场景
- **[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** (23.1k⭐): 1000+ Agent 技能，含环境相关技能

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| - | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | Markdown | AI for Science 综合列表（含环境科学） | 气候与气象 |
| - | [labclaw/awesome-physical-ai-for-science](https://github.com/labclaw/awesome-physical-ai-for-science) | Markdown | 物理 AI for Science 精选 | 气候与气象 |
| - | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 138个科学技能（含地理空间科学） | 地理空间分析 |

| Stars | 仓库 | 语言 | 描述 | 适用场景 |
|-------|------|------|------|----------|
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | Agent 框架，可用于构建环境分析 Agent | 通用 |
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | 低代码 Agent 平台，可快速构建环境监测 Agent | 通用 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 多 Agent 协作，适合多源数据融合场景 | 气候与气象 |
| 23.1k | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Markdown | 1000+ Agent 技能，含环境相关技能 | 通用 |

## 实践指南

### 1. 气候与气象
- 气候模型分析、天气预报辅助、气候变化影响评估
- 关键技术栈：数值天气预报（WRF）、地球系统模型（CESM）、Transformer 气象模型
- 代表性工具：NVIDIA Earth-2、GraphCast、Pangu-Weather、ClimaX
### 2. 污染监测
- 空气质量监测、水质检测分析、土壤污染评估
- 关键技术栈：遥感图像分析、时序预测、IoT 传感器网络
- 代表性工具：OpenAQ API、Google Earth Engine、Sentinel Hub
### 3. 生态保护
- 生物多样性监测、栖息地评估、入侵物种检测
- 关键技术栈：计算机视觉（物种识别）、声学 AI、eDNA 分析
- 代表性工具：Wildlife Insights、iNaturalist API、BirdNET
### 4. 可持续发展
- 碳排放追踪、可再生能源优化、环境影响评估
- 关键技术栈：LCA 分析、能源系统优化、碳核算模型
- 代表性工具：WattTime API、Electricity Maps、OpenLCA
### 5. 地理空间分析
- GIS 数据处理、空间建模、土地利用变化检测
- 关键技术栈：GeoPandas、Rasterio、Google Earth Engine、PostGIS
- 代表性工具：QGIS、ArcGIS API、Planetary Computer
### 6. 自然灾害预警
- 洪水、地震、台风、森林火灾等灾害的预测和预警
- 关键技术栈：时空预测模型、异常检测、多源数据融合
- 代表性工具：USGS Earthquake API、GDACS、FIRMS 火灾监测

## Awesome Lists

- [awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) (1.6k⭐) - AI for Science 综合（含环境科学）
- [awesome-physical-ai-for-science](https://github.com/labclaw/awesome-physical-ai-for-science) - 物理 AI for Science 精选
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (23.1k⭐) - Agent 技能大全

## 扩展空间

> 🔲 待补充：气候建模 Agent（集成 WRF/CESM）
> 🔲 待补充：空气质量监测 Agent（集成 OpenAQ）
> 🔲 待补充：水质分析 Agent（集成 USGS Water Services）
> 🔲 待补充：生态监测 Agent（集成 iNaturalist/Wildlife Insights）
> 🔲 待补充：碳排放追踪 Agent（集成 WattTime/Electricity Maps）
> 🔲 待补充：自然灾害预警 Agent
> 🔲 待补充：环境法规合规 Agent

## See Also

- [航空航天 AI Agent](../aerospace.md) — 相关行业 AI Agent 应用
- [农业 AI Agent](../agriculture.md) — 相关行业 AI Agent 应用
- [汽车 AI Agent](../automotive.md) — 相关行业 AI Agent 应用
- [生物学 AI Agent](../biology.md) — 相关行业 AI Agent 应用
- [化学工程 AI Agent](../chemical-engineering.md) — 相关行业 AI Agent 应用
- [Agent 框架](../../capability/agent-framework.md) — 行业 Agent 的底层框架
- [编码 Agent](../../capability/coding-agent.md) — AI 编程助手

## 来源

- kb/industry/environmental-science.md

## 更新历史

- 2026-06-12 初始编译，从 kb/industry 提炼
