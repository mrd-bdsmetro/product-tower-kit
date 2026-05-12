---
phase: "3"
title: "Implement New Structure"
status: "pending"
priority: P1
effort: "2h"
dependencies: ["2"]
---

# Phase 3: Implement New Structure

## Steps

### 3.1 Create Directory Structure
```powershell
New-Item -ItemType Directory -Path "00_Entry_Point"
New-Item -ItemType Directory -Path "01_Framework_Layer"
New-Item -ItemType Directory -Path "02_Instance_Layer/T_Series"
New-Item -ItemType Directory -Path "02_Instance_Layer/AB_Series"
New-Item -ItemType Directory -Path "02_Instance_Layer/execution"
New-Item -ItemType Directory -Path "03_Execution_Layer"
New-Item -ItemType Directory -Path "04_Learning_Layer"
New-Item -ItemType Directory -Path "06_Assets/templates"
New-Item -ItemType Directory -Path "06_Assets/interview_scripts"
New-Item -ItemType Directory -Path "06_Assets/pitch_deck"
New-Item -ItemType Directory -Path "06_Assets/diagrams"
New-Item -ItemType Directory -Path "07_Archive/v1.4_backup"
```

### 3.2 Move Files

**Framework Layer:**
- `resources/ecosystem-map.md` → `01_Framework_Layer/`
- `templates/product-plan.md` → `01_Framework_Layer/Product_Plan_Template.md`

**Instance Layer (T-Series):**
- `data/t_*.md` → `02_Instance_Layer/T_Series/`
- `data/t0*.md` → `02_Instance_Layer/T_Series/`
- `data/t[1-9]*.md` → `02_Instance_Layer/T_Series/`
- `data/t9_5*.md` → `02_Instance_Layer/T_Series/`

**Instance Layer (AB-Series):**
- `data/ab*.md` → `02_Instance_Layer/AB_Series/`

**Instance Layer (Execution):**
- `data/pipeline_state.json` → `02_Instance_Layer/execution/`

**Entry Point:**
- `CHANGELOG.md` → `00_Entry_Point/`

### 3.3 Generate New Files

**00_Entry_Point/INDEX.md** - Main entry point linking all layers
**00_Entry_Point/Quick_Start_Guide.md** - 15-minute setup guide
**00_Entry_Point/Executive_Summary.md** - 1-page overview

**03_Execution_Layer/decision_log.md** - Decision tracking
**03_Execution_Layer/risk_register.md** - Risk tracking
**03_Execution_Layer/cofounder_search.md** - Cofounder notes
**03_Execution_Layer/weekly_checkpoint.md** - Weekly review

**04_Learning_Layer/lessons_learned.md** - Learnings
**04_Learning_Layer/post_mortem_template.md** - Retrospective template
**04_Learning_Layer/iteration_notes.md** - Iteration tracking

### 3.4 Add Frontmatter
Add standard frontmatter to all markdown files in:
- `01_Framework_Layer/`
- `02_Instance_Layer/T_Series/`
- `02_Instance_Layer/AB_Series/`

## Success Criteria
- [ ] All directories created
- [ ] All files moved to correct layer
- [ ] New files generated with content
- [ ] Frontmatter added