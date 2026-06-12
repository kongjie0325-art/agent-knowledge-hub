---
name: agent-knowledge-hub
description: "Use when building or maintaining the Agent Knowledge Hub. Triggers: ingesting sources into raw/, compiling wiki/ articles, querying wiki knowledge, linting wiki quality, 'add to hub', 'what do I know about', or any mention of 'knowledge hub', 'wiki', 'raw/', or 'ingest'."
---

# Agent Knowledge Hub

Build and maintain a personal AI Agent knowledge base using LLMs. You manage four directories: `raw/` (immutable source material), `wiki/` (compiled knowledge articles), `references/` (templates), and `examples/` (example articles). Sources go into raw/, you compile them into wiki articles, and the wiki compounds over time.

Core ideas from Karpathy LLM Wiki:
- "The LLM writes and maintains the wiki; the human reads and asks questions."
- "The wiki is a persistent, compounding artifact."

## Architecture

Four layers, all under the Hub root (`/home/ubuntu/agent-knowledge-hub/`):

**raw/** — Immutable source material index. You read, never modify. Organized by topic subdirectories:
- `raw/capability/` — Source indices for capability articles
- `raw/industry/` — Source indices for industry articles

**wiki/** — Compiled knowledge articles. You have full ownership. Organized by topic subdirectories:
- `wiki/capability/` — Capability articles (agent-framework, coding-agent, etc.)
- `wiki/industry/` — Industry articles (healthcare, finance, etc.)
- `wiki/index.md` — Global index. One row per article, grouped by topic, with link + summary + Updated date.
- `wiki/log.md` — Append-only operation log.

**references/** — Templates for raw files, articles, index, and archive pages.

**examples/** — Example articles showing what compiled knowledge articles should look like.

**kb/** — Existing knowledge base (preserved, not modified by this workflow).

Templates live in `references/` relative to this file. Read them when you need the exact format.

---

## Ingest

Fetch a source into raw/, then compile it into wiki/. Always both steps, no exceptions.

### Fetch (raw/)

1. Get the source content using web or file tools. If nothing can reach the source, ask the user to paste it directly.

2. Pick a topic directory. Check existing `raw/` subdirectories first; reuse one if the topic is close enough.

3. Save as `raw/<topic>/YYYY-MM-DD-descriptive-slug.md`.
   - Slug from source title, kebab-case, max 60 characters.
   - Include metadata header: source URL, collected date, published date.
   - Preserve original text. Clean formatting noise. Do not rewrite opinions.

   See `references/raw-template.md` for the exact format.

### Compile (wiki/)

Determine where the new content belongs:

- **Same core thesis as existing article** → Merge into that article. Add the new source to Sources/Raw. Update affected sections.
- **New concept** → Create a new article in the most relevant topic directory.
- **Spans multiple topics** → Place in the most relevant directory. Add See Also cross-references.

Check for factual conflicts: if the new source contradicts existing content, annotate the disagreement with source attribution.

See `references/article-template.md` for article format. Key points:
- Sources field: author/organization + date, semicolon-separated.
- Raw field: markdown links to raw/ files, semicolon-separated.
- Relative paths from `wiki/<topic>/` use `../../raw/<topic>/<file>.md`.

### Cascade Updates

After the primary article, check for ripple effects:

1. Scan articles in the same topic directory for content affected by the new source.
2. Scan `wiki/index.md` entries in other topics for articles covering related concepts.
3. Update every article whose content is materially affected. Each updated file gets its Updated date refreshed.

### Post-Ingest

Update `wiki/index.md`: add or update entries for every touched article.

Append to `wiki/log.md`:

```
## [YYYY-MM-DD] ingest | <primary article title>
- Updated: <cascade-updated article title>
```

---

## Query

Search the wiki and answer questions. Examples of triggers:
- "What do I know about X?"
- "Summarize everything related to Y"
- "Compare A and B based on my knowledge hub"

### Steps

1. Read `wiki/index.md` to locate relevant articles.
2. Read those articles and synthesize an answer.
3. Prefer wiki content over your own training knowledge. Cite sources with relative links.
4. Output the answer in the conversation. Do not write files unless asked.

### Archiving

When the user explicitly asks to archive or save the answer to the wiki:

1. Write the answer as a new wiki page. See `references/archive-template.md`.
2. Always create a new page. Never merge into existing articles.
3. Update `wiki/index.md`. Prefix the Summary with `[Archived]`.
4. Append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] query | Archived: <page title>
   ```

---

## Lint

Quality checks on the wiki. Two categories with different authority levels.

### Deterministic Checks (auto-fix)

**Index consistency** — compare `wiki/index.md` against actual wiki/ files:
- File exists but missing from index → add entry with `(no summary)` placeholder.
- Index entry points to nonexistent file → mark as `[MISSING]`.

**Internal links** — for every markdown link in wiki/ article files:
- Target does not exist → search wiki/ for a file with the same name elsewhere.
  - Exactly one match → fix the path.
  - Zero or multiple matches → report to the user.

**Raw references** — every link in a Raw field must point to an existing raw/ file:
- Target does not exist → search raw/ for a file with the same name elsewhere.
  - Exactly one match → fix the path.
  - Zero or multiple matches → report to the user.

**See Also** — within each topic directory:
- Add obviously missing cross-references between related articles.
- Remove links to deleted files.

### Heuristic Checks (report only)

- Factual contradictions across articles
- Outdated claims superseded by newer sources
- Missing conflict annotations where sources disagree
- Orphan pages with no inbound links from other wiki articles
- Missing cross-topic references

### Post-Lint

Append to `wiki/log.md`:

```
## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed
```

---

## Conventions

- Standard markdown with relative links throughout.
- wiki/ supports one level of topic subdirectories only. No deeper nesting.
- Today's date for log entries, Collected dates, and Archived dates. Updated dates reflect when the article's knowledge content last changed.
- Inside wiki/ files, all markdown links use paths relative to the current file. In conversation output, use project-root-relative paths (e.g., `wiki/capability/agent-framework.md`).
- Ingest updates both `wiki/index.md` and `wiki/log.md`. Archive (from Query) updates both. Lint updates `wiki/log.md` (and `wiki/index.md` only when auto-fixing index entries). Plain queries do not write any files.
- kb/ directory is preserved and not modified by this workflow.
