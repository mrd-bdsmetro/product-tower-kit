---
name: user-discovery
version: 1.0.0
description: |
  T4-T6 User Discovery skill. Persona building, need mapping, unmet need filter.
triggers:
  - "persona"
  - "user needs"
  - "unmet needs"
  - "build persona"
---

# User Discovery - T4-T6

## Goal
Discover users: who they are, what they need, what's missing.

---

## T4: USER PERSONAS

2-4 personas based on BEHAVIOR + PURPOSE (NOT demographic):

```markdown
## Persona: [Name]
- **Behavior:** What they do
- **Purpose:** Why they do it
- **Pain:** Biggest frustration
- **Gain:** Desired outcome
- **Quote:** "..." (from interview)
```

**Output:** `data/t4_personas.md`

---

## T5: USER NEEDS

Impact × Frequency matrix:

| Need | Impact (1-5) | Frequency (1-5) | Score | Source |
|------|-------------|-----------------|-------|--------|

**Output:** `data/t5_user_needs.md`

---

## T6: UNMET NEEDS

4-criteria filter:
1. Ai đang solve? (competitors)
2. Mình thể solve? (capability)
3. Tốt hơn? (differentiation)
4. User愿意 trả tiền? (WTP)

⭐ UNMET = pass all 4

**Output:** `data/t6_unmet_needs.md`

---

## GATE
- T3 filter phải xong
- Recommend: interview 5+ người thật (Mom Test)
