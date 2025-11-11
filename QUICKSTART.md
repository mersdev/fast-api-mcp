# Quick Start Guide

Get your Sequential Thinking MCP Server up and running in minutes!

## 🚀 One-Command Setup

### Windows

```bash
git clone https://github.com/mersdev/fast-api-mcp.git
cd fast-api-mcp
setup.bat
```

### Linux/Mac

```bash
git clone https://github.com/mersdev/fast-api-mcp.git
cd fast-api-mcp
chmod +x setup.sh run.sh
./setup.sh
```

## ▶️ Running the Server

### Windows
```bash
run.bat
```

### Linux/Mac
```bash
./run.sh
```

The server will start at: **http://localhost:10000/mcp/**

## 🔌 Connect to AI Assistants

### Cursor

1. Open Cursor
2. Go to **Settings** → **Chat Settings** → **MCP Servers**
3. Add this configuration:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "url": "http://localhost:10000/mcp/"
    }
  }
}
```

### Claude Desktop

1. Open your Claude Desktop config file:
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. Add this configuration:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "url": "http://localhost:10000/mcp/"
    }
  }
}
```

3. Restart Claude Desktop

## 🧪 Test the Server

Once the server is running, you can test it with curl:

```bash
curl http://localhost:10000/mcp/
```

Or open your browser and visit: http://localhost:10000/mcp/

## 🛠️ What the Setup Does

The setup script automatically:
1. ✅ Creates a Python virtual environment (`.venv`)
2. ✅ Upgrades pip to the latest version
3. ✅ Installs all required dependencies:
   - FastAPI (web framework)
   - MCP SDK (Model Context Protocol)
   - Uvicorn (ASGI server)
   - Python-dotenv (environment variables)

## 📁 Project Structure After Setup

```
fast-api-mcp/
├── .venv/                      # Virtual environment (created by setup)
├── sequential_thinking/        # Core library
│   ├── __init__.py
│   └── lib.py
├── server.py                   # Main server file
├── setup.bat                   # Windows setup script
├── setup.sh                    # Linux/Mac setup script
├── run.bat                     # Windows run script
├── run.sh                      # Linux/Mac run script
├── requirements.txt            # Dependencies
└── README.md                   # Full documentation
```

## 🎯 Using the Sequential Thinking Tool

Once connected to your AI assistant, you can use the `sequential_thinking` tool to:

- Break down complex problems into steps
- Revise thoughts as understanding deepens
- Branch into alternative reasoning paths
- Dynamically adjust the number of thoughts needed

### Example Usage

Ask your AI assistant:
> "Use the sequential thinking tool to solve this problem: How can I optimize my Python code for better performance?"

The AI will use the tool to think through the problem step-by-step!

## 🔧 Configuration

### Change Server Port

Set the `PORT` environment variable before running:

**Windows:**
```bash
set PORT=8000
run.bat
```

**Linux/Mac:**
```bash
PORT=8000 ./run.sh
```

### Disable Thought Logging

Set the `DISABLE_THOUGHT_LOGGING` environment variable:

**Windows:**
```bash
set DISABLE_THOUGHT_LOGGING=true
run.bat
```

**Linux/Mac:**
```bash
DISABLE_THOUGHT_LOGGING=true ./run.sh
```

## 🐛 Troubleshooting

### "Python is not installed"
- Install Python 3.11 or higher from [python.org](https://www.python.org/)
- Make sure Python is added to your PATH

### "Virtual environment not found"
- Run the setup script first: `setup.bat` (Windows) or `./setup.sh` (Linux/Mac)

### "Port already in use"
- Change the port: `PORT=8001 python server.py`
- Or stop the process using port 10000

### Server won't start
1. Make sure virtual environment is activated
2. Check if all dependencies are installed: `pip list`
3. Try reinstalling: Delete `.venv` folder and run setup again

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [SETUP_SUMMARY.md](SETUP_SUMMARY.md) for technical details
- Explore the [sequential_thinking/lib.py](sequential_thinking/lib.py) source code
- Customize the server for your needs

## 💡 Tips

1. **Keep the server running** while using AI assistants
2. **Check the console** for thought logs (unless disabled)
3. **Use Ctrl+C** to stop the server gracefully
4. **Restart the server** after making code changes

## 🎉 You're Ready!

Your Sequential Thinking MCP Server is now set up and ready to use. Enjoy enhanced problem-solving capabilities with your AI assistants!

For more information, visit: https://github.com/mersdev/fast-api-mcp

