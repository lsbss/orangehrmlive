from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage

class Test_ct004:

    def test_ordenar_por_nome_do_usuario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.click_employee_name_column()
        admin_page.click_ascending()
        assert admin_page.is_ascending() == True