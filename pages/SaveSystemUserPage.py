import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class SaveSystemUserPage(PageObject):

    input_password = "div[class*='user-password-cell'] > div > div:nth-of-type(2) > input"
    input_confirm_password = "div[class*='user-password-row'] > div > div:nth-of-type(2) > div > div:nth-of-type(2) > input"
    btn_save = "button[class *='oxd-button--secondary']"

    def __init__(self, driver):
        super(SaveSystemUserPage, self).__init__(driver=driver)

    def set_password(self):
        self.driver.find_element(By.CSS_SELECTOR, self.input_password).send_keys('Abcd@1234')

    def set_confirm_password(self):
        self.driver.find_element(By.CSS_SELECTOR, self.input_confirm_password).send_keys('Abcd@1234')

    def press_save_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_save).click()


