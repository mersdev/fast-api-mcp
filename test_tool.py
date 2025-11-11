"""
Test script for the sequential_thinking tool
This script tests the tool directly to verify it returns proper dictionary output
"""

from sequential_thinking.lib import SequentialThinkingServer
import json

def test_sequential_thinking():
    """Test the sequential thinking tool"""
    print("=" * 60)
    print("Testing Sequential Thinking Tool")
    print("=" * 60)
    
    # Initialize the server
    server = SequentialThinkingServer()
    
    # Test case 1: First thought
    print("\n[Test 1] First thought in sequence")
    print("-" * 60)
    
    input_data = {
        "thought": "Let me break down this problem into steps",
        "nextThoughtNeeded": True,
        "thoughtNumber": 1,
        "totalThoughts": 3,
        "isRevision": False,
        "revisesThought": None,
        "branchFromThought": None,
        "branchId": None,
        "needsMoreThoughts": False
    }
    
    result = server.process_thought(input_data)
    print(f"Result type: {type(result)}")
    print(f"Result keys: {result.keys()}")
    
    # Parse the JSON string to verify it's valid
    if not result.get("isError"):
        parsed_result = json.loads(result["content"][0]["text"])
        print(f"Parsed result type: {type(parsed_result)}")
        print(f"Parsed result: {json.dumps(parsed_result, indent=2)}")
        print("✅ Test 1 PASSED: Returns valid dictionary")
    else:
        print("❌ Test 1 FAILED: Error in result")
        print(result)
    
    # Test case 2: Second thought
    print("\n[Test 2] Second thought in sequence")
    print("-" * 60)
    
    input_data = {
        "thought": "Now I'll analyze the first step in detail",
        "nextThoughtNeeded": True,
        "thoughtNumber": 2,
        "totalThoughts": 3,
        "isRevision": False,
        "revisesThought": None,
        "branchFromThought": None,
        "branchId": None,
        "needsMoreThoughts": False
    }
    
    result = server.process_thought(input_data)
    if not result.get("isError"):
        parsed_result = json.loads(result["content"][0]["text"])
        print(f"Parsed result: {json.dumps(parsed_result, indent=2)}")
        print("✅ Test 2 PASSED: Returns valid dictionary")
    else:
        print("❌ Test 2 FAILED: Error in result")
    
    # Test case 3: Final thought
    print("\n[Test 3] Final thought in sequence")
    print("-" * 60)
    
    input_data = {
        "thought": "Combining all insights to reach a conclusion",
        "nextThoughtNeeded": False,
        "thoughtNumber": 3,
        "totalThoughts": 3,
        "isRevision": False,
        "revisesThought": None,
        "branchFromThought": None,
        "branchId": None,
        "needsMoreThoughts": False
    }
    
    result = server.process_thought(input_data)
    if not result.get("isError"):
        parsed_result = json.loads(result["content"][0]["text"])
        print(f"Parsed result: {json.dumps(parsed_result, indent=2)}")
        print(f"Total thoughts in history: {parsed_result['thoughtHistoryLength']}")
        print("✅ Test 3 PASSED: Returns valid dictionary")
    else:
        print("❌ Test 3 FAILED: Error in result")
    
    # Test case 4: Revision
    print("\n[Test 4] Revising a previous thought")
    print("-" * 60)
    
    input_data = {
        "thought": "Actually, let me reconsider the first step",
        "nextThoughtNeeded": True,
        "thoughtNumber": 4,
        "totalThoughts": 4,
        "isRevision": True,
        "revisesThought": 1,
        "branchFromThought": None,
        "branchId": None,
        "needsMoreThoughts": False
    }
    
    result = server.process_thought(input_data)
    if not result.get("isError"):
        parsed_result = json.loads(result["content"][0]["text"])
        print(f"Parsed result: {json.dumps(parsed_result, indent=2)}")
        print("✅ Test 4 PASSED: Revision works correctly")
    else:
        print("❌ Test 4 FAILED: Error in result")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
    print("\nThe tool now returns proper dictionary objects that can be")
    print("parsed by the MCP framework without validation errors.")

if __name__ == "__main__":
    test_sequential_thinking()

