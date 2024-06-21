import time
import random
from time import sleep

import allure
import pytest
from allure_commons._allure import step

from pageobject.media_page import MediaPage
from pageobject.system_page import SystemPage
from common.set_up_media_list import MediaList


@pytest.fixture(scope='class')
def media_page(request, driver):
    media_page = MediaPage(driver)
    request.cls.media_page = media_page
    yield media_page


@pytest.fixture(scope="function", autouse=True)
def media_set_up(media_page):
    media_list = MediaList()
    media_list.delete_all_media()
    media_page.switch_to_media_center()


@allure.epic("项目hkc")
@allure.feature("media center")
@pytest.mark.usefixtures("media_page")
@pytest.mark.usefixtures("media_set_up")
class TestMediaCenter:
    @pytest.mark.run(order=1)
    @allure.title("点击素材中心")
    def test_open_upload_media_alert(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        time.sleep(2)
        with step("点击上传按钮"):
            media_page.click_up_load()
        time.sleep(2)
        with step("关闭上传弹框"):
            media_page.close_upload_media_alert()

    @pytest.mark.run(order=2)
    @allure.title("查看上传tooltips")
    def test_upload_media_tooltips(self):
        media_page = self.media_page
        media_page.refresh()
        media_page.switch_to_media_center()
        time.sleep(2)
        try:
            with step("点击上传按钮"):
                media_page.click_up_load()
            time.sleep(2)
            with step("鼠标hover到问号上面"):
                media_page.upload_media_tooltips()
            with step("关闭上传弹框"):
                time.sleep(1)
                media_page.close_upload_media_alert()
        except:
            raise
    filedatas = [
        "D:\\git\\ui_test\\data\\test001.jpeg",
        "D:\\git\\ui_test\\data\\test_mp4.mp4",
        "D:\\git\\ui_test\\data\\test_mp3.mp3"
    ]

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("filedatas", filedatas)
    @allure.title("上传单个文件")
    def test_upload_media_one_file(self, filedatas):
        media_page = self.media_page
        media_page.refresh()
        media_page.switch_to_media_center()
        time.sleep(2)
        with step("点击上传按钮"):
            media_page.click_up_load()
        time.sleep(2)
        # filepath = r"D:\\git\\ui_test\\data\\test001.jpeg"
        with step("点击上传文件按钮"):
            media_page.upload_media_file(filedatas)
        # time.sleep(8)
        progress_100_locator = 'by_xpath,//span[text()="100%"]'
        if media_page.element_exist(progress_100_locator):
            with step("关闭上传弹框"):
                time.sleep(1)
                media_page.close_upload_media_alert()
        # media_page.refresh()
        time.sleep(1)

    @pytest.mark.run(order=4)
    @allure.title("选择背景类型，进行素材上传")
    def test_upload_media_background_file(self):
        media_page = self.media_page
        media_page.refresh()
        media_page.switch_to_media_center()
        time.sleep(2)
        with step("点击上传按钮"):
            media_page.click_up_load()
        time.sleep(2)

        with step("选择文件类型为背景"):
            media_page.choose_file_type()
            media_page.upload_media_background()
        filepath = r"D:\\git\\ui_test\\data\\test001.jpeg"
        with step("点击上传文件按钮"):
            media_page.upload_media_file(filepath)
        # time.sleep(8)
        progress_100_locator = 'by_xpath,//span[text()="100%"]'
        if media_page.element_exist(progress_100_locator):
            with step("关闭上传弹框"):
                time.sleep(1)
                media_page.close_upload_media_alert()
        # media_page.refresh()
        time.sleep(2)

    @pytest.mark.run(order=5)
    @allure.title("选择屏幕贴类型，进行素材上传")
    def test_upload_media_background_file(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        time.sleep(2)
        with step("点击上传按钮"):
            media_page.click_up_load()
        time.sleep(2)

        with step("选择文件类型为背景"):
            media_page.choose_file_type()
            media_page.upload_screen_label()
        filepath = r"D:\\git\\ui_test\\data\\test001.jpeg"
        with step("点击上传文件按钮"):
            media_page.upload_media_file(filepath)
        # time.sleep(8)
        progress_100_locator = 'by_xpath,//span[text()="100%"]'
        if media_page.element_exist(progress_100_locator):
            with step("关闭上传弹框"):
                time.sleep(1)
                media_page.close_upload_media_alert()
        # media_page.refresh()
        time.sleep(2)

    @pytest.mark.run(order=6)
    @allure.title("上传指定文件夹下的所有文件")
    def test_upload_all_files(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        media_page.refresh()
        time.sleep(2)
        with step("点击上传按钮"):
            media_page.switch_to_media_center()
            media_page.click_up_load()
        time.sleep(2)
        # filepath = r"D:\\git\\ui_test\\data\\test001.jpeg"
        with step("点击上传文件按钮"):
            media_page.upload_all_files()
        time.sleep(15)
        progress_100_locator = 'by_xpath,//span[text()="100%"]'
        if media_page.element_exist(progress_100_locator):
            with step("关闭上传弹框"):
                time.sleep(1)
                media_page.close_upload_media_alert()
        # media_page.refresh()
        time.sleep(1)

    @pytest.mark.run(order=7)
    @allure.title("切换图片、视频、音频tab")
    def test_switch_all_tabs(self):
        # 前提：上传文件
        media_page = self.media_page
        media_page.switch_to_media_center()
        time.sleep(1)
        with step("点击上传按钮"):
            media_page.click_up_load()
        time.sleep(1)
        with step("点击上传文件按钮"):
            media_page.upload_all_files()
        time.sleep(1)
        progress_100_locator = 'by_xpath,//span[text()="100%"]'
        if media_page.element_exist(progress_100_locator):
            with step("关闭上传弹框"):
                time.sleep(1)
                media_page.close_upload_media_alert()
        # media_page.refresh()
        time.sleep(1)
        with step("切换到图片tab上"):
            media_page.switch_picture_tab()
        time.sleep(1)

        with step("切换到视频tab上"):
            media_page.switch_video_tab()
        time.sleep(1)

        with step("切换到音频tab上"):
            media_page.switch_music_tab()

    @pytest.mark.run(order=8)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("预览素材")
    def test_delete_multi_file(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        # 通用方法，进行素材上传
        media_page.upload_media()
        try:
            with step("1、先鼠标hover到素材上面"):
                media_page.hover_to_media()

        except Exception:
            media_page.upload_media()

        with step("点击预览按钮"):
            media_page.media_preview()

        time.sleep(1)
        with step("关闭预览按钮"):
            media_page.close_preview()

    @pytest.mark.run(order=9)
    @pytest.mark.usefixtures('media_set_up')
    @allure.title("查看图片详情")
    def test_media_detail_info(self):
        time.sleep(0.5)
        media_page = self.media_page
        media_page.refresh()
        media_page.switch_to_media_center()
        with step("前提：上传图片"):
            media_page.upload_media()

        with step("点击更多按钮"):
            media_page.click_media_more_button()

        with step("选择详情"):
            media_page.detail_info()

        time.sleep(3)
        with step("关闭详情弹框"):
            media_page.close_detail_info_alert()

    @pytest.mark.run(order=9)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("取消编辑素材")
    def test_cancel_edit(self):
        time.sleep(0.5)
        media_page = self.media_page
        media_page.refresh()
        media_page.switch_to_media_center()
        with step("前提：上传图片"):
            media_page.upload_media()

        with step("点击更多按钮"):
            media_page.click_media_more_button()

        with step("在更多功能处，点击编辑按钮"):
            media_page.edit_info()

        with step("取消编辑"):
            media_page.cancel_edit()

    @pytest.mark.run(order=10)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("重命名文件名称")
    def test_rename_file(self):
        media_page = self.media_page
        media_page.switch_to_media_center()

        with step("前提：上传图片"):
            media_page.upload_media()

        time.sleep(0.5)
        with step("点击更多按钮"):
            media_page.click_media_more_button()

        with step("在更多功能处，点击编辑按钮"):
            media_page.edit_info()

        with step("重命名文件名"):
            media_page.rename_file("new001")

        with step("编辑成功后，点击保存"):
            media_page.confirm_edit()

    @pytest.mark.run(order=11)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("取消删除单个素材")
    def test_cancel_delete(self):
        time.sleep(0.5)
        media_page = self.media_page
        media_page.switch_to_media_center()
        with step("前提：上传图片"):
            media_page.upload_media()

        with step("点击更多按钮"):
            media_page.click_media_more_button()

        with step("点击删除按钮"):
            media_page.more_click_delete()

        with step("在删除弹框上面点击取消按钮"):
            media_page.cancel_delete()

    @pytest.mark.run(order=12)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("在删除单个素材弹框，关闭删除弹框")
    def test_close_delete_alert(self):
        time.sleep(0.5)
        media_page = self.media_page
        media_page.switch_to_media_center()
        with step("前提：上传图片"):
            media_page.upload_media()

        with step("点击更多按钮"):
            media_page.click_media_more_button()

        with step("点击删除按钮"):
            media_page.more_click_delete()

        with step("关闭删除弹框"):
            media_page. close_delete_alert()

    @pytest.mark.run(order=13)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("确认删除单个素材，删除成功")
    def test_delete_success(self):
        time.sleep(0.5)
        media_page = self.media_page
        media_page.switch_to_media_center()
        with step("前提：上传图片"):
            media_page.upload_media()

        with step("点击更多按钮"):
            media_page.click_media_more_button()

        with step("点击删除按钮"):
            media_page.more_click_delete()

        with step("在删除弹框上面点击取消按钮"):
            media_page.confirm_delete_media()

    @pytest.mark.run(order=14)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("取消批量删除")
    def test_cancel_multi_delete(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        # 通用方法，进行素材上传
        media_page.upload_media()
        with step("1、先鼠标hover到素材上面"):
            media_page.hover_to_media()

        with step("2、选择当前素材"):
            media_page.choose_media()

        with step("点击批量删除按钮"):
            media_page.multi_delete_media()

        with step("取消删除"):
            media_page.cancel_delete()

    @pytest.mark.run(order=15)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("关闭批量删除弹框")
    def test_close_multi_delete(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        # 通用方法，进行素材上传
        media_page.upload_media()
        with step("1、先鼠标hover到素材上面"):
            media_page.hover_to_media()

        with step("2、选择当前素材"):
            media_page.choose_media()

        with step("点击批量删除按钮"):
            media_page.multi_delete_media()

        with step("关闭批量删除弹框"):
            media_page.close_delete_alert()

    @pytest.mark.run(order=16)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("批量删除成功")
    def test_success_delete_multi_file(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        # 通用方法，进行素材上传
        media_page.upload_media()
        with step("1、先鼠标hover到素材上面"):
            media_page.hover_to_media()

        with step("2、选择当前素材"):
            media_page.choose_media()

        with step("点击批量删除按钮"):
            media_page.multi_delete_media()

        with step("确认删除"):
            media_page.confirm_delete_media()

    @pytest.mark.run(order=17)
    @pytest.mark.usefixtures("media_set_up")
    @allure.title("单个素材发布")
    def test_cancel_multi_delete(self):
        media_page = self.media_page
        media_page.switch_to_media_center()
        # 通用方法，进行素材上传
        media_page.upload_media()
        with step("1、先鼠标hover到素材上面"):
            media_page.hover_to_media()

        with step("2、选择当前素材"):
            media_page.choose_media()

        with step("3.点击批量发布按钮"):
            media_page.multi_release()



