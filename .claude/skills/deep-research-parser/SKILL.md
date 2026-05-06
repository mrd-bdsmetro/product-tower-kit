---
name: deep-research-parser
version: 1.0.0
description: |
  Pre-T0 skill. Parse Deep Research markdown into structured files.
  Generates t0_mindmap.json + pre-fills T1-T6. Gap report.
triggers:
  - "parse deep research"
  - "parse file"
  - "deep research parser"
---

# Deep Research Parser — Pre-T0

## Goal
Parse Deep Research output (from Gemini/Grok/ChatGPT) into structured Product Tower files.

---

## INPUT

Deep Research markdown file (50-100KB, 40+ citations):
- From Google Deep Research, Grok Deep Search, ChatGPT
- Contains: market size, competitors, trends, pricing, regulations

---

## EXTRACTION (7 sections)

| Section | Maps to | Output file |
|---------|---------|-------------|
| Market Size & Growth | T0 | `data/t0_market_research.md` |
| Target Segments | T1-T3 | `data/t1_target_market.md` |
| User Profiles | T4 | `data/t4_personas.md` |
| Needs & Pain Points | T5-T6 | `data/t5_user_needs.md` |
| Competitive Landscape | T0-CP | `data/t0_competitive_map.md` |
| Pricing Data | T9.5 | (for later) |
| Trends & Timing | T0 | (merged) |

---

## GAP REPORT

After parsing, generate gap report:

```markdown
## Gap Report
| Section | Coverage | Missing | Action |
|---------|----------|---------|--------|
| T0 Market | 80% | Pricing details | Search more |
| T1-T3 Segments | 60% | Behavioral data | Interview |
```

---

## USAGE

```
"parse deep research cho [project]"
"parse file [path] cho product tower"
```

**Output:** Pre-fills T0-T6 files
**Confidence:** 📊 80% (vs 🤖 60% without)
**PMF Penalty:** -1.0 (vs -2.0 without)
