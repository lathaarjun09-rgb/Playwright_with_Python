import asyncio
import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        page = await browser.new_page()
        
        await page.goto("https://www.sierra.com/")
        await page.locator(".nav-link.dropdown-toggle.p-l-0 ").click()
        
# It wait for this asynchronous operations to complete before continuing to the particular task