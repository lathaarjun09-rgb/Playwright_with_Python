from playwright.sync_api import sync_playwright

def test_hidden_dropdown():
    """Demonstrate Playwright interaction with the OrangeHRM hidden dropdown."""

    with sync_playwright() as p:

        print("Launching Browser...")
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        print("Opening OrangeHRM...")
        page.set_default_timeout(60000)
        page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            wait_until="domcontentloaded",
            timeout=60000,
        )

        print("Logging in...")
        page.locator("input[name='username']").wait_for(state="visible")
        page.locator("input[name='username']").fill("Admin")
        page.locator("input[name='password']").fill("admin123")
        page.locator("button[type='submit']").click()

        print("Opening Admin Page...")
        page.get_by_role("link", name="Admin").click()

        print("Clicking dropdown...")
        page.locator(".oxd-select-text").first.click()

        print("Waiting for hidden options to appear...")
        page.locator("div[role='listbox']").wait_for(state="visible")

        print("Selecting Admin...")
        page.locator("div[role='listbox'] span").filter(has_text="Admin").click()

        print("Hidden Dropdown handled successfully.")

        page.wait_for_timeout(3000)
        
        print("Navigating to Admin Module...")
        page.get_by_role("link", name="Admin").click()
        #Opening the bootstarp dropdown
        print("Opening User Role Bootstrap Dropdown...")
        page.locator(".oxd-select-text").first.click()

        print("Selecting 'Admin' option...")
        page.locator("div[role='listbox'] span").filter(has_text="Admin").click()

        print("Bootstrap Dropdown handled successfully.")

        page.wait_for_timeout(3000)
        browser.close()

        print("Browser Closed.")