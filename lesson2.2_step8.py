from xml.etree import cElementTree
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.support.select import Select
        
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.XPATH, "(//input[@placeholder='Enter first name'])[1]")
    input1.send_keys('Vadim')
    
    input1 = browser.find_element(By.XPATH, "(//input[@placeholder='Enter last name'])[1]")
    input1.send_keys('Polianin')
    
    input1 = browser.find_element(By.XPATH, "(//input[@placeholder='Enter email'])[1]")
    input1.send_keys('Polianinvo@lad24.ru')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    element = browser.find_element(By.XPATH, "(//input[@id='file'])[1]")
    element.send_keys(file_path)
    #print(os.path.abspath(os.path.dirname(__file__)))
    #print(os.path.abspath(__file__))


    button1 = browser.find_element (By.XPATH, "(//button[normalize-space()='Submit'])[1]")
    button1.click()
     
    
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
