from mcp.server.fastmcp import FastMCP
from sequential_thinking.lib import SequentialThinkingServer
from typing import Dict, Any, Optional, List
import os
import json
import asyncio
import base64
from playwright.async_api import async_playwright, Browser, Page

# Get port from environment variable
PORT = int(os.environ.get("PORT", 10000))

# Create an MCP server with multiple tools
# Using host and port parameters for streamable-http transport
mcp = FastMCP("mcp-tools-server", host="0.0.0.0", port=PORT)

# Initialize the sequential thinking server
thinking_server = SequentialThinkingServer()

# Tool 1: Echo - Simple echo tool for testing
@mcp.tool(description="A simple echo tool that returns the message you send to it")
def echo(message: str) -> Dict[str, str]:
    """
    Use this tool to test the MCP server connection and basic functionality.

    Args:
        message: The message to echo back

    Returns:
        A dictionary with the echoed message, its length, and status
    """
    return {
        "echo": message,
        "length": len(message),
        "status": "success"
    }


# Tool 2: Sequential Thinking - Advanced problem-solving tool
@mcp.tool(description="A detailed tool for dynamic and reflective problem-solving through structured thoughts")
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

    # Parse the JSON string result back to a dictionary
    if result.get("isError"):
        error_data = json.loads(result["content"][0]["text"])
        return {"error": error_data.get("error", "Unknown error"), "status": "failed"}
    else:
        # Parse the JSON string to return as a dictionary
        return json.loads(result["content"][0]["text"])


# Playwright Browser Manager
class PlaywrightBrowserManager:
    """Manages a singleton Playwright browser instance for browserless automation."""

    def __init__(self):
        self.browser: Optional[Browser] = None
        self.playwright = None

    async def get_browser(self) -> Browser:
        """Get or create a headless browser instance."""
        if self.browser is None or not self.browser.is_connected():
            if self.playwright is None:
                self.playwright = await async_playwright().start()
            # Launch in headless mode for browserless operation
            self.browser = await self.playwright.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-setuid-sandbox']
            )
        return self.browser

    async def close(self):
        """Close the browser and playwright instance."""
        if self.browser:
            await self.browser.close()
            self.browser = None
        if self.playwright:
            await self.playwright.stop()
            self.playwright = None

# Initialize Playwright browser manager
browser_manager = PlaywrightBrowserManager()


# Tool 3: Navigate and Screenshot
@mcp.tool(description="Navigate to a URL and capture a screenshot (browserless headless mode)")
def playwright_screenshot(
    url: str,
    wait_for_selector: Optional[str] = None,
    wait_time: int = 1000,
    full_page: bool = False
) -> Dict[str, Any]:
    """
    Navigate to a URL and take a screenshot using Playwright in browserless headless mode.
    Perfect for visual verification, testing, and monitoring in n8n workflows.

    Args:
        url: The URL to navigate to (must include http:// or https://)
        wait_for_selector: Optional CSS selector to wait for before screenshot
        wait_time: Time to wait in milliseconds after page load (default: 1000)
        full_page: Whether to capture the full scrollable page (default: False)

    Returns:
        Dictionary with screenshot (base64), URL, and metadata
    """
    async def _screenshot():
        try:
            browser = await browser_manager.get_browser()
            context = await browser.new_context(viewport={'width': 1280, 'height': 720})
            page = await context.new_page()

            # Navigate to URL
            await page.goto(url, wait_until='networkidle')

            # Wait for specific selector if provided
            if wait_for_selector:
                await page.wait_for_selector(wait_for_selector, timeout=10000)

            # Additional wait time
            await asyncio.sleep(wait_time / 1000)

            # Take screenshot
            screenshot_bytes = await page.screenshot(full_page=full_page)
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')

            # Get page title
            title = await page.title()

            await context.close()

            return {
                "status": "success",
                "url": url,
                "title": title,
                "screenshot": screenshot_base64,
                "screenshot_size": len(screenshot_bytes),
                "full_page": full_page
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "url": url
            }

    return asyncio.run(_screenshot())


# Tool 4: Scrape Page Content
@mcp.tool(description="Extract text content from a webpage (browserless headless mode)")
def playwright_scrape_text(
    url: str,
    selector: Optional[str] = None,
    wait_time: int = 1000
) -> Dict[str, Any]:
    """
    Navigate to a URL and extract text content using Playwright in browserless headless mode.
    Useful for web scraping and content extraction in n8n workflows.

    Args:
        url: The URL to navigate to (must include http:// or https://)
        selector: Optional CSS selector to extract specific content (if None, gets all body text)
        wait_time: Time to wait in milliseconds after page load (default: 1000)

    Returns:
        Dictionary with extracted text, URL, and metadata
    """
    async def _scrape():
        try:
            browser = await browser_manager.get_browser()
            context = await browser.new_context()
            page = await context.new_page()

            # Navigate to URL
            await page.goto(url, wait_until='networkidle')
            await asyncio.sleep(wait_time / 1000)

            # Extract text content
            if selector:
                element = await page.query_selector(selector)
                if element:
                    text = await element.inner_text()
                else:
                    text = ""
                    return {
                        "status": "warning",
                        "url": url,
                        "selector": selector,
                        "text": "",
                        "message": "Selector not found"
                    }
            else:
                text = await page.inner_text('body')

            # Get page title
            title = await page.title()

            await context.close()

            return {
                "status": "success",
                "url": url,
                "title": title,
                "selector": selector if selector else "body",
                "text": text,
                "text_length": len(text)
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "url": url
            }

    return asyncio.run(_scrape())


# Tool 5: Get Page HTML
@mcp.tool(description="Extract HTML content from a webpage (browserless headless mode)")
def playwright_get_html(
    url: str,
    selector: Optional[str] = None,
    wait_time: int = 1000
) -> Dict[str, Any]:
    """
    Navigate to a URL and extract HTML content using Playwright in browserless headless mode.
    Useful for parsing structured data and analyzing page structure in n8n workflows.

    Args:
        url: The URL to navigate to (must include http:// or https://)
        selector: Optional CSS selector to extract specific HTML (if None, gets all body HTML)
        wait_time: Time to wait in milliseconds after page load (default: 1000)

    Returns:
        Dictionary with extracted HTML, URL, and metadata
    """
    async def _get_html():
        try:
            browser = await browser_manager.get_browser()
            context = await browser.new_context()
            page = await context.new_page()

            # Navigate to URL
            await page.goto(url, wait_until='networkidle')
            await asyncio.sleep(wait_time / 1000)

            # Extract HTML content
            if selector:
                element = await page.query_selector(selector)
                if element:
                    html = await element.inner_html()
                else:
                    return {
                        "status": "warning",
                        "url": url,
                        "selector": selector,
                        "html": "",
                        "message": "Selector not found"
                    }
            else:
                html = await page.content()

            # Get page title
            title = await page.title()

            await context.close()

            return {
                "status": "success",
                "url": url,
                "title": title,
                "selector": selector if selector else "full_page",
                "html": html,
                "html_length": len(html)
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "url": url
            }

    return asyncio.run(_get_html())


# Tool 6: Click Element
@mcp.tool(description="Navigate to a URL, click an element, and optionally screenshot (browserless headless mode)")
def playwright_click(
    url: str,
    selector: str,
    wait_after_click: int = 1000,
    screenshot: bool = True,
    wait_for_navigation: bool = False
) -> Dict[str, Any]:
    """
    Navigate to a URL and click an element using Playwright in browserless headless mode.
    Useful for interacting with buttons, links, and interactive elements in n8n workflows.

    Args:
        url: The URL to navigate to (must include http:// or https://)
        selector: CSS selector for the element to click
        wait_after_click: Time to wait in milliseconds after clicking (default: 1000)
        screenshot: Whether to take a screenshot after clicking (default: True)
        wait_for_navigation: Whether to wait for navigation after click (default: False)

    Returns:
        Dictionary with click result, optional screenshot, and metadata
    """
    async def _click():
        try:
            browser = await browser_manager.get_browser()
            context = await browser.new_context(viewport={'width': 1280, 'height': 720})
            page = await context.new_page()

            # Navigate to URL
            await page.goto(url, wait_until='networkidle')

            # Wait for element and click
            element = await page.wait_for_selector(selector, timeout=10000)
            if not element:
                return {
                    "status": "error",
                    "error": f"Element with selector '{selector}' not found",
                    "url": url
                }

            # Click the element
            if wait_for_navigation:
                async with page.expect_navigation():
                    await element.click()
            else:
                await element.click()

            # Wait after click
            await asyncio.sleep(wait_after_click / 1000)

            # Get current URL and title
            current_url = page.url
            title = await page.title()

            result = {
                "status": "success",
                "original_url": url,
                "current_url": current_url,
                "title": title,
                "selector": selector,
                "clicked": True
            }

            # Optional screenshot
            if screenshot:
                screenshot_bytes = await page.screenshot()
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
                result["screenshot"] = screenshot_base64
                result["screenshot_size"] = len(screenshot_bytes)

            await context.close()
            return result

        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "url": url,
                "selector": selector
            }

    return asyncio.run(_click())


# Tool 7: Fill Form
@mcp.tool(description="Fill form fields on a webpage (browserless headless mode)")
def playwright_fill_form(
    url: str,
    fields: List[Dict[str, str]],
    submit_selector: Optional[str] = None,
    wait_after_submit: int = 2000,
    screenshot: bool = True
) -> Dict[str, Any]:
    """
    Navigate to a URL and fill form fields using Playwright in browserless headless mode.
    Useful for automating form submissions in n8n workflows.

    Args:
        url: The URL to navigate to (must include http:// or https://)
        fields: List of dicts with 'selector' and 'value' keys for each form field
                Example: [{"selector": "#email", "value": "test@example.com"}]
        submit_selector: Optional CSS selector for submit button (if None, no submit)
        wait_after_submit: Time to wait in milliseconds after submit (default: 2000)
        screenshot: Whether to take a screenshot after filling (default: True)

    Returns:
        Dictionary with form fill result, optional screenshot, and metadata
    """
    async def _fill_form():
        try:
            browser = await browser_manager.get_browser()
            context = await browser.new_context(viewport={'width': 1280, 'height': 720})
            page = await context.new_page()

            # Navigate to URL
            await page.goto(url, wait_until='networkidle')

            # Fill each field
            filled_fields = []
            for field in fields:
                selector = field.get('selector')
                value = field.get('value')

                if not selector or value is None:
                    continue

                try:
                    await page.fill(selector, value)
                    filled_fields.append({"selector": selector, "filled": True})
                except Exception as e:
                    filled_fields.append({"selector": selector, "filled": False, "error": str(e)})

            # Submit if selector provided
            submitted = False
            if submit_selector:
                try:
                    await page.click(submit_selector)
                    await asyncio.sleep(wait_after_submit / 1000)
                    submitted = True
                except Exception as e:
                    return {
                        "status": "error",
                        "error": f"Submit failed: {str(e)}",
                        "filled_fields": filled_fields,
                        "url": url
                    }

            # Get current URL and title
            current_url = page.url
            title = await page.title()

            result = {
                "status": "success",
                "original_url": url,
                "current_url": current_url,
                "title": title,
                "filled_fields": filled_fields,
                "submitted": submitted
            }

            # Optional screenshot
            if screenshot:
                screenshot_bytes = await page.screenshot()
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
                result["screenshot"] = screenshot_base64
                result["screenshot_size"] = len(screenshot_bytes)

            await context.close()
            return result

        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "url": url
            }

    return asyncio.run(_fill_form())


# Tool 8: Execute JavaScript
@mcp.tool(description="Execute JavaScript on a webpage and get the result (browserless headless mode)")
def playwright_execute_js(
    url: str,
    script: str,
    wait_time: int = 1000
) -> Dict[str, Any]:
    """
    Navigate to a URL and execute JavaScript using Playwright in browserless headless mode.
    Useful for advanced DOM manipulation and data extraction in n8n workflows.

    Args:
        url: The URL to navigate to (must include http:// or https://)
        script: JavaScript code to execute (should return a JSON-serializable value)
        wait_time: Time to wait in milliseconds after page load (default: 1000)

    Returns:
        Dictionary with script execution result and metadata
    """
    async def _execute_js():
        try:
            browser = await browser_manager.get_browser()
            context = await browser.new_context()
            page = await context.new_page()

            # Navigate to URL
            await page.goto(url, wait_until='networkidle')
            await asyncio.sleep(wait_time / 1000)

            # Execute JavaScript
            result = await page.evaluate(script)

            # Get page title
            title = await page.title()

            await context.close()

            return {
                "status": "success",
                "url": url,
                "title": title,
                "result": result
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "url": url
            }

    return asyncio.run(_execute_js())


# Run the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")

