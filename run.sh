#!/bin/bash
# Sequential Thinking MCP Server - Unix/Linux/Mac Run Script

set -e

echo "========================================"
echo "Sequential Thinking MCP Server"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run ./setup.sh first to create the virtual environment."
    exit 1
fi

echo "Starting server..."
echo "Server will be available at: http://localhost:10000/mcp/"
echo "Press Ctrl+C to stop the server"
echo ""

# Activate virtual environment and run server
source .venv/bin/activate && python server.py

