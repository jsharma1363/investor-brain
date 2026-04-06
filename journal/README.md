# Journal

Personal investing wiki. Persistent context for conversations that use the investor-brain skill.

**This is NOT a source for the skill.** It never feeds back into `references/` or `SKILL.md`.

## How to Update: Skill vs. Journal

There are two completely separate update paths. The trigger language determines which one runs.

### Update the Skill (changes how it thinks)

**Triggers:** "put this into the skill", "capture this source", "add this to the references",
"integrate this into the skill", "update the skill with this"

**What happens:**
1. New material goes into `sources/` (PDFs, books, videos, tweets)
2. A reference file is created or updated in `references/` (distilled markdown)
3. `SKILL.md` is updated if new reasoning steps or frameworks are needed
4. Version bump on SKILL.md

**What changes:** The skill's frameworks. How it reasons. Permanent, structural.

### Update the Journal (saves what you're thinking)

**Triggers:** "save this", "log this", "update the journal", "write this down",
"update the META file", "save this thesis", or accepting the end-of-conversation
offer: "Want me to update the journal?"

**What happens:**
1. Relevant journal files are created or updated (companies, thinking, concepts, etc.)
2. Cross-links are added to connect related entries
3. `index.md` and `log.md` are updated

**What changes:** Your personal context. What you think about specific companies, concepts,
and positions. Accumulating, opinionated, dated.

### Default Behavior

**Everything goes to the journal unless explicitly stated otherwise.** Only "put this into
the skill" / "update the skill" / "add to references" triggers the skill update pipeline.
Tweets, articles, theses, opinions, analysis outputs — all journal by default.

## Structure

- `index.md` — Content catalog mapping concepts to where they live across all files
- `log.md` — Append-only chronological record of what was added/updated and when
- `companies/` — Living theses per company (e.g., META.md). Updated each session.
- `thinking/` — Dated entries on evolving investment philosophy, framework debates, synthesis.
- `positions/` — Active position tracking: entry rationale, sizing, forward returns, sell criteria.
- `people/` — Thinkers, investors, operators worth tracking (e.g., Enright.md, Karpathy.md).
- `concepts/` — Cross-cutting ideas that span companies and thinkers (e.g., duration.md, lollapalooza.md).
- `sources-index/` — Index of books, videos, tweets, and articles with links and key takeaways.

## Rules

1. The skill reads the journal for context. The journal never modifies the skill.
2. Only `sources/` feeds into `references/` and `SKILL.md` (manual, deliberate updates).
3. Journal entries are the user's evolving thinking — opinionated, dated, accumulating.
4. Newer entries take precedence over older ones when views conflict.
5. Each company file has a "last updated" date and a "current view" section at the top.
6. The assistant offers to update the journal at the end of substantive conversations. The user decides.

## Operations

### Ingest
When new source material arrives (book, transcript, article, tweet), the skill reads it,
distills it through the investing frameworks, creates/updates relevant journal entries,
updates the index, and appends to the log. A single source may touch 5-10 journal files.

### Query → File Back
When a conversation produces a valuable analysis (forward returns comparison, thesis update,
framework synthesis), **file it back into the journal.** Good answers shouldn't disappear
into chat history. They become `thinking/` entries, `companies/` updates, or `concepts/`
pages. The journal compounds from conversations, not just from ingested sources.

### Lint
Periodically health-check the journal:
- **Contradictions** — do any entries conflict with each other? (e.g., a bull thesis on META
  in one place and bearish assumptions in another)
- **Stale entries** — has new data superseded an old claim? Check "last updated" dates.
- **Orphan pages** — any entries with zero inbound links? They're invisible to navigation.
- **Missing pages** — concepts mentioned in `[[wiki links]]` that don't have their own entry yet.
- **Gaps** — companies in the portfolio without theses, people referenced without entries.

To run a lint: "lint the journal" or "health check the wiki."

## Log Format

Use a consistent, parseable format so `log.md` is greppable:

```
## [2026-04-05] ingest | CS153 Anjney Midha lecture
- Created `people/anjney-midha.md`
- Added transcript to `sources-index/`
- Updated [[META]] thesis with capex validation
```

Prefix: `## [YYYY-MM-DD] verb | short title`
Verbs: `ingest`, `update`, `query`, `lint`, `create`

## Wiki Link Rules

This journal is designed to work as a graph (e.g., Obsidian). Links must be clean for traversal.

1. **Use `[[wiki links]]` for all cross-references.** Every entry should link to related entries.
2. **Keep link text pithy.** Use the shortest unambiguous name: `[[META]]` not `[[META Platforms Inc.]]`, `[[Enright]]` not `[[Paul Enright's three-path alpha framework]]`, `[[duration]]` not `[[duration as an investing concept]]`.
3. **Link names must match filenames (without extension).** `[[Enright]]` → `people/enright.md`, `[[META]]` → `companies/META.md`, `[[duration]]` → `concepts/duration.md`.
4. **Every entry must have a `## Links` section at the bottom** with a flat list of related wiki links. No descriptions — just the links. Descriptions belong in the body text, not the link list.
   ```
   ## Links
   - [[META]]
   - [[duration]]
   - [[Enright]]
   ```
5. **Limit links to direct relationships.** Don't link everything to everything. If A relates to B and B relates to C, A doesn't need to link to C unless there's a direct connection.
6. **Use consistent casing.** Tickers uppercase (`[[META]]`, `[[GOOG]]`). People capitalized (`[[Enright]]`). Concepts lowercase (`[[duration]]`, `[[lollapalooza]]`).
7. **Index entries are one line each.** `- [[Enright]] — duration taxonomy, three-path alpha.` Keep it under 100 characters.
