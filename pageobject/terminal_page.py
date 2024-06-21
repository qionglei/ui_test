import random
import time

import pytest
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from basepage.base_page import BasePage
from common.set_up_terminal_list import Terminal_List
from conftest import env, env_conf
from allure_commons._allure import step


# @pytest.mark.usefixtures("env")
from data_clean import clear_terminal


class TerminalPage(BasePage):
    fixed_terminal_id = "TERMINAL_ID_0001"
    fixed_terminal_name = "TERMINAL_NAME_0001"

    def switch_to_terminal_center(self):
        terminal_center_loca = 'by_xpath,//div[text()=" 设备中心"]'
        focus = 'by_xpath,//div[text()=" 设备中心"]/../../.'
        focus_ele = self.get_element(focus)
        # focus_text = focus_ele.text
        focus_get = focus_ele.get_attribute("class")
        # print("设备中心是否可见呢？", focus_text)
        try:
            if focus_get == "el-tree-node is-focusable":
                self.click(terminal_center_loca)
            else:
                pass
        except:
            self.refresh()
            self.click(terminal_center_loca)

    def add_new_terminal(self):
        # sys_page.add_new_shop()
        # 进入设备中心
        try:
            self.switch_to_terminal_center()
            # self.refresh()
            # time.sleep(0.5)
            with step("点击设备接入"):
                self.click_bind_terminal()
            time.sleep(0.5)

            with step("输入设备sn码"):
                self.input_terminal_id(self.fixed_terminal_id)

            with step("输入设备名称"):
                self.input_terminal_name(self.fixed_terminal_name)

            with step("先点击所属机构"):
                self.terminal_org()

            with step("在下拉框展开组织架构"):
                self.terminal_org_more()
            time.sleep(0.5)

            with step("在下拉框进行选择"):
                self.select_terminal_org()
            time.sleep(0.5)

            with step("点击保存按钮"):
                self.click_terminal_id()
                self.confirm_bind_terminal()

            try:
                """
                当点击确定按钮时，归属机构有红字报错，则再次进行选择
                """
                red_error_text = self.element_exist('by_xpath,//div[@class="el-form-item__error" and text()="归属机构"]')
                if red_error_text:
                    with step("先点击所属机构"):
                        self.terminal_org()

                    with step("在下拉框展开组织架构"):
                        self.terminal_org_more()
                    time.sleep(0.5)

                    with step("在下拉框进行选择"):
                        self.select_terminal_org()
                    time.sleep(0.5)

                    with step("点击保存按钮"):
                        self.click_terminal_id()
                        self.confirm_bind_terminal()
            except NoSuchElementException:
                pass


            # with step("清理数据，删除之前添加的门店"):
            #     sys_page.del_new_shop()

            # single = 'by_xpath,//div[text()="单个接入"]'
            # # self.element_exist(single)
            # if not self.element_exist(single):
            #     pass
            # else:
            #     self.cancel_bind_terminal()

        except Exception:
            raise

    def click_bind_terminal(self):
        time.sleep(0.5)
        bind_terminal_loca = ('by_xpath,//span[text()="设备接入"]')
        self.click(bind_terminal_loca)

    def click_terminal_id(self):
        input_terminal_id_loca = ('by_xpath,//input[@placeholder="请输入设备ID"]')
        self.click(input_terminal_id_loca)

    def input_terminal_id(self, sn_id):
        input_terminal_id_loca = ('by_xpath,//input[@placeholder="请输入设备ID"]')
        self.input(input_terminal_id_loca, sn_id)

    def click_terminal_name(self):
        input_terminal_name_loca = ('by_xpath,//input[@placeholder="请输入设备名称"]')
        self.click(input_terminal_name_loca)

    def input_terminal_name(self, sn_name):
        input_terminal_name_loca = ('by_xpath,//input[@placeholder="请输入设备名称"]')
        self.input(input_terminal_name_loca, sn_name)

    def terminal_org(self):
        """
        点击请选择按钮
        """
        terminal_org_loca = ('by_xpath,//label[text()="归属机构"]/..//input[@placeholder="请选择"]')
        self.click(terminal_org_loca)

    def terminal_org_more(self):
        """
        展开组织架构
        """
        terminal_org_more_loca = ('by_xpath,//i[@class="el-icon arrow-right el-cascader-node__postfix"]')
        terminal_org_more_eles = self.get_elements(terminal_org_more_loca)
        # print("terminal_org_more_eles:",terminal_org_more_eles)
        first_terminal_org_more_ele = terminal_org_more_eles[0]
        ActionChains(self.driver).move_to_element(first_terminal_org_more_ele).click(first_terminal_org_more_ele).perform()

    def select_terminal_org(self):
        """
        选择一个门店，进行点击
        """
        time.sleep(0.5)
        clickable_locators = ('by_xpath,//label[@class="el-radio"]')
        # clickable_eles = self.get_elements(clickable_locator)
        # clickable_ele = clickable_eles[0]
        # ActionChains(self.driver).move_to_element(clickable_ele).click(clickable_ele).click()

        clickable_eles = self.get_elements(clickable_locators)
        try:
            if clickable_eles:
                first_clickable_ele = clickable_eles[0]
                ActionChains(self.driver).move_to_element(first_clickable_ele).click(first_clickable_ele).perform()
                self.click_terminal_id()
        except IndexError:
            raise

    def confirm_bind_terminal(self):
        confirm_bind_terminal_button_loca = ('by_xpath,//span[text()=" 确定 "]')
        self.click(confirm_bind_terminal_button_loca)
        terminal_id = "terminal_002"
        fail_toast_loca = ('by_xpath,//p[text()="接入失败：设备已被绑定"]')
        if self.element_exist(fail_toast_loca):
            clear_terminal()
            self.click(confirm_bind_terminal_button_loca)

            # self.input_terminal_id(terminal_id)
            # # self.click_terminal_id()
            # time.sleep(0.5)
            # self.click(confirm_bind_terminal_button_loca)

            # 如果设备已被绑定，则判断是不是在当前机构-设备列表中
            terminal_list = Terminal_List()
            all_terminal = terminal_list.get_terminal_list()
            # if input_terminal_id in all_terminal:
            #     pass


        if self.element_exist('by_xpath,//div[@class="el-form-item__error" and text()="归属机构"]'):
            # 先点击所属机构
            self.terminal_org()

            # 在下拉框展开组织架构
            self.terminal_org_more()
            time.sleep(0.5)
            # 在下拉框进行选择
            self.select_terminal_org()
            time.sleep(0.5)
            # 点击保存按钮
            self.click_terminal_id()
            time.sleep(0.5)
            self.confirm_bind_terminal()

        # ids= self.all_terminal_ids
        # print("获取到的所有设备id是：",ids)
        # if id in ids:
        #     print("terminal_002在列表中",id.text)
        # else:
        #     print("terminal_id_0001")

    def cancel_bind_terminal(self):
        cancel_bind_terminal_loca = ('by_xpath,//span[text()="取消"]')
        self.click(cancel_bind_terminal_loca)

    def bind_terminal(self):
        self.click_bind_terminal()
        sn_id = random.randint(1, 100000)
        self.input_terminal_id(sn_id)
        time.sleep(0.5)
        sn_name = "test" + str(sn_id)
        self.input_terminal_name(sn_name)
        self.terminal_org()
        self.terminal_org_more()
        self.select_terminal_org()
        self.click_terminal_id()
        self.confirm_bind_terminal()
        time.sleep(1)
        # 兼容已被绑定的情况
        single = 'by_xpath,//div[text()="单个接入"]'
        # self.element_exist(single)
        if self.element_exist(single):
            self.cancel_bind_terminal()

    def click_terminal_setting(self):
        terminal_setting_loca = ('by_xpath,//img[@title="设置"]')
        self.click(terminal_setting_loca)

    # 指定设备的设置，待实现
    # def click_terminal_setting(self):
    #     terminal_setting_loca = ('by_xpath,//div[text()="{}"]/../../td[11]//img[@title="设置"]')
    #     self.click(terminal_setting_loca)

    def save_terminal_setting(self):
        save_terminal_loca = ('by_xpath,//span[text()=" 保存 "]')
        self.click(save_terminal_loca)

    def cancel_terminal_setting(self):
        cancel_terminal_loca = ('by_xpath,//span[text()=" 取消 "]')
        self.click(cancel_terminal_loca)

    def rename_terminal(self, rename_terminal):
        terminal_name = ('by_xpath,//input[@placeholder="请输入设备名称"]')
        self.clear(terminal_name)
        self.input(terminal_name, rename_terminal)

    def change_terminal_org(self):
        terminal_org = ('by_xpath,//label[text()="所属机构"]/following::input[1]')

    def add_real_terminal(self):
        clear_terminal()
        self.refresh()
        try:
            config_terminal = env_conf()
            # print("config_terminal的值是：*****************",config_terminal)
            # print("config_terminal的值类型是：*****************", type(config_terminal))
            # print("config_terminal的id是：*****************", config_terminal["test_terminal_id"])
            # print("config_terminal的id是：*****************", config_terminal["test_terminal_name"])

            real_terminal_id = config_terminal["test_terminal_id"]
            real_terminal_name = config_terminal["test_terminal_name"]
            # # real_terminal_id = env_config["test_terminal_id"]
            # # real_terminal_name = env_config["test_terminal_name"]
            # sys_page.add_new_shop()
            with step("进入设备中心"):

                self.switch_to_terminal_center()
                time.sleep(0.5)

            with step("点击设备接入"):
                self.click_bind_terminal()
                time.sleep(0.5)
            with step("输入设备sn码"):
                self.input_terminal_id(real_terminal_id)
                time.sleep(0.5)
            with step("输入设备名称"):
                self.input_terminal_name(real_terminal_name)
                time.sleep(0.5)
            with step("先点击所属机构"):
                self.terminal_org()
                time.sleep(0.5)
            with step("在下拉框展开组织架构"):
                self.terminal_org_more()
                time.sleep(1)
            with step("在下拉框进行选择"):
                self.select_terminal_org()
                time.sleep(1)
            with step("点击保存按钮"):
                self.click_terminal_id()
                self.confirm_bind_terminal()
            time.sleep(0.5)
            single = 'by_xpath,//div[text()="单个接入"]'
            # self.element_exist(single)
            # 如果设备已被绑定，则调用数据库进行清理，再进行绑定操作
            if self.element_exist(single):
                # self.cancel_bind_terminal()
                clear_terminal()
                self.refresh()

                with step("点击设备接入"):
                    self.click_bind_terminal()
                    time.sleep(0.5)
                with step("输入设备sn码"):
                    self.input_terminal_id(real_terminal_id)
                    time.sleep(0.5)
                with step("输入设备名称"):
                    self.input_terminal_name(real_terminal_name)
                    time.sleep(0.5)
                with step("先点击所属机构"):
                    self.terminal_org()
                    time.sleep(0.5)
                with step("在下拉框展开组织架构"):
                    self.terminal_org_more()
                    time.sleep(1)
                with step("在下拉框进行选择"):
                    self.select_terminal_org()
                    time.sleep(1)
                with step("点击保存按钮"):
                    self.click_terminal_id()
                    self.confirm_bind_terminal()

        except ElementNotInteractableException as e:
            raise e

    # ++++++++++++++++++++++++++++++++删除设备相关+++++++++++++++++++++++++++++++++

    def click_delete_terminal(self):
        delete_terminal_loca = ('by_xpath,//img[@title="删除"]')
        self.click(delete_terminal_loca)

    def cancel_delete_terminal(self):
        cancel_delete_terminal_loca = ('by_xpath,//span[text()="取消"]')
        self.click(cancel_delete_terminal_loca)

    def success_delete_terminal(self):
        confirm_delete_terminal_button_loca = ('by_xpath,//span[text()="确定"]')
        self.click(confirm_delete_terminal_button_loca)

    # ++++++++++++++++++++++++++++++++搜索设备相关+++++++++++++++++++++++++++++++++

    def search_terminal_by_id(self, terminal_id):
        terminal_id_loca = ('by_xpath,//input[@placeholder="输入ID或者名称"]')
        # self.click(terminal_id_loca)
        self.input(terminal_id_loca, terminal_id)

    def search_terminal_clear(self, terminal_id):
        terminal_id_loca = ('by_xpath,//input[@placeholder="输入ID或者名称"]')
        # self.click(terminal_id_loca)
        self.clear(terminal_id_loca)

    def click_search_terminal_button(self):
        terminal_search_button_loca = ('by_xpath,//button[@class="el-button"]')
        # self.click(terminal_search_button_loca)
        search_button_ele = self.get_element(terminal_search_button_loca)
        ActionChains(self.driver).move_to_element(search_button_ele).click(search_button_ele).perform()

    # 获取所有的设备id
    def all_terminal_ids(self):
        all_terminal_ids = ('by_xpath,//div[@class="cell el-tooltip"]/span')
        e1 = self.get_elements(all_terminal_ids)
        all_ids = []
        for e in e1:
            # all_text =e.get_attribute("color")
            all_text = e.text
            all_ids.append(all_text)
        print("获取到的设备列表为：", all_ids)
        return all_ids

    # ++++++++++++++++++++++++++++++++更多功能+++++++++++++++++++++++++++++++++
    def click_more_button(self):
        more_button_loca = ('by_xpath,//img[@title="更多"]')
        self.click_button(more_button_loca)

    def more_function(self):
        more_function_1_loca = ('by_xpath,//div[@class="popover-cont"]/div[@class="popover-item"]')
        more_functions_1 = self.get_elements(more_function_1_loca)
        all_function_1 = []
        for function in more_functions_1:
            all_function_1.append(function.text)
        print("获取到的更多功能下面,第一行的所有按钮文案是:", all_function_1)
        # all_function_1 = all_function_1[3:7]

        more_function_2_loca = ('by_xpath,//div[@class="popover-cont"]/div[@class="popover-item bottom"]/div/div')
        more_function_2 = self.get_elements(more_function_2_loca)
        all_function_2 = []
        for function in more_function_2:
            all_function_2.append(function.text)
        print("获取到的更多功能下面，第二行的所有按钮文案是：", all_function_2)
        all_function = all_function_1 + all_function_2
        # 去掉空字符串
        all_functions = list(filter(None, all_function))

        return all_functions

    def rechange_terminal_org(self):
        terminal_org_loca = ('by_xpath,//label[text()="音量设置"]/preceding::input[@placeholder="请选择" and not(@ role)]')
        self.click(terminal_org_loca)
        org_more_loca = ('by_xpath,//ul[@class="el-scrollbar__view el-cascader-menu__list"]//i')
        self.click(org_more_loca)
        choice_org_Loca = ('by_xpath,//span[text()="门店002"]')
        self.click(choice_org_Loca)
        self.click_terminal_id()
        confirm_button_loca = ('by_xapth,//span[text()=" 保存 "]')
        self.click(confirm_button_loca)

    def rechange_terminal_label(self):
        terminal_label_loca = ('by_xpath,//input[@placeholder="请选择标签"]')
        self.click(terminal_label_loca)

    def turn_off_terminal(self):
        turn_off_button_loca = ('by_xpath,//div[text()="关机"]')
        self.click(turn_off_button_loca)

    def restart_terminal(self):
        turn_off_button_loca = ('by_xpath,//div[text()="重启"]')
        self.click(turn_off_button_loca)

    def play_terminal(self):
        play_terminal_button_loca = ('by_xpath,//div[text()="播放"]')
        self.click(play_terminal_button_loca)

    def stop_terminal(self):
        stop_terminal_button_loca = ('by_xpath,//div[text()="停止"]')
        self.click(stop_terminal_button_loca)

    def real_time_monitor(self):
        real_time_monitor_loca = ('by_xpath,//div[text()="实时监控"]')
        self.click(real_time_monitor_loca)

    def insert_subtitle(self):
        try:
            insert_subtitle_loca = ('by_xpath,//div[@class="el-popper is-light el-popover"][2]//div[text()="插播字幕"]')
            self.click(insert_subtitle_loca)
        except:
            raise

    def close_insert_subtitle(self):
        insert_subtitle_close_button_loca = ('by_xpath,//button[@aria-label="el.dialog.close"]')
        self.click(insert_subtitle_close_button_loca)

    def program_clone(self):
        program_clone_loca = ('by_xpath,//div[text()="节目克隆"]')
        self.click(program_clone_loca)

    def cancel_program_clone(self):
        cancel_clone_button_loca = ('by_xpath,//span[text()=" 取消 "]')
        self.click(cancel_clone_button_loca)

    def click_insert_subtitle_text(self):
        subtitle_text_loca = ('by_xpath,//textarea[@placeholder="请输入插播内容"]')
        self.click(subtitle_text_loca)

    def input_insert_subtitle_text(self, text):
        subtitle_text_loca = ('by_xpath,//textarea[@placeholder="请输入插播内容"]')
        self.input(subtitle_text_loca, text)

    def insert_subtitle_submit(self):
        insert_subtitle_submit_button_loca = ('by_xpath,//span[text()=" 保存 "]')
        self.click(insert_subtitle_submit_button_loca)

    def insert_subtitle_position_median(self):
        position_median_loca = ('by_xpath,//span[@class="el-radio__label" and text()="中"]')
        self.click(position_median_loca)

    def insert_subtitle_position_up(self):
        position_up_loca = 'by_xpath,//span[@class="el-radio__label" and text()="上"]'
        self.click(position_up_loca)

    def insert_subtitle_position_down(self):
        position_down_loca = 'by_xpath,//span[@class="el-radio__label" and text()="下"]'
        self.click(position_down_loca)

    def insert_subtitle_circle_times(self, times):
        circle_times = 'by_xpath,//input[@placeholder="请输入循环次数"]'
        self.input(circle_times, times)

    def select_all_terminal(self):
        select_all_terminal_locator = 'by_xpath,//div[text()="设备ID"]/preceding::span[@class="el-checkbox__inner"]'
        self.click(select_all_terminal_locator)

    def select_one_terminal(self):
        select_one_terminal_locator = 'by_xpath,//div[text()="设备ID"]/following::span[@class="el-checkbox__inner"]'
        self.click(select_one_terminal_locator)

    # +++++++++++++++++++++++++++++设备的批量操作+++++++++++++++++++++++++++++++++

    def click_terminal_control(self):
        self.click_button('by_xpath,//span[text()="设备控制"]')

    def batch_dispaly(self):
        self.click_button('by_xpath,//span[text()="播放"]')

    def batch_stop(self):
        self.click_button('by_xpath,//span[text()="停止"]')

    def terminal_info(self):
        self.click('by_xpath,//tr[@class="el-table__row"]/td[2]/div/span')

    def close_terminal_info(self):
        self.click('by_xpath,//i[@class="el-icon el-dialog__close"]')

    # ++++++++++++++++++++++++++++++++组织架构相关+++++++++++++++++++++++++++++++++

    def click_terminal_org_tree(self):
        """
        点击组织架构树
        """
        current_win = self.get_window_size()
        try:
            self.click('by_xpath,//div[@class="org-btn"]/span[text()="组织架构"]')
        except ElementClickInterceptedException as e:
            raise e
        self.set_window_size(*current_win)

    def terminal_group_tab(self):
        self.click('by_xpath,//li[@class="active"]/span')

    def terminal_org_tab(self):
        self.click('by_xpath,//div[@class="drawer-box"]//span[text()="组织架构"]')

    # ++++++++++++++++++++++++++++++++播放列表相关+++++++++++++++++++++++++++++++++
    def click_play_bill(self):
        self.click('by_xpath,//img[@title="节目"]')

    def program_list_tab(self):
        self.click('by_xpath,//span[text()="节目列表"]')

    def play_bill_tab(self):
        self.click('by_xpath,//span[text()="播放列表"]')

    def click_play_bill_date(self):
        self.click('by_xpath,//input[@placeholder="请选择日期"]')

    def input_play_bill_date(self, datetime):
        play_bill_date_locator = 'by_xpath,//input[@placeholder="请选择日期"]'
        self.input(play_bill_date_locator, datetime)

    def clear_all_terminal(self):
        all_delete_button = 'by_xpath,//img[@title="删除"]'
        all_delete = self.get_elements(all_delete_button)
        for e in all_delete:
            self.click(e)
