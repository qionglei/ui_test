import time
import random

import pyperclip
import pytest
from selenium.common import InvalidSelectorException

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import wait, expected_conditions

from basepage.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobject.login_page import LoginPage
# import datetime
from datetime import date, datetime
from selenium.common.exceptions import ElementClickInterceptedException


class SystemPage(BasePage):
    # def __init__(self, driver):
    #     super().__init__(driver)
    # username_loc = ('by_xpath,//input[@placeholder="请输入账号或手机号"]')

    add_shop_icon = ('by_xpath,//span[text()="门店" and @class="el-radio__label"]')

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_system_management(self):
        # try:
        #     system_mana_icon = ('by_xpath,//div[text()=" 系统管理"]')
        #
        #     print("点击系统管理成功")
        #
        #     system_management_locator = 'by_xpath,//div[text()=" 系统管理"]'
        #     clickable_ele = self.get_element(system_management_locator)
        #     get_classmethod = clickable_ele.get_attribute("class")
        #     if get_classmethod == "el-tree-node is-current is-focusable":
        #         pass
        #     else:
        #         self.click(system_management_locator)
        # except Exception:
        #     raise
        #
        system_mana_icon = 'by_xpath,//div[text()=" 系统管理"]'
        try:
            clickable_ele = self.get_element(system_mana_icon)
            get_classmethod = clickable_ele.get_attribute("class")
            if get_classmethod == "el-tree-node is-current is-focusable":
                pass
            else:
                self.click(system_mana_icon)
        except ElementClickInterceptedException:
            self.refresh()
            self.click(system_mana_icon)

    def add_org_icon(self):
        self.click('by_xpath,//span[text()="添加机构"]')

    def find_branch_name(self):
        """
        点击添加门店机构成功
        """
        self.driver.find_element(By.XPATH, '//span[text()="添加门店机构"]').click()  # 不建议用

    def click_branch_name(self):
        time.sleep(1)
        shop_name_loca = ('by_xpath,//input[@placeholder="名称最多不超过15个字"]')
        self.click(shop_name_loca)

    def input_branch_name(self, branch_name):
        time.sleep(1)
        branch_name_loca = ('by_xpath,//input[@placeholder="名称最多不超过15个字"]')
        self.click(branch_name_loca)
        self.input(branch_name_loca, branch_name)

    def input_shop_name(self, shop_name):
        time.sleep(1)
        shop_name_loca = ('by_xpath,//input[@placeholder="名称最多不超过15个字"]')
        self.click(shop_name_loca)
        self.input(shop_name_loca, shop_name)

    def select_perent_org_branch(self):
        # self.click("xpath,//input[contains(@placeholder,'请选择')]")
        time.sleep(1)
        org_element_loca = ('by_xpath,//div[@class="el-overlay"]//input[@placeholder="请选择"]')

        # org_element = self.get_element(org_element_loca)
        # print("下拉框定位到的元素是", org_element)
        # time.sleep(3)
        # select_element = Select(org_element)
        # select_element.select_by_index(1)
        self.click(org_element_loca)
        time.sleep(1)
        # select_org_num1_loca = ('by_xpath,//span[@class="el-radio__inner"]')
        # select_org_num1_loca = ('by_xpath,//label[@class="el-radio el-radio--large"]//span[@class="el-radio__inner"]')
        select_org_num1_loca = ('by_xpath,//input[@type="radio" and @value="0"]/following::*')
        self.click(select_org_num1_loca)
        time.sleep(1)
        # self.click("by_xpath,//header")

    def select_perent_org_shop(self):
        # self.click("xpath,//input[contains(@placeholder,'请选择')]")
        time.sleep(1)
        org_element_loca = ('by_xpath,//div[@class="el-overlay"]//input[@placeholder="请选择"]')
        self.click(org_element_loca)
        time.sleep(3)
        select_org_num1_loca = ('by_xpath,//label[@class="el-radio"]/span[@class="el-radio__input"]/span')
        self.click(select_org_num1_loca)
        time.sleep(3)
        # self.click("by_xpath,//header")

    def add_shop_submit_button(self):
        """
        新增门店，提交submit
        """
        self.click("by_xpath,//span[text()= ' 确认 ']")

    def add_shop(self):
        """
        点击门店
        """
        time.sleep(1)
        # win.accept()
        self.click(self.add_shop_icon)

    def edit_org(self):
        edit_org_loca = ('by_xpath,//tbody/tr[2]/td[6]/div/div/img[1]')
        self.click(edit_org_loca)

    def delete_org(self):
        delete_org_icon = ('by_xpath,//tbody/tr[2]/td[6]/div/div/img[2]')
        self.click(delete_org_icon)

    def delete_org_cancel(self):
        delete_org_cancel_loca = ('by_xpath,//span[text()="取消"]')
        self.click(delete_org_cancel_loca)

    def delete_org_confirm(self):
        delete_org_confirm_loca = ('by_xpath,//span[text()="确定"]')
        self.click(delete_org_confirm_loca)

    def switch_account_management(self):
        self.click('by_xpath,//span[text()="账户管理"]')

    # def add_account(self):
    #     time.sleep(1)
    #     self.click('by_xpath,//span[text()="创建账户"]')
    #
    # def loca_tel(self):
    #     time.sleep(2)
    #     tel_loc=('by_xpath,//input[contains(@placeholder,"请输入手机号码")]')
    #     self.click(tel_loc)

    def generate_phone_number(self):
        # 定义国内手机号段
        phone_prefix = ['13', '14', '15', '16', '17', '18']
        prefix = random.choice(phone_prefix)  # 从前缀列表中随机选取一个前缀
        suffix = str(random.randint(10000000, 99999999))  # 生成后八位数字作为后缀
        # 输出的电话号码是", prefix + suffix
        return prefix + suffix

    def input_account_tel(self, tel):
        """
        输入手机号码成功
        :param tel: 电话号码
        """
        time.sleep(1)
        tel_num_loca = '//input[contains(@placeholder,"请输入手机号码")]'
        a = self.driver.find_element(By.XPATH, tel_num_loca)
        a.click()
        a.send_keys(tel)

    def account_submit(self):
        time.sleep(1)
        self.click('by_xpath,//span/button[2]/span')

    def add_account_icon(self):
        add_account_icon_loca = ('by_xpath,//span[text()="创建账户"]')
        self.click(add_account_icon_loca)

    def add_account_submit(self):
        add_account_submit_loca = ('by_xpath,//span[text()=" 确认 "]')
        self.click(add_account_submit_loca)

    def add_account_cancel(self):
        add_account_cancel = ('by_xpath,//span[text()=" 取消 "]')
        self.click(add_account_cancel)

    def add_account_phone_num(self):
        """
        输入手机号码
        :return:
        """
        add_account_phone_num_loca = ('by_xpath,//input[@placeholder="请输入手机号码"]')
        self.click(add_account_phone_num_loca)

    def account_type_admin(self):
        """
        选择账户类型为admin
        """
        account_select_type_loca = ('by_xpath,//input[@placeholder="请选择账户类型"]')
        self.click(account_select_type_loca)
        time.sleep(0.5)
        account_type_admin_loca = ('by_xpath,//span[text()="企业管理员"]')
        self.click(account_type_admin_loca)

    def account_type_approver(self):
        account_select_type_loca = ('by_xpath,//input[@placeholder="请选择账户类型"]')
        self.click(account_select_type_loca)
        time.sleep(0.5)
        account_type_approver_loca = ('by_xpath,//span[text()="企业安全审批员"]')
        self.click(account_type_approver_loca)

    def account_org(self):
        account_org_loca = ('by_xpath,//label[text()="所属机构"]/following-sibling::div/div/div/div/input')
        time.sleep(0.5)
        self.click(account_org_loca)
        time.sleep(0.5)
        select_org_loca = (
            'by_xpath,//div[@class="el-cascader-panel"]//span[@class="el-radio__inner"]')
        self.click(select_org_loca)

    def add_account_confirm(self):
        # 先点击弹框标题，让下拉框消失
        time.sleep(0.5)
        click_add_account_title_loca = ('by_xpath,//span[text()="创建账户" and @role="heading"]')
        self.click(click_add_account_title_loca)
        time.sleep(0.5)
        add_account_confirm_loca = ('by_xpath,//span[text()=" 确认 "]')
        self.click(add_account_confirm_loca)

    def switch_to_operation_log(self):
        operation_log_loca = ('by_xpath,//span[text()="操作日志"]')
        self.click(operation_log_loca)

    def operation_log_start_date(self):
        operation_log_start_date_loca = ('by_xpath,//input[@placeholder="开始日期"]')
        self.click(operation_log_start_date_loca)
        return operation_log_start_date_loca

    # ++++++++++++++==========++++++操作日志+++++++++++++++++++++++++++++++++++++++++++++++++
    def search_log_date(self, start, end):
        start_button = ('by_xpath,//input[@placeholder="开始日期"]')
        end_button = ('by_xpath,//input[@placeholder="结束日期"]')

        start_locator = self.click('by_xpath,//input[@placeholder="开始日期"]')
        end_locator = self.click('by_xpath,//input[@placeholder="结束日期"]')
        self.input(start_button, start)
        ActionChains(self.driver).send_keys_to_element(start_locator, Keys.ENTER).perform()
        self.input(end_button, end)
        ActionChains(self.driver).send_keys_to_element(end_locator, Keys.ENTER).perform()

    def clear_log_date(self):
        self.hover('by_xpath,//input[@placeholder="结束日期"]')
        clear_button_locator = 'by_xpath,//i[contains(@class,"el-icon el-input__icon el-range__close-icon")]'
        try:
            if self.element_exist(clear_button_locator):
                self.click(clear_button_locator)
            else:
                print("操作日志清除按钮不可见")
        except InvalidSelectorException as e:
            raise e

    def add_new_shop(self, shop_name):
        self.switch_to_system_management()
        # 点击系统管理-组织架构-添加机构按钮
        self.add_org_icon()
        time.sleep(0.5)
        # 点击门店tab
        self.add_shop()
        time.sleep(0.5)
        # shop_name = "test门店"
        # 输入门店名称
        self.input_shop_name(shop_name)
        time.sleep(1)
        # 选择上级机构
        self.select_perent_org_shop()
        time.sleep(1)
        # 隐藏下拉框，去点击分支名称
        self.click_branch_name()
        # 点击确认按钮
        self.add_shop_submit_button()

    def del_new_shop(self):
        self.switch_to_system_management()
        del_new_shop_loca = ('by_xpath,//div[text()="test门店"]/following::img[2]')
        self.click(del_new_shop_loca)
        self.delete_org_confirm()

    def switch_to_system_setting(self):
        """
        切换到系统管理-系统设置tab上
        :return:
        """
        system_setting = 'by_xpath,//span[text()="系统设置"]'
        self.click(system_setting)

    # **************************横屏系统垫片操作***********************************
    def add_accross_system_spacer(self):
        """
        添加横屏系统垫片
        :return:
        """
        add_system_spacer_button = 'by_xpath,//div[@class="img-box imgBody"]/../input'
        # self.click(add_system_spacer_button)
        upload_file = self.get_element(add_system_spacer_button)
        time.sleep(2)
        system_file_path = r'D:\git\ui_test\data\system_spacer_accross.jpeg'
        upload_file.send_keys(system_file_path)

    def hover_to_accross(self):
        """
        鼠标hover到横屏系统垫片
        :return:
        """
        hover_to_accross = 'by_xpath,//div[@class="img-box imgBody"]'
        hover_to_accross_ele = self.get_element(hover_to_accross)
        ActionChains(self.driver).move_to_element(hover_to_accross_ele).perform()

    def preview_accross_system_spacer(self):
        """
        预览横屏系统垫片
        :return:
        """
        preview_system_spacer = 'by_xpath,//div[@class="mask1"]/img[1]'
        self.click(preview_system_spacer)

    def close_accross_preview(self):
        """
        关闭横屏系统垫片预览
        :return:
        """
        hover_preview = 'by_xpath,//div[@class="dialogImg"]'
        hover_preview_ele = self.get_element(hover_preview)
        ActionChains(self.driver).move_to_element(hover_preview_ele).perform()

        close_preview_button = 'by_xpath,//i[@class="el-icon closeBtn"]'
        if self.element_exist(close_preview_button):
            self.click(close_preview_button)

    def replace_accross_system_spacer(self):
        """
        更新横屏系统垫片
        """
        replace_system_spacer = 'by_xpath,//div[@class="img-box imgBody"]/../input'
        replace_system_spacer_ele = self.get_element(replace_system_spacer)
        replace_path = r'D:\git\ui_test\data\system_spacer_stand_1.jpg'
        replace_system_spacer_ele.send_keys(replace_path)

    def delete_accross_system_spacer(self):
        """
        删除横屏系统垫片
        :return:
        """
        delete_accross_system_spacer = 'by_xpath,//div[@class="mask1"]/img[3]'
        self.click(delete_accross_system_spacer)

    # **************************竖屏系统垫片操作***********************************

    def add_stand_system_spacer(self):
        """
        添加竖屏系统垫片
        :return:
        """
        add_stand_system_spacer_button = 'by_xpath,//div[@class="imgBody"]/../input'
        upload_file = self.get_element(add_stand_system_spacer_button)
        time.sleep(2)
        system_file_path = r'D:\git\ui_test\data\system_spacer_stand.jpeg'
        upload_file.send_keys(system_file_path)

    def hover_to_stand(self):
        """
        鼠标hover到竖屏系统垫片
        :return:
        """
        hover_to_stand = 'by_xpath,//div[@class="imgBody"]'
        hover_to_stand_ele = self.get_element(hover_to_stand)
        ActionChains(self.driver).move_to_element(hover_to_stand_ele).perform()

    def preview_stand_system_spacer(self):
        """
        预览竖屏系统垫片
        :return:
        """
        preview_stand_system_spacer = 'by_xpath,//div[@class="mask2"]/img[1]'
        self.click(preview_stand_system_spacer)

    def close_stand_preview(self):
        """
        关闭竖屏系统垫片预览
        :return:
        """
        hover_preview = 'by_xpath,//div[@class="dialogImg"]'
        hover_preview_ele = self.get_element(hover_preview)
        ActionChains(self.driver).move_to_element(hover_preview_ele).perform()

        close_preview_button = 'by_xpath,//i[@class="el-icon closeBtn"]'
        if self.element_exist(close_preview_button):
            self.click(close_preview_button)

    def replace_stand_system_spacer(self):
        """
        更新竖屏系统垫片
        """
        replace_system_spacer = 'by_xpath,//div[@class="imgBody"]/../input'
        replace_system_spacer_ele = self.get_element(replace_system_spacer)
        replace_path = r'D:\git\ui_test\data\system_spacer_stand_1.jpg'
        replace_system_spacer_ele.send_keys(replace_path)

    def delete_stand_system_spacer(self):
        """
        删除竖屏系统垫片
        :return:
        """
        delete_accross_system_spacer = 'by_xpath,//div[@class="mask2"]/img[3]'
        self.click(delete_accross_system_spacer)

    # ************************** 开发者tab页*********************************
    def switch_to_develops(self):
        """
        切换到开发者页面
        :return:
        """
        switch_to_develops = 'by_xpath,//span[text()="开发者"]'
        self.click(switch_to_develops)

    def click_gen_access_key(self):
        """
        点击重新生成
        :return:
        """
        get_access_key ='by_xpath,//span[text()="重新生成"]'
        self.click(get_access_key)

    def close_gen_access_key_alert(self):
        """
        关闭生成弹框
        :return:
        """
        close_gen_access_key = 'by_xpath,//i[@class="el-icon el-dialog__close"]'
        self.click(close_gen_access_key)

    def cancel_gen_access_key_alert(self):
        """
        取消重新生成key
        :return:
        """
        cancel_gen_button = 'by_xpath,//span[text()="取消"]'
        self.click(cancel_gen_button)

    def confirm_gen_access_key(self):
        """
        确认生成access key
        :return:
        """
        confirm_gen_access_key = 'by_xpath,//span[text()=" 确定 "]'
        self.click(confirm_gen_access_key)

    def copy_access_key(self):
        """
        复制access key,从剪贴板拿到key
        :return:
        """
        copy_access_key_button ='by_xpath,//img[@class="copy"]'
        self.click(copy_access_key_button)

        clipboard_content = pyperclip.paste()
        print("\n从剪贴板拿到的access key是：",clipboard_content)

        return None

    def return_access_key(self):
        """
        拿到access key
        :return:
        """
        access_key_locator = 'by_xpath,//span[@class="val"]'
        key = self.get_element(access_key_locator)
        access_key = key.text
        print("\n通过元素拿到的key是:",access_key)

    def download_dynamic_api_instruction(self):
        """
        动态数据API说明文件
        :return:
        """
        download_instruction_locator = 'by_xpath,//span[text()="动态数据API说明文件"]/../span[2]'
        self.click(download_instruction_locator)

    def download_dynamic_sdk_file(self):
        """
        下载动态数据SDK依赖包
        :return:
        """
        download_sdk_file = 'by_xpath,//span[text()="动态数据SDK依赖包"]/../span[2]'
        self.click(download_sdk_file)

    def download_dynamic_example_code(self):
        """
        下载动态数据调用样例代码
        :return:
        """
        download_dynamic_example_code ='by_xpath,//span[text()="动态数据调用样例代码"]/../span[2]'
        self.click(download_dynamic_example_code)

# ****************************** 选项维护tab页 *************************************************

    def switch_to_option_maintenance(self):
        """
        切换到选项维护tab页上
        :return:
        """
        option_maintenance ='by_xpath,//span[text()="选项维护"]'
        self.click(option_maintenance)

    def click_add_org_type_icon(self):
        """
        点击添加机构分类的加号
        :return:
        """
        add_org_type_icon = 'by_xpath,//i[@class="el-icon"]/*'
        add_eles = self.get_elements(add_org_type_icon)
        add_ele = add_eles[0]
        ActionChains(self.driver).click(add_ele).perform()
        # add_org_type_icon = 'by_xpath,//li[text()="机构分类"]/../li[2]/i'
        # self.click(add_org_type_icon)


    def input_org_type_description(self,description):
        """
        添加机构分类，输入分类描述
        :return:
        """
        org_type_description = 'by_xpath,//input[@placeholder="分类描述最多不超过10个字"]'
        self.input(org_type_description,description)

    def input_org_type_remark(self,remark):
        """
        输入机构分类备注
        :return:
        """
        org_type_remark = 'by_xpath,//input[@placeholder="备注最多不超过10个字"]'
        self.input(org_type_remark,remark)

    def edit_org_type(self):
        """
        修改机构分类，点击修改icon
        :return:
        """
        edit_org_type = 'by_xpath,//li[text()="机构分类"]/../../ul[2]/li[1]//img[1]'
        self.click(edit_org_type)

    def delete_org_type(self):
        """
        删除机构分类，点击删除icon
        :return:
        """
        delete_org_type = 'by_xpath,//li[text()="机构分类"]/../../ul[2]/li[1]//img[2]'
        self.click(delete_org_type)


#  ***************************机构级别**********************************************
    def click_add_org_level_icon(self):
        """
        点击添加机构级别的加号
        :return:
        """
        add_org_level_icon = 'by_xpath,//i[@class="el-icon"]/*'
        add_eles = self.get_elements(add_org_level_icon)
        add_ele = add_eles[1]
        ActionChains(self.driver).click(add_ele).perform()
        # add_org_level_icon = 'by_xpath,//li[text()="机构级别"]/../li[2]/i'
        # self.click(add_org_level_icon)


    def input_org_level_description(self,description):
        """
        添加机构级别，输入级别描述
        :return:
        """
        org_level_description = 'by_xpath,//input[@placeholder="级别描述最多不超过10个字"]'
        self.input(org_level_description,description)

    def input_org_level_remark(self,remark):
        """
        输入机构级别备注
        :return:
        """
        org_level_remark = 'by_xpath,//input[@placeholder="备注最多不超过10个字"]'
        self.input(org_level_remark,remark)

    def edit_org_level(self):
        """
        修改机构级别，点击修改icon
        :return:
        """
        edit_org_level = 'by_xpath,//li[text()="机构级别"]/../../ul[2]/li[1]//img[1]'
        self.click(edit_org_level)

    def delete_org_level(self):
        """
        删除机构级别，点击删除icon
        :return:
        """
        delete_org_level = 'by_xpath,//li[text()="机构级别"]/../../ul[2]/li[1]//img[2]'
        self.click(delete_org_level)

