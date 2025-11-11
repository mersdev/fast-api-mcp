"""
Sequential Thinking Library
Provides structured problem-solving through step-by-step thinking process.
"""

from typing import Optional, Dict, List, Any
from dataclasses import dataclass, asdict
import json
import os


@dataclass
class ThoughtData:
    """Represents a single thought in the sequential thinking process."""
    thought: str
    thought_number: int
    total_thoughts: int
    next_thought_needed: bool
    is_revision: Optional[bool] = None
    revises_thought: Optional[int] = None
    branch_from_thought: Optional[int] = None
    branch_id: Optional[str] = None
    needs_more_thoughts: Optional[bool] = None


class SequentialThinkingServer:
    """
    Server for processing sequential thinking steps.
    Maintains thought history and supports branching and revision.
    """
    
    def __init__(self):
        self.thought_history: List[ThoughtData] = []
        self.branches: Dict[str, List[ThoughtData]] = {}
        self.disable_thought_logging = os.environ.get("DISABLE_THOUGHT_LOGGING", "").lower() == "true"
    
    def validate_thought_data(self, data: Dict[str, Any]) -> ThoughtData:
        """
        Validate and convert input data to ThoughtData.
        
        Args:
            data: Dictionary containing thought data
            
        Returns:
            ThoughtData object
            
        Raises:
            ValueError: If validation fails
        """
        # Check required fields
        if not data.get("thought") or not isinstance(data["thought"], str):
            raise ValueError("Invalid thought: must be a non-empty string")
        
        if not data.get("thoughtNumber") or not isinstance(data["thoughtNumber"], int):
            raise ValueError("Invalid thoughtNumber: must be a number")
        
        if not data.get("totalThoughts") or not isinstance(data["totalThoughts"], int):
            raise ValueError("Invalid totalThoughts: must be a number")
        
        if "nextThoughtNeeded" not in data or not isinstance(data["nextThoughtNeeded"], bool):
            raise ValueError("Invalid nextThoughtNeeded: must be a boolean")
        
        # Create ThoughtData object
        return ThoughtData(
            thought=data["thought"],
            thought_number=data["thoughtNumber"],
            total_thoughts=data["totalThoughts"],
            next_thought_needed=data["nextThoughtNeeded"],
            is_revision=data.get("isRevision"),
            revises_thought=data.get("revisesThought"),
            branch_from_thought=data.get("branchFromThought"),
            branch_id=data.get("branchId"),
            needs_more_thoughts=data.get("needsMoreThoughts")
        )
    
    def format_thought(self, thought_data: ThoughtData) -> str:
        """
        Format a thought for display with visual indicators.
        
        Args:
            thought_data: The thought to format
            
        Returns:
            Formatted string representation
        """
        prefix = ""
        context = ""
        
        if thought_data.is_revision:
            prefix = "🔄 Revision"
            context = f" (revising thought {thought_data.revises_thought})"
        elif thought_data.branch_from_thought:
            prefix = "🌿 Branch"
            context = f" (from thought {thought_data.branch_from_thought}, ID: {thought_data.branch_id})"
        else:
            prefix = "💭 Thought"
            context = ""
        
        header = f"{prefix} {thought_data.thought_number}/{thought_data.total_thoughts}{context}"
        border_length = max(len(header), len(thought_data.thought)) + 4
        border = "─" * border_length
        
        return f"""
┌{border}┐
│ {header.ljust(border_length - 2)} │
├{border}┤
│ {thought_data.thought.ljust(border_length - 2)} │
└{border}┘"""
    
    def process_thought(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a thought step in the sequential thinking process.
        
        Args:
            input_data: Dictionary containing thought data
            
        Returns:
            Response dictionary with processing results
        """
        try:
            # Validate input
            validated_input = self.validate_thought_data(input_data)
            
            # Auto-adjust total thoughts if needed
            if validated_input.thought_number > validated_input.total_thoughts:
                validated_input.total_thoughts = validated_input.thought_number
            
            # Add to history
            self.thought_history.append(validated_input)
            
            # Track branches
            if validated_input.branch_from_thought and validated_input.branch_id:
                if validated_input.branch_id not in self.branches:
                    self.branches[validated_input.branch_id] = []
                self.branches[validated_input.branch_id].append(validated_input)
            
            # Log thought if enabled
            if not self.disable_thought_logging:
                formatted_thought = self.format_thought(validated_input)
                print(formatted_thought, flush=True)
            
            # Return success response
            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "thoughtNumber": validated_input.thought_number,
                        "totalThoughts": validated_input.total_thoughts,
                        "nextThoughtNeeded": validated_input.next_thought_needed,
                        "branches": list(self.branches.keys()),
                        "thoughtHistoryLength": len(self.thought_history)
                    }, indent=2)
                }]
            }
        
        except Exception as e:
            # Return error response
            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "error": str(e),
                        "status": "failed"
                    }, indent=2)
                }],
                "isError": True
            }

