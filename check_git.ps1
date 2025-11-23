# Quick Git Installation Checker
# Run this after installing Git and restarting PowerShell

Write-Host "`n=== Git Installation Check ===" -ForegroundColor Cyan
Write-Host ""

# Add Git to PATH if installed but not in PATH
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    if (Test-Path "C:\Program Files\Git\bin\git.exe") {
        $env:Path += ";C:\Program Files\Git\bin"
        Write-Host "⚠️  Git found but not in PATH. Added to current session." -ForegroundColor Yellow
        Write-Host "   You may need to restart PowerShell for permanent fix." -ForegroundColor Yellow
        Write-Host ""
    }
}

try {
    $gitVersion = git --version 2>&1
    if ($gitVersion -match "git version") {
        Write-Host "✅ SUCCESS! Git is installed!" -ForegroundColor Green
        Write-Host "   $gitVersion" -ForegroundColor White
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Yellow
        Write-Host "  1. Run: .\setup_git.ps1" -ForegroundColor Cyan
        Write-Host "  2. Follow: DEPLOYMENT_CHECKLIST_SIMPLE.md" -ForegroundColor Cyan
        Write-Host ""
        exit 0
    }
} catch {
    Write-Host "❌ Git is NOT installed or not in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please do this:" -ForegroundColor Yellow
    Write-Host "  1. Install Git from: https://git-scm.com/download/win" -ForegroundColor White
    Write-Host "  2. During installation, choose:" -ForegroundColor White
    Write-Host "     'Git from the command line and also from 3rd-party software'" -ForegroundColor Cyan
    Write-Host "  3. Complete installation" -ForegroundColor White
    Write-Host "  4. CLOSE and REOPEN PowerShell" -ForegroundColor White
    Write-Host "  5. Run this script again: .\check_git.ps1" -ForegroundColor White
    Write-Host ""
    Write-Host "Opening Git download page..." -ForegroundColor Yellow
    Start-Process "https://git-scm.com/download/win"
    exit 1
}

