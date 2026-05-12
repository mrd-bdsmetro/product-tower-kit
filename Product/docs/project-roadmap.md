# Product Tower Kit - Project Roadmap

## Current Status

| Metric | Value |
|--------|-------|
| **Version** | 1.5.0 |
| **PMF Score** | 22/50 adjusted (NO-GO) |
| **Tiers Completed** | 18/19 |
| **Skills** | 23 (+ ClaudeKit Engineer Kit: 87 total available) |
| **Agents** | 7 (+ ClaudeKit Engineer Kit: 14 total available) |
| **Commands** | 7 (+ ClaudeKit Engineer Kit: 50+ total available) |
| **Files** | 91 |
| **Total LOC** | 6,278 |
| **Requires** | ClaudeKit Engineer Kit (**$79 via ref IJBRLXD6**, 20% off) — [Buy](https://claudekit.cc/?ref=IJBRLXD6) |

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

### [1.4.0] - 2026-05-12

**Added (ClaudeKit Integration):**
- `06_Tools_Stack/ClaudeKit_API.md` - Full API documentation
- VidCap API (YouTube): info, caption, summary, screenshot, comments, search
- ReviewWeb API (Scraping + SEO): scrape, extract, markdown, backlinks, keywords, traffic
- Rate limits: 10,000 requests/hour

**Changed:**
- README, docs updated with ClaudeKit requirement notice
- Pricing model clarification (requires ClaudeKit Engineer Kit purchase)

**Skills count:** 23 (base) + ClaudeKit Engineer Kit access (87 skills, 14 agents, 50+ commands)

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

**Note:** Product Tower Kit requires ClaudeKit Engineer Kit (**$79 via ref IJBRLXD6**, 20% off). The kit itself is a template/framework; revenue comes from add-on tiers + ClaudeKit license.

### Phase 1: Core Framework (COMPLETED)
- [x] 19-tier DAG implementation
- [x] Gate enforcement system
- [x] Anti-bias layer (AB1-AB6)
- [x] PMF scoring (≥30/50 threshold)
- [x] CLI commands (init/check/complete/pmf/status/assess/naming)

### Phase 2: ClaudeKit Integration (COMPLETED)
- [x] 23 base skills + ClaudeKit Engineer Kit (87 skills, 14 agents, 50+ commands)
- [x] ClaudeKit API docs (VidCap, ReviewWeb)
- [x] Valyu search integration
- [x] 7 base agents + ClaudeKit agents
- [x] 7 base commands + ClaudeKit commands

### Phase 3: Launch Readiness (IN PROGRESS)
- [ ] Landing page with waitlist
- [ ] GitHub repository setup (AIScale-Corp/product-tower-kit)
- [ ] npm package publication
- [ ] AB4: Real user interviews (remove placeholder)
- [ ] Product Hunt launch

### Phase 4: Validation (NEXT)
- [ ] 5+ user interviews
- [ ] 100+ waitlist signups
- [ ] Collect feedback
- [ ] PMF reassessment

### Phase 5: Revenue (Q3 2026)
- [ ] $49 Starter tier add-on launch
- [ ] $99 Pro tier add-on launch
- [ ] $199 Team tier add-on launch
- [ ] Payment integration (SePay, Polar, Stripe)
- [ ] ClaudeKit referral revenue

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
| ClaudeKit Engineer Kit | Latest | **Yes** | Skills, agents, commands, hooks (private repo at claudekit.cc/?ref=IJBRLXD6) |
| Node.js | ≥ 18.0.0 | Yes | CLI wrapper, syntax checks |
| Python 3 | Any | Yes | Gate enforcement, PMF scoring, Valyu search |
| PowerShell | Any | No | Harness health checks (Windows) |
| Claude Code | Latest | Yes | Skills, agents, commands execution |
| Valyu | Latest | No | Enhanced market research |
| ClaudeKit API | Latest | No | VidCap, ReviewWeb APIs |

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low AB4 completion | Medium | High | User interview guide, incentives |
| Adoption challenge | Medium | High | Vietnamese-first marketing, community |
| Claude Code changes | Low | Medium | Modular design, easy skill updates |
| Gate system too strict | Low | Medium | Force skip option, configurable thresholds |
| Python not installed | Medium | Low | Node.js fallback, clear error messages |
