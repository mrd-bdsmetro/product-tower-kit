# /pt:validate - Run T7 PMF Validation

## Usage
```
/pt:validate PMF
/pt:validate [project]
```

## Behavior
1. Check anti-bias completion (AB1-AB4)
2. Activate pmf-validator skill
3. Activate pmf-validator agent
4. Score 10 PMF signals
5. Apply penalty/bonus
6. Make GO/NO-GO decision
7. Output `data/t7_pmf.md`

## Gate
- AB1-AB4 ALL complete (or force skip with penalty)
- PMF(adjusted) ≥ 30/50 = PASS

## Output
```
⭐ PMF VALIDATION - [Project]

Anti-Bias: AB1 ✅ AB2 ✅ AB3 ✅ AB4 ✅
PMF Raw: X/50
PMF Adjusted: X/50
Threshold: 30/50

Decision: GO / NO-GO
```
