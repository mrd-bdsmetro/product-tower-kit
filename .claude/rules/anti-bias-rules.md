# Anti-Bias Rules

## Why Anti-Bias?

AI desk research is biased:
- Google SEO = clickbait
- Survivorship bias
- Confirmation bias
- No real-world friction

Anti-Bias Layer creates artificial friction to counter these biases.

## AB1: Counter-Search

**Purpose:** Find data that CONTRADICTS T0 findings

**Rules:**
- Use `search_web` with NEW keywords
- Keywords: "thất bại [ngành]", "rủi ro", "lỗ vốn", "[competitor] problems"
- NOT extracting from T0
- Must find counter-evidence

**Output:** `data/ab1_counter_search.md`

## AB2: Red Team

**Purpose:** Challenge PMF assumptions

**Rules:**
- Use anti-bias-challenger agent (sparring mode)
- Challenge every PMF signal
- Find counter-arguments
- Score risk level

**Output:** `data/ab2_red_team.md`

## AB3: Field Observation

**Purpose:** Real-world validation

**Rules:**
- Digital product: API measurement (Google Maps, GA4, Stripe)
- Physical product: Site visit, count competitors, take photos
- Digital = valid field observation
- Physical without visit = INCOMPLETE (penalty -1)

**Output:** `data/ab3_field_notes.md`

## AB4: User Interview

**Purpose:** Real user feedback

**Rules:**
- Minimum 5 people
- Use Mom Test methodology
- Ask about BEHAVIOR, not OPINIONS
- Record actual quotes

**Output:** `data/ab4_user_interview.md`

## AB5: Strategic Analysis (Optional)

**Purpose:** Long-term strategic thinking

**Rules:**
- Risk/Reward asymmetric? (Naval)
- Monopoly possible? (Thiel: 0→1?)
- Antifragile? (Taleb)

**Output:** `data/ab5_strategic_analysis.md`
**Bonus:** +0.5 PMF

## AB6: Founder Insight (Mandatory for Solo)

**Purpose:** Domain expertise from founder

**Rules:**
- Solo founder: MANDATORY
- Team/Corporate: Optional
- Content: Pricing insight + Revenue model

**Output:** `data/ab6_founder_insight.md`
**Bonus:** +1.0 PMF
