from utilities.constants import BASE_URL

from Pages_reusable.check_out import checkout
from Pages_reusable.login_page import LoginPage


def test_checkout_process(page, login_data):
    """Log in with fixture data and execute the page-object checkout process."""
    login_page = LoginPage(page)
    login_page.login(login_data["email"], login_data["password"])

    page.goto(f"{BASE_URL}/checkout")

    checkout_page = checkout(page)
    checkout_page.checkout_process()