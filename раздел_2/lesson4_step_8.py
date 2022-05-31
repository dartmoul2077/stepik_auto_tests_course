import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn = browser.find_element_by_id('book').click()

    # browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(10)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()
