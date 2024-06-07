import time
import random
from time import sleep

import allure
import pytest
from allure_commons._allure import step

from common.set_up_org import OrgList
from pageobject.system_page import SystemPage


@pytest.fixture(scope='class')
def system_page(request, driver):
    system_page = SystemPage(driver)
    request.cls.system_page = system_page
    yield system_page

    org_list = OrgList()
    all_org_ids = org_list.get_org_ids()
    org_list.clear_all_org()
    org_list.add_branch("test_分支")


# @pytest.fixture(scope='class')
# def account_page(request, driver):
#     account_page = AccountManagement(driver)
#     request.cls.account_page = account_page
#     yield account_page


@allure.epic("项目hkc")
@allure.feature("system management")
@pytest.mark.usefixtures("system_page")
# @pytest.mark.usefixtures("env")
class TestSystemManagement:

    @allure.title("点击系统管理")
    @pytest.mark.run(order=1)
    def test_system_logo(self):
        system_page = self.system_page
        with step("左侧栏进入系统管理模块"):
            system_page.switch_to_system_management()
        sleep(0.5)

    @allure.title("添加分支")
    @pytest.mark.run(order=2)
    def test_add_branch(self):
        system_page = self.system_page
        system_page.refresh()
        with step("左侧栏进入系统管理模块"):
            system_page.switch_to_system_management()
        time.sleep(0.5)
        with step("点击系统管理-组织架构-添加机构按钮"):
            system_page.add_org_icon()
        # self.driver.switch_to_alert()
        with step("点击分支名称处"):
            system_page.find_branch_name()
        branch_name = random.randint(1, 1000)
        with step("输入分支名称"):
            system_page.input_branch_name(branch_name)
        with step("选择上级机构"):
            system_page.select_perent_org_branch()
        with step("隐藏下拉框，去点击分支名称"):
            system_page.click_branch_name()
        with step("点击确定按钮"):
            system_page.add_shop_submit_button()

    # @pytest.mark.skip(reason="没写好 不要执行")
    @allure.title("添加门店")
    @pytest.mark.run(order=3)
    def test_add_shop(self):
        system_page = self.system_page
        with step("左侧栏进入系统管理模块"):
            system_page.switch_to_system_management()
        time.sleep(0.5)
        with step("点击系统管理-组织架构-添加机构按钮"):
            system_page.add_org_icon()
        with step("点击门店tab"):
            system_page.add_shop()
        shop_name = random.randint(1, 1000)
        with step("输入门店名称"):
            system_page.input_shop_name(shop_name)
        with step("选择上级机构"):
            system_page.select_perent_org_shop()
        with step("隐藏下拉框，去点击分支名称"):
            system_page.click_branch_name()
        with step("点击确认按钮"):
            system_page.add_shop_submit_button()

    #
    # @allure.title("批量添加门店100个")
    # @pytest.mark.run(order=3)
    # def test_batch_add_shop(self):
    #     system_page = self.system_page
    #     with step("左侧栏进入系统管理模块"):
    #         system_page.switch_to_system_management()
    #     # time.sleep(0.5)
    #     for i in range(1,100):
    #         with step("点击系统管理-组织架构-添加机构按钮"):
    #             system_page.add_org_icon()
    #         # time.sleep(0.5)
    #         with step("点击门店tab"):
    #             system_page.add_shop()
    #         # time.sleep(0.5)
    #         shop_name = random.randint(1, 1000)
    #         with step("输入门店名称"):
    #             system_page.input_shop_name(shop_name)
    #         # time.sleep(1)
    #         with step("选择上级机构"):
    #             system_page.select_perent_org_shop()
    #         # time.sleep(1)
    #         with step("隐藏下拉框，去点击分支名称"):
    #             system_page.click_branch_name()
    #         # time.sleep(1)
    #         with step("点击确认按钮"):
    #             system_page.add_shop_submit_button()

    @allure.title("修改名称门店")
    @pytest.mark.run(order=4)
    def test_edit_org(self):
        system_page = self.system_page
        time.sleep(0.5)
        with step("左侧栏进入系统管理模块"):
            system_page.switch_to_system_management()
        time.sleep(0.5)
        with step("点击修改icon"):
            system_page.edit_org()
        shop_name = random.randint(1, 1000)
        time.sleep(0.5)
        with step("输入门店名称"):
            system_page.input_shop_name(shop_name)
        with step("点击确认按钮"):
            system_page.add_shop_submit_button()

    @allure.title("删除机构-取消删除")
    @pytest.mark.run(order=5)
    def test_add_org_cancel(self):
        system_page = self.system_page
        time.sleep(0.5)
        with step("左侧栏进入系统管理模块"):
            system_page.switch_to_system_management()
        time.sleep(0.5)
        with step("点击删除按钮"):
            system_page.delete_org()
        time.sleep(0.5)
        with step("点击取消按钮"):
            system_page.delete_org_cancel()

    @allure.title("删除机构-确定删除")
    @pytest.mark.run(order=6)
    def test_delete_org(self):
        system_page = self.system_page
        time.sleep(0.5)
        with step("左侧栏进入系统管理模块"):
            system_page.switch_to_system_management()
        time.sleep(0.5)
        with step("点击删除按钮"):
            system_page.delete_org()
        time.sleep(0.5)
        with step("点击确定按钮"):
            system_page.delete_org_confirm()

    @allure.title("创建新账号,不输入内容，点击确认")
    @pytest.mark.run(order=7)
    def test_add_account_nothing_input(self):
        system_page = self.system_page
        system_page.switch_to_system_management()
        with step("点击添加账户按钮"):
            time.sleep(0.5)
            system_page.switch_account_management()
            time.sleep(0.5)
            # system_page.add_account()
        with step("创建账户icon"):
            system_page.add_account_icon()
        time.sleep(0.5)
        with step("不输入内容，直接点击确认"):
            system_page.add_account_submit()
        time.sleep(0.5)
        with step("点击取消"):
            system_page.add_account_cancel()

    @allure.title("创建新账户,新账户的类型是企业管理员")
    @pytest.mark.run(order=8)
    def test_add_account(self):
        system_page = self.system_page
        system_page.switch_to_system_management()
        system_page.switch_account_management()
        with step("创建账户icon"):
            system_page.add_account_icon()
        time.sleep(0.5)
        with step('输入手机号码'):
            time.sleep(1)
            # random_tel = system_page.generate_phone_number()
            system_page.input_account_tel("13752848596")
        time.sleep(0.5)
        with step("选择账户类型:管理员"):
            system_page.account_type_admin()
        time.sleep(0.5)
        with step("选择所属机构"):
            system_page.account_org()
        with step("点击确定按钮"):
            system_page.add_account_confirm()

    # 获取下今天、明天、昨天的日期
    today = time.strftime("%Y-%m-%d", time.localtime())
    yesterday = time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400))
    tomorrow = time.strftime("%Y-%m-%d", time.localtime(time.time() + 86400))
    date_today = str(today)
    date_yesterday = str(yesterday)
    date_tomorrow = str(tomorrow)

    @allure.title("筛选操作日志：昨天、今天")
    def test_filter_operation_log(self):
        system_page = self.system_page
        system_page.refresh()
        system_page.switch_to_system_management()
        with step("进入操作日志页面"):
            system_page.switch_to_operation_log()
        with step("查看当天的操作日志"):
            time.sleep(0.3)
            system_page.search_log_date(start=self.today, end=self.today)
            time.sleep(0.3)
            system_page.clear_log_date()
        #
        with step("查看昨天的操作日志"):
            time.sleep(0.3)
            system_page.search_log_date(start=self.yesterday, end=self.yesterday)
            time.sleep(0.3)
            system_page.clear_log_date()

        with step("查看明天的操作日志"):
            time.sleep(0.3)
            system_page.search_log_date(start=self.yesterday, end=self.tomorrow)
            time.sleep(0.3)
            system_page.clear_log_date()

        with step("查看昨天到今天2天的操作日志"):
            time.sleep(0.3)
            system_page.search_log_date(start=self.yesterday, end=self.today)
            time.sleep(0.3)
            system_page.clear_log_date()
