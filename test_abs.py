
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_abs1():
    
   link = "http://suninjuly.github.io/registration1.html"
   browser = webdriver.Chrome()
   browser.get(link)
   input1 = browser.find_element(By.XPATH, "(//input[@class='form-control first'])[1]")
   input1.send_keys("Ivan")
         
   input2 = browser.find_element(By.XPATH, "(//input[@class='form-control second'])[1]")
   input2.send_keys("Petrov")
         
   input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
   input3.send_keys("Polianinvo@lad24.ru")
         

   button = browser.find_element(By.CSS_SELECTOR, "button.btn")
   button.click()

    
   welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

   welcome_text = welcome_text_elt.text

   assert "Congratulations! You have successfully registered!" == welcome_text

   
    
def test_abs2(self):

   link = "http://suninjuly.github.io/registration2.html"
   browser = webdriver.Chrome()
   browser.get(link)

        
   input1 = browser.find_element(By.XPATH, "(//label[text()='First name*']/following::input)[1]")
   input1.send_keys("Ivan")
   input2 = browser.find_element(By.XPATH, "(//label[text()='Last name*']/following::input)[1]")
   input2.send_keys("Petrov")
   input3 = browser.find_element(By.XPATH, "(//label[text()='Email*']/following::input)[1]")
   input3.send_keys("Polianinvo@lad24.ru")
    
   button = browser.find_element(By.CSS_SELECTOR, "button.btn")
   button.click()

    

    
   welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
   welcome_text = welcome_text_elt.text    
        
   assert "Congratulations! You have successfully registered!" == welcome_text
   



  