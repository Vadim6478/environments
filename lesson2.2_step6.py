from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.select import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
        
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.XPATH , "(//span[@id='input_value'])[1]")
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    input1 = browser.find_element(By.XPATH, "(//input[@id='answer'])[1]")
    input1.send_keys(y)
   
    option1 = browser.find_element(By.XPATH, "(//input[@id='robotCheckbox'])[1]")
    option1.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    
    option1 = browser.find_element(By.XPATH, "(//input[@value='robots'])[1]")
    option1.click()

    button = browser.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]") 
    button.click()
     
    
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
