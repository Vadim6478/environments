from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://merchant.dev.unoto.ladcloud.ru/"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вводим телефон
    input1 = browser.find_element(By.XPATH, "(//input[@class='ant-input'])[1]")
    input1.send_keys("9000000004")
    
    #time.sleep(2) # для того чтоб видеть как выполняется тест
    # Вводим пароль
    input2 = browser.find_element(By.XPATH, "(//input[@class='ant-input'])[2]")
    input2.send_keys("456456")

    #time.sleep(2) # для того чтоб видеть как выполняется тест

    # Нажимаем кнопку Войти

    button = browser.find_element(By.XPATH, "//button[@type='submit']//span[1]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

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
