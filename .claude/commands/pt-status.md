# /pt:status - Show Pipeline Status

## Usage
```
/pt:status
```

## Behavior
1. Read `pipeline_state.json`
2. Show completed tiers
3. Show skipped tiers
4. Show PMF score
5. Show anti-bias status

## Output
```
📊 PIPELINE STATUS - [Project]

Completed: T-1 ✅ T0 ✅ T1 ✅ T2 ✅
Skipped: (none)
Current: T3

PMF: Not scored yet
Anti-Bias: AB1 ✅ AB2 ⏳ AB3 ⏳ AB4 ⏳

Next: Complete T3 → T4-T6 Discovery
```
