from mcp.server.fastmcp import FastMCP
from sequential_thinking.lib import SequentialThinkingServer
from typing import Dict, Any
import os

PORT = int(os.environ.get("PORT", 10000))

# Create an MCP server
mcp = FastMCP("sequential-thinking", host="0.0.0.0", port=PORT)

# Initialize the sequential thinking server
thinking_server = SequentialThinkingServer()

# Add the sequential thinking tool
@mcp.tool()
def sequential_thinking(
    thought: str,
    nextThoughtNeeded: bool,
    thoughtNumber: int,
    totalThoughts: int,
    isRevision: bool = False,
    revisesThought: int = None,
    branchFromThought: int = None,
    branchId: str = None,
    needsMoreThoughts: bool = False
) -> Dict[str, Any]:
    """
    A detailed tool for dynamic and reflective problem-solving through thoughts.
    This tool helps analyze problems through a flexible thinking process that can adapt and evolve.
    Each thought can build on, question, or revise previous insights as understanding deepens.
    
    When to use this tool:
    - Breaking down complex problems into steps
    - Planning and design with room for revision
    - Analysis that might need course correction
    - Problems where the full scope might not be clear initially
    - Problems that require a multi-step solution
    - Tasks that need to maintain context over multiple steps
    - Situations where irrelevant information needs to be filtered out
    
    Key features:
    - You can adjust total_thoughts up or down as you progress
    - You can question or revise previous thoughts
    - You can add more thoughts even after reaching what seemed like the end
    - You can express uncertainty and explore alternative approaches
    - Not every thought needs to build linearly - you can branch or backtrack
    - Generates a solution hypothesis
    - Verifies the hypothesis based on the Chain of Thought steps
    - Repeats the process until satisfied
    - Provides a correct answer
    
    Args:
        thought: Your current thinking step
        nextThoughtNeeded: Whether another thought step is needed
        thoughtNumber: Current thought number (numeric value, e.g., 1, 2, 3)
        totalThoughts: Estimated total thoughts needed (numeric value, e.g., 5, 10)
        isRevision: Whether this revises previous thinking
        revisesThought: Which thought is being reconsidered
        branchFromThought: Branching point thought number
        branchId: Branch identifier
        needsMoreThoughts: If more thoughts are needed
    
    Returns:
        Processing result with thought status and history information
    """
    # Prepare input data
    input_data = {
        "thought": thought,
        "nextThoughtNeeded": nextThoughtNeeded,
        "thoughtNumber": thoughtNumber,
        "totalThoughts": totalThoughts,
        "isRevision": isRevision,
        "revisesThought": revisesThought,
        "branchFromThought": branchFromThought,
        "branchId": branchId,
        "needsMoreThoughts": needsMoreThoughts
    }
    
    # Process the thought
    result = thinking_server.process_thought(input_data)
    
    # Return the text content from the result
    if result.get("isError"):
        return {"error": result["content"][0]["text"], "status": "failed"}
    else:
        return result["content"][0]["text"]


# Run the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")

