---
status: active
type: technical
owner: MR.D
last_updated: 2026-05-12
tags: [technical, mvp, feasibility, architecture, build-vs-buy]
pmf_impact: high
---

# Technical Feasibility

## Overview
Technical Feasibility ensures the product can be built with available resources. Per the Product Management Tower: **"Technical Feasibility is the third leg of the stool"** — without it, even great products fail.

**Key Principle:** Build vs Buy decisions must be made early. Don't build what you can buy. Don't buy what you can integrate.

## MVP Scope Definition

### MVP Features (Must Have)

| Feature | Complexity | Build/Buy | Priority |
|---------|------------|-----------|----------|
| Markdown editor | Low | Buy (Obsidian) | P0 |
| File system storage | Low | Buy (Git) | P0 |
| Validation tracking | Medium | Build | P0 |
| PMF scoring calculator | Low | Build | P0 |
| PDF export | Medium | Buy (browser print) | P1 |

### Non-MVP Features (Post-PMF)

| Feature | Complexity | Build/Buy | Priority |
|---------|------------|-----------|----------|
| Notion sync | High | Build | P2 |
| API access | High | Build | P2 |
| Team collaboration | High | Buy (Notion) | P2 |
| Mobile app | Very High | — | P3 |

### Out of Scope (Forever)

- Payment processing (use Stripe)
- Email automation (use Mailchimp)
- Analytics (use Plausible)
- User authentication (use Auth0)

## Tech Stack

### Current Stack

| Layer | Technology | Why | Risk |
|-------|------------|-----|------|
| **Framework** | Markdown + Git | Simple, versioned | Low |
| **Hosting** | Vercel | Free tier, fast deploy | Low |
| **Editor** | Obsidian | Local, graph view | Low |
| **Tracking** | Manual + JSON | No DB needed | Low |
| **Search** | 5 providers | Brave, Firecrawl, Valyu, DDG, Exa | Medium |

### Future Stack (Post-PMF)

| Layer | Technology | Why | Cost |
|-------|------------|-----|------|
| **Backend** | Supabase | PostgreSQL, Auth, Edge Functions | $25/mo |
| **Hosting** | Vercel | Already familiar | $20/mo |
| **DB** | Supabase | PostgreSQL +向量 | $25/mo |
| **Email** | Resend | Developer-first | $20/mo |

## Build vs Buy Decisions

### Decision Matrix

| Category | Build | Buy | Integrate | Rationale |
|----------|-------|-----|-----------|-----------|
| Markdown editing | ❌ | ✅ | — | Obsidian is best-in-class |
| User authentication | ❌ | ✅ | — | Auth0/Clerk better than build |
| Database | ❌ | ✅ | — | Supabase handles scale |
| Email sending | ❌ | ✅ | — | Resend 10x better |
| File storage | ✅ | — | — | Git is perfect for this |
| Validation logic | ✅ | — | — | Core differentiation |
| PMF scoring | ✅ | — | — | Core differentiation |
| Search providers | ✅ | — | — | Integration only |
| Design system | ✅ | — | — | Custom needed for brand |

### Build vs Buy Principles

1. **Build what differentiates, buy what is commoditized**
2. **Buy time, not technology**
3. **Don't build a DB when Git already has one**
4. **Integration > Building > Buying**

## Technical Constraints

### Resource Constraints

| Resource | Limit | Mitigation |
|----------|-------|------------|
| Solo developer | 1 | Focus on low-code tools |
| Budget | $0-100/mo | Use free tiers |
| Time | Evenings/weekends | Automate CI/CD |
| Technical skill | Full-stack | Use managed services |

### Platform Constraints

| Constraint | Impact | Mitigation |
|------------|--------|------------|
| Windows only | Low | Cross-platform tools |
| No server | Medium | Serverless (Vercel) |
| Limited API access | Low | Use client-side APIs |
| No mobile | Medium | Progressive Web App |

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│  USER INTERFACE (Browser / Obsidian)                            │
│  - Read/Write Markdown                                           │
│  - View validation progress                                      │
│  - Export PDF                                                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  APPLICATION LAYER                                               │
│  - Product Tower CLI (Node.js)                                  │
│  - Gate Checker (Python)                                        │
│  - Search Scripts (Python)                                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  DATA LAYER                                                      │
│  - Git (file versioning)                                         │
│  - JSON (state management)                                       │
│  - Markdown (content)                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  EXTERNAL SERVICES (Integrated)                                 │
│  - Brave Search API (free tier)                                 │
│  - Firecrawl API (free tier)                                    │
│  - Valyu API (free tier)                                        │
│  - Obsidian Sync (free tier)                                    │
│  - Vercel (free tier)                                           │
└─────────────────────────────────────────────────────────────────┘
```

## MVP Technical Requirements

### Minimum Viable Product

| Requirement | Solution | Status |
|-------------|----------|--------|
| File management | Git + local folder | ✅ |
| Search | Brave + Valyu + Firecrawl | ✅ |
| Validation tracking | JSON state + CLI | ✅ |
| PMF scoring | Python calculator | ✅ |
| Export | Browser print to PDF | ✅ |

### Launch Criteria

- [ ] All T-tiers have valid Markdown templates
- [ ] CLI runs without errors
- [ ] Health check passes 100%
- [ ] No external API dependency (works offline)

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Search API rate limits | Medium | Low | Multiple providers |
| Git conflicts | Low | Medium | Clear workflow |
| Data loss | Low | High | Git backup + local |
| Platform lock-in | Low | Low | Markdown is portable |

## Next Steps

1. **Validate MVP scope** with 3 potential users
2. **Test offline capability** (critical for solo founders)
3. **Benchmark search providers** for reliability

---
*Technical Feasibility v1.7.0 — MVP scope, build vs buy, architecture*