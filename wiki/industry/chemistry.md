# 化学 AI Agent

> Sources: kb/industry/chemistry.md; 2026-06-12
> Raw: [chemistry](../../raw/industry/chemistry.md)

## 概述

> 行业分类: 化学 (Chemistry) | 更新时间: 2026-06-12

## 关键概念

- 1. 分子设计与药物发现 (Molecular Design & Drug Discovery)
- **定义**：AI Agent 辅助虚拟筛选、分子生成和 ADMET 性质预测
- **技术栈**：GNN、扩散模型、RDKit、分子对接、药效团模型
- 2. 反应预测与合成规划 (Reaction Prediction & Synthesis Planning)
- **定义**：AI Agent 预测化学反应结果、设计合成路线和优化反应条件
- **技术栈**：Transformer 反应预测、图卷积网络、逆合成分析、贝叶斯优化
- 3. 计算化学 (Computational Chemistry)
- **定义**：AI Agent 辅助 DFT 计算、分子动力学和量子化学模拟
- **技术栈**：PySCF、VASP、GROMACS、ASE、机器学习势函数
- 4. 化学信息学 (Cheminformatics)
- **定义**：AI Agent 管理化学数据库、分析结构-活性关系和化学命名
- **技术栈**：RDKit、Open Babel、化学 NLP、知识图谱
- 5. 实验室自动化 (Laboratory Automation)
- **定义**：AI Agent 驱动自动化实验平台和自驱动实验室
- **技术栈**：Opentrons、LabRobot、主动学习、贝叶斯实验设计

## 核心发现

- **[HICAI-ZJU/SciToolAgent](https://github.com/HICAI-ZJU/SciToolAgent)** (-⭐): 科学工具知识图谱驱动Agent，覆盖生物/化学/材料
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** (2.7k forks⭐): 138个科学技能，含化学信息学/药物发现10个技能
- **[JuDFTteam/best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning)** (-⭐): 510个原子级ML项目，250K stars汇总
- **[yuzhimanhua/Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models)** (-⭐): 科学领域预训练语言模型综述（含化学）
- **[blaiszik/awesome-matchem-datasets](https://github.com/blaiszik/awesome-matchem-datasets)** (-⭐): 材料/化学数据集精选
- **[Eipgen/Neural-Network-Models-for-Chemistry](https://github.com/Eipgen/Neural-Network-Models-for-Chemistry)** (-⭐): 化学神经网络模型集合
- **[deepmodeling/dpgen](https://github.com/deepmodeling/dpgen)** (-⭐): 深度势能生成器
- **[mir-group/flare](https://github.com/mir-group/flare)** (-⭐): 快速环境原子间势能
- **[sedaoturak/data-resources-for-materials-science](https://github.com/sedaoturak/data-resources-for-materials-science)** (-⭐): 材料科学数据资源
- **[labclaw/awesome-physical-ai-for-science](https://github.com/labclaw/awesome-physical-ai-for-science)** (-⭐): 物理AI for Science精选
- **[rxn4chemistry/rxn](https://github.com/rxn4chemistry/rxn)** (2k+⭐): IBM RXN for Chemistry，反应预测和逆合成分析
- **[MIT-COS/ASKCOS](https://github.com/MIT-COS/ASKCOS)** (1k+⭐): MIT 自驱动化学合成规划系统
- **[langgenius/dify](https://github.com/langgenius/dify)** (142k⭐): 低代码 Agent 平台
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** (138k⭐): Agent 框架
- **[microsoft/autogen](https://github.com/microsoft/autogen)** (58k⭐): 多 Agent 协作

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| - | [HICAI-ZJU/SciToolAgent](https://github.com/HICAI-ZJU/SciToolAgent) | Python | 科学工具知识图谱驱动Agent，覆盖生物/化学/材料 | 实验室自动化 |
| 2.7k forks | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 138个科学技能，含化学信息学/药物发现10个技能 | 分子设计 |
| - | [JuDFTteam/best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning) | YAML | 510个原子级ML项目，250K stars汇总 | 计算化学 |
| - | [yuzhimanhua/Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) | Markdown | 科学领域预训练语言模型综述（含化学） | 化学信息学 |
| - | [blaiszik/awesome-matchem-datasets](https://github.com/blaiszik/awesome-matchem-datasets) | Markdown | 材料/化学数据集精选 | 计算化学 |
| - | [Eipgen/Neural-Network-Models-for-Chemistry](https://github.com/Eipgen/Neural-Network-Models-for-Chemistry) | Python | 化学神经网络模型集合 | 分子设计 |
| - | [deepmodeling/dpgen](https://github.com/deepmodeling/dpgen) | Python | 深度势能生成器 | 计算化学 |
| - | [mir-group/flare](https://github.com/mir-group/flare) | Python | 快速环境原子间势能 | 计算化学 |
| - | [sedaoturak/data-resources-for-materials-science](https://github.com/sedaoturak/data-resources-for-materials-science) | Markdown | 材料科学数据资源 | 化学信息学 |
| - | [labclaw/awesome-physical-ai-for-science](https://github.com/labclaw/awesome-physical-ai-for-science) | Markdown | 物理AI for Science精选 | 实验室自动化 |

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 2k+ | [rxn4chemistry/rxn](https://github.com/rxn4chemistry/rxn) | Python | IBM RXN for Chemistry，反应预测和逆合成分析 | 反应预测 |
| 1k+ | [MIT-COS/ASKCOS](https://github.com/MIT-COS/ASKCOS) | Python | MIT 自驱动化学合成规划系统 | 反应预测 |

| Stars | 仓库 | 语言 | 描述 | 适用场景 |
|-------|------|------|------|----------|
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | TypeScript | 低代码 Agent 平台 | 化学信息学 |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | Agent 框架 | 全场景 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 多 Agent 协作 | 协同研发 |

| 类别 | 技术/工具 |
|------|-----------|
| 分子建模 | RDKit, Open Babel, Pybel, ChemAxon |
| 反应预测 | Transformer, GNN, Molecular Fingerprints |
| 量子化学 | PySCF, Psi4, ORCA, VASP |
| 分子动力学 | OpenMM, LAMMPS, GROMACS, ASE |
| 机器学习 | PyTorch, DeepChem, scikit-learn, JAX |
| 实验室自动化 | Opentrons, Chemotion, LabArchives |
| AI 框架 | LangChain, AutoGen, CrewAI |

## 实践指南

### 1. 分子设计与药物发现 (Molecular Design & Drug Discovery)
- **定义**：AI Agent 辅助虚拟筛选、分子生成和 ADMET 性质预测
- **技术栈**：GNN、扩散模型、RDKit、分子对接、药效团模型
- **代表工具**：DeepChem、Schrödinger、Atomwise、Insilico Medicine AI
### 2. 反应预测与合成规划 (Reaction Prediction & Synthesis Planning)
- **定义**：AI Agent 预测化学反应结果、设计合成路线和优化反应条件
- **技术栈**：Transformer 反应预测、图卷积网络、逆合成分析、贝叶斯优化
- **代表工具**：IBM RXN for Chemistry、ASKCOS (MIT)、Chemformer
### 3. 计算化学 (Computational Chemistry)
- **定义**：AI Agent 辅助 DFT 计算、分子动力学和量子化学模拟
- **技术栈**：PySCF、VASP、GROMACS、ASE、机器学习势函数
- **代表工具**：Materials Project、AFLOW、OQMD
### 4. 化学信息学 (Cheminformatics)
- **定义**：AI Agent 管理化学数据库、分析结构-活性关系和化学命名
- **技术栈**：RDKit、Open Babel、化学 NLP、知识图谱
- **代表工具**：ChEMBL、PubChem API、ChemSpider API
### 5. 实验室自动化 (Laboratory Automation)
- **定义**：AI Agent 驱动自动化实验平台和自驱动实验室
- **技术栈**：Opentrons、LabRobot、主动学习、贝叶斯实验设计
- **代表工具**：Chemotion ELN、LabArchives、Emerald Cloud Lab
### 6. 材料发现 (Materials Discovery)
- **定义**：AI Agent 加速新材料发现和性能优化
- **技术栈**：GNoME、MACE-MP、DFT+ML、高通量筛选
- **代表工具**：Materials Project、NOMAD、AFLOW

## Awesome Lists

- [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) (1.6k⭐) — AI for Science 综合
- [JuDFTteam/best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning) — 原子级 ML 项目排名
- [blaiszik/awesome-matchem-datasets](https://github.com/blaiszik/awesome-matchem-datasets) — 材料/化学数据集精选
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (23.1k⭐) — Agent 技能大全

## 扩展空间

> 🔲 待补充：化学合成规划 Agent（逆合成分析自动化）
> 🔲 待补充：分子动力学模拟 Agent（自动化工作流）
> 🔲 待补充：化学实验室自动化平台（自驱动实验室）
> 🔲 待补充：化学反应数据库 Agent（智能检索与推荐）
> 🔲 待补充：化学安全评估 Agent（GHS 分类、风险评估）
> 🔲 待补充：化学专利分析 Agent（FTO 分析、专利布局）
> 🔲 待补充：催化剂设计 Agent（高通量筛选、DFT 辅助）
> 🔲 待补充：高分子材料设计 Agent（聚合物性质预测）

## See Also

- [航空航天 AI Agent](../aerospace.md) — 相关行业 AI Agent 应用
- [农业 AI Agent](../agriculture.md) — 相关行业 AI Agent 应用
- [汽车 AI Agent](../automotive.md) — 相关行业 AI Agent 应用
- [生物学 AI Agent](../biology.md) — 相关行业 AI Agent 应用
- [化学工程 AI Agent](../chemical-engineering.md) — 相关行业 AI Agent 应用
- [Agent 框架](../../capability/agent-framework.md) — 行业 Agent 的底层框架
- [编码 Agent](../../capability/coding-agent.md) — AI 编程助手

## 来源

- kb/industry/chemistry.md

## 更新历史

- 2026-06-12 初始编译，从 kb/industry 提炼
