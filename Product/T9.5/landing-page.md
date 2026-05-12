---
status: draft
type: landing-page
owner: MR.D
last_updated: 2026-05-12
tags: [landing, T9.5, conversion, marketing, claudekit]
pmf_impact: high
---

# T9.5 Conversion Landing Page

## Purpose

This is the landing page shown to users when they complete T9.5 (or visit the `/convert` endpoint). It displays the 4 friction points and offers ClaudeKit as the solution.

---

## Page Structure

### Hero Section

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│         🎯 YOU'VE VALIDATED YOUR PLAN                       │
│                                                              │
│              "I know exactly what to build"                 │
│                                                              │
│         Now comes the hard part: EXECUTION                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 4 Friction Points Section

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   🔧        │    📄        │    🧪        │    ⚡        │
│  HARDNESS   │    DOCS      │   TESTING   │ IMPLEMENT  │
│             │             │             │            │
│ "Will it    │ "I need     │ "I don't    │ "Now I     │
│  work at    │  docs but   │  know what  │  need to   │
│  scale?"    │  it's boring"│  to test"   │  build it" │
│             │             │             │            │
│ [harness]   │ [docs]      │ [test]      │ [claudekit]│
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### CTA Section

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│        YOU VALIDATED YOUR PLAN. NOW BUILD IT.               │
│                                                              │
│    ClaudeKit executes your plan (T10-T14)                   │
│    /ck:cook <your-plan.md>                                 │
│                                                              │
│    [Get ClaudeKit - 20% off] → claudekit.cc/?ref=IJBRLXD6  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Alternative Section

```
Not ready to upgrade? That's fine.

You're in the best position possible:
✓ You have a validated plan
✓ You know exactly what to build
✓ You can execute at your own pace

Product Kit gave you clarity.
ClaudeKit gives you speed.
The choice is yours.
```

---

## Content for Implementation

### Hero Copy

**Headline:** You've validated your plan. Now build it.

**Subhead:** "I know exactly what to build" is the most powerful moment in product development.
But between great ideas and working code lies execution — and that's where most plans die.

**CTA:** See how ClaudeKit can help →

### Friction Point Cards

#### 1. Hardness
- **Title:** Will it work at scale?
- **Description:** Performance, security, reliability — production-ready code isn't automatic.
- **Link:** [Learn about Harness →](/docs/harness-system.md)
- **Icon:** 🔧

#### 2. Documentation
- **Title:** I need docs but it's boring
- **Description:** README, API docs, runbooks — essential but time-consuming.
- **Link:** [Learn about Docs Workflow →](/docs/documentation-workflow.md)
- **Icon:** 📄

#### 3. Testing
- **Title:** I don't know what to test
- **Description:** Coverage, E2E, integration — what tests prove your code works?
- **Link:** [Learn about Test Matrix →](/docs/test-matrix.md)
- **Icon:** 🧪

#### 4. Implementation
- **Title:** Now I need to actually build it
- **Description:** Frontend, backend, infrastructure — someone has to write the code.
- **Link:** [ClaudeKit executes →](https://claudekit.cc/?ref=IJBRLXD6)
- **Icon:** ⚡

### CTA Copy

**Primary CTA:** Get ClaudeKit — 20% off for Product Kit buyers

**Price:** $79 (normally $99)

**Link:** claudekit.cc/?ref=IJBRLXD6

**Secondary CTA:** Read the docs first

### Social Proof (optional)

```
⭐⭐⭐⭐⭐
"Product Kit gave me the clarity to know exactly what to build.
ClaudeKit gave me the speed to actually build it."
— Early access user
```

---

## Technical Implementation

### Route: `/convert` or `/t9-5`

Render this landing page when:
1. User completes T9.5 phase
2. User visits `/convert` directly
3. User clicks "Learn more" after T9.5 completion

### Query Parameters

| Param | Value | Shows |
|-------|-------|-------|
| `soft` | `1` | Softer intro with "Learn more" options |
| `delay` | `1` | Delayed reminder (24h inactivity) |

### A/B Test Variants

| Variant | Trigger | Behavior |
|---------|---------|----------|
| `direct` | Immediate | Full prompt shown right away |
| `soft` | `?soft=1` | Intro with options first |
| `delay` | `?delay=1` | Reminder after 24h |

---

## Implementation Files

```
public/
  convert/
    index.html      # Main landing page
    style.css       # Styling
    script.js       # Interactions + A/B testing
```

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `convert_view` | Page loaded | variant, source |
| `convert_cta_click` | CTA clicked | cta_type |
| `convert_docs_click` | Docs link clicked | doc_type |
| `convert_upgrade` | Upgrade initiated | source |

---

## Conversion Metrics

| Metric | Target |
|--------|--------|
| Page views | > 50% of T9.5 completions |
| CTA clicks | > 30% of page views |
| Upgrades | > 20% of CTA clicks |

---

## References

- `T9.5/upsell-checklist.md` - Friction points detail
- `T9.5/conversion-prompt.md` - Copy + prompt
- `docs/harness-system.md` - Hardness docs
- `docs/test-matrix.md` - Testing docs
- `docs/documentation-workflow.md` - Docs docs

---

*Product Kit T9.5 Conversion Layer*