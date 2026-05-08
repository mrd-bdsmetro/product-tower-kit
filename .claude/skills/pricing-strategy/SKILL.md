---
name: pricing-strategy
version: 1.0.0
description: |
  T9.5 Offer Bridge skill. Pricing model selection, Value Equation, WTP validation.
triggers:
  - "pricing"
  - "offer"
  - "giá"
  - "bán thế nào"
---

# Pricing Strategy - T9.5

## Goal
Design offer bridge: pricing + guarantee + CTA. Bridge giữa "build gì" và "bán thế nào".

---

## PRICING MODELS (6 models)

| Model | Khi nào | Example |
|-------|----------|---------|
| Freemium | SaaS, tool | Free tier → paid features |
| Subscription | Recurring value | $9-29/month |
| One-time | Toolkit, course | $49-199 |
| Usage | API, cloud | Pay per use |
| Tiered | Multiple segments | Basic/Pro/Enterprise |
| Hybrid | Complex product | Free + paid add-ons |

---

## VALUE EQUATION (Hormozi)

```
Value = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort)
```

- Dream Outcome: What user wants
- Perceived Likelihood: Trust that it works
- Time Delay: How fast
- Effort: How easy

---

## WTP VALIDATION

Source: AB4 user interview + AB6 founder insight

```markdown
| Segment | WTP Range | Source | Confidence |
|---------|-----------|--------|------------|
```

---

## OUTPUT

```markdown
# T9.5: Offer Bridge - [Project]

## PRODUCT ROUTE (SaaS/App/Tool):
- Pricing model: [model]
- Price point: $X - DATA: from AB4/AB6
- Guarantee: [type]
- CTA: [main action]
- Lead Magnet: [free tool/demo/trial]

## SERVICE ROUTE (Advisory/Consulting):
- → Route to sales-tower S4 Grand Slam Offer
```

**Output:** `data/t9_5_offer_bridge.md`

---

## GATE
- T9 (features + user stories) must be complete
- Pricing validation required (from AB4/AB6 data)
