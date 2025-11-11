# Sequential Thinking MCP Server over FastAPI

A FastAPI-based MCP (Model Context Protocol) server that provides a sequential thinking tool for dynamic and reflective problem-solving through structured thinking processes.

## Features

- **Sequential Thinking Tool**: Break down complex problems into manageable steps
- **Dynamic Thought Revision**: Revise and refine thoughts as understanding deepens
- **Branching Reasoning**: Branch into alternative paths of reasoning
- **Adaptive Planning**: Adjust the total number of thoughts dynamically
- **Hypothesis Generation & Verification**: Generate and verify solution hypotheses
- **HTTP Transport**: Accessible over streamable HTTP using FastAPI

## Tool: sequential_thinking

Facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

**Inputs:**
- `thought` (string): The current thinking step
- `nextThoughtNeeded` (boolean): Whether another thought step is needed
- `thoughtNumber` (integer): Current thought number
- `totalThoughts` (integer): Estimated total thoughts needed
- `isRevision` (boolean, optional): Whether this revises previous thinking
- `revisesThought` (integer, optional): Which thought is being reconsidered
- `branchFromThought` (integer, optional): Branching point thought number
- `branchId` (string, optional): Branch identifier
- `needsMoreThoughts` (boolean, optional): If more thoughts are needed

## Installation

### Prerequisites
- Python 3.11 or higher

### Quick Setup (Recommended)

#### Windows
```bash
# Clone the repository
git clone https://github.com/mersdev/fast-api-mcp.git
cd fast-api-mcp

# Run the setup script (creates venv and installs dependencies)
setup.bat
```

#### Linux/Mac
```bash
# Clone the repository
git clone https://github.com/mersdev/fast-api-mcp.git
cd fast-api-mcp

# Make scripts executable
chmod +x setup.sh run.sh

# Run the setup script (creates venv and installs dependencies)
./setup.sh
```

### Manual Setup

If you prefer to set up manually:

```bash
# Clone the repository
git clone https://github.com/mersdev/fast-api-mcp.git
cd fast-api-mcp

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Server

#### Quick Start (Recommended)

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
./run.sh
```

#### Manual Start

Activate the virtual environment and run the server:

**Windows:**
```bash
.venv\Scripts\activate
python server.py
```

**Linux/Mac:**
```bash
source .venv/bin/activate
python server.py
```

The server will start on `http://0.0.0.0:10000` by default.

You can customize the port using the `PORT` environment variable:
```bash
PORT=8000 python server.py
```

### Debug with MCP Inspector

1. Make sure your virtual environment is activated and dependencies are installed

2. Launch the inspector:
```bash
# Windows
.venv\Scripts\activate
mcp dev server.py

# Linux/Mac
source .venv/bin/activate
mcp dev server.py
```

Then go to: `http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=...`

### Connect to Cursor

In Cursor, add your MCP server under Chat Settings > MCP Servers:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "url": "http://localhost:10000/mcp/"
    }
  }
}
```

✅ **Note**: You must include the trailing `/` in the URL.

### Connect to Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "url": "http://localhost:10000/mcp/"
    }
  }
}
```

## Use Cases

The Sequential Thinking tool is designed for:
- Breaking down complex problems into steps
- Planning and design with room for revision
- Analysis that might need course correction
- Problems where the full scope might not be clear initially
- Tasks that need to maintain context over multiple steps
- Situations where irrelevant information needs to be filtered out

## Environment Variables

- `PORT`: Server port (default: 10000)
- `DISABLE_THOUGHT_LOGGING`: Set to `true` to disable thought logging to console (default: false)

## Testing

To verify the tool works correctly, run the test script:

```bash
# Windows
.venv\Scripts\activate
python test_tool.py

# Linux/Mac
source .venv/bin/activate
python test_tool.py
```

The test script verifies:
- ✅ Tool returns proper dictionary output (not JSON strings)
- ✅ Thought sequencing works correctly
- ✅ Revisions are handled properly
- ✅ Thought history is maintained
- ✅ No Pydantic validation errors

## Project Structure

```
.
├── server.py                    # Main FastAPI MCP server
├── sequential_thinking/         # Sequential thinking library
│   ├── __init__.py
│   └── lib.py                   # Core logic for thought processing
├── test_tool.py                 # Test script for the tool
├── setup.bat                    # Windows setup script
├── setup.sh                     # Linux/Mac setup script
├── run.bat                      # Windows run script
├── run.sh                       # Linux/Mac run script
├── requirements.txt             # Python dependencies
├── pyproject.toml               # Project metadata
├── runtime.txt                  # Python runtime version
├── .python-version              # Python version for pyenv/uv
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## How It Works

The server uses the FastMCP library to expose the sequential thinking tool over HTTP. The tool:

1. Accepts thought inputs with metadata (thought number, total thoughts, etc.)
2. Validates the input data
3. Maintains a history of thoughts
4. Supports branching and revision of previous thoughts
5. Returns structured responses with thought status

## Development

### Running Tests

```bash
# Install dev dependencies
uv pip install pytest

# Run tests (if available)
pytest
```

### Code Structure

- **server.py**: FastAPI server setup and tool definition
- **sequential_thinking/lib.py**: Core sequential thinking logic
  - `ThoughtData`: Data class for thought representation
  - `SequentialThinkingServer`: Main server class for processing thoughts

## License

MIT License

## Credits

Based on:
- [Sequential Thinking MCP Server](https://github.com/modelcontextprotocol/servers) by Anthropic
- [MCP Servers over Streamable HTTP](https://github.com/alejandro-ao/mcp-streamable-http) by Alejandro AO

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### Server won't start
- Make sure Python 3.11+ is installed
- Check if port 10000 is available
- Verify all dependencies are installed: `pip list`
- Make sure virtual environment is activated

### Tool not appearing in AI assistant
- Restart the AI assistant after adding the configuration
- Check that the server is running
- Verify the URL is correct in the configuration
- Check server logs for any errors

### Validation Error: "Input should be a valid dictionary"
This error has been **fixed** in the latest version. The tool now properly returns dictionary objects instead of JSON strings.

**To verify the fix:**
```bash
python test_tool.py
```

**If you still see this error:**
1. Make sure you have the latest version: `git pull`
2. Restart the server
3. Clear any cached connections in your AI assistant
4. Check that `server.py` imports `json` and parses the result

### Port already in use
```bash
# Change the port
PORT=8000 python server.py
```

## Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/mersdev/fast-api-mcp/issues).

