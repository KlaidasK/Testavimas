from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://fill.dev/form/registration-simple"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Locate input fields and enter values
    input1 = browser.find_element(By.NAME, "email")  # Corrected locator
    input1.send_keys("new@mail.com")

    input2 = browser.find_element(By.NAME, "username")  # Username
    input2.send_keys("tom")

    input3 = browser.find_element(By.NAME, "password")  # password
    input3.send_keys("tom123")

    input4 = browser.find_element(By.NAME, "password_confirmation")  # password confirmation
    input4.send_keys("tom123")

    # Click submit button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)  
    browser.quit()
