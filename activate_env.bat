@echo off
REM Batch script to activate virtual environment for Django
REM Usage: activate_env.bat

call C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\activate.bat
echo Virtual environment activated!
echo You can now run Django commands like:
echo   python manage.py makemigrations
echo   python manage.py migrate
echo   python manage.py runserver

