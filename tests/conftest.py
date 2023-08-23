import random

import pytest

from pages.AdminPage import AdminPage
from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage
from pages.SaveSystemUserPage import SaveSystemUserPage


def pytest_addoption(parser):
    parser.addoption("--select_browser", default="chrome", help="Select browser")


@pytest.fixture
def select_browser(request):
    yield request.config.getoption("--select_browser").lower()


@pytest.fixture
def setup(select_browser):
    login_page = LoginPage()
    yield login_page
    login_page.close()


@pytest.fixture
def login_orange_hrm(setup):
    login_page = setup
    login_page.efetuar_login()
    yield login_page


@pytest.fixture
def adicionar_usuario(login_orange_hrm):
    menu_page = MenuPage(driver=login_orange_hrm.driver)
    menu_page.click_menu_admin()
    admin_page = AdminPage(driver=menu_page.driver)
    admin_page.click_btn_adicionar()
    nome = 'Novo Usuario' + str(random.randint(200, 300))
    admin_page.digitar_nome_do_usuario(nome)
    admin_page.set_role_admin()
    admin_page.set_status('Enabled')
    admin_page.set_employee_name()
    save_system_user_page = SaveSystemUserPage(driver=admin_page.driver)
    save_system_user_page.set_password()
    save_system_user_page.set_confirm_password()
    save_system_user_page.press_save_btn()
    assert admin_page.validar_btn_pesquisar()
    yield admin_page, nome
