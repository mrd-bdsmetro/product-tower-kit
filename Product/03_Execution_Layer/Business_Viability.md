---
status: active
type: business
owner: MR.D
last_updated: 2026-05-12
tags: [business, revenue, pricing, unit-economics, viability]
pmf_impact: high
---

# Business Viability

## Overview
Business Viability ensures the product can make money and sustain operations. According to the Product Management Tower, this must be validated BEFORE building features.

**Key Principle:** "If you only balance User and Business, you're already in trouble. Technical Feasibility is the third leg." — Video #coroference

## Revenue Model

### Primary Model: SaaS Subscription

| Tier | Price | Features | Target |
|------|-------|----------|--------|
| **Free** | $0 | T_Minus1, T0-T3, Basic tracking | Trial users |
| **Pro** | $29/mo | Full T0-T14, AB challenges, Export | Solo founders |
| **Team** | $79/mo | 3 seats, Priority support, API | Early startups |

### Revenue Streams

| Stream | % Revenue | Status |
|--------|-----------|--------|
| Subscription (Pro + Team) | 70% | Primary |
| One-time services (setup, training) | 20% | Secondary |
| Enterprise customization | 10% | Future |

### Pricing Psychology

| Principle | Application |
|-----------|-------------|
| Anchoring | Show $99/mo Enterprise, highlight $29 Pro |
| Freemium | Let users taste T0-T3 free, gate T4+ |
| Annual discount | 2 months free = 14% discount |

## Unit Economics

### Customer Acquisition Cost (CAC)

| Channel | Cost | Conversion | CAC |
|---------|------|------------|-----|
| Content (YouTube, Blog) | $200/mo | 50 signups | $4 |
| Community (LinkedIn, Twitter) | $100/mo | 20 signups | $5 |
| Paid ads (Meta, Google) | $500/mo | 25 signups | $20 |
| Referral (organic) | $0 | 10 signups | $0 |

**Target CAC:** < $15
**Average CAC:** $9.67

### Lifetime Value (LTV)

| Metric | Value |
|--------|-------|
| Average MRR per user | $25 |
| Average subscription length | 6 months |
| LTV (simple) | $150 |
| LTV (with expansion) | $200 |

### LTV:CAC Ratio

| Ratio | Status | Implication |
|-------|--------|-------------|
| < 1:1 | ❌ | Losing money per customer |
| 1:1 - 3:1 | ⚠️ | Need to improve |
| 3:1 - 5:1 | ✅ | Healthy |
| > 5:1 | 🚀 | Excellent, scale fast |

**Current Target:** 15:1 (too early to measure)

### Payback Period

| Metric | Target | Current |
|--------|--------|---------|
| Payback period | < 3 months | TBD |

## Market Sizing (from Target_Market.md)

| Market Level | Size | Notes |
|--------------|------|-------|
| TAM | 65,000 | Vietnam solo founders + indie hackers |
| SAM | 1,000 | Willing to pay $29/mo |
| SOM (Year 1) | 50 | 5% of SAM |
| SOM (Year 2) | 200 | 20% of SAM |

### Revenue Projections

| Year | Users | ARPU | Revenue |
|------|-------|------|---------|
| Year 1 | 50 | $25/mo | $15,000/yr |
| Year 2 | 200 | $30/mo | $72,000/yr |
| Year 3 | 500 | $35/mo | $210,000/yr |

## Cost Structure

### Fixed Costs (Monthly)

| Item | Cost | Notes |
|------|------|-------|
| Hosting (Vercel) | $20 | Pro plan |
| Domain | $10 | annual proration |
| Tools (Notion, Obsidian) | $30 | Team subscriptions |
| **Total Fixed** | $60/mo | |

### Variable Costs (Per Customer)

| Item | Cost | Notes |
|------|------|-------|
| Support | $2 | 30 min/customer/month |
| Infrastructure | $1 | Per active user |
| **Total Variable** | $3/user | |

### Break-even Analysis

| Metric | Value |
|--------|-------|
| Fixed costs | $60/mo |
| Variable per user | $3 |
| Price (Pro) | $29 |
| **Break-even users** | 3 (paying) |

## Business Viability Checklist

- [ ] Revenue model defined
- [ ] Pricing tested with 3+ users
- [ ] CAC calculated
- [ ] LTV estimated
- [ ] Break-even analysis done
- [ ] Market sizing validated

## Integration with Validation Funnel

```
Idea → Coffee Talk → Deal → Active → PMF
   ↓         ↓         ↓        ↓       ↓
  None    Business  Business  Business  Business
          Viability Viability Viability Viability
                       ↓
               Can we make money?
               Break-even: 3 users ✅
```

## Next Steps

1. **Validate pricing** with 5 early users
2. **Track CAC** from first marketing campaign
3. **Calculate LTV** after 6 months of retention data

---
*Business Viability v1.7.0 — Revenue model, pricing, and unit economics*