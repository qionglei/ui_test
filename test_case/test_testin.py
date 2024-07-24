import allure
import pytest
from time import sleep
from selenium import webdriver
from common.excel import read_excel
from pageobject.login_page import LoginPage


@allure.epic("项目hkc")
@allure.feature("login")
@pytest.mark.skip(reason="重复用例，隐藏不运行")
class SkipTestTestIn:
    # 打开浏览器
    def setup(self) -> None:
        self.driver = webdriver.Chrome()
        driver = self.driver
        print("\n setup begin=============")

    def teardown(self) -> None:
        sleep(0.5)
        print("\n tear down=============")
        # self.driver.close()
    '''利用excel导入登录测试数据'''

    @pytest.mark.parametrize('case', read_excel(r'D:\git\ui_test\data\data.xlsx', 'login'))
    @allure.title("登录成功")
    def Skip_test_01_login(self, case):
        """测试登录模块"""
        xh, case_name, username, password, is_exc, result, bz = case
        lp = LoginPage(self.driver)
        lp.testin_login(username, password)

    # def test_02_select_iphone_12(self):
    #     """测试根据品牌选择手机"""
    #     lp = LoginPage(self.driver)
    #     lp.testin_login()
    #     ps = SelectPage(self.driver)
    #     ps.testin_select_01_iphone()
    #
    # def test_03_select_androi_sys(self):
    #     """测试根据安卓系统选择手机"""
    #     lp = LoginPage(self.driver)
    #     lp.testin_login()
    #     ps = SelectPage(self.driver)
    #     ps.testin_select_02_android()
    #
    # def test_04_select_online_time(self):
    #     """测试根据上市时间来选择手机"""
    #     lp = LoginPage(self.driver)
    #     lp.testin_login()
    #     ps = SelectPage(self.driver)
    #     ps.testin_select_03_onlin_time()

# import os
# if __name__ == "__main__":
#     print("-----------------开始main")
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
#     pytest.main(["-s","-v",'--alluredir', './temp'])
#     # 执行命令生成测试报告
#
#     print("-----------------结束")
#     os.system('allure generate ./temp -o ./Report --clean')
