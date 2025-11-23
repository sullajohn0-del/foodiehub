# Django command wrapper - Always uses virtual environment Python
# Usage: .\django.ps1 makemigrations
# Usage: .\django.ps1 migrate
# Usage: .\django.ps1 runserver
# Usage: .\django.ps1 createsuperuser

$pythonExe = "C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe"
$managePy = "manage.py"

if ($args.Count -eq 0) {
    Write-Host "Usage: .\django.ps1 <command> [options]" -ForegroundColor Yellow
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "  .\django.ps1 makemigrations" -ForegroundColor Cyan
    Write-Host "  .\django.ps1 migrate" -ForegroundColor Cyan
    Write-Host "  .\django.ps1 runserver" -ForegroundColor Cyan
    Write-Host "  .\django.ps1 createsuperuser" -ForegroundColor Cyan
    exit
}

& $pythonExe $managePy $args

