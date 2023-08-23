from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage
from tests.conftest import adicionar_usuario


class Test_ct002:

    def test_deletar_usuario(self, adicionar_usuario):
        admin_page, nome = adicionar_usuario
        admin_page.digitar_nome_do_usuario(nome)
        admin_page.click_btn_pesquisar()
        admin_page.delete_admin()
        admin_page.confirm_delete_admin()
        admin_page.click_btn_pesquisar()
        assert admin_page.confirm_not_found() == True

