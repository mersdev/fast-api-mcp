"""
Test script for Playwright MCP tools.

This script tests the Playwright browser automation tools to ensure they work correctly
in browserless headless mode.
"""

import sys
from server import (
    playwright_screenshot,
    playwright_scrape_text,
    playwright_get_html,
    playwright_click,
    playwright_fill_form,
    playwright_execute_js
)


def test_screenshot():
    """Test the playwright_screenshot tool."""
    print("\n" + "="*60)
    print("TEST 1: Screenshot Tool")
    print("="*60)

    # Test with example.com
    result = playwright_screenshot(
        url="https://example.com",
        full_page=False
    )

    print(f"Status: {result.get('status')}")
    print(f"URL: {result.get('url')}")
    print(f"Title: {result.get('title')}")
    print(f"Screenshot size: {result.get('screenshot_size')} bytes")
    print(f"Full page: {result.get('full_page')}")

    assert result.get('status') == 'success', "Screenshot should succeed"
    assert result.get('screenshot'), "Screenshot should be present"
    assert isinstance(result.get('screenshot'), str), "Screenshot should be base64 string"

    print("✅ Screenshot test passed!")
    return True


def test_scrape_text():
    """Test the playwright_scrape_text tool."""
    print("\n" + "="*60)
    print("TEST 2: Scrape Text Tool")
    print("="*60)

    # Test with example.com
    result = playwright_scrape_text(
        url="https://example.com"
    )

    print(f"Status: {result.get('status')}")
    print(f"URL: {result.get('url')}")
    print(f"Title: {result.get('title')}")
    print(f"Text length: {result.get('text_length')} characters")
    print(f"Text preview: {result.get('text')[:100]}...")

    assert result.get('status') == 'success', "Text scraping should succeed"
    assert result.get('text'), "Text should be extracted"
    assert len(result.get('text')) > 0, "Text should not be empty"

    print("✅ Scrape text test passed!")
    return True


def test_get_html():
    """Test the playwright_get_html tool."""
    print("\n" + "="*60)
    print("TEST 3: Get HTML Tool")
    print("="*60)

    # Test with example.com
    result = playwright_get_html(
        url="https://example.com"
    )

    print(f"Status: {result.get('status')}")
    print(f"URL: {result.get('url')}")
    print(f"Title: {result.get('title')}")
    print(f"HTML length: {result.get('html_length')} characters")
    print(f"HTML preview: {result.get('html')[:100]}...")

    assert result.get('status') == 'success', "HTML extraction should succeed"
    assert result.get('html'), "HTML should be extracted"
    assert len(result.get('html')) > 0, "HTML should not be empty"
    assert '<html' in result.get('html').lower(), "HTML should contain html tag"

    print("✅ Get HTML test passed!")
    return True


def test_execute_js():
    """Test the playwright_execute_js tool."""
    print("\n" + "="*60)
    print("TEST 4: Execute JavaScript Tool")
    print("="*60)

    # Test with example.com - count all links
    result = playwright_execute_js(
        url="https://example.com",
        script="document.querySelectorAll('a').length"
    )

    print(f"Status: {result.get('status')}")
    print(f"URL: {result.get('url')}")
    print(f"Title: {result.get('title')}")
    print(f"Result: {result.get('result')}")

    assert result.get('status') == 'success', "JavaScript execution should succeed"
    assert result.get('result') is not None, "Result should be present"
    assert isinstance(result.get('result'), (int, float, str, bool, list, dict)), "Result should be JSON serializable"

    print("✅ Execute JavaScript test passed!")
    return True


def test_click():
    """Test the playwright_click tool."""
    print("\n" + "="*60)
    print("TEST 5: Click Element Tool")
    print("="*60)

    # Test with example.com - click on first link
    result = playwright_click(
        url="https://example.com",
        selector="a",
        screenshot=True,
        wait_for_navigation=True
    )

    print(f"Status: {result.get('status')}")
    print(f"Original URL: {result.get('original_url')}")
    print(f"Current URL: {result.get('current_url')}")
    print(f"Title: {result.get('title')}")
    print(f"Clicked: {result.get('clicked')}")
    print(f"Screenshot size: {result.get('screenshot_size')} bytes" if result.get('screenshot_size') else "No screenshot")

    assert result.get('status') == 'success', "Click should succeed"
    assert result.get('clicked') == True, "Element should be clicked"
    assert result.get('current_url'), "Current URL should be present"

    print("✅ Click element test passed!")
    return True


def test_fill_form():
    """Test the playwright_fill_form tool."""
    print("\n" + "="*60)
    print("TEST 6: Fill Form Tool")
    print("="*60)

    # Test with httpbin.org form endpoint (a public test API)
    result = playwright_fill_form(
        url="https://httpbin.org/forms/post",
        fields=[
            {"selector": "input[name='custname']", "value": "Test User"},
            {"selector": "input[name='custtel']", "value": "1234567890"}
        ],
        submit_selector=None,  # Don't submit for this test
        screenshot=True
    )

    print(f"Status: {result.get('status')}")
    print(f"URL: {result.get('url')}")
    print(f"Filled fields: {result.get('filled_fields')}")
    print(f"Submitted: {result.get('submitted')}")

    assert result.get('status') == 'success', "Form filling should succeed"
    assert len(result.get('filled_fields', [])) > 0, "Some fields should be filled"

    print("✅ Fill form test passed!")
    return True


def run_all_tests():
    """Run all Playwright tests."""
    print("\n" + "="*60)
    print("PLAYWRIGHT MCP TOOLS TEST SUITE")
    print("="*60)
    print("\nTesting Playwright tools in browserless headless mode...")
    print("This may take a minute as browsers are being initialized...\n")

    tests = [
        ("Screenshot", test_screenshot),
        ("Scrape Text", test_scrape_text),
        ("Get HTML", test_get_html),
        ("Execute JavaScript", test_execute_js),
        ("Click Element", test_click),
        ("Fill Form", test_fill_form),
    ]

    passed = 0
    failed = 0

    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"❌ {test_name} test failed: {str(e)}")
            failed += 1

    print("\n" + "="*60)
    print("TEST RESULTS")
    print("="*60)
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}/{len(tests)}")

    if failed == 0:
        print("\n✅ All tests passed!")
        return 0
    else:
        print(f"\n❌ {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
