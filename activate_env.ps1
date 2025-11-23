# PowerShell script to activate virtual environment and run Django commands
# Usage: .\activate_env.ps1

$venvPath = "C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    & $venvPath
    Write-Host ""
    Write-Host "✓ Virtual environment activated!" -ForegroundColor Green
    Write-Host ""
    Write-Host "You can now run Django commands:" -ForegroundColor Yellow
    Write-Host "  python manage.py makemigrations" -ForegroundColor Cyan
    Write-Host "  python manage.py migrate" -ForegroundColor Cyan
    Write-Host "  python manage.py runserver" -ForegroundColor Cyan
    Write-Host "  python manage.py createsuperuser" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Or use the wrapper script (no activation needed):" -ForegroundColor Yellow
    Write-Host "  .\django.ps1 makemigrations" -ForegroundColor Cyan
    Write-Host "  .\django.ps1 migrate" -ForegroundColor Cyan
    Write-Host "  .\django.ps1 runserver" -ForegroundColor Cyan
} else {
    Write-Host "Error: Virtual environment not found at $venvPath" -ForegroundColor Red
    exit 1
}

