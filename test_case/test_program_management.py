import random
import time

import allure
import pytest
from allure_commons._allure import step
from selenium.common import ElementClickInterceptedException, ElementNotInteractableException

from common.set_up_media_list import MediaList
from common.set_up_program_list import ProgramList
from pageobject.program_page import ProgramPage


@pytest.fixture(scope="class")
def program_page(request, driver):
    program_page = ProgramPage(driver)
    request.cls.program_page = program_page
    yield program_page

@pytest.fixture()
def program_management_set_up(program_page):
    # 1、清理所有的节目，避免形成干扰
    programlist = ProgramList()
    programlist.get_program_list_ids()
    programlist.delete_all_program()
    program_page.switch_to_program_management()
    # return programlist


@allure.epic("项目hkc")
@allure.feature("program management")
@pytest.mark.usefixtures("program_page")
@pytest.mark.usefixtures("program_management_set_up")
class TestProgramManagement:

    """
    在类内初始化ProgramList，用于普通方法进行接口层读取节目列表和批量删除节目
    """
    program_list_class = ProgramList()

    @allure.title("新增一个横屏的普通节目")
    @pytest.mark.run(order=1)
    def test_create_General_program_accross(self):
        program_page = self.program_page
        program_page.refresh()
        program_name = "test_横屏普通节目"
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()
        with step("输入节目名称（普通节目）"):
            program_page.input_program_name(program_name)

        with step("选择屏幕方向"):
            program_page.screen_direction("x")

        with step("选择分辨率"):
            program_page.click_resolution()
            program_page.choose_screen("1920x1080")

        with step("点击保存按钮"):
            program_page.confirm_create_program()

        with step("在编辑器中进行保存"):
            program_page.save_general_program()
            time.sleep(3)
            program_page.comeback_general_program()
            time.sleep(1)

    @allure.title("新增一个竖屏的普通节目")
    @pytest.mark.run(order=2)
    def test_create_General_program_hard(self):
        program_page = self.program_page
        program_name = "test_竖屏-普通节目"
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()
        with step("输入节目名称（普通节目）"):
            program_page.input_program_name(program_name)

        with step("选择屏幕方向"):
            program_page.screen_direction("y")

        with step("选择分辨率"):
            program_page.click_resolution()
            program_page.choose_screen("1080x1920")

        with step("点击确定按钮"):
            program_page.confirm_create_program()

        with step("在编辑器中进行保存"):
            program_page.save_general_program()
            time.sleep(3)
            program_page.comeback_general_program()
            time.sleep(1)

    @allure.title("新增一个自定义屏幕尺寸的普通节目")
    @pytest.mark.run(order=3)
    def test_create_general_program_diy(self):
        program_page = self.program_page
        program_name = "test_自定义尺寸-普通节目"
        screen_wide = random.randint(100, 10000)
        screen_high = random.randint(100, 10000)
        input_screen = str(screen_wide) + "x" + str(screen_high)
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()
        with step("输入节目名称（普通节目）"):
            program_page.input_program_name(program_name)

        with step("选择屏幕方向"):
            program_page.screen_direction("z")

        with step("输入屏幕尺寸"):
            program_page.input_screen(input_screen)

        with step("点击确定按钮"):
            program_page.confirm_create_program()

        with step("在编辑器中进行保存"):
            program_page.save_general_program()
            time.sleep(3)
            program_page.comeback_general_program()
            time.sleep(1)

    @allure.title("取消新增普通节目")
    @pytest.mark.run(order=4)
    def test_cancel_general_program(self):
        program_page = self.program_page
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()

        with step("取消创建"):
            program_page.cancel_create_program()

    @allure.title("关闭创建节目弹框")
    @pytest.mark.run(order=5)
    def test_close_general_program(self):
        program_page = self.program_page
        with step("点击创建节目"):
            program_page.click_create_program()

        with step("关闭创建弹框"):
            program_page.close_create_pragram()

    @allure.title("新增一个横屏的联屏节目")
    @pytest.mark.run(order=6)
    def test_create_relevance_program_accross(self):
        program_page = self.program_page
        program_page.refresh()
        # 联屏节目随机名称
        ran_int = random.randint(100, 999)
        relevance_program_name = "test_联屏横屏_" + str(ran_int)

        # 行、列随机
        randow_row = str(random.randint(1, 5))
        randow_col = str(random.randint(1, 4))
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()

        with step("切换到联屏节目tab上"):
            program_page.relevance_program_tab()

        with step("输入联屏节目的节目名称"):
            program_page.input_program_name(relevance_program_name)

        with step("输入屏幕组合行和列值"):
            # time.sleep(5)
            program_page.row_numbers(randow_row)
            time.sleep(0.5)
            program_page.col_numbers(randow_col)

        time.sleep(2)
        with step("创建联屏节目，点击选择素材"):
            program_page.choose_relevance_media()

        with step("上传一个素材"):
            win_size = program_page.get_window_size()
            program_page.maxsize_window()
            time.sleep(0.5)
            program_page.create_program_and_upload_media()

        with step("选择一个素材"):
            program_page.hover_to_media()
            program_page.choose_media()
        with step("选择好素材后，点击确认按钮"):
            # 忽略方法名，没有用错
            program_page.confirm_delete_media()

        with step("再次点击确认按钮，生成一个联屏节目"):
            program_page.confirm_delete_program()
        time.sleep(3)
        program_page.refresh()
        time.sleep(3)
        # program_page.set_window_size(*win_size)

    @allure.title("新增一个竖屏的联屏节目")
    @pytest.mark.run(order=7)
    def test_create_relevance_program_hard(self):
        program_page = self.program_page
        program_page.refresh()
        # 联屏节目随机名称
        ran_int = random.randint(100, 999)
        relevance_program_name = "test_联屏竖屏_" + str(ran_int)

        #设置窗口最大化
        current_win_size = program_page.get_window_size()
        program_page.maxsize_window()

        # 行、列随机
        randow_row = str(random.randint(1, 5))
        randow_col = str(random.randint(1, 4))
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()

        with step("切换到联屏节目tab上"):
            program_page.relevance_program_tab()

        with step("输入联屏节目的节目名称"):
            program_page.input_program_name(relevance_program_name)

        with step("输入屏幕组合行和列值"):
            # time.sleep(5)
            program_page.row_numbers(randow_row)
            time.sleep(0.5)
            program_page.col_numbers(randow_col)

        with step("切换到竖屏tab上"):
            program_page.screen_direction("y")

        time.sleep(2)
        with step("创建联屏节目，点击选择素材"):
            program_page.choose_relevance_media()

        #先判断暂无数据是否存在，如果存在，就进行素材上传
        no_media_locator = 'by_xpath,//div[@class="content"]/div[@class="empty-box"]'
        no_media_ele  = program_page.get_element(no_media_locator)
        if no_media_ele:
            program_page.upload_media()

        # #先判断是不是有素材：
        # media_List = MediaList()
        # list_media , folder_ids = media_List.get_media_list=()
        # print("当前列表为:",list_media)
        # if not list_media:
        #     with step("上传一个素材"):
        #         program_page.upload_media()

        with step("选择一个素材"):
            program_page.hover_to_media()
            program_page.choose_media()
        with step("选择好素材后，点击确认按钮"):
            # 忽略方法名，没有用错
            program_page.confirm_delete_media()

        with step("再次点击确认按钮，生成一个联屏节目"):
            program_page.confirm_delete_program()
        time.sleep(3)
        program_page.refresh()
        program_page.set_window_size(*current_win_size)
        time.sleep(3)

    @allure.title("创建联屏节目，测试屏幕组合-行数，箭头向下减少个数分功能")
    @pytest.mark.run(order=8)
    def test_relevance_program_raw_decrease(self):
        program_page = self.program_page
        program_page.refresh()
        raw_times = 6
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()

        with step("切换到联屏节目tab上"):
            program_page.relevance_program_tab()

        with step("输入联屏节目的节目名称"):
            program_page.input_program_name(raw_times)

        with step("在行数中先输入固定值，然后再，进行减小操作"):
            program_page.row_numbers(str(raw_times))
            program_page.row_decrease()

        with step("关闭弹框"):
            program_page.cancel_create_program()


    @allure.title("创建联屏节目，测试屏幕组合-行数，箭头向上增加个数分功能")
    @pytest.mark.run(order=9)
    def test_relevance_program_raw_increase(self):
        program_page = self.program_page
        raw_times = random.randint(1, 5)
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()

        with step("切换到联屏节目tab上"):
            program_page.relevance_program_tab()

        with step("输入联屏节目的节目名称"):
            program_page.input_program_name(raw_times)

        with step("在行数中，进行增加操作"):
            for i in range(1, raw_times):
                program_page.row_increase()
                i += 1
                time.sleep(0.3)
        with step("关闭弹框"):
            program_page.cancel_create_program()

    @allure.title("创建联屏节目，测试屏幕组合-列数，箭头向下减少个数分功能")
    @pytest.mark.run(order=10)
    def test_relevance_program_col_decrease(self):
        program_page = self.program_page
        col_times = random.randint(1, 5)
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()

        with step("切换到联屏节目tab上"):
            program_page.relevance_program_tab()

        with step("输入联屏节目的节目名称"):
            program_page.input_program_name(col_times)

        with step("在行数中先输入固定值，然后再，进行减小操作"):
            program_page.col_numbers(col_times)
            program_page.col_decrease()

        with step("关闭弹框"):
            program_page.cancel_create_program()

    @allure.title("创建联屏节目，测试屏幕组合-列数，箭头向上增加个数分功能")
    @pytest.mark.run(order=11)
    def test_relevance_program_col_increase(self):
        program_page = self.program_page
        col_times = random.randint(1, 5)
        with step("点击创建节目"):
            program_page.switch_to_program_management()
            program_page.click_create_program()

        with step("切换到联屏节目tab上"):
            program_page.relevance_program_tab()

        with step("输入联屏节目的节目名称"):
            program_page.input_program_name(col_times)

        with step("在行数中，进行增加操作"):
            for i in range(1, col_times):
                program_page.col_increase()
                i += 1
                time.sleep(0.3)
        with step("关闭弹框"):
            program_page.cancel_create_program()

    @allure.title("新建一个文件夹")
    @pytest.mark.run(order=12)
    def test_mkdir(self):
        program_page = self.program_page
        random_name = random.randint(10, 500)
        program_page.switch_to_program_management()
        time.sleep(0.3)
        try:
            with step("点击右上角文件夹按钮"):
                program_page.click_mkdir()
        except ElementClickInterceptedException as e:
            raise e
        with step("输入文件夹名称"):
            program_page.dir_name(random_name)
        with step("点击确认按钮"):
            program_page.confirm_mkdir()


    @allure.title("删除一个节目")
    @pytest.mark.run(order=13)
    def test_confirm_delete_one_program(self):
        program_page = self.program_page
        program_page.refresh()
        program_list_class =self.program_list_class

        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            program_page.create_general_program()
        with step("鼠标hover到一个节目上面"):
            program_page.hover_to_media()
        # time.sleep(100000)
        # 先获取所有的节目名称
        program_names = program_list_class.get_program_list_names()
        program_name = program_names[0]
        with step("选择一个节目"):
            program_page.choose_first_program()
        with step("点击批量删除按钮"):
            program_page.multi_delete_program()
        with step("点击确认按钮"):
            program_page.multi_delete_confirm()

    @allure.title("同时删除3个节目")
    @pytest.mark.run(order=14)
    def test_multi_delete_three_program(self):
        program_page = self.program_page
        with step("先创建一个节目"):
            for i in range(0, 3):
                program_page.switch_to_program_management()
                program_page.create_general_program()
                # random_name = rerurn_name.random_program_name

        with step("选择3个节目"):
            # 拿到所有的节目数量
            # 节目进行逐个hover，然后进行勾选
            program_list_class = self.program_list_class
            program_list_all = program_list_class.get_program_list_names()
            count = len(program_list_all)
            for i in range(0,count):
                program_page.hover_to_all_program(i)
                program_page.choose_all_program(i)

        with step("点击批量删除按钮"):
            program_page.multi_delete_program()
        with step("点击确认按钮"):
            program_page.multi_delete_confirm()

    @allure.title("取消删除一个节目")
    @pytest.mark.run(order=15)
    def test_cancel_delete_program(self):
        program_page = self.program_page
        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            program_page = self.refresh()
            program_page.create_general_program()
        with step("鼠标hover到一个节目上面"):
            program_page.hover_to_media()
        with step("选择一个节目"):
            program_page.choose_program()
        with step("点击批量删除按钮"):
            program_page.multi_delete_program()
        with step("点击取消按钮"):
            program_page.multi_delete_cancel()

    @allure.title("重新编辑节目")
    @pytest.mark.run(order=16)
    def test_reedit_program(self):
        program_page =self.program_page
        size = program_page.get_window_size()
        program_page.maxsize_window()
        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            program_page.create_general_program()
        program_page.refresh()

        with step("点击更多按钮"):
            program_page.program_more_button()

        with step("点击编辑按钮"):
            program_page.edit_info()

        time.sleep(0.5)
        with step("在编辑器中点击返回"):
            program_page.comeback_general_program()

    @allure.title("引用节目")
    @pytest.mark.run(order=17)
    def test_copy_program(self):
        program_page = self.program_page
        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            program_page.create_general_program()
        program_page.refresh()

        with step("点击更多按钮"):
            program_page.program_more_button()

        with step("点击引用按钮"):
            program_page.program_copy_button()

        with step("输入引用名称"):
            program_page.program_copy_name("引用后新的名称")

        with step("点击确定按钮"):
            program_page.confirm_create_program()

        time.sleep(0.5)
        with step("在编辑器中点击返回"):
            program_page.comeback_general_program()

    @allure.title("重命名节目")
    @pytest.mark.run(order=18)
    def test_rename_program(self):
        program_page = self.program_page
        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            time.sleep(0.3)
            program_page.create_general_program()
        program_page.refresh()

        with step("点击更多按钮"):
            program_page.program_more_button()

        with step("点击重命名按钮"):
            program_page.click_rename_program()

        time.sleep(0.5)
        with step("输入新的节目名称"):
            program_page.rename_program_name("新的节目名称")

        with step("点击确定按钮"):
            program_page.confirm_create_program()

    @allure.title("取消删除节目")
    @pytest.mark.run(order=19)
    def test_cancel_delete_program(self):
        program_page = self.program_page
        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            program_page.create_general_program()
        program_page.refresh()

        with step("点击更多按钮"):
            program_page.program_more_button()

        with step("点击删除节目按钮"):
            program_page.more_click_delete()

        with step("在弹框中点击取消按钮"):
            program_page.cancel_delete()

    @allure.title("关闭删除节目弹框")
    @pytest.mark.run(order=20)
    def test_close_delete_program(self):
        program_page = self.program_page
        program_page.refresh()
        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            program_page.create_general_program()
        # program_page.refresh()

        with step("点击更多按钮"):
            program_page.program_more_button()

        with step("点击删除节目按钮"):
            program_page.more_click_delete()

        with step("在弹框中点击关闭按钮"):
            program_page.close_delete_program_alert()

    @allure.title("确认删除节目")
    @pytest.mark.run(order=21)
    def test_confirm_delete_program(self):
        program_page = self.program_page
        with step("先创建一个节目"):
            program_page.switch_to_program_management()
            program_page.create_general_program()
        program_page.refresh()

        with step("点击更多按钮"):
            program_page.program_more_button()

        with step("点击删除节目按钮"):
            program_page.more_click_delete()

        with step("在弹框中点击确认按钮"):
            program_page.confirm_delete_program()

    @allure.title("从节目管理中，点击发布，跳转到节目发布")
    @pytest.mark.run(order=22)
    def test_program_release(self):
        program_page = self.program_page
        program_page.refresh()
        with step("点击发布按钮"):
            program_page.switch_to_program_management()
            time.sleep(0.5)
            program_page.multi_release()
