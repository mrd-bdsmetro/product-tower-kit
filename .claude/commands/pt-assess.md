# /pt:assess - Quick Tower Health Check

## Usage
```
/pt:assess
/pt:assess [project]
```

## Behavior
1. Scan all `data/t*.md` files
2. Score each tier 0-3
3. Calculate tower score (/42)
4. Identify weakest link
5. Suggest next action

## Scoring (0-3)
| Score | Meaning | Dấu hiệu |
|-------|---------|----------|
| 0 | ❌ Chưa làm | Không có data |
| 1 | 🟡 Giả định | Có ý tưởng, chưa validate |
| 2 | 🟢 Validated | Có data từ user thật |
| 3 | ✅ Proven | Data + kết quả thực tế |

## Output
```
🏗️ PRODUCT TOWER ASSESSMENT - [Project]

DATA:           T0 [0-3] | [detail]
FOUNDATION:     T1 [0-3] | T2 [0-3] | T3 [0-3]
DISCOVERY:      T4 [0-3] | T5 [0-3] | T6 [0-3]
STRATEGY:       T7 [0-3]
PRODUCT:        T8 [0-3] | T9 [0-3]
OFFER:          T9.5 [0-3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOWER SCORE: [X]/42
WEAKEST LINK: T[N]
NEXT ACTION: [specific action]
```
