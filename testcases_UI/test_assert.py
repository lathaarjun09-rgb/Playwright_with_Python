import pytest

def test_soft_assertion(page):
    page.goto("https://tricentis.com")
    
    # Track errors manually if external modules are restricted by IT
    failures = []
    
    if page.title() != "Demo Web Shop":
        failures.append(f"Title mismatch: Expected 'Demo Web Shop' but got '{page.title()}'")
        
    if not page.locator(".ico-register").is_visible():
        failures.append("Register link is not visible")
    else:
        print("Is visible")
        
    if not page.locator(".ico-login").is_visible():
        failures.append("Login link is not visible")
    else:
        print("Login is visible in the application")
        
    # Block triggers test failure at the very end with all collected errors
    assert not failures, "\n".join(failures)