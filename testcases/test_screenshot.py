from playwright.sync_api import sync_playwright

import datetime

def test_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Partial Screenshot
        # page.screenshot(path = f"Playwright_with_Python/screenshots/file-{timestamp}.png")
        page.screenshot(path = f"Playwright_with_Python/screenshots/file-{timestamp}.png",full_page = True)
        table = page.locator("#productTable")
        print("\n Pagination Web table\n", table)
        rows = table.locator("tbody tr")
        row_count = rows.count()
        print("\n Total no.of Rows:", row_count)
        
        heading_text=page.get_by_role("heading", name = "Automation Testing Practice")
        heading_text.screenshot(path = f"Playwright_with_Python/screenshots/heading-{timestamp}.png")
        
       