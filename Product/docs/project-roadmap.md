# Product Tower Kit - Project Roadmap

## Current Status

| Metric | Value |
|--------|-------|
| **Version** | 1.4.0 |
| **PMF Score** | 22/50 adjusted (NO-GO) |
| **Tiers Completed** | 18/19 |
| **Skills** | 23 |
| **Agents** | 7 |
| **Commands** | 7 |
| **Files** | 91 |
| **Total LOC** | 6,278 |

### Current PMF Breakdown

```
Raw Score:  33/50
Penalty:    -11 (AB4 placeholder)
Adjusted:   22/50
Threshold:  30/50
Status:     ❌ NO-GO
```

### Gap to PMF ≥30/50

- **Required:** +8 points
- **Main blocker:** AB4 placeholder user interviews
- **Target path:**
  1. Launch free tier → +3
  2. Landing page → +2
  3. 5+ real user interviews → +5
  4. 100+ users → +3
  - **Total potential:** PMF 35/50 ✅

---

## Version History

### [1.4.0] - 2026-05-06

**Added (Marketing Skills):**
- `launch-strategy` - ORB Framework, 5-phase launch, Product Hunt strategy
- `marketing-ideas` - 140+ proven marketing ideas (Content, PLG, Social, Email, Partnerships, PR)
- `marketing-psychology` - 70+ mental models (persuasion, pricing, UX, growth)
- `competitor-alternatives` - Comparison page templates for SEO and sales
- `free-tool-strategy` - Engineering-as-marketing for lead generation
- `onboarding-cro` - User onboarding and activation optimization

**Skills count:** 17 → 23

---

### [1.3.0] - 2026-05-06

**Added:**
- Valyu Search Integration - Enhanced market research with real-time web + proprietary content
- `scripts/valyu_search.py` - Python CLI for Valyu API (web, deep, academic modes)

---

### [1.2.0] - 2026-05-06

**Added (Thinking/Process Skills):**
- `brainstorm` - Product brainstorming with trade-off analysis
- `research` - Market research methodology with confidence scoring
- `problem-solving` - Systematic approaches for PMF pivot
- `retro` - Sprint retrospectives for T14 feedback loop
- `sequential-thinking` - Structured problem-solving
- `brainstormer agent` - CTO-level advisor
- Enhanced `researcher agent` - Technical analyst with saturation check

---

### [1.1.0] - 2026-05-06

**Changed:**
- Broader market positioning (vibe coders, startups, freelancers, agencies)
- Target audience: 50K → 8M+ potential users
- Multi-platform support (Claude Code, Cursor, other AI tools)

---

### [1.0.0] - 2026-05-06

**Added:**
- 14-tier Product Tower framework
- 12 SKILL.md files
- 5 agent definitions
- 7 slash commands
- 3 automation hooks
- Python CLI (gate_checker.py)
- Gate enforcement system
- Anti-Bias layer (AB1-AB6)
- PMF scoring with penalty system

---

## Roadmap Phases

### Phase 1: Core Framework (COMPLETED)
- [x] 19-tier DAG implementation
- [x] Gate enforcement system
- [x] Anti-bias layer (AB1-AB6)
- [x] PMF scoring (≥30/50 threshold)
- [x] CLI commands (init/check/complete/pmf/status/assess/naming)

### Phase 2: Claude Code Integration (COMPLETED)
- [x] 23 skills (product-tower master + domain skills + process skills)
- [x] 7 agents (planner, researcher, challenger, validator, scoper, brainstormer, researcher)
- [x] 7 commands (pt-init, pt-research, pt-validate, pt-scope, pt-assess, pt-status, pt-report)
- [x] 3 hooks (gate-check, pmf-alert, tier-progress)
- [x] 3 rules (product-workflow, gate-enforcement, anti-bias)

### Phase 3: Launch Readiness (IN PROGRESS)
- [ ] AB4: Real user interviews (remove placeholder)
- [ ] Free tier launch (T0-T7 core)
- [ ] Landing page with waitlist
- [ ] GitHub repository setup
- [ ] npm package publication
- [ ] Product Hunt launch

### Phase 4: Validation (NEXT)
- [ ] 5+ user interviews
- [ ] 100+ free users
- [ ] Collect feedback
- [ ] PMF reassessment

### Phase 5: Revenue (Q3 2026)
- [ ] $49 Starter tier launch
- [ ] $99 Pro tier launch
- [ ] $199 Team tier launch
- [ ] Payment integration (SePay, Polar, Stripe)

---

## Next Steps (Immediate)

1. **AB4: Real User Interviews** - Highest impact on PMF
   - Conduct 5+ interviews
   - Focus: WTP, problem urgency, alternative solutions
   - Expected impact: +5 PMF points

2. **Free Tier Launch** - Lower friction entry
   - Core skills T0-T7
   - GitHub + npm distribution
   - Expected impact: +3 PMF points

3. **Landing Page + Waitlist** - WTP validation
   - Quick landing page
   - Email capture
   - Expected impact: +2 PMF points

---

## Success Metrics

| Metric | Current | Target (3 months) | Target (6 months) | Target (12 months) |
|--------|---------|-------------------|-------------------|---------------------|
| **PMF Score** | 22/50 | 30/50 ✅ | 35/50 | 40/50 |
| **npm Downloads** | 0 | 500/mo | 1,000/mo | 5,000/mo |
| **GitHub Stars** | 0 | 100 | 500 | 2,500 |
| **Revenue** | $0 | $0 | $1,000 MRR | $10,000 MRR |
| **Active Projects** | 0 | 50 | 250 | 1,250 |
| **Free Users** | 0 | 100 | 500 | 2,500 |
| **Paid Users** | 0 | 10 | 50 | 250 |

---

## Dependencies

| Dependency | Version | Required | Purpose |
|------------|---------|----------|---------|
| Node.js | ≥ 18.0.0 | Yes | CLI wrapper, syntax checks |
| Python 3 | Any | Yes | Gate enforcement, PMF scoring, Valyu search |
| PowerShell | Any | No | Harness health checks (Windows) |
| Claude Code | Latest | Yes | Skills, agents, commands |
| Valyu | Latest | No | Enhanced market research |

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low AB4 completion | Medium | High | User interview guide, incentives |
| Adoption challenge | Medium | High | Vietnamese-first marketing, community |
| Claude Code changes | Low | Medium | Modular design, easy skill updates |
| Gate system too strict | Low | Medium | Force skip option, configurable thresholds |
| Python not installed | Medium | Low | Node.js fallback, clear error messages |
