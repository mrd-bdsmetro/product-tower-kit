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

# Market Research — T0

## Goal
Thu thập data thị trường cho product. 3 modes: Express, Pro, Valyu.

## Target Audiences
- **Vibe coders** — Developers using AI coding tools (Claude Code, Cursor, Copilot)
- **Startup founders** — Solo or small team founders validating ideas
- **Freelancers** — PM consultants using frameworks for client work
- **Agencies** — Dev shops using templates for projects
- **Vietnamese founders** — Vietnamese-first PM framework

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

**Khi nào dùng:** Muốn data chất lượng cao, sẵn sàng đầu tư thời gian.

### Steps:
1. Copy mega prompt từ `references/mega-prompt.md`
2. Thay [PLACEHOLDER] → paste vào Google Deep Research
3. Đợi 2-10 phút → save output
4. Nói: "parse deep research [file path]"
5. AI extract → fill T0-T6

**Output:** `data/t0_market_research.md`
**Confidence:** 📊 80%
**PMF Penalty:** -1.0

---

## MODE 3: VALYU (API Search) ⭐ NEW

**Khi nào dùng:** Muốn data chất lượng cao, nhanh, có proprietary content.

### Setup:
```bash
pip install valyu
export VALYU_API_KEY=your_key  # Get from https://valyu.ai
```

### Usage:
```bash
# Web search (fast, broad)
python scripts/valyu_search.py "Vietnam SaaS market size 2025" --mode web

# Deep search (full content extraction)
python scripts/valyu_search.py "product-market fit framework" --mode deep

# Academic search (papers, filings, patents)
python scripts/valyu_search.py "startup validation methodology" --mode academic
```

### In Claude Code:
```
"valyu search Vietnam SaaS market"
"deep search product-market fit"
"academic search startup validation"
```

**Output:** `data/t0_market_research.md` + `data/search_*.md`
**Confidence:** 📊 75-80%
**PMF Penalty:** -1.0

### Valyu Modes:

| Mode | Use Case | Content | Speed |
|------|----------|---------|-------|
| `web` | General market data | Web pages, news | Fast |
| `deep` | Full content extraction | Complete articles | Medium |
| `academic` | Research papers | Papers, filings, patents | Slow |

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
# T0: Market Research — [Project]

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
- [Source 1](url) — type: web/deep/academic
- [Source 2](url) — type: web/deep/academic
```

---

## MODE COMPARISON

| Mode | Confidence | Speed | Cost | Best For |
|------|------------|-------|------|----------|
| Express | 🤖 60% | Fast | Free | Quick validation |
| Pro | 📊 80% | Slow | Free | Deep research |
| Valyu | 📊 75-80% | Fast | $$ | Production research |

**Recommendation:** Start with Express, upgrade to Valyu for production.
