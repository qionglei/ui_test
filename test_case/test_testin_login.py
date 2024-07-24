import random
import time

import allure
import pytest
from time import sleep

from allure_commons._allure import step

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
    @pytest.mark.parametrize('case', read_excel(r'D:\git\ui_test\data\data.xlsx', 'login'))
    @allure.title("登录成功")
    def test_login_ddt(self, case):
        """测试登录模块"""

        xh, case_name, username, password, is_exc, result, bz = case
        login_page = self.login_page
        login_page.refresh()
        login_page.login_ddt(username, password, env)

    @pytest.mark.run(order=2)
    @allure.title("点击头像logo")
    def test_click_logo(self):
        login_page = self.login_page
        with step("点击头像"):
            login_page.click_personal_picture()

    @pytest.mark.run(order=3)
    @allure.title("关闭个人中心弹框")
    def test_close_personal_center(self):
        login_page = self.login_page
        with step("点击头像"):
            login_page.click_personal_picture()

        with step("点击个人中心"):
            login_page.click_personal_center()

        time.sleep(3)

        with step("断言标题正确"):
            personal_center_title = 'by_xpath,//span[@class="el-dialog__title"]'
            assert login_page.element_exist(personal_center_title)

        with step("关闭个人中心弹框"):
            login_page.close_personal_center_alert()

    @pytest.mark.run(order = 4)
    @allure.title("在个人中心，修改邮箱")
    def test_modify_email(self):
        login_page = self.login_page
        random_num = random.randint(10,99)
        email_name = "uitest"+f"{random_num}"+"@qq.com"
        with step("点击头像"):
            login_page.click_personal_picture()

        with step("点击个人中心"):
            login_page.click_personal_center()

        with step("输入新的邮箱名称"):
            login_page.modify_email(email_name)

        with step("点击确定按钮"):
            login_page.personal_center_confirm_button()






