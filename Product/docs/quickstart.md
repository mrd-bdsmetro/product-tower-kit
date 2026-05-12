# Product Tower Kit - Quickstart

## Install

```bash
# Option 1: npx (recommended)
npx product-tower-kit init

# Option 2: npm global
npm install -g product-tower-kit
product-tower init

# Option 3: Clone + link
git clone https://github.com/AIScale-Corp/product-tower-kit.git
cd product-tower-kit
npm link
product-tower init
```

---

## Initialize Project

```bash
# In your project directory
product-tower init
```

This creates:
- `data/` directory for tower output files
- `pipeline_state.json` for state tracking

---

## Quick Flow

```bash
# 1. Research market
"research thị trường [ngành]"

# 2. Parse Deep Research (if available)
"parse deep research [file]"

# 3. Run Product Tower
"chạy product tower cho [project]"

# 4. Check status
product-tower status

# 5. Assess health
product-tower assess
```

---

## Step-by-Step

### T0: Market Research
```
"research thị trường bất động sản"
```
→ Creates `data/t0_market_research.md`

### T1-T3: Foundation
```
"phân khúc thị trường cho [project]"
```
→ Creates `data/t1_target_market.md`, `t2_segmentation.md`, `t3_segment_filter.md`

### T4-T6: Discovery
```
"build persona cho [project]"
```
→ Creates `data/t4_personas.md`, `t5_user_needs.md`, `t6_unmet_needs.md`

### AB1-AB6: Anti-Bias
```
"chạy anti-bias cho [project]"
```
→ Creates `data/ab1_counter_search.md` through `ab6_founder_insight.md`

### T7: PMF Validation
```
"validate PMF cho [project]"
```
→ Creates `data/t7_pmf.md` - HARD GATE

### T8-T9: Feature Scoping
```
"scope features cho [project]"
```
→ Creates `data/t8_features.md`, `t9_user_stories.md`

### T9.5: Offer Bridge
```
"pricing cho [project]"
```
→ Creates `data/t9_5_offer_bridge.md`

---

## Commands

| Command | Description |
|---------|-------------|
| `/pt:init` | Initialize project |
| `/pt:research [topic]` | Run T0 market research |
| `/pt:validate PMF` | Run T7 PMF validation |
| `/pt:scope features` | Run T8-T9 feature scoping |
| `/pt:assess` | Quick health check |
| `/pt:status` | Show pipeline status |
| `/pt:report` | Generate full report |

---

## CLI Commands

```bash
product-tower init              # Initialize project
product-tower check T1          # Check gate
product-tower complete T0       # Mark complete
product-tower pmf 44 -4         # Set PMF score
product-tower status            # Show status
product-tower assess            # Quick health check
product-tower naming            # Show naming convention
```

---

## Next Steps

1. Run `/pt:research` to start T0
2. Run `/pt:assess` to check progress
3. Follow the gate system (T0→T1→...→T7)
4. Complete anti-bias before T7
5. PMF ≥ 30/50 to proceed to T8+
