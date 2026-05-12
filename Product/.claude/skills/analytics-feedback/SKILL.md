---
name: analytics-feedback
version: 1.0.0
description: |
  T14 Post-Launch Feedback Loop skill. Monthly feedback loop.
  Data from GA4, Vercel, Supabase, Sentry.
triggers:
  - "analytics"
  - "feedback"
  - "post-launch"
  - "measure"
---

# Analytics & Feedback - T14

## Goal
Post-launch feedback loop. Measure → Learn → Iterate.

---

## 3-STEP LOOP (Repeat monthly)

### 1️⃣ MEASURE
- Analytics: traffic, engagement, conversion, churn
- Revenue: MRR, LTV, CAC
- NPS/CSAT from users

### 2️⃣ LEARN
- What worked? → DO MORE
- What didn't? → STOP or FIX
- What surprised? → INVESTIGATE

### 3️⃣ ITERATE
- Quick wins: fix trong 1 sprint
- Feature gaps: quay lại T8-T9
- Pivot signals: quay lại T1-T3

---

## TRIGGERS QUAY LẠI TOWER

| Signal | Quay lại tầng | Action |
|--------|-------------|--------|
| Churn > 10% | T4-T6 | Re-interview users |
| NPS < 30 | T7 | Re-validate PMF |
| CAC > LTV | T9.5 | Re-price |
| Feature request pattern | T8 | Update features |

---

## OUTPUT

```markdown
# T14: Feedback Loop - [Project]

## Metrics (Month X)
- Traffic: X
- Conversion: X%
- MRR: $X
- NPS: X
- Churn: X%

## Learnings
- What worked: ...
- What didn't: ...
- Surprises: ...

## Actions
- Quick wins: ...
- Feature gaps: ...
- Pivot signals: ...
```

**Output:** `data/t14_feedback_loop.md`
