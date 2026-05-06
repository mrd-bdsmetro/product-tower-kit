# Product Tower Kit — Code Standards

## Directory Structure Convention

```
product-tower-kit/
├── .claude/                    # Claude Code integration (DO NOT MODIFY STRUCTURE)
│   ├── agents/                 # Agent definitions (.md files)
│   ├── commands/               # Slash commands (.md files)
│   ├── hooks/                  # Automation hooks (.sh files)
│   ├── rules/                  # Policy rules (.md files)
│   ├── settings.json           # Hook configuration
│   └── skills/                 # Skill directories (SKILL.md files)
├── bin/                        # CLI entry point
├── docs/                       # Documentation
├── resources/                  # Reference materials
├── scripts/                    # Core scripts (Python, PowerShell, Node.js)
├── templates/                  # Output templates
├── index.js                    # Module exports
└── package.json                # Package configuration
```

---

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Skills | `kebab-case/SKILL.md` | `market-research/SKILL.md` |
| Agents | `kebab-case.md` | `product-planner.md` |
| Commands | `pt-kebab-case.md` | `pt-init.md` |
| Hooks | `kebab-case.sh` | `gate-check.sh` |
| Rules | `kebab-case.md` | `gate-enforcement.md` |
| Python scripts | `snake_case.py` | `gate_checker.py`, `valyu_search.py` |
| PowerShell scripts | `kebab-case.ps1` | `harness-health.ps1` |
| Node.js scripts | `kebab-case.js` | `syntax-check.js` |
| Tower output | `t{N}_{snake_case}.md` | `t0_market_research.md` |
| Anti-bias output | `ab{N}_{snake_case}.md` | `ab1_counter_search.md` |

---

## SKILL.md Format

### Frontmatter

```yaml
---
name: skill-name
version: 1.0.0
description: One-line description of the skill
triggers:
  - "keyword1"
  - "keyword2"
---
```

### Required Sections

```markdown
# skill-name

## Goal
One-paragraph description of what this skill does.

## When to Use
- Trigger condition 1
- Trigger condition 2

## Workflow
1. Step 1
2. Step 2
3. Step 3

## Output Files
- `data/t0_market_research.md` — Description

## References
- [Link](url)
```

### Validation Rules

- Must start with `---` (YAML frontmatter delimiter)
- Must contain `name:` field
- Must contain `description:` field
- Must have `## Goal` section
- Must close frontmatter with `---`

---

## Agent Markdown Format

### Required Sections

```markdown
# agent-name

## Role
One-paragraph description of the agent's role.

## Behavior
- Behavior rule 1
- Behavior rule 2
- Behavior rule 3

## Activation
Trigger phrases or conditions:
- "trigger phrase 1"
- "trigger phrase 2"

## Output
- Output format description
- File naming convention
```

### Validation Rules

- Must have `## Role` section
- Must have `## Behavior` section
- Must have `## Activation` section

---

## Command Markdown Format

### Required Sections

```markdown
# /pt:command-name

## Usage
```
/pt:command-name [args]
```

## Behavior
1. Step 1
2. Step 2
3. Step 3

## Gate
- Required tiers: T0, T1, ...
- PMF threshold: ≥30/50

## Output
- File: `data/t0_market_research.md`
- Format: Markdown with frontmatter
```

### Validation Rules

- Must have `## Usage` section
- File must be named `pt-{command}.md`

---

## Python Code Standards

### File Structure

```python
#!/usr/bin/env python3
"""
Module docstring with usage examples.
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

# Fix Unicode on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Constants
CONSTANT_NAME = "value"

# Functions
def function_name():
    """Docstring."""
    pass

# Main
def main():
    """Entry point."""
    if len(sys.argv) < 2:
        print("Usage: script.py <args>")
        sys.exit(1)
    
    # Logic here
    pass

if __name__ == "__main__":
    main()
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Constants | UPPER_SNAKE_CASE | `PMF_THRESHOLD` |
| Functions | snake_case | `cmd_init()` |
| Variables | snake_case | `project_dir` |
| Classes | PascalCase | `GateChecker` |

### Error Handling

```python
# Exit codes
sys.exit(0)  # Success
sys.exit(1)  # Error

# Error messages
print(f"❌ Error: {message}")
print(f"✅ Success: {message}")
```

---

## PowerShell Code Standards

### File Structure

```powershell
<#
.SYNOPSIS
    Brief description.
.DESCRIPTION
    Detailed description.
#>

$ErrorActionPreference = "Continue"
$root = (Get-Item $PSScriptRoot).Parent.FullName
$totalChecks = 0
$passedChecks = 0
$issues = @()

function Add-Check {
    param(
        [string]$Category,
        [string]$Label,
        [bool]$Pass,
        [string]$Detail = ""
    )
    $script:totalChecks++
    if ($Pass) { $script:passedChecks++ }
    # Output and tracking
}

function Run-Check {
    param(
        [string]$Name,
        [string]$Command
    )
    # Execute and track
}

# Main logic
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Functions | PascalCase | `Add-Check` |
| Variables | $camelCase | `$totalChecks` |
| Parameters | PascalCase | `-Category` |

### Patterns

```powershell
# Add-Check pattern (for static checks)
Add-Check "Category" "Label" $condition "detail"

# Run-Check pattern (for dynamic checks)
$results += Run-Check "name" "command"
```

---

## Node.js Code Standards

### File Structure

```javascript
// Comment describing the file

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
let passed = 0;
let failed = 0;

function read(relativePath) {
  return fs.readFileSync(path.join(ROOT, relativePath), 'utf8');
}

function exists(relativePath) {
  return fs.existsSync(path.join(ROOT, relativePath));
}

function check(name, fn) {
  try {
    fn();
    console.log(`  [OK] ${name}`);
    passed++;
  } catch (err) {
    console.log(`  [FAIL] ${name}: ${err.message}`);
    failed++;
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

// Main logic
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Constants | UPPER_SNAKE_CASE | `ROOT` |
| Functions | camelCase | `readJson()` |
| Variables | camelCase | `passed` |

### Patterns

```javascript
// check/assert pattern
check('description', () => {
  assert(condition, 'error message');
});
```

---

## Git Commit Conventions

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation |
| `style` | Formatting |
| `refactor` | Code refactor |
| `test` | Tests |
| `chore` | Maintenance |

### Examples

```
feat(gate): add PMF penalty system
fix(cli): handle missing Python gracefully
docs(readme): update quickstart guide
test(invariants): add gate consistency checks
```

---

## Quality Gates

### Before Commit

1. **Syntax check passes:** `npm run test:syntax`
2. **Invariant checks pass:** `npm run test:invariants`
3. **Harness health passes:** `npm run harness:health`

### Before Release

1. **All tests pass:** `npm run harness:hardness`
2. **No FAIL items in health check**
3. **All SKILL.md files have valid frontmatter**
4. **All agents have required sections**
5. **All commands have Usage section**
6. **Gate checker has all tiers**
