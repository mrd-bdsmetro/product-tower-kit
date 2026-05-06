# /pt:research — Run T0 Market Research

## Usage
```
/pt:research [topic]
/pt:research thị trường [industry]
```

## Behavior
1. Check if project initialized
2. Activate market-research skill
3. Activate market-researcher agent
4. Collect data with confidence tags
5. Output `data/t0_market_research.md`

## Gate
- None (T0 is first tier)

## Output
```
🔍 MARKET RESEARCH — [Topic]

Collecting data...
✅ T0 complete: data/t0_market_research.md
📊 Confidence: 60% (AI search) / 80% (Deep Research)

➡️ Next: "phân khúc thị trường" (T1-T3)
```
