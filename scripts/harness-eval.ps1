<#
.SYNOPSIS
    Product Tower Kit — Harness Evaluator.
.DESCRIPTION
    Runs deterministic checks and exits non-zero on failure.
#>

param(
    [switch]$IncludeGate,
    [switch]$IncludePython
)

$ErrorActionPreference = "Continue"
$root = (Get-Item $PSScriptRoot).Parent.FullName
$results = @()

function New-Result {
    param(
        [string]$Name,
        [bool]$Pass,
        [double]$Seconds,
        [string]$Output
    )

    return [pscustomobject]@{
        Name = $Name
        Pass = $Pass
        Seconds = $Seconds
        Output = $Output
    }
}

function Run-Check {
    param(
        [string]$Name,
        [string]$Command
    )

    Write-Host ("  [..] " + $Name) -ForegroundColor Yellow
    $start = Get-Date
    Push-Location $root
    try {
        $output = & cmd.exe /c "$Command" 2>&1
        $exitCode = $LASTEXITCODE
    } catch {
        $output = $_.Exception.Message
        $exitCode = 1
    } finally {
        Pop-Location
    }

    $elapsed = [math]::Round(((Get-Date) - $start).TotalSeconds, 1)
    $pass = $exitCode -eq 0
    $status = if ($pass) { "[OK]" } else { "[FAIL]" }
    $color = if ($pass) { "Green" } else { "Red" }
    Write-Host ("  " + $status + " " + $Name + " (" + $elapsed + "s)") -ForegroundColor $color

    return (New-Result $Name $pass $elapsed ([string]::Join("`n", $output)))
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  PRODUCT TOWER KIT — HARNESS EVAL" -ForegroundColor Cyan
Write-Host ("  " + (Get-Date -Format "yyyy-MM-dd HH:mm")) -ForegroundColor DarkGray
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Health check (always)
$results += Run-Check "health" "powershell -ExecutionPolicy Bypass -File scripts/harness-health.ps1"

# Node.js syntax check
$results += Run-Check "node-syntax" "node -c bin/product-tower.js"

# Package validation
$results += Run-Check "npm-pack" "npm pack --dry-run"

if ($IncludeGate) {
    # Python gate checker init test
    $testDir = Join-Path $env:TEMP "pt-test-$(Get-Random)"
    New-Item -ItemType Directory -Path $testDir -Force | Out-Null
    $results += Run-Check "gate-init" "python scripts/gate_checker.py `"$testDir`" init"
    $results += Run-Check "gate-status" "python scripts/gate_checker.py `"$testDir`" status"
    $results += Run-Check "gate-naming" "python scripts/gate_checker.py `"$testDir`" naming"
    Remove-Item -Recurse -Force $testDir -ErrorAction SilentlyContinue
} else {
    Write-Host "  [SKIP] gate (pass -IncludeGate to run Python gate checker tests)" -ForegroundColor DarkGray
}

if ($IncludePython) {
    # Python syntax check
    $results += Run-Check "python-syntax" "python -m py_compile scripts/gate_checker.py"
} else {
    Write-Host "  [SKIP] python-syntax (pass -IncludePython to validate Python syntax)" -ForegroundColor DarkGray
}

$failed = @($results | Where-Object { -not $_.Pass })
$verdict = if ($failed.Count -eq 0) { "PASS" } else { "FAIL" }
$color = if ($verdict -eq "PASS") { "Green" } else { "Red" }

Write-Host ""
Write-Host "============================================================" -ForegroundColor $color
Write-Host ("  VERDICT: " + $verdict) -ForegroundColor $color
Write-Host ("  CHECKS: " + (($results | Where-Object { $_.Pass }).Count) + "/" + $results.Count + " passed") -ForegroundColor $color

if ($failed.Count -gt 0) {
    Write-Host ""
    Write-Host "  FAILURE DETAILS:" -ForegroundColor Red
    foreach ($result in $failed) {
        Write-Host ""
        Write-Host ("  [" + $result.Name + "]") -ForegroundColor Red
        $lines = $result.Output -split "`n" | Select-Object -Last 30
        foreach ($line in $lines) {
            if ($line) { Write-Host ("    " + $line) -ForegroundColor DarkGray }
        }
    }
}

Write-Host "============================================================" -ForegroundColor $color
Write-Host ""

if ($failed.Count -gt 0) { exit 1 }
exit 0
