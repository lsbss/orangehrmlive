import pytest

from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage

class TestLogin:
    @pytest.fixture
    def setup(self):
        login_page = LoginPage()
        yield login_page
        login_page.close()

    def test_login(self, setup):
        login_page = setup
        login_page.efetuar_login(user_name='Admin', password='admin123')
