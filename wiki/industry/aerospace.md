# 航空航天 AI Agent

> Sources: kb/industry/aerospace.md; 2026-06-12
> Raw: [aerospace](../../raw/industry/aerospace.md)

## 概述

> 行业分类: 航空航天 (Aerospace) | 更新时间: 2026-06-12

## 关键概念

- 1. 飞行器设计 (Aircraft Design)
- **定义**：利用 AI Agent 辅助气动外形优化、结构轻量化和推进系统设计
- **技术栈**：OpenMDAO、ANSYS、CFD 仿真、强化学习、生成式设计
- 2. 任务规划与导航 (Mission Planning & Navigation)
- **定义**：自主规划飞行轨道、航线和导航决策，适应动态环境约束
- **技术栈**：A* / RRT* 路径规划、强化学习、SLAM、星敏感器数据处理
- 3. 飞行控制与运营 (Flight Control & Operations)
- **定义**：实时飞行控制、空中交通管理和卫星星座自主运营
- **技术栈**：PID 控制、模型预测控制 (MCP)、多 Agent 协调、RTOS
- 4. 测试与验证 (Testing & Validation)
- **定义**：通过仿真和故障注入测试验证 Agent 系统的安全性和可靠性
- **技术栈**：硬件在环 (HIL) 仿真、故障树分析 (FTA)、形式化验证
- 5. 卫星与航天器自主操作 (Spacecraft Autonomy)
- **定义**：深空探测器和在轨卫星的自主决策与故障恢复
- **技术栈**：约束规划、自主调度、星载 AI 推理

## 核心发现

- **[tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents)** (-⭐): 多 Agent 框架，可适配航空航天协同设计场景
- **[nasa/fprime](https://github.com/nasa/fprime)** (-⭐): NASA F' 飞行软件框架，适用于航天器嵌入式系统
- **[PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot)** (-⭐): PX4 开源自动驾驶仪，支持无人机自主飞行控制
- **[ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot)** (-⭐): ArduPilot 开源自动驾驶平台，支持多旋翼/固定翼/无人车
- **[OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO)** (-⭐): NASA 开源多学科设计优化框架，支持飞行器设计优化
- **[jsbsim-team/jsbsim](https://github.com/jsbsim-team/jsbsim)** (1.5k⭐): JSBSim 开源飞行动力学模型，支持飞行器仿真
- **[gazebo-fortress/gazebo](https://github.com/gazebo-fortress/gazebo)** (1.2k⭐): Gazebo 高保真物理仿真，支持无人机和航天器仿真
- **[nasa/GMAT](https://github.com/nasa/GMAT)** (-⭐): NASA 通用任务分析工具，支持轨道力学仿真
- **[langgenius/dify](https://github.com/langgenius/dify)** (142k⭐): 低代码 Agent 平台，可快速构建航空工作流
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** (138k⭐): Agent 框架，支持多步骤推理
- **[microsoft/autogen](https://github.com/microsoft/autogen)** (58k⭐): 多 Agent 协作框架
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** (52k⭐): 多角色 Agent 框架

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| - | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | - | 多 Agent 框架，可适配航空航天协同设计场景 | 飞行器设计 |
| - | [nasa/fprime](https://github.com/nasa/fprime) | C++ | NASA F' 飞行软件框架，适用于航天器嵌入式系统 | 飞行控制与运营 |
| - | [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot) | C/C++ | PX4 开源自动驾驶仪，支持无人机自主飞行控制 | 飞行控制与运营 |
| - | [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | C/C++ | ArduPilot 开源自动驾驶平台，支持多旋翼/固定翼/无人车 | 飞行控制与运营 |
| - | [OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) | Python | NASA 开源多学科设计优化框架，支持飞行器设计优化 | 飞行器设计 |

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 1.5k | [jsbsim-team/jsbsim](https://github.com/jsbsim-team/jsbsim) | C++ | JSBSim 开源飞行动力学模型，支持飞行器仿真 | 测试与验证 |
| 1.2k | [gazebo-fortress/gazebo](https://github.com/gazebo-fortress/gazebo) | C++ | Gazebo 高保真物理仿真，支持无人机和航天器仿真 | 测试与验证 |
| - | [nasa/GMAT](https://github.com/nasa/GMAT) | C++ | NASA 通用任务分析工具，支持轨道力学仿真 | 任务规划与导航 |

| Stars | 仓库 | 语言 | 描述 | 适用场景 |
|-------|------|------|------|----------|
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | 低代码 Agent 平台，可快速构建航空工作流 | 运营 |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | Agent 框架，支持多步骤推理 | 全场景 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 多 Agent 协作框架 | 集群协调 |
| 52k | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 多角色 Agent 框架 | 协同设计 |

| 类别 | 技术/工具 |
|------|-----------|
| 飞行动力学仿真 | JSBSim, Gazebo, Simulink, STK |
| 多学科优化 | OpenMDAO, ANSYS, COMSOL |
| 自主控制 | PX4, ArduPilot, ROS2, MAVSDK |
| 路径规划 | OMPL, SBPL, A*, RRT* |
| 形式化验证 | SPIN, UPPAAL, Coq |
| 星载计算 | NVIDIA Jetson (边缘推理), RTEMS, VxWorks |
| AI 框架 | PyTorch, TensorFlow, ONNX Runtime |

## 实践指南

### 1. 飞行器设计 (Aircraft Design)
- **定义**：利用 AI Agent 辅助气动外形优化、结构轻量化和推进系统设计
- **技术栈**：OpenMDAO、ANSYS、CFD 仿真、强化学习、生成式设计
- **代表工具**：OpenMDAO (NASA)、Autodesk Generative Design、Airbus AI 设计助手
### 2. 任务规划与导航 (Mission Planning & Navigation)
- **定义**：自主规划飞行轨道、航线和导航决策，适应动态环境约束
- **技术栈**：A* / RRT* 路径规划、强化学习、SLAM、星敏感器数据处理
- **代表工具**：NASA GMAT、STK (Systems Tool Kit)、ROS 导航栈
### 3. 飞行控制与运营 (Flight Control & Operations)
- **定义**：实时飞行控制、空中交通管理和卫星星座自主运营
- **技术栈**：PID 控制、模型预测控制 (MCP)、多 Agent 协调、RTOS
- **代表工具**：PX4 Autopilot、ArduPilot、NASA F' Flight Software
### 4. 测试与验证 (Testing & Validation)
- **定义**：通过仿真和故障注入测试验证 Agent 系统的安全性和可靠性
- **技术栈**：硬件在环 (HIL) 仿真、故障树分析 (FTA)、形式化验证
- **代表工具**：Gazebo、JSBSim、NASA V&V 工具链
### 5. 卫星与航天器自主操作 (Spacecraft Autonomy)
- **定义**：深空探测器和在轨卫星的自主决策与故障恢复
- **技术栈**：约束规划、自主调度、星载 AI 推理
- **代表工具**：NASA APGen、ESA 自主导航系统、Deep Space Network AI
### 6. 无人机集群与 UAM (Drone Swarms & Urban Air Mobility)
- **定义**：多无人机协同作业和城市空中交通管理
- **技术栈**：多 Agent 强化学习、共识算法、4D 航迹规划
- **代表工具**：AirSim、PX4 Swarm、NASA UAM 研究平台

## Awesome Lists

- [ReducedBasis/awesome-space-ai](https://github.com/ReducedBasis/awesome-space-ai) — (如有) 太空 AI 资源精选
- [nasa/fprime](https://github.com/nasa/fprime) — NASA 开源飞行软件生态
- [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot) — 开源无人机生态

## 扩展空间

> 🔲 待补充：卫星任务规划 Agent 平台
> 🔲 待补充：空域管理 AI 系统（UTM）
> 🔲 待补充：飞行器健康监测与预测性维护 Agent
> 🔲 待补充：航空发动机数字孪生与 AI 优化
> 🔲 待补充：航天器自主故障诊断系统
> 🔲 待补充：eVTOL 城市空中交通管理 Agent
> 🔲 待补充：航空航天适航认证 AI 辅助工具
> 🔲 待补充：太空碎片规避决策 Agent

## See Also

- [农业 AI Agent](../agriculture.md) — 相关行业 AI Agent 应用
- [汽车 AI Agent](../automotive.md) — 相关行业 AI Agent 应用
- [生物学 AI Agent](../biology.md) — 相关行业 AI Agent 应用
- [化学工程 AI Agent](../chemical-engineering.md) — 相关行业 AI Agent 应用
- [化学 AI Agent](../chemistry.md) — 相关行业 AI Agent 应用
- [Agent 框架](../../capability/agent-framework.md) — 行业 Agent 的底层框架
- [编码 Agent](../../capability/coding-agent.md) — AI 编程助手

## 来源

- kb/industry/aerospace.md

## 更新历史

- 2026-06-12 初始编译，从 kb/industry 提炼
