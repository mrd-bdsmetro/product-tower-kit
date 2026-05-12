---
status: active
type: tooling
owner: MR.D
last_updated: 2026-05-12
tags: [tools, stack, obsidian, quartz, github, vercel]
pmf_impact: medium
---

# Tools Stack: Obsidian + Quartz + GitHub

## Overview

Product Kit uses a **local-first, Git-based workflow** with Obsidian for thinking and Quartz for publishing. No cloud lock-in, no Notion dependency.

```
Obsidian (Local) → GitHub (Version) → Quartz (Publish)
     ↓                  ↓                  ↓
  Framework        Instance           Public Site
```

## Tool Stack

| Tool | Role | Why |
|------|------|-----|
| **Obsidian** | Local knowledge base | Fast, local, graph view, no cloud |
| **Quartz** | Static site generator | Hugo-based, GitHub Pages deploy |
| **GitHub** | Version control + hosting | Free, ubiquitous, CI/CD |
| **Vercel** | Alternative hosting | Faster, preview deploys |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  OBSIDIAN (Local)                                            │
│  ──────────────────────────────────────────────────────────  │
│  • Product folder synced locally                            │
│  • Graph view for linking                                   │
│  • Daily notes + T-Series templates                        │
│  • Vault: ~/Product-Kit-Vault/                              │
└─────────────────────────────────────────────────────────────┘
                              ↓ git push
┌─────────────────────────────────────────────────────────────┐
│  GITHUB (Remote + Version Control)                           │
│  ──────────────────────────────────────────────────────────  │
│  • github.com/mrd-bdsmetro/product-tower-kit                │
│  • Branches for experiments                                 │
│  • Issues for tracking                                      │
└─────────────────────────────────────────────────────────────┘
                              ↓ git push / Vercel webhook
┌─────────────────────────────────────────────────────────────┐
│  QUARTZ (Public Site)                                       │
│  ──────────────────────────────────────────────────────────  │
│  • quartz.obsidian.page → deployed site                    │
│  • Automatic build on push                                 │
│  • Full-text search                                         │
│  • Backlinks preserved                                      │
└─────────────────────────────────────────────────────────────┘
```

## Layer-to-Tool Mapping

| Layer | Tool | Location |
|-------|------|----------|
| **Framework** | Obsidian | `01_Framework_Layer/` |
| **Instance** | Obsidian + Git | `02_Instance_Layer/` |
| **Execution** | Obsidian | `03_Execution_Layer/` |
| **Learning** | Obsidian | `04_Learning_Layer/` |
| **Entry Point** | Quartz (published) | `00_Entry_Point/` |
| **Archive** | GitHub | `07_Archive/` |

## Why Obsidian + Quartz?

### Advantages

| Aspect | Notion | Obsidian + Quartz |
|--------|--------|-------------------|
| **Portability** | Locked to Notion | Markdown = forever |
| **Sync** | Cloud required | Local first |
| **Cost** | $8-15/mo | Free (self-hosted) |
| **Speed** | Can be slow | Instant |
| **Privacy** | Data on Notion servers | Your machine |
| **Ownership** | You don't own it | You own everything |

### Disadvantages

| Aspect | Obsidian + Quartz | Mitigation |
|--------|-------------------|------------|
| No real-time collab | True | Use Git for async collab |
| Sync between devices | Manual | Obsidian Sync ($4/mo) or iCloud |
| Learning curve | Medium | This guide helps |

## Quick Setup (30 minutes)

### Step 1: Clone Product Folder

```bash
git clone https://github.com/mrd-bdsmetro/product-tower-kit.git
cd product-tower-kit/Product
```

### Step 2: Open in Obsidian

1. Download [Obsidian](https://obsidian.md)
2. Open Obsidian → "Open folder as vault"
3. Select the `Product` folder

### Step 3: Enable Recommended Plugins

In Obsidian settings:

| Plugin | Enable | Why |
|--------|--------|-----|
| **Daily Notes** | ✅ | Weekly checkpoint tracking |
| **Templates** | ✅ | Quick T-tier creation |
| **Graph View** | ✅ | See T-series relationships |
| **Backlinks** | ✅ | Track dependencies |
| **Search** | ✅ | Full-text search |

### Step 4: Setup Quartz for Publishing

```bash
# Go to Product folder
cd Product

# Clone Quartz into public folder
git clone https://github.com/Nickytongxue/quartz.git public

# Or initialize fresh
npx create-quartz@latest public
```

### Step 5: Configure Quartz

Edit `public/quartz.config.ts`:

```typescript
const config: Configuration = {
  name: "Product Tower Kit",
  description: "Validate before you build",
  theme: {
    style: {
      accentColor: "#6366f1",
    },
  },
  navigation: [
    { name: "Start Here", link: "/00_Entry_Point/INDEX" },
    { name: "Framework", link: "/01_Framework_Layer/" },
    { name: "Instance", link: "/02_Instance_Layer/" },
  ],
  serves: "./",  // Serve from root
}
```

### Step 6: Publish to GitHub Pages

```bash
cd public
npx quartz build --push
```

Or use GitHub Actions (automatic on push):

```yaml
# .github/workflows/quartz.yml
name: Quartz Publish
on:
  push:
    branches: [master]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: topof-1357/quartz-github-action@v1
```

## Obsidian Workflow

### Daily Usage

```markdown
1. Open Obsidian → Select Product vault
2. Check weekly_checkpoint.md → Update progress
3. Work on current T-tier
4. Git commit (when significant changes)
5. Push to GitHub
```

### Creating New T-Tier

1. Press Ctrl+T → Template: T-Series
2. Fill in frontmatter
3. Write content
4. Git commit + push

### Graph View Analysis

1. Press Ctrl+G (Graph View)
2. Filter by folder: `02_Instance_Layer/T_Series`
3. See which T-tiers link to each other
4. Identify orphaned files

## Quartz Publishing

### Manual Publish

```bash
cd Product/public
npx quartz build --push
```

### Automatic Publish (GitHub Actions)

Push to master → Quartz rebuilds → Site updates in 2-3 minutes

### Custom Domain (optional)

In Quartz config:

```typescript
const config: Configuration = {
  // ...
  base: "https://product-kit.yourdomain.com",
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Obsidian vault won't open | Check path has no special characters |
| Quartz build fails | Run `npx quartz sync` first |
| Graph view shows no links | Add wikilinks `[[file]]` in content |
| Publishing slow | Check GitHub Actions logs |

## Sync Between Devices

| Method | Cost | Setup |
|--------|------|-------|
| **Obsidian Sync** | $4/mo | Built-in |
| **iCloud** | Free (Apple) | System-level |
| **Git** | Free | Manual push/pull |
| **Syncthing** | Free | P2P, local network |

---
*Tools Stack v2.0.0 — Obsidian + Quartz focused*