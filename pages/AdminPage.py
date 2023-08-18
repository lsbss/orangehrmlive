from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class AdminPage(PageObject):
    btn_adicionar_usuario = 'bi-plus'
    btn_lixeira = 'bi-trash'
    btn_lapis = 'bi-pencil-fill'
    btn_reset = 'button--ghost'
    btn_pesquisar = "button[class*='orangehrm-left-space']"
    btn_reset = "//button[normalize-space()='Reset']"
    select = "(//div[@class='oxd-select-text oxd-select-text--active'][contains(.,'-- Select --')])[1]"
    input_user_name = "(//input[contains(@class,'oxd-input oxd-input--active')])[2]"
    delete_user = "div[class*='oxd-table-cell-actions'] > button:nth-of-type(1)"
    edit_user = "div[class*='oxd-table-cell-actions'] > button:nth-of-type(2)"
    confirm_delete = "button[class*='oxd-button--label-danger']"
    select_user_role = "(//div[@class='oxd-select-text oxd-select-text--active'][contains(.,'-- Select --')])[1]"
    not_found = "//span[@class='oxd-text oxd-text--span'][contains(.,'No Records Found')]"
    search_result = "//span[@class='oxd-text oxd-text--span'][contains(.,'(1) Record Found')]"
    employee_name_column = "//i[contains(@class,'oxd-icon bi-sort-alpha-down oxd-icon-button__icon oxd-table-header-sort-icon')]"
    ascending = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[2]/div/div/ul/li[1]/span'
    first_employee_name = "(//div[contains(.,'Aaliyah Haq')])[13]"

    def __init__(self, driver):
        super(AdminPage, self).__init__(driver=driver)

    def click_btn_adicionar(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_adicionar_usuario).click()

    def click_btn_lixeira(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_lixeira).click()

    def click_btn_lapis(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_lapis).click()

    def click_btn_reset(self):
        self.driver.find_element(By.XPATH, self.btn_reset).click()

    def click_btn_pesquisar(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_pesquisar).click()

    def digitar_nome_do_usuario(self, user_name='Grupo_6_Teste'):
        self.driver.find_element(By.XPATH, self.input_user_name).send_keys(user_name)

    def set_role_admin(self):
        self.choose_drop_down_item(label='User Role', item_to_be_select='Admin')

    def set_status(self, status):
        self.choose_drop_down_item(label='Status', item_to_be_select=status)

    def set_employee_name(self):
        self.select_autocomplete_option(label='Employee Name', item_to_be_select='Lisa Andrews')

    def delete_admin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.delete_user).click()

    def confirm_delete_admin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.confirm_delete).click()

    def confirm_not_found(self):
        return self.driver.find_element(By.XPATH, self.not_found).is_displayed()

    def confirm_one_result(self):
        return self.driver.find_element(By.XPATH, self.search_result).is_displayed()

    def click_employee_name_column(self):
        self.driver.find_element(By.XPATH, self.employee_name_column).click()

    def click_ascending(self):
        self.driver.find_element(By.XPATH, self.ascending).click()

    def is_ascending(self):
        return self.driver.find_element(By.XPATH, self.first_employee_name).is_displayed()
