from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage
import random

from pages.SaveSystemUserPage import SaveSystemUserPage


class Test_ct003:

    def test_editar_usuario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.digitar_nome_do_usuario('Usuario Editado')
        admin_page.click_btn_pesquisar()
        admin_page.edit_admin()
        nome = random.randint(1, 99)
        admin_page.digitar_nome_do_usuario(str(nome))
        save_system_user_page = SaveSystemUserPage(driver=admin_page.driver)
        save_system_user_page.press_save_btn()
        admin_page.digitar_nome_do_usuario('Usuario Editado' + str(nome))
        admin_page.click_btn_pesquisar()
        assert admin_page.confirm_edit == True
