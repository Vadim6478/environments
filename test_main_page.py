
def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    driver.get(link)
    login_link = driver.find_element("css selector", "#login_link")
    login_link.click()