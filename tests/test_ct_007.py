from pages.BuzzPage import BuzzPage
from pages.MenuPage import MenuPage


class Test_ct007:

    def test_adicionar_comentario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_buzz()
        buzz_page = BuzzPage(driver=menu_page.driver)
        buzz_page.click_btn_adicionar_comentario()
        buzz_page.inserir_novo_comentario()
        assert buzz_page.validar_comentario_adicionado(), "Comentário não foi encontrado!"
