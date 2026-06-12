# MCP 生态

> 能力分类: MCP 生态 (MCP Ecosystem) | 更新时间: 2026-06-12

## 概述

Model Context Protocol (MCP) 是由 Anthropic 提出的开放协议，用于标准化 AI 模型与外部工具和数据源之间的连接方式。MCP 定义了 Client-Server 架构：MCP Server 暴露工具（Tools）、资源（Resources）和提示（Prompts），MCP Client（通常是 AI Agent 或 IDE）通过协议发现和调用这些能力。MCP 的意义在于打破了每个平台自己定义工具格式的碎片化局面——类似 USB-C 统一了充电接口。

MCP 协议基于 JSON-RPC 2.0 传输，支持 stdio、SSE 和 HTTP 三种传输层。核心能力包括：工具发现与调用（Client → Server）、资源读取（Server → Client）、提示模板（Server → Client）、以及采样（Server 让 Client 调用 LLM）。2026 年，MCP 已成为 Agent 工具集成的事实标准，主流框架（LangChain、AutoGen、CrewAI）和平台（Dify、OpenAI Agents）都已原生支持 MCP。

## 核心能力矩阵

| 维度 | 说明 |
|------|------|
| 协议规范 | JSON-RPC 2.0 / stdio / SSE / Streamable HTTP |
| 能力类型 | Tools / Resources / Prompts / Sampling |
| 传输层 | stdio（本地）/ SSE（远程）/ HTTP（云原生） |
| Server 类型 | 文件系统 / 数据库 / API / 浏览器 / 自定义 |
| Client 集成 | Agent 框架 / IDE / CLI / Web 应用 |
| 安全模型 | 权限声明 / 用户确认 / 沙箱隔离 |
| 发现机制 | 注册表 / 配置文件 / 自动发现 |
| 生态规模 | 官方 Server / 社区 Server / 企业 Server |

## 主流方案对比

| 方案 | Stars | 语言 | 架构 | 优势 | 劣势 | 适用场景 |
|------|-------|------|------|------|------|----------|
| Awesome MCP Servers | 88,047 | - | 精选列表 | 最全面的 MCP Server 合集 | 仅列表，非工具 | 发现可用 Server |
| Awesome MCP Clients | 6,449 | - | 精选列表 | 全面的 MCP Client 合集 | 仅列表，非工具 | 发现可用 Client |
| MCP Python SDK | - | Python | SDK | 官方 SDK，文档完善 | 仅 Python | Python MCP 开发 |
| MCP TypeScript SDK | - | TypeScript | SDK | 官方 SDK，类型安全 | 仅 TypeScript | TypeScript MCP 开发 |
| Smithery | - | - | 注册表 | MCP Server 托管和发现平台 | 中心化 | Server 发布和发现 |
| Glama | - | - | 网关 | MCP Server 网关和监控 | 较新 | 企业级 MCP 管理 |

## 选型决策树

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

快速体验：
- 想立即试用 MCP？ → 安装 Cursor IDE + 配置 MCP Server
- 想开发 MCP Server？ → 从 MCP Python/TypeScript SDK 开始
- 想发现可用 Server？ → 浏览 Awesome MCP Servers
```

## 快速上手

### 创建最小 MCP Server（Python）
```python
# pip install mcp
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

### 创建最小 MCP Server（TypeScript）
```typescript
// npm install @modelcontextprotocol/sdk
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({
  name: "my-server",
  version: "1.0.0"
});

server.tool("add", "Add two numbers", {
  a: { type: "number" },
  b: { type: "number" }
}, async ({ a, b }) => ({
  content: [{ type: "text", text: String(a + b) }]
}));

const transport = new StdioServerTransport();
await server.connect(transport);
```

### 在 Claude Desktop 配置 MCP Server
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

## 高引用仓库

| Stars | 仓库 | 语言 | 描述 |
|-------|------|------|------|
| 88,047 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | - | A collection of MCP servers |
| 6,449 | [punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) | - | A collection of MCP clients |

## Awesome Lists

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP Server 精选合集
- [punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) - MCP Client 精选合集

## 扩展空间

> 🔲 待补充：MCP Server 开发最佳实践
> 🔲 待补充：MCP 安全模型和权限控制详解
> 🔲 待补充：MCP 与 OpenAPI/REST API 的对比
> 🔲 待补充：MCP 在主流 Agent 框架中的集成方式
> 🔲 待补充：MCP Server 性能优化和部署方案
