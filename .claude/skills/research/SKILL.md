---
name: research
version: 1.1.0
description: |
  Market research methodology. Systematic information gathering for product decisions.
  For T0 market research, competitor analysis, user research.
triggers:
  - "research"
  - "market research"
  - "competitor research"
  - "user research"
  - "thu thập data"
---

# Research — Market & Product

## Goal
Conduct systematic research for product decisions. Max 5 research calls per session.

---

## Phases

### 1. Scope Definition
- What do we need to know?
- Why do we need it?
- What decisions will this inform?

### 2. Information Gathering

**Sources (priority order):**
1. User interviews (👤 90%)
2. Cited reports (📊 80%)
3. Competitor analysis (📊 75%)
4. AI inference (🤖 60%)

**Methods:**
- WebSearch for market data
- Deep Content Analysis for reports
- Competitor website analysis
- User interview quotes

### 3. Analysis & Synthesis
- Cross-reference sources
- Identify patterns
- Score confidence

### 4. Report Generation
- Executive summary
- Key findings
- Comparative analysis
- Recommendations

---

## Output Format

```markdown
# Research: [Topic]

## Executive Summary
[1-2 sentences]

## Key Findings
| Finding | Source | Confidence |
|---------|--------|------------|

## Comparative Analysis
| Dimension | Option A | Option B | Option C |
|-----------|----------|----------|----------|

## Recommendations
1. ...
2. ...

## Sources
- [Source 1](url) — credibility: high/medium/low
- [Source 2](url) — credibility: high/medium/low
```

---

## Confidence Scoring

| Tag | Score | Source |
|-----|-------|--------|
| 🤖 | 60% | AI inference |
| 📊 | 80% | Cited data |
| 👤 | 90% | User interview |
| ✅ | 95% | Validated by usage |

---

## Saturation Check

After each iteration, check 5 signals:
1. Diminishing returns? (new insights?)
2. Coverage? (7 questions answered?)
3. Cascade feed? (T1-T3 can run?)
4. Source diversity? (4+ categories?)
5. Time box? (max 2-3 sessions)
