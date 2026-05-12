---
status: "in-progress"
type: "instance"
owner: "MR.D"
last_updated: "2026-05-12"
tags: [feedback-loop, iteration, learning, pmf]
pmf_impact: "high"
---

# T14: Feedback Loop

## Overview

T14 is the final tier in the Product Tower validation framework. It establishes a systematic **Feedback Loop** that connects user behavior back to product decisions, completing the cycle from market research to continuous improvement.

> **Per the Product Management Tower:** "The loop is what makes products improve over time, not features."

## Purpose

1. **Close the validation cycle** — Connect insights back to market understanding
2. **Measure PMF health over time** — Track if PMF is strengthening or weakening
3. **Drive iteration** — Use data to decide what to build next
4. **Build accountability** — Regular review prevents stagnation

## Feedback Loop Framework

```
┌─────────────────────────────────────────────────────────────┐
│                    FEEDBACK LOOP CYCLE                       │
│                                                              │
│    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│    │  USER   │───▶│ PRODUCT │───▶│ MEASURE  │───▶│ LEARN    │ │
│    │ ACTION  │    │ RESPONSE│    │ METRICS  │    │ INSIGHT  │ │
│    └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│         ▲                                              │ │
│         └──────────────────────────────────────────────┘ │
│                         FEEDBACK                            │
└─────────────────────────────────────────────────────────────┘
```

## Key Metrics to Track

### North Star Metric

| Metric | Definition | Target | Current |
|--------|------------|--------|---------|
| **Weekly Active Validators** | Number of users running validation per week | 10 | 1 |

### Engagement Metrics

| Metric | Definition | Target | Current |
|--------|------------|--------|--------|
| **T-tier completion rate** | % of started tiers completed | > 80% | — |
| **Time to PMF** | Days from T-1 to PMF score ≥ 30 | < 60 days | — |
| **Feature adoption** | % of users using advanced features | > 50% | — |
| **Retention** | % of users returning after 30 days | > 60% | — |

### PMF Health Score

Track quarterly:

| Component | Questions to Answer |
|-----------|-------------------|
| **Retention** | Are users coming back? |
| **NPS** | Would users recommend? |
| **Expansion** | Are users paying more? |
| **Churn** | Why do users leave? |

## Feedback Collection Methods

### 1. Direct Feedback

| Method | Frequency | Tool |
|--------|-----------|------|
| **Weekly checkpoint** | Weekly | `03_Execution_Layer/weekly_checkpoint.md` |
| **User interviews** | Monthly | AB4 tier |
| **Survey (NPS)** | Quarterly | Google Forms / Notion |
| **Support tickets** | Real-time | Email / Discord |

### 2. Behavioral Feedback

| Signal | What It Tells You |
|--------|-------------------|
| **Which T-tiers are skipped** | Too complex or not relevant |
| **Time spent per tier** | Difficulty level |
| **Where users drop off** | Funnel holes |
| **Feature usage patterns** | What users actually need |

### 3. Market Feedback

| Source | What to Monitor |
|--------|-----------------|
| **Competitor moves** | New features, pricing changes |
| **Market trends** | Emerging needs |
| **Regulatory changes** | New requirements |
| **Technology shifts** | New possibilities |

## Feedback Integration Process

### Step 1: Collect (Weekly)

```markdown
## Weekly Feedback Collection
- Review support tickets
- Check user engagement metrics
- Update stakeholder_feedback.md
```

### Step 2: Analyze (Monthly)

```markdown
## Monthly Analysis
1. Aggregate feedback themes
2. Identify top 3 pain points
3. Calculate NPS score
4. Update PMF health assessment
```

### Step 3: Decide (Quarterly)

```markdown
## Quarterly Decision Framework
| Feedback | Frequency | Impact | Decision |
|----------|-----------|--------|----------|
| NPS drop | Quarterly | High | Emergency review |
| Feature request | Weekly | Medium | Roadmap update |
| UI issue | Real-time | Low | Quick fix |
```

### Step 4: Act (Ongoing)

```markdown
## Action Items from Feedback
1. **P0** - PMF risk detected → Immediate review
2. **P1** - Top user pain → Next sprint
3. **P2** - Nice to have → Backlog
```

## Learning Loop

After each feedback cycle:

1. **What worked?** → Keep doing it
2. **What didn't work?** → Stop or change
3. **What should we try?** → New hypothesis
4. **What did we learn?** → Document in `04_Learning_Layer/`

## Customer Feedback Template

```markdown
## Feedback from [Source] - YYYY-MM-DD

### Summary
[1-2 sentence summary of feedback]

### Detailed Feedback
[Full feedback or quote]

### Source
- Name: [Anonymous or name]
- Role: [User type]
- Product: [Which product/version]

### Our Response
[How we're addressing this]

### Status
- [ ] Addressed
- [ ] In progress
- [ ] Won't do (reason: ...)

### Related Decision
[Link to decision_log.md if applicable]
```

## PMF Health Assessment

### Quarterly PMF Check

| Metric | Q1 | Q2 | Q3 | Q4 | Trend |
|--------|----|----|----|----|-------|
| NPS Score | | | | | |
| Retention | | | | | |
| Feature usage | | | | | |
| PMF Score | | | | | |

### PMF Health Indicators

| State | Symptoms | Action |
|-------|----------|--------|
| **Strong PMF** | Growth > 20%/week, NPS > 50 | Scale, don't change |
| **Weakening PMF** | Slowdown, NPS drop | Identify issue, fix fast |
| **No PMF** | Stagnation, churn | Re-validate from T0 |

## Integration with Other Tiers

| Tier | Connection |
|------|------------|
| **T-1** | Feedback loop starts from first validation |
| **T7** | PMF score is the North Star we track |
| **T8** | Features to build come from feedback |
| **AB6** | Founder insight drives the loop |

## Next Steps

- [ ] Set up weekly feedback collection ritual
- [ ] Create NPS survey
- [ ] Define baseline metrics
- [ ] Review feedback quarterly
- [ ] Document learnings in `04_Learning_Layer/`

## Resources

- Previous learnings: `04_Learning_Layer/lessons_learned.md`
- Stakeholder feedback: `04_Learning_Layer/stakeholder_feedback.md`
- Decision log: `03_Execution_Layer/decision_log.md`

---
*T14: Feedback Loop v1.0.0 — Complete the validation cycle*