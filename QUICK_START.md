# Quick Start Guide - Django Project

## The Easiest Way to Run Django Commands

### Option 1: Direct Python Path (No Activation Needed) ⭐ RECOMMENDED

Just use the full path to Python from the virtual environment:

```powershell
# Navigate to project directory
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject

# Run any Django command
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py makemigrations
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py migrate
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py runserver
```

### Option 2: Enable PowerShell Scripts (One-Time Setup)

If you want to use the activation script, first enable PowerShell script execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then you can use:
```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
.\activate_env.ps1
python manage.py makemigrations
```

### Option 3: Use Batch File (Works Without Execution Policy)

```cmd
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
activate_env.bat
python manage.py makemigrations
```

### Option 4: Use Helper Script (After Enabling Execution Policy)

```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
.\run_django.ps1 makemigrations
.\run_django.ps1 migrate
.\run_django.ps1 runserver
```

## Common Commands

```powershell
# Create migrations
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py makemigrations

# Apply migrations
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py migrate

# Run development server
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py runserver

# Create superuser
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py createsuperuser
```

## Troubleshooting

**Error: "running scripts is disabled on this system"**
- Use Option 1 (direct Python path) - no activation needed!
- Or enable execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Error: "ModuleNotFoundError: No module named 'django'"**
- Make sure you're using the Python from the virtual environment
- Use the full path: `C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe`

