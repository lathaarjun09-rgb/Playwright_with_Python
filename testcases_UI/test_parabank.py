import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("Testrim3456789")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("Test@123")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("heading", name="Customer Login")).to_be_visible()
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("button")).to_contain_text("Log In")
    
    
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
