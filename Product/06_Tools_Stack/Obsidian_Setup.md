---
status: active
type: setup
owner: MR.D
last_updated: 2026-05-12
tags: [obsidian, setup, vault, plugins, workflow]
pmf_impact: low
---

# Obsidian Setup Guide

## Prerequisites

- [Obsidian](https://obsidian.md/download) installed
- Git installed (for version control)
- Node.js 18+ (for Quartz)

## Step 1: Create Vault

### Option A: Open Existing Folder

```bash
# Navigate to Product folder
cd /path/to/product-tower-kit/Product

# Open in Obsidian
# Obsidian → Open folder as vault → Select Product folder
```

### Option B: Clone Fresh

```bash
git clone https://github.com/mrd-bdsmetro/product-tower-kit.git
cd product-tower-kit/Product
# Then open in Obsidian
```

## Step 2: Enable Core Plugins

Open Obsidian → Settings → Core Plugins

| Plugin | Enable | Why |
|--------|--------|-----|
| **Daily Notes** | ✅ | Log weekly checkpoints |
| **Templates** | ✅ | Quick T-tier creation |
| **Graph View** | ✅ | Visualize T-series dependencies |
| **Backlinks** | ✅ | Track file relationships |
| **Search** | ✅ | Find content fast |
| **Command Palette** | ✅ | Quick actions |

## Step 3: Community Plugins (Recommended)

Settings → Community Plugins → Browse

| Plugin | Purpose | Why |
|--------|---------|-----|
| **Templater** | Advanced templates | More flexible than built-in |
| **Minimal Theme** | Clean look | Reduces distraction |
| **Quick Add** | Fast file creation | Speed up workflow |
| **Git** | Version control | Auto-backup to GitHub |

### Install Templater

1. Community Plugins → Search "Templater"
2. Install → Enable
3. Configure template folder: `01_Framework_Layer/templates`

## Step 4: Configure Templater Templates

Create template file: `01_Framework_Layer/templates/t-template.md`

```markdown
---
status: "in-progress"
type: "instance"
owner: "MR.D"
last_updated: "<% tp.date.now() %>"
tags: []
pmf_impact: "medium"
---

# <% tp.file.title %>

## Overview
<% tp.system.clipboard() %>

## Key Findings

-

## Next Steps

- [ ]

## Dependencies
-

## Evidence

-
```

## Step 5: Set Up Git Integration

### Option A: Obsidian Git Plugin

1. Install "Git" community plugin
2. Configure:

```json
{
  "commitMessage": "vault backup: {{date}}",
  "autoCommitInterval": 30,
  "autoPull": true,
  "autoPush": true
}
```

### Option B: External Git

```bash
# Initialize git if not present
cd Product
git init
git remote add origin https://github.com/mrd-bdsmetro/product-tower-kit.git

# Add .gitignore for Obsidian
echo ".obsidian/" >> .gitignore
echo "*.icloud" >> .gitignore

# Commit all
git add -A
git commit -m "Initial Product Kit vault"
git push -u origin master
```

## Step 6: Graph View Organization

Press `Ctrl+G` for Graph View

### Filter by Layer

| Layer | Color | Node |
|-------|-------|------|
| Framework | Blue | `01_Framework_Layer/` |
| Instance (T) | Orange | `02_Instance_Layer/T_Series/` |
| Instance (AB) | Red | `02_Instance_Layer/AB_Series/` |
| Execution | Green | `03_Execution_Layer/` |
| Learning | Purple | `04_Learning_Layer/` |

### Add Links Between T-Tiers

In each T-tier file, add links to dependencies:

```markdown
## Dependencies
- [[T0_Competitive_Map|T0]] - Must complete T0 first
- [[T1_Target_Market|T1]] - Depends on T1
```

## Step 7: Daily Workflow

### Morning

1. Open Obsidian → Product vault
2. Daily Notes (Ctrl+D)
3. Review `03_Execution_Layer/weekly_checkpoint.md`
4. Identify today's priority

### During Work

1. Open current T-tier
2. Add findings under headers
3. Update frontmatter `last_updated`
4. Commit with `Ctrl+P` → "Git: Commit"

### Evening

1. Update weekly_checkpoint.md
2. Push to GitHub: `Ctrl+P` → "Git: Push"
3. Check Quartz published site

## Step 8: Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+G` | Graph view |
| `Ctrl+O` | Quick open |
| `Ctrl+N` | New note |
| `Ctrl+D` | Daily note |
| `Ctrl+P` | Command palette |
| `Ctrl+Shift+F` | Search all files |
| `Ctrl+E` | Toggle edit/preview |
| `Ctrl+,` | Settings |

## Step 9: Search and Find

### Quick Search

```markdown
Press Ctrl+Shift+F

# Search examples:
- "PMF" → All files mentioning PMF
- "T7" → All T7 references
- "tag:pmf" → Files with pmf tag
```

### Tags Panel

Settings → Appearance → Show Tags Panel

Tags help organize:
- `#pmf` - PMF-related files
- `#done` - Completed tiers
- `#wip` - Work in progress

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Vault too slow | Disable unused plugins |
| Graph view messy | Use filter by folder |
| Git plugin not working | Check Git is installed |
| Can't find files | Use Ctrl+O quick open |

---
*Obsidian Setup Guide v1.0.0*