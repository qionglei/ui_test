import random
import time

from allure_commons._allure import step
from selenium.common import ElementClickInterceptedException, ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basepage.base_page import BasePage
from pageobject.media_page import MediaPage


class ProgramPage(MediaPage):
    def switch_to_program_management(self):
        """
        侧边栏，切换到节目管理
        :return:
        """
        media_center_locator = 'by_xpath,//div[text()=" 节目管理"]'
        try:

            clickable_ele = self.get_element('by_xpath,//div[text()=" 节目管理"]/../..')
            get_classmethod = clickable_ele.get_attribute("class")
            if get_classmethod == "el-tree-node is-current is-focusable":
                pass
            else:
                self.click(media_center_locator)

        except Exception:
            self.refresh()
            # time.sleep(1)
            self.click(media_center_locator)

    # ******************************新增一个普通节目*****************************************
    def create_general_program(self):
        """
        通用方法：创建一个普通节目
        """
        try:
            self.switch_to_program_management()
            random_name = random.randint(1, 100)
            random_program_name = "test_横屏普通节目" + str(random_name)
            with step("点击创建节目"):
                self.click_create_program()
            with step("输入节目名称（普通节目）"):
                self.input_program_name(random_program_name)

            with step( "选择屏幕方向"):
                self.screen_direction("x")

            try:
                with step( "选择分辨率"):
                    self.click_resolution()
                    time.sleep(0.3)
                    self.choose_screen("1920x1080")
            except ElementNotInteractableException:
                time.sleep(0.3)
                with step( "选择分辨率"):
                    self.click_resolution()
                    time.sleep(0.3)
                    self.choose_screen("1920x1080")

            with step( "点击保存按钮"):
                self.confirm_create_program()

            try:
                """
                捕捉异常，如果提交时提示分辨率没有填，则重新执行选择
                """
                error_text = 'by_xpath,//div[@class="el-form-item__error" and text()="请选择分辨率"]'
                if error_text:
                    with step( "选择分辨率"):
                        self.click_resolution()
                        time.sleep(0.3)
                        self.choose_screen("1920x1080")
            except NoSuchElementException:
                pass

            with step("在编辑器中进行保存"):
                self.click('by_xpath,//span[text()="保存"]')
                time.sleep(2)
                self.comeback_general_program()
                time.sleep(0.5)
                self.refresh()
        except ElementNotInteractableException as e:
            raise e

        return random_program_name

    # ******************************新增一个联屏节目*****************************************

    def create_relevance_program(self):
        """
        通用方法：创建一个联屏节目
        :return:
        """
        self.switch_to_program_management()
        random_name = random.randint(1, 100)
        random_program_name = "test_横屏联屏节目" + str(random_name)
        # "点击创建节目"
        self.click_create_program()
        # "输入节目名称（联屏节目）"
        self.input_program_name(random_program_name)

        self.row_numbers(2)
        self.col_numbers(2)

        # "选择屏幕方向"
        self.screen_direction("x")

        # "选择素材"
        self.click_resolution()
        self.choose_relevance_media()

        # 上传一个素材
        self.upload_media()

        # 选择一个素材
        self.hover_to_media()
        self.choose_media()

        # 选择好素材后，点击确认按钮
        # 忽略方法名，没有用错
        self.confirm_delete_media()

        # 再次点击确认按钮，生成一个联屏节目
        self.confirm_delete_program()
        time.sleep(3)
        self.refresh()
        time.sleep(3)

        return random_program_name

    def click_create_program(self):
        """
        在节目管理中，点击创建节目按钮
        :return:
        """
        create_program_locator = 'by_xpath,//div[text()="创建节目"]/../img'
        create_program_ele = self.element_exist(create_program_locator)
        # try:
        #     if create_program_ele:
        #         self.click(create_program_locator)
        #     else:
        #         self.refresh()
        #         time.sleep(0.5)
        #         self.click(create_program_locator)
        # except ElementClickInterceptedException:
        #     print("创建节目失败")
        #
        # finally:
        #     self.refresh()

        self.click(create_program_locator)

    def input_program_name(self, pragram_name):
        """
        创建普通节目弹框中，输入节目名称
        :return:
        """
        program_name_locator = 'by_xpath,//input[@placeholder="请输入节目名称"]'
        self.input(program_name_locator, pragram_name)

    def screen_direction(self, direction):
        """
        设置屏幕方向。传入x代表是横屏，传入y是代表竖屏,z是代表自定义
        注意：联屏没有自定义
        :param direction:
        :param args:
        :return:
        """
        x_locator = 'by_xpath,//span[text()="横屏"]/../div'
        y_locator = 'by_xpath,//span[text()="竖屏"]/../div'
        z_locator = 'by_xpath,//span[text()="自定义"]/../div'
        if direction == "x":
            self.click(x_locator)
        elif direction == "y":
            self.click(y_locator)
        else:
            self.click(z_locator)

    def click_resolution(self):
        """
        点击分辨率，唤起下拉框
        :return:
        """
        resolution_locator = 'by_xpath,//span[text()="分辨率"]/../..//input[@placeholder="请选择"]'
        self.click(resolution_locator)

    def choose_screen(self, resolution="1920x1080"):
        """
        创建节目时，选择不同的分辨率
        :param resolution:
        :return:
        """
        if resolution == "1920x1080":
            self.click('by_xpath,//span[text()="1920x1080"]')
        elif resolution == "3840x2160":
            self.click('by_xpath,//span[text()="3840x2160"]')
        elif resolution == "1366x768":
            self.click('by_xpath,//span[text()="1366x768"]')
        elif resolution == "1280x720":
            self.click('by_xpath,//span[text()="1280x720"]')
        elif resolution == "1080x1920":
            self.click('by_xpath,//span[text()="1080x1920"]')
        elif resolution == "1280x720":
            self.click('by_xpath,//span[text()="1280x720"]')
        elif resolution == "768x1366":
            self.click('by_xpath,//span[text()="768x1366"]')
        elif resolution == "720x1280":
            self.click('by_xpath,//span[text()="720x1280"]')
        else:
            self.click('by_xpath,//span[text()="1920x1080"]')

    def input_screen(self, resolution="1920x1080"):
        wide = str(resolution.split("x")[0])
        high = str(resolution.split("x")[1])
        wide_locator = 'by_xpath,//input[@placeholder="请输入分辨率宽"]'
        high_locator = 'by_xpath,//input[@placeholder="请输入分辨率高"]'
        wide_ele = self.get_element(wide_locator)
        high_ele = self.get_element(high_locator)
        wide_ele.send_keys(wide)
        high_ele.send_keys(high)

    def cancel_create_program(self):
        """
        取消创建普通节目
        :return:
        """
        self.click('by_xpath,//span[text()="取消"]')

    def confirm_create_program(self):
        """
        确定创建节目:普通节目、联屏节目
        :return:
        """
        self.click('by_xpath,//span[text()=" 确定 "]')

    def save_general_program(self):
        """
        在编辑器中，进行保存
        :return:
        """

        self.click('by_xpath,//span[text()="保存"]')

    def comeback_general_program(self):
        """
        点击返回按钮
        :return:
        """
        self.click('by_xpath,//span[text()="返回"]')

    def close_create_pragram(self):
        """
        关闭创建弹框
        :return:
        """
        self.click('by_xpath,//span[text()="创建节目"]/../button/i')

    # ========================================创建联屏节目=============================================

    def relevance_program_tab(self):
        """
        在创建节目弹框中，切换到联屏节目tab上
        :return:
        """
        self.click('by_xpath,//div[@class="pval"]/div[@class="btn" and text()="联屏节目"]')

    def row_numbers(self, nums):
        """
        联屏节目，输入行数
        :param nums:
        :return:
        """
        row_locator = 'by_xpath,//span[text()="行"]/..//input'
        self.input(row_locator, nums)

    def col_numbers(self, nums):
        """
        联屏节目，输入列数
        :param nums:
        :return:
        """
        col_locator = 'by_xpath,//span[text()="列"]/..//input'
        self.input(col_locator, nums)

    def row_decrease(self):
        """
        联屏节目，行数减少
        :return:
        """
        self.click('by_xpath,//span[text()="行"]/..//span[@aria-label="el.inputNumber.decrease"]')

    def row_increase(self):
        """
        联屏节目，行数减少
        :return:
        """
        self.click('by_xpath,//span[text()="行"]/..//span[@aria-label="el.inputNumber.increase"]')

    def col_decrease(self):
        """
        联屏节目，行数减少
        :return:
        """
        self.click('by_xpath,//span[text()="列"]/..//span[@aria-label="el.inputNumber.decrease"]')

    def col_increase(self):
        """
        联屏节目，行数减少
        :return:
        """
        self.click('by_xpath,//span[text()="列"]/..//span[@aria-label="el.inputNumber.increase"]')

    def choose_relevance_media(self):
        """
        联屏节目：选择节素材进行分割
        :return:
        """
        choose_media_locator = 'by_xpath,//div[@class="rect"]'
        self.click(choose_media_locator)

    def hover_to_program(self, name):
        """
        素材列表中，鼠标hover到素材遮罩上面去
        :return:
        """
        driver = self.driver
        hover_locator = f'by_xpath,//div[@title="{name}"]/preceding::div[@class="mask radiusAll"]'
        if self.element_exist(hover_locator):
            # wait = WebDriverWait(driver, 10)
            # click_element = wait.until(EC.visibility_of_element_located((By.XPATH, hover_locator)))
            ele = self.get_element(hover_locator)
            # print("ele:****************", ele)
            ActionChains(driver).move_to_element(ele).perform()
        else:
            print("hover到节目上。蒙版mask不可见")
        time.sleep(1)

    def hover_to_first_program(self):
        all_mask = 'by_xpath,//div[@class="img-box"]'
        all_mask_ele = self.get_elements(all_mask)
        # print("all_mask_ele::::", all_mask_ele)
        first_mask_ele = all_mask_ele[0]
        # print("first_mask_ele:::::", first_mask_ele)
        ActionChains(self.driver).move_to_element(first_mask_ele).perform()

    def choose_first_program(self):
        choose_first_program_locator = 'by_xpath,//div[@class="mask radiusAll"]/img[2]'
        # all_eles = self.get_elements(choose_first_program_locator)
        # first_ele = all_eles[1]
        # ActionChains(self.driver).move_to_element(first_ele).click(first_ele).perform()
        self.click(choose_first_program_locator)

    def choose_program(self, name):
        """
        选择节目
        :return:
        """
        # 判断对号是否可见,等待可见后，再进行操作
        driver = self.driver
        is_selectable = f'by_xpath,//div[@title="{name}"]/preceding::div[@class="mask radiusAll"]/img[2]'

        if self.element_exist(is_selectable):
            wait = WebDriverWait(driver, 10)  # 等待最多10秒
            click_element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@title="{name}"]/preceding::div['
                                                                             f'@class="mask radiusAll"]/img[2]')))
            click_element.click()
        else:
            pass

    def multi_delete_program(self):
        """
        点击批量删除按钮
        :return:
        """
        self.click('by_xpath,//div[@class="bar-tools"]/div/div[2]/span[text()="刪除"]')

    def multi_delete_confirm(self):
        """
        确认删除弹框中，点击确认
        :return:
        """
        self.click('by_xpath,//span[text()=" 确定 "]')

    def multi_delete_cancel(self):
        """
        确认删除弹框中，点击取消
        :return:
        """
        self.click('by_xpath,//span[text()="取消"]')

    def program_more_button(self):
        """
        在节目列表中，点击更多按钮
        :return:
        """
        program_more_button_locator = 'by_xpath,// div[ @class ="pop"] / div[@ class ="el-dropdown"] / span'
        self.click(program_more_button_locator)

    def program_copy_button(self):
        """
        在节目列表中，点击更多-引用按钮
        :return:
        """
        try:
            program_copy_button_locator = 'by_xpath,//span[text()="引用"]'
            self.click(program_copy_button_locator)

        except ElementNotInteractableException as e:
            raise e

    def program_copy_name(self, copy_name):
        """
        节目管理页面，引用节目时，输入节目名称
        :return:
        """
        program_copy_name_locator = 'by_xpath,//input[@placeholder="请输入名称"]'
        # self.clear(program_copy_name_locator)
        self.input(program_copy_name_locator, copy_name)

    def click_rename_program(self):
        """
        重命名节目
        :return:
        """
        self.click('by_xpath,//span[text()="重命名"]')

    def rename_program_name(self,name):
        """
        进行节目的重命名,先清空 再输入新的名字
        :return:
        """
        rename_locator = 'by_xpath,//input[@placeholder="请输入名称"]'
        self.clear(rename_locator)
        self.input(rename_locator,name)


    def close_delete_program_alert(self):
        """
        关闭删除弹框
        :return:
        """
        self.click('by_xpath,//span[@class="el-dialog__title"]/..//i')

    def confirm_delete_program(self):
        """
        确认删除
        :return:
        """

        self.click('by_xpath,//span[text()=" 确定 "]')
