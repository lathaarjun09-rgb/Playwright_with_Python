from playwright.sync_api import sync_playwright,expect
from pathlib import *


def test_static_web_table():
    """Demonstrate drag-and-drop, custom dropdown selection, and slider verification."""
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
        
        print("\n----- SLIDER -----")

        slider = page.locator("#slider-range")
        handles = slider.locator(".ui-slider-handle")
        print("Number of handles:", handles.count())
        first_handle = handles.nth(0)
        print("First handle identified")
        # Get handle position
        box = first_handle.bounding_box()
        print("Initial position:", box)
        # Move the slider using FOR LOOP
        for i in range(1, 6):
            print("Moving slider:", i)
            box = first_handle.bounding_box()
            page.mouse.move(box["x"] + 20,box["y"] + box["height"] / 2)
            page.wait_for_timeout(500)
        print("Slider movement completed")
        #Working with slider using loop
        print("---------------- Working with Slider -----------------------")

        slider = page.locator("#slider-range")
        handles = slider.locator(".ui-slider-handle")
        first_handle = handles.nth(0)
        print("Number of handles:", handles.count())

        for i in range(1, 6):
            print(f"\nSlider Step {i}")
            box = first_handle.bounding_box()
            print("Before X:", box["x"])
            page.mouse.move(box["x"] + box["width"] / 2,box["y"] + box["height"] / 2)
            page.mouse.down()
            page.mouse.move(box["x"] + 25,box["y"] + box["height"] / 2,steps=25)
            page.mouse.up()
            page.wait_for_timeout(1000)
            new_box = first_handle.bounding_box()
            print("After X:", new_box["x"])
        print("\nSlider movement completed")
        
        print("---------------- Working with Slider ----------------")
        slider = page.locator("#slider-range")
        # Set first handle to 150
        page.evaluate("""() => {$("#slider-range").slider("values", 0, 150);}""")
        page.wait_for_timeout(1000)
        # Read displayed value
        amount = page.locator("#amount")
        print("Displayed value:", amount.input_value())
        # Verify exact value
        expect(amount).to_have_value("₹150 - ₹300")
        print("PASS: First slider value is exactly 150")