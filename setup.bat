@echo off
REM Sequential Thinking MCP Server - Windows Setup Script
REM This script creates a virtual environment and installs dependencies

echo ========================================
echo Sequential Thinking MCP Server Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Checking Python version...
python --version

echo.
echo [2/4] Creating virtual environment...
if exist .venv (
    echo Virtual environment already exists. Skipping creation.
) else (
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
)

echo.
echo [3/4] Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo.
echo [4/4] Installing dependencies...
python -m pip install --upgrade pip
pip install fastapi "mcp[cli]" python-dotenv uvicorn
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To start the server:
echo   1. Activate the virtual environment: .venv\Scripts\activate
echo   2. Run the server: python server.py
echo.
echo Or simply run: run.bat
echo.
pause

