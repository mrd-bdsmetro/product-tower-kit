# Product Tower Kit - System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER (Founder)                           │
│                    Claude Code + Terminal                        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     UX LAYER (Commands)                          │
│  /pt:init  /pt:research  /pt:validate  /pt:scope  /pt:assess    │
│  /pt:status  /pt:report                                          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   KNOWLEDGE LAYER (Skills)                       │
│  product-tower (master) → market-research → market-segmentation │
│  → user-discovery → pmf-validator → pricing-strategy            │
│  → competitor-analysis → deep-research-parser                   │
│  → analytics-feedback → delivery-tower → sales-tower            │
│  → product-sale → brainstorm → research → problem-solving       │
│  → retro → sequential-thinking                                  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   EXECUTION LAYER (Agents)                       │
│  product-planner  market-researcher  anti-bias-challenger       │
│  pmf-validator  feature-scoper  brainstormer  researcher        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  ENFORCEMENT LAYER (Hooks + Rules)               │
│  gate-check.sh (PreToolUse)  pmf-alert.sh (PostToolUse)         │
│  tier-progress.sh (SessionStart)                                 │
│  product-workflow.md  gate-enforcement.md  anti-bias-rules.md   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   BUSINESS LOGIC (Python)                        │
│                    scripts/gate_checker.py                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Gate Engine  │  │ PMF Scorer  │  │ State Mgmt  │             │
│  │ (19-tier DAG)│  │ (penalties) │  │ (JSON)      │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   OUTPUT LAYER (Files)                           │
│  data/t0_market_research.md  data/t7_pmf.md  ...                │
│  pipeline_state.json                                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3-Language Stack

### Python - Business Logic + Valyu Search

**Files:**
- `scripts/gate_checker.py` (277 lines) - Gate enforcement
- `scripts/valyu_search.py` (159 lines) - Valyu API integration

**Responsibilities:**
- Gate enforcement (19-tier DAG)
- PMF scoring with penalty system
- State management (pipeline_state.json)
- File naming conventions
- Health assessment
- Valyu search integration (web, deep, academic modes)

**Key Components:**
```python
# Gate rules (DAG)
GATE_RULES = {
    "T-1": {"requires_tiers": [], "name": "Rapid Validation"},
    "T0": {"requires_tiers": ["T-1"], "name": "Market Research"},
    # ... 19 tiers total
}

# PMF threshold
PMF_THRESHOLD = 30
PMF_SCALE = 50

# Commands
cmd_init()      # Initialize project
cmd_check()     # Check gate
cmd_complete()  # Mark tier complete
cmd_pmf()       # Set PMF score
cmd_status()    # Show status
cmd_assess()    # Health assessment
cmd_naming()    # Show naming convention
```

### PowerShell - Orchestration

**Files:**
- `scripts/harness-health.ps1` (259 lines) - Health check
- `scripts/harness-eval.ps1` (103 lines) - Harness evaluator

**Responsibilities:**
- Health checks (70+ checks across all components)
- Harness evaluation (runs health + syntax + gate)
- Quality assurance pipeline

**Key Patterns:**
```powershell
# Add-Check pattern (static checks)
function Add-Check {
    param([string]$Category, [string]$Label, [bool]$Pass, [string]$Detail)
    $script:totalChecks++
    if ($Pass) { $script:passedChecks++ }
}

# Run-Check pattern (dynamic checks)
function Run-Check {
    param([string]$Name, [string]$Command)
    # Execute command and track result
}
```

### Node.js - CLI Wrapper + CI Contracts

**Files:**
- `bin/product-tower.js` (82 lines) - CLI entry point
- `scripts/invariant-checks.js` (178 lines) - Invariant checks
- `scripts/syntax-check.js` (78 lines) - Syntax validation
- `index.js` (31 lines) - Module exports

**Responsibilities:**
- CLI wrapper (maps commands to Python scripts)
- Invariant checks (package, skills, agents, commands)
- Syntax validation (Node.js, Python, JSON, SKILL.md)

**Key Patterns:**
```javascript
// check/assert pattern
function check(name, fn) {
  try {
    fn();
    console.log(`  [OK] ${name}`);
    passed++;
  } catch (err) {
    console.log(`  [FAIL] ${name}: ${err.message}`);
    failed++;
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}
```

---

## 6 Systems

**Note:** Product Tower Kit base provides 23 skills, 7 agents, 7 commands. Full ClaudeKit Engineer Kit adds 87 skills, 14 agents, 50+ commands, 20+ hooks.

### 1. Skills System (Knowledge Layer)

**Base: 23 SKILL.md files** + ClaudeKit Engineer Kit (87 skills)

| Skill | Tiers | Purpose |
|-------|-------|---------|
| product-tower | ALL | Master orchestrator |
| market-research | T0 | Data collection (Express/Pro/Valyu modes) |
| market-segmentation | T1-T3 | Segment targeting |
| user-discovery | T4-T6 | Persona + needs |
| pmf-validator | T7 | PMF gate |
| pricing-strategy | T9.5 | Offer design |
| competitor-analysis | T0-CP | Competitive map |
| deep-research-parser | Pre-T0 | Parse deep research |
| analytics-feedback | T14 | Feedback loop |
| delivery-tower | D1-D6 | GTM + launch |
| sales-tower | S0-S9 | Hormozi framework |
| product-sale | P0-P10 | Unified BUILD+SELL |
| brainstorm | - | Trade-off analysis, anti-rationalization |
| research | - | Systematic research with confidence scoring |
| problem-solving | - | 5 Whys, 80/20, Inversion |
| retro | - | Sprint retrospectives for T14 |
| sequential-thinking | - | Structured problem-solving |
| launch-strategy | - | ORB Framework, 5-phase launch |
| marketing-ideas | - | 140+ proven marketing ideas |
| marketing-psychology | - | 70+ mental models |
| competitor-alternatives | - | Comparison page templates |
| free-tool-strategy | - | Engineering-as-marketing |
| onboarding-cro | - | User onboarding and activation |

**ClaudeKit Engineer Kit skills:** ck:plan, ck:cook, ck:scout, ck:debug, ck:fix, ck:ship, ck:deploy, ck:git, ck:docs, research, and 77 more.

### 2. Agents System (Execution Layer)

**Base: 7 agents** + ClaudeKit Engineer Kit (14 agents)

| Agent | Role | Trigger |
|-------|------|---------|
| product-planner | Tier progression | "plan next", "what's next" |
| market-researcher | Data collection | "research", "find data" |
| anti-bias-challenger | AB1-AB6 enforcement | "challenge", "red team" |
| pmf-validator | PMF scoring | "validate PMF" |
| feature-scoper | Feature scoping | "scope features", "MVP" |
| brainstormer | CTO-level advisor | "brainstorm", "trade-off" |
| researcher | Technical analyst | "deep research", "analyze" |

### 3. Commands System (UX Layer)

**7 commands** in `.claude/commands/`

| Command | Description |
|---------|-------------|
| /pt:init | Initialize project |
| /pt:research [topic] | Run T0 market research |
| /pt:validate PMF | Run T7 PMF validation |
| /pt:scope features | Run T8-T9 feature scoping |
| /pt:assess | Quick health check |
| /pt:status | Show pipeline status |
| /pt:report | Generate full report |

### 4. Hooks System (Enforcement Layer)

**3 hooks** in `.claude/hooks/`

| Hook | Event | Purpose |
|------|-------|---------|
| gate-check.sh | PreToolUse | Check gate before file writes |
| pmf-alert.sh | PostToolUse | Alert on PMF-related commands |
| tier-progress.sh | SessionStart | Show tier progress on session start |

**Configuration:** `.claude/settings.json`

### 5. Rules System (Policy Layer)

**3 rules** in `.claude/rules/`

| Rule | Purpose |
|------|---------|
| product-workflow.md | Workflow rules |
| gate-enforcement.md | Gate enforcement rules |
| anti-bias-rules.md | Anti-bias rules |

### 6. Harness System (Quality Assurance)

**5 scripts** in `scripts/`

| Script | Language | Lines | Purpose |
|--------|----------|------:|---------|
| syntax-check.js | Node.js | 78 | Syntax validation |
| invariant-checks.js | Node.js | 178 | Invariant checks |
| harness-eval.ps1 | PowerShell | 103 | Harness evaluator |
| harness-health.ps1 | PowerShell | 259 | Health check |
| valyu_search.py | Python | 159 | Valyu API integration |
| gate_checker.py | Python | 277 | Gate enforcement + PMF scoring |

**3 Levels:**
1. **Health** - File existence, structure, frontmatter
2. **Eval** - Health + syntax + gate tests
3. **Hardness** - Eval + Python syntax + gate integration

---

## Gate System Design

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

### Gate Rules

| Tier | Requires | Name |
|------|----------|------|
| T-1 | - | Rapid Validation |
| T0 | T-1 | Market Research |
| T1 | T0 | Target Market |
| T2 | T0, T1 | Market Segmentation |
| T3 | T0, T1, T2 | Segment Filter |
| T4 | T3 | User Personas |
| T5 | T3, T4 | User Needs |
| T6 | T3, T4, T5 | Unmet Needs |
| AB1 | T4 | Counter-Search |
| AB2 | T4, AB1 | Red Team |
| AB3 | T4, AB1, AB2 | Field Observation |
| AB4 | T4, AB1, AB2, AB3 | User Interview |
| AB5 | T4, AB1, AB2, AB3, AB4 | Strategic Analysis |
| AB6 | T4, AB1, AB2, AB3, AB4 | Founder Insight |
| T7 | T6, AB1, AB2, AB3, AB4 | PMF Validation |
| T8 | T7 | Feature Set |
| T9 | T7, T8 | User Stories |
| T9.5 | T7, T8, T9 | Offer Bridge |
| T0-CP | T0 | Competitive Positioning |
| T14 | T9.5 | Feedback Loop |

### PMF Scoring

```
PMF Adjusted = PMF Raw + Penalty

Penalty Table:
  Desk-only (no AB)     → -11
  +AB1 only             → -5
  +AB1+AB2              → -2.5
  +AB1+AB2+AB3          → 0
  +AB1+AB2+AB3+AB4      → -5 (placeholder penalty)
  +AB5                  → +0.5
  +AB6                  → +1.0

Threshold: ≥30/50 = GO
```

**Current Status:** 33/50 raw, 22/50 adjusted (NO-GO)
- AB4 is PLACEHOLDER - real user interviews needed
- Target: PMF 35/50 after 1-2 months validation

### Confidence Tagging

| Tag | Score | Source |
|-----|-------|--------|
| 🤖 | 60% | AI-generated |
| 📊 | 80% | Cited data |
| 👤 | 90% | User interview |
| ✅ | 95% | Validated |

---

## State Management

### pipeline_state.json

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

### State Transitions

```
init → T-1 complete → T0 complete → ... → T6 complete
  → AB1 complete → AB2 complete → AB3 complete → AB4 complete
  → T7 (PMF check) → T8 complete → T9 complete → T9.5 complete
  → T14 complete
```

---

## Data Flow

```
User Input (Claude Code)
    │
    ▼
Command (/pt:research, /pt:validate, etc.)
    │
    ▼
Skill (market-research, pmf-validator, etc.)
    │
    ▼
Agent (market-researcher, pmf-validator, etc.)
    │
    ▼
Output File (data/t0_market_research.md, data/t7_pmf.md, etc.)
    │
    ▼
State Update (pipeline_state.json)
    │
    ▼
Gate Check (gate_checker.py)
    │
    ▼
Next Tier or Block
```

---

## Integration Points

### Claude Code

**Requires:** ClaudeKit Engineer Kit (**$79 via ref IJBRLXD6**, 20% off at [claudekit.cc/?ref=IJBRLXD6](https://claudekit.cc/?ref=IJBRLXD6)) — provides private GitHub repo access

| Component | Source | Location |
|-----------|--------|----------|
| Skills | Base (23) + ClaudeKit Engineer Kit (87) | `.claude/skills/*/SKILL.md` |
| Agents | Base (7) + ClaudeKit Engineer Kit (14) | `.claude/agents/*.md` |
| Commands | Base (7) + ClaudeKit Engineer Kit (50+) | `.claude/commands/*.md` |
| Hooks | ClaudeKit Engineer Kit (20+) | `.claude/hooks/*.sh` |
| Rules | ClaudeKit Engineer Kit | `.claude/rules/*.md` |
| Settings | ClaudeKit Engineer Kit | `.claude/settings.json` |

### npm

- **Package:** `product-tower-kit` - npm package
- **CLI:** `bin/product-tower.js` - CLI entry point
- **Scripts:** `npm run test:syntax`, `npm run test:invariants`, etc.

### Python

- **Gate Checker:** `scripts/gate_checker.py` - Gate enforcement
- **Valyu Search:** `scripts/valyu_search.py` - Market research via Valyu API
- **Called by:** Node.js CLI via `child_process.execSync()`
- **State:** `pipeline_state.json` - Project state

---

## ClaudeKit API Layer

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLAUDEKIT API INTEGRATION                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  VidCap (YouTube Processing)                                    │
│  ├── /youtube/info          → Metadata, tags, description        │
│  ├── /youtube/caption       → Phụ đề đa ngôn ngữ                │
│  ├── /youtube/summary       → Tóm tắt AI                        │
│  ├── /youtube/screenshot    → Frame capture                     │
│  ├── /youtube/comments      → Comment extraction                │
│  └── /youtube/search        → Video search                       │
│                                                                  │
│  ReviewWeb (Scraping + SEO)                                      │
│  ├── /scrape, /extract      → Web content extraction            │
│  ├── /convert/markdown      → Web → Markdown                     │
│  ├── /screenshot            → Page screenshots                  │
│  ├── /summarize/*          → AI summaries                        │
│  └── /seo-insights/*       → Backlinks, keywords, traffic       │
│                                                                  │
│  Base: https://claudekit.cc/api/proxy/                           │
│  Auth: X-API-Key header                                         │
│  Limits: 10,000 req/hour                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**See:** `06_Tools_Stack/Tools_Stack.md` (ClaudeKit API section)

---

## Valyu Integration Layer

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    VALYU SEARCH INTEGRATION                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  market-research skill                                           │
│       │                                                          │
│       ▼                                                          │
│  valyu_search.py (Python CLI)                                    │
│       │                                                          │
│       ├── web mode      → General market data (fast)             │
│       ├── deep mode     → Full content extraction (medium)       │
│       └── academic mode → Papers, filings, patents (slow)        │
│       │                                                          │
│       ▼                                                          │
│  Valyu API (https://valyu.ai)                                    │
│       │                                                          │
│       ▼                                                          │
│  data/search_{mode}_{timestamp}.md                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Usage

```bash
# Direct CLI usage
python scripts/valyu_search.py "Vietnam SaaS market" --mode deep
python scripts/valyu_search.py "PMF framework" --mode academic --max-results 5

# Via Claude Code
"valyu search Vietnam SaaS market"
"deep search product-market fit"
"academic search startup validation"
```

### Search Modes

| Mode | Use Case | Speed | Content |
|------|----------|-------|---------|
| `web` | General market data | Fast | Web pages, news |
| `deep` | Full content extraction | Medium | Complete articles |
| `academic` | Research papers | Slow | Papers, filings, patents |

### Dependencies

| Dependency | Required | Purpose |
|------------|----------|---------|
| `valyu` (pip) | Yes | Python SDK for Valyu API |
| `VALYU_API_KEY` | Yes | API authentication |

---

## Security Considerations

| Concern | Mitigation |
|---------|------------|
| State file tampering | Gate checker validates state structure |
| Script injection | CLI uses `execSync` with proper escaping |
| File path traversal | Path resolution uses `path.resolve()` |
| Unicode handling | Windows Unicode fix in gate_checker.py |
