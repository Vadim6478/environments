
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import math, pytest, time

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

##["236895","236896","236897","236898","236899","236903","236904","236905"] 
# #фикстура с параметрами для теста
#@pytest.mark.parametrize('url', ["236895"])

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(driver):
    driver.get(link)
    driver.find_element("id", "login_link") 