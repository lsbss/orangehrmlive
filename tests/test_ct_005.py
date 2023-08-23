from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage


class Test_ct005:

    def test_pesquisar_usuario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.digitar_nome_do_usuario()
        admin_page.set_role_admin()
        admin_page.set_status('Enabled')
        admin_page.click_btn_pesquisar()
        assert admin_page.validar_pesquisa(), "Erro na pesquisa"
