---
name: market-research
version: 1.2.0
description: |
  T0 Market Research skill. 3 modes: Express (AI search), Pro (Deep Research), Valyu (API search).
  Valyu provides real-time web + proprietary content (papers, filings, patents).
  Mega Prompt template for Google Deep Research. Data saturation check.
triggers:
  - "research thị trường"
  - "market research"
  - "thu thập data"
  - "deep research"
  - "market size"
  - "competitor"
  - "valyu"
---

# Market Research - T0

## Goal
Thu thập data thị trường cho product. 3 modes: Express, Pro, Valyu.

## Target Audiences
- **Vibe coders** - Developers using AI coding tools (Claude Code, Cursor, Copilot)
- **Startup founders** - Solo or small team founders validating ideas
- **Freelancers** - PM consultants using frameworks for client work
- **Agencies** - Dev shops using templates for projects
- **Vietnamese founders** - Vietnamese-first PM framework

---

## MODE 1: EXPRESS (AI search)

**Khi nào dùng:** Cần data nhanh, chưa commit full tower.

```
Prompt: "research thị trường [ngành] cho [project]"
```

**Output:** `data/t0_market_research.md`
**Confidence:** 🤖 60%
**PMF Penalty:** -2.0

---

## MODE 2: PRO (Deep Research)

**Khi nao dung:** Muon data chat luong cao, san sang dau tu thoi gian.

### Steps:
1. Copy mega prompt tu `references/mega-prompt.md`
2. Thay [PLACEHOLDER] -> paste vao Google Deep Research
3. Doi 2-10 phut -> save output
4. Noi: "parse deep research [file path]"
5. AI extract -> fill T0-T6

**Output:** `data/t0_market_research.md`
**Confidence:** 80%
**PMF Penalty:** -1.0

---

## MODE 3: WEB SEARCH PROVIDERS

**Khi nao dung:** Muon data nhanh, chinh xac, voi nhieu lua chon.

Unified CLI: `python scripts/web_search.py <provider> <query>`

| Provider | Description | Free | Best For |
|----------|-------------|------|----------|
| **Valyu** | Real-time web + proprietary content | No | Papers, filings, patents |
| **Firecrawl** | Scrape any site -> markdown | No | Full page extraction |
| **Brave Search** | Free web search, no tracking | Yes | Privacy-first research |
| **Tavily** | AI-optimized search | Yes | AI-friendly results |
| **crawl4ai** | AI extraction, Python | Yes | Markdown conversion |

### Setup:

```bash
# Core search tools
pip install valyu
pip install firecrawl-py
pip install brave-search
pip install tavily-python
pip install crawl4ai

# API Keys (export hoac set trong .env)
export VALYU_API_KEY=your_key        # https://valyu.ai
export FIRECRAWL_API_KEY=your_key   # https://firecrawl.dev
export BRAVE_API_KEY=your_key       # https://brave.com/search/api
export TAVILY_API_KEY=your_key      # https://tavily.com
# crawl4ai: FREE, khong can key
```

### Usage:

```bash
# Valyu (web / deep / academic)
python scripts/web_search.py valyu "Vietnam SaaS market" --mode web
python scripts/web_search.py valyu "startup framework" --mode deep
python scripts/web_search.py valyu "product validation" --mode academic

# Firecrawl (scrape / crawl)
python scripts/web_search.py firecrawl "https://example.com" --mode scrape
python scripts/web_search.py firecrawl "https://example.com" --mode crawl

# Brave Search (free)
python scripts/web_search.py brave "market research tools" --num-results 10

# Tavily (basic / advanced)
python scripts/web_search.py tavily "startup tools" --search-depth advanced

# crawl4ai (AI extraction, free)
python scripts/web_search.py crawl4ai "https://example.com" --extract-ai
```

### In Claude Code:

```
"valyu search Vietnam SaaS market"
"firecrawl scrape https://competitor.com"
"brave search startup tools"
"tavily deep research market"
"crawl4ai extract https://site.com"
```

### Provider Modes:

| Provider | Mode | Use Case | Cost |
|----------|------|----------|------|
| Valyu | web | General web data | $$ |
| Valyu | deep | Full content extraction | $$ |
| Valyu | academic | Papers, filings, patents | $$ |
| Firecrawl | scrape | Single page -> markdown | $$ |
| Firecrawl | crawl | Multi-page crawling | $$ |
| Brave | web | General web search | Free |
| Brave | news | News articles | Free |
| Tavily | basic | Quick search | Free tier |
| Tavily | advanced | Deep research | Free tier |
| crawl4ai | scrape | AI markdown extraction | Free |
| crawl4ai | crawl | Batch crawling | Free |

**Output:** `data/t0_market_research.md` + `data/search_*.md`
**Confidence:** 75-85%
**PMF Penalty:** -1.0

---

## MODE 4: VALYU (API Search) [LEGACY]

**Khi nao dung:** Muon data chat luong cao, nhanh, co proprietary content.

### Setup:
```bash
pip install valyu
export VALYU_API_KEY=your_key  # Get from https://valyu.ai
```

### Usage:
```bash
python scripts/valyu_search.py "Vietnam SaaS market" --mode web
```

---

## SATURATION CHECK

Sau mỗi iteration, check 5 signals:

| # | Signal | Test | ✅ Đủ khi |
|---|--------|------|----------|
| 1 | Diminishing Returns | Search thêm 5 query → insight MỚI? | Không mới |
| 2 | Coverage | 7 câu trả lời được? | ≥ 6/7 |
| 3 | Cascade Feed | T1-T3 chạy được? | Solid |
| 4 | Source Diversity | ≥ 4/6 categories? | Pass |
| 5 | Time Box | MAX 2-3 sessions (6-8h) | Quá = paralysis |

---

## OUTPUT FORMAT

```markdown
# T0: Market Research - [Project]

## Market Size
- TAM: $X (source, confidence)
- SAM: $X (source, confidence)
- SOM: $X (source, confidence)

## Competitors
| Name | Size | Strength | Weakness |
|------|------|----------|----------|

## Trends
- Trend 1 (source, confidence)
- Trend 2 (source, confidence)

## Price Data
- Range: $X-$Y (source)

## Regulatory
- Key regulations

## Timing Catalyst
- Why now?

## Sources
- [Source 1](url) - type: web/deep/academic
- [Source 2](url) - type: web/deep/academic
```

---

## MODE COMPARISON

| Mode | Confidence | Speed | Cost | Best For |
|------|------------|-------|------|----------|
| Express | 60% | Fast | Free | Quick validation |
| Pro | 80% | Slow | Free | Deep research |
| Valyu | 75-80% | Fast | $$ | Proprietary content |
| Firecrawl | 80% | Medium | $$ | Full page scrape |
| Brave | 70% | Fast | Free | Privacy-first |
| Tavily | 75% | Fast | Free | AI-optimized results |
| crawl4ai | 85% | Fast | Free | AI markdown extraction |

**Recommendation:** Start with Express, upgrade to crawl4ai/Tavily for production.
