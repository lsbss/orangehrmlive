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
        novo_nome = 'Novo Usuario' + str(random.randint(800, 900))
        admin_page.digitar_novo_do_usuario(novo_nome)
        save_system_user_page = SaveSystemUserPage(driver=admin_page.driver)
        save_system_user_page.press_save_btn()
        assert admin_page.validar_btn_pesquisar()
        admin_page.digitar_nome_do_usuario(novo_nome)
        admin_page.click_btn_pesquisar()
        assert admin_page.validar_pesquisa() == True
