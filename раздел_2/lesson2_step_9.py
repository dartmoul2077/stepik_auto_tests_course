import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)


    
    # for label in browser.find_element_by_class_name('form-group'):
    #     labels = label.find_element_by_partial_link_text('*')
    #     if browser.find_element_by_partial_link_text('*'):
    #         browser.find_element_by_class_name('form-control').send_keys('dick')

    labels = browser.find_elements_by_tag_name('label') # Список лэйблов над текстовыми полями
    inputs = browser.find_elements_by_tag_name('input') # Список текстовых полей

    for i, label in enumerate(labels):          # Если последний символ
        if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Обязалово!')   # то в поле ввода печатаем "Обязалово!"

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')  

    dowloand = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    dowloand.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(10)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()