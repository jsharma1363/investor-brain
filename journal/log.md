# Log

Append-only chronological record of journal changes.
Format: `## [YYYY-MM-DD] verb | short title`

---

## [2026-04-03] create | Journal initialized
- Created `companies/META.md` — Lollapalooza thesis from Cialdini analysis
- Created `thinking/2026-04-03-duration-alpha-and-compounders.md` — Enright framework synthesis
- Created `people/enright.md` — duration taxonomy, three-path alpha
- Created `people/evergreen.md` — moved from `references/mauboussin.md` (opinions → journal)
- Created `concepts/duration.md`
- Created `concepts/lollapalooza.md`

## [2026-04-03] ingest | SEC filings — META
- Pulled 10-K filings into `companies/META/filings/`
- Created `scripts/pull_filings.py`

## [2026-04-04] ingest | SEC filings — GOOG, PM, BN, AMZN
- Pulled 10-K/40-F annual reports (10yr) for all five tickers
- Updated script to auto-detect foreign private issuers (40-F/20-F/6-K)
- Cleaned up: annual reports only, removed amendments

## [2026-04-05] ingest | CS153 Anjney Midha lecture
- Created `people/anjney-midha.md` — compute scarcity, context moats, infrastructure trade
- Added transcript to `sources-index/cs153-anjney-midha-frontier-systems-transcript.md`
- Updated [[META]] thesis: capex validated by Anthropic revenue-compute correlation

## [2026-04-05] update | Skill v3.2.0
- Added "How to process source material" section to SKILL.md
- Added distillation lens, "extract insights not summaries" rule
- Added wiki link rules to journal README
- Added operations (ingest, query→file back, lint) to journal README
- Reformatted log.md to parseable prefix format
