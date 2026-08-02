# DemoWebShop Playwright Automation Framework Guide

This document explains the current automation framework in a simple way so you can continue adding new user stories confidently.

---

## 1. What this project is doing

This project automates the DemoWebShop website using:
- Python
- Pytest
- Playwright

The current focus is on the registration flow, but the same structure can be reused for login, search, cart, checkout, and other user stories.

---

## 2. Main framework idea

The framework follows the Page Object Model (POM) approach.

In simple words:
- Tests should describe the user flow.
- Page classes should contain the actions on a page.
- Locators should be stored separately.
- Test data should be kept outside the test logic.

This keeps the code clean, reusable, and easier to maintain.

---

## 3. Project structure and purpose

### Root files
- conftest.py
  - Contains shared test fixtures.
  - Creates the Playwright browser page and opens the application.
  - Loads test data for tests.

- structure.md
  - A general folder template.
  - It is not the exact current implementation, but it helps explain the expected structure.

### Main folders

#### Pages/
This folder contains page-specific classes.

Example:
- Pages/registerloctor.py
- Pages/register_palywrightlocators.py

Each class represents one page or one feature and contains methods like:
- open page
- enter data
- click button
- verify success message

This is the heart of the framework.

#### Locators/
This folder contains all element locators.

Example:
- Locators/register_locators.py

Why this matters:
- If a UI element changes, you update it in one place.
- Tests and page classes stay cleaner.

#### testcases/
This folder contains test cases.

Example:
- testcases/test_reg.py
- testcases/test_register.py

Each test should:
- create a page object
- call page methods
- assert the expected outcome

#### utilities/
This folder contains reusable helper modules.

Example:
- utilities/constants.py
- utilities/data_reader.py

These files hold shared constants and reusable functions.

#### data/
This folder stores test data.

Example:
- data/register.json

This is where you keep input values such as names, emails, passwords, etc.

---

## 4. How the current registration flow works

The current flow is:

1. A test starts.
2. The fixture creates a browser page and opens the DemoWebShop URL.
3. The test creates a page object for registration.
4. The page object clicks the Register link.
5. The test passes user details from JSON data.
6. The page object fills the registration form.
7. The system registers the user.
8. The test checks the success message.
9. The page object clicks Continue.

### Current test flow example
In testcases/test_reg.py:
- the test uses RegisterPlaywrightPage
- it calls open_register_page
- then new_user
- then verify_success_msg
- then click_cont

This is a good example of how future tests should be structured.

---

## 5. Important file roles

### conftest.py
This file is very important because it defines the shared fixtures.

Current fixtures:
- page
  - launches the browser
  - opens the application URL
  - gives the test a page object
- register_data
  - loads registration data from JSON

This means every test can reuse the same browser setup without rewriting it.

### utilities/constants.py
This file holds constants like:
- BASE_URL

Instead of hardcoding the URL everywhere, it is stored in one place.

### utilities/data_reader.py
This file reads JSON files.

This is useful because test inputs can be changed without editing the test code.

---

## 6. How to add a new user story

When you add a new feature like Login, Search, or Cart, follow this pattern.

### Step 1: Add locators
Create or update a locator file in Locators/.

Example idea:
- Locators/login_locators.py

Store all XPath or Playwright locators there.

### Step 2: Create a page object class
Create a new class in Pages/.

Example idea:
- Pages/login_page.py

This class should include methods such as:
- open_login_page()
- enter_credentials()
- click_login()
- verify_success_message()

### Step 3: Add a test case
Create a test in testcases/.

Example idea:
- testcases/test_login.py

The test should:
- use the page object
- call the methods
- perform assertions

### Step 4: Keep test data external
Store values in data/.

Example:
- data/login.json

This makes your tests easier to maintain.

### Step 5: Reuse fixtures
If a new test needs the browser page, use the existing fixture from conftest.py.

---

## 7. Recommended coding pattern for new stories

Use this structure whenever you add a new feature:

1. Locator file
   - define all selectors

2. Page object class
   - define actions and validations

3. Test case file
   - call the page object and verify results

4. Data file
   - keep input values separate

This keeps your framework scalable.

---

## 8. Best practices for this project

### Follow Page Object Model
Do not put direct locator actions inside tests. Keep them inside page classes.

### Keep locators centralized
Do not scatter XPath directly in tests.

### Keep test data separate
Do not hardcode names, emails, or passwords inside tests.

### Use meaningful method names
Example:
- open_register_page()
- new_user()
- verify_success_msg()

### Keep tests readable
A good test should read like a real user flow.

### Avoid duplicate implementations
Right now, registration has two page object versions:
- Pages/registerloctor.py
- Pages/register_palywrightlocators.py

For future work, choose one style and use it consistently.

---

## 9. Current observations about the project

These are useful points for you as a new contributor:

- The framework is already structured in a basic POM style.
- Registration is implemented and works as a good starting example.
- The code is simple and beginner-friendly.
- There is some duplication in the registration implementation, so standardizing the approach will make the framework stronger.
- The project can be expanded by adding more page objects and more test cases.

---

## 10. Simple developer workflow for new features

When you get a new user story, follow this checklist:

- Understand the user flow
- Identify the page(s) involved
- Create or update locators
- Create page object methods
- Add a test case
- Put test data in JSON
- Run the test
- Fix issues if any

---

## 11. Example for a future user story: Login

If the next story is Login, you would likely create:

- Locators/login_locators.py
- Pages/login_page.py
- testcases/test_login.py
- data/login.json

And the test would look like this conceptually:

```python
from Pages.login_page import LoginPage


def test_login(page, login_data):
    login = LoginPage(page)
    login.open_login_page()
    login.enter_credentials(login_data["email"], login_data["password"])
    login.click_login()
    assert login.verify_login_success() == "expected message"
```

This is the same pattern used by the registration tests.

---

## 12. Final takeaway

The framework is already built around a clean and learnable pattern:
- tests in testcases
- page actions in Pages
- selectors in Locators
- shared data in data
- common setup in conftest.py

If you continue using this pattern for every new story, the project will stay organized and easy to expand.

---

## 13. Suggested next step

For your next task, start with one simple feature such as:
- Login
- Logout
- Search product
- Add product to cart

Use the registration flow as your template and follow the same structure.
