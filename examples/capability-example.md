# 能力域文章示例：MCP 生态

> **本文展示能力域文章的编译格式。** 以 MCP (Model Context Protocol) 为例，演示如何将 raw/ 源材料编译为结构化的能力域文章。

---

## 元数据

| 字段 | 值 |
|------|-----|
| **标题** | MCP 生态 |
| **类型** | 能力域文章 (Capability Article) |
| **能力域** | 工具集成 (Tool Integration) |
| **来源** | [raw/capability/mcp.md](../../raw/capability/mcp.md) |
| **编译时间** | 2026-06-12 |
| **状态** | ✅ 已编译 |

---

## 概述

Model Context Protocol (MCP) 是由 Anthropic 提出的开放协议，用于标准化 AI 模型与外部工具和数据源之间的连接方式。MCP 定义了 Client-Server 架构：MCP Server 暴露工具（Tools）、资源（Resources）和提示（Prompts），MCP Client（通常是 AI Agent 或 IDE）通过协议发现和调用这些能力。

MCP 的意义在于打破了每个平台自己定义工具格式的碎片化局面——类似 USB-C 统一了充电接口。2026 年，MCP 已成为 Agent 工具集成的事实标准，主流框架和平台都已原生支持 MCP。

---

## 关键概念

### 1. 协议规范
MCP 基于 JSON-RPC 2.0，支持 stdio（本地）、SSE（远程）和 Streamable HTTP（云原生）三种传输层。

### 2. 能力类型
- **Tools**: Server 暴露的可调用函数
- **Resources**: Server 提供的数据资源
- **Prompts**: 预定义的提示模板
- **Sampling**: Client 请求 Server 进行采样

### 3. Server 类型
文件系统、数据库、API、浏览器、自定义业务逻辑等。

### 4. 安全模型
权限声明、用户确认、沙箱隔离三层安全保障。

### 5. 发现机制
注册表、配置文件、自动发现三种方式。

---

## 核心发现

| # | 发现 | 来源 |
|---|------|------|
| 1 | Awesome MCP Servers 最全面，88k+ Stars | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) |
| 2 | Awesome MCP Clients 全面收录 Client 实现 | [punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) |
| 3 | MCP 已成为事实标准，主流框架原生支持 | LangChain、AutoGen、CrewAI、Dify、OpenAI Agents |
| 4 | MCP Python/TypeScript SDK 官方维护 | 文档完善，上手简单 |
| 5 | Smithery/Glama 提供 Server 托管和网关管理 | 降低运维门槛 |

---

## 实践指南

### 选型决策树

```
角色？
├── MCP Server 开发者
│   ├── Python → MCP Python SDK
│   ├── TypeScript → MCP TypeScript SDK
│   └── 需要灵感 → Awesome MCP Servers
├── MCP Client 开发者（Agent/IDE）
│   ├── 需要现成 Client → Awesome MCP Clients
│   └── 框架集成 → 查看框架是否原生支持 MCP
└── MCP 运维/管理
    ├── Server 发布 → Smithery
    └── 网关管理 → Glama
```

### 快速上手

```python
# 创建最小 MCP Server（Python）
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def search(query: str) -> str:
    """Search the web"""
    return f"Results for: {query}"

if __name__ == "__main__":
    mcp.run()
```

```json
// 在 Claude Desktop 配置 MCP Server
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

---

## 来源

- **原始资料**: [raw/capability/mcp.md](../../raw/capability/mcp.md)
- **上游来源**: kb/capability/mcp.md
- **编译方式**: 从 raw/ 源材料提炼，遵循 article-template.md 格式

---

## See Also

- [Agent 框架](../wiki/capability/agent-framework.md) — Agent 框架通过 MCP 集成工具
- [Agent 平台](../wiki/capability/agent-platform.md) — Agent 平台深度集成 MCP
- [编码 Agent](../wiki/capability/coding-agent.md) — 编码 Agent 通过 MCP 扩展能力
