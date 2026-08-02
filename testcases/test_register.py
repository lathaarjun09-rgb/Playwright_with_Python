from Pages.registerloctor import RegisterPage
from utilities.data_writer import write_json


def test_register(page,register_data):
    register = RegisterPage(page) # Creating the Object to use the page functions

    register.open_register_page() # It will click on the register link
    print("Successfully clickeed on the Register link")

    register.user_data(register_data["firstname"],
                       register_data["lastname"],
                       register_data["email"],
                       register_data["password"]) # It is passing the parameters from the json file
    #assert register.verify_msg() == "Your registration completed" # Expected
    # getting from the application matching with the expected details
    actual_msg = register.verify_msg()
    assert actual_msg == "Your registration completed" # Expected
    print("Actual message is: ", actual_msg)

    login_data = {
        "email" : register_data["email"],
        "password" : register_data["password"]
    }
    write_json("data/login.json", login_data) # It will write the data to the login.json file
    print("successfully captured")
    register.click_register()

