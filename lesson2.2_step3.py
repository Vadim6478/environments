from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
# инициализировать новый объект, передав в него WebElement с тегом select. Далее можно найти любой вариант из списка с помощью метода select_by_value(value):
from selenium.webdriver.support.ui import Select 

import time
import math

def calc(x):
  return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    # Запускаю браузер с помощью веб драйвера
    browser = webdriver.Chrome()                      
    browser.get(link)

    # Найти 1 значение и присвоить ему "Х"
    num1 = browser.find_element(By.CSS_SELECTOR , "//span[@id='num1']")
    x = num1.text

    # Найти 2 значение и присвоить ему "Х"
    num2 = browser.find_element(By.CSS_SELECTOR , "//span[@id='num2']")
    y = num2.text

    
    

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=calc(x)) # Ищем любой вариант из списка с select_by_value(value):

    # Это работает тоже работает но долго
    #browser.find_element(By.TAG_NAME, "select").click() - кликаем на выпадающий список
    #rowser.find_element(By.CSS_SELECTOR, "[value='93']").click() - выбираем занчение из выпадающего списка 
    
          
    
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

