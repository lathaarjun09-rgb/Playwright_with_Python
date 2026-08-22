#Frames : The one more html application in the existing html page
from playwright.sync_api import sync_playwright,expect
from pathlib import *



def test_static_web_table():
    """Capture the frames page and read heading text from the first embedded frame."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://demoqa.com/frames")
        page.wait_for_load_state("domcontentloaded")
        
        page.screenshot(path = "Playwright_with_Python/screenshots/frame.png", full_page = True)
        print("Screenshot got captured")
        print("-------Working with the frames-----------------")
        # Pick the frame from the application
        # identify the frames with the help of frame locators
        frame = page.frame_locator("#frame1")
        text = frame.locator("h1").inner_text()
        
        print("Frame 1 text: ",text)
        
       
        
        