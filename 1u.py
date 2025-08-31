from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Palaukti, kol kaina taps 100$
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Kai kaina yra 100$, spausti "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

    # Gauti x reikšmę
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

    # Įvesti atsakymą
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Spausti "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

