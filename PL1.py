from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://hr.dev.unoto.ladcloud.ru/organization/1/organization-management"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вводим телефон
    time.sleep(2)
    input = browser.find_element(By.XPATH, "(//input[@class='ant-input'])[1]")
    input.send_keys("9000000001")
    
    time.sleep(2) 
    # Вводим пароль
    input = browser.find_element(By.XPATH, "(//input[@class='ant-input'])[2]")
    input.send_keys("456456")

    # Нажимаем кнопку Войти
    button = browser.find_element(By.XPATH, "//button[@type='submit']//span[1]")
    button.click()

    
    # ждем загрузки страницы
    time.sleep(2)

    #Заходим в админ организацию
    button = browser.find_element(By.XPATH, "(//a[@class='organization__item'])[1]")
    button.click()
    time.sleep(2)
    # Нажимаем Управление Организациями
    button = browser.find_element(By.XPATH, "//a[contains(text(),'Управление организациями')]")
    button.click()
    time.sleep(2)
    # Нажимаем Создать организацию
    button = browser.find_element(By.XPATH, "(//button[@type='button']//span)[1]")
    button.click()
    time.sleep(2)
    # Вводим Наименование организации
    input = browser.find_element(By.XPATH, "(//label[text()='Наименование']/following::input)[1]")
    input.send_keys("Autotest")
    time.sleep(2)
    # Выбираем тип организации
    # кликаем на выпадающий список
    browser.find_element(By.XPATH, "//input[@id='type']").click() 

    time.sleep(1) #так надо а то не выберет значение из вып списка

    #выбираем занчение из выпадающего списка 
    browser.find_element(By.CSS_SELECTOR, "div[title='Публичная организация'] div[class='ant-select-item-option-content']").click() 
    
    browser.find_element(By.XPATH, "//div[@class='ant-picker org-admin-create__date']").click() 
    time.sleep(1) #так надо а то не выберет дату
    time.sleep(2)
    browser.find_element(By.XPATH, "//div[@class='ant-picker-footer']//a[1]").click() 
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@type='submit']//span[1]").click() 

    input = browser.find_element(By.XPATH, "(//span[text()='Создать организацию']/following::input)[1]")
    input.send_keys("aut")
    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
