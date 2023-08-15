import time
from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage


class Test_ct006:

    def test_resetar_campos_de_pesquisa(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.digitar_nome_do_usuario()
        admin_page.set_role_admin()
        admin_page.set_status()
        admin_page.click_btn_reset()
        assert admin_page.validar_nome_da_pagina_admin_resetado(), "Campo de usuário não foi resetado corretamente"
        assert admin_page.validar_user_role_selecionado(), "User Role não foi resetado para '-- Select --'"
        assert admin_page.validar_status_resetado(), "Status não foi resetado para '-- Select --'"



