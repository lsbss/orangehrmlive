import random
from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage
from pages.SaveSystemUserPage import SaveSystemUserPage


class Test_ct004:

    def test_ordenar_por_nome_do_usuario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.click_btn_adicionar()
        nome = '1111' + 'Novo Usuario' + str(random.randint(1, 999))
        admin_page.digitar_nome_do_usuario(nome)
        admin_page.set_role_admin()
        admin_page.set_status('Enabled')
        admin_page.set_employee_name()
        save_system_user_page = SaveSystemUserPage(driver=admin_page.driver)
        save_system_user_page.set_password()
        save_system_user_page.set_confirm_password()
        save_system_user_page.press_save_btn()
        admin_page.clicar_btn_ordenacao_user_name()
        admin_page.click_btn_opcao_ascending()
        assert admin_page.is_ascending() == True, "Lista de usuarios não ordernado pelos nomes em ordem alfabetica"
