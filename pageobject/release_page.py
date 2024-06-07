import datetime
import random
import time

from selenium.common import ElementNotInteractableException, ElementClickInterceptedException

from basepage.base_page import BasePage
from selenium.webdriver import Keys, ActionChains


class ReleasePage(BasePage):
    def switch_to_release_management(self):
        """
        侧边栏切换到发布管理
        :return:
        """
        release_management_locator = 'by_xpath,//div[text()=" 发布管理"]'
        clickable_ele = self.get_element('by_xpath,//div[text()=" 发布管理"]/../..')
        get_classmethod = clickable_ele.get_attribute("class")
        if get_classmethod == "el-tree-node is-current is-focusable":
            pass
        else:
            self.click(release_management_locator)

    def choose_terminal(self):
        """
        发布管理-选设备
        """
        # try:
        #     choose_terminal_locator = 'by_xpath,//div[text()="选设备"]/../img'
        #     self.click(choose_terminal_locator)
        # except Exception:
        #     raise

        choose_terminal_locator = 'by_xpath,//div[text()="选设备"]/../img'
        self.click(choose_terminal_locator)

    def program_edit(self):
        """
        发布管理-节目编排
        :return:
        """
        program_edit_locator = 'by_xpath,//div[text()="节目编排"]'
        program_edits =self.get_elements(program_edit_locator)
        program_edit_ele = program_edits[0]
        ActionChains(self.driver).move_to_element(program_edit_ele).click(program_edit_ele).perform()

    def selection_strategy(self):
        """
        发布管理-选择策略
        :return:
        """
        selection_strategfy_locator = 'by_xpath,//div[text()="选择策略"]'
        self.click(selection_strategfy_locator)

    def release_general_program(self):
        """
        普通节目发布
        """
        release_general_program_locator = 'by_xpath,//div[text()="发布"]'
        self.click(release_general_program_locator)
        # 如果有设备过期，则点击"知道了"按钮
        # know_alert ='by_xpath,//span[text()="知道了"]'
        # know_alert_ele = self.get_element(know_alert)
        # if not know_alert_ele:
        #     pass
        # else:
        #     self.click(know_alert)

    def set_playbill_name(self, playbill_name):
        """
        重命名节目单
        :param name:
        :return:
        """
        playbill_name_locator = 'by_xpath,//span[text()="节目单名称："]/..//input[@class="el-input__inner"]'
        self.input(playbill_name_locator, playbill_name)

    def temporary_storage(self):
        """
        发布管理页面。点击暂存按钮
        :return:
        """
        temporary_storage_locator = 'by_xpath,//span[text()="暂存"]'
        self.click(temporary_storage_locator)

    #  ============================发布策略======================================================
    def is_silence(self, is_silence=True):
        """
        发布策略：是否静音
        :param is_silence:True代表静音、False代表不静音
        :return:
        """
        if is_silence == "True":
            is_silence_true_locator = 'by_xpath,//span[text()="是"]'
            self.click(is_silence_true_locator)
        elif is_silence == "False":
            is_silence_false_locator = 'by_xpath,//span[text()="否"]'
            self.click(is_silence_false_locator)
        else:
            raise TypeError

    def display_priority(self, priority=2):
        """
        发布策略：优先级
        :param priority: 1:高   2：中    3：低
        :return:
        """
        if priority == 1:
            priority_high = 'by_xpath,//span[text()="高"]'
        elif priority == 2:
            priority_high = 'by_xpath,//span[text()="中"]'
        elif priority == 3:
            priority_high = 'by_xpath,//span[text()="低"]'
        else:
            raise TypeError

    def display_strategy(self, strategy=2):
        """
        发布策略，覆盖
        :param strategy: 1：覆盖 2；追加
        :return:
        """
        if strategy == 1:
            strategy_cover = 'by_xpath,//span[text()="覆盖"]'
            self.click(strategy_cover)
        elif strategy == 2:
            strategy_add = 'by_xpath,//span[text()="追加"]'
        else:
            raise TypeError

    def dismiss_release_strategy(self):
        """
        发布策略弹框，点击取消按钮
        :return:
        """
        self.click('by_xpath,//span[text()="取消"]')

    def confirm_release_strategy(self):
        """
        布策略弹框，点击确定按钮
        :return:
        """
        confirm_button = 'by_xpath,//span[text()="确定"]'
        confirm_button_eles = self.get_elements(confirm_button)
        if confirm_button_eles:
            confirm_button_ele = confirm_button_eles[0]
            ActionChains(self.driver).move_to_element(confirm_button_ele).click(confirm_button_ele).perform()

    def close_relase_strategy(self):
        """
         发布策略弹框，点击关闭按钮
        :return:
        """
        close_locator = 'by_xpath,//span[text()="发布策略"]/../button[@aria-label="el.dialog.close"]'
        self.click(close_locator)

    # ========================选设备=====================================================
    def choose_one_terminal(self):
        """
        在发布管理中，点击选设备
        :return:
        """
        choose_first_terminal = 'by_xpath,//span[@class="el-checkbox__input"]/span[@class="el-checkbox__inner"]'
        self.click(choose_first_terminal)

    def  switch_terminal_group(self):
        """
        在选设备抽屉，切换到‘设备分组’tab上
        :return:
        """
        terminal_group_locator = 'by_xpath,//div[@class="tab-item"]'
        self.click(terminal_group_locator)

    def switch_terminal_framework(self):
        """
        切换到组织架构上面
        :return:
        """
        try:
            terminal_framework_locator = 'by_xpath,//div[@class="tab-item active"]'
            self.click(terminal_framework_locator)
        except ElementNotInteractableException as e:
            raise e

    def switch_union_set(self):
        """
        设备分组，切换交/并集
        :return:
        """
        union_set_locator = 'by_xpath,class="el-switch__core"'

    def release_search_terminal(self, text):
        """
        设备列表进行搜索，可搜索id，可搜索设备名称
        :param text:
        :return:
        """
        try:
            search_locator = 'by_xpath,//input[@placeholder="请输入id或设备名称"]'
            self.input(search_locator, text)
        except ElementNotInteractableException as e:
            raise e

    def click_submit_button(self):
        """
        进行设备搜索后，点击确认按钮
        :return:
        """
        submit_button_locator = 'by_xpath,//div[@class="tools"]//span[text()="确定"]'
        self.click(submit_button_locator)

    def switch_to_choose_terminal(self):
        """
        切换到选择设备弹框上
        """
        switch_to_choose_terminal = 'by_xpath,//span[text()=" 选择设备"]'
        self.click(switch_to_choose_terminal)

    def switch_to_selection_strategy(self):
        """
        切换到选择策略上
        """
        switch_to_selection_strategy = 'by_xpath,//span[text()=" 选择策略"]'
        self.click(switch_to_selection_strategy)

    def enter_keyboard(self, driver):
        """
        键盘enter键，来进行确认
        :return:
        """
        search_locator = 'by_xpath,//input[@placeholder="请输入id或设备名称"]'
        search_button = self.click(search_locator)
        # ele = self.get_element(search_locator)
        # ActionChains(driver).move_to_element(ele).send_keys(Keys.ENTER).perform()
        ActionChains(self.driver).send_keys_to_element(search_button, Keys.ENTER).perform()

        # start_button = ('by_xpath,//input[@placeholder="开始日期"]')
        # end_button = ('by_xpath,//input[@placeholder="结束日期"]')
        #
        # start_locator = self.click('by_xpath,//input[@placeholder="开始日期"]')
        # end_locator = self.click('by_xpath,//input[@placeholder="结束日期"]')
        # self.input(start_button, start)
        # ActionChains(self.driver).send_keys_to_element(start_locator, Keys.ENTER).perform()
        # self.input(end_button, end)
        # ActionChains(self.driver).send_keys_to_element(end_locator, Keys.ENTER).perform()

    def clear_search(self, driver):
        """
        清空搜索条件
        :return:
        """
        search_locator = 'by_xpath,//input[@placeholder="请输入id或设备名称"]'
        # ele = self.get_element(search_locator)
        # ActionChains(driver).move_to_element(ele).perform()
        self.clear(search_locator)

    def select_all_terminals(self):
        """
        在设备列表中，点击全选按钮
        :return:
        """
        select_all_locator = 'by_xpath,//span[text()="全选"]'
        self.click(select_all_locator)

    def select_first_terminal(self):
        """
        发布管理，在设备列表中，选择第一个设备
        :return:
        """
        select_all_locator = 'by_xpath,//span[text()="全选"]'
        self.click(select_all_locator)


    def clear_all_terminal(self):
        """
        设备列表中，点击清空按钮
        :return:
        """

        disselect_all_locator = 'by_xpath,//span[text()="清空"]'
        self.click(disselect_all_locator)

    def switch_program_edit(self):
        """
        在发布管理-设备列表中，点击跳转到节目编排
        :return:
        """
        self.click('by_xpath,//span[text()=" 节目编排"]')

    def expand_all_org(self):
        """

        :return:
        """
        all_org_locator = 'by_xpath,//div[@class="custom-tree-node"]'
        all_org = self.get_elements(all_org_locator)
        first_org = all_org[0]
        first_org.click()

    def select_all_org(self):
        """

        :return:
        """

        select_all_org_locator = 'by_xpath,//input[@class="el-checkbox__original"]/..'

        select_all_org = self.get_elements(select_all_org_locator)

        # print("4544//////////",select_all_org)
        select_first_org = select_all_org[1]
        # print("hjbknkn",select_first_org)

        select_first_org.click()

    # =====================================节目编排=============================================
    def clear_display_start_date(self, driver, start):
        start_button = ('by_xpath,//input[@placeholder="开始时间"]')
        print("上vsdv0wwewe", self.get_attribute_info(start_button))

        ele = self.get_element(start_button)

        ActionChains(driver).move_to_element(ele).perform()

        # 删除符号，是否可见
        is_click = 'by_xpath,//div[@aria-expanded="true"]'

        if self.element_exist(is_click):
            self.input(start_button, start)

    def program_display_start_date(self, start):
        start_button = ('by_xpath,//input[@placeholder="开始时间"]')

        start_locator = self.click(start_button)
        self.clear(start_button)
        start_locator = self.click(start_button)
        self.input(start_button, start)
        ActionChains(self.driver).send_keys_to_element(start_locator, Keys.ENTER).perform()
        time.sleep(5)

    def program_display_end_date(self, end):
        end_button = ('by_xpath,//input[@placeholder="结束时间"]')
        end_locator = self.click(end_button)
        time.sleep(5)
        self.input(end_button, end)
        ActionChains(self.driver).send_keys_to_element(end_locator, Keys.ENTER).perform()

    def click_weekly(self):
        """
        节目编排中，在周期周几处，点击加号按钮
        :return:
        """
        self.click('by_xpath,//div[@class="period"]/../div[@class="add"]')

    def set_every_monday_display(self):
        """
        设置每周一播放
        :return:
        """
        self.click('by_xpath,//span[@class="weekday" and text()="周一"]')

    def set_every_tuesday_display(self):
        self.click('by_xpath,//span[@class="weekday" and text()="周二"]')

    def set_every_wednesday_display(self):
        self.click('by_xpath,//span[@class="weekday" and text()="周三"]')

    def set_every_thursday_display(self):
        self.click('by_xpath,//span[@class="weekday" and text()="周四"]')

    def set_every_friday_display(self):
        self.click('by_xpath,//span[@class="weekday" and text()="周五"]')

    def set_every_saturday_display(self):
        self.click('by_xpath,//span[@class="weekday" and text()="周六"]')

    def set_every_weekday_display(self):
        self.click('by_xpath,//span[@class="weekday" and text()="周日"]')

    def set_iterable_monday_display(self, weekly):
        self.click(f'by_xpath,//span[@class="weekday" and text()="{weekly}"]')

    def save_program_edit(self):
        self.click('by_xpath,//span[text()=" 保存 "]')

    def cancel_program_edit(self):
        self.click('by_xpath,//span[text()="取消"]')

    def add_time_line(self):
        """
        时间轴上面，点击加号按钮
        :return:
        """
        self.click('by_xpath,//div[@class="time-bar"]/div[@class="add"]')

    def click_timeline(self):
        """
        点击到时间轴上
        :return:
        """
        all_time_lines ='by_xpath,//div[@class="tp"]'
        all_time_lines_ele =self.get_elements(all_time_lines)



    # 生成一天内的随机时间
    def generate_random_time(self):
        """生成一天内的随机时间"""
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return datetime.time(hour, minute)

    def generate_random_times_with_diff(self):
        """
        生成开始和结束时间，确保结束时间比开始时间晚至少30分钟。

        返回值:
        - start_time (datetime.time): 随机生成的开始时间。
        - end_time (datetime.time): 随机生成的结束时间，至少比开始时间晚30分钟。
        """
        start_datetime = datetime.datetime.combine(datetime.date.today(), self.generate_random_time())
        end_datetime_delta = datetime.timedelta(minutes=random.randint(30, 1410))  # 30到1410分钟之间
        end_datetime = start_datetime + end_datetime_delta

        # 确保结束时间在当天之内
        end_datetime = min(end_datetime, datetime.datetime.combine(datetime.date.today(), datetime.time(23, 59, 59)))

        start_time = start_datetime.time()
        end_time = end_datetime.time()

        return start_time, end_time

    #     # 生成随机时间
    #
    # start_time, end_time = generate_random_times_with_diff()
    # print(f"开始时间: {start_time.strftime('%H:%M')}")
    # print(f"结束时间: {end_time.strftime('%H:%M')}")

    def time_line_start_time(self, start_time):
        """
        时间段的开始时间  用于随机输入
        :param stime:
        :return:
        """
        time_line_start_time_locator = 'by_xpath,//div[@class="el-dialog__body"]//input[@placeholder="开始时间"]'
        # self.input(time_line_start_time_locator, start_time)
        # ActionChains(driver).send_keys_to_element()
        start_ele = self.click(time_line_start_time_locator)
        ActionChains(self.driver).send_keys_to_element(start_ele, start_time).perform()

    def time_line_end_time(self, end_time):
        """
        时间段的结束时间 用于随机输入
        :param etime:
        :return:
        """
        time_line_end_time_locator = 'by_xpath,//div[@class="el-dialog__body"]//input[@placeholder="结束时间"]'
        # self.input(time_line_end_time_locator, end_time)
        end_ele = self.click(time_line_end_time_locator)
        ActionChains(self.driver).send_keys_to_element(end_ele, end_time).perform()

    def fixed_start_time_line(self):
        """
        固定的开始时间
        :param start_time: 
        :return: 
        """""
        time_line_end_time_locator = 'by_xpath,//div[@class="el-dialog__body"]//input[@placeholder="开始时间"]'
        self.click(time_line_end_time_locator)
        time.sleep(2)
        fixed_start_time_eles=self.get_elements('by_xpath,//span[text()="00:00"]')
        first_fixed_start_time_ele = fixed_start_time_eles[0]

        ActionChains(self.driver).move_to_element(first_fixed_start_time_ele).click(first_fixed_start_time_ele).perform()


    def fixed_end_time_line(self):
        """
        固定的结束时间
        :param end_time: 
        :return: 
        """""
        fixed_end_time = 'by_xpath,//span[text()="00:35"]'
        end_times = self.get_elements(fixed_end_time)
        end_time = end_times[1]
        time_line_end_time_locator = 'by_xpath,//div[@class="el-dialog__body"]//input[@placeholder="结束时间"]'
        self.click(time_line_end_time_locator)
        time.sleep(2)
        ActionChains(self.driver).click(end_time).perform()

    def sumbit_span(self):
        """
        选择时间段后，点击确认按钮
        :return:
        """
        self.click('by_xpath,//span[text()=" 确定 "]')

    def confirm_button(self):
        """
        在节目编排/选设备抽屉中，点击确定按钮
        """
        self.click('by_xpath,//span[text()="确定"]')

    def click_save_as_label(self):
        """
        点击保存为标签
        :return:
        """

        self.click('by_xpath,//span[text()="保存为标签"]')

    def set_label_name(self, name):
        """
        设置标签名称
        :param name: 标签名称
        :return:
        """
        set_name_locator = 'by_xpath,//input[@placeholder="名称最多不超过20个字"]'
        self.input(set_name_locator, name)

    def click_add_program(self):
        """
        新增节目按钮
        :return:
        """
        self.click('by_xpath,//div[text()="新增"]/../img')

    def general_program_type(self):
        """
        选择节目时，对节目的分类、方向进行筛选
        :return:
        """
        self.click('by_xpath,//div[text()="普通" and @class="opt"]')

    def simple_program_type(self):
        self.click('by_xpath,//div[text()="简单" and @class="opt"]')

    def across_direction(self):
        self.click('by_xpath,//div[text()="横屏" and @class="opt"]')

    def stick_direction(self):
        self.click('by_xpath,//div[text()="竖屏" and @class="opt"]')

    def click_screen_resolution(self):
        """
        选择节目，点击分辨率，进行过滤
        :return:
        """
        screen_resolution_locator = 'by_xpath,//span[text()=" 重置 "]/preceding::input[@role="combobox"]'
        self.click(screen_resolution_locator)
        # resolution_ele =self.get_element(screen_resolution_locator)
        # ActionChains(driver).send_keys_to_element(resolution_ele).click(resolution_ele).perform()

    def choose_resolution(self, resolution, driver):
        """
        输入分辨率，进行点击
        :param resolution: 输入分辨率
        :return:
        """

        fixed_resolution = ['1920x1080', '3840x2160', '1366x768', '1280x720',
                            '1080x1920', '2160x3840', '768x1366', '720x1280']

        if resolution in fixed_resolution:
            print("++++++++++++++++++++++++++")
            choose_resolution_locator = f'by_xpath,//span[text()="{resolution}"]'
            # choose_resolution_locator = 'by_xpath,//span[text()="1920x1080"]'
            # choose_resolution_ele = self.get_element(choose_resolution_locator)
            # print("choose_resolution_ele:",choose_resolution_ele)
            # # self.click(choose_resolution_locator)
            # ActionChains(driver).move_to_element(choose_resolution_ele).click(choose_resolution_ele).perform()
            self.click(choose_resolution_locator)
        else:
            raise TypeError

        # if resolution in fixed_resolution:
        #     print("++++++++++++++++++++++++++")
        #     # choose_resolution_locator = f'by_xpath,//span[text()="{resolution}"]'
        #     choose_resolution_locator = 'by_xpath,//span[text()="1920x1080"]'
        #     choose_resolution_ele = self.get_element(choose_resolution_locator)
        #     print("choose_resolution_ele:", choose_resolution_ele)
        #     # self.click(choose_resolution_locator)
        #     ActionChains(driver).
        # else:
        #     raise TypeError

    def search_program_name(self, driver, name):
        search_name_locator = 'by_xpath,//input[@placeholder="输入名称"]'
        search_name_ele = self.get_element(search_name_locator)
        self.input(search_name_locator, name)
        ActionChains(driver).send_keys_to_element(search_name_ele, Keys.ENTER).perform()

    def reset_button(self):
        reset_locator = 'by_xpath,//span[text()=" 重置 "]'
        self.click(reset_locator)

    def program_edit_preview_all(self, driver):
        """
        先移动打预览组件上
        :param driver:
        :return:
        """
        program_edit_preview_all_locator = 'by_xpath,//div[text()="预览"]'
        preview_all_ele = self.get_element(program_edit_preview_all_locator)
        ActionChains(driver).move_to_element(preview_all_ele).perform()

    def hover_to_program_edit(self):
        """
        在节目编排中，鼠标hover到节目遮罩上面
        :param driver:
        :return:
        """
        driver = self.driver
        preview_one_locator = 'by_xpath,//div[@class="hot"]'
        preview_one_eles = self.get_elements(preview_one_locator)
        if preview_one_eles:
            preview_one_ele = preview_one_eles[0]
            ActionChains(driver).move_to_element(preview_one_ele).perform()

    def click_to_preview(self):
        """
        鼠标hover到蒙蔽mask上，进行预览
        locator会拿到两个webelement，第一个是预览，第二个删除
        :return:
        """
        hover_to_preview_locator = 'by_xpath,//div[@class="hot"]/div/img'
        preview_ele = self.get_elements(hover_to_preview_locator)
        preview_ele = preview_ele[0]
        ActionChains(self.driver).move_to_element(preview_ele).click(preview_ele).perform()

    def click_to_delete(self):
        """
        鼠标hover到蒙蔽mask上，进行删除
        locator会拿到两个webelement，第一个是预览，第二个删除
        :return:
        """
        driver = self.driver
        hover_to_preview_locator = 'by_xpath,//div[@class="hot"]/div/img'
        preview_ele = self.get_elements(hover_to_preview_locator)
        if preview_ele:
            preview_ele = preview_ele[1]
            ActionChains(driver).move_to_element(preview_ele).click(preview_ele).perform()

    def collapse_edit_label(self):
        """
        节目编排中，进行标签折叠
        """
        collapse_locator = 'by_xpath,//div[@class="collapse"]'
        self.click(collapse_locator)

    def expand_edit_label(self):
        """
        节目编排中，进行标签展开
        """
        expand_locator = 'by_xpath,//div[@class="collapse reverse"]'
        self.click(expand_locator)

    def hover_to_first_edit_label(self):
        """
        先拿到所有的label，然后获取第一个
        如果没有label，则需要生成至少一个label
        """
        all_labels_locator = 'by_xpath,//div[@class="item-box"]/div'
        if self.element_exist(all_labels_locator):
            all_labels_ele = self.get_elements(all_labels_locator)
            print("all_labels_ele",all_labels_ele)
            first_label_ele = all_labels_ele[0]

            ActionChains(self.driver).move_to_element(first_label_ele).perform()
        else:
            print("当前没有标签111")

    def delete_first_label(self):
        """
        删除第一个标签
        """
        all_delete_locatorn = 'by_xpath,//div[@class="close"]/span[text()="x"]'
        if self.element_exist(all_delete_locatorn):
            all_delete_icon = self.get_elements(all_delete_locatorn)

            first_delete_icon = all_delete_icon[0]
            ActionChains(self.driver).move_to_element(first_delete_icon).click(first_delete_icon).perform()
        else:
            print("当前没有标签222")

    def hover_program_and_choice(self):
        """
        节目编排-选择节目-鼠标hover列表中第一个节目
        :return:
        """
        all_locators = 'by_xpath,//div[@class="imgBody radiusAll"]/img'
        all_locatro_eles = self.get_elements(all_locators)
        if all_locatro_eles:
            first_locator = all_locatro_eles[0]
            ActionChains(self.driver).move_to_element(first_locator).perform()
        else:
            print("当前列表无节目，无法进行选择")

    def choose_program_and_choice(self):
        """
        节目编排-选择节目-选择列表中第一个节目
        :return:
        """
        all_locators = 'by_xpath,//div[@class="mask radiusAll"]/img[2]'
        all_locatro_eles = self.get_elements(all_locators)
        if all_locatro_eles:
            first_locator = all_locatro_eles[0]
            ActionChains(self.driver).move_to_element(first_locator).click(first_locator).perform()
        else:
            print("当前列表无节目，无法进行选择")