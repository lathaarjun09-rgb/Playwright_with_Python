from Pages.register_palywrightlocators import RegisterPlaywrightPage
from utilities.data_writer import write_json


def test_register(page, register_data):
    """Submit registration fixture data and verify that registration completes successfully."""
    register = RegisterPlaywrightPage(page)  # Creating the Object to use the page functions

    register.open_register()  # It will click on the register link
    print("Successfully clicked on the Register link")

    register.new_user(
        register_data["firstname"],
        register_data["lastname"],
        register_data["email"],
        register_data["password"]
    )

    actual_msg = register.verify_success_msg()
    assert actual_msg == "Your registration completed"
    print("Actual message is: ", actual_msg)

    login_data = {
        "email": register_data["email"],
        "password": register_data["password"]
    }
    write_json("data/login.json", login_data)

    register.click_cont()

