# Sequential Thinking MCP Server over FastAPI

A FastAPI-based MCP (Model Context Protocol) server that provides a sequential thinking tool for dynamic and reflective problem-solving through structured thinking processes, plus powerful browserless Playwright automation tools for web scraping and testing.

## Features

- **Sequential Thinking Tool**: Break down complex problems into manageable steps
- **Dynamic Thought Revision**: Revise and refine thoughts as understanding deepens
- **Branching Reasoning**: Branch into alternative paths of reasoning
- **Adaptive Planning**: Adjust the total number of thoughts dynamically
- **Hypothesis Generation & Verification**: Generate and verify solution hypotheses
- **Playwright Browser Automation**: Browserless web scraping, screenshots, form filling, and JavaScript execution
- **Echo Tool**: Simple echo tool for testing and debugging MCP connections
- **HTTP Transport**: Accessible over streamable HTTP using FastAPI
- **n8n Ready**: All Playwright tools are designed for seamless integration with n8n workflows

## Tools

### Tool: echo

A simple echo tool that returns the message you send to it. Useful for testing the MCP server connection and basic functionality.

**Inputs:**
- `message` (string): The message to echo back

**Returns:**
- `echo` (string): The original message
- `length` (integer): The length of the message
- `status` (string): Status of the operation (always "success")

**Example:**
```json
{
  "message": "Hello, World!"
}
```

**Response:**
```json
{
  "echo": "Hello, World!",
  "length": 13,
  "status": "success"
}
```

### Playwright Automation Tools

All Playwright tools run in **browserless headless mode**, making them perfect for server environments and n8n workflows. Screenshots are returned as base64-encoded strings for easy integration.

#### Tool: playwright_screenshot

Navigate to a URL and capture a screenshot.

**Inputs:**
- `url` (string, required): The URL to navigate to (must include http:// or https://)
- `wait_for_selector` (string, optional): CSS selector to wait for before screenshot
- `wait_time` (integer, optional): Time to wait in milliseconds after page load (default: 1000)
- `full_page` (boolean, optional): Whether to capture the full scrollable page (default: false)

**Returns:**
- `status` (string): "success" or "error"
- `url` (string): The URL that was navigated to
- `title` (string): Page title
- `screenshot` (string): Base64-encoded screenshot image
- `screenshot_size` (integer): Size of screenshot in bytes
- `full_page` (boolean): Whether full page was captured

**Example:**
```json
{
  "url": "https://example.com",
  "full_page": true
}
```

#### Tool: playwright_scrape_text

Extract text content from a webpage.

**Inputs:**
- `url` (string, required): The URL to navigate to
- `selector` (string, optional): CSS selector to extract specific content (if None, gets all body text)
- `wait_time` (integer, optional): Time to wait in milliseconds after page load (default: 1000)

**Returns:**
- `status` (string): "success", "warning", or "error"
- `url` (string): The URL that was navigated to
- `title` (string): Page title
- `selector` (string): The selector used
- `text` (string): Extracted text content
- `text_length` (integer): Length of extracted text

#### Tool: playwright_get_html

Extract HTML content from a webpage.

**Inputs:**
- `url` (string, required): The URL to navigate to
- `selector` (string, optional): CSS selector to extract specific HTML (if None, gets all page HTML)
- `wait_time` (integer, optional): Time to wait in milliseconds after page load (default: 1000)

**Returns:**
- `status` (string): "success", "warning", or "error"
- `url` (string): The URL that was navigated to
- `title` (string): Page title
- `selector` (string): The selector used
- `html` (string): Extracted HTML content
- `html_length` (integer): Length of extracted HTML

#### Tool: playwright_click

Navigate to a URL and click an element.

**Inputs:**
- `url` (string, required): The URL to navigate to
- `selector` (string, required): CSS selector for the element to click
- `wait_after_click` (integer, optional): Time to wait in milliseconds after clicking (default: 1000)
- `screenshot` (boolean, optional): Whether to take a screenshot after clicking (default: true)
- `wait_for_navigation` (boolean, optional): Whether to wait for navigation after click (default: false)

**Returns:**
- `status` (string): "success" or "error"
- `original_url` (string): The original URL navigated to
- `current_url` (string): The current URL after clicking
- `title` (string): Page title after clicking
- `selector` (string): The selector that was clicked
- `clicked` (boolean): Whether the click was successful
- `screenshot` (string, optional): Base64-encoded screenshot if requested
- `screenshot_size` (integer, optional): Size of screenshot in bytes

#### Tool: playwright_fill_form

Fill form fields on a webpage.

**Inputs:**
- `url` (string, required): The URL to navigate to
- `fields` (array, required): List of objects with 'selector' and 'value' keys
  - Example: `[{"selector": "#email", "value": "test@example.com"}, {"selector": "#password", "value": "secret"}]`
- `submit_selector` (string, optional): CSS selector for submit button (if None, no submit)
- `wait_after_submit` (integer, optional): Time to wait in milliseconds after submit (default: 2000)
- `screenshot` (boolean, optional): Whether to take a screenshot after filling (default: true)

**Returns:**
- `status` (string): "success" or "error"
- `original_url` (string): The original URL navigated to
- `current_url` (string): The current URL after form submission
- `title` (string): Page title
- `filled_fields` (array): List of objects showing which fields were filled successfully
- `submitted` (boolean): Whether form was submitted
- `screenshot` (string, optional): Base64-encoded screenshot if requested
- `screenshot_size` (integer, optional): Size of screenshot in bytes

#### Tool: playwright_execute_js

Execute JavaScript on a webpage and get the result.

**Inputs:**
- `url` (string, required): The URL to navigate to
- `script` (string, required): JavaScript code to execute (should return a JSON-serializable value)
- `wait_time` (integer, optional): Time to wait in milliseconds after page load (default: 1000)

**Returns:**
- `status` (string): "success" or "error"
- `url` (string): The URL that was navigated to
- `title` (string): Page title
- `result` (any): The result returned by the JavaScript code

**Example:**
```json
{
  "url": "https://example.com",
  "script": "document.querySelectorAll('a').length"
}
```

### Tool: sequential_thinking

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

# Install Playwright browsers (required for Playwright tools)
playwright install chromium
```

**Note:** The Playwright tools require Chromium to be installed. The setup scripts will prompt you to install it, or you can run `playwright install chromium` manually after installing the Python dependencies.

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

### Using with n8n Workflows

The Playwright tools are designed to work seamlessly with n8n. To use them:

1. **Start the MCP server** (make sure it's running on the configured port)

2. **In n8n, use the HTTP Request node** to call the MCP tools:
   - Method: POST
   - URL: `http://localhost:10000/mcp/` (or your server URL)
   - Body: JSON with the tool name and parameters

3. **Example n8n HTTP Request for screenshot:**
   ```json
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "tools/call",
     "params": {
       "name": "playwright_screenshot",
       "arguments": {
         "url": "https://example.com",
         "full_page": true
       }
     }
   }
   ```

4. **Example n8n HTTP Request for web scraping:**
   ```json
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "tools/call",
     "params": {
       "name": "playwright_scrape_text",
       "arguments": {
         "url": "https://example.com",
         "selector": ".content"
       }
     }
   }
   ```

5. **Process the response** in subsequent n8n nodes - screenshots are base64-encoded and can be saved or processed directly.

**Common n8n Use Cases:**
- Automated website monitoring and screenshots
- Web scraping for data collection
- Form automation for testing
- Content extraction from dynamic websites
- JavaScript execution for advanced data extraction

## Use Cases

### Sequential Thinking Tool
- Breaking down complex problems into steps
- Planning and design with room for revision
- Analysis that might need course correction
- Problems where the full scope might not be clear initially
- Tasks that need to maintain context over multiple steps
- Situations where irrelevant information needs to be filtered out

### Playwright Tools
- **Web Scraping**: Extract text or HTML content from dynamic websites
- **Visual Monitoring**: Capture screenshots of websites for change detection
- **Testing**: Automate UI testing and verification
- **Form Automation**: Fill and submit forms programmatically
- **Data Extraction**: Execute custom JavaScript for advanced data gathering
- **n8n Workflows**: Integrate browser automation into workflow automation
- **API Alternative**: Access web content that doesn't have an API

## Environment Variables

- `PORT`: Server port (default: 10000)
- `DISABLE_THOUGHT_LOGGING`: Set to `true` to disable thought logging to console (default: false)

## Testing

### Test the Echo Tool

To verify the echo tool works correctly:

```bash
# Windows
.venv\Scripts\activate
python test_echo.py

# Linux/Mac
source .venv/bin/activate
python test_echo.py
```

The echo test verifies:
- ✅ Simple message echo
- ✅ Empty message handling
- ✅ Long message support
- ✅ Special characters support
- ✅ Correct length calculation

### Test the Sequential Thinking Tool

To verify the sequential thinking tool works correctly:

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
├── server.py                    # Main FastAPI MCP server (with echo & sequential_thinking tools)
├── sequential_thinking/         # Sequential thinking library
│   ├── __init__.py
│   └── lib.py                   # Core logic for thought processing
├── test_echo.py                 # Test script for the echo tool
├── test_tool.py                 # Test script for the sequential thinking tool
├── setup.bat                    # Windows setup script
├── setup.sh                     # Linux/Mac setup script
├── run.bat                      # Windows run script
├── run.sh                       # Linux/Mac run script
├── requirements.txt             # Python dependencies
├── pyproject.toml               # Project metadata
├── runtime.txt                  # Python runtime version
├── .python-version              # Python version for pyenv/uv
├── .gitignore                   # Git ignore rules
├── FIX_SUMMARY.md              # Documentation of the validation error fix
└── README.md                    # This file
```

## How It Works

The server uses the FastMCP library to expose multiple MCP tools over HTTP:

### Echo Tool
A simple tool that:
1. Accepts a message string
2. Returns the message along with its length
3. Useful for testing MCP connections

### Playwright Tools
Browserless automation tools that:
1. Use a singleton Playwright browser instance for efficiency
2. Run in headless mode (no GUI required)
3. Support screenshots (base64-encoded), text/HTML extraction, clicking, form filling, and JavaScript execution
4. Return structured JSON responses perfect for n8n workflows
5. Handle errors gracefully with detailed error messages
6. Use async operations for better performance

### Sequential Thinking Tool
A complex tool that:
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

