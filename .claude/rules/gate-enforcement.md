# Gate Enforcement Rules

## Tier Dependencies

```
T-1 → T0 → T1 → T2 → T3 → T4 → T5 → T6
                                         ↓
                                    AB1 → AB2 → AB3 → AB4
                                                       ↓
                                              T7 (PMF ≥ 30/50)
                                                       ↓
                                              T8 → T9 → T9.5
                                                       ↓
                                              T10-T14 (handoff)
```

## Gate Check Logic

Before allowing tier X:
1. Check `pipeline_state.json` for completed tiers
2. Verify all prerequisite tiers are complete
3. Check required files exist in `data/`
4. If blocked, show specific blocker message

## Force Skip

User can say "force skip [tier]":
- Risk acknowledged
- Output marked with ⚠️
- PMF penalty applied (if applicable)
- Logged in `pipeline_state.json`

## PMF Gate (T7)

Special gate with additional requirements:
- AB1-AB4 must be complete (or force skip)
- PMF(adjusted) ≥ 30/50 = PASS
- PMF(adjusted) < 30/50 = BLOCKED
- NO-GO → suggest pivot to T1 or T4
