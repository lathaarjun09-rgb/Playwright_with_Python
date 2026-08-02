from playwright.sync_api import sync_playwright

def test_hidden_dropdown():

    with sync_playwright() as p:

        print("Launching Browser...")
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        print("Opening OrangeHRM...")
        page.goto(
            "https://opensource-demo.orangehrmlive.com/",
            wait_until="domcontentloaded"
        )

        print("Logging in...")
        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        page.get_by_role("button", name="Login").click()

        print("Opening Admin Page...")
        page.get_by_role("link", name="Admin").click()

        print("Clicking dropdown...")
        page.locator(".oxd-select-text").first.click()

        print("Waiting for hidden options to appear...")
        page.get_by_role("listbox").wait_for(state="visible")

        print("Selecting Admin...")
        page.get_by_role("option", name="Admin").click()

        print("Hidden Dropdown handled successfully.")

        page.wait_for_timeout(3000)
        browser.close()

        print("Browser Closed.")

        print("Opening OrangeHRM...")
        page.goto(
            "https://opensource-demo.orangehrmlive.com/",
            wait_until="domcontentloaded"
        )

        print("Logging into OrangeHRM...")
        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        page.get_by_role("button", name="Login").click()

        print("Navigating to Admin Module...")
        page.get_by_role("link", name="Admin").click()

        print("Opening User Role Bootstrap Dropdown...")
        page.locator(".oxd-select-text").first.click()

        print("Selecting 'Admin' option...")
        page.get_by_role("option", name="Admin").click()

        print("Bootstrap Dropdown handled successfully.")

        page.wait_for_timeout(3000)
        browser.close()

        print("Browser Closed.")