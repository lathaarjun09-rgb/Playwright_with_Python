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

        #Product names
        for i in range(row_count): # 1,2,3,4,5
            product = rows.nth(i).locator("td").nth(1).inner_text()
            print(product)

        search_product = "Smartwatch"
        print(f"\n Search for the item:",{search_product})
        found = False 

        search_products = "	Tablet"
        print(f"\n Search for the item:",{search_products})
        found = False 

        for i in range(row_count):
            product = (rows.nth(i).locator("td").nth(1).inner_text())

            if product == search_product:
                print("product found")

                found = True
                break
            elif product == search_products:
                print(product)


        if not found:
            print("Product not found")

    # pick the 2 items
        smart_row = rows.filter(has_text = "Smartphone").first
        if smart_row.count()>0:
            smart_row.locator("td").nth(1).inner_text()
            check_box = smart_row.locator("td").nth(3).locator("input")
            check_box.click()
            page.wait_for_timeout(1000)
            print("Successfully selected")
        else :
            print("Item not found")

        laptop_row = rows.filter(has_text = "Laptop").first
        if laptop_row.count()>0:
                laptop_row.locator("td").nth(1).inner_text()
                check_box = laptop_row.locator("td").nth(3).locator("input")
                check_box.click()
                page.wait_for_timeout(1000)
                print("Successfully selected")
        else:
            print("Laptop not found")        


        smart_row = rows.filter(has_text = "Smartphone").first
        laptop_row = rows.filter(has_text = "Laptop").first
        if smart_row.count()>0:
                 smart_row.locator("td").nth(1).inner_text()
                 check_box = smart_row.locator("td").nth(3).locator("input")
                 check_box.click()
                 page.wait_for_timeout(1000)
                 print("Successfully selected")

        elif laptop_row.count()>0:
                     laptop_row.locator("td").nth(1).inner_text()
                     check_box = laptop_row.locator("td").nth(3).locator("input")
                     check_box.click()
                     page.wait_for_timeout(1000)
                     print("Successfully selected")
        else:
                 print("Laptop not found")   
        
        pagination_no = page.locator("#pagination")
        pagination_c = pagination_no.locator("li a")
        page_count = pagination_c.count()
        print(page_count)

        for i in range(page_count):
              print(pagination_c.nth(i).inner_text())
        pagination_c.nth(1).click()
        page.wait_for_timeout(1000)  
        

        pagination_no = page.locator("#pagination")
        pagination_c = pagination_no.locator("li a")
        total_pages = pagination_c.count()
        print(total_pages)

        for page_no in range(total_pages):
              pagination_c = pagination_no.locator("li a")
              pagination_c.nth(page_no).click()
              page.wait_for_timeout(1000)
            
        