---
status: draft
type: upsell
owner: MR.D
last_updated: 2026-05-12
tags: [T9.5, conversion, prompt, claudekit, upsell]
pmf_impact: high
---

# T9.5 Conversion Prompt - ClaudeKit Upsell Trigger

## The Trigger

After user completes T9.5 (plan validated), show this prompt to introduce ClaudeKit as the natural next step.

---

## The Prompt

```
╔══════════════════════════════════════════════════════════════╗
║                    CONGRATULATIONS                          ║
║                                                              ║
║         You've completed Product Kit Phase T9.5             ║
║              Your plan is VALIDATED                         ║
╚══════════════════════════════════════════════════════════════╝

                    "I know exactly what to build"

This is the most powerful moment in product development.
You have clarity. You have focus. You have a validated plan.

But now comes the hard part: EXECUTION.

Most validated plans die here — between "great idea" and "working code."

───────────────────────────────────────────────────────────────

The 4 friction points between your plan and your product:

  🔧 HARDNESS     "Will it work at scale?"
                  docs/harness-system.md

  📄 DOCS         "I need docs but it's boring"
                  docs/documentation-workflow.md

  🧪 TESTING      "I don't know what to test"
                  docs/test-matrix.md

  ⚡ IMPLEMENTATION "Now I need to actually build it"
                  → This is where ClaudeKit helps

───────────────────────────────────────────────────────────────

              YOU VALIDATED YOUR PLAN

                   NOW BUILD IT

          ClaudeKit executes your plan (T10-T14)
          /ck:cook <your-plan.md>

          $79 (20% off for Product Kit buyers)
          → claudekit.cc/?ref=IJBRLXD6

───────────────────────────────────────────────────────────────

  Not ready to upgrade? That's fine.

  You're in the best position possible:
  - You have a validated plan
  - You know exactly what to build
  - You can execute at your own pace

  Product Kit gave you clarity.
  ClaudeKit gives you speed.

  The choice is yours.

╔══════════════════════════════════════════════════════════════╗
║  NEXT: /ck:cook <path-to-your-plan>                         ║
║  DOCS: docs/harness-system.md                               ║
║  REF:  claudekit.cc/?ref=IJBRLXD6 (20% off)                ║
╚══════════════════════════════════════════════════════════════╝
```

---

## When to Show This Prompt

| Trigger | Condition |
|---------|-----------|
| T9.5 complete | Phase status = "completed" |
| Plan file exists | plan.md has YAML frontmatter with status: approved |
| User requests next | User says "next", "build", "execute", "implement" |
| Cart abandonment | User viewed T9.5 but didn't continue to T10 |

---

## A/B Test Variants

### Variant A: Direct ("Now build it")

Show the full prompt immediately after T9.5 completion.

### Variant B: Soft ("Learn more")

Show a softer intro first, then prompt:

```
You've completed T9.5. Want to:
  [ ] See what T10-T14 looks like
  [ ] Read the harness docs
  [ ] Continue on your own

If you choose [1], we'll show you ClaudeKit pricing.
```

### Variant C: Delay ("Not yet")

Show a reminder after 24h if user hasn't upgraded:

```
"Hey, remember your validated plan?"
"It's still ready to build."
"Need help executing? ClaudeKit handles T10-T14."
```

---

## Pricing Context

| Product | Price | Notes |
|---------|-------|-------|
| Product Kit | $49 (one-time) | Validates your plan (T0-T9.5) |
| ClaudeKit | $79 via ref | Executes your plan (T10-T14) |
| Bundle | $128 if separate | 20% off via ref |

**Message:** "Product Kit gave you clarity. ClaudeKit gives you execution."

---

## Success Metrics

| Metric | Target |
|--------|--------|
| T9.5 → T10 conversion | > 20% |
| Time to conversion | < 24h |
| ClaudeKit activation | > 50% of converted |

---

## References

- `T9.5/upsell-checklist.md` - Detailed friction points
- `docs/harness-system.md` - Quality framework
- `docs/test-matrix.md` - Validation standards
- `06_Tools_Stack/ClaudeKit_API.md` - API documentation

---

*Product Kit T9.5 Conversion Layer*