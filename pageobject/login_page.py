from time import sleep

import pytest

from basepage.base_page import BasePage
from selenium.webdriver.common.by import By


# @pytest.mark.usefixtures("env")
class LoginPage(BasePage):
    """登录功能"""
    username_loc = ('by_xpath,//input[@placeholder="请输入账号或手机号"]')
    password_loc = ('by_xpath,//input[@placeholder="请输入密码"]')
    # 点击登录按钮
    login_button = ('by_xpath,//div[@class="form"]/preceding-sibling::div//div[@class="cus-btn"]/*')

    @pytest.mark.usefixtures("env")
    def login_ddt(self, username, password, env):

        # if env["test_env_url"] in "https://test.hkciot.com/#/login":
        #     test_env_url = env["test_env_url"]
        #     self.go_to( test_env_url)
        # else:
        #     cloud_env_url = env["cloud_env_url"]
        #     self.go_to(cloud_env_url)
        # test_env_url = env["test_env_url"]
        self.driver.refresh()
        test_env_url = "https://test.hkciot.com/#/login"
        self.go_to(test_env_url)
        self.driver.refresh()
        sleep(0.3)
        self.click(self.username_loc)
        self.input(self.username_loc, username)
        # "读excel-输入用户名成功"
        sleep(0.3)

        self.click(self.password_loc)
        self.input(self.password_loc, password)
        # 读excel-输入密码成功"
        sleep(0.3)

        self.click_button(self.login_button)
        # print("读excel-点击登录按钮成功")
        sleep(0.3)

    # 登录成功操作流程
    # def success_login(self, username='test', password='Aa12345678'):
    def success_login(self, env):
        try:
            if env["test_env_url"] in "https://test.hkciot.com/#/login":
                username = env["test_env_username"]
                password = env["test_env_password"]
            else:
                username = env["cloud_env_username"]
                password = env["cloud_env_password"]

            self.click(self.username_loc)
            self.input(self.username_loc, username)
            # print("输入用户名成功")
            sleep(0.5)

            self.click(self.password_loc)
            self.input(self.password_loc, password)
            # print("输入密码成功")
            sleep(0.5)

            self.click_button(self.login_button)

            # print("点击登录按钮成功")
            sleep(0.5)
        except Exception:
            raise

    def click_personal_picture(self):
        """
        点击右上角头像
        :return:
        """
        personal_picture_locator ='by_xpath,//div[@class="avatar"]'
        self.click(personal_picture_locator)


    def click_personal_center(self):
        """
        点击个人中心
        :return:
        """
        personal_center_locator = 'by_xpath,//*[text()=" 个人中心 "]'
        self.click(personal_center_locator)

    def close_personal_center_alert(self):
        """
        关闭个人中心弹框
        :return:
        """
        close_personal_center_button ='by_xpath,//i[@class="el-icon el-dialog__close"]'
        self.click(close_personal_center_button)

    def modify_email(self,email):
        """
        修改邮箱名称
        :return:
        """
        email_locator = 'by_xpath,//input[@placeholder="请输入邮箱"]'
        self.clear(email_locator)
        self.input(email_locator,email)

    def personal_center_confirm_button(self):
        """
        在个人中心弹框，点击确认按钮
        :return:
        """
        personal_center_confirm_button ='by_xpath,//span[text() =" 确定 "]'

        self.click(personal_center_confirm_button)