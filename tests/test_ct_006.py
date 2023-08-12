import time

from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage
from pages.SaveSystemUserPage import SaveSystemUserPage


class Test_ct006:

    def test_resetar_campos_de_pesquisa(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.digitar_nome_do_usuario()
        admin_page.click_btn_reset()
        time.sleep(5)


