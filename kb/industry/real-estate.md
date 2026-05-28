# 房地产 AI Agent

> 行业分类: 房地产 (Real Estate / PropTech) | 更新时间: 2026-05-28

## 概述

AI Agent 在房地产领域的应用正在快速渗透，涵盖房产检测、估价分析、智能客服、物业管理、投资决策、数据抓取等多个方向。随着大语言模型（LLM）和多模态能力的成熟，房地产行业正经历从"信息化"到"智能化"的转型。Amazon Bedrowk、Azure 等云平台纷纷推出房地产行业专属 Agent 方案，Zillow 等传统巨头也在积极将 AI Agent 融入核心业务。

### 关键趋势
- **多 Agent 协作**：房产搜索、估价、法律审查等任务由多个专业 Agent 协同完成
- **多模态检测**：结合计算机视觉（CV）进行房屋损伤检测、虚拟看房
- **合规驱动**：美国《公平住房法》（Fair Housing Act）推动合规聊天机器人的研发
- **MCP 集成**：Model Context Protocol 成为连接房产数据源和 AI Agent 的标准协议
- **RAG + 本地知识库**：利用向量数据库（如 ChromaDB）构建区域化房产知识库

## 子分类

### 1. 房产检测与评估
- 基于计算机视觉的房屋损伤/异常检测
- 自动化房产检测报告生成
- 多模态（图像 + 文本）房产状况评估

### 2. 智能搜索与推荐
- 自然语言驱动的房产搜索
- 个性化房源推荐（基于用户偏好、预算、位置）
- 对话式房产导购助手

### 3. 投资分析与估值
- ML 驱动的房价预测（Zestimate 等）
- 多 Agent 投资分析系统
- 商业地产（CRE）承销与尽职调查

### 4. 智能客服与合规
- 7×24 小时房产咨询聊天机器人
- 合规性保障（反歧视、反引导）
- 租户/房东法律问题解答

### 5. 物业管理
- AI 驱动的物业维护工单管理
- 租户沟通自动化
- 房产数据提取与结构化

### 6. 数据抓取与市场分析
- 房产公开数据智能抓取（MCP + 爬虫）
- 市场趋势分析与报告生成
- 竞品定价与社区分析

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 | 子分类 |
|-------|------|------|------|--------|
| 142k | [langgenius/dify](https://github.com/langgenius/dify) | Python/TypeScript | 生产级 Agentic 工作流平台，支持 RAG、多模型Provider，广泛用于构建房产搜索和分析 Agent | 通用框架 |
| 138k | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | 最流行的 LLM Agent 开发框架，大量房产 Agent 项目基于此构建 | 通用框架 |
| 138k | [open-webui/open-webui](https://github.com/open-webui/open-webui) | Python/Svelte | 开源 AI 交互界面平台，可作为房产 Agent 的前端交互层 | 通用框架 |
| 127k | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Rust | Anthropic 的 AI 编码 Agent，支持 Skills 插件，ahacker-1/cre-agent-skills 等房地产 Skills 基于此运行 | 通用框架 |
| 111k | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 100+ AI Agent & RAG 应用模板，包含多个房产 Agent 参考实现 | 通用框架 |
| 77k | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | TypeScript | 开源多模型聊天框架，支持 Agent 插件，可用于构建房产咨询助手 | 通用框架 |
| 58k | [microsoft/autogen](https://github.com/microsoft/autogen) | Python | 微软多 Agent 协作框架，Azure-Samples 房产投资分析方案基于此 | 通用框架 |
| 53k | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | TypeScript | 低代码 Agent 构建平台，适合快速搭建房产搜索 Agent | 通用框架 |
| 52k | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 多 Agent 编排框架，Arindam200/awesome-ai-apps 中的 Car Finder Agent 使用 | 通用框架 |
| 30k | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | Jupyter Notebook | 500+ AI Agent 跨行业应用案例合集，含房地产方向 | 通用框架 |
| 23k | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Markdown | 精选 Agent Skills 集合，包含房地产领域 Skills | 通用框架 |
| - | [aws-samples/sample-amazon-bedrock-property-inspection-agent](https://github.com/aws-samples/sample-amazon-bedrock-property-inspection-agent) | Python | AWS 官方示例：基于 Amazon Bedrock 的房产异常检测 Agent，支持对话式深度分析 | 房产检测与评估 |
| - | [brightdata/real-estate-ai-agent](https://github.com/brightdata/real-estate-ai-agent) | Python | 基于 Bright Data MCP + Nebius Qwen LLM 的房产数据智能提取系统，输出结构化 JSON | 数据抓取与市场分析 |
| - | [zillow/compliant-real-estate-chatbot](https://github.com/zillow/compliant-real-estate-chatbot) | Python | Zillow 官方开源：基于 Llama3 8B 微调的合规房产聊天机器人，防止歧视性引导 | 智能客服与合规 |
| - | [Josephrp/EasyRealEstate](https://github.com/Josephrp/EasyRealEstate) | Python | 多 Agent 房产分析系统，专为意大利房产市场设计，支持编码辅助分析 | 投资分析与估值 |
| - | [ahacker-1/cre-agent-skills](https://github.com/ahacker-1/cre-agent-skills) | Markdown | 50+ 商业地产 AI Agent Skills，覆盖承销、尽职调查、融资、法律、交割全流程 | 投资分析与估值 |
| - | [AleksNeStu/ai-real-estate-assistant](https://github.com/AleksNeStu/ai-real-estate-assistant) | Python/TypeScript | 对话式房产搜索与分析平台，FastAPI + Next.js + ChromaDB 技术栈 | 智能搜索与推荐 |
| - | [Kaos599/PropertyLoop](https://github.com/Kaos599/PropertyLoop) | Python | 多 Agent 房产管理助手，支持房东/物业/租户三方，含图像分析、租赁法律、维护建议 | 物业管理 |
| - | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | Python | 80+ LLM 应用案例合集，含 Car Finder Agent 等可迁移至房产搜索场景 | 智能搜索与推荐 |
| - | [mallahyari/ml-practical-usecases](https://github.com/mallahyari/ml-practical-usecases) | Markdown | 650+ ML 系统设计案例，含 Zillow/StreetEasy 等房产 AI 实践 | 投资分析与估值 |
| 84 | [noahgift/real_estate_ml](https://github.com/noahgift/real_estate_ml) | Python | 房产估值机器学习实战，端到端 ML 工程教程 | 投资分析与估值 |

## Awesome Lists

- [etewiah/awesome-real-estate](https://github.com/etewiah/awesome-real-estate) - 房地产开源资源精选列表
- [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) - 500+ AI Agent 跨行业项目合集（含房地产）
- [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) - AI Agent 框架与工具大全
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - 开源 AI Agent 列表
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) - Agent Skills 精选集合
- [proptech (GitHub Topic)](https://github.com/topics/proptech) - GitHub 房地产科技主题页
- [real-estate-ai (GitHub Topic)](https://github.com/topics/real-estate-ai?l=python) - GitHub 房地产 AI 主题页

## 相关资源

- [HouseTour: A Virtual Real Estate A(I)gent](https://arxiv.org/abs/2510.18054) - ICCV 2025 论文，虚拟房产参观 Agent
- [Zillow Applied Science Research](https://github.com/zillow/as-research) - Zillow 应用科学研究（CV、NLP、推荐系统）
- [Zillow AI Journey - StreetEasy](https://www.zillow.com/tech/revolutionizing-the-real-estate-experience-with-llms-streeteasys-ai-journey/) - Zillow LLM 实践博客
- [Building an Intelligent Real Estate Investment Analyzer with AI Agents](https://dev.to/exploredataaiml/building-an-intelligent-real-estate-investment-analyzer-with-ai-agents-khi) - Dev.to 教程

## 扩展空间

> 🔲 待补充：更多房产检测与计算机视觉仓库
> 🔲 待补充：虚拟看房 / 3D 重建相关 Agent 项目
> 🔲 待补充：房产法律合规 Agent 工具（各国法规适配）
> 🔲 待补充：房产金融 / 贷款审批 Agent
> 🔲 待补充：中国/亚太市场房产 AI Agent 项目
> 🔲 待补充：房产数据标准与基准测试
> 🔲 待补充：PropTech 创业公司开源项目
