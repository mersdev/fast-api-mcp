# Changelog

All notable changes to this project will be documented in this file.

## [1.3.0] - 2025-11-20

### Added - Playwright Browser Automation Tools

#### New Features
- **Playwright Integration**: Added 6 powerful browserless automation tools
  - **playwright_screenshot**: Navigate to URL and capture screenshots
    - Supports full-page screenshots
    - Returns base64-encoded images
    - Optional selector waiting
    - Configurable wait times

  - **playwright_scrape_text**: Extract text content from webpages
    - Full page or selector-based extraction
    - Perfect for web scraping workflows
    - Returns structured text data

  - **playwright_get_html**: Extract HTML content from webpages
    - Full page or element-specific HTML
    - Useful for parsing structured data
    - Returns complete HTML structure

  - **playwright_click**: Click elements on webpages
    - CSS selector-based targeting
    - Optional navigation waiting
    - Screenshot after click capability
    - Handles dynamic page changes

  - **playwright_fill_form**: Fill and submit web forms
    - Multi-field form filling
    - Optional form submission
    - Field-by-field success tracking
    - Error handling per field

  - **playwright_execute_js**: Execute custom JavaScript on pages
    - Run arbitrary JavaScript code
    - Returns JSON-serializable results
    - Advanced data extraction
    - DOM manipulation support

#### Technical Implementation
- **PlaywrightBrowserManager**: Singleton browser management
  - Efficient browser instance reuse
  - Automatic browser lifecycle management
  - Headless mode for serverless environments
  - Chromium browser with no-sandbox args for Docker/cloud compatibility

#### n8n Integration
- All tools designed for seamless n8n workflow integration
- HTTP Request node compatible
- JSON-RPC 2.0 protocol support
- Base64 screenshots for direct processing
- Structured error responses

#### Dependencies
- Added `playwright>=1.40.0` to requirements.txt
- Chromium browser installation required (`playwright install chromium`)

#### Testing
- **test_playwright.py**: Comprehensive test suite
  - Tests screenshot capture
  - Tests text scraping
  - Tests HTML extraction
  - Tests JavaScript execution
  - Tests element clicking
  - Tests form filling
  - Verifies browserless headless operation
  - Validates base64 encoding
  - Checks error handling

#### Documentation
- **README.md**: Extensive Playwright documentation
  - Added Playwright tools to features list
  - Detailed tool documentation for each tool
  - Input/output specifications
  - n8n integration examples
  - HTTP Request node configuration
  - Common use cases and examples
  - Installation instructions for Playwright browsers
  - Troubleshooting guide

### Changed
- Updated README title to reflect browser automation capabilities
- Added n8n-ready badge to features
- Enhanced installation instructions with Playwright browser setup
- Updated "How It Works" section with Playwright details
- Expanded use cases section with web automation examples

### Technical Details
- Browserless operation (headless mode)
- Async/await for all Playwright operations
- Proper error handling and structured responses
- Base64 encoding for screenshot transport
- Singleton pattern for browser efficiency
- Compatible with Docker and serverless environments

---

## [1.2.0] - 2025-11-11

### Added - Echo Tool & MCP Standards Compliance

#### New Features
- **Echo Tool**: Added simple echo tool for testing MCP connections
  - Returns message, length, and status
  - Useful for debugging and verifying server connectivity
  - Comprehensive test suite in `test_echo.py`

#### Architecture Improvements
- **Refactored server.py** to follow Alejandro AO MCP standards
  - Renamed server from "sequential-thinking" to "mcp-tools-server"
  - Added tool descriptions to `@mcp.tool()` decorators
  - Improved code organization and comments
  - Better alignment with MCP best practices

#### Documentation
- **ARCHITECTURE.md**: Comprehensive architecture documentation
  - Explains MCP server patterns
  - Compares single-server vs multi-server approaches
  - Documents tool implementation details
  - Includes deployment and testing strategies
  - References to MCP specifications and examples

#### Testing
- **test_echo.py**: Complete test suite for echo tool
  - Tests simple messages
  - Tests empty messages
  - Tests long messages
  - Tests special characters
  - Verifies output format

#### Updated Documentation
- **README.md**: Updated with echo tool information
  - Added echo tool to features list
  - Added echo tool documentation section
  - Updated testing section with echo tests
  - Updated project structure
  - Updated "How It Works" section

### Changed
- Server name: "sequential-thinking" → "mcp-tools-server"
- Tool decorators now include descriptions
- Improved code comments and structure

### Technical Details
- Follows FastMCP library patterns
- Uses streamable HTTP transport
- Multiple tools in single server pattern
- Type hints and comprehensive docstrings
- Proper error handling

---

## [1.1.0] - 2025-11-11

### Fixed - Pydantic Validation Error

#### Bug Fix
- **Fixed Pydantic validation error** in sequential_thinking tool
  - Issue: Tool was returning JSON string instead of dictionary
  - Solution: Parse JSON string to dictionary before returning
  - Added `import json` to server.py
  - Modified return statement to use `json.loads()`

#### Testing
- **test_tool.py**: Added comprehensive test suite
  - Tests thought sequencing
  - Tests revisions
  - Tests branching
  - Verifies dictionary output
  - Confirms no Pydantic errors

#### Documentation
- **FIX_SUMMARY.md**: Detailed fix documentation
  - Root cause analysis
  - Solution explanation
  - Verification steps
  - Technical details
  - Alternative approaches considered

- **README.md**: Updated with testing and troubleshooting
  - Added Testing section
  - Added Troubleshooting section
  - Documented the validation error fix
  - Added solutions for common issues

### Technical Details
- Error: `Input should be a valid dictionary [type=dict_type, input_value='...', input_type=str]`
- Root Cause: `sequential_thinking/lib.py` returns JSON string in MCP format
- Solution: Parse JSON string in `server.py` before returning to MCP framework

---

## [1.0.0] - 2025-11-11

### Initial Release - Virtual Environment Setup

#### Features
- **Sequential Thinking MCP Server**: FastAPI-based MCP server
  - Dynamic thought adjustment
  - Branching reasoning paths
  - Thought revision capability
  - Complete history tracking
  - HTTP-based access via streamable HTTP

#### Setup Scripts
- **setup.bat**: Windows automated setup
  - Creates virtual environment
  - Upgrades pip
  - Installs all dependencies
  
- **setup.sh**: Linux/Mac automated setup
  - Same functionality as setup.bat
  - Bash-based implementation

#### Run Scripts
- **run.bat**: Windows run script
  - Activates virtual environment
  - Starts the server
  
- **run.sh**: Linux/Mac run script
  - Same functionality as run.bat

#### Core Files
- **server.py**: Main FastAPI MCP server
- **sequential_thinking/lib.py**: Core thinking logic
- **requirements.txt**: Python dependencies
- **pyproject.toml**: Project metadata
- **runtime.txt**: Python runtime version
- **.python-version**: Python version for pyenv/uv
- **.gitignore**: Git ignore rules

#### Documentation
- **README.md**: Comprehensive project documentation
- **QUICKSTART.md**: Quick start guide
- **SETUP_SUMMARY.md**: Setup and usage summary

#### Dependencies
- fastapi >= 0.115.12
- mcp[cli] >= 1.9.3
- python-dotenv >= 1.1.0
- uvicorn >= 0.38.0

---

## Version History Summary

| Version | Date | Key Changes |
|---------|------|-------------|
| **1.3.0** | 2025-11-20 | Playwright browser automation, 6 new tools, n8n integration |
| **1.2.0** | 2025-11-11 | Echo tool, MCP standards compliance, architecture docs |
| **1.1.0** | 2025-11-11 | Fixed Pydantic validation error, added tests |
| **1.0.0** | 2025-11-11 | Initial release with virtual environment setup |

---

## Upgrade Guide

### From 1.2.0 to 1.3.0

Pull the latest code and install Playwright:

```bash
git pull

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install new dependencies
pip install -r requirements.txt

# Install Playwright Chromium browser
playwright install chromium

# Restart the server
# Windows:
run.bat
# Linux/Mac:
./run.sh
```

**New Features Available:**
- 6 Playwright browser automation tools
- Screenshot capture: `playwright_screenshot(url, ...)`
- Text scraping: `playwright_scrape_text(url, ...)`
- HTML extraction: `playwright_get_html(url, ...)`
- Element clicking: `playwright_click(url, selector, ...)`
- Form filling: `playwright_fill_form(url, fields, ...)`
- JavaScript execution: `playwright_execute_js(url, script, ...)`
- n8n workflow integration support
- Browserless headless operation

**Important:** You must install Playwright browsers with `playwright install chromium` for the new tools to work.

### From 1.1.0 to 1.2.0

No breaking changes. Simply pull the latest code:

```bash
git pull
```

The server now includes an additional echo tool. No configuration changes needed.

**New Features Available:**
- Echo tool for testing: `echo(message: str)`
- Improved server naming and organization
- Comprehensive architecture documentation

### From 1.0.0 to 1.1.0

No breaking changes. Pull the latest code and restart the server:

```bash
git pull
# Windows
run.bat
# Linux/Mac
./run.sh
```

**Bug Fixes:**
- Pydantic validation error is now fixed
- Tool returns proper dictionary objects

---

## Future Roadmap

### Completed
- [x] Browser automation tools (Playwright) - v1.3.0
- [x] n8n workflow integration - v1.3.0

### Planned Features
- [ ] Additional utility tools (math, string manipulation, etc.)
- [ ] Caching for expensive operations
- [ ] Rate limiting
- [ ] Prometheus metrics
- [ ] Health check endpoint
- [ ] API versioning
- [ ] Authentication/authorization
- [ ] PDF generation from screenshots
- [ ] Advanced web scraping patterns (pagination, infinite scroll)

### Under Consideration
- [ ] Plugin system for dynamic tool loading
- [ ] Separate servers for independent tools
- [ ] WebSocket transport support
- [ ] GraphQL API
- [ ] Docker containerization
- [ ] Kubernetes deployment configs
- [ ] Playwright Firefox/WebKit browser support
- [ ] Browser session persistence

---

## Contributing

Contributions are welcome! Please see the main README.md for contribution guidelines.

### Development Setup
```bash
# Clone the repository
git clone https://github.com/mersdev/fast-api-mcp.git
cd fast-api-mcp

# Setup virtual environment
setup.bat  # or setup.sh

# Install Playwright browsers
playwright install chromium

# Run tests
python test_echo.py
python test_tool.py
python test_playwright.py

# Start server
run.bat  # or run.sh
```

---

## Credits

Based on:
- [Sequential Thinking MCP Server](https://github.com/modelcontextprotocol/servers) by Anthropic
- [MCP Servers over Streamable HTTP](https://github.com/alejandro-ao/mcp-streamable-http) by Alejandro AO

## License

MIT License - See LICENSE file for details

---

**Last Updated:** 2025-11-20
**Current Version:** 1.3.0
**Repository:** https://github.com/mersdev/fast-api-mcp

