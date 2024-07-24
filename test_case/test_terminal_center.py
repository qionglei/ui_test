import random
import time

import pytest, allure
from allure_commons._allure import step
from selenium.common import NoSuchElementException, ElementClickInterceptedException

from common.set_up_org import OrgList
from common.set_up_terminal_list import Terminal_List
from pageobject.system_page import SystemPage
from pageobject.terminal_page import TerminalPage
from data_clean import clear_terminal


@pytest.fixture(scope='class')
def terminal_page(request, driver):
    terminal_page = TerminalPage(driver)
    request.cls.terminal_page = terminal_page
    yield terminal_page


@pytest.fixture(scope='class')
def sys_page(request, driver):
    sys_page = SystemPage(driver)
    request.cls.sys_page = sys_page
    yield sys_page

@pytest.fixture(scope="function")
def clear_terminal_list():
    list_t = Terminal_List()
    # if __name__ == '__main__':
    # list_t.login_cookie()
    ids = list_t.get_terminal_list()
    list_t.delete_terminal(ids)
    clear_terminal()

@pytest.fixture(scope="class",autouse=True)
def set_up_org():
    org_list = OrgList()
    org_list.clear_all_org()
    org_list.add_branch()


@pytest.fixture(scope="function")
def terminal_set_up(terminal_page, sys_page):
    sn_id = random.randint(1, 100000)
    sn_name = "test" + str(sn_id)
    terminal_page.switch_to_terminal_center()
    # terminal_page = self.terminal_page
    # sys_page = self.sys_page
    # time.sleep(0.5)
    # sys_page.add_new_shop("test门店")
    list_ele = 'by_xpath,//div[@class="action-right"]/img[@title="设置"]'
    if terminal_page.element_exist(list_ele):
        pass
    else:
        with step("点击设备接入"):
            terminal_page.click_bind_terminal()
        time.sleep(0.5)
        with step("输入设备sn码"):
            terminal_page.input_terminal_id(sn_id)
        time.sleep(0.5)
        with step("输入设备名称"):
            terminal_page.input_terminal_name(sn_name)
        time.sleep(0.5)
        with step("先点击所属机构"):
            terminal_page.terminal_org()
        time.sleep(0.5)
        with step("在下拉框展开组织架构"):
            terminal_page.terminal_org_more()
        time.sleep(0.5)
        with step("在下拉框进行选择"):
            terminal_page.select_terminal_org()
        time.sleep(0.5)
        with step("点击保存按钮"):
            terminal_page.click_terminal_id()
            terminal_page.confirm_bind_terminal()
        time.sleep(0.5)


@pytest.mark.usefixtures("terminal_page")
@pytest.mark.usefixtures("sys_page")
@pytest.mark.usefixtures("env")
@allure.epic("项目hkc")
@allure.feature("terminal_center")
class TestTerminalCenter:
    sn_id = random.randint(1, 100000)
    sn_name = "test" + str(sn_id)

    # @pytest.mark.skip(reason="搜索后没进行清理")
    @allure.title("搜索设备id")
    @pytest.mark.run(order=1)
    def test_search_terminal_by_id(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        with step("前提：切到设备中心去，而且新增一个设备"):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_new_terminal()
        fixed_terminal_id = "TERMINAL_ID_0001"
        with step("点击搜索输入框，输入内容"):
            terminal_page.search_terminal_by_id(fixed_terminal_id)
        time.sleep(0.5)
        with step("点击搜索按钮"):
            terminal_page.click_search_terminal_button()
            time.sleep(0.5)
            all_terminal_ids = terminal_page.all_terminal_ids()
        # try:
        #     assert fixed_terminal_id in all_terminal_ids
        # except AssertionError as e:
        #     raise e
        # finally:
        #     terminal_page.refresh()

        terminal_page.refresh()


    # @pytest.mark.skip("fail,定位下拉框有点问题")
    @allure.title("设备设置中重新选择机构")
    @pytest.mark.run(order=3)
    def test_rechange_terminal_org(self):
        terminal_page = self.terminal_page
        with step("2、新增一个设备"):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_new_terminal()
        with step("打开设备设置按钮"):
            terminal_page.click_terminal_setting()
        with step("点击下拉框"):
            terminal_page.rechange_terminal_org()
        with step("进行选择门店,变更门店"):
            terminal_page.rechange_terminal_org()

    @pytest.mark.skip(reason="还缺少新增标签的功能")
    @allure.title("设备设置中，重新选择设备标签")
    @pytest.mark.run(order=4)
    def test_rechange_terminal_label(self):
        terminal_page = self.terminal_page
        terminal_page.rechange_terminal_label()


    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("发送插播字幕，位置：中")
    @pytest.mark.run(order=7)
    def test_insert_subtitle_median(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        text = random.randint(999, 9999999999)
        # sql_execute()
        with step("各种前提："):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_real_terminal()
            terminal_page.click_more_button()
            terminal_page.insert_subtitle()

        subtitle_position_loca = ('by_xapth,//label[text()="播放位置"]')
        try:
            if terminal_page.element_exist(subtitle_position_loca):
                # with step("先点击插播内容弹框"):
                #     terminal_page.click_insert_subtitle_text()
                time.sleep(0.5)
                with step("发送随机弹幕"):
                    terminal_page.input_insert_subtitle_text(text)
                with step("点击位置：中"):
                    terminal_page.insert_subtitle_position_median()
                with step("点击保存按钮"):
                    terminal_page.insert_subtitle_submit()
        except NoSuchElementException as e:
            print("非真实设备，无法发送插播字幕")
            with step("收起更多弹框"):
                terminal_page.click_more_button()

        finally:
            terminal_page.refresh()

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("发送插播字幕，位置：上")
    @pytest.mark.run(order=8)
    def test_insert_subtitle_up(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        random_text = random.randint(999, 9999999999)
        # sql_execute()
        with step("各种前提："):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_real_terminal()
            terminal_page.click_more_button()
            terminal_page.insert_subtitle()

        subtitle_position_loca = ('by_xapth,//label[text()="播放位置"]')
        try:
            if terminal_page.element_exist(subtitle_position_loca):
                # with step("先点击插播内容弹框"):
                #     terminal_page.click_insert_subtitle_text()
                time.sleep(0.5)
                with step("发送随机弹幕"):
                    time.sleep(0.5)
                    terminal_page.input_insert_subtitle_text(random_text)
                with step("点击位置：中"):
                    terminal_page.insert_subtitle_position_median()
                with step("点击位置：上"):
                    terminal_page.insert_subtitle_position_up()
                with step("点击保存按钮"):
                    terminal_page.insert_subtitle_submit()
        except NoSuchElementException as e:
            print("非真实设备，无法发送插播字幕")
            with step("收起更多弹框"):
                terminal_page.click_more_button()

        finally:
            terminal_page.refresh()

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("发送插播字幕，位置：下")
    @pytest.mark.run(order=9)
    def test_insert_subtitle_down(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        text = random.randint(999, 9999999999)
        # sql_execute()
        with step("各种前提："):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_real_terminal()
            terminal_page.click_more_button()
            terminal_page.insert_subtitle()

        subtitle_position_loca = ('by_xapth,//label[text()="播放位置"]')
        try:
            if terminal_page.element_exist(subtitle_position_loca):
                # with step("先点击插播内容弹框"):
                #     terminal_page.click_insert_subtitle_text()
                time.sleep(0.5)
                with step("发送随机弹幕"):
                    terminal_page.input_insert_subtitle_text(text)
                with step("点击位置：下"):
                    terminal_page.insert_subtitle_position_down()
                with step("点击保存按钮"):
                    terminal_page.insert_subtitle_submit()
        except NoSuchElementException as e:
            print("非真实设备，无法发送插播字幕")
            with step("收起更多弹框"):
                terminal_page.click_more_button()

        finally:
            terminal_page.refresh()

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("发送插播字幕，次数：随机1-10次")
    @pytest.mark.run(order=10)
    def test_insert_subtitle_down(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        text = random.randint(999, 9999999999)
        times = random.randint(1, 10)
        with step("各种前提："):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_real_terminal()
            terminal_page.click_more_button()
            terminal_page.insert_subtitle()

        subtitle_position_loca = ('by_xapth,//label[text()="播放位置"]')
        try:
            if terminal_page.element_exist(subtitle_position_loca):
                # with step("先点击插播内容弹框"):
                #     terminal_page.click_insert_subtitle_text()
                time.sleep(0.5)
                with step("发送随机弹幕"):
                    terminal_page.input_insert_subtitle_text(text)
                with step("发送次数，随机1-10次"):
                    terminal_page.insert_subtitle_circle_times(times)
                with step("点击保存按钮"):
                    terminal_page.insert_subtitle_submit()
        except NoSuchElementException as e:
            print("非真实设备，无法发送插播字幕")
            with step("收起更多弹框"):
                terminal_page.click_more_button()

        finally:
            terminal_page.refresh()

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("批量操作：停止、播放")
    @pytest.mark.run(order=11)
    def test_batch_terminal_stop_and_display(self):
        terminal_page = self.terminal_page
        # sql_execute()
        with step("新增真实设备"):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_real_terminal()
        with step("点击全选按钮"):
            terminal_page.select_one_terminal()
            # time.sleep(3)
            # terminal_page.select_all_terminal()
            print("点击全选按钮成功")
        time.sleep(0.5)
        with step("点击设备控制按钮"):
            # terminal_page.click_terminal_control()
            terminal_page.click_button('by_xpath,//span[text()="设备控制"]')
        with step("点击批量停止按钮"):
            terminal_page.click_button('by_xpath,//span[text()="停止"]')
        time.sleep(0.5)
        with step("点击批量播放按钮"):
            terminal_page.click_button('by_xpath,//span[text()="播放"]')
        # with step("点击批量关机按钮"):
        #     terminal_page.click_button('by_xpath,//span[text()="关机"]')
        with step("收起设备控制按钮"):
            terminal_page.click_button('by_xpath,//span[text()="设备控制"]')

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("批量发送插播字幕")
    @pytest.mark.run(order=12)
    def test_batch_subtitle(self):
        # sql_execute()
        terminal_page = self.terminal_page
        time.sleep(0.5)
        with step("新增一个真实的设备"):
            terminal_page.add_real_terminal()
        with step("点击全选按钮"):
            terminal_page.select_one_terminal()
            # time.sleep(0.5)
            # terminal_page.select_all_terminal()
            print("点击全选按钮成功")
        time.sleep(0.5)
        with step("点击设备控制按钮"):
            # terminal_page.click_terminal_control()
            terminal_page.click_button('by_xpath,//span[text()="设备控制"]')
        with step("点击插播字幕按钮"):
            terminal_page.click_button('by_xpath,//span[text()="字幕"]')
        with step("输入随机的弹幕内容"):
            text = random.randint(999999, 999999999999999)
            terminal_page.input_insert_subtitle_text(text)
            if terminal_page.element_exist('by_xpath,//div[text()="请输入插播内容"]'):
                with step("位置选择：中"):
                    terminal_page.insert_subtitle_position_median()
                with step("点击保存按钮"):
                    terminal_page.insert_subtitle_submit()


    @allure.title("查看设备中心-组织架构树，折叠和展开所有门店")
    @pytest.mark.run(order=14)
    def test_terminal_expl_org(self):
        # sql_execute()
        terminal_page = self.terminal_page
        terminal_page.refresh()
        terminal_page.switch_to_terminal_center()
        # terminal_page.add_new_terminal()
        with step("点击组织架构按钮"):
            terminal_page.click_terminal_org_tree()

        with step("折叠所有门店"):
            terminal_page.click_button('by_xpath,//i[@class="el-icon el-tree-node__expand-icon expanded"]')

        with step("展开所有门店"):
            terminal_page.click_button('by_xpath,//i[@class="el-icon el-tree-node__expand-icon"]')
        with step("收起抽屉"):
            terminal_page.refresh()

    @allure.title("查看设备中心-组织架构树，取消选择和全选所有门店")
    @pytest.mark.run(order=15)
    def test_expand_and_fold_org(self):
        terminal_page = self.terminal_page
        terminal_page.switch_to_terminal_center()
        time.sleep(0.5)
        with step("点击组织架构按钮"):
            terminal_page.click_terminal_org_tree()
        time.sleep(0.5)
        with step("点击取消全选按钮"):
            terminal_page.click_button('by_xpath,//i[@class="el-icon el-tree-node__expand-icon expanded"]/../label')
        time.sleep(0.5)
        with step("点击全选按钮"):
            terminal_page.click_button('by_xpath,//i[@class="el-icon el-tree-node__expand-icon expanded"]/../label')
        with step("收起抽屉"):
            terminal_page.refresh()

    @pytest.mark.usefixtures('terminal_set_up')
    @allure.title("查看设备中心-组织架构，切换到设备分组tab和组织架构tab")
    @pytest.mark.run(order=16)
    def test_switch_group_and_org(self):
        terminal_page = self.terminal_page
        terminal_page.switch_to_terminal_center()
        time.sleep(0.5)
        with step("点击组织架构按钮"):
            terminal_page.click_terminal_org_tree()
        time.sleep(0.5)
        with step("切换到设备分组tab上"):
            terminal_page.terminal_group_tab()
        time.sleep(0.5)
        with step("切换到组织架构tab上"):
            terminal_page.terminal_org_tab()
        with step("收起抽屉"):
            terminal_page.refresh()

    @pytest.mark.usefixtures("terminal_set_up")
    @allure.title("查看播放列表")
    @pytest.mark.run(order=17)
    def test_display_paly_bill(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        terminal_page.switch_to_terminal_center()
        # time.sleep(0.5)
        # terminal_page.add_new_terminal()
        time.sleep(0.5)
        with step("打开播放列表"):
            terminal_page.click_play_bill()
        terminal_page.refresh()

    @pytest.mark.usefixtures("terminal_set_up")
    @allure.title("打开节目列表")
    @pytest.mark.run(order=18)
    def test_display_program_list(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        terminal_page.switch_to_terminal_center()
        # terminal_page.add_new_terminal()
        time.sleep(0.5)
        with step("打开节目列表"):
            terminal_page.click_play_bill()
            terminal_page.program_list_tab()
        terminal_page.refresh()

    # @allure.title("播放列表种进行日期筛选")
    # @pytest.mark.run(order=19)
    # def test_play_bill_date(self):22
    #     terminal_page = self.terminal_page
    #     terminal_page.switch_to_terminal_center()
    #     terminal_page.add_new_terminal()
    #     #获取当天日期
    #
    #     from datetime import datetime, timedelta
    #
    #     # 获取今天的日期
    #     today = datetime.now()
    #
    #     # 计算明天的日期
    #     tomorrow = today + timedelta(days=1)
    #
    #     print(tomorrow.strftime('%Y-%m-%d'))
    #     with step("打开播放列表"):
    #         terminal_page.click_play_bill()
    #     with step("在播放列表种，筛选时间"):

    # # end_date=date.today()
    # today = time.strftime("%Y-%m-%d", time.localtime())
    # yesterday = time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400))
    # # print("start-time:",start_date)
    # # print("end_time:",end_date)
    # end_date = str(today)
    # start_date = str(yesterday)
    #

    # pass-----------+++++++++++++++++++++++++++++++++++++
    @pytest.mark.usefixtures('terminal_set_up')
    @allure.title("取消绑定设备")
    @pytest.mark.run(order=20)
    def test_cancel_bind_terminal(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        terminal_page.switch_to_terminal_center()
        time.sleep(0.5)
        with step("点击设备接入"):
            terminal_page.click_bind_terminal()
        time.sleep(0.5)
        with step("在绑定弹框上，点击取消按钮"):
            terminal_page.cancel_bind_terminal()

    @allure.title("绑定-接入设备")
    @pytest.mark.run(order=21)
    def test_add_terminal(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        # sys_page = self.sys_page
        # time.sleep(0.5)
        # sys_page.add_new_shop("test门店")
        with step("进入设备中心"):
            terminal_page.switch_to_terminal_center()
        time.sleep(0.5)
        with step("点击设备接入"):
            terminal_page.click_bind_terminal()
        with step("输入设备sn码"):
            terminal_page.input_terminal_id(self.sn_id)
        with step("输入设备名称"):
            terminal_page.input_terminal_name(self.sn_name)
        with step("先点击所属机构"):
            terminal_page.terminal_org()
        with step("在下拉框展开组织架构"):
            terminal_page.terminal_org_more()
        with step("在下拉框进行选择"):
            terminal_page.select_terminal_org()
        with step("点击保存按钮"):
            terminal_page.click_terminal_id()
            terminal_page.confirm_bind_terminal()
        # with step("清理数据，删除之前添加的门店"):
        #     sys_page.del_new_shop()

    #
    # @allure.title("批量绑定-接入设备")
    # @pytest.mark.run(order=22)
    # def test_batch_add_terminal(self):
    #     terminal_page = self.terminal_page
    #     sys_page = self.sys_page
    #     time.sleep(0.5)
    #     # sys_page.add_new_shop("test门店")
    #     with step("进入设备中心"):
    #         terminal_page.switch_to_terminal_center()
    #     time.sleep(0.5)
    #     for i in range(1,100):
    #         with step("点击设备接入"):
    #             terminal_page.click_bind_terminal()
    #         time.sleep(0.5)
    #         with step("输入设备sn码"):
    #             terminal_page.input_terminal_id(self.sn_id)
    #         time.sleep(0.5)
    #         with step("输入设备名称"):
    #             terminal_page.input_terminal_name(self.sn_name)
    #         time.sleep(0.5)
    #         with step("先点击所属机构"):
    #             terminal_page.terminal_org()
    #         time.sleep(0.5)
    #         with step("在下拉框展开组织架构"):
    #             terminal_page.terminal_org_more()
    #         time.sleep(0.5)
    #         with step("在下拉框进行选择"):
    #             terminal_page.select_terminal_org()
    #         time.sleep(0.5)
    #         with step("点击保存按钮"):
    #             terminal_page.click_terminal_id()
    #             terminal_page.confirm_bind_terminal()
    #     time.sleep(0.5)
    #     with step("清理数据，删除之前添加的门店"):
    #         sys_page.del_new_shop()

    # ++++++++++++++++++++++++++++++++++++pass
    @pytest.mark.usefixtures('clear_terminal_list')
    @pytest.mark.usefixtures('terminal_set_up')
    @allure.title("设备设置中，直接点击保存")
    @pytest.mark.run(order=23)
    def test_click_terminal_setting(self):
        terminal_page = self.terminal_page
        # terminal_page.switch_to_terminal_center()
        # terminal_page.bind_terminal()
        # sql_execute()
        time.sleep(0.5)
        terminal_page.click_terminal_setting()
        time.sleep(0.3)
        # terminal_page.click_terminal_id()
        terminal_page.save_terminal_setting()

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("重命名设备名称")
    @pytest.mark.run(order=24)
    def test_rename_terminal_name(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        # sql_execute()
        terminal_page.switch_to_terminal_center()
        # terminal_page.bind_terminal()
        time.sleep(0.3)
        terminal_page.add_new_terminal()
        terminal_name = random.randint(1000, 99999)
        try:
            time.sleep(0.5)
            with step("点击设备设置："):
                #//div[text()="设备00799"]/../../td[11]//img[@title="设置"]
                terminal_page.click_terminal_setting()
            with step("进行重命名"):
                terminal_page.rename_terminal(terminal_name)
            with step("进行保存"):
                terminal_page.save_terminal_setting()
        except ElementClickInterceptedException as e:
            raise e
        else:
            pass
        finally:
            terminal_page.refresh()

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("取消删除设备")
    @pytest.mark.run(order=25)
    def test_cancel_delete_terminal(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        terminal_page.switch_to_terminal_center()
        terminal_page.add_new_terminal()
        # sql_execute()
        time.sleep(0.5)
        with step("点击删除按钮，并进行确认删除"):
            terminal_page.click_delete_terminal()
            time.sleep(0.5)
            terminal_page.cancel_delete_terminal()

    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("删除设备成功")
    @pytest.mark.run(order=26)
    def test_success_delete_terminal(self):
        terminal_page = self.terminal_page
        # sql_execute()
        terminal_page.switch_to_terminal_center()
        terminal_page.add_new_terminal()
        time.sleep(0.5)
        with step("点击删除按钮"):
            terminal_page.click_delete_terminal()
        time.sleep(0.5)
        with step("删除弹框上面，点击确定按钮"):
            terminal_page.success_delete_terminal()


    # @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("查看设备信息")
    @pytest.mark.run(order=27)
    def test_terminal_info(self):
        # sql_execute()
        terminal_page = self.terminal_page
        terminal_page.switch_to_terminal_center()
        terminal_page.add_new_terminal()
        try:
            with step("点击设备id，查看设备信息"):
                terminal_page.terminal_info()

            info_locator = 'by_xpath,//span[text()="设备信息"]'
            assert terminal_page.element_exist(info_locator)

            with step("关闭设备信息弹框"):
                terminal_page.close_terminal_info()
        except:
            raise


    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("插播字幕，输入随机内容")
    @pytest.mark.run(order=28)
    def test_insert_subtile_random_text(self):
        terminal_page = self.terminal_page
        random_text = random.randint(999, 9999999999)
        # sql_execute()
        with step("各种前提："):
            time.sleep(0.5)
            terminal_page.add_real_terminal()
            time.sleep(0.5)
            terminal_page.click_more_button()
            time.sleep(0.5)
            terminal_page.insert_subtitle()
            time.sleep(0.5)
        subtitle_position_loca = ('by_xapth,//label[text()="播放位置"]')
        try:
            if terminal_page.element_exist(subtitle_position_loca):
                # with step("先点击插播内容弹框"):
                #     terminal_page.click_insert_subtitle_text()
                time.sleep(0.5)
                with step("输入随机的插播内容"):
                    terminal_page.input_insert_subtitle_text(random_text)
                with step("点击保存按钮"):
                    terminal_page.insert_subtitle_submit()
        except NoSuchElementException as e:
            print("非真实设备，无法发送插播字幕")
            with step("收起更多弹框"):
                terminal_page.click_more_button()

        finally:
            terminal_page.refresh()


    # @pytest.mark.usefixtures('terminal_set_up')
    # @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("在设备中心，点击更多按钮")
    @pytest.mark.run(order=29)
    def test_click_more_button(self):
        terminal_page = self.terminal_page
        # terminal_page.switch_to_terminal_center()
        # sql_execute()
        # terminal_page.refresh()
        # time.sleep(0.5)
        terminal_page.add_new_terminal()
        # all_terminal_ids = terminal_page.all_terminal_ids()

        with step("点击更多按钮"):
            terminal_page.click_more_button()
        all_func = terminal_page.more_function()
        print("获取；", all_func)
        all_fixed_functions = ["关机", "重启", "播放", "停止", "插播字幕", "节目克隆"]
        try:
            for fixed_function in all_fixed_functions:
                assert fixed_function in all_func
        except AssertionError as e:
            raise e
        finally:
            terminal_page.refresh()

    # @pytest.mark.skip(reason="这个功能谨慎操作")
    @pytest.mark.usefixtures('clear_terminal_list')
    @allure.title("下发关机指令")
    @pytest.mark.run(order=30)
    def test_reboot_terminal(self):
        terminal_page = self.terminal_page
        terminal_page.refresh()
        with step("两个前提：1、新增一台机器 2、新增一个门店  2、点击更多按钮 "):
            terminal_page.switch_to_terminal_center()
            terminal_page.add_real_terminal()
            terminal_page.click_more_button()

        time.sleep(2)
        with step("下发播放指令"):
            terminal_page.play_terminal()

        time.sleep(2)
        with step("下发停止指令"):
            terminal_page.stop_terminal()

        # time.sleep(2)
        # with step("下发实时监控指令"):
        #     terminal_page.real_time_monitor()

        time.sleep(2)
        with step("下发重启指令"):
            terminal_page.click_more_button()
            terminal_page.restart_terminal()

        time.sleep(3)
        # with step("下发关机指令"):
        #     terminal_page.turn_off_terminal()

        with step("下发插播字幕指令"):
            terminal_page.insert_subtitle()
        subtitle_position_loca = ('by_xapth,//label[text()="播放位置"]')
        try:
            if terminal_page.element_exist(subtitle_position_loca):
                # with step("先点击插播内容弹框"):
                #     terminal_page.click_insert_subtitle_text()
                time.sleep(0.5)
                with step("发送随机弹幕"):
                    terminal_page.input_insert_subtitle_text("自动化弹幕ing....")
                with step("点击保存按钮"):
                    terminal_page.insert_subtitle_submit()
        except NoSuchElementException as e:
            print("非真实设备，无法发送插播字幕")
            terminal_page.refresh()
        #
        # time.sleep(2)
        # with step("下发节目克隆指令"):
        #     terminal_page.program_clone()
        #     clone_ele = terminal_page.element_exist('by_xpath,//input[@placeholder="请搜索克隆设备"]')
        #     if clone_ele:
        #         with step("关闭节目克隆弹框"):
        #             terminal_page.cancel_program_clone()


        with step("收起更多弹框"):
            terminal_page.click_more_button()

