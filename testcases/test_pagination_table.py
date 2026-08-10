from playwright.sync_api import sync_playwright


def test_static_web_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)

# Dynamic Table
# Dont depend upon the particular row numbers. 
#Find the row based on the data whatever present in the table:table data

        table = page.locator("#productTable")
        print("\n Pagination Web table\n", table)

        rows = table.locator("tbody tr")
        row_count = rows.count()
        print("\n Total no.of Rows:", row_count)

        page.locator("#pagination li")# Individual Pagination
        page.locator("#pagination li a")

        #Navigation,data in the current page, selecting the check boxes, Serch the product among the pages

        headers = table.locator("thead th")
        column_count = headers.count()
        print("\n Total no.of.columns:",column_count)

        #Current Page
        for i in range(row_count):
            row = rows.nth(i)
            cells = row.locator("td")
            for j in range(cells.count()):
                print(cells.nth(j).inner_text(),end="|")
        print()        