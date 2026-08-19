from playwright.sync_api import sync_playwright,expect
from pathlib import *


def test_static_web_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_load_state("domcontentloaded")
        
        # drag & drop
        print("-----------Drag the content and drop---------------")
        
        source = page.get_by_text("Drag me to my target")
        target = page.get_by_text("Drop here")
        
        source.drag_to(target)
        page.wait_for_timeout(2000)
        print("Drag and drop is completed to the exact location")
        
        #Slider
        #(//span[@class ='ui-slider-handle ui-corner-all ui-state-default'])[2]
        
        print("----------------Working with Slider-----------------------")
        
        slider = page.locator("#slider-range")
        
        handles = slider.locator(".ui-slider-handle")
        print("Number of handles: ", handles.count())
        
        # Handling the First one
        
        first_handle = handles.nth(0)
        
        print("Identified the first handle")
        
        print(first_handle.bounding_box())
        
        #Move the first handle
        
        first_handle.hover()
        page.mouse.down()
        
        page.mouse.move(first_handle.bounding_box()["x"]+75,first_handle.bounding_box()["y"]+20)
        
        page.wait_for_timeout(1000)
        
        print("--------------- Scrolling Dropdown--------------------")
        
        combo_box = page.locator("#comboBox")
        combo_box.click()
        
        drop_down = page.locator("#dropdown")
        
        options = drop_down.locator(".option")
                
        print("The Scrolling dropdown count is :",options.count())
        #Item 119
        
        for i in range(options.count()):
            print(i,options.nth(i).inner_text())
        page.wait_for_timeout(1000)
        item = drop_down.locator(".option").filter(has_text="Item 75") #item 119

        # Ensure the element is scrolled into view within the custom container
        item.scroll_into_view_if_needed()

        # Click the option
        item.click()
        page.wait_for_timeout(1000)
        expect(combo_box).to_have_value("Item 75")
        print(combo_box)
        print("Selected the item")
        