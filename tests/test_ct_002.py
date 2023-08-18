from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage


class Test_ct002:

    def test_deletar_usuario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.digitar_nome_do_usuario('Usuario Editado')
        admin_page.click_btn_pesquisar()
        admin_page.delete_admin()
        admin_page.confirm_delete_admin()
        admin_page.click_btn_pesquisar()
        assert admin_page.confirm_not_found() == True

