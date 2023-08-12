from selenium import webdriver
from selenium.webdriver.common.by import By

class MenuPage:
    menu_admin = "Admin"

    def click_menu_admin(self):
        self.driver.find_element(By.LINK_TEXT, self.menu_admin).click()
