# FoodieHub Deployment Helper Script
# This script helps prepare your project for deployment

Write-Host "`n=== FoodieHub Deployment Helper ===" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
Write-Host "Checking Git installation..." -ForegroundColor Yellow
try {
    $gitVersion = git --version 2>&1
    Write-Host "✓ Git is installed: $gitVersion" -ForegroundColor Green
    $gitInstalled = $true
} catch {
    Write-Host "✗ Git is NOT installed" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git first:" -ForegroundColor Yellow
    Write-Host "  1. Go to: https://git-scm.com/download/win" -ForegroundColor Cyan
    Write-Host "  2. Download and install Git" -ForegroundColor Cyan
    Write-Host "  3. Restart PowerShell after installation" -ForegroundColor Cyan
    Write-Host "  4. Run this script again" -ForegroundColor Cyan
    $gitInstalled = $false
    exit 1
}

Write-Host ""

# Check if Git repository is initialized
Write-Host "Checking Git repository..." -ForegroundColor Yellow
if (Test-Path .git) {
    Write-Host "✓ Git repository is initialized" -ForegroundColor Green
} else {
    Write-Host "✗ Git repository is NOT initialized" -ForegroundColor Yellow
    Write-Host ""
    $init = Read-Host "Initialize Git repository now? (y/n)"
    if ($init -eq 'y' -or $init -eq 'Y') {
        git init
        Write-Host "✓ Git repository initialized" -ForegroundColor Green
    }
}

Write-Host ""

# Check for .gitignore
Write-Host "Checking .gitignore..." -ForegroundColor Yellow
if (Test-Path .gitignore) {
    Write-Host "✓ .gitignore exists" -ForegroundColor Green
} else {
    Write-Host "✗ .gitignore is missing" -ForegroundColor Red
}

Write-Host ""

# Check for requirements.txt
Write-Host "Checking requirements.txt..." -ForegroundColor Yellow
if (Test-Path requirements.txt) {
    Write-Host "✓ requirements.txt exists" -ForegroundColor Green
} else {
    Write-Host "✗ requirements.txt is missing" -ForegroundColor Red
}

Write-Host ""

# Check for Procfile
Write-Host "Checking Procfile..." -ForegroundColor Yellow
if (Test-Path Procfile) {
    Write-Host "✓ Procfile exists" -ForegroundColor Green
} else {
    Write-Host "✗ Procfile is missing" -ForegroundColor Red
}

Write-Host ""

# Summary
Write-Host "=== Deployment Readiness ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Create GitHub account (if you don't have one)" -ForegroundColor White
Write-Host "  2. Create a new repository on GitHub" -ForegroundColor White
Write-Host "  3. Run these commands:" -ForegroundColor White
Write-Host ""
Write-Host "     git add ." -ForegroundColor Cyan
Write-Host "     git commit -m 'FoodieHub ready for deployment'" -ForegroundColor Cyan
Write-Host "     git remote add origin https://github.com/YOUR_USERNAME/foodiehub.git" -ForegroundColor Cyan
Write-Host "     git branch -M main" -ForegroundColor Cyan
Write-Host "     git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "  4. Deploy to Render:" -ForegroundColor White
Write-Host "     - Go to https://render.com" -ForegroundColor Cyan
Write-Host "     - Create PostgreSQL database" -ForegroundColor Cyan
Write-Host "     - Create Web Service" -ForegroundColor Cyan
Write-Host "     - Connect your GitHub repository" -ForegroundColor Cyan
Write-Host ""
Write-Host "For detailed instructions, see: START_DEPLOYMENT.md" -ForegroundColor Yellow
Write-Host ""

