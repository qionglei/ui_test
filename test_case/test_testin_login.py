import allure
import pytest
from time import sleep

from common.excel import read_excel
from conftest import env
from pageobject.login_page import LoginPage


@pytest.fixture(scope='class')
def login_page(request, driver):
    login_page = LoginPage(driver)
    request.cls.login_page = login_page
    yield login_page


@allure.epic("项目hkc")
@allure.feature("login-test")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("env")
class TestLogin:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('case', read_excel(r'D:\ui\data\data.xlsx', 'login'))
    @allure.title("登录成功")
    def test_login_ddt(self, case):
        """测试登录模块"""

        xh, case_name, username, password, is_exc, result, bz = case
        login_page = self.login_page
        login_page.refresh()
        login_page.login_ddt(username, password, env)

    @pytest.mark.run(order=2)
    @pytest.mark.skip(reason="hover没有效果，也没报错，没写好")
    @allure.title("点击个人中心头像logo")
    def test_click_logo(self):
        login_page = self.login_page
        login_page.success_login()
        sleep(0.5)
        login_page.click_personal_logo()

    # @pytest.mark.parametrize('case', read_excel(r'D:\ui\data\data.xlsx', 'login'))
    # @allure.title("登录成功")
    # def test_01_login(self, case):
    #     """测试登录模块"""
    #     xh, case_name, username, password, is_exc, result, bz = case
    #     login_page= self.login_page
    #     login_page.testin_login(username, password)



