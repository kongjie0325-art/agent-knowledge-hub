#!/usr/bin/env python3
"""
Agent Knowledge Hub - GitHub 仓库自动拉取脚本
支持按行业 (industry) 和能力 (capability) 双维度分类
使用 gh CLI 获取数据（避免 GitHub API 限流）
"""
import os, json, subprocess, csv, argparse
from pathlib import Path
from datetime import datetime

# 仓库清单：支持 industry 和 capability 双维度分类
# 格式: (owner/repo, category, priority, description, [industries], [capabilities])
REPOS = [
    # === Agent Framework ===
    ("NousResearch/hermes-agent", "capability", "P0", "The agent that grows with you", [], ["agent-framework"]),
    ("langchain-ai/langchain", "capability", "P0", "The agent engineering platform", [], ["agent-framework"]),
    ("geekan/MetaGPT", "capability", "P0", "Multi-Agent Framework", [], ["agent-framework"]),
    ("microsoft/autogen", "capability", "P0", "Programming framework for agentic AI", [], ["agent-framework"]),
    ("crewAIInc/crewAI", "capability", "P0", "Orchestrating role-playing AI agents", [], ["agent-framework"]),
    ("microsoft/semantic-kernel", "capability", "P1", "Integrate LLM into apps", [], ["agent-framework"]),
    ("openai/openai-agents-python", "capability", "P0", "Multi-agent workflows", [], ["agent-framework"]),
    ("TransformerOptimus/SuperAGI", "capability", "P1", "Autonomous AI agent framework", [], ["agent-framework"]),
    ("simular-ai/Agent-S", "capability", "P1", "Agentic framework using computers like a human", ["healthcare"], ["agent-framework"]),

    # === Agent Platform ===
    ("langgenius/dify", "capability", "P0", "Production-ready agentic workflow platform", [], ["agent-platform"]),
    ("FlowiseAI/Flowise", "capability", "P1", "Build AI Agents Visually", [], ["agent-platform"]),
    ("chatchat-space/Langchain-Chatchat", "capability", "P1", "RAG and Agent framework (Chinese)", [], ["agent-platform"]),
    ("reworkd/AgentGPT", "capability", "P1", "Autonomous AI Agents in browser", [], ["agent-platform"]),
    ("xlang-ai/OpenAgents", "capability", "P2", "Open Platform for Language Agents", [], ["agent-platform"]),
    ("gobii-ai/gobii-platform", "capability", "P2", "Always-on AI workforce", [], ["agent-platform"]),

    # === Coding Agent ===
    ("anthropics/claude-code", "capability", "P0", "Agentic coding tool in terminal", [], ["coding-agent"]),
    ("All-Hands-AI/OpenHands", "capability", "P0", "AI-Driven Development", [], ["coding-agent"]),
    ("stitionai/devika", "capability", "P1", "Agentic Software Engineer", [], ["coding-agent"]),

    # === Inference ===
    ("ollama/ollama", "capability", "P0", "Run LLMs locally", [], ["inference"]),
    ("ggerganov/llama.cpp", "capability", "P0", "LLM inference in C/C++", [], ["inference"]),
    ("vllm-project/vllm", "capability", "P0", "High-throughput LLM inference engine", [], ["inference"]),
    ("mistralai/mistral-inference", "capability", "P2", "Mistral inference library", [], ["inference"]),

    # === Model ===
    ("deepseek-ai/DeepSeek-V3", "capability", "P0", "DeepSeek V3 model", [], ["model"]),
    ("meta-llama/llama", "capability", "P1", "Llama inference code", [], ["model"]),
    ("huggingface/transformers", "capability", "P0", "State-of-the-art ML model framework", [], ["model"]),

    # === MCP ===
    ("punkpeye/awesome-mcp-servers", "capability", "P0", "Collection of MCP servers", [], ["mcp"]),
    ("punkpeye/awesome-mcp-clients", "capability", "P1", "Collection of MCP clients", [], ["mcp"]),

    # === UI/Frontend ===
    ("open-webui/open-webui", "capability", "P0", "User-friendly AI Interface", [], ["ui-frontend"]),
    ("lobehub/lobe-chat", "capability", "P1", "LobeHub Agent Operator", [], ["ui-frontend"]),

    # === Cookbook ===
    ("openai/openai-cookbook", "capability", "P0", "OpenAI API examples and guides", [], ["cookbook"]),
    ("anthropics/anthropic-cookbook", "capability", "P0", "Claude API recipes", [], ["cookbook"]),
    ("google-gemini/cookbook", "capability", "P1", "Gemini API examples", [], ["cookbook"]),

    # === Awesome List ===
    ("Shubhamsaboo/awesome-llm-apps", "capability", "P0", "100+ AI Agent & RAG apps", [], ["awesome-list"]),
    ("e2b-dev/awesome-ai-agents", "capability", "P1", "List of AI autonomous agents", [], ["awesome-list"]),
    ("Hannibal046/Awesome-LLM", "capability", "P1", "Curated list of LLM resources", [], ["awesome-list"]),
    ("luo-junyu/Awesome-Agent-Papers", "capability", "P2", "LLM Agent survey papers", [], ["awesome-list"]),
    ("kyrolabs/awesome-agents", "capability", "P2", "Awesome list of AI Agents", [], ["awesome-list"]),
    ("jim-schwoebel/awesome_ai_agents", "capability", "P2", "1500+ AI agent resources", [], ["awesome-list"]),
    ("caramaschiHG/awesome-ai-agents-2026", "capability", "P2", "AI agents list 2026", [], ["awesome-list"]),

    # === Learning ===
    ("microsoft/ai-agents-for-beginners", "capability", "P0", "12 Lessons for AI Agents", [], ["learning"]),
    ("karpathy/nanochat", "capability", "P0", "Best ChatGPT that $100 can buy", [], ["learning"]),
    ("karpathy/nn-zero-to-hero", "capability", "P0", "Neural Networks: Zero to Hero", [], ["learning"]),
    ("NirDiamant/GenAI_Agents", "capability", "P0", "50+ GenAI Agent tutorials", [], ["learning"]),
    ("ashishps1/learn-ai-engineering", "capability", "P1", "Learn AI from scratch", [], ["learning"]),
    ("ed-donner/agents", "capability", "P1", "Complete Agentic AI Engineering Course", [], ["learning"]),
    ("coleam00/ai-agents-masterclass", "capability", "P2", "AI Agents Masterclass", [], ["learning"]),

    # === Prompts & Resources ===
    ("x1xhlol/system-prompts-and-models-of-ai-tools", "capability", "P0", "System prompts collection", [], ["cookbook"]),

    # === Industry: Healthcare ===
    ("AgenticHealthAI/Awesome-AI-Agents-for-Healthcare", "industry", "P1", "Healthcare AI Agent resources", ["healthcare"], []),
    ("mims-harvard/TxAgent", "industry", "P1", "AI agent for therapeutic reasoning", ["healthcare"], []),
    ("yhzhu99/HealthFlow", "industry", "P1", "Self-Evolving AI Agent for Healthcare Research", ["healthcare"], []),
    ("stanfordmlgroup/MedAgentBench", "industry", "P1", "Virtual EHR Environment for Medical LLM Agents", ["healthcare"], []),
    ("gersteinlab/medagents-benchmark", "industry", "P2", "Medical Reasoning Benchmark", ["healthcare"], []),
    ("samuelschmidgall/agentclinic", "industry", "P2", "Multimodal Agent Benchmark for Clinical AI", ["healthcare"], []),

    # === Industry: Multi-industry ===
    ("ashishpatel26/500-AI-Agents-Projects", "industry", "P0", "500+ AI agent use cases across industries", ["healthcare", "finance", "education", "retail", "manufacturing"], []),
    ("msitarzewski/agency-agents", "industry", "P1", "51 AI Specialist Agents (Engineering/Design/Marketing/PM/QA/Support)", ["marketing", "sales", "customer-service", "human-resources"], []),
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
    parser.add_argument("--format", choices=["json", "csv", "both"], default="both", help="Output format")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    repos_to_fetch = REPOS
    if args.repos:
        repos_to_fetch = [r for r in REPOS if r[0] in args.repos]

    results = []
    for i, (repo, cat, pri, desc, industries, capabilities) in enumerate(repos_to_fetch, 1):
        print(f"[{i}/{len(repos_to_fetch)}] {repo}")
        info = fetch_repo_gh(repo)
        info["category"] = cat
        info["priority"] = pri
        info["description"] = desc
        info["industries"] = industries
        info["capabilities"] = capabilities
        if "error" in info:
            print(f"  ERROR: {info['error']}")
        else:
            print(f"  {info.get('stars', 0)} stars | {info.get('language', 'N/A')} | ind:{industries} cap:{capabilities}")
        results.append(info)

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    ok = [r for r in results if "error" not in r]
    total_stars = sum(r.get("stars", 0) for r in ok)

    if args.format in ("json", "both"):
        json_path = output_dir / f"repos_{ts}.json"
        json_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        latest_json = output_dir / "repos_latest.json"
        latest_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"JSON: {json_path}")

    if args.format in ("csv", "both"):
        fields = ["full_name", "description", "url", "language", "stars", "forks",
                  "category", "priority", "industries", "capabilities", "topics", "updated_at"]
        csv_path = output_dir / f"repos_{ts}.csv"
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in results:
                row = {k: r.get(k, "") for k in fields}
                row["topics"] = ", ".join(row.get("topics", []))
                row["industries"] = ", ".join(row.get("industries", []))
                row["capabilities"] = ", ".join(row.get("capabilities", []))
                w.writerow(row)
        latest_csv = output_dir / "repos_latest.csv"
        with open(latest_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in results:
                row = {k: r.get(k, "") for k in fields}
                row["topics"] = ", ".join(row.get("topics", []))
                row["industries"] = ", ".join(row.get("industries", []))
                row["capabilities"] = ", ".join(row.get("capabilities", []))
                w.writerow(row)
        print(f"CSV:  {csv_path}")

    print(f"\nDone. {len(ok)}/{len(results)} repos fetched. {total_stars:,} total stars.")

if __name__ == "__main__":
    main()
