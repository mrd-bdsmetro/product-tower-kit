# T9: User Stories - Product Tower Kit

## User Stories (MUST features)

### Story 1: Initialize Project
```
As a solo founder,
I want to initialize a Product Tower project,
So that I can start validating my idea with a structured framework.

Acceptance Criteria:
- Run `product-tower init` in my project directory
- Creates `data/` directory
- Creates `pipeline_state.json` with initial state
- Shows welcome message with next steps
```

### Story 2: Research Market (T0)
```
As a solo founder,
I want to research my market before building,
So that I can understand the landscape and competitors.

Acceptance Criteria:
- Run `/pt:research [topic]` in Claude Code
- Creates `data/t0_market_research.md`
- Includes market size, competitors, trends
- Confidence tags on all data points
```

### Story 3: Validate PMF (T7)
```
As a solo founder,
I want to validate Product-Market Fit before scaling,
So that I don't waste time on products nobody wants.

Acceptance Criteria:
- Run `/pt:validate PMF` in Claude Code
- Scores 10 PMF signals
- Applies anti-bias penalty
- GO/NO-GO decision with threshold ≥30/50
- Creates `data/t7_pmf.md`
```

### Story 4: Check Gate
```
As a solo founder,
I want to check if I can proceed to the next tier,
So that I don't skip important validation steps.

Acceptance Criteria:
- Run `product-tower check T1`
- Checks if T0 is complete
- Blocks if prerequisite missing
- Shows specific blocker message
```

### Story 5: Track Progress
```
As a solo founder,
I want to see my current progress in the framework,
So that I know what's done and what's next.

Acceptance Criteria:
- Run `/pt:status` in Claude Code
- Shows completed tiers
- Shows PMF score
- Shows anti-bias status
```

### Story 6: Anti-Bias Enforcement
```
As a solo founder,
I want my assumptions challenged before validating PMF,
So that my validation is based on real data, not wishful thinking.

Acceptance Criteria:
- AB1: Counter-search with negative keywords
- AB2: Red team challenges PMF signals
- AB3: Field observation (digital or physical)
- AB4: User interviews (5+ people)
- All AB files created before T7
```

### Story 7: Quick Assessment
```
As a solo founder,
I want a quick health check of my product tower,
So that I can identify weak areas quickly.

Acceptance Criteria:
- Run `/pt:assess` in Claude Code
- Scores all tiers 0-3
- Calculates tower score (/42)
- Identifies weakest link
- Suggests next action
```

## Story Map

```
Epic: Product Validation
├── Story 1: Initialize (MUST)
├── Story 2: Research T0 (MUST)
├── Story 3: Validate PMF T7 (MUST)
├── Story 4: Check Gate (MUST)
├── Story 5: Track Progress (MUST)
├── Story 6: Anti-Bias (MUST)
└── Story 7: Quick Assessment (MUST)
```

## Velocity Estimate

| Story | Points | Priority |
|-------|--------|----------|
| Initialize | 1 | MUST |
| Research T0 | 3 | MUST |
| Validate PMF | 5 | MUST |
| Check Gate | 2 | MUST |
| Track Progress | 2 | MUST |
| Anti-Bias | 5 | MUST |
| Quick Assessment | 2 | MUST |
| **Total** | **20** | |

**All MUST stories are already implemented** in the current product-tower-kit.

**Confidence:** 📊 85% (stories match existing implementation)
