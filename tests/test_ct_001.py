import time

from pages.MenuPage import MenuPage


class Test_ct001:

    def test_adicionar_usuario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        time.sleep(5)
