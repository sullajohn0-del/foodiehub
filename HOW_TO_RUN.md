# How to Run Django Commands

## ⚠️ Problem
You're getting: `ModuleNotFoundError: No module named 'django'`

This happens because you're using the system Python instead of the virtual environment Python.

## ✅ Solutions (Choose One)

### Solution 1: Use the Wrapper Script (EASIEST - No Activation Needed!)

**For PowerShell:**
```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject

# Run any Django command
.\django.ps1 makemigrations
.\django.ps1 migrate
.\django.ps1 runserver
.\django.ps1 createsuperuser
```

**For Command Prompt:**
```cmd
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject

# Run any Django command
django.bat makemigrations
django.bat migrate
django.bat runserver
django.bat createsuperuser
```

### Solution 2: Use Full Python Path (Works Everywhere)

```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject

# Always use the full path to the virtual environment Python
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py makemigrations
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py migrate
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py runserver
```

### Solution 3: Activate Virtual Environment First

**Step 1: Activate the virtual environment**

**For PowerShell:**
```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
.\activate_env.ps1
```

**For Command Prompt:**
```cmd
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
activate_env.bat
```

**Step 2: Now you can use `python` directly**
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**Note:** You must activate the virtual environment in EACH new terminal window/session!

## 🎯 Recommended: Use Solution 1 (Wrapper Script)

The wrapper script (`django.ps1` or `django.bat`) is the easiest because:
- ✅ No activation needed
- ✅ Always uses the correct Python
- ✅ Works in any terminal
- ✅ Simple to remember

## Quick Test

Try this to verify everything works:

```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
.\django.ps1 --version
```

You should see Django version 5.2.8

## Common Commands

```powershell
# Create migrations
.\django.ps1 makemigrations

# Apply migrations
.\django.ps1 migrate

# Run development server
.\django.ps1 runserver

# Create superuser
.\django.ps1 createsuperuser

# Run tests
.\django.ps1 test

# Django shell
.\django.ps1 shell
```

