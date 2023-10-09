from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

        
try:
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    button1 = browser.find_element(By.XPATH, "(//button[normalize-space()='Verify'])[1]").click()
    
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

      
     
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
