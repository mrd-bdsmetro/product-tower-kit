---
status: active
type: entry
owner: MR.D
last_updated: 2026-05-12
tags: [summary, overview, executive]
---

# Executive Summary

## Product Tower Kit v1.5.0

**Purpose:** Validate product ideas before building. For solo founders and small teams.

## What It Does

| Capability | Description |
|------------|-------------|
| **Market Research** | 5 search providers (Brave, Firecrawl, Valyu, DuckDuckGo, Exa) |
| **Validation Framework** | 14-phase T0-T9.5 pipeline with gates |
| **Anti-Bias System** | 6-challenge AB series to stress-test assumptions |
| **PMF Scoring** | Quantitative validation with threshold gates |
| **CLI Tool** | `product-tower` command for automation |

## Architecture (7 Layers)

```
00_Entry_Point      ← Quick start, index, changelog
01_Framework_Layer   ← Reusable templates (copy for new idea)
02_Instance_Layer    ← ONYX-specific data (T0-T13, AB1-AB6)
03_Execution_Layer   ← Trackers, logs, decisions
04_Learning_Layer    ← Lessons learned, retrospectives
05_Design_System     ← UI components (21 skills)
06_Assets           ← Templates, scripts, diagrams
07_Archive          ← Version backups
```

## Current Status: ONYX Validation

- **Product:** ONYX (B2B SaaS for real estate market analysis)
- **Phase:** T7 (PMF Validation)
- **Score:** 7.2/10 (above threshold)
- **Last Updated:** 2026-05-12

## Tech Stack

- **CLI:** Node.js 18+, npm
- **Scripts:** Python 3.8+
- **Automation:** PowerShell harness scripts
- **Storage:** Markdown files + JSON state

## Key Metrics

| Metric | Value |
|--------|-------|
| Files | 40+ markdown files |
| Skills | 21 specialized skills |
| Agents | 8 AI agents |
| Gates | 3 automated checkpoints |

## Repository

https://github.com/mrd-bdsmetro/product-tower-kit

---
*Built by MR.D — Validate before you build*