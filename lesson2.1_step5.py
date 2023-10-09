from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.XPATH , "(//span[@id='input_value'])[1]")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "(//span[text()='?']/following::input)[1]")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
        
    
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
