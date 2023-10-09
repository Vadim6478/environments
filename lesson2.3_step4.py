from xml.etree import cElementTree
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, "(//button[normalize-space()='I want to go on a magical journey!'])[1]" ).click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.XPATH , "(//span[@id='input_value'])[1]")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "(//input[@id='answer'])[1]")
    input1.send_keys(y)

    button = browser.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()
    


    
   
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
