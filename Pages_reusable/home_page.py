from Locators.home_locators import HomePageLocators

class homepage:

    def __init__(self, page):
        self.page = page


    def add_product(self):
        self.page.locator(HomePageLocators.addtocart2).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(HomePageLocators.addtocart4).click()
        #waits for the product to be appear on the page
        self.page.wait_for_timeout(4000) #3s
        self.page.wait_for_selector(".button-1.add-to-cart-button").is_visible()
        self.page.locator(HomePageLocators.hdd_radio_btn).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(HomePageLocators.buycomputerAddtocart).click()       
        self.page.wait_for_timeout(1000)


    def click_shopping_cart(self):  
        self.page.locator(HomePageLocators.shoppingcart).click()  

    