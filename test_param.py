

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, pytest, time

    

@pytest.mark.parametrize('url', ["236895","236896","236897","236898","236899","236903","236904","236905"]) #["236895","236896","236897","236898","236899","236903","236904","236905"] #фикстура с параметрами для теста

class TestMainOption():



    def test_params(self,browser,url):
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.implicitly_wait(5)
        answer = math.log(int(time.time()))
        print(answer)

        browser.get(link) 
        browser.implicitly_wait(30)  # ждём прогрузки страницы (неявное ожидание)

        button_enter = browser.find_element(By.ID, "ember33")  # нажимаем на кнопку авторизации на сайте
        button_enter.click()

        input_email = browser.find_element(By.ID, "id_login_email")  # вводим логин
        input_email.send_keys("Polianinvo@lad24.ru")

        input_password = browser.find_element(By.ID, "id_login_password")
        input_password.send_keys("Unapeb822")  # вводим пароль

        button_login = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")  # нажимаем на кнопку "Войти"
        button_login.click()

        time.sleep(10)       

        # Вводим ответ
        try:
            # Если кнопка "Решить снова" есть
            browser.implicitly_wait(10)
            button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
            button_again.click()

            # Если кнопки "Решить снова" нет
        except NoSuchElementException:
            print('Кнопка "Решить снова" отсутствует')

        finally:
            # Находим поле ввода ответа
            time.sleep(20)
            input_answer = browser.find_element(By.TAG_NAME, 'textarea')
            input_answer.clear()

            # Вычисляем ответ
            # Если ваше время не совпадает со временем на сайте, то смотрим на сайте отображаемую разницу
            #answer = math.log(int(time.time()) - 0.034)
            answer_text = str(answer)

            # Вводим и отправляем ответ
            input_answer.send_keys(answer_text)
            time.sleep(5)
            button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
            button_send.click()

            # Проверяем ответ
            browser.implicitly_wait(10)
            answer_feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
            assert answer_feedback.text == "Correct!", "Wrong answer!"

  