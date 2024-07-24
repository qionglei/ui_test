import time

from allure_commons._allure import step
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basepage.base_page import BasePage
from conftest import driver


class MediaPage(BasePage):
    def switch_to_media_center(self):
        """
        侧边栏，切换到素材中心
        :return:
        """
        time.sleep(0.3)
        try:
            media_center_locator = 'by_xpath,//div[text()=" 素材中心"]'

            clickable_ele = self.get_element('by_xpath,//div[text()=" 素材中心"]/../..')
            get_classmethod = clickable_ele.get_attribute("class")
            # if get_classmethod == "el-tree-node is-current is-focusable":
            #     pass
            # else:
            #     self.click(media_center_locator)
            # time.sleep(0.5)
            if get_classmethod == "el-tree-node is-focusable":
                self.click(media_center_locator)
        except Exception as e:
            self.refresh()

    def upload_media(self):
        """
        封装一个上传文件的通用方法
        :return:
        """
        current_window_size = self.get_window_size()
        print("当前的size为：", current_window_size)
        self.maxsize_window()
        # self.switch_to_media_center()   #去掉是因为在联屏姐节目的弹框中，也可以进行上传
        try:
            with step("点击上传按钮"):
                self.click_up_load()
                time.sleep(0.5)
            filepath = r"D:\\git\\ui_test\\data\\test001.jpeg"
            with step("进行文件上传"):
                self.upload_media_file(filepath)
                time.sleep(5)
            progress_100_locator = 'by_xpath,//span[text()="100%"]'
            with step("当进度为100%时，则关闭上传弹框"):
                if self.element_exist(progress_100_locator):
                    time.sleep(1)
                    self.close_upload_media_alert()
                time.sleep(1)
        except Exception:
            raise
        finally:
            self.set_window_size(*current_window_size)

    def create_program_and_upload_media(self):
        """
        封装一个上传文件的通用方法
        :return:
        """
        try:
            with step("点击上传按钮"):
                self.click_up_load_from_program()
                time.sleep(0.5)
            filepath = r"D:\\git\\ui_test\\data\\test001.jpeg"
            with step("进行文件上传"):
                self.upload_media_file(filepath)
                time.sleep(5)
            progress_100_locator = 'by_xpath,//span[text()="100%"]'
            with step("当进度为100%时，则关闭上传弹框"):
                if self.element_exist(progress_100_locator):
                    time.sleep(1)
                    self.close_upload_media_alert()
                time.sleep(1)
        except Exception:
            raise

    def click_up_load(self):
        """
        先判断是不是有搜索按钮，再进行操作
        在素材中心，点击“上传”按钮，隐式等待
        :return:
        """
        search_locator = 'by_xpath,//span[text()="搜索"]'
        search_ele = self.element_exist(search_locator)
        if search_ele:
            wait = WebDriverWait(self.driver, 10)
            my_element = '//span[text()="上传"]'
            element = wait.until(EC.element_to_be_clickable((By.XPATH, my_element)))
            element.click()
        else:
            self.switch_to_media_center()
            self.refresh()
            time.sleep(0.3)

            wait = WebDriverWait(self.driver, 10)
            my_element = '//span[text()="上传"]'
            element = wait.until(EC.element_to_be_clickable((By.XPATH, my_element)))
            element.click()

    def click_up_load_from_program(self):
        """
        在素材中心，点击“上传”按钮
        :return:
        """
        # try:
        #     up_load_locator = 'by_xpath,//span[text()="上传"]/../div'
        #     self.click(up_load_locator)
        # except Exception:
        #     raise

        up_load_locator = 'by_xpath,//span[text()="上传"]'
        self.click(up_load_locator)

    def upload_media_file(self, filepath):
        """
        上传文件弹框中，点击上传按钮，单次仅上传一个文件
        :param filepath:
        :return:
        """
        open_up_load = 'by_xpath,//input[@class="el-upload__input"]'
        up_load_ele = self.get_element(open_up_load)
        time.sleep(2)
        up_load_ele.send_keys(filepath)

    def upload_all_files(self):
        """
        上传指定文件下的所有文件
        :return:
        """
        import os
        folder = 'D:\\ui\\data'
        file_name_list = os.listdir(folder)
        path_list = [os.path.join(folder, x) for x in file_name_list]
        path_split_by_newline = '\n'.join(path_list)
        file_input = self.get_element('by_xpath,//input[@class="el-upload__input"]')
        file_input.send_keys(path_split_by_newline)

    def close_upload_media_alert(self):
        """
        关闭上传弹框
        :return:
        """
        close_button = 'by_xpath,//div[text()="上传列表"]/../button/i'
        self.click(close_button)

    def upload_media_tooltips(self):
        """
        上传文件弹框上，鼠标hover到tooltips
        :return:
        """
        self.hover('by_xpath,//img[@class="help el-tooltip__trigger el-tooltip__trigger"]')

    def choose_file_type(self):
        """
        在传弹框上，点击“请选择图片类型”
        :return:
        """
        self.click('by_xpath,//input[@placeholder="请选择图片类型"]')

    def upload_background(self):
        """
        选择背景，进行上传
        :return:
        """
        self.click('by_xpath,//span[text()="背景"]')

    def upload_screen_label(self):
        """
        选择背景，进行上传
        :return:
        """
        self.click('by_xpath,//span[text()="屏幕贴"]')

    # ==========================切换类型tab===============================
    def switch_picture_tab(self):
        """
        切换到图片tab
        :return:
        """
        self.click('by_xpath,//span[text()="图片"]')

    def switch_video_tab(self):
        """
        切换到视频tab
        :return:
        """
        self.click('by_xpath,//span[text()="视频"]')

    def switch_music_tab(self):
        """
        切换到音频tab
        :return:
        """
        self.click('by_xpath,//span[text()="音频"]')

    def click_delete_media(self):
        """
        点击删除按钮
        :return:
        """
        self.click('by_xpath,//span[text()="删除"]')

    def click_media_more_button(self):
        """
        点击素材右下角的更多按钮
        :return:
        """
        try:
            all_more_buttons = 'by_xpath,//div[@class="info-bar"]/..//div[@class="tool"]//img'
            all_more_button_ele = self.get_elements(all_more_buttons)
            if all_more_button_ele:
                first_more_button = all_more_button_ele[0]
                ActionChains(self.driver).move_to_element(first_more_button).click(first_more_button).perform()
        except Exception:
            raise

    def detail_info(self):
        """
        查看图片详情
        :return:
        """
        try:
            detail_info_locator = 'by_xpath,//span[text()="详情"]'
            detail_info_eles = self.get_elements(detail_info_locator)
            first_detail_info = detail_info_eles[0]
            ActionChains(self.driver).move_to_element(first_detail_info).click(first_detail_info).perform()

        except ElementNotInteractableException:
            my_element = '//span[text()="详情"]'

            wait = WebDriverWait(self.driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, my_element)))
            element.click()

    def close_detail_info_alert(self):
        """
        1、先鼠标hover到遮罩上面去
        2、再进行点击操作
        :return:
        """
        self.click('by_xpath,//span[text()="图片详情"]/../button[@class="el-dialog__headerbtn"]')

    def edit_info(self):
        """
        在更多中，点击编辑按钮
        """
        try:
            edit_info_locator = 'by_xpath,//span[text()="编辑"]'
            edit_info_eles = self.get_elements(edit_info_locator)
            first_detail_info = edit_info_eles[0]
            ActionChains(self.driver).move_to_element(first_detail_info).click(first_detail_info).perform()
        except ElementNotInteractableException:
            my_element = '//span[text()="编辑"]'
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, my_element)))
            element.click()

    def cancel_edit(self):
        """
        取消编辑
        :return:
        """
        self.click('by_xpath,//span[text()=" 取消 "]')

    def confirm_edit(self):
        """
        保存修改
        :return:
        """
        self.click('by_xpath,//span[text()=" 保存 "]')

    def rename_file(self, newname):
        """
        重命名文件名称
        :param newname:
        :return:
        """
        rename_locator = 'by_xpath,//input[@placeholder="名称最多不超过20个字"]'
        self.input(rename_locator, newname)

    def more_click_delete(self):
        """
        更多按钮处，进行删除
        :return:
        """
        self.click('by_xpath,//div[@class="pop-item"]//span[text()="删除"]')

    def cancel_delete(self):
        """
        取消删除素材
        :return:
        """
        self.click('by_xpath,//span[text()="取消"]')

    def close_delete_alert(self):
        """
        在删除弹框点击关闭按钮，关闭弹框
        :return:
        """

        self.click('by_xpath,//i[@class="el-icon el-message-box__close"]')

    def confirm_delete_media(self):
        """
        确认删除素材
        :return:
        """
        self.click('by_xpath,//span[text()="确定"]')

    # ========================批量操作=============================

    def hover_to_media(self):
        """
        素材列表中，鼠标hover到素材遮罩上面去
        """
        hover_locator = 'by_xpath,//div[@class="img-box"]'
        try:
            eles = self.get_elements(hover_locator)
            first_ele = eles[0]
            ActionChains(self.driver).move_to_element(first_ele).perform()
        except IndexError:
            """
            当列表为空时，则进行再次上传
            """
            # no_data_errpr = self.element_exist('by_xpath,//div[@class="content"]/div[@class="empty-box"]')

            self.upload_media()
            eles = self.get_elements(hover_locator)
            first_ele = eles[0]
            ActionChains(self.driver).move_to_element(first_ele).perform()
        time.sleep(1)

    def choose_media(self):
        """
        选择素材
        :return:
        """
        # 判断对号是否可见,等待可见后，再进行操作
        driver = self.driver
        all_selectable = 'by_xpath,//div[@class="mask"]/div/img'
        # if self.element_exist(all_selectable):
        #     wait = WebDriverWait(driver, 10)  # 等待最多10秒
        #     click_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mask"]/div/img')))
        #     click_element.click()
        # else:
        #     pass
        all_selectable_elements = self.get_elements(all_selectable)
        first_selectable_element = all_selectable_elements[0]
        try:
            # self.click(first_selectable_element)
            ActionChains(driver).move_to_element(first_selectable_element).click(first_selectable_element).perform()
        except Exception:
            # 异常捕捉："当前列表没有节目"
            # 此时就需要生成节目了
            self.create_program_and_upload_media()

            ActionChains(driver).move_to_element(first_selectable_element).click(first_selectable_element).perform()

    def media_preview(self):
        """
        素材预览
        :return:
        """
        driver = self.driver
        preview_loactor = 'by_xpath,//div[@class="mask"]/img'
        if self.element_exist(preview_loactor):
            wait = WebDriverWait(driver, 10)
            click_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mask"]/img')))
            click_element.click()

    def close_preview(self):
        """
        关闭预览功能
        1、先鼠标hover到预览的图片上
        2、找到关闭按钮
        3、点击关闭按钮，进行关闭预览
        :return:
        """
        # preview_place = 'by_xpath,//div[@class="main"]'

        # 鼠标hover到素材上面，目的：等待关闭按钮出现
        preview_place = 'by_xpath,//div[@class="dialogImg"]'
        place_ele = self.get_element(preview_place)
        ActionChains(self.driver).move_to_element(place_ele).click(place_ele).perform()

        # 关闭按钮是否可见
        close_preview_locator = 'by_xpath,//i[@class="el-icon closeBtn"]/*'
        try:
            if self.element_exist(close_preview_locator):
                self.click(close_preview_locator)
            else:
                print("关闭预览按钮不可见")
        except ElementNotInteractableException as e:
            raise e

    def multi_delete_media(self):
        """

        :return:
        """
        multi_delete_media = 'by_xpath,//div[@class="material-search-right"]//span[text()="删除"]'
        self.click(multi_delete_media)

    def multi_release(self):
        """
        批量发布
        :return:
        """
        self.click('by_xpath,//span[text()="发布"]')

        # 创建文件夹

    def click_mkdir(self):
        """
        批量操作：点击新建文件夹按钮
        :return:
        """
        try:
            mkdir_locator = 'by_xpath,//span[text()="文件夹"]'
            self.click(mkdir_locator)
        except ElementClickInterceptedException as e:
            raise e

    def dir_name(self, dir_name):
        """
        在新建文件夹弹框内，输入文件夹名称
        :param dir_name:
        :return:
        """
        input_dir_name = 'by_xpath,//input[@placeholder="请输入名称(最多20个字)"]'
        self.input(input_dir_name, dir_name)

    def confirm_mkdir(self):
        """
        在新建文件夹弹框内，点击确认按钮
        :return:
        """
        confirm_button_locator = 'by_xpath,//input[@placeholder="请输入名称(最多20个字)"]'
        self.click(confirm_button_locator)
