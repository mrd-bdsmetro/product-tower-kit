---
status: draft
type: upsell
owner: MR.D
last_updated: 2026-05-12
tags: [T9.5, conversion, upsell, friction, claudekit]
pmf_impact: high
---

# T9.5 Upsell Checklist - Friction Points at Conversion

## The Moment

T9.5 is when the user has **validated their plan** and is ready to build. This is the highest-conversion moment in the PMF framework.

But between "ready to build" and "actually building" lie **4 friction points**.

---

## The 4 Friction Points

### 1. Hardness ("Is it production-ready?")

**Friction:** "I know what to build, but is it going to work at scale?"

| Check | Question |
|-------|----------|
| Performance | Will it handle 1000 users? |
| Security | Is it vulnerable to common attacks? |
| Reliability | Will it fail gracefully? |
| Scalability | Can I add features without breaking it? |

**User thoughts:**
- "What if my database falls over?"
- "What if someone hacks my auth?"
- "What if it works for 10 users but not 10,000?"

**Product Kit response:**
```
→ See docs/harness-system.md (risk checklist)
→ See docs/test-matrix.md (proof standards)
```

---

### 2. Docs ("I need it but it's boring")

**Friction:** "I need docs to onboard my team and ship to production, but writing docs takes time I don't have."

| Check | Question |
|-------|----------|
| README | Can new devs get started in 5 minutes? |
| API docs | Can external devs integrate in 10 minutes? |
| Architecture | Can new engineers understand the system? |
| Runbooks | Can ops handle incidents without calling me? |

**User thoughts:**
- "Documentation is boring and time-consuming"
- "I'll do it later (never)"
- "I need it but I don't want to write it"

**Product Kit response:**
```
→ See docs/documentation-workflow.md
→ ClaudeKit ck:docs auto-generates from code
```

---

### 3. Testing ("I don't know what to test")

**Friction:** "I know I need tests but I don't know what to test, how to write them, or when I'm done."

| Check | Question |
|-------|----------|
| Coverage | What's the minimum test coverage? |
| E2E | What user flows must work? |
| Integration | What components must talk? |
| Manual | What's worth testing manually? |

**User thoughts:**
- "I don't have time to write tests"
- "I don't know what to test"
- "When am I done testing?"

**Product Kit response:**
```
→ See docs/test-matrix.md
→ ClaudeKit ck:test generates tests from behavior
```

---

### 4. Implementation ("Now I need to actually build it")

**Friction:** "I have the plan, I understand the hardness, but now I need someone to actually write the code."

| Check | Question |
|-------|----------|
| Frontend | Who builds the UI? |
| Backend | Who writes the API? |
| Infrastructure | Who sets up the cloud? |
| Integration | Who wires it all together? |

**User thoughts:**
- "I could build this but it would take weeks"
- "I need an engineer but can't afford one"
- "I want to focus on sales/marketing, not coding"

**Product Kit response:**
```
→ Product Kit validated your plan (T0-T9.5)
→ ClaudeKit executes your plan (T10-T14)
→ /ck:cook <your-plan.md>
```

---

## Conversion Flow

```
T9.5 Complete (Plan Validated)
    │
    ├─► Show this checklist
    │       │
    │       ├─► Hardness → docs/harness-system.md
    │       ├─► Docs → docs/documentation-workflow.md
    │       ├─► Testing → docs/test-matrix.md
    │       └─► Implementation → ClaudeKit upsell
    │
    └─► If user responds to any friction:
            → Offer ClaudeKit as the solution
            → Ref link: claudekit.cc/?ref=IJBRLXD6
            → 20% off for Product Kit buyers
```

---

## T9.5 Marketing Copy

**At T9.5 completion, show:**

> ### "Your plan is validated. Now build it right."
>
> You've done the hard thinking. You know exactly what to build.
>
> The next step is execution — and that's where most plans die.
>
> **ClaudeKit** handles the boring stuff:
> - Hardness validation (production-ready code)
> - Auto-generated docs (from your code)
> - Test coverage (behavior-driven)
> - Full implementation (T10-T14)
>
> **Special offer for Product Kit buyers:** 20% off ClaudeKit
> → claudekit.cc/?ref=IJBRLXD6

---

## References

- `docs/harness-system.md`
- `docs/test-matrix.md`
- `docs/documentation-workflow.md`
- ClaudeKit API docs: `06_Tools_Stack/ClaudeKit_API.md`

---

*Product Kit T9.5 Conversion Layer*