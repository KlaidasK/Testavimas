import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def fill_form_and_submit(self, url):
        browser = webdriver.Chrome()
        browser.get(url)

        try:
            # Užpildyti privalomus laukus
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Test")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("User")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@example.com")

            # Paspausti Submit
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            # Patikrinti rezultatą
            time.sleep(1)
            success_text = browser.find_element(By.TAG_NAME, "h1").text
            return success_text
        finally:
            time.sleep(5)
            browser.quit()

    def test_registration1_should_pass(self):
        url = "http://suninjuly.github.io/registration1.html"
        result = self.fill_form_and_submit(url)
        self.assertEqual(result, "Congratulations! You have successfully registered!")

    def test_registration2_should_fail(self):
        url = "http://suninjuly.github.io/registration2.html"
        result = self.fill_form_and_submit(url)
        self.assertEqual(result, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
