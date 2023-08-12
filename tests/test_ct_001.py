from pages.AdminPage import AdminPage
from pages.MenuPage import MenuPage
from pages.SaveSystemUserPage import SaveSystemUserPage


class Test_ct001:

    def test_adicionar_usuario(self, login_orange_hrm):
        menu_page = MenuPage(driver=login_orange_hrm.driver)
        menu_page.click_menu_admin()
        admin_page = AdminPage(driver=menu_page.driver)
        admin_page.click_btn_adicionar()
        save_system_user_page = SaveSystemUserPage(driver=admin_page.driver)
        save_system_user_page.select_user_role()
