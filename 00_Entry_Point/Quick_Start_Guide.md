---
status: active
type: entry
owner: MR.D
last_updated: 2026-05-12
tags: [quick-start, setup, onboarding]
---

# Quick Start Guide

## Setup (15 minutes)

### 1. Prerequisites
- Node.js 18+
- Python 3.8+
- Git

### 2. Initialize Project
```bash
npm install
python init-project.py
```

### 3. Run Health Check
```bash
npm run harness:health
```

### 4. Start Validation
```bash
# Research phase
npm run search -- "your product idea"

# Run validation gates
node bin/product-tower.js validate
```

## Validation Workflow

```
T_Minus1 → T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8 → T9 → T9.5
   ↓        ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓     ↓
  AB1      AB2  AB3  AB4  AB5  AB6
```

### Phase Gates
| Gate | Checkpoint | Script |
|------|------------|--------|
| G0 | Rapid validation | `npm run test:syntax` |
| G1 | Competitive map | Health check |
| G2 | Target market | Manual review |
| G3 | PMF score ≥ 7 | `npm run harness:eval` |

## Key Commands

| Command | Purpose |
|---------|---------|
| `npm run init` | Initialize new product |
| `npm run harness:health` | Run health checks |
| `npm run harness:eval` | Full evaluation |
| `npm run search` | Web search |
| `node bin/product-tower.js status` | Check pipeline status |

## Next Steps

1. Read [INDEX.md](./INDEX.md) for full navigation
2. Check [CHANGELOG](./CHANGELOG.md) for version info
3. Review [docs/quickstart.md](../docs/quickstart.md) for detailed guide

---
*Questions? Check docs/ or run `node bin/product-tower.js --help`*