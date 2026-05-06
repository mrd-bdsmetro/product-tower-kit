# Product Tower Kit

Product management toolkit for Claude Code — validate ideas, score PMF, scope MVPs.

**Vietnamese-first. ADHD-friendly. Solo founder mode.**

---

## What is Product Tower Kit?

A complete product management system powered by Claude Code. Copy into your project, run `/pt:init`, and follow the 14-tier framework to validate ideas before building.

**Inspired by:** Product Management for Managers — Hiếu (Vietnamese PM, Australia)

---

## Features

- **14-Tier Framework** — From market research to post-launch feedback
- **Anti-Bias Enforcement** — AB1-AB6 mandatory layer before PMF validation
- **PMF Gate System** — Code-enforced threshold (≥30/50) to proceed
- **5 Specialized Agents** — Planner, researcher, challenger, validator, scoper
- **12 Skills** — Complete PM toolkit with Claude Code integration
- **Confidence Tagging** — Every data point scored (60%-95%)
- **ADHD-Friendly** — One tier at a time, clear next actions

---

## Documentation

- [Project Overview & PDR](docs/project-overview-pdr.md) — Project overview, target audience, pricing, timeline
- [Codebase Summary](docs/codebase-summary.md) — LOC breakdown, architecture, dependencies, testing strategy
- [Code Standards](docs/code-standards.md) — Directory structure, naming conventions, code patterns
- [System Architecture](docs/system-architecture.md) — 6 systems, gate system, state management, data flow
- [Quickstart Guide](docs/quickstart.md) — Installation, setup, step-by-step guide
- [Ecosystem Map](resources/ecosystem-map.md) — Skills, agents, tier mapping

---

## Quick Start

```bash
# Install
npm install -g product-tower-kit

# Initialize in your project
product-tower init

# Start with Claude Code
"research thị trường [your industry]"
```

---

## The Tower

```
T14: Feedback Loop 🔄        ← MEASURE & ITERATE
T13: QA / Validation         ← BUILD
T12: Development
T11: UI Design               ← DESIGN
T10: UX Design
T9.5: Offer Bridge 💰        ← OFFER DESIGN
T9: User Stories              ← PRODUCT
T8: Feature Set
T7: PMF Validation ⭐⭐⭐      ← STRATEGY (HARD GATE)
─────────────────────────────
🔴 ANTI-BIAS LAYER           ← ENFORCEMENT
AB1: Counter-Search
AB2: Red Team
AB3: Field Observation
AB4: User Interview
AB5: Strategic Analysis ⭐
AB6: Founder Insight 💰
─────────────────────────────
T6: Unmet Needs ⭐            ← DISCOVERY
T5: User Needs
T4: User Personas
T3: Segment Filter            ← FOUNDATION
T2: Market Segmentation
T1: Target Market
T0: Market Research 🔍        ← DATA
```

---

## CLI Commands

```bash
product-tower init              # Initialize project
product-tower check T1          # Check gate
product-tower complete T0       # Mark complete
product-tower pmf 44 -4         # Set PMF score
product-tower status            # Show status
product-tower assess            # Quick health check
product-tower naming            # Show naming convention
```

---

## Claude Code Commands

```
/pt:init                        # Initialize project
/pt:research [topic]            # Run T0 market research
/pt:validate PMF                # Run T7 PMF validation
/pt:scope features              # Run T8-T9 feature scoping
/pt:assess                      # Quick health check
/pt:status                      # Show pipeline status
/pt:report                      # Generate full report
```

---

## Pricing

| Tier | Price | Includes |
|------|-------|----------|
| **Starter** | $49 | Core skills (T0-T7), gate checker, basic templates |
| **Pro** | $99 | All skills (T0-T14), agents, hooks, advanced templates |
| **Team** | $199 | Pro + multi-project, team collaboration, priority support |

---

## Resources

- [Mega Prompt](.claude/skills/market-research/references/mega-prompt.md) — Deep research prompt template

---

## License

Proprietary. See [LICENSE](LICENSE) for details.

---

## Author

**MR.D** — AI Systems × Wealth × BĐS
