# Product Tower Kit - Codebase Summary

## Overview

**Total: 6,278 lines | 91 files | 8 directories | 4 languages**

Product Tower Kit is a product management toolkit for Claude Code. The codebase spans Python (business logic + Valyu search), PowerShell (orchestration), Node.js (CLI wrapper + CI contracts), and Markdown (docs, skills, agents, templates).

---

## Directory Structure

```
product-tower-kit/
├── .claude/                    # Claude Code integration
│   ├── agents/                 # 7 agent definitions
│   ├── commands/               # 7 slash commands
│   ├── hooks/                  # 3 automation hooks
│   ├── rules/                  # 3 policy rules
│   ├── settings.json           # Hook configuration
│   └── skills/                 # 23 SKILL.md files
├── bin/                        # CLI entry point
│   └── product-tower.js        # 97 lines
├── data/                       # Product Tower output (19 files)
│   ├── t*.md                   # Tower tier outputs (T-1, T0, T0-CP, T1-T6, T7-T9, T9.5)
│   └── ab*.md                  # Anti-bias outputs (AB1-AB6)
├── docs/                       # Documentation (5 files)
│   └── quickstart.md
├── public/                     # llms.txt files
│   ├── llms.txt
│   └── llms-full.txt
├── resources/                  # Reference materials
│   └── ecosystem-map.md
├── scripts/                    # Core scripts (6 files)
│   ├── gate_checker.py         # 277 lines - Gate enforcement
│   ├── valyu_search.py         # 159 lines - Valyu API integration
│   ├── harness-health.ps1      # 259 lines - Health check
│   ├── harness-eval.ps1        # 103 lines - Harness evaluator
│   ├── invariant-checks.js     # 178 lines - Invariant checks
│   └── syntax-check.js         # 78 lines - Syntax validation
├── templates/                  # Output templates
│   └── product-plan.md         # 92 lines
├── index.js                    # 26 lines - Module exports
├── package.json                # 56 lines
├── README.md                   # 171 lines
├── CHANGELOG.md                # 79 lines
├── LICENSE                     # 18 lines
├── pipeline_state.json         # 88 lines - State file
└── .gitignore                  # (gitignore)
```

---

## Lines of Code by Directory

| Directory | Lines | Files | Purpose |
|-----------|------:|------:|---------|
| Root | 379 | 7 | Config, exports, docs |
| bin | 97 | 1 | CLI entry point |
| data | 1,253 | 19 | Product Tower output (T-1, T0-T9.5, AB1-AB6) |
| docs | 1,189 | 5 | Documentation |
| public | 184 | 2 | llms.txt files |
| resources | 74 | 1 | Ecosystem map |
| scripts | 1,024 | 6 | Gate checker, Valyu, harness |
| templates | 92 | 1 | Product plan template |
| **Total** | **6,278** | **91** | |

---

## Language Breakdown

| Language | Lines | Files | Purpose |
|----------|------:|------:|---------|
| Python | 436 | 2 | Business logic (gate_checker.py) + Valyu search (valyu_search.py) |
| PowerShell | 362 | 2 | Orchestration (harness-health.ps1, harness-eval.ps1) |
| Node.js | 364 | 4 | CLI + CI (bin/product-tower.js, invariant-checks.js, syntax-check.js, index.js) |
| Markdown | 5,116 | 83 | Docs, skills, agents, commands, templates, data output |
| **Total** | **6,278** | **91** | |

---

## Key Files

### Scripts (Core Logic)

| File | Lines | Language | Purpose |
|------|------:|----------|---------|
| `scripts/gate_checker.py` | 277 | Python | Gate enforcement, PMF scoring, state management |
| `scripts/valyu_search.py` | 159 | Python | Valyu API integration (web, deep, academic search) |
| `scripts/harness-health.ps1` | 259 | PowerShell | Health check (~50 checks across all components) |
| `scripts/harness-eval.ps1` | 103 | PowerShell | Harness evaluator (runs health + syntax + gate) |
| `scripts/invariant-checks.js` | 178 | Node.js | Invariant checks (package, skills, agents, commands) |
| `scripts/syntax-check.js` | 78 | Node.js | Syntax validation (Node.js, Python, JSON, SKILL.md) |

### CLI

| File | Lines | Language | Purpose |
|------|------:|----------|---------|
| `bin/product-tower.js` | 82 | Node.js | CLI entry point (init, check, complete, pmf, status, assess, naming) |
| `index.js` | 31 | Node.js | Module exports (KIT_ROOT, SKILLS_DIR, SCRIPTS_DIR) |

### Claude Code Integration

| Directory | Files | Purpose |
|-----------|------:|---------|
| `.claude/skills/` | 23 | SKILL.md files (knowledge layer) |
| `.claude/agents/` | 7 | Agent definitions (execution layer) |
| `.claude/commands/` | 7 | Slash commands (UX layer) |
| `.claude/hooks/` | 3 | Automation hooks (enforcement layer) |
| `.claude/rules/` | 3 | Policy rules (policy layer) |

---

## Architecture

### 3-Language Stack

```
┌─────────────────────────────────────────────────┐
│                    Node.js                       │
│  CLI wrapper + CI contracts                      │
│  (bin/product-tower.js, invariant-checks.js)     │
├─────────────────────────────────────────────────┤
│                    Python                        │
│  Business logic (gate enforcement, PMF scoring)  │
│  (scripts/gate_checker.py)                       │
├─────────────────────────────────────────────────┤
│                   PowerShell                     │
│  Orchestration (health checks, eval pipeline)    │
│  (scripts/harness-health.ps1, harness-eval.ps1)  │
└─────────────────────────────────────────────────┘
```

### 6 Systems

| System | Layer | Files | Purpose |
|--------|-------|------:|---------|
| **Skills** | Knowledge | 23 | SKILL.md files for Claude Code |
| **Agents** | Execution | 7 | Agent definitions |
| **Commands** | UX | 7 | Slash commands |
| **Hooks** | Enforcement | 3 | Automation hooks |
| **Rules** | Policy | 3 | Policy rules |
| **Harness** | Quality | 5 | Quality assurance scripts (includes Valyu) |

---

## Dependencies

### Runtime Dependencies

| Dependency | Version | Required | Purpose |
|------------|---------|----------|---------|
| Node.js | ≥ 18.0.0 | Yes | CLI wrapper, syntax checks |
| Python 3 | Any | Yes | Gate enforcement, PMF scoring, Valyu search |
| PowerShell | Any | No | Harness health checks (Windows) |
| Claude Code | Latest | Yes | Skills, agents, commands |
| Valyu | Latest | No | Enhanced market research (web, deep, academic) |

### npm Dependencies

**Zero npm dependencies.** The kit uses only Node.js built-in modules:
- `child_process` - Execute Python scripts
- `path` - Path manipulation
- `fs` - File system operations
- `os` - Platform detection

---

## Testing Strategy

### 3-Layer Testing

```
Layer 1: Syntax Check (node scripts/syntax-check.js)
  ├── Node.js files parse correctly
  ├── Python files have valid structure
  ├── JSON files parse correctly
  └── SKILL.md files have valid frontmatter

Layer 2: Invariant Checks (node scripts/invariant-checks.js)
  ├── Package structure (name, bin, files, license)
  ├── CLI commands (shebang, command mapping)
  ├── Skills (23 SKILL.md files, frontmatter)
  ├── Agents (7 agents, Role/Behavior/Activation sections)
  ├── Commands (7 commands, Usage section)
  ├── Hooks (3 hooks, settings.json)
  ├── Rules (3 rules)
  ├── Gate consistency (all tiers, all commands)
  └── Skill cross-references (master orchestrator)

Layer 3: Harness Health (powershell scripts/harness-health.ps1)
  ├── Package files (6 files)
  ├── CLI entry point (shebang)
  ├── Skills (23 SKILL.md files, frontmatter, Goal section)
  ├── Agents (7 agents, Role/Behavior sections)
  ├── Commands (7 commands, Usage section)
  ├── Hooks (3 hooks, settings.json)
  ├── Rules (3 rules)
  ├── Scripts (gate_checker.py, valyu_search.py, Python available)
  ├── Templates (product-plan.md)
  ├── Resources (ecosystem-map.md)
  ├── Docs (quickstart.md)
  ├── npm scripts (test, lint, init)
  └── Gate consistency (all tiers in gate_checker.py)
```

### Running Tests

```bash
# Layer 1: Syntax check
npm run test:syntax

# Layer 2: Invariant checks
npm run test:invariants

# Layer 3: Harness health
npm run harness:health

# Full harness eval (health + syntax + gate)
npm run harness:eval

# Hardness eval (includes Python + gate tests)
npm run harness:hardness
```

---

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Skills | `kebab-case/SKILL.md` | `market-research/SKILL.md` |
| Agents | `kebab-case.md` | `product-planner.md` |
| Commands | `pt-kebab-case.md` | `pt-init.md` |
| Hooks | `kebab-case.sh` | `gate-check.sh` |
| Rules | `kebab-case.md` | `gate-enforcement.md` |
| Scripts | `kebab-case.{py,ps1,js}` | `gate_checker.py` |
| Tower output | `t{N}_{name}.md` | `t0_market_research.md` |

---

## State Management

Each project maintains a `pipeline_state.json` file:

```json
{
  "project": "my-project",
  "created_at": "2026-05-06T00:00:00",
  "updated_at": "2026-05-06T00:00:00",
  "version": "1.0.0",
  "tiers_completed": {
    "T0": {"completed_at": "2026-05-06T01:00:00"}
  },
  "tiers_skipped": {},
  "anti_bias": {
    "AB1": {"status": "pending", "file": "data/ab1_counter_search.md"},
    "AB2": {"status": "pending", "file": "data/ab2_red_team.md"},
    "AB3": {"status": "pending", "file": "data/ab3_field_notes.md"},
    "AB4": {"status": "pending", "file": "data/ab4_user_interview.md"}
  },
  "pmf": {
    "raw": null,
    "adjusted": null,
    "penalty": 0,
    "scale": 50,
    "threshold": 30
  }
}
```

---

## Gate System

### 19-Tier DAG

```
T-1 → T0 → T1 → T2 → T3 → T4 → T5 → T6
                ↓
              AB1 → AB2 → AB3 → AB4 → AB5/AB6
                ↓
              T7 (PMF Gate: ≥30/50)
                ↓
              T8 → T9 → T9.5 → T14
```

### PMF Scoring

| Anti-Bias Status | Penalty |
|------------------|--------:|
| Desk-only (no AB) | -10 |
| +AB1 only | -5 |
| +AB1+AB2 | -2.5 |
| Full AB (AB1-AB4) | 0 |
| +AB5 | +0.5 |
| +AB6 | +1.5 |

### Confidence Tagging

| Tag | Score | Source |
|-----|-------|--------|
| 🤖 | 60% | AI-generated |
| 📊 | 80% | Cited data |
| 👤 | 90% | User interview |
| ✅ | 95% | Validated |
