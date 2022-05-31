import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    window = browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element_by_id('input_value')
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