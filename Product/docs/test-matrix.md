---
status: draft
type: documentation
owner: MR.D
last_updated: 2026-05-12
tags: [testing, proof, validation, test-matrix, T13]
pmf_impact: medium
---

# Test Matrix - Behavior to Proof Mapping

## Overview

Test Matrix maps **behavior** (what the system does) to **proof** (how we verify it works). Every row = one behavior. Every column = one validation method.

**Use when:** Writing tests, reviewing coverage, planning validation

---

## Matrix Structure

| Behavior | Unit | Integration | E2E | Manual | Proof Standard |
|----------|------|-------------|-----|--------|----------------|
| *Category: Auth* | | | | | |
| Login works | ✓ | ✓ | ✓ | - | Can login with valid creds |
| Invalid creds rejected | ✓ | ✓ | - | - | 401 returned |
| Session persists | - | ✓ | ✓ | - | Auth works after refresh |
| Logout clears session | ✓ | - | ✓ | - | 401 after logout |
| *Category: Data* | | | | | |
| Create record | ✓ | ✓ | ✓ | - | Record in DB |
| Read record | ✓ | ✓ | - | - | Correct data returned |
| Update record | ✓ | ✓ | ✓ | - | Changes persisted |
| Delete record | ✓ | ✓ | - | - | Record removed |
| *Category: API* | | | | | |
| GET returns 200 | ✓ | ✓ | ✓ | - | Correct JSON shape |
| POST returns 201 | ✓ | ✓ | - | - | Resource created |
| 404 returns proper shape | ✓ | ✓ | - | - | Error JSON format |
| Validation errors surface | ✓ | ✓ | - | - | Field-level errors |
| *Category: UI* | | | | | |
| Page loads | - | - | ✓ | - | No console errors |
| Form submits | - | - | ✓ | - | Success state shown |
| Error displays | - | - | ✓ | - | User-friendly message |
| Loading states | - | - | ✓ | - | Spinner/skeleton shown |
| *Category: Platform* | | | | | |
| Docker builds | - | - | - | ✓ | Image builds without error |
| Deploy succeeds | - | - | - | ✓ | Healthy on target env |
| Mobile builds | - | - | - | ✓ | IPA/APK generated |
| Desktop builds | - | - | - | ✓ | EXE/DMG generated |

---

## Validation Levels

### Unit Tests
- **Run:** `npm run test:unit` (fast, no deps)
- **Purpose:** Verify individual functions work in isolation
- **Mock:** Database, external APIs, file system
- **Coverage target:** 80% for business logic

### Integration Tests
- **Run:** `npm run test:integration` (medium, real deps)
- **Purpose:** Verify components work together
- **Mock:** External providers only (Stripe, SendGrid)
- **Coverage target:** Critical paths covered

### E2E Tests
- **Run:** `npm run test:e2e` (slow, real browser)
- **Purpose:** Verify user-visible flows work
- **Mock:** None (full stack)
- **Coverage target:** Happy paths + error paths

### Manual Verification
- **Run:** Human reviewer
- **Purpose:** Platform-specific, visual, UX validation
- **When:** Docker, mobile, desktop, visual regression

---

## Proof Standards

Every test must prove:

1. **Happy path works** - What should happen, happens
2. **Error path caught** - What shouldn't happen, doesn't
3. **Data persists** - Changes survive restart
4. **Auth enforced** - Unauthorized access blocked

---

## Coverage Rules

| Type | Required coverage |
|------|-------------------|
| Business logic | 80% line |
| API endpoints | 100% happy + error |
| Auth flows | 100% coverage |
| Data mutations | All CRUD ops tested |
| UI interactions | Key flows E2E tested |

---

## Quick Validation Command

```bash
# Run all levels
npm run validate:quick      # unit + lint + typecheck
npm run validate:integration # integration tests
npm run validate:e2e        # e2e tests (local)
```

---

## Integration with Harness System

Test Matrix is part of Harness System (see `docs/harness-system.md`):

```
Feature Intake → Risk Classification → Test Matrix → Validation
     ↓                   ↓                  ↓            ↓
  tiny/normal      0-1 flags = tiny    unit only      quick validate
  high-risk        4+ flags = high    full matrix     full validate
```

---

## References

- ClaudeKit `ck:test` skill
- harness-experimental test-matrix.md
- PMF validations: T0-T9.5 framework

---

*Product Kit T13 Quality Layer*