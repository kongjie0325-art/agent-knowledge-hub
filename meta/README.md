# Meta 层 — 元框架与知识管理方法论

> 知识管理 awesome 列表、分类体系、知识编译理论、认知框架

更新时间: 2026-06-12

---

## 一、知识管理成熟度模型

| 层级 | 名称 | 特征 | 典型工具 |
|------|------|------|----------|
| L0 | 文件管理 | 文件夹 + 搜索 | 文件系统、Everything |
| L1 | 笔记管理 | 个人知识卡片 | Notion、Obsidian、Logseq |
| L2 | 知识图谱 | 实体 + 关系 + 推理 | Neo4j、Trilium、Graphiti |
| L3 | 知识编译 | 原始资料 → 结构化知识 | Karpathy LLM Wiki、Synthadoc |
| L4 | Agent 维护知识库 | Agent 自动 ingest + compile + query | LLM Wiki + MCP + Memory |
| L5 | 集体智慧网络 | 多 Agent 协作知识构建 | 分布式知识图谱 + 联邦学习 |

## 二、知识编译（Knowledge Compilation）

### 核心概念
知识编译是将**原始资料（raw）**转化为**结构化、可查询、可复用的知识（wiki）**的过程。

```
原始资料 → 提取 → 结构化 → 交叉引用 → 知识文章
  ↓          ↓         ↓          ↓           ↓
 PDF/URL   关键发现   标准格式    相关链接    持久知识
```

### 编译原则
1. **不可变性**：原始资料只读，编译知识可更新
2. **归一化**：同一概念的多源信息合并到一篇文章
3. **交叉引用**：文章间建立 See Also 链接
4. **溯源性**：每个知识点标注来源
5. **时效性**：标注更新日期，过期内容标记

## 三、分类体系设计

### 双维度分类法
- **行业维度（Industry）**：按应用领域分类 → 回答"这个行业用什么 AI"
- **能力维度（Capability）**：按技术能力分类 → 回答"这个技术怎么用"

### 行业分类（36个）
healthcare, finance, legal, education, manufacturing, retail, marketing, sales, customer-service, security, agriculture, energy, government, research, real-estate, entertainment, logistics, human-resources, insurance, chemistry, biology, materials-science, environmental-science, computer-science, software-engineering, web-development, network-engineering, mechanical-engineering, electrical-engineering, chemical-engineering, civil-engineering, aerospace, automotive, food-beverage, textile-fashion, tourism-hospitality, sports-fitness, military-defense, mining-metallurgy, information-engineering, pharmaceutical

### 能力分类（10个）
agent-framework, agent-platform, coding-agent, inference, model, mcp, ui-frontend, awesome-list, cookbook, learning

## 四、知识图谱 Schema

### 实体类型
- **Concept**：核心概念（如"注意力机制"）
- **Tool**：工具/框架（如"LangGraph"）
- **Person**：关键人物（如"Karpathy"）
- **Paper**：论文/文章
- **Repo**：GitHub 仓库
- **Industry**：行业领域

### 关系类型
- `implements`：工具实现概念
- `extends`：扩展关系
- `cites`：引用关系
- `belongs_to`：属于某行业/能力
- `related_to`：相关概念
- `contradicts`：矛盾/争议

## 五、知识管理 Awesome 列表

### 核心项目
| 项目 | Stars | 定位 | 优先级 |
|------|-------|------|--------|
| [brettkromkamp/awesome-knowledge-management](https://github.com/brettkromkamp/awesome-knowledge-management) | - | 知识管理总目录 | P0 |
| [junegunn/fzf](https://github.com/junegunn/fzf) | 67k | 模糊搜索 | P0 |
| [yappie/search-engine](https://github.com/yappie/search-engine) | - | 搜索引擎集合 | P1 |

### 知识图谱
| 项目 | Stars | 定位 | 优先级 |
|------|-------|------|--------|
| [getzep/graphiti](https://github.com/getzep/graphiti) | 26.7k | 时序知识图谱 | P0 |
| [getzep/zep](https://github.com/getzep/zep) | 4.6k | 知识图谱平台 | P0 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 33.2k | 知识图谱构建 | P0 |
| [neo4j/neo4j](https://github.com/neo4j/neo4j) | - | 图数据库 | P1 |

### 知识编译
| 项目 | Stars | 定位 | 优先级 |
|------|-------|------|--------|
| [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 932 | LLM Wiki 框架 | P0 |
| [Yrzhe/pagefly](https://github.com/Yrzhe/pagefly) | 63 | 页面级知识编译 | P0 |
| [axoviq-ai/synthadoc](https://github.com/axoviq-ai/synthadoc) | 301 | 合成文档引擎 | P0 |
| [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault) | 501 | 本地优先知识保险库 | P0 |

## 六、认知框架：如何组织 Agent 知识

### 三层架构（Hub 核心设计）
```
Meta 层（元框架）     ← 分类体系、方法论、Schema
  ↕
KB 层（知识库）       ← 按行业/能力分类的编译知识
  ↕
Memory 层（记忆）     ← Agent 运行时记忆、经验沉淀
  ↕
Platform 层（平台）   ← 存储、搜索、部署工具
```

### 知识生命周期
1. **采集（Ingest）**：从 URL/PDF/文本获取原始资料
2. **编译（Compile）**：提取关键信息，结构化存储
3. **关联（Link）**：交叉引用，建立知识图谱关系
4. **查询（Query）**：Agent 按需检索，带引用回答
5. **更新（Update）**：新信息到来时合并/修正
6. **淘汰（Archive）**：过期知识归档，不删除

## 七、参考资料
- [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [知识管理 Wikipedia](https://en.wikipedia.org/wiki/Knowledge_management)
- [Zettelkasten 方法](https://en.wikipedia.org/wiki/Zettelkasten)
- [Second Brain 方法论](https://fortelabs.com/blog/second-brain/)
