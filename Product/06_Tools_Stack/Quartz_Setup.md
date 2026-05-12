---
status: active
type: setup
owner: MR.D
last_updated: 2026-05-12
tags: [quartz, hugo, static-site, publishing, github-pages]
pmf_impact: low
---

# Quartz Setup Guide

## What is Quartz?

Quartz transforms your Obsidian vault into a fast, beautiful static site. Built on Hugo, deploys to GitHub Pages for free.

**Why Quartz over other static site generators?**

| Feature | Quartz | Notion → Static | Jekyll |
|---------|--------|-----------------|--------|
| Markdown native | ✅ | ❌ | ✅ |
| Obsidian sync | ✅ | ❌ | ❌ |
| Backlinks preserved | ✅ | ❌ | Manual |
| Free hosting | ✅ (Pages) | ❌ (paid) | ✅ |
| No config needed | ✅ | N/A | ❌ |

## Prerequisites

- Git installed
- Node.js 18+
- GitHub account
- Obsidian vault ready

## Option 1: Clone Full Repository

### Step 1: Clone Repository

```bash
git clone https://github.com/mrd-bdsmetro/product-tower-kit.git
cd product-tower-kit
```

### Step 2: Setup Quartz Submodule

```bash
# Add Quartz as submodule in public folder
git submodule add https://github.com/Nickytongxue/quartz.git public
```

### Step 3: Configure Quartz

Edit `public/quartz.config.ts`:

```typescript
import { Configuration } from "./quartz/components"

const config: Configuration = {
  name: "Product Tower Kit",
  description: "Validate before you build",
  theme: {
    style: {
      accentColor: "#6366f1",  // Indigo
      fontSize: "16px",
    },
  },
  navigation: [
    { name: "Start Here", link: "/00_Entry_Point/INDEX" },
    { name: "Framework", link: "/01_Framework_Layer/" },
    { name: "Instance", link: "/02_Instance_Layer/" },
    { name: "Execution", link: "/03_Execution_Layer/" },
    { name: "Learning", link: "/04_Learning_Layer/" },
  ],
}
```

### Step 4: Build

```bash
cd public
npm install
npx quartz build
```

### Step 5: Preview Locally

```bash
npx quartz serve
# Open http://localhost:8080
```

## Option 2: Fresh Quartz Install

### Step 1: Create Quartz Site

```bash
mkdir product-kit-site
cd product-kit-site
npx create-quartz@latest .
```

### Step 2: Copy Product Content

```bash
# Copy your Product folder content
cp -r /path/to/product-tower-kit/Product/* .

# Keep Quartz config, ignore product config
rm -f quartz.config.ts
```

### Step 3: Configure

```bash
# Edit quartz.config.ts
nano quartz.config.ts
```

### Step 4: Build & Preview

```bash
npm install
npx quartz build
npx quartz serve
```

## GitHub Pages Deployment

### Option A: GitHub Actions (Recommended)

Create `.github/workflows/quartz.yml`:

```yaml
name: Quartz Deploy
on:
  push:
    branches: [master]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: recursive
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18
      
      - name: Build Quartz
        run: |
          cd public
          npm ci
          npx quartz build
      
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
          publish_branch: gh-pages
```

### Option B: Manual Deploy

```bash
cd public
npx quartz build --push
```

### Set GitHub Pages Source

1. Go to repo Settings → Pages
2. Source: Deploy from branch
3. Branch: `gh-pages` / (root)

## Custom Domain (Optional)

### Configure in Quartz

Edit `quartz.config.ts`:

```typescript
const config: Configuration = {
  // ...
  base: "https://productkit.yourdomain.com",
}
```

### DNS Settings

Add to your DNS provider:

| Type | Name | Value |
|------|------|-------|
| CNAME | productkit | mrd-bdsmetro.github.io |

## Quartz Features

### Backlinks

Quartz automatically shows backlinks at bottom of each page:

```markdown
## Backlinks
- [[T7_PMF|T7]] - PMF Validation
- [[Validation_Funnel]] - References this
```

### Full-Text Search

Press `Ctrl+K` to search all content.

### Graph View

Hover on "Graph View" button in header.

## Obsidian → Quartz Workflow

```
Obsidian (local) → Edit → Save → Git Commit → Git Push
                                    ↓
                            GitHub Actions
                                    ↓
                            Quartz Builds
                                    ↓
                            Site Published
```

### Auto-Publish on Save

Using Obsidian Git plugin:

```json
{
  "commitMessage": "{{date}}",
  "autoCommitInterval": 5,
  "autoPush": true
}
```

Push → GitHub Actions triggers → Site updates in ~2 min

## Troubleshooting

| Error | Solution |
|-------|----------|
| Build failed | Run `npm install` in public folder |
| 404 on pages | Check base path in config |
| Missing CSS | Clear cache, rebuild |
| Submodule not found | `git submodule update --init` |

## Quick Commands

| Command | Action |
|---------|--------|
| `npx quartz build` | Build site |
| `npx quartz serve` | Preview locally |
| `npx quartz build --push` | Build + deploy |
| `npx quartz sync` | Sync with remote |

---
*Quartz Setup Guide v1.0.0*