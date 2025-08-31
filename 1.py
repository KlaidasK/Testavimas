import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Pytest fixture to create a new browser for each test
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(1)  
    driver.quit()

class TestRegistrationForms:
    
    def fill_form_and_submit(self, browser, url):
        browser.get(url)

        # Fill required fields
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Test")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("User")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@example.com")

        # Click Submit
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Wait for result and return text
        time.sleep(1)
        return browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1_should_pass(self, browser):
        url = "http://suninjuly.github.io/registration1.html"
        result = self.fill_form_and_submit(browser, url)
        assert result == "Congratulations! You have successfully registered!"

    def test_registration2_should_fail(self, browser):
        url = "http://suninjuly.github.io/registration2.html"
        result = self.fill_form_and_submit(browser, url)
        assert result == "Congratulations! You have successfully registered!"
