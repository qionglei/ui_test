import time
import random
from time import sleep

import allure
import pytest
from allure_commons._allure import step

from common.set_up_option_management import OptionManagement
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

    option_class = OptionManagement()
    option_class.clear_all_org_type()
    option_class.clear_all_org_level()


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
    @pytest.mark.skip("定位元素未实现")
    def test_click_system_logo(self):
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
        branch_name = random.randint(100, 1000)
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
        shop_name = random.randint(100, 1000)
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
    #         shop_name = random.randint(10, 1000)
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
        shop_name = random.randint(100, 1000)
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
    @pytest.mark.run(order=9)
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

    # *******************************操作横屏系统垫片******************************

    @allure.title("预览横屏系统垫片")
    @pytest.mark.run(order=10)
    def test_preview_accross_system_spacer(self):
        system_page = self.system_page

        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("如果有垫片，就直接预览，没有就先进行上传"):
            system_page.hover_to_accross()
            preview_system_spacer = 'by_xpath,//div[@class="mask1"]/img[1]'
            if not system_page.element_exist(preview_system_spacer):
                system_page.add_accross_system_spacer()
                time.sleep(2)
                system_page.refresh()
                system_page.switch_to_system_setting()
                time.sleep(1)
                system_page.hover_to_accross()
                system_page.preview_accross_system_spacer()
            else:
                system_page.preview_accross_system_spacer()

        with step("关闭预览按钮"):
            system_page.close_accross_preview()

    @allure.title("更换横屏系统垫片")
    @pytest.mark.run(order=11)
    def test_change_accross_system_spacer(self):
        system_page = self.system_page
        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("有就进行更换，没有就上传"):
            system_page.hover_to_accross()
            preview_system_spacer = 'by_xpath,//div[@class="mask1"]/img[2]'
            if not system_page.element_exist(preview_system_spacer):
                system_page.add_accross_system_spacer()
            else:
                system_page.replace_accross_system_spacer()

    @allure.title("删除横屏系统垫片")
    @pytest.mark.run(order=12)
    def test_delete_accross_system_spacer(self):
        system_page = self.system_page

        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("删除系统垫片"):
            system_page.hover_to_accross()
            del_button = 'by_xpath,//div[@class="mask1"]/img[3]'
            if system_page.element_exist(del_button):
                system_page.delete_accross_system_spacer()
            else:
                system_page.add_accross_system_spacer()
                time.sleep(2)
                system_page.refresh()
                system_page.switch_to_system_setting()
                time.sleep(1)
                system_page.hover_to_accross()
                system_page.delete_accross_system_spacer()

    @allure.title("添加横屏系统垫片")
    @pytest.mark.run(order=13)
    def test_add_accross_system_spacer(self):
        system_page = self.system_page

        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("点击上传按钮，进行系统垫片上传"):
            system_page.add_accross_system_spacer()

    # **************************操作竖屏系统垫片************************************

    @allure.title("预览竖屏系统垫片")
    @pytest.mark.run(order=14)
    def test_preview_stand_system_spacer(self):
        system_page = self.system_page

        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("如果有垫片，就直接预览，没有就先进行上传"):
            system_page.hover_to_stand()
            preview_system_spacer = 'by_xpath,//div[@class="mask2"]/img[1]'
            if not system_page.element_exist(preview_system_spacer):
                system_page.add_stand_system_spacer()
                time.sleep(3)
                system_page.switch_to_system_setting()
                system_page.hover_to_stand()
                system_page.preview_stand_system_spacer()
            else:
                system_page.hover_to_stand()
                system_page.preview_stand_system_spacer()

        with step("关闭预览按钮"):
            system_page.close_stand_preview()

    @allure.title("更换竖屏系统垫片")
    @pytest.mark.run(order=15)
    def test_change_stand_system_spacer(self):
        system_page = self.system_page
        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("有就进行更换，没有就上传"):
            system_page.hover_to_stand()
            preview_system_spacer = 'by_xpath,//div[@class="mask2"]/img[2]'
            if not system_page.element_exist(preview_system_spacer):
                system_page.add_stand_system_spacer()
            else:
                system_page.replace_stand_system_spacer()

    @allure.title("删除竖屏系统垫片")
    @pytest.mark.run(order=16)
    def test_delete_stand_system_spacer(self):
        system_page = self.system_page

        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("删除系统垫片"):
            system_page.hover_to_stand()
            del_button = 'by_xpath,//div[@class="mask2"]/img[3]'
            if system_page.element_exist(del_button):
                system_page.delete_stand_system_spacer()
            else:
                system_page.add_stand_system_spacer()
                time.sleep(2)
                system_page.refresh()
                time.sleep(1)
                system_page.switch_to_system_setting()
                time.sleep(1)
                system_page.hover_to_stand()
                system_page.delete_stand_system_spacer()

    @allure.title("添加竖屏系统垫片")
    @pytest.mark.run(order=17)
    def test_add_stand_system_spacer(self):
        system_page = self.system_page

        with step("进入系统设置tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_system_setting()

        with step("点击上传按钮，进行系统垫片上传"):
            system_page.add_stand_system_spacer()

    # ************************开发者页面************************************
    @allure.title("点击生成新的access key")
    @pytest.mark.run(order=18)
    def test_gen_access_key(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("点击重新生成按钮"):
            system_page.click_gen_access_key()

    @allure.title("取消生成access key")
    @pytest.mark.run(order=19)
    def test_cancel_gen_access_key(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("点击重新生成按钮"):
            system_page.click_gen_access_key()

        with step("点击取消按钮"):
            system_page.cancel_gen_access_key_alert()

    @allure.title("确认生成access key")
    @pytest.mark.run(order=20)
    def test_confirm_gen_access_key(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("点击重新生成按钮"):
            system_page.click_gen_access_key()

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

    @allure.title("复制生成access key")
    @pytest.mark.run(order=21)
    def test_copy_access_key(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("点击重新生成按钮"):
            system_page.click_gen_access_key()

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

        with step("点击复制按钮"):
            system_page.copy_access_key()

    @allure.title("通过元素拿到生成的access key")
    @pytest.mark.run(order=21)
    def test_get_access_key(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("点击重新生成按钮"):
            system_page.click_gen_access_key()

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

        with step("点击复制按钮"):
            system_page.return_access_key()

    @allure.title("下载动态数据API说明文件")
    @pytest.mark.run(order=22)
    def test_download_dynamic_api_instruction(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("下载动态数据API说明文件"):
            system_page.download_dynamic_api_instruction()

    @allure.title("下载动态数据SDK依赖包")
    @pytest.mark.run(order=23)
    def test_download_dynamic_sdk_file(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("下载动态数据SDK依赖包"):
            system_page.download_dynamic_sdk_file()

    @allure.title("动态数据调用样例代码")
    @pytest.mark.run(order=24)
    def test_download_dynamic_example_code(self):
        system_page = self.system_page

        with step("进入开发者tab"):
            system_page.switch_to_system_management()
            system_page.switch_to_develops()

        with step("下载动态数据调用样例代码"):
            system_page.download_dynamic_example_code()

    #
    # **************************选项维护***********************
    @allure.title("选项维护tab页，打开新增机构分类弹框")
    @pytest.mark.run(order=25)
    def test_close_add_org_type_alert(self):
        system_page = self.system_page

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构分类icon"):
            system_page.click_add_org_type_icon()

        with step("关闭新增机构分类弹框"):
            system_page.cancel_gen_access_key_alert()

    @allure.title("选项维护tab页，取消新增机构分类")
    @pytest.mark.run(order=26)
    def test_cancel_add_org_type_alert(self):
        system_page = self.system_page

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构分类icon"):
            system_page.click_add_org_type_icon()

        with step("关闭新增机构分类弹框"):
            system_page.close_gen_access_key_alert()

    @allure.title("选项维护tab页，新增一个机构分类")
    @pytest.mark.run(order=27)
    def test_add_org_type(self):
        system_page = self.system_page
        random_type_description = "org_type" + str(random.randint(100, 1000))
        random_remark = "org_remark" + str(random.randint(100, 100))

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构分类icon"):
            system_page.click_add_org_type_icon()

        with step("输入分类描述"):
            system_page.input_org_type_description(random_type_description)

        with step('输入备注'):
            system_page.input_org_type_remark(random_remark)

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

    @allure.title("选项维护tab页，机构分类，分类描述和备注不输入内容")
    @pytest.mark.run(order=28)
    def test_add_org_type_no_input(self):
        system_page = self.system_page

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构分类icon"):
            system_page.click_add_org_type_icon()

        with step("输入分类描述"):
            system_page.input_org_type_description("")

        with step('输入备注'):
            system_page.input_org_type_remark("")

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

        header_org_type = 'by_xpath,//header[@class="el-dialog__header"]/span[text()="机构分类"]'

        if system_page.element_exist(header_org_type):
            system_page.cancel_gen_access_key_alert()

    @allure.title("选项维护tab页，修改第一个机构分类")
    @pytest.mark.run(order=29)
    def test_edit_org_type(self):
        system_page = self.system_page
        random_type_description = "org_type" + str(random.randint(100, 1000))
        random_remark = "org_remark" + str(random.randint(100, 1000))

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构分类icon"):
            system_page.click_add_org_type_icon()

        with step("输入分类描述"):
            system_page.input_org_type_description(random_type_description)

        with step('输入备注'):
            system_page.input_org_type_remark(random_remark)
            system_page.confirm_gen_access_key()

        with step("修改分类描述"):
            system_page.edit_org_type()
            system_page.input_org_type_description(random_type_description)
            system_page.input_org_type_remark(random_remark)

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

    @allure.title("选项维护tab页，删除第一个机构分类")
    @pytest.mark.run(order=30)
    def test_delete_org_type(self):
        system_page = self.system_page
        random_type_description = "org_type" + str(random.randint(100, 1000))
        random_remark = "org_remark" + str(random.randint(100, 1000))

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构分类icon"):
            system_page.click_add_org_type_icon()

        with step("输入分类描述"):
            system_page.input_org_type_description(random_type_description)

        with step('输入备注'):
            system_page.input_org_type_remark(random_remark)
            system_page.confirm_gen_access_key()

        with step("删除分类描述"):
            system_page.delete_org_type()

    # ****************************机构级别**************************************************
    @allure.title("选项维护tab页，打开新增机构级别弹框")
    @pytest.mark.run(order=31)
    def test_close_add_org_level_alert(self):
        system_page = self.system_page

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构级别icon"):
            system_page.click_add_org_level_icon()

        with step("关闭新增机构级别弹框"):
            system_page.cancel_gen_access_key_alert()

    @allure.title("选项维护tab页，取消新增机构级别")
    @pytest.mark.run(order=32)
    def test_cancel_add_org_level_alert(self):
        system_page = self.system_page

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构级别icon"):
            system_page.click_add_org_level_icon()

        with step("关闭新增机构级别弹框"):
            system_page.close_gen_access_key_alert()

    @allure.title("选项维护tab页，新增一个机构级别")
    @pytest.mark.run(order=33)
    def test_add_org_level(self):
        system_page = self.system_page
        random_level_description = "org_type" + str(random.randint(100, 1000))
        random_remark = "org_remark" + str(random.randint(100, 1000))

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构级别icon"):
            system_page.click_add_org_level_icon()

        with step("输入级别描述"):
            system_page.input_org_level_description(random_level_description)

        with step('输入备注'):
            system_page.input_org_level_remark(random_remark)

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

    @allure.title("选项维护tab页，机构级别，级别描述和备注不输入内容")
    @pytest.mark.run(order=34)
    def test_add_org_type_no_input(self):
        system_page = self.system_page
        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构级别icon"):
            system_page.click_add_org_level_icon()

        with step("输入级别描述"):
            system_page.input_org_level_description("")

        with step('输入备注'):
            system_page.input_org_level_remark("")

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

        header_org_type = 'by_xpath,//header[@class="el-dialog__header"]/span[text()="机构级别"]'

        if system_page.element_exist(header_org_type):
            system_page.cancel_gen_access_key_alert()

    @allure.title("选项维护tab页，修改第一个机构级别")
    @pytest.mark.run(order=35)
    def test_edit_org_level(self):
        system_page = self.system_page
        random_level_description = "org_type" + str(random.randint(100, 1000))
        random_remark = "org_remark" + str(random.randint(100, 1000))

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构级别icon"):
            system_page.click_add_org_level_icon()

        with step("输入级别描述"):
            system_page.input_org_level_description(random_level_description)

        with step('输入备注'):
            system_page.input_org_level_remark(random_remark)
            system_page.confirm_gen_access_key()

        with step("修改级别描述"):
            system_page.edit_org_level()
            system_page.input_org_level_description(random_level_description)
            system_page.input_org_level_remark(random_remark)

        with step("点击确认按钮"):
            system_page.confirm_gen_access_key()

    @allure.title("选项维护tab页，删除第一个机构级别")
    @pytest.mark.run(order=36)
    def test_delete_org_level(self):
        system_page = self.system_page
        random_level_description = "org_type" + str(random.randint(100, 1000))
        random_remark = "org_remark" + str(random.randint(100, 1000))

        with step("切换到选项维护tab页"):
            system_page.switch_to_system_management()
            system_page.switch_to_option_maintenance()

        with step("点击新增机构级别icon"):
            system_page.click_add_org_level_icon()

        with step("输入级别描述"):
            system_page.input_org_level_description(random_level_description)

        with step('输入备注'):
            system_page.input_org_level_remark(random_remark)
            system_page.confirm_gen_access_key()
        with step("删除级别描述"):
            system_page.delete_org_level()
