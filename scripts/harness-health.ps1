<#
.SYNOPSIS
    Product Tower Kit - Harness Health Check.
.DESCRIPTION
    Checks required files, SKILL.md validity, agent definitions, commands, hooks, and package structure.
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

    $status = if ($Pass) { "[OK]" } else { "[FAIL]" }
    $color = if ($Pass) { "Green" } else { "Red" }
    $suffix = if ($Detail) { " - $Detail" } else { "" }
    Write-Host ("  " + $status + " " + $Label + $suffix) -ForegroundColor $color

    if (-not $Pass) {
        $script:issues += [pscustomobject]@{
            Category = $Category
            Label = $Label
            Detail = $Detail
        }
    }
}

function Test-RelativePath {
    param([string]$RelativePath)
    return (Test-Path (Join-Path $root $RelativePath))
}

function Read-Json {
    param([string]$RelativePath)
    $path = Join-Path $root $RelativePath
    if (-not (Test-Path $path)) { return $null }
    try {
        return (Get-Content $path -Raw | ConvertFrom-Json)
    } catch {
        return $null
    }
}

function Test-SkillFrontmatter {
    param([string]$RelativePath)
    $path = Join-Path $root $RelativePath
    if (-not (Test-Path $path)) { return $false }
    $content = Get-Content $path -Raw
    return ($content -match "^---\s*\n" -and $content -match "name:" -and $content -match "description:")
}

function Test-HasSection {
    param([string]$RelativePath, [string]$Section)
    $path = Join-Path $root $RelativePath
    if (-not (Test-Path $path)) { return $false }
    $content = Get-Content $path -Raw
    return ($content -match [regex]::Escape($Section))
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  PRODUCT TOWER KIT - HARNESS HEALTH" -ForegroundColor Cyan
Write-Host ("  " + (Get-Date -Format "yyyy-MM-dd HH:mm")) -ForegroundColor DarkGray
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# === PACKAGE FILES ===
Write-Host "  Package Files" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

foreach ($file in @("package.json", "index.js", "README.md", "LICENSE", "CHANGELOG.md", ".gitignore")) {
    Add-Check "Package" $file (Test-RelativePath $file) "required"
}

$pkg = Read-Json "package.json"
Add-Check "Package" "package.json parses" ($null -ne $pkg) "valid JSON"

if ($pkg) {
    Add-Check "Package" "name is product-tower-kit" ($pkg.name -eq "product-tower-kit") ("actual: " + $pkg.name)
    Add-Check "Package" "has bin entry" ($null -ne $pkg.bin) "CLI entry point"
    Add-Check "Package" "has files array" ($null -ne $pkg.files) "npm publish filter"
    Add-Check "Package" "license is proprietary" ($pkg.license -match "SEE LICENSE") ("actual: " + $pkg.license)
}

# === CLI ===
Write-Host ""
Write-Host "  CLI Entry Point" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

Add-Check "CLI" "bin/product-tower.js exists" (Test-RelativePath "bin\product-tower.js") "CLI wrapper"
Add-Check "CLI" "bin/product-tower.js has shebang" (Test-HasSection "bin\product-tower.js" "#!/usr/bin/env node") "Node CLI"

# === SKILLS ===
Write-Host ""
Write-Host "  Skills (.claude/skills/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

$expectedSkills = @(
    "product-tower",
    "market-research",
    "market-segmentation",
    "user-discovery",
    "pmf-validator",
    "pricing-strategy",
    "competitor-analysis",
    "deep-research-parser",
    "analytics-feedback",
    "delivery-tower",
    "sales-tower",
    "product-sale"
)

foreach ($skill in $expectedSkills) {
    $skillPath = ".claude\skills\$skill\SKILL.md"
    $exists = Test-RelativePath $skillPath
    Add-Check "Skills" "$skill/SKILL.md exists" $exists "required"

    if ($exists) {
        $hasFrontmatter = Test-SkillFrontmatter $skillPath
        Add-Check "Skills" "$skill has YAML frontmatter" $hasFrontmatter "name + description"

        $hasGoal = Test-HasSection $skillPath "## Goal" -or $content -match [regex]::Escape("# $skill")
        Add-Check "Skills" "$skill has Goal section" $hasGoal "skill header"
    }
}

# === AGENTS ===
Write-Host ""
Write-Host "  Agents (.claude/agents/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

$expectedAgents = @(
    "product-planner",
    "market-researcher",
    "anti-bias-challenger",
    "pmf-validator",
    "feature-scoper"
)

foreach ($agent in $expectedAgents) {
    $agentPath = ".claude\agents\$agent.md"
    $exists = Test-RelativePath $agentPath
    Add-Check "Agents" "$agent.md exists" $exists "required"

    if ($exists) {
        $hasRole = Test-HasSection $agentPath "## Role"
        Add-Check "Agents" "$agent has Role section" $hasRole "agent definition"

        $hasBehavior = Test-HasSection $agentPath "## Behavior"
        Add-Check "Agents" "$agent has Behavior section" $hasBehavior "agent definition"
    }
}

# === COMMANDS ===
Write-Host ""
Write-Host "  Commands (.claude/commands/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

$expectedCommands = @(
    "pt-init",
    "pt-research",
    "pt-validate",
    "pt-scope",
    "pt-assess",
    "pt-status",
    "pt-report"
)

foreach ($cmd in $expectedCommands) {
    $cmdPath = ".claude\commands\$cmd.md"
    $exists = Test-RelativePath $cmdPath
    Add-Check "Commands" "$cmd.md exists" $exists "required"

    if ($exists) {
        $hasUsage = Test-HasSection $cmdPath "## Usage"
        Add-Check "Commands" "$cmd has Usage section" $hasUsage "command definition"
    }
}

# === HOOKS ===
Write-Host ""
Write-Host "  Hooks (.claude/hooks/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

$expectedHooks = @(
    "gate-check.sh",
    "pmf-alert.sh",
    "tier-progress.sh"
)

foreach ($hook in $expectedHooks) {
    $hookPath = ".claude\hooks\$hook"
    $exists = Test-RelativePath $hookPath
    Add-Check "Hooks" "$hook exists" $exists "required"
}

Add-Check "Hooks" "settings.json exists" (Test-RelativePath ".claude\settings.json") "hook config"

# === RULES ===
Write-Host ""
Write-Host "  Rules (.claude/rules/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

$expectedRules = @(
    "product-workflow",
    "gate-enforcement",
    "anti-bias-rules"
)

foreach ($rule in $expectedRules) {
    $rulePath = ".claude\rules\$rule.md"
    Add-Check "Rules" "$rule.md exists" (Test-RelativePath $rulePath) "required"
}

# === SCRIPTS ===
Write-Host ""
Write-Host "  Scripts (scripts/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

Add-Check "Scripts" "gate_checker.py exists" (Test-RelativePath "scripts\gate_checker.py") "Python CLI"

# Test Python script syntax
$pythonCmd = "python"
try {
    $pyVersion = & python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        $pythonCmd = "python3"
        $pyVersion = & python3 --version 2>&1
    }
    Add-Check "Scripts" "Python available" ($LASTEXITCODE -eq 0) ($pyVersion -join "")
} catch {
    Add-Check "Scripts" "Python available" $false "not found"
}

# === TEMPLATES ===
Write-Host ""
Write-Host "  Templates (templates/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

Add-Check "Templates" "product-plan.md exists" (Test-RelativePath "templates\product-plan.md") "plan template"

# === RESOURCES ===
Write-Host ""
Write-Host "  Resources (resources/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

Add-Check "Resources" "ecosystem-map.md exists" (Test-RelativePath "resources\ecosystem-map.md") "routing map"

# === DOCS ===
Write-Host ""
Write-Host "  Docs (docs/)" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

Add-Check "Docs" "quickstart.md exists" (Test-RelativePath "docs\quickstart.md") "user guide"

# === NPM SCRIPTS ===
Write-Host ""
Write-Host "  npm Scripts" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

if ($pkg) {
    foreach ($scriptName in @("test", "lint", "init")) {
        $hasScript = $null -ne $pkg.scripts.PSObject.Properties[$scriptName]
        Add-Check "npm" ("script: " + $scriptName) $hasScript "package.json"
    }
}

# === GATE CONSISTENCY ===
Write-Host ""
Write-Host "  Gate Consistency" -ForegroundColor White
Write-Host "  ------------------------------" -ForegroundColor DarkGray

# Check that gate_checker.py has all expected tiers
$gateCheckerPath = Join-Path $root "scripts\gate_checker.py"
if (Test-Path $gateCheckerPath) {
    $gateChecker = Get-Content $gateCheckerPath -Raw
    foreach ($tier in @("T-1", "T0", "T1", "T2", "T3", "T4", "T5", "T6", "AB1", "AB2", "AB3", "AB4", "AB5", "AB6", "T7", "T8", "T9", "T9.5", "T14")) {
        $hasTier = $gateChecker -match "`"$tier`""
        Add-Check "Gate" "tier $tier in gate_checker.py" $hasTier "NAMING_CONVENTION"
    }
}

# === SCORE ===
Write-Host ""

$score = if ($totalChecks -gt 0) { [math]::Round(($passedChecks / $totalChecks) * 100) } else { 0 }
$scoreColor = if ($issues.Count -eq 0) { "Green" } elseif ($score -ge 80) { "Yellow" } else { "Red" }

$checkSummary = "$passedChecks/$totalChecks checks passed"
Write-Host "============================================================" -ForegroundColor $scoreColor
Write-Host "  HEALTH SCORE: $score% ($checkSummary)" -ForegroundColor $scoreColor

if ($issues.Count -gt 0) {
    Write-Host ""
    Write-Host "  ACTION ITEMS:" -ForegroundColor Yellow
    foreach ($issue in $issues) {
    Write-Host "    [$($issue.Category)] $($issue.Label) - $($issue.Detail)" -ForegroundColor White
    }
}

Write-Host "============================================================" -ForegroundColor $scoreColor
Write-Host ""

if ($issues.Count -gt 0) { exit 1 }
exit 0
