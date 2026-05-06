# /pt:init — Initialize Product Tower Project

## Usage
```
/pt:init
/pt:init [project-name]
```

## Behavior
1. Create `data/` directory
2. Create `pipeline_state.json` with initial state
3. Show welcome message with quickstart guide
4. Suggest first action (T-1 rapid validation or T0 research)

## Output
```
✅ Product Tower initialized for [project]

📁 Structure created:
├── data/                    # Tower output files
└── pipeline_state.json     # Pipeline state

🚀 Next steps:
1. "research thị trường [ngành]" — Start T0
2. "parse deep research [file]" — If you have Deep Research output
3. "assess [project]" — Check current state
```
