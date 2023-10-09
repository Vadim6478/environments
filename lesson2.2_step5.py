from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.select import Select
def calc(x:str , y:str):
        return str(int(x) + int(y))

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.XPATH , "(//span[@id='num1'])[1]")
    x = x_element.text
    print(int(x))
    y_element = browser.find_element(By.XPATH , "(//span[@id='num2'])[1]")
    y = y_element.text
    print(int(y))
    
    print(calc(x , y))
    z = calc(x , y)

    select = Select(browser.find_element(By.XPATH , "(//select[@id='dropdown'])[1]"))
    select.select_by_value(value = z)
    

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()
        
    
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
