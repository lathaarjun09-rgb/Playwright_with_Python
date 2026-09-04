from playwright.sync_api import sync_playwright


def test_static_web_table():
    """Fill the start and end controls and print the selected date-range values."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)
        #Date Picker 1: Format :mm/dd/yyyy:08/13/2026
        #fill
        # date_picker1 = page.locator("#datepicker")
        # date_picker1.scroll_into_view_if_needed()
        # date_picker1.fill("08/13/2026")
        # print("Date Picker 1 is :",date_picker1.input_value())
        #JQUERY:
        # date_picker2 = page.locator("#txtDate")
        # date_picker2.click()
        # page.locator(".ui-datepicker-month").select_option(label = "Oct")
        # page.locator(".ui-datepicker-year").select_option("2025")
        # page.locator(".ui-datepicker-calendar td a", has_text="13").click()
        # print("Select the date:", date_picker2.input_value())
        # page.wait_for_timeout(1000)
        
        #Date Range Picker
        start_date = page.get_by_placeholder("Start Date")
        end_date = page.locator("#end-date")
        start_date.fill("2026-08-10")
        end_date.fill("2026-08-20")
        print("StartDate is :",start_date.input_value())
        print("EndDate is :",end_date.input_value())