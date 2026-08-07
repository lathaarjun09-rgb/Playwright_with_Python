from playwright.sync_api import sync_playwright


def test_static_web_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        # page.wait_for_timeout(3000)
        # Wait until the page loads
        page.wait_for_load_state("networkidle")
        table = page.locator("//table[@name='BookTable']")
        print(table)

        #How many rows in the table

        # #Locate the all the rows
        # rows = table.locator("tbody tr")
        # print(rows)

        #table,tbody:Contentent in the table,
        #tr:Rows in the table,th:Headers in the table,td:Data in the table
        
        #Pick the data from the row
        rows = table.locator("tr").filter(has = page.locator("td"))
        print(rows)
        row_count = rows.count
        print(row_count)

        # Locate all header columns
        headers = table.locator("tr").first.locator("th")
        print(headers)
        # Get the total number of rows
        row_count = rows.count()
        print(row_count)
        #Get the total number of columns
        column_count = headers.count()
        print(column_count)
        #Print the header names
        print("\n Header Names \n")

        for i in range(column_count):
            header = headers.nth(i).inner_text()
            print(header)
            
        # Print complete table
        print("\n Complete Table\n")

        for i in range(row_count):
            column = rows.nth(i).locator("td")
            for j in range(column_count):
                print(column.nth(j).inner_text(), end = "|")
            print()