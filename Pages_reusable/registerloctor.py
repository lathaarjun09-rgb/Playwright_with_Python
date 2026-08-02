from Locators.register_locators import RegisterLocators

class RegisterPage:

    def __init__(self,page): #constructor: Whenever we are creating objects automatically to execute the objects
        self.page = page

    def open_register_page(self):
        self.page.locator(RegisterLocators.register_link).click()
# Create new user
    def user_data(self, firstname, lastname, email, password):
        self.page.locator(RegisterLocators.gender_female).click() # button, radio button, link
        self.page.locator(RegisterLocators.first_name).fill(firstname) # text 
        self.page.locator(RegisterLocators.last_name).fill(lastname)
        self.page.locator(RegisterLocators.email).fill(email)
        self.page.locator(RegisterLocators.password).fill(password)
        self.page.locator(RegisterLocators.confirm_password).fill(password)
        self.page.locator(RegisterLocators.register_button).click()

    def verify_msg(self):
        return self.page.locator(RegisterLocators.success_msg).inner_text()

    def click_register(self):
        self.page.locator(RegisterLocators.continue_btn).click()



