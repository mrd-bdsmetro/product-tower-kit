---
status: active
type: learning
owner: MR.D
last_updated: 2026-05-12
tags: [lessons, learnings, retrospective]
---

# Lessons Learned

## Purpose
Document key insights from validation cycles.

---

### 2026-05-12 | Architecture Restructure

**What Went Well:**
- Clear 7-layer separation makes navigation easy
- Frontmatter standard enables future automation
- Entry points (INDEX, Quick_Start) reduce onboarding friction

**What Could Improve:**
- Should have restructured earlier (at v1.2.0)
- Search files (24) clutter data/ - consider archiving

**Action Items:**
- Add frontmatter to remaining files by 2026-05-15
- Archive old search files to reduce noise

---

### 2026-05-08 | Multi-Provider Search Integration

**What Went Well:**
- Fallback system prevents complete failure
- Provider-specific parsing handles different formats

**What Could Improve:**
- Too many providers (5) = maintenance burden
- Consider reducing to 2-3 core providers

**Action Items:**
- Evaluate provider usage after 10 more searches
- Consider consolidating to Brave + Valyu

---
*Add new lessons at top*