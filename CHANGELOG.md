# Changelog

All notable changes to this project will be documented in this file.

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
| **1.2.0** | 2025-11-11 | Echo tool, MCP standards compliance, architecture docs |
| **1.1.0** | 2025-11-11 | Fixed Pydantic validation error, added tests |
| **1.0.0** | 2025-11-11 | Initial release with virtual environment setup |

---

## Upgrade Guide

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

### Planned Features
- [ ] Additional utility tools (math, string manipulation, etc.)
- [ ] Async/await support for I/O operations
- [ ] Caching for expensive operations
- [ ] Rate limiting
- [ ] Prometheus metrics
- [ ] Health check endpoint
- [ ] API versioning
- [ ] Authentication/authorization

### Under Consideration
- [ ] Plugin system for dynamic tool loading
- [ ] Separate servers for independent tools
- [ ] WebSocket transport support
- [ ] GraphQL API
- [ ] Docker containerization
- [ ] Kubernetes deployment configs

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

# Run tests
python test_echo.py
python test_tool.py

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

**Last Updated:** 2025-11-11  
**Current Version:** 1.2.0  
**Repository:** https://github.com/mersdev/fast-api-mcp

