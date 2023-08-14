from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class AdminPage(PageObject):
    btn_adicionar_usuario = 'bi-plus'
    btn_lixeira = 'bi-trash'
    btn_lapis = 'bi-pencil-fill'
    btn_reset = 'button--ghost'
    btn_pesquisar = 'left-space'
    input_user_name = "(//input[contains(@class,'oxd-input oxd-input--active')])[2]"
    #btn_reset = "//button[normalize-space()='Reset']"
    #btn_pesquisar = "//button[normalize-space()='Search']"
    #menu_buzz = '[href="/web/index.php/buzz/viewBuzz"]'
    #imput_user_name = "(//input[contains(@class,'oxd-input oxd-input--active')])[2]"
    select_user_role = "(//div[@class='oxd-select-text oxd-select-text--active'][contains(.,'-- Select --')])[1]"


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

    def digitar_nome_do_usuario(self, user_name='Grupo_6_Teste'):
        self.driver.find_element(By.XPATH, self.input_user_name).send_keys(user_name)

    def set_role_admin(self):
        self.choose_drop_down_item(label='User Role', item_to_be_select='Admin')

    def set_status(self):
        self.choose_drop_down_item(label='Status', item_to_be_select='Enabled')

    def set_employee_name(self):
        self.choose_drop_down_item(label='Employee Name', item_to_be_select='Lisa Andrews')
