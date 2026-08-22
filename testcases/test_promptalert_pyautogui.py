# Handling prompt alert by using pyautogui 

from playwright.sync_api import sync_playwright,expect
from pathlib import *
import pyautogui
import time


def test_static_web_table():
    """Handle the prompt-alert demonstration and verify the resulting page interaction."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_load_state("domcontentloaded")
        
        page.locator("#promptBtn").click()
        time.sleep(4)
        #Select the text in the prompt alert
        pyautogui.hotkey("ctrl", "a")
        # pyautogui.typewrite("Welcome to the Class")
        pyautogui.write("Welcome",interval = 0.1)
        time.sleep(2)
        pyautogui.press("enter")
        page.wait_for_timeout(2000)
        
        # Handling Prompt Alert: Prompt Alert
        print("---------------Prompt Alert------------------")
        
        def promt_alert(dialog):
            print("Prompt Message",dialog.message)
            page.wait_for_timeout(1000)
            
            dialog.accept("Welcome to the Class")
            page.wait_for_timeout(1000)
            
        page.once("dialog",promt_alert)
        # page.get_by_role("button", name = "Prompt Alert").click()
        page.wait_for_selector("#promptBtn",timeout=30000).click()
                
        page.wait_for_timeout(1000)
        