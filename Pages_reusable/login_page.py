from Locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, page):
        self.page = page

    def open_login_page(self):
        self.page.locator(LoginLocators.LOGIN_LINK).click()

    class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, email, password):
        self.page.goto(f"{BASE_URL}/login")
        self.page.locator("#Email").fill(email)
        self.page.locator("#Password").fill(password)
        self.page.locator("//input[@class='button-1 login-button']").click()
        self.page.wait_for_load_state("networkidle")
        

    # def get_error_message(self):
    #     return self.page.locator(LoginLocators.ERROR_MSG).inner_text()

    # def verify_login(self):
    #     return self.page.locator(LoginLocators.LOGOUT_LINK).is_visible()

