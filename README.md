# Django Food Delivery Project

## Setup Instructions

### 1. Activate Virtual Environment

**For PowerShell:**
```powershell
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\Activate.ps1
```

Or use the helper script:
```powershell
.\activate_env.ps1
```

**For Command Prompt:**
```cmd
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\activate.bat
```

Or use the helper script:
```cmd
activate_env.bat
```

**Alternative (if activation doesn't work):**
You can use the Python executable directly from the virtual environment:
```powershell
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py <command>
```

### 2. Run Django Commands

Once the virtual environment is activated, you can run:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### 3. Common Issues

**Issue: "ModuleNotFoundError: No module named 'django'"**

**Solution:** Make sure you've activated the virtual environment before running Django commands. If activation doesn't work, use the full path to the virtual environment's Python:

```powershell
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe manage.py makemigrations
```

**Issue: "Activate.ps1 cannot be loaded because running scripts is disabled on this system"**

**Solution:** Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Installed Packages

- Django 5.2.8
- Pillow 12.0.0
- Other dependencies (asgiref, sqlparse, tzdata)

## Project Structure

```
myproject/
├── manage.py
├── myapp/          # Django app
├── myproject/      # Django project settings
└── db.sqlite3      # SQLite database
```

## Quick Start

1. Activate virtual environment
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`
5. Open browser to: `http://127.0.0.1:8000`

