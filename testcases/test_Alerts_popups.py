from playwright.sync_api import sync_playwright,expect
from pathlib import *


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
        
        