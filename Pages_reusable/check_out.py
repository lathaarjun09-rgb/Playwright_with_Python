from .checkout_locators import CheckoutLocators


class checkout:

    def __init__(self, page):
        self.page = page

    def checkout_process(self):
        self.page.wait_for_selector(CheckoutLocators.COUNTRY_DROPDOWN, timeout=30000)
        self.page.wait_for_timeout(3000)

        count_of_country = self.page.locator(CheckoutLocators.COUNTRY_OPTIONS).count()
        print(f"The count of the country dropdown: {count_of_country}")

        options = self.page.locator(CheckoutLocators.COUNTRY_OPTIONS).all_text_contents()
        values = self.page.locator(CheckoutLocators.COUNTRY_OPTIONS).evaluate_all(
            "els => els.map(e => e.value)"
        )
        print(options)
        print(values)

        state_dropdown = self.page.locator(CheckoutLocators.STATE_DROPDOWN)
        state_options = state_dropdown.locator(CheckoutLocators.STATE_OPTIONS).all_text_contents()
        print("Available State Options:", state_options)

        state_dropdown.select_option(label="Other (Non US)")
        self.page.wait_for_timeout(3000)

        terms_checkbox = self.page.locator(CheckoutLocators.TERMS_CHECKBOX)
        terms_checkbox.check()
        print("successfully clicked on the check box")

        self.page.wait_for_timeout(3000)
        self.page.wait_for_selector(CheckoutLocators.COUNTRY_DROPDOWN, timeout=30000)
        self.page.wait_for_timeout(5000)

        self.page.locator(CheckoutLocators.COUNTRY_DROPDOWN).select_option(label="India")
        self.page.locator(CheckoutLocators.COUNTRY_DROPDOWN).select_option(index=41)
        print("Successfully selected the dropdown with index")
        self.page.locator(CheckoutLocators.COUNTRY_DROPDOWN).select_option(value="41")
        country = self.page.locator(CheckoutLocators.COUNTRY_DROPDOWN).all_text_contents()
        print(country)

        self.page.wait_for_timeout(5000)
        checkbox = self.page.locator(CheckoutLocators.TERMS_CHECKBOX)
        self.page.wait_for_timeout(2000)
        checkbox.uncheck()
        self.page.wait_for_timeout(2000)

        print("The Checkbox got selected")
        if checkbox.is_checked():
            checkbox.uncheck()
            print("It unselected")
        else:
            checkbox.check()
            print("It got selected")

        self.page.locator(CheckoutLocators.CHECKOUT_BUTTON).click()
        print("successfully clicked on the Checkout box")
        self.page.wait_for_timeout(3000)