class RegisterPlaywrightPage:

    def __init__(self, page):
        self.page = page

    def open_register(self):

        self.page.get_by_role("link", name = "Register").click()

    def new_user(self, firstname, lastname, email, password):
        self.page.get_by_label("Female").click()
        self.page.get_by_label("First name:").fill(firstname)
        self.page.get_by_role("textbox", name = "Last name:").fill(lastname)
        self.page.get_by_role("textbox", name = "Email:").fill(email)
        self.page.get_by_label("Password:").fill(password)
        self.page.get_by_label("Confirm password:").fill(password)
        self.page.get_by_role("button", name = "Register").click()

    def verify_success_msg(self):
        return self.page.get_by_text("Your registration completed").inner_text()

    def click_cont(self):
        self.page.get_by_role("button", name = "Continue").click()
        