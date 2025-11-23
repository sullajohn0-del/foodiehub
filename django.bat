@echo off
REM Django command wrapper - Always uses virtual environment Python
REM Usage: django.bat makemigrations
REM Usage: django.bat migrate
REM Usage: django.bat runserver

set PYTHON_EXE=C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe
set MANAGE_PY=manage.py

if "%~1"=="" (
    echo Usage: django.bat ^<command^> [options]
    echo Examples:
    echo   django.bat makemigrations
    echo   django.bat migrate
    echo   django.bat runserver
    exit /b
)

%PYTHON_EXE% %MANAGE_PY% %*

