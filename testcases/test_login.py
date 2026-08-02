from Pages_reusable.login_page import LoginPage
from Pages_reusable.home_page import homepage


def test_login(page, login_data):
    login = LoginPage(page)
    home = homepage(page)

    login.open_login_page()
    login.login(login_data["email"], login_data["password"])
    print("Successfully login to the application")

    # home.add_product()
    # print("Successfully added the products")
    home.click_shopping_cart()
    print("successfully clicked on the Shoppingcart")
    home.checkout_process()
    



    # Create test case and add the shopping functionality to that new test file

    



    # assert login.verify_login(), "Login did not succeed with saved credentials"



# def test_login_invalid_credentials(page):
#     login = LoginPage(page)

#     login.open_login_page()
#     login.login("invalid_user@test.com", "WrongPass@123")
#     page.wait_for_timeout(3000)

#     error_message = login.get_error_message()
#     print("Login error message:", error_message)
#     assert "No customer account found" in error_message, "Expected invalid login error message"
