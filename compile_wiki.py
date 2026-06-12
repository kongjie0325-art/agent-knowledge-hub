#!/usr/bin/env python3
"""Compile kb/industry/*.md into wiki/industry/*.md articles."""

import os
import re
import sys

KB_DIR = "/home/ubuntu/agent-knowledge-hub/kb/industry"
WIKI_DIR = "/home/ubuntu/agent-knowledge-hub/wiki/industry"

# Files already compiled
EXISTING = {"education.md", "finance.md", "healthcare.md", "software-engineering.md"}

# All industry files
all_files = sorted(f for f in os.listdir(KB_DIR) if f.endswith(".md"))
to_compile = [f for f in all_files if f not in EXISTING]

print(f"Total kb/industry files: {len(all_files)}")
print(f"Already compiled: {len(EXISTING)}")
print(f"To compile: {len(to_compile)}")

# Build the full list of industry names for See Also cross-references
# Map slug to display name from first line of each file
slug_to_name = {}
for f in all_files:
    path = os.path.join(KB_DIR, f)
    with open(path) as fh:
        first_line = fh.readline().strip()
        # Pattern: "# Display Name" or "# Display Name AI Agent"
        name = first_line.lstrip("# ").strip()
        slug_to_name[f.replace(".md", "")] = name

print(f"\nIndustry articles: {list(slug_to_name.keys())}")


def extract_repo_table(text):
    """Extract markdown table blocks (repo data) from text."""
    lines = text.split("\n")
    tables = []
    in_table = False
    table_lines = []
    for line in lines:
        if line.strip().startswith("|") and "---" not in line:
            # Check if it's a header line (has | Stars | or similar)
            in_table = True
            table_lines.append(line)
        elif in_table and line.strip().startswith("|"):
            table_lines.append(line)
        elif in_table and not line.strip().startswith("|"):
            if table_lines:
                tables.append("\n".join(table_lines))
                table_lines = []
            in_table = False
    if table_lines:
        tables.append("\n".join(table_lines))
    return tables


def parse_kb_content(filepath):
    """Parse a kb/industry/*.md file and extract structured content."""
    with open(filepath) as f:
        content = f.read()

    lines = content.split("\n")

    # Extract title
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # Extract overview (概述) - text between # title and ## 子分类
    overview = ""
    in_overview = False
    for line in lines:
        if line.startswith("# "):
            in_overview = True
            continue
        if line.startswith("## ") and in_overview:
            break
        if in_overview:
            overview += line + "\n"
    overview = overview.strip()

    # Extract sub-categories (子分类)
    sub_categories = []
    current_cat = None
    current_items = []
    in_sub = False
    for line in lines:
        if line.startswith("## 子分类") or line.startswith("## 高引用"):
            if current_cat:
                sub_categories.append((current_cat, current_items))
                current_cat = None
                current_items = []
            in_sub = line.startswith("## 子分类")
            continue
        if in_sub:
            if line.startswith("### "):
                if current_cat:
                    sub_categories.append((current_cat, current_items))
                current_cat = line[4:].strip()
                current_items = []
            elif line.startswith("- ") and current_cat:
                current_items.append(line[2:].strip())
    if current_cat:
        sub_categories.append((current_cat, current_items))

    # Extract repo tables
    tables = extract_repo_table(content)

    # Extract Awesome Lists
    awesome_items = []
    in_awesome = False
    for line in lines:
        if "Awesome Lists" in line or "Awesome List" in line:
            in_awesome = True
            continue
        if in_awesome:
            if line.startswith("## ") and "Awesome" not in line:
                in_awesome = False
                continue
            if line.startswith("- [") or line.startswith("- "):
                awesome_items.append(line[2:].strip())

    # Extract related resources
    related = []
    in_related = False
    for line in lines:
        if "相关资源" in line:
            in_related = True
            continue
        if in_related:
            if line.startswith("## ") and "相关" not in line:
                in_related = False
                continue
            if line.startswith("- [") or line.startswith("- "):
                related.append(line[2:].strip())

    # Extract expansion areas
    expansion = []
    in_expansion = False
    for line in lines:
        if "扩展空间" in line:
            in_expansion = True
            continue
        if in_expansion:
            if line.startswith("## "):
                in_expansion = False
                continue
            if line.startswith("> 🔲"):
                expansion.append(line.strip())

    return {
        "title": title,
        "overview": overview,
        "sub_categories": sub_categories,
        "tables": tables,
        "awesome_items": awesome_items,
        "related": related,
        "expansion": expansion,
        "raw_content": content,
    }


def compile_wiki_article(parsed, slug, all_slugs):
    """Compile parsed kb content into wiki article format."""
    title = parsed["title"]

    # Build See Also - cross-reference other industry articles
    see_also = []
    for other_slug, other_name in sorted(all_slugs.items()):
        if other_slug == slug:
            continue
        # Simple relevance: share words in title
        title_words = set(title.lower().replace("ai agent", "").split())
        other_words = set(other_name.lower().replace("ai agent", "").split())
        # Always include a few related ones
        see_also.append((other_slug, other_name))

    # Limit See Also to 5 most relevant (by shared words)
    def relevance(item):
        s, n = item
        tw = set(title.lower().split())
        nw = set(n.lower().split())
        return len(tw & nw)

    see_also.sort(key=relevance, reverse=True)
    see_also = see_also[:5]

    # Build key concepts from sub-categories
    key_concepts = []
    for cat_name, items in parsed["sub_categories"]:
        key_concepts.append(cat_name)
        for item in items[:2]:  # top 2 items per category
            # Clean up the item - take first part before dash or comma
            concept = item.split("（")[0].split(" - ")[0].strip()
            if concept and len(concept) < 60:
                key_concepts.append(concept)

    # Build core findings from repo tables
    core_findings = []
    for table in parsed["tables"]:
        for line in table.split("\n"):
            if line.strip().startswith("|") and "---" not in line and "Stars" not in line:
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if len(cells) >= 3:
                    # Format: Stars | Repo | Lang | Desc | Category
                    repo = cells[1] if len(cells) > 1 else ""
                    desc = cells[3] if len(cells) > 3 else cells[2] if len(cells) > 2 else ""
                    stars = cells[0] if cells[0] else "-"
                    if repo and repo != "仓库":
                        core_findings.append(f"- **{repo}** ({stars}⭐): {desc}")

    # Build practice guide from sub-categories
    practice_items = []
    for cat_name, items in parsed["sub_categories"]:
        practice_items.append(f"### {cat_name}")
        for item in items:
            practice_items.append(f"- {item}")

    # Build the wiki article
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"> Sources: kb/industry/{slug}.md; 2026-06-12")
    lines.append(f"> Raw: [{slug}](../../raw/industry/{slug}.md)")
    lines.append("")
    lines.append("## 概述")
    lines.append("")
    lines.append(parsed["overview"])
    lines.append("")

    # Key concepts
    lines.append("## 关键概念")
    lines.append("")
    for concept in key_concepts[:15]:
        lines.append(f"- {concept}")
    lines.append("")

    # Core findings
    lines.append("## 核心发现")
    lines.append("")
    for finding in core_findings[:15]:
        lines.append(finding)
    lines.append("")

    # Repo tables
    if parsed["tables"]:
        lines.append("## 高引用仓库")
        lines.append("")
        for table in parsed["tables"]:
            lines.append(table)
            lines.append("")

    # Practice guide
    lines.append("## 实践指南")
    lines.append("")
    for item in practice_items:
        lines.append(item)
    lines.append("")

    # Awesome Lists
    if parsed["awesome_items"]:
        lines.append("## Awesome Lists")
        lines.append("")
        for item in parsed["awesome_items"]:
            lines.append(f"- {item}")
        lines.append("")

    # Related resources
    if parsed["related"]:
        lines.append("## 相关资源")
        lines.append("")
        for item in parsed["related"]:
            lines.append(f"- {item}")
        lines.append("")

    # Expansion areas
    if parsed["expansion"]:
        lines.append("## 扩展空间")
        lines.append("")
        for item in parsed["expansion"]:
            lines.append(item)
        lines.append("")

    # See Also
    lines.append("## See Also")
    lines.append("")
    for other_slug, other_name in see_also:
        lines.append(f"- [{other_name}](../{other_slug}.md) — 相关行业 AI Agent 应用")
    # Add capability cross-refs
    lines.append("- [Agent 框架](../../capability/agent-framework.md) — 行业 Agent 的底层框架")
    lines.append("- [编码 Agent](../../capability/coding-agent.md) — AI 编程助手")
    lines.append("")

    # Source
    lines.append("## 来源")
    lines.append("")
    lines.append(f"- kb/industry/{slug}.md")
    lines.append("")

    # Update history
    lines.append("## 更新历史")
    lines.append("")
    lines.append("- 2026-06-12 初始编译，从 kb/industry 提炼")
    lines.append("")

    return "\n".join(lines)


# Compile each file
compiled = []
for filename in to_compile:
    slug = filename.replace(".md", "")
    filepath = os.path.join(KB_DIR, filename)
    print(f"\nCompiling: {filename}")

    try:
        parsed = parse_kb_content(filepath)
        wiki_content = compile_wiki_article(parsed, slug, slug_to_name)

        outpath = os.path.join(WIKI_DIR, filename)
        with open(outpath, "w") as f:
            f.write(wiki_content)

        compiled.append(filename)
        print(f"  ✓ {filename} -> wiki/industry/{filename}")
    except Exception as e:
        print(f"  ✗ {filename}: {e}")
        import traceback
        traceback.print_exc()

print(f"\n{'='*60}")
print(f"Compiled {len(compiled)}/{len(to_compile)} files successfully")
print(f"Total wiki/industry articles: {len(EXISTING) + len(compiled)}")
