---
status: active
type: architecture
owner: MR.D
last_updated: 2026-05-12
tags: [6-elements, success-factors, balance, framework]
pmf_impact: high
---

# 6 Success Factors Framework

## Overview

Per the Product Management Tower (video #coroference): **A product must satisfy ALL 6 elements simultaneously to succeed.** If you only balance User and Business, you're already in trouble.

```
┌─────────────────────────────────────────────────────────────┐
│                    6 ELEMENTS BALANCE                       │
│                                                             │
│        User Desirability ←→ Business Viability             │
│               ↕                         ↕                  │
│         User Interface    ←→    Technical Feasibility       │
│               ↕                         ↕                  │
│         User Experience   ←→    User Utility               │
│                                                             │
│         "The Seesaw of Product Success"                     │
└─────────────────────────────────────────────────────────────┘
```

## The 6 Elements

| Element | Vietnamese | Definition | Example |
|---------|------------|------------|---------|
| **User Desirability** | Khách hàng "yêu" cực mạnh | Emotional attachment, brand love | Apple butterfly keyboard - tệ nhưng fan vẫn mua |
| **User Interface** | Đẹp, rõ ràng, hài hòa | Visual design, typography, colors | "Great design is invisible" |
| **User Experience** | Cảm xúc, flow mượt mà | Journey, touchpoints, no manual needed | iPhone - không cần hướng dẫn |
| **User Utility** | Giải quyết nhu cầu thật sự | Job-to-be-done, effectiveness | Giúp user làm việc hiệu quả |
| **Business Viability** | Có lãi, không làm từ thiện | Revenue model, unit economics | Model kiếm tiền rõ ràng |
| **Technical Feasibility** | Khả năng kỹ thuật | Build vs Buy, MVP scope | Team dev làm được |

---

## Element 1: User Desirability

**"Khách hàng 'yêu' cực mạnh"**

### In Product Kit

| File | Coverage | Status |
|------|----------|--------|
| `00_Entry_Point/Value_Proposition.md` | Why kit exists, emotional hook | ✅ Complete |
| `00_Entry_Point/Product_Kit_Tower.md` | 12-layer framework | ✅ Complete |
| `04_Learning_Layer/stakeholder_feedback.md` | NPS tracking | ✅ New |

### Kit Desirability Score

| Metric | Target | Current | Gap |
|--------|--------|---------|-----|
| NPS Score | > 40 | TBD | Need feedback |
| "Would recommend" | > 50% | TBD | Need feedback |
| Emotional hook clarity | "Validate before build" | ✅ | OK |

### How Kit Creates Desirability

```
Story: "Tao build xong mới biết không ai cần"
     ↓
Solution: "Product Tower Kit giúp validate TRƯỚC"
     ↓
Desirability: 15 phút để bắt đầu, không cần tool phức tạp
     ↓
Evidence: PMF score rõ ràng, không guess
```

### What Creates "Apple Fan" Loyalty in Kit

1. **Simplicity** — One command to start (`npm run init`)
2. **Clarity** — PMF score vs gut feeling
3. **Structure** — ADHD-friendly, clear next action
4. **Credibility** — Based on Marc Andreessen's PMF definition

---

## Element 2: User Interface

**"Đẹp, rõ ràng, hài hòa"**

### In Product Kit

| File | Coverage | Status |
|------|----------|--------|
| `05_Design_System/` | TypeScript components, tokens | ✅ Complete |
| `.claude/skills/*/SKILL.md` | 21 skill interfaces | ✅ Complete |

### UI Quality Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Design tokens defined | 100% | ✅ |
| Components documented | 21 skills | ✅ |
| Consistent typography | Yes | ✅ |

### "Great design is invisible" in Kit

- **Quick_Start_Guide.md** — One page, no clutter
- **INDEX.md** — Visual navigation, no walls of text
- **Product_Kit_Tower.md** — ASCII diagram, no external tool needed

---

## Element 3: User Experience

**"Cảm xúc, flow mượt mà"**

### In Product Kit

| File | Coverage | Status |
|------|----------|--------|
| `03_Execution_Layer/Customer_Journey_Map.md` | 5-phase emotional journey | ✅ Complete |
| `00_Entry_Point/Quick_Start_Guide.md` | 15-min onboarding | ✅ Complete |

### UX Journey Phases

```
Phase 1: Awareness        → Skeptic → Curious 😊
Phase 2: Consideration    → Overwhelmed → Deciding 🤔
Phase 3: Activation       → Excited → Accomplished 😊
Phase 4: Validation       → Challenged → Validated 🥹
Phase 5: PMF Decision     → Anxious → Relieved (or 😐 if No-Go)
```

### North Star Metric

**"Time from init to first T-tier completed"**

- Target: < 30 minutes
- Current: ~45 minutes
- Why: First-time setup friction

### UX Improvements Needed

| Phase | Issue | Fix |
|-------|-------|-----|
| Activation | Setup takes 45 min | Add `--quick` flag |
| Validation | Solo discipline hard | Add daily reminder hook |
| Decision | No-Go feels like failure | Add "pivot guidance" |

---

## Element 4: User Utility

**"Giải quyết nhu cầu thật sự"**

### In Product Kit

| File | Coverage | Status |
|------|----------|--------|
| `02_Instance_Layer/T_Series/t5_user_needs.md` | Needs analysis | ✅ |
| `02_Instance_Layer/T_Series/t6_underserved_needs.md` | Underserved needs (GOLD) | ✅ |
| `00_Entry_Point/PMF_Definition.md` | PMF as utility measure | ✅ |
| `03_Execution_Layer/Business_Viability.md` | Job-to-be-done | ✅ |

### Utility: Job-to-be-Done Framework

```
Statement: "When [situation], I want to [motivation], so I can [expected outcome]"

Examples for Product Kit:
- When I have a product idea, I want to validate it quickly, so I don't waste 6 months building nothing
- When I'm unsure about PMF, I want a score, so I can make a GO/NO-GO decision
- When I'm stuck, I want clear next action, so I can move forward
```

### Utility Metrics

| Metric | Target | How Measured |
|--------|--------|---------------|
| Problem solved | Yes | User feedback |
| Time saved | > 10 hrs/project | User estimation |
| Confidence increase | +50% | Self-reported |

---

## Element 5: Business Viability

**"Có lãi, không làm từ thiện"**

### In Product Kit

| File | Coverage | Status |
|------|----------|--------|
| `03_Execution_Layer/Business_Viability.md` | Full business model | ✅ Complete |

### Business Model Summary

| Item | Value |
|------|-------|
| **Pricing** | Free (T0-T3), $29/mo (Pro), $79/mo (Team) |
| **CAC Target** | < $15 |
| **LTV Target** | $150 |
| **LTV:CAC Target** | > 3:1 |
| **Break-even** | 3 paying users |

### Unit Economics

| Metric | Target | Formula |
|--------|--------|---------|
| CAC | < $15 | Marketing spend / Signups |
| LTV | > $150 | ARPU × Subscription length |
| LTV:CAC | > 3:1 | LTV / CAC |
| Payback | < 3 months | CAC / (ARPU - variable cost) |

### Market Sizing

| Level | Size | Notes |
|-------|------|-------|
| TAM | 65,000 | Vietnam solo founders |
| SAM | 1,000 | Willing to pay |
| SOM (Y1) | 50 | 5% of SAM |

---

## Element 6: Technical Feasibility

**"Có khả năng kỹ thuật thực hiện được"**

### In Product Kit

| File | Coverage | Status |
|------|----------|--------|
| `03_Execution_Layer/Technical_Feasibility.md` | MVP, Build vs Buy | ✅ Complete |
| `06_Tools_Stack/Tools_Stack.md` | Tool-layer mapping | ✅ Complete |

### Build vs Buy Matrix

| Category | Decision | Rationale |
|----------|----------|-----------|
| Markdown editing | Buy | Obsidian is best-in-class |
| Auth | Buy | Clerk/Auth0 better than build |
| Database | Buy | Supabase handles scale |
| Search | Build | Integration is differentiation |
| PMF scoring | Build | Core algorithm |
| Validation logic | Build | Core differentiation |

### MVP Scope

| Priority | Feature | Status |
|----------|---------|--------|
| P0 | Markdown templates | ✅ |
| P0 | Gate checker CLI | ✅ |
| P0 | Health check | ✅ |
| P1 | Search providers | ✅ |
| P2 | Notion sync | Post-PMF |
| P2 | API access | Post-PMF |

---

## Balancing the 6 Elements

### The Seesaw Principle

```
If you only balance User + Business:
        User ←→ Business
           ⚠️
   You're already in trouble!

Because Technical Feasibility is the third leg.

Correct balance:
        User ←→ Business
          ↕         ↕
    Technical ←→ Utility
```

### Balance Check

| Element Pair | Balanced? | Evidence |
|--------------|----------|----------|
| User Desirability ↔ Business Viability | ⚠️ | Need revenue validation |
| UI ↔ Technical Feasibility | ✅ | Obsidian + CLI approach |
| UX ↔ User Utility | ⚠️ | Need faster activation |

### Risk: Over-emphasizing One Element

| Over-emphasis | Consequence |
|---------------|-------------|
| User Desirability | Fanboy but no revenue |
| UI | Beautiful but useless |
| UX | Smooth but doesn't solve problem |
| Utility | Useful but ugly/hard to use |
| Business Viability | Greedy, users leave |
| Technical Feasibility | "We built it, nobody cares" |

---

## 6 Elements Checklist

### User Desirability
- [ ] Clear emotional hook ("Validate before build")
- [ ] Brand story resonates with solo founder
- [ ] NPS tracking in place

### User Interface
- [ ] Design tokens defined
- [ ] 21 skills documented
- [ ] Consistent visual language

### User Experience
- [ ] Customer Journey Map created
- [ ] < 30 min to first T-tier
- [ ] No manual needed for basics

### User Utility
- [ ] Job-to-be-done clear
- [ ] Problem solved demonstrated
- [ ] Time savings quantified

### Business Viability
- [ ] Pricing model defined
- [ ] CAC/LTV calculated
- [ ] Break-even analysis done

### Technical Feasibility
- [ ] MVP scope defined
- [ ] Build vs Buy decisions made
- [ ] Tech stack validated

---

## Integration with Product Tower Layers

```
Target Market → Segmentation → Personas → Needs → Underserved Needs
     ↓              ↓             ↓         ↓           ↓
 Layer 12        Layer 11     Layer 10   Layer 9    Layer 8 (GOLD)
     ↓              ↓             ↓         ↓           ↓
  Desirability  Interface     UX      Utility    Technical (Base)
     ↓              ↓             ↓         ↓           ↓
 Business ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←← Feasibility
```

### File-to-Element Mapping

| Element | Files |
|---------|-------|
| User Desirability | `00_Entry_Point/Value_Proposition.md`, `00_Entry_Point/Product_Kit_Tower.md` |
| User Interface | `05_Design_System/`, `.claude/skills/*/` |
| User Experience | `03_Execution_Layer/Customer_Journey_Map.md`, `00_Entry_Point/Quick_Start_Guide.md` |
| User Utility | `02_Instance_Layer/T_Series/t5_*`, `02_Instance_Layer/T_Series/t6_*`, `00_Entry_Point/PMF_Definition.md` |
| Business Viability | `03_Execution_Layer/Business_Viability.md` |
| Technical Feasibility | `03_Execution_Layer/Technical_Feasibility.md`, `06_Tools_Stack/Tools_Stack.md` |

---
*6 Success Factors Framework v1.8.0 — Based on Product Management Tower video #coroference*