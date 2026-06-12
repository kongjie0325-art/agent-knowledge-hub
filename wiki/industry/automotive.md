# 汽车 AI Agent

> Sources: kb/industry/automotive.md; 2026-06-12
> Raw: [automotive](../../raw/industry/automotive.md)

## 概述

> 行业分类: 汽车 (Automotive) | 更新时间: 2026-06-12

## 关键概念

- 1. 自动驾驶 (Autonomous Driving)
- **定义**：从 L2 辅助驾驶到 L4/L5 全自动驾驶的 AI 决策系统
- **技术栈**：BEV 感知、Transformer 多模态融合、端到端驾驶模型、强化学习
- 2. 智能座舱 (Smart Cockpit)
- **定义**：车载 AI Agent 实现自然的人机交互和个性化座舱体验
- **技术栈**：车载 LLM、语音识别 (ASR)、NLP、多模态融合、AR-HUD
- 3. 制造与供应链 (Manufacturing & Supply Chain)
- **定义**：AI Agent 优化整车制造流程和零部件供应链管理
- **技术栈**：数字孪生、预测性维护、多 Agent 协调、RPA
- 4. 售后与服务 (After-Sales & Service)
- **定义**：车辆智能诊断、预测性维护和客户服务自动化
- **技术栈**：OBD 数据分析、异常检测、LLM 对话系统、知识图谱
- 5. 车联网与 V2X (Connected Vehicle & V2X)
- **定义**：车辆与基础设施、其他车辆和行人的智能通信与协调
- **技术栈**：C-V2X、5G NR、边缘计算、联邦学习

## 核心发现

- **[commaai/openpilot](https://github.com/commaai/openpilot)** (-⭐): 开源自动驾驶系统，支持多品牌车型的辅助驾驶
- **[autowarefoundation/autoware](https://github.com/autowarefoundation/autoware)** (-⭐): Autoware 开源自动驾驶平台，支持 L4 级自动驾驶
- **[carla-simulator/carla](https://github.com/carla-simulator/carla)** (-⭐): CARLA 开源自动驾驶仿真平台，支持 Agent 训练与测试
- **[commaai/opendbc](https://github.com/commaai/opendbc)** (-⭐): 开放汽车 DBC 数据库，支持车辆通信协议解析
- **[NVIDIA-AI-IOT/CUDA-Agents](https://github.com/NVIDIA-AI-IOT/CUDA-Agents)** (15k⭐): NVIDIA CUDA 加速的 AI Agent 集合，含自动驾驶感知
- **[microsoft/airsim](https://github.com/microsoft/airsim)** (3.5k⭐): AirSim 高保真无人机和汽车仿真平台
- **[lgsvl/simulator](https://github.com/lgsvl/simulator)** (-⭐): LG SVL 自动驾驶仿真器，支持 ROS 集成
- **[langgenius/dify](https://github.com/langgenius/dify)** (142k⭐): 低代码 Agent 平台，可快速构建车载应用
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** (138k⭐): Agent 框架，支持多步骤推理
- **[microsoft/autogen](https://github.com/microsoft/autogen)** (58k⭐): 多 Agent 协作框架
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** (52k⭐): 多角色 Agent 框架

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| - | [commaai/openpilot](https://github.com/commaai/openpilot) | Python/C++ | 开源自动驾驶系统，支持多品牌车型的辅助驾驶 | 自动驾驶 |
| - | [autowarefoundation/autoware](https://github.com/autowarefoundation/autoware) | C++/Python | Autoware 开源自动驾驶平台，支持 L4 级自动驾驶 | 自动驾驶 |
| - | [carla-simulator/carla](https://github.com/carla-simulator/carla) | C++/Python | CARLA 开源自动驾驶仿真平台，支持 Agent 训练与测试 | 自动驾驶 |
| - | [commaai/opendbc](https://github.com/commaai/opendbc) | Python | 开放汽车 DBC 数据库，支持车辆通信协议解析 | 智能座舱 |
| 15k | [NVIDIA-AI-IOT/CUDA-Agents](https://github.com/NVIDIA-AI-IOT/CUDA-Agents) | Python | NVIDIA CUDA 加速的 AI Agent 集合，含自动驾驶感知 | 自动驾驶 |

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 3.5k | [microsoft/airsim](https://github.com/microsoft/airsim) | C++/Python | AirSim 高保真无人机和汽车仿真平台 | 自动驾驶 |
| - | [lgsvl/simulator](https://github.com/lgsvl/simulator) | C++ | LG SVL 自动驾驶仿真器，支持 ROS 集成 | 自动驾驶 |

| Stars | 仓库 | 语言 | 描述 | 适用场景 |
|-------|------|------|------|----------|
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | 低代码 Agent 平台，可快速构建车载应用 | 智能座舱 |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | Agent 框架，支持多步骤推理 | 全场景 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 多 Agent 协作框架 | 供应链 |
| 52k | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 多角色 Agent 框架 | 制造 |

| 类别 | 技术/工具 |
|------|-----------|
| 感知 | BEVFormer, YOLO, PointPillars, Occupancy Networks |
| 规划 | A*, RRT*, MPC, 强化学习 |
| 控制 | PID, MPC, 端到端驾驶 (NVIDIA PilotNet) |
| 仿真 | CARLA, AirSim, LGSVL, NVIDIA DRIVE Sim |
| 硬件 | NVIDIA DRIVE Orin/Thor, Qualcomm Snapdragon Ride, 地平线征程 |
| 通信 | C-V2X, 5G NR, MQTT, DDS |
| AI 框架 | PyTorch, TensorRT, ONNX Runtime, CUDA |

## 实践指南

### 1. 自动驾驶 (Autonomous Driving)
- **定义**：从 L2 辅助驾驶到 L4/L5 全自动驾驶的 AI 决策系统
- **技术栈**：BEV 感知、Transformer 多模态融合、端到端驾驶模型、强化学习
- **代表工具**：Tesla FSD、Waymo Driver、comma.ai openpilot、Autoware
### 2. 智能座舱 (Smart Cockpit)
- **定义**：车载 AI Agent 实现自然的人机交互和个性化座舱体验
- **技术栈**：车载 LLM、语音识别 (ASR)、NLP、多模态融合、AR-HUD
- **代表工具**：NVIDIA DRIVE Thor、高通 Snapdragon Ride、Cerence 语音助手
### 3. 制造与供应链 (Manufacturing & Supply Chain)
- **定义**：AI Agent 优化整车制造流程和零部件供应链管理
- **技术栈**：数字孪生、预测性维护、多 Agent 协调、RPA
- **代表工具**：Siemens Digital Twin、BMW AI 质检、Tesla 一体化压铸 AI
### 4. 售后与服务 (After-Sales & Service)
- **定义**：车辆智能诊断、预测性维护和客户服务自动化
- **技术栈**：OBD 数据分析、异常检测、LLM 对话系统、知识图谱
- **代表工具**：Bosch AI 诊断、Carfax AI 报告、4S 店智能客服
### 5. 车联网与 V2X (Connected Vehicle & V2X)
- **定义**：车辆与基础设施、其他车辆和行人的智能通信与协调
- **技术栈**：C-V2X、5G NR、边缘计算、联邦学习
- **代表工具**：Qualcomm V2X、华为 C-V2X、Autotalks 芯片
### 6. 汽车设计与研发 (Automotive Design & R&D)
- **定义**：AI 辅助车辆外观设计、空气动力学优化和虚拟碰撞测试
- **技术栈**：生成式 AI、CFD 仿真、参数化设计、NeRF 3D 建模
- **代表工具**：Autodesk VRED、Ansys Discovery、Car Design AI

## Awesome Lists

- [awesome-autonomous-driving](https://github.com/DeepakKumar14/awesome-autonomous-driving) — 自动驾驶综合资源
- [awesome-self-driving-car](https://github.com/daohu527/awesome-self-driving-car) — 自动驾驶开源项目精选
- [awesome-cars](https://github.com/seryl/awesome-cars) — 汽车技术资源列表

## 扩展空间

> 🔲 待补充：车载语音助手 Agent 框架（多语言、多轮对话）
> 🔲 待补充：电池管理系统 AI 优化（SOC/SOH 预测、充电策略）
> 🔲 待补充：汽车供应链 Agent 平台（零部件追踪、风险预警）
> 🔲 待补充：智能充电调度 Agent（V2G、峰谷电价优化）
> 🔲 待补充：汽车网络安全检测 Agent（入侵检测、OTA 安全）
> 🔲 待补充：座舱个性化推荐 Agent（音乐、导航、空调自动调节）
> 🔲 待补充：二手车 AI 评估 Agent（车况检测、残值预测）
> 🔲 待补充：共享出行调度 Agent（拼车路径优化、需求预测）

## See Also

- [航空航天 AI Agent](../aerospace.md) — 相关行业 AI Agent 应用
- [农业 AI Agent](../agriculture.md) — 相关行业 AI Agent 应用
- [生物学 AI Agent](../biology.md) — 相关行业 AI Agent 应用
- [化学工程 AI Agent](../chemical-engineering.md) — 相关行业 AI Agent 应用
- [化学 AI Agent](../chemistry.md) — 相关行业 AI Agent 应用
- [Agent 框架](../../capability/agent-framework.md) — 行业 Agent 的底层框架
- [编码 Agent](../../capability/coding-agent.md) — AI 编程助手

## 来源

- kb/industry/automotive.md

## 更新历史

- 2026-06-12 初始编译，从 kb/industry 提炼
