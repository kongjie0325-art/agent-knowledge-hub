# Platform 层 — 知识库平台与工具

> 笔记应用、维基、文档管理、部署方案、工具链

更新时间: 2026-06-12

---

## 一、平台分类

### 本地优先（Local-First）
| 项目 | Stars | 语言 | 特点 | 部署方式 |
|------|-------|------|------|----------|
| [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium) | 36.2k | TS | 层级知识库、自托管、脚本化 | Docker |
| [obsidianmd/obsidian](https://github.com/obsidianmd/obsidian) | - | TS | 双向链接、插件生态、本地 Markdown | 桌面端 |
| [logseq/logseq](https://github.com/logseq/logseq) | 35k | Clojure | 开源 Obsidian 替代、大纲驱动 | Docker/桌面 |
| [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 71.4k | Dart | 开源 Notion 替代、Flutter | Docker/桌面 |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 68.8k | TS | 块编辑器 + 白板 + 数据库 | Docker/桌面 |

### 维基/文档
| 项目 | Stars | 语言 | 特点 | 部署方式 |
|------|-------|------|------|----------|
| [requarks/wiki](https://github.com/requarks/wiki) | 28.4k | Vue | Git 驱动、Markdown、权限 | Docker |
| [BookStackApp/BookStack](https://github.com/BookStackApp/BookStack) | 18.8k | PHP | 文档管理、书页结构 | Docker |
| [outline/outline](https://github.com/outline/outline) | 31.2k | TS | 团队知识库、Slack 集成 | Docker |

### 知识管理
| 项目 | Stars | 语言 | 特点 | 部署方式 |
|------|-------|------|------|----------|
| [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault) | 501 | TS | 本地优先知识保险库、Agent 友好 | npm |
| [axoviq-ai/synthadoc](https://github.com/axoviq-ai/synthadoc) | 301 | Python | 合成文档引擎、领域适配 | pip |
| [Yrzhe/pagefly](https://github.com/Yrzhe/pagefly) | 63 | Python | 页面级知识编译、Telegram Bot | Docker |

### 笔记同步
| 项目 | Stars | 语言 | 特点 | 部署方式 |
|------|-------|------|------|----------|
| [laurent22/joplin](https://github.com/laurent22/joplin) | 55k | TS | 端到端加密、多平台同步 | Docker/桌面 |
| [standardnotes/standardnotes](https://github.com/standardnotes/standardnotes) | 5.2k | TS | 加密笔记、扩展架构 | Docker |

## 二、选型矩阵

| 需求 | 推荐 | 理由 |
|------|------|------|
| 个人知识库 | Obsidian + Trilium | 层级结构 + 双向链接 |
| 团队协作 | Outline / Wiki.js | 权限管理 + 实时协作 |
| Agent 集成 | SwarmVault / Synthadoc | API 优先、结构化输出 |
| 离线优先 | Joplin / Logseq | 本地存储 + 可选同步 |
| 知识编译 | Pagefly + LLM Wiki | 自动化编译流程 |
| 大规模文档 | BookStack | 书页结构、搜索性能 |

## 三、Hub 推荐部署方案

### 方案 A：轻量级（适合个人）
```
Obsidian（本地编辑）
  ↓ 同步
Syncthing / OneDrive（已有）
  ↓ 发布
Wiki.js（Docker，只读镜像）
```

### 方案 B：Agent 原生（推荐）
```
Agent → KB 层（Markdown 文件）
  ↓ Embedding
Qdrant（已有）+ PostgreSQL（已有）
  ↓ 查询
mem0（记忆层）
  ↓ 前端
Trilium（自托管知识库）
```

### 方案 C：团队协作
```
Outline（Docker）
  ↓
PostgreSQL（已有）
  ↓
Agent 集成（MCP Server）
```

## 四、工具链

### 文档处理
| 工具 | 用途 | 优先级 |
|------|------|--------|
| Pandoc | 格式转换（PDF/HTML/Markdown） | P0 |
| Marker | PDF 转 Markdown | P1 |
| Tesseract | OCR | P2 |

### 搜索
| 工具 | 用途 | 优先级 |
|------|------|--------|
| SearXNG（已有） | 搜索引擎聚合 | P0 |
| Qdrant（已有） | 向量搜索 | P0 |
| Elasticsearch | 全文搜索 | P2 |

### 同步
| 工具 | 用途 | 优先级 |
|------|------|--------|
| Syncthing | P2P 文件同步 | P1 |
| rclone（已有） | 云存储同步 | P0 |
| Git | 版本控制 | P0 |

## 五、Hub 已有基础设施
| 组件 | 技术 | 端口 | 状态 |
|------|------|------|------|
| 向量数据库 | Qdrant | 6333 | ✅ 运行中 |
| 关系存储 | PostgreSQL + pgvector | 5433 | ✅ 运行中 |
| 缓存 | Redis | 6379 | ✅ 运行中 |
| 嵌入服务 | Embedding Server | 8000 | ✅ 运行中 |
| 搜索引擎 | SearXNG | 8888 | ✅ 运行中 |
| 监控 | Grafana | 3002 | ✅ 运行中 |
| 对象存储 | Cloudflare R2 | - | ✅ 配置中 |
