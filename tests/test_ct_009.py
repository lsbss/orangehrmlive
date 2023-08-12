import time

from pages.BuzzPage import BuzzPage
from pages.MenuPage import MenuPage


class Test_ct009:

    def test_compartilhar_postagem(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_buzz()
        buzz_page = BuzzPage(driver=menu_page.driver)
        buzz_page.click_btn_compartilhar()
        buzz_page.compartilhar_comentario()
        assert buzz_page.validar_comentario_compartilhado()
