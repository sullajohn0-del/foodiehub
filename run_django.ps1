# Simple Django command runner
# Usage: .\run_django.ps1 makemigrations
# Usage: .\run_django.ps1 migrate
# Usage: .\run_django.ps1 runserver

param(
    [Parameter(Mandatory=$true)]
    [string]$Command
)

$pythonPath = "C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe"
$managePy = "manage.py"

& $pythonPath $managePy $Command $args

