import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class MenuPage(PageObject):
    menu_admin = '[href="/web/index.php/admin/viewAdminModule"]'
    menu_buzz = '[href="/web/index.php/buzz/viewBuzz"]'

    def __init__(self,driver):
        super(MenuPage, self).__init__(driver=driver)

    def click_menu_admin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.menu_admin).click()

    def click_menu_buzz(self):
        self.driver.find_element(By.CSS_SELECTOR, self.menu_buzz).click()
