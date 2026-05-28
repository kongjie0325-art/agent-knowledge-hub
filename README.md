# Agent Knowledge Hub

> 基于 Karpathy LLM Wiki / 知识编译路线的 Agent 优先知识库目录。
> 自动从 GitHub 检索、拉取、整理。

## 结构

```
meta/      知识库构建元框架和核心理念
kb/        核心知识库项目（按底座路线分类）
memory/    长期记忆系统
platform/  传统知识库/文档平台
scripts/   自动化拉取和整理脚本
data/      导出的结构化数据（CSV/JSON）
```

## 快速开始

```bash
# 一键拉取所有项目信息
python3 scripts/fetch_repos.py

# 输出: data/repos_*.json + data/repos_*.csv
```

## 底座路线

| 路线 | 核心项目 | 说明 |
|------|----------|------|
| 本地优先 Wiki | swarmvault, synthadoc | 本地知识保险库 |
| 知识编译 | pagefly, karpathy-llm-wiki | 文档→知识转换 |
| 长期记忆 | mem0, langmem | Agent 记忆层 |
| 时序图谱 | graphiti, zep, langgraph | 知识图谱 |

## 项目清单

详见 [data/repos_*.csv](data/) 或各层目录。

## License

MIT
