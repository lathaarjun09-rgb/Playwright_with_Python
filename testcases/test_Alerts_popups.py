from playwright.sync_api import sync_playwright,expect
from pathlib import *
import pyautogui


def test_static_web_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_load_state("domcontentloaded")
        
        print("---------------Simple Alert------------------")
        #dailog
        
        page.once("dialog", lambda dialog:(print("Alert Message:",dialog.message),dialog.accept()))
        page.get_by_role("button", name = "Simple Alert").click()
        
        # Confirmation Alert
        print("---------------Confirmation Alert------------------")
        page.once("dialog", lambda dialog:(print("Alert Message:",dialog.message),dialog.accept()))
        page.get_by_role("button", name = "Confirmation Alert").click()
        
        # Creating the function and handling the confirmation message
        print("---------------Confirmation Alert------------------")
        def confirm_alert(dialog):
            print("Confirm Message",dialog.message)
            dialog.accept()
            
        page.once("dialog",confirm_alert)
        page.get_by_role("button", name = "Confirmation Alert").click()
        # dismiss the alert
        def confirm_alert(dialog):
            print("Confirm Message",dialog.message)
            dialog.dismiss()
            
        page.once("dialog",confirm_alert)
        page.get_by_role("button", name = "Confirmation Alert").click()
        
        page.wait_for_timeout(1000)
        
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
        
        # New Tab: <button onclick="myFunction()">New Tab</button>
        print("----------------New Tab----------------")
        #Expecting new tab. We are capturing that in page.expect_popup() and storing it in new_tab variable. Then we are performing the actions on that new tab.
        with page.expect_popup() as popup_info:
            page.get_by_role("button", name = "New Tab").click()
        #get the newly opened tab    
        new_tab = popup_info.value
        new_tab.wait_for_load_state()
        #Printing the new tab URL
        print("New tab Url", new_tab.url)
        
        new_tab.wait_for_timeout(1000)
        #Selecting the element in the new tab
        new_tab.locator("//a[text()='TypeScript For Playwright & Cypress']").click()
        new_tab.wait_for_timeout(3000)
        print(new_tab)        
        new_tab.close() 
        
        #Popup Window
        print("---------------Popup window----------------")
        with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Popup Windows").click()
        popup = popup_info.value
        popup.wait_for_load_state()
        print("Popup URL:", popup.url)
        popup.close()
        
       
        
        
        
        