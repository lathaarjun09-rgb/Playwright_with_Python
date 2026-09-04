from playwright.sync_api import sync_playwright

def test_hidden_dropdown():
    """Demonstrate selecting an option from the OrangeHRM Bootstrap dropdown."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.locator("input[name='username']").fill("Admin")
        page.locator("input[name='password']").fill("admin123")
        page.locator("button[type='submit']").click()

        page.locator("//span[text()='Admin']").click()

        # Click dropdown (options become visible)
        page.locator(".oxd-select-text").first.click()

        # Wait for the hidden listbox to appear
        page.locator("div[role='listbox']").wait_for(state="visible")

        # Click option
        page.locator("div[role='listbox'] span").filter(has_text="Admin").click()

        page.wait_for_timeout(3000)
        browser.close()