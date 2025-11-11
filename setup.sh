#!/bin/bash
# Sequential Thinking MCP Server - Unix/Linux/Mac Setup Script
# This script creates a virtual environment and installs dependencies

set -e

echo "========================================"
echo "Sequential Thinking MCP Server Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.11 or higher"
    exit 1
fi

echo "[1/4] Checking Python version..."
python3 --version

echo ""
echo "[2/4] Creating virtual environment..."
if [ -d ".venv" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    python3 -m venv .venv
    echo "Virtual environment created successfully!"
fi

echo ""
echo "[3/4] Activating virtual environment..."
source .venv/bin/activate

echo ""
echo "[4/4] Installing dependencies..."
python -m pip install --upgrade pip
pip install fastapi "mcp[cli]" python-dotenv uvicorn

echo ""
echo "========================================"
echo "Setup completed successfully!"
echo "========================================"
echo ""
echo "To start the server:"
echo "  1. Activate the virtual environment: source .venv/bin/activate"
echo "  2. Run the server: python server.py"
echo ""
echo "Or simply run: ./run.sh"
echo ""

