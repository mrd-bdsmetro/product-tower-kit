---
name: market-segmentation
version: 1.0.0
description: |
  T1-T3 Market Segmentation skill. Target market selection, 3-5 segments, segment filter.
triggers:
  - "phân khúc thị trường"
  - "target market"
  - "segmentation"
  - "chọn thị trường"
---

# Market Segmentation — T1-T3

## Goal
Chọn thị trường mục tiêu, phân khúc, và filter segments.

---

## T1: TARGET MARKET

**Decision Matrix:** Expertise × Market Size

```
| Segment | Expertise (1-5) | Market Size (1-5) | Score |
|---------|-----------------|-------------------|-------|
| A       |                 |                   |       |
| B       |                 |                   |       |
```

**Output:** `data/t1_target_market.md`

---

## T2: MARKET SEGMENTATION

3-5 segments với:
- Demographic (age, income, location)
- Behavioral (habits, preferences)
- Psychographic (values, lifestyle)

**Output:** `data/t2_segmentation.md`

---

## T3: SEGMENT FILTER

3 criteria:
1. Đủ lớn? (market size)
2. Serve được? (capability)
3. Align strategy? (vision)

**Output:** `data/t3_segment_filter.md`

---

## GATE
- T0 data phải tồn tại
- Nếu T1 output cover đủ T2+T3 → tạo stub files (merge OK)
