from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class AdminPage(PageObject):
    btn_adicionar_usuario = 'bi-plus'
    btn_lixeira = 'bi-trash'
    btn_lapis = 'bi-pencil-fill'
    btn_pesquisar = "//button[normalize-space()='Search']"
    input_user_name = "(//input[contains(@class,'oxd-input oxd-input--active')])[2]"
    btn_reset = "//button[normalize-space()='Reset']"
    select = "(//div[@class='oxd-select-text oxd-select-text--active'][contains(.,'-- Select --')])[1]"
    resultado_pesquisa = "//span[@class='oxd-text oxd-text--span'][contains(.,'(1) Record Found')]"

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
        self.driver.find_element(By.XPATH, self.btn_pesquisar).click()

    def digitar_nome_do_usuario(self, user_name='Admin'):
        self.driver.find_element(By.XPATH, self.input_user_name).send_keys(user_name)

    def set_role_admin(self):
        self.choose_drop_down_item(label='User Role', item_to_be_select='Admin')

    def set_status(self):
        self.choose_drop_down_item(label='Status', item_to_be_select='Enabled')

    def set_employee_name(self):
        self.choose_drop_down_item(label='Employee Name', item_to_be_select='Lisa Andrews')

    def validar_nome_da_pagina_admin_resetado(self):
        user_name_input = self.driver.find_element(By.XPATH, self.input_user_name)
        username_value = user_name_input.get_attribute("value")
        return username_value == ""

    def validar_user_role_selecionado(self):
        user_role_select = self.driver.find_element(By.XPATH, self.select)
        selected_user_role = user_role_select.get_attribute("innerText").strip()
        return selected_user_role == "-- Select --"

    def validar_status_resetado(self):
        status_select = self.driver.find_element(By.XPATH, self.select)
        selected_status = status_select.get_attribute("innerText").strip()
        return selected_status == "-- Select --"

    def validar_pesquisa(self):
        return self.driver.find_element(By.XPATH, self.resultado_pesquisa).is_displayed()
