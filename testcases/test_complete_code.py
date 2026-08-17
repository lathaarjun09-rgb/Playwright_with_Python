from playwright.sync_api import sync_playwright
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