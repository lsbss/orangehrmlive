from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class SaveSystemUserPage(PageObject):
    select_user_role = ("//div[@class='oxd-select-text oxd-select-text--focus']//div[@class='oxd-select-text-input']["
                        "normalize-space()='-- Select --']")

    def __init__(self, driver):
        super(SaveSystemUserPage, self).__init__(driver=driver)

    def digitar_nome_do_usuario(self, user_role='Admin'):
        select = Select(self.driver.find_element(By.XPATH, self.select_user_role))
        select.select_by_index(1)
