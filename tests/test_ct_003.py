import time

from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage
import random

from pages.SaveSystemUserPage import SaveSystemUserPage


class Test_ct003:

    def test_editar_usuario(self, adicionar_usuario):
        admin_page, nome = adicionar_usuario
        admin_page.digitar_nome_do_usuario(nome)
        admin_page.click_btn_pesquisar()
        admin_page.click_btn_lapis()
        admin_page.digitar_nome_do_usuario('editado')
        save_system_user_page = SaveSystemUserPage(driver=admin_page.driver)
        time.sleep(6)
        save_system_user_page.press_save_btn()
        admin_page.digitar_nome_do_usuario(nome + 'editado')
        admin_page.click_btn_pesquisar()
        assert admin_page.validar_pesquisa() == True
