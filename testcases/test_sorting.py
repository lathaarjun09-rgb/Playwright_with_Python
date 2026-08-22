"""Verify that the sample sorted list is ordered and the unsorted list is not."""

from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    sorted_list = page.locator("#sortedList option").all_text_contents()

    print("Sorted List:", sorted_list)

    assert sorted_list == sorted(sorted_list)

    print("Sorted list verification PASSED")


    # Select an option
    page.locator("#sortedList").select_option(label="Dog")
    unsorted_list = page.locator("#unsortedList option").all_text_contents()

    print("Unsorted List:", unsorted_list)

    assert unsorted_list != sorted(unsorted_list)

    print("Unsorted list verification PASSED")
    page.locator("#unsortedList").select_option(label="Elephant")
    page.wait_for_timeout(2000)
    browser.close()