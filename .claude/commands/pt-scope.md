# /pt:scope - Run T8-T9 Feature Scoping

## Usage
```
/pt:scope features
/pt:scope MVP
/pt:scope [project]
```

## Behavior
1. Check PMF gate (≥30/50)
2. Activate feature-scoper agent
3. Read T4-T6 user needs
4. Create MoSCoW feature set
5. Write user stories
6. Output `data/t8_features.md` + `data/t9_user_stories.md`

## Gate
- PMF(adjusted) ≥ 30/50

## Output
```
🎯 FEATURE SCOPING - [Project]

PMF: X/50 ✅
Features: X must, X should, X could
User Stories: X stories

✅ T8 complete: data/t8_features.md
✅ T9 complete: data/t9_user_stories.md

➡️ Next: "pricing" (T9.5) or "design" (T10)
```
