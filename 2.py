import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Fixture with `function` scope (default) - runs once per test
@pytest.fixture(scope="function")
def browser():
    print("\n[Setup] Starting browser for test...")
    driver = webdriver.Chrome()
    yield driver
    print("\n[Teardown] Quitting browser...")
    time.sleep(1)
    driver.quit()


# class-scoped fixture (shared within one class)
@pytest.fixture(scope="class")
def class_data():
    return {
        "name": "Test",
        "surname": "User",
        "email": "test@example.com"
    }


# autouse fixture (applies automatically)
@pytest.fixture(scope="module", autouse=True)
def before_all_tests():
    print("\n=== Starting registration test module ===")
    yield
    print("\n=== Ending registration test module ===")

class TestRegistrationForms:

    def fill_form_and_submit(self, browser, url, class_data):
        browser.get(url)

        # Fill the form using test data
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(class_data["name"])
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(class_data["surname"])
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(class_data["email"])

        # Submit the form
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)

        return browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1_should_pass(self, browser, class_data):
        url = "http://suninjuly.github.io/registration1.html"
        result = self.fill_form_and_submit(browser, url, class_data)
        assert result == "Congratulations! You have successfully registered!"

    def test_registration2_should_fail(self, browser, class_data):
        url = "http://suninjuly.github.io/registration2.html"
        result = self.fill_form_and_submit(browser, url, class_data)
        assert result == "Congratulations! You have successfully registered!"
