import time

from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage
from pages.SaveSystemUserPage import SaveSystemUserPage
import random


class Test_ct001:

    def test_adicionar_usuario(self, adicionar_usuario):
        admin_page, nome = adicionar_usuario
        admin_page.digitar_nome_do_usuario(nome)
        admin_page.click_btn_pesquisar()
        assert admin_page.validar_pesquisa() == True
