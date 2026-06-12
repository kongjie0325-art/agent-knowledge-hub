# MCP 生态

> Sources: kb/capability/mcp.md; 2026-06-12
> Raw: [mcp](../../raw/capability/mcp.md)

## 概述

Model Context Protocol (MCP) 是由 Anthropic 提出的开放协议，用于标准化 AI 模型与外部工具和数据源之间的连接方式。MCP 定义了 Client-Server 架构：MCP Server 暴露工具（Tools）、资源（Resources）和提示（Prompts），MCP Client（通常是 AI Agent 或 IDE）通过协议发现和调用这些能力。

MCP 的意义在于打破了每个平台自己定义工具格式的碎片化局面——类似 USB-C 统一了充电接口。2026 年，MCP 已成为 Agent 工具集成的事实标准，主流框架和平台都已原生支持 MCP。

## 关键概念

- **协议规范**: JSON-RPC 2.0 / stdio / SSE / Streamable HTTP
- **能力类型**: Tools / Resources / Prompts / Sampling
- **传输层**: stdio（本地）/ SSE（远程）/ HTTP（云原生）
- **Server 类型**: 文件系统 / 数据库 / API / 浏览器 / 自定义
- **Client 集成**: Agent 框架 / IDE / CLI / Web 应用
- **安全模型**: 权限声明 / 用户确认 / 沙箱隔离
- **发现机制**: 注册表 / 配置文件 / 自动发现

## 核心发现

1. **Awesome MCP Servers 最全面**（88k+ Stars），最全面的 MCP Server 合集
2. **Awesome MCP Clients**（6.4k+ Stars），全面的 MCP Client 合集
3. **MCP 已成为事实标准**: LangChain、AutoGen、CrewAI、Dify、OpenAI Agents 原生支持
4. **MCP Python/TypeScript SDK**: 官方 SDK，文档完善
5. **Smithery/Glama**: MCP Server 托管和网关管理平台

## 实践指南

### 选型决策树

```
角色？
├── MCP Server 开发者
│   ├── Python → MCP Python SDK
│   ├── TypeScript → MCP TypeScript SDK
│   └── 需要灵感 → Awesome MCP Servers（参考现有实现）
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

## See Also

- [Agent 框架](../capability/agent-framework.md) — Agent 框架通过 MCP 集成工具
- [Agent 平台](../capability/agent-platform.md) — Agent 平台深度集成 MCP

## 更新历史

- 2026-06-12 初始编译，从 kb/capability/mcp.md 提炼
