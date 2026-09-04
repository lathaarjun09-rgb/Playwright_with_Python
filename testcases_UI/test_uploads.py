from playwright.sync_api import sync_playwright
from pathlib import *


def test_static_web_table():
    """Upload a file through the sample control and inspect the upload result."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)
        
        #Get the project root folder
        
        # project_path = Path(__file__).resolve().parents[1]
        
        # file_path = project_path/"data"/"test_input1.txt"
        # file_2 = project_path/"data"/"test_input2.txt"
        # file_3 = project_path/"data"/"test_input3.txt"
                
        
        # file_upload = page.locator('input[type = "file"]').nth(0)
        
        # file_upload.set_input_files(str(file_path))
        
        # print(file_path.name)
        
        # page.get_by_role("button", name = "Upload Single File").click()
        # page.wait_for_timeout(1000)
        
        # print("File uploaded successfully")
        
        # #uploading multiple files
        
        # file_uploads = page.locator('input[type = "file"]').nth(1)
        
        # file_uploads.set_input_files([str(file_2),str(file_3)])
        
        # print(file_2.name)
        # print(file_3.name)
        
        # page.get_by_role("button", name = "Upload Multiple Files").click()
        # page.wait_for_timeout(1000)
        
        # print("Multiple files uploaded successfully")
        
        project_path = Path(__file__).resolve().parents[1]
        data_folder = project_path/"data"        
        files = list(data_folder.iterdir())#iterate the contents of this directory ["text","test"]
        
        for file in files:
            print(file.name)
            
        file_uploads = page.locator('input[type = "file"]').nth(1)   
        file_uploads.set_input_files([str(file) for file in files if file.is_file()])
        
        print("All files selected")
        page.get_by_role("button", name = "Upload Multiple Files").click()
        page.wait_for_timeout(1000) 
                
        browser.close()
        
        
        
        
        