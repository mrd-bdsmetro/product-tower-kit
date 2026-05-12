---
title: "Product Tower Kit Architecture Restructure"
status: "in-progress"
priority: P1
phases:
  - id: "1"
    title: "Analyze Current Structure"
    status: "in-progress"
  - id: "2"
    title: "Design New Architecture"
    status: "pending"
  - id: "3"
    title: "Implement New Structure"
    status: "pending"
  - id: "4"
    title: "Verify & Commit"
    status: "pending"
created: 2026-05-12
updated: 2026-05-12
---

# Product Tower Kit Architecture Restructure

## Problem Statement
Current flat file structure (22+ files in `data/`) lacks clear layering, making it difficult to navigate, maintain, and reuse framework components for new product ideas.

## Target Architecture

```
Produc_tower_final/
├── 00_Entry_Point/           # Quick start, index, changelog
├── 01_Framework_Layer/       # Reusable templates (copy for new idea)
├── 02_Instance_Layer/        # ONYX-specific data (T0-T13, AB1-AB6)
├── 03_Execution_Layer/       # Trackers, logs, decisions
├── 04_Learning_Layer/        # Lessons learned, retros
├── 05_Design_System/          # UI components (existing)
├── 06_Assets/                # Templates, diagrams
├── 07_Archive/               # Old versions backup
├── .claude/                   # Agents, skills, hooks
├── bin/                       # CLI entry point
├── docs/                      # Technical docs
├── scripts/                   # Automation scripts
├── templates/                 # Product plan templates
└── public/                    # LLM metadata
```

## Scope

### Phase 1: Analyze (DONE at context gathering)
- Map current file inventory
- Classify: Framework vs Instance vs Execution vs Learning
- Identify dependencies

### Phase 2: Design
- Create new folder structure
- Define frontmatter standard
- Plan migration mapping

### Phase 3: Implement
- Create directories
- Move files to appropriate layers
- Generate new files (Executive_Summary, Quick_Start, etc.)
- Add frontmatter to all markdown files

### Phase 4: Verify
- Test CLI still works
- Verify all links intact
- Commit & push

## Success Criteria
- [ ] All files moved to correct layers
- [ ] New entry points created (INDEX.md, Quick_Start_Guide.md)
- [ ] Frontmatter added to all markdown files
- [ ] CLI commands functional
- [ ] Git clean (all changes committed)