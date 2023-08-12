import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return self.driver.current_url == url

    def choose_drop_down_item(self, label, item_to_be_select):
        grid_items = self.driver.find_elements(By.CLASS_NAME, 'oxd-input-group')
        for item in grid_items:
            if item.find_element(By.CLASS_NAME, 'oxd-label').text == label:
                item.find_element(By.CLASS_NAME, "oxd-select-text").click()
                # Localizar o item específico no menu suspenso usando seu seletor
                menu_items = item.find_elements(By.CSS_SELECTOR, '[role="option"]')
                for menu_tem in menu_items:
                    if menu_tem.text == item_to_be_select:
                        menu_tem.click()
                        time.sleep(3)
                        break
                break

    def select_autocomplete_option(self, label, item_to_be_select):
        grid_items = self.driver.find_elements(By.CLASS_NAME, 'oxd-input-group')
        for item in grid_items:
            if item.find_element(By.CLASS_NAME, 'oxd-label').text == label:
                item.find_element(By.CLASS_NAME, "oxd-autocomplete-option").send_keys('Lisa')
                # Localizar o item específico no menu suspenso usando seu seletor
                menu_items = item.find_elements(By.CSS_SELECTOR, '[role="option"]')
                for menu_tem in menu_items:
                    if menu_tem.text == item_to_be_select:
                        menu_tem.click()
                        time.sleep(3)
                        break
                break
