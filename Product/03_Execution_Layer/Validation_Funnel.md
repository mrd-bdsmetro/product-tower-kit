---
status: active
type: validation
owner: MR.D
last_updated: 2026-05-12
tags: [funnel, validation, customer-journey, pmf]
pmf_impact: high
---

# Validation Funnel

## Overview
Maps the customer journey from initial idea to PMF validation. Each stage has clear gates and exit criteria.

## 5-Stage Funnel

```
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 1: IDEA                                                      │
│  ─────────────────────────────────────────────────────────────────  │
│  Entry: Product concept in mind                                     │
│  Exit:  T_Minus1 completed (Rapid Validation)                      │
│  Gate:  PMF potential score ≥ 25/50                                │
│  Files: 02_Instance_Layer/T_Series/t_minus1_rapid_validation.md     │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 2: COFFEE TALK                                               │
│  ─────────────────────────────────────────────────────────────────  │
│  Entry: 3-5 conversations with target customers                    │
│  Exit:  T0-T3 completed (Market Research → Segmentation)          │
│  Gate:  At least 1 "I would pay for this" signal                  │
│  Files: 02_Instance_Layer/T_Series/t0_*, t1_*, t2_*, t3_*          │
│  AB Gate: AB1 (Counter Search) completed                           │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 3: DEAL (Early Traction)                                     │
│  ─────────────────────────────────────────────────────────────────  │
│  Entry: 5+ conversations, 1+ paying customer or LOI                  │
│  Exit:  T4-T6 completed (Personas → Needs → Unmet Needs)           │
│  Gate:  PMF raw score ≥ 35/50                                      │
│  Files: 02_Instance_Layer/T_Series/t4_*, t5_*, t6_*                │
│  AB Gate: AB2-AB4 completed                                         │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 4: ACTIVE (Building)                                         │
│  ─────────────────────────────────────────────────────────────────  │
│  Entry: 3+ paying customers or signed LOIs                         │
│  Exit:  T7-T9.5 completed (PMF → Features → User Stories)          │
│  Gate:  PMF adjusted score ≥ 30/50                                 │
│  Files: 02_Instance_Layer/T_Series/t7_pmf.md, t8_*, t9_*           │
│  AB Gate: AB5-AB6 completed                                         │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 5: PMF (Product-Market Fit)                                  │
│  ─────────────────────────────────────────────────────────────────  │
│  Entry: 10+ paying customers, 60-day tenure                        │
│  Exit:  T14 completed (Feedback Loop)                              │
│  Gate:  PMF adjusted score ≥ 35/50 + 60% retention                 │
│  Files: 02_Instance_Layer/T_Series/t14_*.md                        │
└────────────────────────────────────────────────────────────────────┘
```

## Stage Metrics

| Stage | Metric | Target | Current |
|-------|--------|--------|---------|
| 1: Idea | Rapid validation score | ≥ 25/50 | — |
| 2: Coffee Talk | Conversations | 5+ | — |
| 2: Coffee Talk | "Would pay" signals | 1+ | — |
| 3: Deal | Early customers | 3+ | — |
| 3: Deal | PMF raw score | ≥ 35/50 | — |
| 4: Active | Paying customers | 10+ | — |
| 4: Active | PMF adjusted | ≥ 30/50 | — |
| 5: PMF | 60-day retention | ≥ 60% | — |
| 5: PMF | PMF adjusted | ≥ 35/50 | — |

## Funnel Analytics

### Conversion Rates

| Transition | Target | Warning | Critical |
|------------|--------|---------|----------|
| Idea → Coffee Talk | 60% | 40-59% | < 40% |
| Coffee Talk → Deal | 40% | 25-39% | < 25% |
| Deal → Active | 50% | 30-49% | < 30% |
| Active → PMF | 40% | 25-39% | < 25% |

### Anti-Bias Gates

Each stage requires passing the corresponding anti-bias challenge:

```
Stage 1: No AB gate (initial validation)
Stage 2: AB1 - Counter Search (challenge assumptions)
Stage 3: AB2 - Red Team (adversarial review)
Stage 4: AB3 - Field Notes + AB4 - User Interview
Stage 5: AB5 - Strategic Analysis + AB6 - Founder Insight
```

## Dependency Map

```
T_Minus1 → T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8 → T9 → T9.5 → T14
   ↓        ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓     ↓
  AB1      AB1  AB1  AB1  AB1  AB2  AB3  AB4  AB5  AB6  AB6  AB6   DONE
```

## Kill Triggers

Stop validation if:
- Coffee Talk stage: < 3 conversations in 14 days
- Deal stage: No "would pay" signal in 30 days
- Active stage: Churn > 30% in first 30 days
- PMF stage: Retention < 40% at 60 days

---
*Validation Funnel v1.6.0 — Customer journey from idea to PMF*