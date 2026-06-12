# Agent Knowledge Hub

> 基于 Karpathy LLM Wiki / 知识编译路线的 Agent 优先知识库。
> 四层架构：Meta（元框架）→ KB（知识库）→ Memory（记忆）→ Platform（平台）。

## 架构

```
agent-knowledge-hub/
├── meta/           ← 元框架：分类体系、方法论、知识编译理论
├── kb/             ← 知识库：按行业(36) × 能力(10) 分类的深度知识
├── memory/         ← 记忆层：Agent 记忆系统、时序知识图谱
├── platform/       ← 平台层：知识库工具、部署方案、基础设施
├── raw/            ← 原始资料索引（Karpathy Wiki 架构）
├── wiki/           ← 编译知识文章（kb/ 的结构化编译版本）
│   ├── index.md    ← 全局索引
│   ├── log.md      ← 操作日志
│   ├── industry/   ← 36篇行业编译文章
│   └── capability/  ← 10篇能力域编译文章
├── references/     ← Karpathy Wiki 模板
├── examples/       ← 示例文章
├── api/            ← Hermes 可查询的 JSON 索引
├── data/           ← 结构化数据（47+ GitHub 仓库）
└── scripts/        ← 自动化脚本
```

## 四层架构

| 层 | 目录 | 内容 | 回答的问题 |
|----|------|------|-----------|
| **Meta** | `meta/` | 知识管理方法论、分类体系、知识图谱 Schema | "怎么组织知识？" |
| **KB** | `kb/` | 36个行业 + 10个能力域的知识编译 | "这个行业/技术用什么 AI？" |
| **Memory** | `memory/` | Agent 记忆系统对比、时序知识图谱方案 | "Agent 怎么记住知识？" |
| **Platform** | `platform/` | 知识库平台对比、部署方案、工具链 | "用什么工具管理知识？" |

## Karpathy LLM Wiki 工作流

基于 [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) 的核心理念：

1. **Ingest**：采集原始资料 → 存入 `raw/`
2. **Compile**：编译为结构化知识 → 存入 `wiki/`
3. **Query**：Agent 查询 wiki/，带引用回答
4. **Lint**：检查索引完整性、交叉引用

详细工作流见 [SKILL.md](SKILL.md)。

## 行业分类（36个）

healthcare, finance, legal, education, manufacturing, retail, marketing, sales, customer-service, security, agriculture, energy, government, research, real-estate, entertainment, logistics, human-resources, insurance, chemistry, biology, materials-science, environmental-science, computer-science, software-engineering, web-development, network-engineering, mechanical-engineering, electrical-engineering, chemical-engineering, civil-engineering, aerospace, automotive, food-beverage, textile-fashion, tourism-hospitality, sports-fitness, military-defense, mining-metallurgy, information-engineering, pharmaceutical

## 能力分类（10个）

agent-framework, agent-platform, coding-agent, inference, model, mcp, ui-frontend, awesome-list, cookbook, learning

## 统计数据

| 指标 | 数据 |
|------|------|
| 行业文档 | 40 篇（3,904 行） |
| 能力文档 | 10 篇（1,164 行） |
| Wiki 编译文章 | 50 篇（5,661 行） |
| Raw 源材料 | 38 篇（1,416 行） |
| GitHub 仓库索引 | 47+ |
| 总 Stars | 2,700,000+ |
| 总文件 | 316 |
| 总大小 | 2.5MB |

## Hermes 调用方式

### 查询行业知识
```
read_file("kb/industry/healthcare.md")  # 医疗健康 AI Agent 全景
read_file("kb/capability/mcp.md")       # MCP 生态深度分析
```

### 查询元框架
```
read_file("meta/README.md")             # 知识管理方法论
read_file("memory/README.md")           # Agent 记忆系统对比
read_file("platform/README.md")         # 知识库平台选型
```

### 知识编译工作流
```
read_file("SKILL.md")                   # 完整工作流定义
read_file("wiki/index.md")              # 编译知识索引
```

## License

MIT
