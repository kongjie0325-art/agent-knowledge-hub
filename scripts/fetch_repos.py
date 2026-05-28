#!/usr/bin/env python3
import os, json, time, base64, argparse, csv, requests
from pathlib import Path
from datetime import datetime

REPOS = [
    ("swarmclawai/swarmvault", "platform", "P0", "本地优先知识保险库"),
    ("axoviq-ai/synthadoc", "platform", "P0", "合成文档引擎"),
    ("Yrzhe/pagefly", "kb", "P0", "页面级知识编译"),
    ("Astro-Han/karpathy-llm-wiki", "kb", "P0", "Karpathy LLM Wiki"),
    ("mem0ai/mem0", "memory", "P0", "Agent 长期记忆层"),
    ("langchain-ai/langmem", "memory", "P0", "LangChain 记忆模块"),
    ("langchain-ai/langgraph", "kb", "P0", "知识图谱构建"),
    ("getzep/graphiti", "memory", "P0", "时序知识图谱"),
    ("getzep/zep", "memory", "P0", "知识图谱平台"),
    ("toeverything/AFFiNE", "platform", "P1", "开源 Notion 替代"),
    ("AppFlowy-IO/AppFlowy", "platform", "P1", "开源 Notion 替代"),
    ("laurent22/joplin", "platform", "P1", "开源笔记应用"),
    ("TriliumNext/Trilium", "platform", "P1", "层级知识库"),
    ("requarks/wiki", "platform", "P2", "Wiki.js 维基平台"),
    ("BookStackApp/BookStack", "platform", "P2", "文档管理平台"),
    ("MaggieAppleton/awesome-knowledge-management", "meta", "P2", "知识管理awesome"),
]

GITHUB_API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def get_headers():
    h = {"Accept": "application/vnd.github.v3+json"}
    if TOKEN:
        h["Authorization"] = "token " + TOKEN
    return h

def fetch_repo_info(owner_repo):
    url = GITHUB_API + "/repos/" + owner_repo
    try:
        resp = requests.get(url, headers=get_headers(), timeout=15)
        if resp.status_code == 200:
            d = resp.json()
            return {
                "full_name": d["full_name"],
                "description": d.get("description", ""),
                "html_url": d["html_url"],
                "language": d.get("language", ""),
                "stars": d["stargazers_count"],
                "forks": d["forks_count"],
                "topics": d.get("topics", []),
                "license": (d.get("license") or {}).get("spdx_id", ""),
                "updated_at": d["updated_at"],
            }
        return {"error": "http_" + str(resp.status_code)}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/")
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for i, (repo, cat, pri, desc) in enumerate(REPOS, 1):
        print(f"[{i}/{len(REPOS)}] {repo}")
        info = fetch_repo_info(repo)
        info["category"] = cat
        info["priority"] = pri
        info["description"] = desc
        if "error" in info:
            print(f"  ERROR: {info['error']}")
        else:
            print(f"  {info.get('stars', 0)} stars | {info.get('language', 'N/A')}")
        results.append(info)
        time.sleep(args.delay)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    (output_dir / f"repos_{ts}.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    fields = ["full_name","description","html_url","language","stars","forks","license","category","priority","topics","updated_at"]
    with open(output_dir / f"repos_{ts}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in results:
            row = {k: r.get(k, "") for k in fields}
            row["topics"] = ", ".join(row.get("topics", []))
            w.writerow(row)
    print(f"\nDone. {len(results)} repos saved.")

if __name__ == "__main__":
    main()
