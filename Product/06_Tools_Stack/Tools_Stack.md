---
status: active
type: tooling
owner: MR.D
last_updated: 2026-05-12
tags: [tools, stack, notion, obsidian, github, vercel]
pmf_impact: medium
---

# Tools Stack Overview

## Overview
Product Kit uses a "Best of Breed" approach to tooling, selecting tools based on their strength in specific layers rather than trying to use one tool for everything.

## Tool-Layer Mapping

| Layer | Primary Tool | Alternative | Purpose |
|-------|-------------|-------------|---------|
| **Execution** | Notion | Spreadsheet | Real-time tracking, accountability |
| **Framework** | Obsidian | Notion | Markdown notes, graph view |
| **Instance** | GitHub | — | Version control, collaboration |
| **Design System** | VS Code | — | TypeScript, components |
| **Publish** | Vercel | Netlify | Static site hosting |

## Tool Selection Criteria

| Tool | Strengths | Weaknesses | Best For |
|------|-----------|------------|----------|
| **Notion** | Database, API, collaboration | Slow for large docs | Execution Layer, tracking |
| **Obsidian** | Fast, local, graph view | No collaboration | Framework Layer, thinking |
| **GitHub** | Version control, issues | Learning curve | Instance Layer, plans |
| **Vercel** | Fast deploy, preview | No backend | Static sites, docs |
| **VS Code** | Extensions, flexibility | Heavy | All development |

## Integration Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  NOTION (Execution Layer)                                    │
│  - validation_tracker                                        │
│  - decision_log                                              │
│  - risk_register                                             │
│  - weekly_checkpoint                                         │
│  API: Notion API → Webhooks → GitHub Actions                │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  OBSIDIAN (Framework Layer)                                  │
│  - Product_Plan_Template                                     │
│  - ecosystem-map                                             │
│  - learnings                                                 │
│  Sync: Obsidian Sync / iCloud                               │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  GITHUB (Instance + Archive)                                  │
│  - T_Series, AB_Series                                       │
│  - plans/                                                    │
│  - docs/                                                     │
│  Sync: GitHub Desktop / CLI                                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  VERCEL (Publish)                                            │
│  - public/llms.txt                                           │
│  - docs/                                                     │
│  Auto-deploy on push to master                              │
└─────────────────────────────────────────────────────────────┘
```

## Setup Instructions

### Notion
1. Create workspace
2. Duplicate [Product Kit Template](https://notion.so)
3. Connect API key to `.env`

### Obsidian
1. Install Obsidian
2. Clone Framework Layer folder
3. Enable sync plugin

### GitHub
1. Fork repository
2. Clone locally
3. Configure GitHub Desktop

### Vercel
1. Import repository
2. Configure root directory to `Product/public`
3. Deploy

---
*Tools Stack v1.6.0*