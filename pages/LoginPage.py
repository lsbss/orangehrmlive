from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    url = 'https://opensource-demo.orangehrmlive.com/'
    element_username = "//input[@name='username']"
    element_password = "//input[@name='password']"
    login_button = "button[class*='oxd-button']"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def click_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def efetuar_login(self, user_name='Admin', password='admin123'):
        self.driver.find_element(By.XPATH, self.element_username).send_keys(user_name)
        self.driver.find_element(By.XPATH, self.element_password).send_keys(password)
        self.click_login_btn()
