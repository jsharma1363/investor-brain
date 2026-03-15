# Investor Brain

A Claude Code skill that thinks like Buffett and Munger.

Distilled from 60 years of Berkshire Hathaway shareholder letters, annual meeting transcripts, and *Poor Charlie's Almanack* into ~59KB of structured reference material.

## What it does

Type `/investor` followed by any investing question:

```
/investor analyze Costco's moat
/investor what would Munger say about this SPAC?
/investor evaluate Apple's capital allocation
/investor is this 10-K a red flag?
```

Claude reasons through your question using Buffett and Munger's actual frameworks — not generic investing advice, but specific principles grounded in real letters, real case studies, and real mistakes.

## What's inside

| File | Size | Contents |
|------|------|----------|
| `SKILL.md` | 4.6 KB | How to reason through investment questions |
| `references/principles.md` | 12 KB | Core principles with specific examples from letters |
| `references/mental_models.md` | 10 KB | Munger's latticework + Buffett's decision frameworks |
| `references/checklists.md` | 7.9 KB | Sequential evaluation: gate → quality → management → valuation → risk |
| `references/case_studies.md` | 11 KB | 15 real investments — thesis, outcome, transferable lesson |
| `references/cognitive_biases.md` | 13 KB | Munger's 25 cognitive biases with investing applications |

## Install

```bash
git clone https://github.com/jsharma1363/Jai.git investor-brain
ln -s "$(pwd)/investor-brain" ~/.claude/skills/investor-brain
```

That's it. `/investor` is now available in any Claude Code session.

## How it works

When you invoke `/investor`, Claude Code loads `SKILL.md` + all five reference files into context (~59KB). Claude then reasons through your question using the frameworks, principles, and case studies as its knowledge base.

```
You ask a question
       │
       ▼
SKILL.md tells Claude HOW to think
       │
       ▼
references/ tell Claude WHAT to think with
       │
       ▼
Structured analysis using Buffett/Munger frameworks
```

No API calls, no external services, no internet required. Just markdown files on your machine.

## Improve it

The skill gets smarter as you add material:

1. Drop a PDF (annual report, investor letter, book) into `sources/`
2. Ask Claude to distill it: *"Read this PDF and update the references"*
3. The new principles are available next time you use `/investor`

The `sources/` folder is gitignored — it's your personal working material, not part of the distributed skill.

## Sources

Built from:
- 60 Berkshire Hathaway shareholder letters (1965–2024)
- 33 annual meeting transcripts (1994–2024)
- *Poor Charlie's Almanack* — all talks and essays

## Disclaimer

This is an educational tool, not financial advice. Always do your own research and consult qualified professionals before making investment decisions.
