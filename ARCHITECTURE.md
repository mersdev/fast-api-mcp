# MCP Server Architecture

This document explains the architecture of the MCP (Model Context Protocol) server implementation, following the patterns established by the Alejandro AO MCP Streamable HTTP example.

## Overview

This project implements an MCP server using FastAPI and the FastMCP library, exposing multiple tools over HTTP using the streamable HTTP transport protocol.

## Architecture Pattern

The server follows the **Single Server, Multiple Tools** pattern, which is one of two common MCP server architectures:

### Pattern 1: Single Server with Multiple Tools (Our Implementation)
```
┌─────────────────────────────────────┐
│     MCP Server (FastMCP)            │
│  Name: "mcp-tools-server"           │
│  Transport: streamable-http         │
│  Port: 10000                        │
├─────────────────────────────────────┤
│  Tool 1: echo                       │
│  Tool 2: sequential_thinking        │
└─────────────────────────────────────┘
```

**Advantages:**
- Simple deployment (single process)
- Easy to manage and configure
- All tools share the same server lifecycle
- Lower resource usage

**Use Case:** When tools are related or part of the same service

### Pattern 2: Multiple Servers Mounted in FastAPI (Alternative)
```
┌─────────────────────────────────────┐
│        FastAPI Application          │
├─────────────────────────────────────┤
│  /echo/mcp/                         │
│    └─ MCP Server 1 (Echo)           │
│  /math/mcp/                         │
│    └─ MCP Server 2 (Math)           │
│  /thinking/mcp/                     │
│    └─ MCP Server 3 (Thinking)       │
└─────────────────────────────────────┘
```

**Advantages:**
- Independent server lifecycles
- Can be developed/tested separately
- Different configuration per server
- Better separation of concerns

**Use Case:** When tools are independent services or need isolation

## Our Implementation Details

### Server Configuration

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server with multiple tools
mcp = FastMCP("mcp-tools-server", host="0.0.0.0", port=PORT)
```

**Key Parameters:**
- `name`: Server identifier (used in MCP protocol)
- `host`: Bind address (0.0.0.0 for all interfaces)
- `port`: Port number (default: 10000)

### Tool Registration

Tools are registered using the `@mcp.tool()` decorator:

```python
@mcp.tool(description="Tool description here")
def tool_name(param1: str, param2: int) -> Dict[str, Any]:
    """
    Detailed docstring explaining the tool.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    """
    # Tool implementation
    return {"result": "value"}
```

**Best Practices:**
1. Always provide a `description` parameter to `@mcp.tool()`
2. Use type hints for all parameters and return values
3. Write comprehensive docstrings
4. Return dictionary objects (not JSON strings)
5. Handle errors gracefully

### Transport Layer

The server uses **streamable HTTP transport**:

```python
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

This transport:
- Uses HTTP for communication
- Supports streaming responses
- Compatible with MCP clients (Cursor, Claude Desktop, etc.)
- Managed by FastMCP's internal session manager

### Server Lifecycle

```
1. Server Initialization
   ├─ Load environment variables
   ├─ Initialize FastMCP instance
   └─ Register tools with decorators

2. Server Startup
   ├─ Start StreamableHTTP session manager
   ├─ Bind to host:port
   └─ Start Uvicorn ASGI server

3. Request Handling
   ├─ Receive MCP request
   ├─ Route to appropriate tool
   ├─ Execute tool function
   └─ Return response

4. Server Shutdown
   ├─ Stop accepting new requests
   ├─ Complete pending requests
   └─ Clean up resources
```

## Tool Implementations

### Tool 1: Echo

**Purpose:** Simple echo tool for testing MCP connections

**Implementation:**
```python
@mcp.tool(description="A simple echo tool that returns the message you send to it")
def echo(message: str) -> Dict[str, str]:
    return {
        "echo": message,
        "length": len(message),
        "status": "success"
    }
```

**Characteristics:**
- Stateless (no shared state)
- Synchronous execution
- Simple input/output
- Useful for debugging

### Tool 2: Sequential Thinking

**Purpose:** Advanced problem-solving through structured thinking

**Implementation:**
```python
@mcp.tool(description="A detailed tool for dynamic and reflective problem-solving")
def sequential_thinking(
    thought: str,
    nextThoughtNeeded: bool,
    thoughtNumber: int,
    totalThoughts: int,
    # ... optional parameters
) -> Dict[str, Any]:
    # Complex processing logic
    result = thinking_server.process_thought(input_data)
    return json.loads(result["content"][0]["text"])
```

**Characteristics:**
- Stateful (maintains thought history)
- Complex input validation
- Supports branching and revision
- Returns structured data

## Comparison with Alejandro AO Example

### Similarities
✅ Uses FastMCP library  
✅ Streamable HTTP transport  
✅ Tool decorator pattern  
✅ Type hints and docstrings  
✅ Environment variable configuration  
✅ `mcp.run(transport="streamable-http")` pattern  

### Differences
| Aspect | Alejandro AO | Our Implementation |
|--------|--------------|-------------------|
| **Pattern** | Single tool (web_search) | Multiple tools (echo, sequential_thinking) |
| **Complexity** | Simple API call | Complex stateful processing |
| **External Deps** | Tavily API | Internal library |
| **State** | Stateless | Stateful (thinking history) |
| **Return Type** | List[Dict] | Dict[str, Any] |

## Configuration

### Environment Variables

```bash
# Server port (default: 10000)
PORT=10000

# Disable thought logging (optional)
DISABLE_THOUGHT_LOGGING=false
```

### Client Configuration

**Cursor / Claude Desktop:**
```json
{
  "mcpServers": {
    "mcp-tools": {
      "url": "http://localhost:10000/mcp/"
    }
  }
}
```

## Testing Strategy

### Unit Tests
- `test_echo.py`: Tests echo tool functionality
- `test_tool.py`: Tests sequential thinking tool

### Integration Tests
- Start server
- Connect MCP client
- Execute tools
- Verify responses

### Test Coverage
- ✅ Tool registration
- ✅ Input validation
- ✅ Output format
- ✅ Error handling
- ✅ State management (for stateful tools)

## Deployment

### Local Development
```bash
# Setup
setup.bat  # or setup.sh

# Run
run.bat    # or run.sh
```

### Production Considerations
1. **Environment Variables**: Use proper configuration management
2. **Port Configuration**: Ensure port is available and not blocked
3. **Logging**: Configure appropriate log levels
4. **Error Handling**: Implement comprehensive error handling
5. **Monitoring**: Add health checks and metrics
6. **Security**: Consider authentication/authorization if needed

## Future Enhancements

### Potential Improvements
1. **Add more tools**: Expand functionality
2. **Async support**: Use async/await for I/O operations
3. **Caching**: Add caching for expensive operations
4. **Rate limiting**: Protect against abuse
5. **Metrics**: Add Prometheus metrics
6. **Health checks**: Add `/health` endpoint
7. **API versioning**: Support multiple API versions

### Alternative Patterns to Consider
1. **Separate servers**: Split into multiple MCP servers
2. **Plugin system**: Dynamic tool loading
3. **Middleware**: Add request/response middleware
4. **Authentication**: Add API key or OAuth support

## References

- [MCP Specification](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Alejandro AO MCP Example](https://github.com/alejandro-ao/mcp-streamable-http)
- [Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers)

## Summary

This implementation follows MCP best practices by:
- ✅ Using the FastMCP library correctly
- ✅ Implementing proper tool decorators
- ✅ Following type hint conventions
- ✅ Providing comprehensive documentation
- ✅ Including test coverage
- ✅ Supporting standard MCP clients

The architecture is clean, maintainable, and follows the patterns established by the community.

