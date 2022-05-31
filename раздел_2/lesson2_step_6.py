import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x=69):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option2 = browser.find_element(By.ID, "robotsRule").click()
    button.click()
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()



finally:
    time.sleep(15)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()