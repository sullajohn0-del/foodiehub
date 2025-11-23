# Git Setup Helper for FoodieHub Deployment
# This script helps you set up Git and prepare for deployment

# Add Git to PATH if needed
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    if (Test-Path "C:\Program Files\Git\bin\git.exe") {
        $env:Path += ";C:\Program Files\Git\bin"
        Write-Host "Git found but not in PATH. Added to current session." -ForegroundColor Yellow
        Write-Host ""
    }
}

Write-Host "`n=== FoodieHub Git Setup Helper ===" -ForegroundColor Cyan
Write-Host ""

# Check Git installation
Write-Host "Step 1: Checking Git installation..." -ForegroundColor Yellow
try {
    $gitVersion = git --version 2>&1
    if ($gitVersion -match "git version") {
        Write-Host "✓ Git is installed: $gitVersion" -ForegroundColor Green
        $gitInstalled = $true
    } else {
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

# Check if Git is configured
Write-Host "Step 2: Checking Git configuration..." -ForegroundColor Yellow
try {
    $gitUser = git config --global user.name 2>&1
    $gitEmail = git config --global user.email 2>&1
    
    if ($gitUser -and $gitUser -notmatch "error" -and $gitUser.Trim() -ne "") {
        Write-Host "✓ Git user name: $gitUser" -ForegroundColor Green
    } else {
        Write-Host "✗ Git user name not set" -ForegroundColor Yellow
        $userName = Read-Host "Enter your name (for Git commits)"
        if ($userName) {
            git config --global user.name $userName
            Write-Host "✓ Git user name set" -ForegroundColor Green
        }
    }
    
    if ($gitEmail -and $gitEmail -notmatch "error" -and $gitEmail.Trim() -ne "") {
        Write-Host "✓ Git email: $gitEmail" -ForegroundColor Green
    } else {
        Write-Host "✗ Git email not set" -ForegroundColor Yellow
        $userEmail = Read-Host "Enter your email (for Git commits)"
        if ($userEmail) {
            git config --global user.email $userEmail
            Write-Host "✓ Git email set" -ForegroundColor Green
        }
    }
} catch {
    Write-Host "Error configuring Git" -ForegroundColor Red
}

Write-Host ""

# Check if repository is initialized
Write-Host "Step 3: Checking Git repository..." -ForegroundColor Yellow
if (Test-Path .git) {
    Write-Host "✓ Git repository is already initialized" -ForegroundColor Green
    Write-Host ""
    Write-Host "Current status:" -ForegroundColor Yellow
    git status --short
} else {
    Write-Host "✗ Git repository is NOT initialized" -ForegroundColor Yellow
    Write-Host ""
    $init = Read-Host "Initialize Git repository now? (y/n)"
    if ($init -eq 'y' -or $init -eq 'Y') {
        git init
        Write-Host "✓ Git repository initialized" -ForegroundColor Green
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Yellow
        Write-Host "  1. Run: git add ." -ForegroundColor Cyan
        Write-Host "  2. Run: git commit -m 'FoodieHub ready for deployment'" -ForegroundColor Cyan
        Write-Host "  3. Create GitHub repository" -ForegroundColor Cyan
        Write-Host "  4. Push to GitHub" -ForegroundColor Cyan
    }
}

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next: Follow DEPLOYMENT_CHECKLIST_SIMPLE.md for deployment steps" -ForegroundColor Yellow
Write-Host ""
