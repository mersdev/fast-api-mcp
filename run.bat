@echo off
REM Sequential Thinking MCP Server - Windows Run Script

echo ========================================
echo Sequential Thinking MCP Server
echo ========================================
echo.

REM Check if virtual environment exists
if not exist .venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first to create the virtual environment.
    pause
    exit /b 1
)

echo Starting server...
echo Server will be available at: http://localhost:10000/mcp/
echo Press Ctrl+C to stop the server
echo.

REM Activate virtual environment and run server
call .venv\Scripts\activate.bat && python server.py

