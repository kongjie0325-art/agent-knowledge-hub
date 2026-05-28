#!/usr/bin/env python3
"""generate_docs.py - 从 JSON 数据生成各层 Markdown 文档"""

import json
from pathlib import Path
from datetime import datetime

data_dir = Path("data")
json_files = sorted(data_dir.glob("repos_*.json"))
if not json_files:
    print("No JSON files found")
    exit(1)

latest = json_files[-1]
with open(latest) as f:
    repos = json.load(f)

by_cat = {}
for r in repos:
    cat = r.get("category", "unknown")
    by_cat.setdefault(cat, []).append(r)

cat_info = {
    "kb": ("知识库核心项目", "知识编译、LLM Wiki、知识图谱构建"),
    "memory": ("长期记忆系统", "Agent 记忆层、时序知识图谱"),
    "platform": ("传统知识库平台", "笔记应用、维基、文档管理"),
    "meta": ("元框架与目录", "知识管理 awesome 列表、目录型仓库"),
}

pri_order = {"P0": 0, "P1": 1, "P2": 2}

def gen_doc(items, title, desc):
    lines = [
        f"# {title}",
        "",
        f"> {desc}",
        "",
        f"更新时间: {datetime.utcnow().strftime(\'%Y-%m-%d %H:%M\')} UTC",
        "",
    ]
    items.sort(key=lambda x: pri_order.get(x.get("priority", "P2"), 99))
    for r in items:
        name = r.get("full_name", "?")
        description = r.get("description", "")
        url = r.get("html_url", "")
        lang = r.get("language", "N/A")
        stars = r.get("stars", "?")
        forks = r.get("forks", "?")
        license_ = r.get("license", "")
        topics = r.get("topics", [])
        updated = r.get("updated_at", "")[:10]
        pri = r.get("priority", "")
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"**{description}**")
        lines.append("")
        lines.append(f"- ⭐ Stars: {stars}")
        lines.append(f"- 🍴 Forks: {forks}")
        lines.append(f"- 💻 语言: {lang}")
        lines.append(f"- 📋 License: {license_}")
        lines.append(f"- 🏷️ Topics: {\', \'.join(topics)}")
        lines.append(f"- 📅 更新: {updated}")
        lines.append(f"- 🔗 URL: {url}")
        lines.append(f"- 📊 优先级: {pri}")
        lines.append("")
    return "\n".join(lines)

for cat, (title, desc) in cat_info.items():
    items = by_cat.get(cat, [])
    content = gen_doc(items, title, desc)
    path = Path(f"{cat}/README.md")
    path.write_text(content, encoding="utf-8")
    print(f"✅ {path}")

print("Done.")
