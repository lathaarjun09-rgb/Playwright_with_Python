#Soft Assertion

from pytest_check import check

def test_soft_assertion(page):
    page.goto("https://demowebshop.tricentis.com/")
    
    check.equal(page.title(),"Demo Shop")
    
    check.is_true(page.locator(".ico-register").is_visible())
    print("Is visible")
    
    check.is_true(page.locator(".ico-login").is_visible())
    print("Login is visible in the application")