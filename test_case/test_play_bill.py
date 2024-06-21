import random
import time
import traceback

import pytest
import allure
from allure_commons._allure import step

from common.set_up_media_list import MediaList
from common.set_up_play_bill import PlayBill
from common.set_up_program_list import ProgramList
from common.set_up_terminal_list import Terminal_List
from config.log_config import logger
from conftest import driver
from pageobject.media_page import MediaPage
from pageobject.play_bill_page import PlayBillPage
from pageobject.program_page import ProgramPage
from pageobject.release_page import ReleasePage
from pageobject.terminal_page import TerminalPage


@pytest.fixture(scope='class')
def release_page(request, driver):
    release_page = ReleasePage(driver)
    request.cls.release_page = release_page
    yield release_page


@pytest.fixture(scope='class')
def play_bill_page(request, driver):
    play_bill_page = PlayBillPage(driver)
    request.cls.play_bill_page = play_bill_page
    yield play_bill_page
    play_bill = PlayBill()
    play_bill.clear_play_bill()

@pytest.fixture(scope='class',autouse=True)
def init_clear_all_play_bill_list():
    play_bill = PlayBill()
    play_bill.clear_play_bill()


@pytest.fixture(scope='class',autouse=True)
def init_play_bill(driver):
    """
    初始化节目单，如果没有节目单，则创建普通节目，进行发布操作
    以达到环境初始化的作用
    """
    try:
        play_bill = PlayBill()
        play_bill.clear_play_bill()
        program_page = ProgramPage(driver)
        release_page = ReleasePage(driver)
        terminal_page = TerminalPage(driver)
        terminal_list = Terminal_List()

        sn_api = random.randint(10000, 100000000)
        terminal_list.add_terminal_api(sn_api)
        release_page.refresh()
        program_list = ProgramList()
        all_play_bill_ids = play_bill.get_play_bill_ids()
        if not all_play_bill_ids:
            all_program_ids, program_folder_id = program_list.get_program_list_ids()
            all_terminal_list = terminal_list.get_terminal_list()
            if not all_terminal_list:
                # terminal_page.add_new_terminal()
                terminal_list.add_terminal_api(sn_api)
            if not all_program_ids:
                program_page.switch_to_program_management()
                program_page.create_general_program()
                program_page.hover_to_first_program()
                # 获取节目名称
                with step("选择第一个节目"):
                    program_page.choose_first_program()
                    program_page.multi_release()
                with step("选择设备"):
                    win_size = release_page.get_window_size()
                    release_page.maxsize_window()
                    release_page.choose_terminal()
                    release_page.select_all_terminals()
                    release_page.confirm_terminal_button()
                    release_page.click_system_icon()

                # release_page.confirm_button()
                release_page.release_general_program()

                release_page.set_window_size(*win_size)
            else:
                program_page.switch_to_program_management()
                program_page.create_general_program()
                program_page.hover_to_first_program()
                # 获取节目名称
                with step("选择第一个节目"):
                    program_page.choose_first_program()
                    program_page.multi_release()
                with step("选择设备"):
                    win_size = release_page.get_window_size()
                    release_page.maxsize_window()
                    release_page.choose_terminal()
                    release_page.select_all_terminals()
                    release_page.confirm_terminal_button()
                    release_page.click_system_icon()

                # release_page.confirm_button()
                release_page.release_general_program()

                release_page.set_window_size(*win_size)

    except Exception:
        print("节目单初始化出错")
        raise


@pytest.fixture(scope="function")
def generate_one_program(driver,release_page):
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
            time.sleep(0.3)
            mediapage.refresh()
            mediapage.switch_to_media_center()
            mediapage.upload_media()
            time.sleep(2)
            # 素材发布
            # media_ids, folder_ids = media_list.get_media_list()
            mediapage.hover_to_media()
            mediapage.choose_media()
            mediapage.multi_release()
            #选择设备，然后发布节目

            with step("点击选设备"):
                release_page.choose_terminal()

            with step("选择一个设备"):
                # release_page.choose_one_terminal()

                # release_page.choose_terminal()
                release_page.select_all_terminals()
                # release_page.confirm_terminal_button()
                # release_page.click_system_icon()

                # time.sleep(6)
            with step("选完设备后，点击确定"):
                # release_page.confirm_release_strategy()
                release_page.confirm_terminal_button()
                release_page.click_system_icon()

            with step("发布普通节目"):
                release_page.release_general_program()

        else:
            media_list.delete_all_media()
            mediapage.switch_to_media_center()
            mediapage.upload_media()
            mediapage.hover_to_media()
            mediapage.choose_media()
            mediapage.multi_release()
            with step("点击选设备"):
                release_page.choose_terminal()

            with step("选择一个设备"):
                # release_page.choose_one_terminal()

                # release_page.choose_terminal()
                release_page.select_all_terminals()
                # release_page.confirm_terminal_button()
                # release_page.click_system_icon()

                # time.sleep(6)
            with step("选完设备后，点击确定"):
                # release_page.confirm_release_strategy()
                release_page.confirm_terminal_button()
                release_page.click_system_icon()

            with step("发布普通节目"):
                release_page.release_general_program()

@allure.epic("项目hkc")
@allure.feature("play bill list")
@pytest.mark.usefixtures("init_play_bill")
@pytest.mark.usefixtures("play_bill_page")
@pytest.mark.usefixtures("release_page")
class TestPlayBill:
    release_page = ReleasePage(driver)
    terminal_list = Terminal_List()

    @pytest.mark.run(order=1)
    @allure.title("节目单预览")
    # @pytest.mark.usefixtures("generate_one_program")
    def test_preview_play_bill(self):
        play_bill_page = self.play_bill_page
        play_bill_page.refresh()
        time.sleep(0.5)

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击节目单预览按钮"):
            play_bill_page.preview_play_bill()
            time.sleep(0.5)
            play_bill_page.refresh()

    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures("generate_one_program")
    @allure.title("取消节目单引用")
    def test_cancel_copy_play_bill(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()
        try:
            play_bill_list = PlayBill()
            all_ids = play_bill_list.get_play_bill_ids()
            if not all_ids:
                generate_one_program()
            with step("点击节目单引用按钮"):
                play_bill_page.copy_play_bill()

            with step("点击取消引用按钮"):
                release_page.dismiss_release_strategy()
        except:
            raise

    @pytest.mark.run(order=3)
    @allure.title("关闭节目单引用弹框")
    # @pytest.mark.usefixtures("generate_one_program")
    def test_close_copy_play_bill(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击节目单引用按钮"):
            play_bill_page.copy_play_bill()

        with step("点击关闭引用按钮，来关闭弹框"):
            play_bill_page.close_copy_alert()

        logger.info("Start print log")
        logger.debug("Do something")
        logger.warning("Something maybe fail.")
        logger.info("Finish")

    @pytest.mark.run(order=4)
    @allure.title("成功引用用节目单")
    # @pytest.mark.usefixtures("generate_one_program")
    def test_copy_play_bill_and_save(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page
        release_page.refresh()

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击节目单引用按钮"):
            play_bill_page.copy_play_bill()

        time.sleep(0.5)
        with step("点击确认按钮"):
            play_bill_page.confirm_copy_button()

        with step("点击暂存按钮"):
            release_page.release_general_program()



    @pytest.mark.run(order=7)
    @allure.title("取消节目单失效")
    @pytest.mark.usefixtures("generate_one_program")
    def test_cancel_expiry_play_bill(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击失效按钮，进行失效操作"):
            play_bill_page.expiry_play_bill()

        with step("点击取消按钮"):
            release_page.dismiss_release_strategy()

    @pytest.mark.run(order=8)
    @allure.title("成功失效节目单")
    # @pytest.mark.usefixtures("generate_one_program")
    def test_success_expiry_play_bill(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击删除按钮，进行失效"):
            play_bill_page.delete_play_bill()

        with step("点击确认按钮，确认失效"):
            play_bill_page.confirm_close_button()

    @pytest.mark.run(order=9)
    @allure.title("取消删除节目单")
    @pytest.mark.usefixtures("generate_one_program")
    def test_cancel_delete_play_bill(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击删除按钮，进行删除操作"):
            play_bill_page.delete_play_bill()

        with step("点击取消按钮"):
            release_page.dismiss_release_strategy()

    @pytest.mark.run(order=10)
    @allure.title("成功删除节目单")
    @pytest.mark.usefixtures("generate_one_program")
    def test_success_delete_play_bill(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击删除按钮，进行失效"):
            play_bill_page.delete_play_bill()

        with step("点击确认按钮，确认失效"):
            play_bill_page.confirm_close_button()

    @pytest.mark.run(order=11)
    @allure.title("使用状态过滤，过滤暂存节目单")
    # @pytest.mark.usefixtures("generate_one_program")
    def test_filter_temporary_storage(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("进行暂存状态过滤"):
            play_bill_page.click_filter_status()
            play_bill_page.filter_temporary_storage_status()

    @pytest.mark.run(order=12)
    @allure.title("使用状态过滤，过滤审批中节目单")
    def test_filter_in_process_approve_status(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("进行审批中状态过滤"):
            play_bill_page.click_filter_status()
            play_bill_page.filter_in_process_approve_status()

    @pytest.mark.run(order=13)
    @allure.title("使用状态过滤，过滤返回修改节目单")
    def test_filter_return_modify_status(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("进行返回修改状态过滤"):
            play_bill_page.click_filter_status()
            play_bill_page.filter_return_modify_status()

    @pytest.mark.run(order=14)
    @allure.title("使用状态过滤，过滤审批不通过节目单")
    def test_filter_fail_to_approve_status(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("进行审批不通过状态过滤"):
            play_bill_page.click_filter_status()
            play_bill_page.filter_fail_to_approve_status()

    @pytest.mark.run(order=15)
    @allure.title("使用状态过滤，过滤已发布节目单")
    def test_filter_released_status(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("进行已发布状态过滤"):
            play_bill_page.click_filter_status()
            play_bill_page.filter_released_status()

    @pytest.mark.run(order=16)
    @allure.title("使用状态过滤，过滤已发布节目单")
    def test_filter_disabled_status(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("进行已失效状态过滤"):
            play_bill_page.click_filter_status()
            play_bill_page.filter_disabled_status()

    @pytest.mark.run(order=17)
    @allure.title("将引用的节目单进行暂存操作")
    # @pytest.mark.usefixtures("generate_one_program")
    def test_copy_play_bill_temporary_storage(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page

        with step("侧边栏切到到发布管理"):
            play_bill_page.switch_to_release_management()

        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        with step("点击节目单引用按钮"):
            play_bill_page.copy_play_bill()

        with step("点击确认按钮"):
            play_bill_page.confirm_copy_button()
            print("确定按钮，已被点击")

        with step("点击暂存按钮"):
            release_page.temporary_storage()

    @pytest.mark.run(order=18)
    @allure.title("进行节目单的编辑")
    @pytest.mark.usefixtures("init_clear_all_play_bill_list")
    @pytest.mark.usefixtures("generate_one_program")
    def test_edit_play_bill(self):
        play_bill_page = self.play_bill_page
        release_page = self.release_page
        terminal_list = self.terminal_list
        all_terminal = terminal_list.get_terminal_list()
        print("all_terminal:",all_terminal)
        sn_api = random.randint(10000,100000000)
        if all_terminal ==[]:
            terminal_list.add_terminal_api(sn_api)

        set_up_play_bill = PlayBill()
        if set_up_play_bill.get_play_bill_ids() != []:
            set_up_play_bill.clear_play_bill()
            release_page.refresh()

        all_terminal = terminal_list.get_terminal_list()
        print("all_terminal---new:", all_terminal)

        time.sleep(5)
        with step("侧边栏切到到发布管理"):
            release_page.refresh()
            play_bill_page.switch_to_release_management()

        time.sleep(5)
        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        time.sleep(5)
        with step("点击节目单引用按钮"):
            play_bill_page.copy_play_bill()

        time.sleep(5)
        with step("点击确认按钮"):
            play_bill_page.confirm_copy_button()
            print("点击确认按钮成功")

        time.sleep(5)
        with step("点击暂存按钮"):
            release_page.temporary_storage()

        time.sleep(5)
        with step("发布管理中，切到节目单"):
            play_bill_page.switch_to_play_bill()

        time.sleep(5)
        with step("发布管理中，点击编辑按钮"):
            play_bill_page.edit_play_bill()

        time.sleep(5)
        with step("进行发布操作"):
            release_page.release_general_program()


