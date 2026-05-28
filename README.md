# Agent Knowledge Hub

> 基于 Karpathy LLM Wiki / 知识编译路线的 Agent 优先知识库目录。
> 按**各行各业**分类，支持 Hermes Agent 查询和扩展。

## 结构

```
api/                    Hermes 可查询的 JSON 索引
  index.json            主索引（行业 + 能力 + API 说明）

kb/                    知识库
  industry/            按行业分类（18 个行业）
    healthcare.md      医疗健康
    finance.md         金融
    legal.md           法律
    education.md       教育
    manufacturing.md   制造业
    retail.md          零售电商
    marketing.md       营销
    sales.md           销售
    customer-service.md 客户服务
    security.md        安全合规
    agriculture.md     农业
    energy.md          能源
    government.md      政府公共
    research.md        科研
    real-estate.md     房地产
    entertainment.md   娱乐媒体
    logistics.md       物流运输
    human-resources.md 人力资源
    insurance.md       保险

  capability/          按能力分类（10 个能力域）
    agent-framework.md Agent 框架
    agent-platform.md  Agent 平台
    coding-agent.md    编码 Agent
    inference.md       推理部署
    model.md           基础模型
    mcp.md             MCP 生态
    ui-frontend.md     UI/前端
    awesome-list.md    Awesome List
    cookbook.md        Cookbook
    learning.md        学习资源

data/                  结构化数据
  repos_latest.json    最新仓库数据（JSON）
  repos_latest.csv     最新仓库数据（CSV）

scripts/               自动化脚本
  fetch_repos.py       仓库数据拉取
  generate_docs.py     文档生成
```

## Hermes 调用方式

### 1. 读取索引
```bash
# 查看所有行业分类
cat api/index.json | jq '.industries | keys'

# 查看指定行业
cat api/index.json | jq '.industries.healthcare'

# 查看所有能力分类
cat api/index.json | jq '.capabilities | keys'
```

### 2. 查询仓库数据
```bash
# 按 Stars 排序查看 Top 10
cat data/repos_latest.json | jq 'sort_by(.stars) | reverse | .[0:10]'

# 按分类筛选
cat data/repos_latest.json | jq '.[] | select(.category == "agent-framework")'
```

### 3. 扩展新仓库
在 `data/repos_latest.json` 中添加新仓库，然后运行：
```bash
python3 scripts/generate_docs.py  # 自动更新各分类文档
```

## 行业分类（18 个）

| 行业 | 英文 | 文件 |
|------|------|------|
| 医疗健康 | Healthcare | `kb/industry/healthcare.md` |
| 金融 | Finance | `kb/industry/finance.md` |
| 法律 | Legal | `kb/industry/legal.md` |
| 教育 | Education | `kb/industry/education.md` |
| 制造业 | Manufacturing | `kb/industry/manufacturing.md` |
| 零售电商 | Retail | `kb/industry/retail.md` |
| 营销 | Marketing | `kb/industry/marketing.md` |
| 销售 | Sales | `kb/industry/sales.md` |
| 客户服务 | Customer Service | `kb/industry/customer-service.md` |
| 安全合规 | Security | `kb/industry/security.md` |
| 农业 | Agriculture | `kb/industry/agriculture.md` |
| 能源 | Energy | `kb/industry/energy.md` |
| 政府公共 | Government | `kb/industry/government.md` |
| 科研 | Research | `kb/industry/research.md` |
| 房地产 | Real Estate | `kb/industry/real-estate.md` |
| 娱乐媒体 | Entertainment | `kb/industry/entertainment.md` |
| 物流运输 | Logistics | `kb/industry/logistics.md` |
| 人力资源 | HR | `kb/industry/human-resources.md` |
| 保险 | Insurance | `kb/industry/insurance.md` |

## 能力分类（10 个）

| 能力 | 英文 | 文件 |
|------|------|------|
| Agent 框架 | Agent Framework | `kb/capability/agent-framework.md` |
| Agent 平台 | Agent Platform | `kb/capability/agent-platform.md` |
| 编码 Agent | Coding Agent | `kb/capability/coding-agent.md` |
| 推理部署 | Inference | `kb/capability/inference.md` |
| 基础模型 | Foundation Model | `kb/capability/model.md` |
| MCP 生态 | MCP Ecosystem | `kb/capability/mcp.md` |
| UI/前端 | UI & Frontend | `kb/capability/ui-frontend.md` |
| Awesome List | Awesome Lists | `kb/capability/awesome-list.md` |
| Cookbook | Cookbooks | `kb/capability/cookbook.md` |
| 学习资源 | Learning | `kb/capability/learning.md` |

## 统计数据

- **总仓库数**: 47+
- **总 Stars**: 2,700,000+
- **行业覆盖**: 18 个
- **能力覆盖**: 10 个

## 扩展指南

### 添加新行业
1. 在 `kb/industry/` 创建 `{industry}.md`
2. 在 `api/index.json` 的 `industries` 中添加条目
3. 在 `data/repos_latest.json` 中为新仓库添加 `"industry": "{industry}"` 字段

### 添加新能力分类
1. 在 `kb/capability/` 创建 `{capability}.md`
2. 在 `api/index.json` 的 `capabilities` 中添加条目

### 添加新仓库
1. 在 `data/repos_latest.json` 中添加仓库信息
2. 运行 `python3 scripts/generate_docs.py` 自动分发到对应分类

## License

MIT
