# -*- coding: utf-8 -*-
import time
import random
from time import sleep

import allure
import pytest
from allure_commons._allure import step
from selenium.webdriver import ActionChains

from common.set_up_media_list import MediaList
from common.set_up_program_list import ProgramList
from common.set_up_terminal_list import Terminal_List
from conftest import driver
from pageobject.media_page import MediaPage
from pageobject.program_page import ProgramPage
from pageobject.release_page import ReleasePage
from pageobject.system_page import SystemPage
from pageobject.terminal_page import TerminalPage


@pytest.fixture(scope='class')
def release_page(request, driver):
    release_page = ReleasePage(driver)
    request.cls.release_page = release_page
    # window_size = release_page.get_window_size()
    # release_page.maxsize_window()
    yield release_page
    # release_page.set_window_size(*window_size)
    # driver.close()


# @pytest.fixture()
# def terminal_page(request, driver):
#     terminal_page = TerminalPage(driver)
#     request.cls.terminal_page = terminal_page
#     yield terminal_page


# @pytest.mark.usefixtures("terminal_page")
@pytest.fixture(scope="class")
def add_terminal():
    terminal_page = TerminalPage(driver)
    terminal_list = Terminal_List()
    terminal_ids = terminal_list.get_terminal_list()

    print("设备列表是***********：", terminal_ids)
    time.sleep(3)

    if not terminal_ids:
        print("进行执行了.......")
        terminal_page.switch_to_terminal_center()
        terminal_page.bind_terminal()
    else:
        print("列表不为空")


# @pytest.fixture(scope='class')
# def system_page(request, driver):
#     system_page = SystemPage(driver)
#     request.cls.system_page = system_page
#     yield system_page


@pytest.fixture()
def generate_program(driver):
    """
    1、判断素材中心是不是有素材，有就先清空，再上传，再生成节目
    2、没有就直接上传，再生成节目
    :return:
    """

    media_list = MediaList()
    mediapage = MediaPage(driver)
    media_ids, folder_ids = media_list.get_media_list()
    programlist = ProgramList()
    program_names = programlist.get_program_list_names()

    if program_names == []:
        if media_ids == []:
            # 素材上传
            mediapage.switch_to_media_center()
            mediapage.upload_media()
            time.sleep(2)
            # 素材发布
            # media_ids, folder_ids = media_list.get_media_list()
            mediapage.hover_to_media()
            mediapage.choose_media()
            mediapage.multi_release()
        else:
            media_list.delete_all_media()
            mediapage.switch_to_media_center()
            mediapage.upload_media()
            time.sleep(2)
            mediapage.hover_to_media()
            mediapage.choose_media()
            mediapage.multi_release()


@allure.epic("项目hkc")
@allure.feature("release management")
@pytest.mark.usefixtures("release_page")
class TestReleaseStrategy:
    """
    选择策略相关
    """
    terminal_list = Terminal_List()

    @pytest.mark.run(order=1)
    @allure.title("发布策略，选择静音播放")
    def test_silence_strategy(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择静音播放：是"):
            release_page.is_silence("True")

        with step("点击确定按钮"):
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=2)
    @allure.title("发布策略，选择不静音播放")
    def test_not_silence_strategy(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择静音播放：否"):
            release_page.is_silence("False")

        with step("点击确定按钮"):
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=3)
    @allure.title("发布策略，选择优先级为: 高")
    def test_priority_high(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择播放优先级：高"):
            release_page.display_priority(1)

        with step("点击确定按钮"):
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=4)
    @allure.title("发布策略，选择优先级为: 低")
    def test_priority_low(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择播放优先级：低"):
            release_page.display_priority(3)

        with step("点击确定按钮"):
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=5)
    @allure.title("发布策略，选择发布策略： 覆盖")
    def test_strategy_cover(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择发布策略： 覆盖"):
            release_page.display_strategy(1)

        with step("点击确定按钮"):
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=6)
    @allure.title("发布策略，选择发布策略： 追加")
    def test_strategy_add(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择发布策略： 追加"):
            release_page.display_strategy(2)

        with step("点击确定按钮"):
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=7)
    @allure.title("发布策略，取消发布")
    def test_dismiss_strategy(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择发布策略： 追加"):
            release_page.display_strategy(2)

        with step("点击取消按钮"):
            release_page.dismiss_release_strategy()

    @pytest.mark.run(order=8)
    @allure.title("发布策略，关闭发布")
    def test_close_strategy(self):
        release_page = self.release_page
        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("点击选择策略"):
            release_page.selection_strategy()

        with step("选择发布策略： 追加"):
            release_page.display_strategy(2)

        with step("点击取消按钮"):
            release_page.close_relase_strategy()

    @pytest.mark.skip(">           terminal_page.switch_to_terminal_center()")
    @pytest.mark.run(order=8)
    @pytest.mark.usefixtures("add_terminal")
    # @pytest.mark.usefixtures("terminal_page")
    @allure.title("发布管理：选择一个设备")
    def test_choose_terminal_release(self):
        # terminal_page =self.terminal_page
        release_page = self.release_page
        # self
        # with step("先判断设备列表是不是有设备，无则pass，有则添加"):
        #     terminal_ids = terminal_list()
        #     print("设备列表是***********：", terminal_ids)
        #     time.sleep(3)
        #
        #     if not terminal_ids:
        #         print("进行执行了.......")
        #         terminal_page.switch_to_terminal_center()
        #         terminal_page.bind_terminal()
        #     else:
        #         print("列表不为空")
        # time.sleep(3)
        with step("切换到发布管理tab页"):
            release_page.switch_to_release_management()

        time.sleep(3)
        with step("点击选设备"):
            release_page.choose_terminal()

        time.sleep(3)
        with step("选择一个设备"):
            release_page.choose_one_terminal()

        with step("选完设备后，点击确定"):
            release_page.confirm_release_strategy()

    # @allure.epic("项目hkc")
    # @allure.feature("release management2")
    # @pytest.mark.usefixtures("release_page")
    # class TestReleaseManagemen_2:
    # terminal_list = Terminal_List()

    @pytest.mark.run(order=9)
    @allure.title("选设备，切换到设备分组，再切到组织架构")
    def test_switch_terminal_group(self):
        release_page = self.release_page
        # terminal_page =self.terminal_page
        # terminal_list =self.terminal_list

        # with step("切换到发布管理上"):
        #     release_page.switch_to_release_management()
        #
        # with step("先判断设备列表是不是有设备，无则pass，有则添加"):
        #     terminal_ids = terminal_list.get_terminal_list()
        #     print("设备列表是***********：", terminal_ids)
        #     time.sleep(3)
        #
        #     if not terminal_ids:
        #         print("进行执行了.......")
        #         terminal_page.switch_to_terminal_center()
        #         terminal_page.bind_terminal()
        #     else:
        #         print("列表不为空")
        # time.sleep(3)

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("切到设备分组tab"):
            release_page.switch_terminal_group()

        with step("切到组织架构tab"):
            release_page.switch_terminal_framework()

    @pytest.mark.run(order=10)
    @allure.title("通过设备id，来搜索设备")
    def test_search_terminal_by_id(self):
        release_page = self.release_page
        release_page.refresh()
        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("点击到搜索框上"):
            release_page.release_search_terminal("测试id，后期进行优化")

        with step("点击确定按钮"):
            release_page.click_submit_button()

    @pytest.mark.run(order=11)
    @allure.title("通过设备名称，来搜索设备")
    def test_search_terminal_by_name(self):
        release_page = self.release_page
        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("点击到搜索框上,输入设备id"):
            release_page.release_search_terminal("测试名称，后期进行优化")

        with step("点击确定按钮"):
            release_page.click_submit_button()

    @pytest.mark.skip(reason="清空元素时，元素不可见")
    @pytest.mark.run(order=12)
    @allure.title("清空搜索")
    def test_clear_search_terminal(self):
        release_page = self.release_page
        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("点击到搜索框上，输入设备名称"):
            release_page.release_search_terminal("测试名称，后期进行优化")

        with step("在输入框中，点击回车键，来确认搜索"):
            release_page.enter_keyboard(driver)

        time.sleep(5)

        with step("进行清空操作"):
            release_page.clear_search(driver)

    @allure.title("全选设备")
    @pytest.mark.run(order=13)
    def test_select_all_terminal(self):
        release_page = self.release_page
        release_page.refresh()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("点击全选按钮"):
            release_page.select_all_terminals()

    @allure.title("清空设备")
    @pytest.mark.run(order=14)
    def test_clear_all_terminal(self):
        release_page = self.release_page
        win_size = release_page.get_window_size()
        release_page.maxsize_window()
        release_page.refresh()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        time.sleep(0.5)
        with step("点击选设备"):
            release_page.choose_terminal()

        with step("点击全选按钮"):
            release_page.select_all_terminals()

        with step("点击清空按钮"):
            release_page.clear_all_terminal()

        release_page.set_window_size(*win_size)

    @allure.title("在选设备抽屉，切换到‘设备分组’tab上")
    @pytest.mark.run(order=15)
    def test_switch_terminal_group(self):
        release_page = self.release_page

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        time.sleep(0.3)
        with step("点击选设备"):
            release_page.choose_terminal()

        with step("切换到设备分组tab上"):
            release_page.switch_terminal_group()

        time.sleep(0.3)
        with step("切换到组织架构tab上"):
            release_page.switch_terminal_framework()

    @allure.title("切换交并集")
    @pytest.mark.run(order=16)
    def test_switch_union_set(self):
        release_page = self.release_page
        release_page.refresh()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("切换到设备分组tab上"):
            release_page.switch_terminal_group()

        with step("切换到并集"):
            release_page.switch_union_set()

        with step("切换到交集"):
            release_page.switch_union_set()

    @allure.title("从选设备，跳转到‘节目编排’")
    @pytest.mark.run(order=17)
    def test_switch_program_edit(self):
        release_page = self.release_page
        release_page.refresh()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        time.sleep(1)
        with step("点击节目编排按钮，切换到节目编排上"):
            release_page.switch_program_edit()

    @allure.title("展开所有的机构")
    @pytest.mark.run(order=18)
    def test_expand_all_org(self, driver):
        release_page = self.release_page
        release_page.refresh()
        release_page.maxsize_window()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("点击选择全部机构"):
            release_page.select_all_org()

    @allure.title("折叠所有的机构")
    @pytest.mark.run(order=19)
    def test_collapsible_all_org(self, driver):
        release_page = self.release_page
        release_page.maxsize_window()
        release_page.refresh()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        time.sleep(0.5)
        with step("点击选设备"):
            release_page.choose_terminal()

        with step("点击选择全部机构"):
            release_page.select_all_org()

        time.sleep(3)
        with step("点击选择折叠机构"):
            release_page.select_all_org()

    @allure.title("取消选择所有的机构")
    @pytest.mark.run(order=20)
    def test_deselect_all_org(self, driver):
        release_page = self.release_page
        release_page.refresh()
        release_page.maxsize_window()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("在组织架构中，点击全选按钮，取消全选"):
            release_page.select_all_org()

    @allure.title("选择所有的机构")
    @pytest.mark.run(order=21)
    def test_select_all_org(self, driver):
        release_page = self.release_page
        release_page.refresh()
        release_page.maxsize_window()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step("点击选设备"):
            release_page.choose_terminal()

        with step("在组织架构中，点击全选按钮"):
            release_page.select_all_org()
            time.sleep(3)
            release_page.select_all_org()

    # ============================节目编排================================
    @staticmethod
    def get_start_end_time():
        from datetime import datetime, timedelta

        # 获取今天10点的时间
        today_start = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
        start_date = today_start.strftime('%Y-%m-%d %H:%M:%S')

        # 获取明天12点的时间
        tomorrow_start = (today_start + timedelta(days=1)).replace(hour=12, minute=0, second=0, microsecond=0)
        end_date = tomorrow_start.strftime('%Y-%m-%d %H:%M:%S')
        return start_date, end_date

    # pytest.mark.skip("结束时间处报错")
    @allure.title("节目编排中，选择日期")
    @pytest.mark.run(order=22)
    def test_set_display_date(self):
        release_page = self.release_page
        release_page.refresh()

        start_date, end_date = self.get_start_end_time()
        print("aaaaaaaaaaaaaaaa", start_date, end_date)

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("输入开始时间"):
            time.sleep(5)
            release_page.program_display_start_date(start_date)
            time.sleep(5)
            release_page.program_edit()
            release_page.program_display_end_date(end_date)

    # ======================时间周期，周几播放==================================
    @allure.title("取消选择周几播放")
    @pytest.mark.run(order=23)
    def test_cancel_weekly_display(self):
        release_page = self.release_page
        release_page.refresh()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击日期编排上面加号，唤起弹框"):
            release_page.click_weekly()

        with step("选择周五"):
            release_page.set_every_friday_display()

        with step("点击取消按钮"):
            release_page.cancel_program_edit()

    weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

    @pytest.mark.run(order=24)
    @pytest.mark.parametrize("weekly", weekday)
    @allure.title("设置每周一到周日，每天都播放")
    def test_every_monday_display(self, weekly):
        release_page = self.release_page
        release_page.refresh()
        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击日期编排上面加号，唤起弹框"):
            release_page.click_weekly()

        with step("依次选择周一到周日"):
            release_page.set_iterable_monday_display(weekly)
            time.sleep(3)
        with step("点击保存按钮"):
            release_page.save_program_edit()

        with step("点击确定按钮"):
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=25)
    @allure.title("设置时间段1，随机时间播放")
    def test_set_time_line(self):
        release_page = self.release_page
        release_page.refresh()
        start_time, end_time = release_page.generate_random_times_with_diff()
        print(start_time)
        print(end_time)
        print(f"开始时间: {start_time.strftime('%H:%M')}")
        print(f"结束时间: {end_time.strftime('%H:%M')}")
        start_time = str(start_time.strftime('%H:%M'))
        end_time = str(end_time.strftime('%H:%M'))

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("时间轴上面，点击加号按钮"):
            release_page.add_time_line()

        time.sleep(5)
        with step("输入开始时间"):
            release_page.time_line_start_time(start_time)

        time.sleep(5)
        with step("输入结束时间"):
            release_page.time_line_end_time(end_time)

        with step("点击确定按钮"):
            release_page.sumbit_span()

        with step("点击到时间轴上面，进行查看"):
            release_page.click_timeline()

    @pytest.mark.skip("没写好报错了")
    @pytest.mark.run(order=26)
    @allure.title("设置时间段1，固定时间播放")
    def test_set_fixed_time_line(self):
        release_page = self.release_page
        release_page.refresh()
        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("时间轴上面，点击加号按钮"):
            release_page.add_time_line()

        time.sleep(5)
        with step("输入开始时间"):
            release_page.fixed_start_time_line()

        time.sleep(5)
        with step("输入结束时间"):
            release_page.fixed_end_time_line()

        with step("点击确定按钮"):
            release_page.sumbit_span()

    @pytest.mark.run(order=27)
    @allure.title("保存为标签")
    def test_save_as_label(self, driver):
        release_page = self.release_page
        release_page.refresh()
        release_page.maxsize_window()
        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击保存为标签按钮"):
            release_page.click_save_as_label()

        with step("输入标签名称"):
            release_page.set_label_name("标签001")

        with step("点击保存按钮"):
            release_page.save_program_edit()
            release_page.confirm_release_strategy()

    @pytest.mark.run(order=28)
    # @pytest.mark.usefixtures("generate_program")
    @allure.title("在节目编排中，选择节目")
    def test_add_program(self, driver):
        # ---------前提-----------------
        # 后期优化：将这段代码作为fixture

        media_list = MediaList()
        mediapage = MediaPage(driver)
        mediapage.refresh()
        media_ids, folder_ids = media_list.get_media_list()
        media_list.delete_all_media()
        programlist = ProgramList()
        program_names = programlist.get_program_list_names()
        print("所有的节目名称:", program_names)

        if not program_names:
            # if media_ids is None:
            # 素材上传
            mediapage.refresh()
            mediapage.switch_to_media_center()
            mediapage.upload_media()
            print("上传成功------------------")
            time.sleep(2)
            # 素材发布
            # media_ids, folder_ids = media_list.get_media_list()
            mediapage.hover_to_media()
            mediapage.choose_media()
            mediapage.multi_release()
            print("发布成功------------------")
        else:
            # 清空所有的节目，然后再生成
            media_list.delete_all_media()
            mediapage.switch_to_media_center()
            mediapage.upload_media()
            time.sleep(2)
            mediapage.hover_to_media()
            mediapage.choose_media()
            mediapage.multi_release()

        # ---------------前提-结束---------------

        release_page = self.release_page
        release_page.refresh()
        release_page.maxsize_window()

        program_page = ProgramPage(driver)
        program_list_class = ProgramList()

        with step("切换到发布管理tab上"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        # with step("通过接口，拿到节目列表中所有的节目名称"):
        #     program_list_all = program_list_class.get_program_list_names()
        #     print("所有的节目名名称为",program_list_all)
        #     program_name = program_list_all[0]
        #     print("拿到的第一个的节目名名称为", program_name)
        #     time.sleep(0.5)
        with step("鼠标hover到一个节目上面"):
            mediapage.hover_to_media()
            time.sleep(0.5)
        try:
            with step("选择一个节目"):
                release_page.choose_program_and_choice()
                time.sleep(0.5)
        except IndexError as e:
            print("当前列表无节目")
            raise e

        with step("点击保存按钮"):
            time.sleep(2)
            release_page.sumbit_span()

    @pytest.mark.run(order=29)
    @allure.title("节目编排-选节目-筛选普通节目")
    def test_filter_general_program(self, driver):
        release_page = self.release_page
        release_page.refresh()
        # 前提：生成一个普通节目

        program_page = ProgramPage(driver)
        program_page.switch_to_program_management()
        program_page.create_general_program()

        with step("切到发布管理"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        with step("点击节目分类：普通"):
            release_page.general_program_type()

        # 进行断言
        labellocator = 'by_xpath,//div[@class="tag s3" and text()="普通"]'
        bool_ture = release_page.element_exist(labellocator)
        assert labellocator

    @pytest.mark.run(order=30)
    @allure.title("节目编排-选节目-筛选简单节目")
    def test_filter_simple_program(self, driver):
        media_list = MediaList()
        media_list.delete_all_media()
        release_page = self.release_page
        release_page.refresh()
        # 前提：1、生成一个简单节目
        #      2、发布简单节目

        media_page = MediaPage(driver)
        media_page.switch_to_media_center()
        media_page.upload_media()
        #      2、发布简单节目
        media_page.hover_to_media()
        media_page.choose_media()
        media_page.multi_release()

        with step("切到发布管理"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        with step("点击节目分类：简单"):
            release_page.simple_program_type()

        # 进行断言
        labellocator = 'by_xpath,//div[@class="tag s3" and text()="简单"]'
        bool_ture = release_page.element_exist(labellocator)
        assert labellocator

    @pytest.mark.run(order=31)
    @allure.title("节目编排-选节目-筛选横屏节目")
    def test_filter_across_direction_program(self, driver):
        release_page = self.release_page
        release_page.refresh()
        # 前提：先上传一个横屏的素材

        program_page = ProgramPage(driver)
        program_page.switch_to_program_management()
        program_page.create_general_program()

        with step("切到发布管理"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        with step("点击屏幕方向：横屏"):
            release_page.across_direction()

        # 进行断言
        labellocator = 'by_xpath,//div[@class="tag s3" and text()="横屏"]'
        bool_ture = release_page.element_exist(labellocator)
        assert labellocator

    @pytest.mark.run(order=32)
    @allure.title("节目编排-选节目-筛选竖屏节目")
    def test_filter_stick_direction_program(self, driver):
        release_page = self.release_page
        release_page.refresh()
        # 前提：1、生上传一个竖屏的素材

        media_page = MediaPage(driver)
        media_page.switch_to_media_center()
        media_page.upload_media()

        # 2、发布简单节目
        media_page.click_up_load()
        time.sleep(0.5)
        filepath = r"D:\\ui\\data\\test_stick.jpg"
        media_page.upload_file(filepath)
        time.sleep(5)
        progress_100_locator = 'by_xpath,//span[text()="100%"]'
        if media_page.element_exist(progress_100_locator):
            time.sleep(1)
            media_page.close_upload_alert()
        time.sleep(1)

        #      2、发布简单节目
        media_page.hover_to_media()
        media_page.choose_media()
        media_page.multi_release()

        with step("切到发布管理"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        with step("点击屏幕方向：竖屏"):
            release_page.stick_direction()

        # 进行断言
        labellocator = 'by_xpath,//div[@class="tag s3" and text()="竖屏"]'
        bool_ture = release_page.element_exist(labellocator)
        assert labellocator

    @pytest.mark.run(order=33)
    @allure.title("节目编排-选节目-过滤分辨率")
    def test_filter_resolution(self, driver):
        release_page = self.release_page
        release_page.refresh()
        # 前提：生成一个普通节目

        program_page = ProgramPage(driver)
        program_page.switch_to_program_management()
        program_page.create_general_program()

        with step("切到发布管理"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()
        init_window_size = release_page.get_window_size()
        release_page.maxsize_window()

        with step("先点击分辨率按钮,引出下拉菜单"):
            release_page.click_screen_resolution()

        time.sleep(0.5)

        with step("输入需要过滤的分辨率，然后进行筛选"):
            release_page.choose_resolution("1920x1080", driver)

        release_page.set_window_size(*init_window_size)

    @pytest.mark.run(order=34)
    @allure.title("节目编排-选节目-重置筛选条件")
    def test_filter_stick_direction_program(self, driver):
        release_page = self.release_page
        release_page.refresh()

        with step("切到发布管理"):
            release_page.switch_to_release_management()

        with step('点击节目编排'):
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        with step("点击屏幕方向：竖屏"):
            release_page.stick_direction()

        with step("点击重置按钮"):
            release_page.reset_button()

    @pytest.mark.run(order=35)
    @allure.title("节目编排-选节目-预览所有")
    def test_program_edit_preview_all(self, driver):

        release_page = self.release_page
        release_page.refresh()
        # 前提：生成一个普通节目

        program_page = ProgramPage(driver)

        program_page.switch_to_program_management()
        program_page.create_general_program()
        with step('点击节目编排'):
            release_page.switch_to_release_management()
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        mediapage = MediaPage(driver)
        program_list_class = ProgramList()
        with step("通过接口，拿到节目列表中所有的节目名称"):
            program_list_all = program_list_class.get_program_list_names()
            print("所有的节目名名称为", program_list_all)
            program_name = program_list_all[0]
            print("拿到的第一个的节目名名称为", program_name)
            time.sleep(0.5)
        with step("鼠标hover到一个节目上面"):
            mediapage.hover_to_media()
            time.sleep(3)
        with step("选择一个节目"):
            release_page.choose_program_and_choice()
            time.sleep(3)
        with step("点击保存按钮"):
            time.sleep(2)
            release_page.sumbit_span()
        with step("点击预览全部按钮"):
            release_page.program_edit_preview_all(driver)

    @pytest.mark.run(order=36)
    @allure.title("节目编排-选节目-预览仅一个节目")
    def test_program_edit_preview_one(self, driver):

        release_page = self.release_page
        release_page.refresh()
        # 前提：生成一个普通节目

        program_page = ProgramPage(driver)

        program_page.switch_to_program_management()
        program_page.create_general_program()
        with step('点击节目编排'):
            release_page.switch_to_release_management()
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        mediapage = MediaPage(driver)
        program_list_class = ProgramList()
        with step("通过接口，拿到节目列表中所有的节目名称"):
            program_list_all = program_list_class.get_program_list_names()
            print("所有的节目名名称为", program_list_all)
            program_name = program_list_all[0]
            print("拿到的第一个的节目名名称为", program_name)
            time.sleep(0.5)
        with step("鼠标hover到一个节目上面"):
            mediapage.hover_to_media()
            time.sleep(1)
        with step("选择一个节目"):
            release_page.choose_program_and_choice()
            time.sleep(1)
        with step("点击保存按钮"):
            time.sleep(1)
            release_page.sumbit_span()
        time.sleep(1)
        with step("鼠标移动到遮罩上面"):
            time.sleep(0.5)
            release_page.hover_to_program_edit()
        with step("点击预览按钮"):
            release_page.click_to_preview()

    @pytest.mark.usefixtures("generate_program")
    @pytest.mark.run(order=37)
    @allure.title("节目编排-选节目-删除单个节目")
    def test_program_edit_delete_one(self):

        release_page = self.release_page
        release_page.refresh()
        # 前提：生成一个普通节目

        # program_page = ProgramPage(driver)
        # with step("首先要先生成节目"):
        #     program_page.switch_to_program_management()
        #     program_lst = ProgramList()
        #     list_p = program_lst.get_program_list_ids()
        #     if not list_p:
        #         program_page.create_general_program()
        #     else:
        #         release_page.switch_to_release_management()
        with step('点击节目编排'):
            release_page.switch_to_release_management()
            release_page.program_edit()

        with step("点击新增按钮"):
            release_page.click_add_program()

        mediapage = MediaPage(driver)
        # program_list_class = ProgramList()
        # with step("通过接口，拿到节目列表中所有的节目名称"):
        # program_list_all = program_list_class.get_program_list_names()
        # print("所有的节目名名称为", program_list_all)
        # program_name = program_list_all[0]
        # print("拿到的第一个的节目名名称为", program_name)
        time.sleep(10)
        with step("鼠标hover到一个节目上面"):
            time.sleep(2)
            release_page.hover_program_and_choice()
        with step("选择一个节目"):
            release_page.choose_program_and_choice()
            time.sleep(2)
        with step("点击保存按钮"):
            time.sleep(0.5)
            release_page.sumbit_span()
        time.sleep(0.5)
        with step("鼠标移动到遮罩上面"):
            release_page.hover_to_program_edit()
        with step("点击删除按钮"):
            release_page.click_to_delete()

    @pytest.mark.run(order=38)
    @allure.title("节目编排-选节目-切换到选择设备弹框上")
    def test_switch_to_choose_terminal(self):

        release_page = self.release_page
        release_page.refresh()

        with step('点击节目编排'):
            release_page.switch_to_release_management()
            time.sleep(0.5)
            release_page.program_edit()

        time.sleep(0.5)
        with step("在节目编排的弹框上面，点击选择设备按钮"):
            release_page.switch_to_choose_terminal()
            time.sleep(0.5)

    @pytest.mark.run(order=39)
    @allure.title("节目编排-选节目-切换到选择策略弹框上")
    def test_switch_to_choose_terminal(self):

        release_page = self.release_page
        release_page.refresh()
        with step('点击节目编排'):
            release_page.switch_to_release_management()
            release_page.program_edit()

        time.sleep(0.5)
        with step("在节目编排的弹框上面，点击选择策略按钮"):
            release_page.switch_to_selection_strategy()
            time.sleep(0.5)

    @pytest.mark.run(order=40)
    @allure.title("节目编排-选节目-进行标签的折叠")
    def test_collapse_edit_label(self):

        release_page = self.release_page
        release_page.refresh()

        with step('点击节目编排'):
            release_page.switch_to_release_management()
            release_page.program_edit()

        time.sleep(0.5)
        with step("在节目编排的弹框上面，点击折叠全部标签按钮"):
            release_page.collapse_edit_label()
            time.sleep(0.5)

    @pytest.mark.run(order=41)
    @allure.title("节目编排-选择节目-进行标签的展开")
    def test_expand_all_label(self):
        release_page = self.release_page
        release_page.refresh()

        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()
        time.sleep(0.5)
        with step("打开节目编排弹框"):
            release_page.program_edit()

        with step("先点击折叠label按钮"):
            release_page.collapse_edit_label()

        time.sleep(0.5)
        with step("在点击展开label按钮"):
            release_page.expand_edit_label()

    @pytest.mark.run(order=42)
    @allure.title("删除第一个标签")
    def test_delete_first_label(self):
        release_page = self.release_page
        release_page.refresh()
        window_size = release_page.get_window_size()
        release_page.maxsize_window()

        with step("切换到发布管理tab页上"):
            release_page.switch_to_release_management()

        with step("打开节目编排弹框"):
            release_page.program_edit()

        all_labels_locator = 'by_xapth,//div[@class="item-box"]/div'
        all_labels_ele = release_page.get_elements(all_labels_locator)
        print("all_labels_ele", all_labels_ele)
        if all_labels_ele is None:
            release_page.click_save_as_label()
            release_page.set_label_name("label_001")
            release_page.save_program_edit()
            print("新增标签成功")
            with step("鼠标hover到第一个标签上面"):
                release_page.hover_to_first_edit_label()
            with step("删除第一个label"):
                release_page.delete_first_label()
        else:
            with step("鼠标hover到第一个标签上面"):
                release_page.hover_to_first_edit_label()
            with step("删除第一个label"):
                release_page.delete_first_label()
        release_page.set_window_size(*window_size)
