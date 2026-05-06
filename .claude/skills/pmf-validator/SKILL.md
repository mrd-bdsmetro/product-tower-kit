---
name: pmf-validator
version: 1.0.0
description: |
  T7 PMF Validation skill. 10 PMF signals, Sean Ellis Test, PMF scoring with penalty system.
  HARD GATE: PMF(adjusted) < 30/50 = BLOCKED.
triggers:
  - "PMF"
  - "validate PMF"
  - "product-market fit"
  - "check PMF"
---

# PMF Validator — T7

## Goal
Validate Product-Market Fit với scoring system. HARD GATE cho T8+.

---

## 10 PMF SIGNALS (0-5 each, /50 total)

| # | Signal | Weight | Score |
|---|--------|--------|-------|
| 1 | Problem-Solution Fit | 5 | /5 |
| 2 | User Willingness to Pay | 5 | /5 |
| 3 | Organic Growth | 5 | /5 |
| 4 | Retention Rate | 5 | /5 |
| 5 | NPS Score | 5 | /5 |
| 6 | Feature Request Quality | 5 | /5 |
| 7 | Competitor Comparison | 5 | /5 |
| 8 | Market Timing | 5 | /5 |
| 9 | Distribution Channel | 5 | /5 |
| 10 | Revenue Potential | 5 | /5 |

---

## SEAN ELLIS TEST

> "How would you feel if you could no longer use [product]?"
> - Very disappointed: ≥40% = PMF signal
> - Somewhat disappointed: 25-40% = close
> - Not disappointed: <25% = no PMF

---

## PMF SCORING

```
PMF RAW = Sum of 10 signals (0-50)
PMF ADJUSTED = RAW + penalty/bonus

Penalty table:
  Desk research only     → -10
  + AB1 (counter-search) → -5
  + AB1 + AB2 (red team) → -2.5
  + AB1-AB4 (full)       → 0
  + AB1-AB5 (strategic)  → +0.5
  + AB1-AB6 (founder)    → +1.5

Threshold: PMF(adjusted) ≥ 30/50 = GO
```

---

## OUTPUT

```markdown
# T7: PMF Validation — [Project]

## PMF Signals
| # | Signal | Score | Evidence |
|---|--------|-------|----------|

## Sean Ellis Test
- Very disappointed: X%
- Somewhat disappointed: X%
- Not disappointed: X%

## PMF Score
- Raw: X/50
- Penalty: X
- Adjusted: X/50
- Threshold: 30/50

## Decision: GO / NO-GO
- Reasoning: ...
```

**Output:** `data/t7_pmf.md`

---

## GATE
- AB1-AB4 ALL complete (or force skip with penalty)
- PMF(adjusted) ≥ 30/50 = PASS → T8
- PMF(adjusted) < 30/50 = BLOCKED → pivot to T1 or T4
