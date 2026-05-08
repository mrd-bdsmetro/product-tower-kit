Write-Host "=== API KEYS CHECK ===" -ForegroundColor Cyan
$providers = @('VALYU_API_KEY', 'FIRECRAWL_API_KEY', 'BRAVE_API_KEY', 'TAVILY_API_KEY')
foreach ($p in $providers) {
    $val = [Environment]::GetEnvironmentVariable($p)
    if ($val) {
        $masked = $val.Substring(0, 8) + "..."
        Write-Host "[OK] $p : $masked" -ForegroundColor Green
    } else {
        Write-Host "[--] $p : NOT SET" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "=== INSTALLED PACKAGES ===" -ForegroundColor Cyan
pip list 2>$null | ForEach-Object {
    if ($_ -match "valyu|firecrawl|brave|tavily|crawl4ai") {
        Write-Host $_
    }
}

Write-Host ""
Write-Host "=== PROVIDER STATUS ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Valyu:     " -NoNewline
try { Import-Module valyu -ErrorAction Stop; Write-Host "INSTALLED" -ForegroundColor Green } catch {
    $v = [Environment]::GetEnvironmentVariable('VALYU_API_KEY')
    if ($v) { Write-Host "KEY SET, module missing" -ForegroundColor Yellow }
    else { Write-Host "NOT SETUP" -ForegroundColor Red }
}

Write-Host "Firecrawl: " -NoNewline
try { pip show firecrawl-py -ErrorAction Stop | Out-Null; Write-Host "INSTALLED" -ForegroundColor Green } catch {
    $v = [Environment]::GetEnvironmentVariable('FIRECRAWL_API_KEY')
    if ($v) { Write-Host "KEY SET, module missing" -ForegroundColor Yellow }
    else { Write-Host "NOT SETUP" -ForegroundColor Red }
}

Write-Host "Brave:     " -NoNewline
$v = [Environment]::GetEnvironmentVariable('BRAVE_API_KEY')
if ($v) { Write-Host "READY ($($v.Substring(0,8))...)" -ForegroundColor Green }
else { Write-Host "NOT SETUP" -ForegroundColor Red }

Write-Host "Tavily:    " -NoNewline
try { pip show tavily-python -ErrorAction Stop | Out-Null; Write-Host "INSTALLED" -ForegroundColor Green } catch {
    $v = [Environment]::GetEnvironmentVariable('TAVILY_API_KEY')
    if ($v) { Write-Host "KEY SET, module missing" -ForegroundColor Yellow }
    else { Write-Host "NOT SETUP" -ForegroundColor Red }
}

Write-Host "crawl4ai:  " -NoNewline
try { pip show crawl4ai -ErrorAction Stop | Out-Null; Write-Host "INSTALLED (FREE, no key needed)" -ForegroundColor Green } catch {
    Write-Host "NOT INSTALLED" -ForegroundColor Red
}
