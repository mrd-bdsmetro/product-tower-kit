---
name: competitor-alternatives
version: 1.0.0
description: |
  Competitor comparison and alternative pages for SEO and sales.
  For T0-CP competitive positioning, comparison content.
triggers:
  - "competitor"
  - "alternatives"
  - "comparison"
  - "vs"
  - "so sánh"
---

# Competitor Alternatives - Comparison Pages

## Goal
Create competitor comparison and alternative pages for SEO and sales enablement.

---

## 4 Page Formats

### 1. Singular Alternative
"[Competitor] Alternative" - Why you're different from one competitor.

### 2. Plural Alternatives
"Best [Competitor] Alternatives" - List of alternatives including yourself.

### 3. You vs Competitor
"[Your Product] vs [Competitor]" - Direct comparison.

### 4. Competitor vs Competitor
"[Competitor A] vs [Competitor B]" - Compare two competitors (position yourself as alternative).

---

## Section Templates

### TL;DR (Top of page)
```
Looking for a [Competitor] alternative?
[Your Product] is [1-sentence value prop].
Unlike [Competitor], we [key differentiator].
[CTA Button]
```

### Paragraph Comparison
```
[Competitor] is great for [use case].
But if you need [differentiator], [Your Product] is better because [reason].
```

### Feature Comparison Table
| Feature | [Your Product] | [Competitor] |
|---------|----------------|--------------|
| Feature 1 | ✅ | ✅ |
| Feature 2 | ✅ | ❌ |
| Feature 3 | ✅ | ⚠️ Limited |
| Price | $49 | $99 |

### Pricing Comparison
| Plan | [Your Product] | [Competitor] |
|------|----------------|--------------|
| Free | ✅ | ❌ |
| Starter | $49/mo | $99/mo |
| Pro | $99/mo | $199/mo |

### Migration Guide
```
Switching from [Competitor] to [Your Product]:
1. Export your data from [Competitor]
2. Import into [Your Product]
3. [Setup steps]
[CTA: Start migration]
```

### Social Proof
```
"I switched from [Competitor] to [Your Product] and..."
- [Customer Name], [Role]
```

---

## Competitor Data Schema (YAML)

```yaml
competitors:
  - name: "Competitor A"
    url: "https://competitor-a.com"
    pricing:
      free: false
      starter: "$99/mo"
      pro: "$199/mo"
    strengths:
      - "Feature X"
      - "Brand recognition"
    weaknesses:
      - "Expensive"
      - "Complex"
    target: "Enterprise"
    alternatives_count: 5
```

---

## SEO Considerations

1. **Title tag** - "[Your Product] vs [Competitor]: Which is Better in 2026?"
2. **Meta description** - Compare key features and pricing
3. **H1** - "[Your Product] vs [Competitor]"
4. **Internal links** - Link to your features, pricing pages
5. **Schema markup** - Product comparison structured data

---

## Output Format

```markdown
# [Your Product] vs [Competitor]

## TL;DR
[Quick comparison]

## Feature Comparison
[table]

## Pricing Comparison
[table]

## When to Choose [Competitor]
[honest assessment]

## When to Choose [Your Product]
[key differentiators]

## Migration Guide
[steps]

## Social Proof
[quotes]
```
