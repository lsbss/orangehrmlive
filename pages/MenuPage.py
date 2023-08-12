import time

import selenium.common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class MenuPage(PageObject):
    menu_admin = "(//span[contains(.,'Admin')])[1]"

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def click_menu_admin(self):
        self.driver.find_element(By.XPATH, self.menu_admin).click()
        time.sleep(5)
