---
name: product-tower
version: 1.1.0
description: |
  Product Tower Kit - Master Orchestrator. 14-tier product management framework.
  Anti-Bias enforcement (AB1-AB6). PMF gate system.
  For vibe coders, startup founders, freelancers, agencies.
  Routes to 5 agents + 12 skills. ADHD-friendly.
triggers:
  - "build product"
  - "product plan"
  - "product strategy"
  - "product tower"
  - "validate idea"
  - "chạy product tower"
  - "build cái gì"
  - "nên ship gì"
  - "vibe code"
  - "startup"
  - "MVP"
---

# Product Tower Kit - Master Orchestrator

## Goal
Điều phối quá trình build sản phẩm theo mô hình **Product Tower 14 tầng**.
Mọi quyết định product dựa trên data + user insight, không dựa cảm tính founder.

> **Target**: Vibe coders, startup founders, freelancers, agencies, solo founders
> **Nguyên tắc**: User-Centric, Not CEO-Centric. Validate before you code.

---

## PRODUCT TOWER - OVERVIEW

```
┌─────────────────────────────────────┐
│  14. Feedback Loop 🔄               │ ← MEASURE & ITERATE
│      GA4 + Vercel + Supabase        │   → analytics-feedback skill
├─────────────────────────────────────┤
│  13. QA / Validation                │ ← BUILD
│  12. Development                    │   → external agents
├─────────────────────────────────────┤
│  11. UI Design                      │ ← DESIGN
│  10. UX Design                      │   → external agents
├─────────────────────────────────────┤
│ 9.5. Offer Bridge 💰                │ ← OFFER DESIGN
│      pricing + guarantee + CTA      │   → pricing-strategy skill
├─────────────────────────────────────┤
│   9. User Stories                   │ ← PRODUCT
│   8. Feature Set                    │   → feature-scoper agent
├─────────────────────────────────────┤
│   7. Value Prop + PMF  ⭐⭐⭐        │ ← STRATEGY (HARD GATE)
│                                     │   → pmf-validator skill
├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│  🔴 ANTI-BIAS LAYER (MANDATORY)    │ ← ENFORCEMENT
│      AB1: Counter-search            │   → anti-bias-challenger agent
│      AB2: Red team / Sparring       │   → anti-bias-challenger agent
│      AB3: Field observation         │   → manual or API
│      AB4: User interview (min 5)    │   → manual (Mom Test)
│      AB5: Strategic analysis ⭐     │   → anti-bias-challenger agent
│      AB6: Founder insight 💰        │   ⚠️ MANDATORY cho solo founder
├─────────────────────────────────────┤
│   6. Unmet Needs ⭐                 │ ← DISCOVERY
│   5. User Needs (Prioritized)       │   → user-discovery skill
│   4. User Personas                  │
├─────────────────────────────────────┤
│   3. Segment Filter                 │ ← FOUNDATION
│   2. Market Segmentation            │   → market-segmentation skill
│   1. Target Market                  │
├─────────────────────────────────────┤
│   0. Market Research  🔍            │ ← DATA
│      0-CP. Competitive Positioning   │   → market-research skill
└─────────────────────────────────────┘
```

---

## NGUYÊN TẮC CỐT LÕI

1. **User-Centric** - Mọi thứ xuất phát từ user needs, không từ ý tưởng founder
2. **Validate Before Build** - Test giả thuyết TRƯỚC KHI viết code
3. **No PMF = No Scale** - Tầng 7 là hard gate. PMF(adjusted) < 30/50 = KHÔNG lên tầng 8+
4. **Data-Driven** - Quantitative (WHAT happened) + Qualitative (WHY happened)
5. **Anti-Bias Enforced** - Counter-search + red team TRƯỚC KHI chấm PMF
6. **Real Data Required** - AI desk research ≠ truth. Interview/observation = bắt buộc
7. **Friction = Feature** - Không shortcut. Khó = đúng.

---

## SCOPE

```
Product Tower OWN:    T0-T9.5 (Research → Market → User → PMF → Scope → Offer)
Product Tower POINT:  T10-T14  (Design → Build → QA → Feedback) → delegate
```

> Product Tower = **WHAT to build + WHY + HOW TO SELL.**

---

## ROUTING TABLE

| User nói | Skill | Agent | Tầng | Gate |
|----------|-------|-------|------|------|
| "research", "data thị trường" | market-research | market-researcher | T0 | None |
| "competitive", "đối thủ" | competitor-analysis | anti-bias-challenger | T0-CP | None |
| "target market", "phân khúc" | market-segmentation | product-planner | T1-T3 | T0 done? |
| "persona", "user needs" | user-discovery | product-planner | T4-T6 | T3 done? |
| "counter", "phản biện" | - | anti-bias-challenger | AB1 | T4 done? |
| "red team", "sparring" | - | anti-bias-challenger | AB2 | AB1 done? |
| "field observation" | - | - | AB3 | AB2 done? |
| "interview user" | - | - | AB4 | AB3 done? |
| "PMF", "validate" | pmf-validator | pmf-validator | T7 | AB1-AB4 ALL? |
| "feature", "user story" | - | feature-scoper | T8-T9 | PMF ≥ 30? |
| "offer", "pricing" | pricing-strategy | feature-scoper | T9.5 | T9 done? |
| "analytics", "feedback" | analytics-feedback | - | T14 | Post-launch |

---

## ANTI-BIAS LAYER (MANDATORY - giữa T4 và T7)

| Step | Tool | Output file |
|------|------|-------------|
| **AB1** | search_web | `data/ab1_counter_search.md` |
| **AB2** | anti-bias-challenger agent | `data/ab2_red_team.md` |
| **AB3** | Google Maps API / manual | `data/ab3_field_notes.md` |
| **AB4** | Manual (Mom Test) | `data/ab4_user_interview.md` |
| **AB5** ⭐ | anti-bias-challenger agent | `data/ab5_strategic_analysis.md` |
| **AB6** ⭐ | Manual (founder) | `data/ab6_founder_insight.md` |

### PMF Adjustment Rules (Scale /50):

```
PMF RAW (desk research)              → AUTO -10 penalty
PMF + AB1 (counter-search)           → -5 penalty
PMF + AB1 + AB2 (red team)           → -2.5 penalty
PMF + AB1-AB4 (full anti-bias)       → NO penalty
PMF + AB1-AB5 (full + strategic)     → +0.5 BONUS
PMF + AB1-AB6 (full + founder)       → +1.5 BONUS

Threshold: PMF(adjusted) ≥ 30/50 = GO
```

---

## CONFIDENCE TAGGING

| Tag | Meaning | Confidence | Source |
|-----|---------|------------|--------|
| 🤖 | AI inference/guess | 60% | search_web, desk research |
| 📊 | Cited research data | 80% | Reports (Savills, CBRE, Mordor) |
| 👤 | User interview data | 90% | Real conversations (Mom Test) |
| ✅ | Validated by usage | 95% | Analytics, real transactions |

---

## GATE ENFORCEMENT

```
🛑 PRODUCT TOWER GATE BLOCK

Anh đang hỏi về tầng [X] nhưng tầng [Y] chưa hoàn thành.
Cascade failure risk: build sai từ gốc → lãng phí toàn bộ dev effort.

→ BLOCKED: hoàn thành tầng [Y] trước.
→ Override: confirm "force skip [Y]" (ghi nhận risk, output sẽ đánh dấu ⚠️)
```

---

## FILE NAMING CONVENTION

```
MỖI TIER = 1 FILE RIÊNG. TUYỆT ĐỐI KHÔNG ĐƯỢC GỘP.

data/t0_market_research.md       data/ab1_counter_search.md
data/t0_competitive_map.md       data/ab2_red_team.md
data/t1_target_market.md         data/ab3_field_notes.md
data/t2_segmentation.md          data/ab4_user_interview.md
data/t3_segment_filter.md        data/ab5_strategic_analysis.md
data/t4_personas.md              data/ab6_founder_insight.md
data/t5_user_needs.md            data/t7_pmf.md
data/t6_unmet_needs.md           data/t8_features.md
                                 data/t9_user_stories.md
                                 data/t9_5_offer_bridge.md
```

---

## HANDOFF: T10-T14

Khi T0-T9.5 hoàn thành VÀ PMF(adjusted) ≥ 30/50:

```
✅ Product Tower DONE (T0-T9.5)
├── T10 UX Design     → external skills
├── T11 UI Design     → external agents
├── T12 Development   → external agents
├── T13 QA/Testing    → external agents
└── T14 Feedback Loop → analytics-feedback skill
```
