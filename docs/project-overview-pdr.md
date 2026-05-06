# Product Tower Kit — Project Overview & PDR

## Project Identity

| Field | Value |
|-------|-------|
| **Name** | Product Tower Kit |
| **Version** | 1.0.0 |
| **Author** | MR.D |
| **License** | Proprietary |
| **Repository** | [github.com/AIScale-Corp/product-tower-kit](https://github.com/AIScale-Corp/product-tower-kit) |
| **npm Package** | `product-tower-kit` |

---

## Description

Product Tower Kit is a Vietnamese-first, ADHD-friendly product management toolkit for Claude Code. It provides a 14-tier framework (T0→T14) with anti-bias enforcement (AB1→AB6), a PMF gate system (≥30/50), 5 specialized agents, 12 skills, 7 commands, and 3 hooks.

**Inspired by:** Product Management for Managers — Hiếu (Vietnamese PM, Australia)

---

## Target Audience

| Segment | Description |
|---------|-------------|
| **Solo Founders** | One-person teams validating ideas before building |
| **Indie Hackers** | Bootstrappers needing structured product validation |
| **Vietnamese PM Community** | Vietnamese-first product managers |
| **ADHD Founders** | Need clear next actions, one tier at a time |
| **Claude Code Users** | Developers using Claude Code for product work |

---

## Problem Statement

**No product management toolkit exists for AI coding tools.**

- Existing PM frameworks (Lean Startup, Jobs-to-be-Done) are manual and paper-based
- AI coding tools (Claude Code, Cursor) lack structured product validation
- Solo founders skip market research and build blindly
- Bias in AI-generated research goes unchecked
- No code-enforced gates to prevent premature building

---

## Solution

### 14-Tier Framework

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

### Key Differentiators

1. **Anti-Bias Enforcement** — AB1-AB6 mandatory layer before PMF validation
2. **Code-Enforced Gates** — PMF ≥ 30/50 required to proceed
3. **Confidence Tagging** — Every data point scored (60%-95%)
4. **ADHD-Friendly** — One tier at a time, clear next actions
5. **Vietnamese-First** — Vietnamese prompts and documentation

---

## Pricing

| Tier | Price | Includes |
|------|-------|----------|
| **Starter** | $49 | Core skills (T0-T7), gate checker, basic templates |
| **Pro** | $99 | All skills (T0-T14), agents, hooks, advanced templates |
| **Team** | $199 | Pro + multi-project, team collaboration, priority support |

---

## Success Metrics

| Metric | Target (6 months) | Target (12 months) |
|--------|-------------------|---------------------|
| **npm Downloads** | 100/month | 500/month |
| **GitHub Stars** | 50 | 200 |
| **Revenue** | $500 MRR | $2,000 MRR |
| **Active Projects** | 20 | 100 |
| **PMF Pass Rate** | 60% | 70% |

---

## Timeline

| Phase | Date | Milestone |
|-------|------|-----------|
| **v1.0 Launch** | May 2026 | Initial release with 14-tier framework |
| **v1.1** | June 2026 | Vietnamese documentation, community feedback |
| **v1.2** | July 2026 | Advanced templates, team features |
| **v2.0** | Sep 2026 | Multi-language support, integrations |

---

## Technical Constraints

| Constraint | Detail |
|------------|--------|
| **Runtime** | Node.js ≥ 18.0.0 |
| **Dependencies** | Zero npm dependencies |
| **Python** | Required for gate_checker.py |
| **Platform** | Cross-platform (Windows, macOS, Linux) |
| **Claude Code** | Required for skills, agents, commands |

---

## Dependencies

| Dependency | Type | Purpose |
|------------|------|---------|
| Node.js | Runtime | CLI wrapper, syntax checks |
| Python 3 | Runtime | Gate enforcement, PMF scoring |
| PowerShell | Runtime | Harness health checks (optional) |
| Claude Code | Platform | Skills, agents, commands execution |

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low adoption | Medium | High | Vietnamese-first marketing, community building |
| Claude Code changes | Low | Medium | Modular design, easy skill updates |
| Python not installed | Medium | Low | Node.js fallback, clear error messages |
| Gate system too strict | Low | Medium | Force skip option, configurable thresholds |

---

## Competitive Landscape

| Tool | Focus | Gap |
|------|-------|-----|
| **Notion PM Templates** | Manual | No code enforcement, no AI integration |
| **Productboard** | Enterprise | Too complex for solo founders |
| **Lean Canvas** | Manual | No gate system, no bias checking |
| **Claude Code (raw)** | AI | No structure, no validation framework |

**Product Tower Kit fills the gap:** Structured PM framework with code enforcement, integrated with Claude Code.
