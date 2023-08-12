from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/'
    element_username = 'username'
    element_password = 'password'
    login_button = 'oxd-button'

    def __init__(self):
        super(LoginPage, self).__init__()
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button).click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def efetuar_login(self, user_name='Admin', password='admin123'):
        self.driver.find_element(By.NAME, self.element_username).send_keys(user_name)
        self.driver.find_element(By.NAME, self.element_password).send_keys(password)
        self.click_login_btn()
