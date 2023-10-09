from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import time

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    
    button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.XPATH, "(//h5[normalize-space()='$100'])[1]"))
    )
   
    button1 = browser.find_element(By.XPATH, "(//button[normalize-space()='Book'])[1]").click()

    x_element = browser.find_element(By.XPATH , "(//span[@id='input_value'])[1]")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "(//input[@id='answer'])[1]")
    input1.send_keys(y)

    button = browser.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()


    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
