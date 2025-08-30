from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Paspauskite mygtuką
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Pereiti prie kito lango
    browser.switch_to.window(browser.window_handles[1])

    # Gauti x reikšmę
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)

    # Apskaičiuoti
    result = math.log(abs(12 * math.sin(x)))

    # Įvesti atsakymą
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))

    # Paspausti mygtuką
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(20)
    browser.quit()
