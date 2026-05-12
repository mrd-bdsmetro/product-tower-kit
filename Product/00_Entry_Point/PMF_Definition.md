---
status: active
type: entry
owner: MR.D
last_updated: 2026-05-12
tags: [pmf, definition, threshold, measurement]
pmf_impact: high
---

# PMF Definition

## What is PMF?

Product-Market Fit (PMF) is achieved when your product satisfies strong market demand. According to Marc Andreessen: **"The only thing that matters is getting to product-market fit."**

## PMF Measurement

Product Kit uses a quantitative PMF score with the following formula:

```
PMF Adjusted = Raw Score + Penalty
PMF Scale: 50 points
PMF Threshold: 30/50 (GO decision)
```

### Raw Score Components (50 points)

| Component | Max Points | Weight |
|------------|------------|--------|
| **Customer Validation** | | |
| - Coffee talks completed | 5 | 10% |
| - "Would pay" signals | 5 | 10% |
| - Paying customers (LOI accepted) | 10 | 20% |
| **Evidence Quality** | | |
| - T-Series completion (T0-T7) | 10 | 20% |
| - Anti-bias challenges passed (AB1-AB6) | 5 | 10% |
| **Market Traction** | | |
| - Early revenue | 5 | 10% |
| - Customer retention (30-day) | 5 | 10% |
| - NPS score | 5 | 10% |

### Penalty Adjustments

| Risk Factor | Penalty |
|-------------|---------|
| Solo founder | -5 |
| No technical co-founder | -3 |
| Market timing uncertain | -2 |
| Competitive landscape crowded | -2 |
| Regulatory uncertainty | -2 |

## PMF Stages

| Stage | Score | Decision |
|-------|-------|----------|
| **Pre-PMF** | 0-19 | NO-GO: Keep validating |
| **Approaching PMF** | 20-29 | CAUTION: Accelerate validation |
| **PMF Achieved** | 30-39 | GO: Start scaling |
| **Strong PMF** | 40-50 | GO: Raise capital, scale fast |

## Current PMF Score

| Metric | Value |
|--------|-------|
| **Raw Score** | TBD |
| **Penalty** | TBD |
| **Adjusted Score** | TBD |
| **Stage** | Pre-PMF |
| **Last Updated** | 2026-05-12 |

## How to Calculate

1. Complete T-Series (T0-T9.5)
2. Pass Anti-Bias challenges (AB1-AB6)
3. Run: `npm run test:invariants`
4. Review in: `03_Execution_Layer/validation_tracker.md`

## PMF vs Features

> "Don't worry about features until you have PMF. Features are how you get to PMF, not the goal." — Marc Andreessen

**Focus:** Customer validation first, feature development second.

---
*PMF Definition v1.6.0*