from playwright.sync_api import sync_playwright


def test_static_web_table():
    """Read a dynamic table and demonstrate locating rows, cells, and calculated values."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)

# Dynamic Table
# Dont depend upon the particular row numbers. 
#Find the row based on the data whatever present in the table:table data

        table = page.locator("#taskTable")
        print("\n Dynamic Web table\n", table)

        # Locate the rows
        rows = table.locator("tbody tr")
        row_count = rows.count()
        print("\n Total no.of Rows:", row_count)

        headers = table.locator("thead th")
        column_count = headers.count()
        print("\n Total no.of.columns:",column_count)

        
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

        #CPU load of Chrome process: 1.6%    
        chrome_row = rows.filter(has_text="chrome")
        chrome_count = chrome_row.count()
        print(chrome_count)

        # Pick Chrome from the dynamic table and check the value

        chrome_row = rows.filter(has_text="Chrome").first
        assert chrome_row.count()>0

        print("We found the Chrome")

        cpu_column_index = -1

        for i in range(column_count):
            header_name = (headers.nth(i).inner_text().strip())
            if header_name == "CPU(%)":
                cpu_column_index = i
                break
            print(header_name)    

        assert cpu_column_index == -1 # verifying the cpu is found or not

        chrome_cell = chrome_row.locator("td")
        chrome_cpu = (chrome_cell.nth(cpu_column_index).inner_text())

        print(chrome_cpu)

# Assignment:Memory Size of Firefox process: 59.0 MB

#Network speed of Chrome process: 6.0 Mbps

#Disk space of Firefox process: 0.30 MB/s        

        
        firefox_row = rows.filter(has_text="Firefox").first

        # Verify Firefox row exists
        assert firefox_row.count() > 0

        print("Firefox Row Found")

        #Find Memory column
        
        memory_column_index = -1

        for i in range(column_count):

           
            header_name = (headers.nth(i).inner_text().strip())

            
            if header_name == "Memory (MB)":

                memory_column_index = i
                break

        assert memory_column_index != -1
        # Get Firefox Memory
        firefox_cells = firefox_row.locator("td")

       
        firefox_memory = (firefox_cells.nth(memory_column_index).inner_text())

        print("Firefox Memory :",firefox_memory)

        # GET NETWORK OF CHROME
        print("NETWORK OF CHROME")
        # Chrome row already identified
        print("Chrome Row Found")
        #Find Network column
        network_column_index = -1

        for i in range(column_count):
            header_name = (headers.nth(i).inner_text().strip())

            # Check Network header
            if header_name == "Network (Mbps)":

                network_column_index = i

                break
        assert network_column_index != -1

        # Get Chrome Network
        chrome_cells = chrome_row.locator("td")

       
        chrome_network = (chrome_cells.nth(network_column_index).inner_text())

        print("Chrome Network :",chrome_network)
        # GET DISK OF FIREFOX
        # ======================================================

        # Firefox row already identified
        # ------------------------------------------------------

        print("Firefox Row Found")
        # Find Disk column

        disk_column_index = -1

        # Loop through headers
        for i in range(column_count):

            # Read header text
            header_name = (headers.nth(i).inner_text().strip())
           
            if header_name == "Disk (MB/s)":

                disk_column_index = i

                break

        assert disk_column_index != -1
       

        firefox_cells = firefox_row.locator("td")

        firefox_disk = (firefox_cells.nth(disk_column_index).inner_text())

        print("Firefox Disk :", firefox_disk)

        
        print("1. Chrome CPU :",chrome_cpu)

        print("2. Firefox Memory  :",firefox_memory)

        print("3. Chrome Network  :",chrome_network)

        print("4. Firefox Disk    :",firefox_disk)
        