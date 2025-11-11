"""
Test script for the echo tool
This script tests the echo tool directly to verify it works correctly
"""

def test_echo_tool():
    """Test the echo tool by importing and calling it directly"""
    print("=" * 60)
    print("Testing Echo Tool")
    print("=" * 60)
    
    # Import the server module to get access to the tools
    import server
    
    # Test case 1: Simple message
    print("\n[Test 1] Simple echo message")
    print("-" * 60)
    
    result = server.echo("Hello, World!")
    print(f"Input: 'Hello, World!'")
    print(f"Result: {result}")
    print(f"Echo: {result['echo']}")
    print(f"Length: {result['length']}")
    print(f"Status: {result['status']}")
    
    assert result['echo'] == "Hello, World!", "Echo message doesn't match"
    assert result['length'] == 13, "Length is incorrect"
    assert result['status'] == "success", "Status is not success"
    print("✅ Test 1 PASSED")
    
    # Test case 2: Empty message
    print("\n[Test 2] Empty message")
    print("-" * 60)
    
    result = server.echo("")
    print(f"Input: ''")
    print(f"Result: {result}")
    
    assert result['echo'] == "", "Echo should be empty"
    assert result['length'] == 0, "Length should be 0"
    assert result['status'] == "success", "Status is not success"
    print("✅ Test 2 PASSED")
    
    # Test case 3: Long message
    print("\n[Test 3] Long message")
    print("-" * 60)
    
    long_message = "This is a longer message to test the echo functionality with more content."
    result = server.echo(long_message)
    print(f"Input: '{long_message}'")
    print(f"Result: {result}")
    print(f"Length: {result['length']}")
    
    assert result['echo'] == long_message, "Echo message doesn't match"
    assert result['length'] == len(long_message), "Length is incorrect"
    assert result['status'] == "success", "Status is not success"
    print("✅ Test 3 PASSED")
    
    # Test case 4: Special characters
    print("\n[Test 4] Special characters")
    print("-" * 60)
    
    special_message = "Hello! @#$%^&*() 123 🎉"
    result = server.echo(special_message)
    print(f"Input: '{special_message}'")
    print(f"Result: {result}")
    
    assert result['echo'] == special_message, "Echo message doesn't match"
    assert result['length'] == len(special_message), "Length is incorrect"
    assert result['status'] == "success", "Status is not success"
    print("✅ Test 4 PASSED")
    
    print("\n" + "=" * 60)
    print("All echo tests completed successfully!")
    print("=" * 60)
    print("\nThe echo tool is working correctly and returns:")
    print("  - echo: The original message")
    print("  - length: The length of the message")
    print("  - status: 'success'")

if __name__ == "__main__":
    test_echo_tool()

