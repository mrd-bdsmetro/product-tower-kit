---
status: active
type: architecture
owner: MR.D
last_updated: 2026-05-12
tags: [architecture, tower, pmf, validation]
pmf_impact: high
---

# Product Kit Tower

## Overview
Product Kit Tower maps the Product Management Tower framework to the Product Tower Kit structure, providing a 12-layer architecture for validating product ideas from market research to deployment.

## 12-Layer Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 12: TARGET MARKET          ← Who is this kit for?       │
│  ─────────────────────────────────────────────────────────────  │
│  Entry: Solo founders, ADHD brain, early-stage VN market        │
│  File: 00_Entry_Point/Target_Market.md                         │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 11: SEGMENTATION           ← Which market segments?      │
│  ─────────────────────────────────────────────────────────────  │
│  Segments: Solo founder, Early-stage startup, Indie hacker      │
│  File: 00_Entry_Point/Segmentation.md                          │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 10: VALUE PROPOSITION     ← Why is this kit different?  │
│  ─────────────────────────────────────────────────────────────  │
│  Core Value: "Biến analysis thành evidence + execution"         │
│  File: 00_Entry_Point/Value_Proposition.md                     │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 9: PMF DEFINITION         ← When is PMF achieved?        │
│  ─────────────────────────────────────────────────────────────  │
│  Threshold: PMF score ≥ 30/50 in 60 days                       │
│  File: 00_Entry_Point/PMF_Definition.md                        │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 8: EXECUTION LAYER        ← Underserved Needs (GOLD)    │
│  ─────────────────────────────────────────────────────────────  │
│  - decision_log.md         (Why we chose X over Y)              │
│  - risk_register.md        (All risks + mitigation)             │
│  - validation_tracker.md   (Real-time PMF tracker)             │
│  - weekly_checkpoint.md    (Accountability ritual)             │
│  - cofounder_search.md     (Team building)                      │
│  Files: 03_Execution_Layer/*                                    │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 7: INSTANCE LAYER         ← Product-specific data       │
│  ─────────────────────────────────────────────────────────────  │
│  - T_Series/  (T0-T13, T_Minus1)                              │
│  - AB_Series/ (AB1-AB6 anti-bias challenges)                   │
│  - execution/pipeline_state.json                               │
│  Files: 02_Instance_Layer/*                                     │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 6: FRAMEWORK LAYER        ← Reusable templates          │
│  ─────────────────────────────────────────────────────────────  │
│  - ecosystem-map.md            (Ecosystem overview)             │
│  - Product_Plan_Template.md    (Plan template)                 │
│  Files: 01_Framework_Layer/*                                   │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 5: LEARNING LAYER         ← Feedback Loop               │
│  ─────────────────────────────────────────────────────────────  │
│  - lessons_learned.md          (Key insights)                  │
│  - iteration_notes.md          (Iteration tracking)            │
│  - post_mortem_template.md     (Retrospective)                 │
│  - stakeholder_feedback.md     (Co-founder, investor, KOC)     │
│  Files: 04_Learning_Layer/*                                   │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 4: ENTRY POINT            ← Quick Start + Navigation    │
│  ─────────────────────────────────────────────────────────────  │
│  - INDEX.md                     (Main entry)                    │
│  - Quick_Start_Guide.md         (15-min setup)                 │
│  - Executive_Summary.md         (1-page overview)               │
│  - CHANGELOG.md                 (Version history)              │
│  Files: 00_Entry_Point/*                                      │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: VALIDATION FUNNEL      ← Customer Journey            │
│  ─────────────────────────────────────────────────────────────  │
│  Idea → Coffee Talk → Deal → Active → PMF Re-score             │
│  File: Validation_Funnel.md                                    │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: DESIGN SYSTEM         ← UI Components                │
│  ─────────────────────────────────────────────────────────────  │
│  - TypeScript tokens + components                              │
│  - 21 skills with SKILL.md                                     │
│  Files: .claude/skills/*                                       │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 1: TOOLS STACK             ← Technical Feasibility       │
│  ─────────────────────────────────────────────────────────────  │
│  - Notion (Execution)                                          │
│  - Obsidian (Framework)                                        │
│  - GitHub (Version control)                                    │
│  - Vercel (Publish)                                            │
│  Files: 06_Tools_Stack/*                                      │
└─────────────────────────────────────────────────────────────────┘
```

## File-to-Layer Mapping

| Layer | Files | Count |
|-------|-------|-------|
| 12: Target Market | `00_Entry_Point/Target_Market.md` | 1 |
| 11: Segmentation | `00_Entry_Point/Segmentation.md` | 1 |
| 10: Value Proposition | `00_Entry_Point/Value_Proposition.md` | 1 |
| 9: PMF Definition | `00_Entry_Point/PMF_Definition.md` | 1 |
| 8: Execution Layer | `03_Execution_Layer/*.md` | 5 |
| 7: Instance Layer | `02_Instance_Layer/T_Series/*.md`, `02_Instance_Layer/AB_Series/*.md` | 20 |
| 6: Framework Layer | `01_Framework_Layer/*.md` | 2 |
| 5: Learning Layer | `04_Learning_Layer/*.md` | 4 |
| 4: Entry Point | `00_Entry_Point/{INDEX,Quick_Start,Executive_Summary,CHANGELOG}.md` | 4 |
| 3: Validation Funnel | `Validation_Funnel.md` | 1 |
| 2: Design System | `.claude/skills/*/SKILL.md` | 21 |
| 1: Tools Stack | `06_Tools_Stack/*.md` | 3 |

**Total: 65+ files across 12 layers**

## PMF Score Calculation

For the kit itself:

| Metric | Target | Current |
|--------|--------|---------|
| PMF Score | ≥ 30/50 | TBD |
| Time to PMF | 60 days | — |
| Founders using kit | 10 | 1 (MR.D) |
| Active users | 5 | 0 |

## Dependencies

```
Target Market → Segmentation → Personas → Needs → PMF
     ↓              ↓             ↓         ↓        ↓
 Layer 12      Layer 11     Layer 10   Layer 9   Layer 8
     ↓              ↓             ↓         ↓        ↓
 Entry Point → Framework → Instance → Execution → Learning
 Layer 4         Layer 6    Layer 7   Layer 8     Layer 5
```

## Usage

1. **New Product**: Copy `01_Framework_Layer/` + `00_Entry_Point/` to new folder
2. **Track Progress**: Use `03_Execution_Layer/validation_tracker.md`
3. **Learn**: Review `04_Learning_Layer/lessons_learned.md` after each iteration

---
*Product Kit Tower v1.6.0 — Based on Product Management Tower framework*