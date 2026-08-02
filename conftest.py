import pytest

from playwright.sync_api import sync_playwright
from utilities.constants import BASE_URL
from utilities.data_reader import load_json


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(BASE_URL)
        yield page
        browser.close()


@pytest.fixture
def register_data():
    return load_json("data/register.json")


@pytest.fixture
def login_data():
    return load_json("data/login.json")
