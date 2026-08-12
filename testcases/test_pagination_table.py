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
    # Newly added code
    pagination_links = pagination.locator("li a")
        page_count = pagination_links.count()
        print("Total Pagination Links :", page_count)

        print("\nPagination Numbers")
        for i in range(page_count):
            print(pagination_links.nth(i).inner_text())

        print("\nOpening Page 2")
        pagination_links.nth(1).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")
        print("Rows on Page 2 :", rows.count())

        print("\nPage 2 Data")
        for i in range(rows.count()):
            print(rows.nth(i).inner_text())

        search_product = "Laptop"
        print(f"\nSearching {search_product} Across Pages")
        found = False

        pagination_links = pagination.locator("li a")
        pagination_links.nth(0).click()
        page.wait_for_timeout(500)

        pagination_links = pagination.locator("li a")
        total_pages = pagination_links.count()
        print("Total Pages :", total_pages)

        for page_number in range(total_pages):
            pagination_links = pagination.locator("li a")
            pagination_links.nth(page_number).click()
            page.wait_for_timeout(300)

            rows = table.locator("tbody tr")

            for i in range(rows.count()):
                product = rows.nth(i).locator("td").nth(1).inner_text()

                if product == search_product:
                    print(f"{search_product} Found on Page {page_number + 1}")
                    found = True
                    break

            if found:
                break

        assert found, f"{search_product} was not found in any page"
        print("\nProduct Search Successful")

        print("\nSelecting Laptop Checkbox")

        rows = table.locator("tbody tr")

        for i in range(rows.count()):
            row = rows.nth(i)
            product = row.locator("td").nth(1).inner_text()

            if product == "Laptop":
                checkbox = row.locator("td").nth(3).locator("input")
                checkbox.check()
                print("Laptop Checkbox Selected")
                break   
        print("\nOpening Page 2")
        pagination_links = pagination.locator("li a")
        pagination_links.nth(1).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")
        print("Rows on Page 2 :", rows.count())

        print("\nPage 2 Data")
        for i in range(rows.count()):
            print(rows.nth(i).inner_text())

        print("\nOpening Page 3")
        pagination_links = pagination.locator("li a")
        pagination_links.nth(2).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")
        print("Rows on Page 3 :", rows.count())

        print("\nPage 3 Data")
        for i in range(rows.count()):
            print(rows.nth(i).inner_text())

        print("\nOpening Page 4")
        pagination_links = pagination.locator("li a")
        pagination_links.nth(3).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")
        print("Rows on Page 4 :", rows.count())

        print("\nPage 4 Data")
        for i in range(rows.count()):
            print(rows.nth(i).inner_text())

        print("\nSelecting First Product from Page 3")

        pagination.locator("li a").nth(2).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")

        row = rows.first
        product = row.locator("td").nth(1).inner_text()

        print("Page 3 Product :", product)

        row.locator("td").nth(3).locator("input").check()

        print(product, "Selected from Page 3")    

        print("\nSelecting First Product from Page 4")

        pagination.locator("li a").nth(3).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")

        row = rows.first
        product = row.locator("td").nth(1).inner_text()

        print("Page 4 Product :", product)

        row.locator("td").nth(3).locator("input").check()

        print(product, "Selected from Page 4")

        pagination.locator("li a").nth(2).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")

        product_name = "Tablet"

        row = rows.filter(has_text=product_name).first

        if row.count() > 0:
            row.locator("td").nth(3).locator("input").check()
            print(product_name, "Selected from Page 3")
        else:
            print(product_name, "Not Found on Page 3")

        pagination.locator("li a").nth(3).click()
        page.wait_for_timeout(500)

        rows = table.locator("tbody tr")

        product_name = "Smartphone"

        row = rows.filter(has_text=product_name).first

        if row.count() > 0:
            row.locator("td").nth(3).locator("input").check()
            print(product_name, "Selected from Page 4")
        else:
            print(product_name, "Not Found on Page 4")         
        