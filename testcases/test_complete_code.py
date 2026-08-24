from playwright.sync_api import expect


def test_static_web_table(page, screenshot):
    """Demonstrate drag-and-drop, custom dropdown selection, and slider verification."""
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_load_state("domcontentloaded")

    print("-----------Drag the content and drop---------------")
    screenshot("01_Pagess")
    source = page.get_by_text("Drag me to my target")
    target = page.get_by_text("Drop here")
    screenshot("02_Pagess")
    source.drag_to(target)
    # expect(target).to_contain_text("Dropped")

    print("--------------- Scrolling Dropdown --------------------")
    combo_box = page.locator("#comboBox")
    combo_box.click()
    item = page.locator("#dropdown .option").filter(has_text="Item 75")
    item.scroll_into_view_if_needed()
    item.click()
    expect(combo_box).to_have_value("Item 75")

    print("---------------- Working with Slider ----------------")
    amount = page.locator("#amount")
    page.evaluate("() => $('#slider-range').slider('values', 0, 150)")
    # expect(amount).to_have_value("$300 - $300")
    screenshot("03_Pagess")
