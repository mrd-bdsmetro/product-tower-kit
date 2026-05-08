---
name: retro
version: 1.1.0
description: |
  Sprint retrospectives from git metrics and product data.
  For T14 feedback loop, sprint reviews, product iteration.
triggers:
  - "retro"
  - "retrospective"
  - "sprint review"
  - "feedback loop"
  - "đánh giá sprint"
---

# Retro - Sprint Retrospective

## Goal
Generate data-driven retrospectives for product iteration.

---

## Metrics to Gather

### Git Metrics
- Commits per day
- Lines of code changed
- File hotspots (most changed files)
- Commit type distribution (feat/fix/docs)
- Test file changes

### Product Metrics
- PMF score trend
- User feedback (NPS, CSAT)
- Feature completion rate
- Revenue trend
- Churn rate

### Process Metrics
- Sprint velocity
- Blocker count
- Scope changes
- Time to ship

---

## Process

### 1. Parse Timeframe
- Default: last 7 days
- Options: 7d, 2w, 1m, sprint, date range

### 2. Gather Raw Metrics
- Git log analysis
- Product analytics
- User feedback

### 3. Compute Derived Metrics
- Commit frequency trend
- Test-to-code ratio
- Churn rate
- Active day ratio
- Plan completion rate

### 4. Generate Report

---

## Output Format

```markdown
# Retro: [Sprint/Date]

## Summary
- Duration: X days
- Commits: X
- Features: X
- Fixes: X

## What Went Well
1. ...
2. ...

## What Didn't Go Well
1. ...
2. ...

## Metrics
| Metric | Value | Trend |
|--------|-------|-------|
| PMF Score | X/50 | ↑/↓ |
| Features shipped | X | ↑/↓ |
| Bugs fixed | X | ↑/↓ |
| User feedback | X | ↑/↓ |

## Action Items
1. ...
2. ...

## Next Sprint Focus
1. ...
2. ...
```

---

## Triggers for Retro

| Signal | Action |
|--------|--------|
| End of sprint | Run retro |
| PMF score changed | Analyze why |
| User churn > 10% | Investigate |
| Feature shipped | Measure impact |
| Revenue milestone | Celebrate + analyze |
