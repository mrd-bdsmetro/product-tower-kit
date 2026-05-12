---
status: draft
type: documentation
owner: MR.D
last_updated: 2026-05-12
tags: [harness, quality, testing, hardness, T13, validation]
pmf_impact: high
---

# Harness System - T13 Quality & Hardness Framework

## Overview

Harness is the **quality foundation** that turns validated plans into production-ready code. It provides layered validation, risk-aware feature intake, and proof-based testing.

**Applies to:** T10-T14 (Build Phase via ClaudeKit)

---

## Core Principle

> **"Tests prove behavior. Harness proves quality."**

Every code change must prove it works, not just that it compiles.

---

## 3-Level Validation Ladder

| Level | Command | What it checks |
|-------|---------|----------------|
| **Quick** | `npm run validate:quick` | Format, lint, typecheck, unit tests |
| **Integration** | `npm run validate:integration` | Backend, database, providers |
| **E2E** | `npm run validate:e2e` | User-visible browser flows |
| **Platform** | `npm run validate:platform` | Shell, mobile, desktop, deployment |
| **Release** | `npm run validate:release` | Full suite + performance smoke |

### Quick Validation (Baseline)

```bash
npm run validate:quick
```

Checks:
- [ ] Format (prettier, rustfmt)
- [ ] Lint (eslint, ruff)
- [ ] Typecheck (tsc --noEmit)
- [ ] Unit tests pass

### Integration Validation

```bash
npm run validate:integration
```

Checks:
- [ ] Database queries work
- [ ] API contracts match
- [ ] Provider SDKs respond
- [ ] Jobs/queues process
- [ ] Webhooks fire correctly

### E2E Validation

```bash
npm run validate:e2e
```

Checks:
- [ ] User signup flow works
- [ ] Core user journeys complete
- [ ] Error states display correctly
- [ ] Auth persists across sessions

### Platform Validation

```bash
npm run validate:platform
```

Checks:
- [ ] Docker build succeeds
- [ ] Deployment succeeds
- [ ] Mobile build succeeds
- [ ] Desktop build succeeds

### Release Validation

```bash
npm run validate:release
```

Checks:
- [ ] Full test suite passes
- [ ] Performance smoke tests pass
- [ ] No critical logs errors
- [ ] Health checks pass

---

## Feature Intake System

### Risk Lanes

| Lane | Use when | Requirements |
|------|----------|--------------|
| **Tiny** | Docs, copy, low-risk | Patch + quick validate |
| **Normal** | Story-sized, bounded | Story packet + validation |
| **High-Risk** | Auth, data, security | Full execplan + human confirm |

### Risk Checklist (10 flags)

| Flag | Applies when |
|------|--------------|
| Auth | Login, JWT, sessions, password |
| Authorization | Roles, permissions, tenant scope |
| Data model | Schema, migrations, deletion |
| Audit/security | Audit logs, privacy, access |
| External systems | Email, payments, webhooks, queues |
| Public contracts | API shape, response format |
| Cross-platform | Browser/mobile/desktop split |
| Existing behavior | Changes to working code |
| Weak proof | Missing or unclear tests |
| Multi-domain | Multiple areas at once |

### Classification

```
0-1 flags → Tiny or Normal
2-3 flags → Normal with stronger validation
4+ flags → High-Risk
```

**Hard gates (always High-Risk unless narrowed):**
- Auth
- Authorization
- Data loss/migration
- Audit/security
- External provider behavior

---

## Test Matrix

See: `docs/test-matrix.md`

---

## Conversion Trigger

When T9.5 is complete, this harness system becomes the upsell point:

> **"Your plan is validated. Now build it right."**

```
T9.5 complete
    → Show harness friction checklist
    → ClaudeKit handles T10-T14 execution
    → /ck:cook <plan-file>
```

---

## References

- ClaudeKit `ck:test` skill
- ClaudeKit `ck:cook` skill
- ClaudeKit `ck:debug` skill
- harness-experimental: https://github.com/hoangnb24/harness-experimental

---

*Product Kit T13 Quality Layer*