# Memory 层 — Agent 长期记忆系统

> Agent 记忆层、时序知识图谱、经验沉淀框架

更新时间: 2026-06-12

---

## 一、记忆层次模型

| 层次 | 名称 | 特点 | 类比 |
|------|------|------|------|
| L0 | Working Memory | 当前上下文窗口 | 大脑工作记忆 |
| L1 | Episodic Memory | 事件/会话记录 | 个人经历 |
| L2 | Semantic Memory | 结构化知识 | 百科全书 |
| L3 | Procedural Memory | 操作流程/技能 | 肌肉记忆 |
| L4 | Collective Memory | 多 Agent 共享知识 | 组织知识库 |

## 二、核心项目对比

### 通用记忆系统

#### [mem0ai/mem0](https://github.com/mem0ai/mem0) ⭐ 56,930
**定位**：Agent 长期记忆层
- **架构**：向量存储 + LLM 提取 + 图数据库
- **能力**：
  - 自动从对话中提取记忆
  - 语义搜索 + 向量检索
  - 记忆分类（用户偏好、事实、事件）
  - 多 Agent 共享记忆
- **存储后端**：Qdrant / Pinecone / Chroma / PGVector
- **集成**：LangChain, CrewAI, AutoGen
- **适用场景**：对话 Agent、客服、个人助理
- **Hub 集成度**：★★★★★（可直接接入 Oracle ARM 的 daos-pg + qdrant）

#### [getzep/graphiti](https://github.com/getzep/graphiti) ⭐ 26,682
**定位**：时序知识图谱
- **架构**：时序图 + LLM 实体提取 + 语义搜索
- **能力**：
  - 自动从文本提取实体和关系
  - 时序感知（知识随时间变化）
  - 矛盾检测（新旧知识冲突时标记）
  - 分层搜索（图遍历 + 语义）
- **存储后端**：Neo4j / FalkorDB
- **独特优势**：时序维度，知识有"有效期"
- **适用场景**：需要追踪知识演化的场景
- **Hub 集成度**：★★★★☆（需要 Neo4j）

#### [getzep/zep](https://github.com/getzep/zep) ⭐ 4,617
**定位**：知识图谱平台
- **架构**：图数据库 + 向量搜索 + LLM
- **能力**：
  - 知识图谱 CRUD
  - 语义搜索 + 图遍历
  - 文档自动索引
- **存储后端**：Neo4j
- **适用场景**：结构化知识管理
- **Hub 集成度**：★★★☆☆

#### [letta-ai/letta](https://github.com/letta-ai/letta) — MemGPT 继任者
**定位**：有状态的 Agent 记忆
- **架构**：分层记忆 + 自动管理 + 工具调用
- **能力**：
  - 无限上下文管理（自动分页）
  - 记忆内省（Agent 主动整理记忆）
  - 多用户/多 Agent
- **独特优势**：记忆管理作为 Agent 工具
- **Hub 集成度**：★★★★☆

### 轻量记忆

#### [langchain-ai/langmem](https://github.com/langchain-ai/langmem) ⭐ 1,473
**定位**：LangChain 记忆模块
- **能力**：对话摘要、实体记忆、向量检索
- **集成**：LangChain / LangGraph
- **适用场景**：LangChain 生态内记忆
- **Hub 集成度**：★★★☆☆

#### [letta-ai/letta](https://github.com/letta-ai/letta)
**定位**：MemGPT 继任者
- **能力**：无限上下文管理、记忆内省
- **Hub 集成度**：★★★★☆

## 三、记忆架构设计

### 单 Agent 记忆架构
```
对话 → 提取 → 分类 → 存储 → 检索 → 注入上下文
  ↓        ↓       ↓       ↓        ↓
原始文本  key    语义/   向量库   RAG
         事实/   时序/
         偏好    实体
```

### 多 Agent 共享记忆
```
Agent A ──→ 共享记忆层 ←── Agent B
  ↑           ↑            ↑
  └── 读取 ───┘── 写入 ────┘
         (向量DB + 知识图谱)
```

### 记忆生命周期管理
1. **创建**：从对话/文档中提取
2. **强化**：多次引用的记忆权重增加
3. **衰减**：长时间未使用的记忆权重降低
4. **合并**：相似记忆合并，减少冗余
5. **归档**：过期/低权重记忆归档存储

## 四、Hub 记忆层设计

### 存储方案
| 组件 | 技术 | 用途 |
|------|------|------|
| 向量存储 | Qdrant (已有) | 语义检索 |
| 图存储 | Neo4j 或 NetworkX | 知识图谱 |
| 关系存储 | PostgreSQL (已有) | 结构化记忆 |
| 缓存 | Redis (已有) | 热记忆缓存 |

### 记忆类型
1. **事实记忆**：行业知识、技术事实、最佳实践
2. **经验记忆**：操作经验、故障修复记录、踩坑日志
3. **偏好记忆**：用户偏好、配置偏好、工作流习惯
4. **关系记忆**：实体关系、项目依赖、人员关联

### 与 Hub 其他层的交互
```
Meta 层 ← 记忆 Schema 定义
  ↕
KB 层 ← 记忆内容检索
  ↕
Memory 层（本层）
  ↕
Platform 层 ← 存储和检索基础设施
```

## 五、选型建议

| 场景 | 推荐方案 | 理由 |
|------|----------|------|
| 个人 Agent 记忆 | mem0 + Qdrant | 开箱即用，Hub 已有基础设施 |
| 知识演化追踪 | Graphiti + Neo4j | 时序知识图谱独有能力 |
| 多 Agent 共享 | mem0 + Redis | 低延迟共享 |
| 轻量集成 | langmem | LangChain 生态最简单 |
| 知识库平台 | Zep | 完整图谱管理 |

## 六、集成方案：Hub + Hermes

### 当前 Hub 已有的记忆基础设施
- **Qdrant**：向量数据库（端口 6333）
- **PostgreSQL + pgvector**：关系存储 + 向量（端口 5433）
- **Redis**：缓存（端口 6379）
- **Embedding Server**：向量嵌入（端口 8000）

### 推荐集成路径
1. **Phase 1**：部署 mem0 → 连接 Qdrant + PostgreSQL
2. **Phase 2**：配置 Graphiti → 建立时序知识图谱
3. **Phase 3**：多 Agent 共享记忆 → Redis pub/sub + mem0
