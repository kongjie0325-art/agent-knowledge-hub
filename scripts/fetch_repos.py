#!/usr/bin/env python3
"""
Agent Knowledge Hub - GitHub 高引用 Agent 仓库自动拉取脚本
使用 gh CLI 获取数据（避免 GitHub API 限流）
"""
import os, json, subprocess, csv, argparse
from pathlib import Path
from datetime import datetime

# 高引用 Agent 相关仓库（按分类组织）
REPOS = [
    # Agent Framework
    ("NousResearch/hermes-agent", "agent-framework", "P0", "The agent that grows with you"),
    ("langchain-ai/langchain", "agent-framework", "P0", "The agent engineering platform"),
    ("geekan/MetaGPT", "agent-framework", "P0", "Multi-Agent Framework"),
    ("microsoft/autogen", "agent-framework", "P0", "Programming framework for agentic AI"),
    ("crewAIInc/crewAI", "agent-framework", "P0", "Orchestrating role-playing AI agents"),
    ("microsoft/semantic-kernel", "agent-framework", "P1", "Integrate LLM into apps"),
    ("openai/openai-agents-python", "agent-framework", "P0", "Multi-agent workflows"),
    ("TransformerOptimus/SuperAGI", "agent-framework", "P1", "Autonomous AI agent framework"),
    ("simular-ai/Agent-S", "agent-framework", "P1", "Agentic framework using computers like a human"),

    # Agent Platform
    ("langgenius/dify", "agent-platform", "P0", "Production-ready agentic workflow platform"),
    ("FlowiseAI/Flowise", "agent-platform", "P1", "Build AI Agents Visually"),
    ("chatchat-space/Langchain-Chatchat", "agent-platform", "P1", "RAG and Agent framework (Chinese)"),
    ("reworkd/AgentGPT", "agent-platform", "P1", "Autonomous AI Agents in browser"),
    ("xlang-ai/OpenAgents", "agent-platform", "P2", "Open Platform for Language Agents"),
    ("gobii-ai/gobii-platform", "agent-platform", "P2", "Always-on AI workforce"),

    # Coding Agent
    ("anthropics/claude-code", "coding-agent", "P0", "Agentic coding tool in terminal"),
    ("All-Hands-AI/OpenHands", "coding-agent", "P0", "AI-Driven Development"),
    ("stitionai/devika", "coding-agent", "P1", "Agentic Software Engineer"),

    # Inference & Deployment
    ("ollama/ollama", "inference", "P0", "Run LLMs locally"),
    ("ggerganov/llama.cpp", "inference", "P0", "LLM inference in C/C++"),
    ("vllm-project/vllm", "inference", "P0", "High-throughput LLM inference engine"),
    ("mistralai/mistral-inference", "inference", "P2", "Mistral inference library"),

    # Model
    ("deepseek-ai/DeepSeek-V3", "model", "P0", "DeepSeek V3 model"),
    ("meta-llama/llama", "model", "P1", "Llama inference code"),

    # ML Framework
    ("huggingface/transformers", "ml-framework", "P0", "State-of-the-art ML model framework"),

    # UI & Frontend
    ("open-webui/open-webui", "ui-frontend", "P0", "User-friendly AI Interface"),
    ("lobehub/lobe-chat", "ui-frontend", "P1", "LobeHub Agent Operator"),

    # MCP
    ("punkpeye/awesome-mcp-servers", "mcp", "P0", "Collection of MCP servers"),
    ("punkpeye/awesome-mcp-clients", "mcp", "P1", "Collection of MCP clients"),

    # Cookbook
    ("openai/openai-cookbook", "cookbook", "P0", "OpenAI API examples and guides"),
    ("anthropics/anthropic-cookbook", "cookbook", "P0", "Claude API recipes"),
    ("google-gemini/cookbook", "cookbook", "P1", "Gemini API examples"),

    # Awesome List
    ("Shubhamsaboo/awesome-llm-apps", "awesome-list", "P0", "100+ AI Agent & RAG apps"),
    ("e2b-dev/awesome-ai-agents", "awesome-list", "P1", "List of AI autonomous agents"),
    ("Hannibal046/Awesome-LLM", "awesome-list", "P1", "Curated list of LLM resources"),
    ("luo-junyu/Awesome-Agent-Papers", "awesome-list", "P2", "LLM Agent survey papers"),
    ("kyrolabs/awesome-agents", "awesome-list", "P2", "Awesome list of AI Agents"),
    ("jim-schwoebel/awesome_ai_agents", "awesome-list", "P2", "1500+ AI agent resources"),
    ("caramaschiHG/awesome-ai-agents-2026", "awesome-list", "P2", "AI agents list 2026"),

    # Learning
    ("microsoft/ai-agents-for-beginners", "learning", "P0", "12 Lessons for AI Agents"),
    ("NirDiamant/GenAI_Agents", "learning", "P0", "50+ GenAI Agent tutorials"),
    ("ashishps1/learn-ai-engineering", "learning", "P1", "Learn AI from scratch"),
    ("ed-donner/agents", "learning", "P1", "Complete Agentic AI Engineering Course"),
    ("coleam00/ai-agents-masterclass", "learning", "P2", "AI Agents Masterclass"),

    # Educational
    ("karpathy/nanochat", "educational", "P0", "Best ChatGPT that $100 can buy"),
    ("karpathy/nn-zero-to-hero", "educational", "P0", "Neural Networks: Zero to Hero"),

    # Prompts & Resources
    ("x1xhlol/system-prompts-and-models-of-ai-tools", "prompts", "P0", "System prompts collection"),
]

def fetch_repo_gh(repo):
    """使用 gh CLI 获取仓库信息"""
    try:
        r = subprocess.run(
            ["gh", "repo", "view", repo,
             "--json", "stargazerCount,forkCount,description,primaryLanguage,updatedAt,url,repositoryTopics"],
            capture_output=True, text=True, timeout=15
        )
        if r.returncode == 0:
            d = json.loads(r.stdout)
            return {
                "full_name": repo,
                "description": d.get("description", ""),
                "url": d.get("url", ""),
                "language": (d.get("primaryLanguage") or {}).get("name", ""),
                "stars": d.get("stargazerCount", 0),
                "forks": d.get("forkCount", 0),
                "topics": [t["name"] for t in d.get("repositoryTopics", [])],
                "updated_at": (d.get("updatedAt") or "")[:10],
            }
        return {"full_name": repo, "error": r.stderr.strip()[:100]}
    except Exception as e:
        return {"full_name": repo, "error": str(e)[:100]}

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repo data for Agent Knowledge Hub")
    parser.add_argument("--output", default="data/", help="Output directory")
    parser.add_argument("--repos", nargs="*", help="Specific repos to fetch (default: all)")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    repos_to_fetch = REPOS
    if args.repos:
        repos_to_fetch = [r for r in REPOS if r[0] in args.repos]

    results = []
    for i, (repo, cat, pri, desc) in enumerate(repos_to_fetch, 1):
        print(f"[{i}/{len(repos_to_fetch)}] {repo}")
        info = fetch_repo_gh(repo)
        info["category"] = cat
        info["priority"] = pri
        info["description"] = desc
        if "error" in info:
            print(f"  ERROR: {info['error']}")
        else:
            print(f"  {info.get('stars', 0)} stars | {info.get('language', 'N/A')}")
        results.append(info)

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    # JSON
    json_path = output_dir / f"repos_{ts}.json"
    json_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

    # CSV
    fields = ["full_name", "description", "url", "language", "stars", "forks",
              "category", "priority", "topics", "updated_at"]
    csv_path = output_dir / f"repos_{ts}.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in results:
            row = {k: r.get(k, "") for k in fields}
            row["topics"] = ", ".join(row.get("topics", []))
            w.writerow(row)

    # Also write latest symlink
    latest_json = output_dir / "repos_latest.json"
    latest_csv = output_dir / "repos_latest.csv"
    latest_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    with open(latest_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in results:
            row = {k: r.get(k, "") for k in fields}
            row["topics"] = ", ".join(row.get("topics", []))
            w.writerow(row)

    ok = [r for r in results if "error" not in r]
    total_stars = sum(r.get("stars", 0) for r in ok)
    print(f"\nDone. {len(ok)}/{len(results)} repos fetched. {total_stars:,} total stars.")
    print(f"  JSON: {json_path}")
    print(f"  CSV:  {csv_path}")

if __name__ == "__main__":
    main()
