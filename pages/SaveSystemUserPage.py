from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class SaveSystemUserPage(PageObject):

    def __init__(self, driver):
        super(SaveSystemUserPage, self).__init__(driver=driver)


