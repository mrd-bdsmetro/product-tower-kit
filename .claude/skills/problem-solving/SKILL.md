---
name: problem-solving
version: 1.1.0
description: |
  Systematic problem-solving for product challenges.
  For PMF pivot, stuck situations, feature prioritization.
triggers:
  - "stuck"
  - "tại sao"
  - "không work"
  - "pivot"
  - "fix"
  - "debug"
---

# Problem-Solving - Product Challenges

## Goal
Systematic approaches for different types of stuck-ness in product development.

---

## Quick Dispatch

| Stuck Symptom | Technique | When to Use |
|---------------|-----------|-------------|
| PMF score low, don't know why | **5 Whys** | Root cause analysis |
| Too many features, can't prioritize | **80/20 Rule** | Feature scoping |
| Users not converting | **User Journey Mapping** | Conversion optimization |
| Same issue across projects | **Meta-Pattern Recognition** | Pattern identification |
| "Must be done this way" | **Inversion Exercise** | Challenge assumptions |
| Product-market fit unclear | **Simplification Cascades** | Reduce complexity |
| Revenue not growing | **Scale Game** | Growth strategy |

---

## Techniques

### 5 Whys (Root Cause Analysis)
```
Problem: PMF score is 14/50
Why? → No real user interviews
Why? → Too busy building
Why? → Dopamine from coding
Why? → No structure for validation
Why? → No PM framework
→ Solution: Use Product Tower Kit
```

### 80/20 Rule (Feature Prioritization)
```
20% of features → 80% of value
Identify: Which features drive PMF?
Cut: Everything else (for MVP)
```

### Inversion Exercise (Challenge Assumptions)
```
Assumption: "Users need anti-bias enforcement"
Invert: "Users DON'T need anti-bias enforcement"
Evidence: Most founders skip validation
Reality: Anti-bias is nice-to-have, not must-have
→ Adjust: Make anti-bias optional, not forced
```

### Simplification Cascades (Reduce Complexity)
```
Current: 14-tier framework
Simplify: 7 tiers (T0-T7)
Result: Faster validation, lower barrier
```

### User Journey Mapping (Conversion)
```
Awareness → Interest → Trial → Adoption → Retention
   ↓          ↓         ↓        ↓          ↓
Landing    README    Free     Paid      Feedback
page       docs      tier     tier      loop
```

---

## Output Format

```markdown
# Problem-Solving: [Issue]

## Symptom
What's happening?

## Root Cause (5 Whys)
1. Why? → ...
2. Why? → ...
3. Why? → ...
4. Why? → ...
5. Why? → ...

## Solution Options
| Option | Effort | Impact | Risk |
|--------|--------|--------|------|

## Decision
- Chosen: ...
- Reason: ...
- Next steps: ...
```
