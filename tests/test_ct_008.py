from pages.BuzzPage import BuzzPage
from pages.MenuPage import MenuPage


class Test_ct008:

    def test_curtir_postagem(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_buzz()
        buzz_page = BuzzPage(driver=menu_page.driver)
        buzz_page.click_btn_curtir()
        assert buzz_page.validar_postagem_curtida(), "Postagem não foi curtida"
