---
phase: "2"
title: "Design New Architecture"
status: "pending"
priority: P1
effort: "1h"
dependencies: ["1"]
---

# Phase 2: Design New Architecture

## Target Structure

```
Produc_tower_final/
├── 00_Entry_Point/
│   ├── INDEX.md                    # Main entry
│   ├── Quick_Start_Guide.md        # 15-min setup
│   ├── Executive_Summary.md       # 1-page overview
│   └── CHANGELOG.md               # (existing - move here)
├── 01_Framework_Layer/
│   ├── Product_Validation_Framework.md
│   ├── PMF_Scoring_System.md
│   ├── Anti_Bias_Method.md
│   ├── Segmentation_Framework.md
│   ├── User_Story_Template.md
│   └── ecosystem-map.md            # (from resources/)
├── 02_Instance_Layer/
│   ├── T_Series/                  # T0-T13, T_Minus1
│   ├── AB_Series/                 # AB1-AB6
│   └── execution/
│       └── pipeline_state.json
├── 03_Execution_Layer/
│   ├── validation_tracker.md
│   ├── decision_log.md
│   ├── risk_register.md
│   ├── cofounder_search.md
│   └── weekly_checkpoint.md
├── 04_Learning_Layer/
│   ├── lessons_learned.md
│   ├── post_mortem_template.md
│   └── iteration_notes.md
├── 05_Design_System/              # (keep .claude/skills/)
├── 06_Assets/
│   ├── templates/                  # (existing templates/)
│   ├── interview_scripts/
│   ├── pitch_deck/
│   └── diagrams/
├── 07_Archive/
│   └── v1.4_backup/               # Before restructure
├── bin/
├── data/                           # Search results (flatten)
├── docs/
├── public/
├── scripts/
├── .claude/
└── README.md
```

## Migration Map
| Old Location | New Location | Notes |
|--------------|--------------|-------|
| `data/t*.md` | `02_Instance_Layer/T_Series/` | |
| `data/ab*.md` | `02_Instance_Layer/AB_Series/` | |
| `data/search_*.md` | `data/` | Flatten, keep as-is |
| `resources/ecosystem-map.md` | `01_Framework_Layer/` | |
| `templates/product-plan.md` | `01_Framework_Layer/` | Rename to Product_Plan_Template.md |
| `CHANGELOG.md` | `00_Entry_Point/` | |

## Frontmatter Standard
```yaml
---
status: active | archived
type: framework | instance | execution | learning
owner: MR.D
last_updated: 2026-05-12
tags: [pmf, validation, ...]
---
```

## Implementation Order
1. Create folders
2. Move framework files
3. Move instance files
4. Generate new files
5. Add frontmatter