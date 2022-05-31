# import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(num1,num2):
    return str(num1+num2)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    x = int(x_element.text)
    y = int(y_element.text)

    sum = calc(x,y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()



finally:
    time.sleep(15)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()