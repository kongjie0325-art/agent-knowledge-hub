# Raw — 原始资料层

> 本目录是 Agent Knowledge Hub 的"原始资料"层，遵循 Karpathy LLM Wiki 的三层架构理念。

## 用途

- 存储从外部获取的原始资料索引（GitHub 仓库链接、描述、元数据）
- 作为 wiki/ 编译层的输入源
- **不可变性**：raw/ 中的内容只读不写，保持原始资料的完整性

## 目录结构

```
raw/
  capability/    # 按能力分类的源材料索引
  industry/      # 按行业分类的源材料索引
  README.md      # 本文件
```

## 与 kb/ 的关系

kb/ 目录中的内容（仓库列表、描述、分类信息）是 raw/ 的主要来源。
raw/ 将这些信息整理为标准化的源材料索引，供 wiki/ 编译使用。

## 与 wiki/ 的关系

wiki/ 是 raw/ 的编译版本——将原始资料提炼为结构化的知识文章。
raw → wiki 的编译过程由 Agent 执行，遵循 SKILL.md 中定义的工作流。
