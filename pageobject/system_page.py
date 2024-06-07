import time
import random

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
