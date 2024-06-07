from selenium.webdriver import ActionChains

from basepage.base_page import BasePage


class PlayBillPage(BasePage):
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
    #
    # def switch_to_release_management(self):
    #     """
    #     侧边栏切换到发布管理
    #     :return:
    #     """
    #     release_management_locator = 'by_xpath,//div[text()=" 发布管理"]'
    #     clickable_ele = self.get_element('by_xpath,//div[text()=" 发布管理"]/../..')
    #     get_classmethod = clickable_ele.get_attribute("class")
    #     if get_classmethod == "el-tree-node is-current is-focusable":
    #         pass
    #     else:
    #         self.click(release_management_locator)

    def switch_to_play_bill(self):
        """
        在发布管理tab上，切到节目单上
        """
        play_bill_locator = 'by_xpath,//div[@class="title" and text()="节目单"]'

        self.click(play_bill_locator)

    def preview_play_bill(self):
        """
        节目单查看
        """
        all_preview_icons = 'by_xpath,//img[@title="查看"]'
        all_preview_icon_buttons = self.get_elements(all_preview_icons)
        first_preview_icon =all_preview_icon_buttons[0]
        if first_preview_icon:
            ActionChains(self.driver).move_to_element(first_preview_icon).click(first_preview_icon).perform()

    def copy_play_bill(self):
        """
        引用节目单按钮
        """
        all_copy_locators = 'by_xpath,//img[@title="引用"]'
        all_copy_eles = self.get_elements(all_copy_locators)
        first_copy_ele = all_copy_eles[0]
        if first_copy_ele:
            ActionChains(self.driver).move_to_element(first_copy_ele).click(first_copy_ele).perform()

    def edit_play_bill(self):
        """
        编辑暂存节目单
        """
        all_edit_locators = 'by_xpath,//img[@title="编辑"]'
        all_edit_eles = self.get_elements(all_edit_locators)
        first_edit_ele = all_edit_eles[0]
        if all_edit_eles:
            ActionChains(self.driver).move_to_element(first_edit_ele).click(first_edit_ele).perform()

    def expiry_play_bill(self):
        """
        节目单失效
        """
        all_expiry_locator ='by_xpath,//img[@title="失效"]'
        all_expiry_buttons = self.get_elements(all_expiry_locator)
        print("all_expiry_buttons:",all_expiry_buttons)
        first_expiry_ele = all_expiry_buttons[0]
        print("first_expiry_ele:",first_expiry_ele)
        if first_expiry_ele:
            ActionChains(self.driver).move_to_element(first_expiry_ele).click(first_expiry_ele).perform()

    def confirm_expiry_button(self):
        """
        失效节目单弹框上面，点击确认按钮
        """
        self.click('by_xpath,//span[text()=" 确定 "]')

    def confirm_copy_button(self):
        """
        引用节目单时，点击确定按钮
        """
        confirm_copy_locator = 'by_xpath,//span[text()="确定"]'
        self.click(confirm_copy_locator)

    def close_copy_alert(self):
        """
        关闭引用节目单弹框
        """
        self.click('by_xpath,//button[@aria-label="el.messagebox.close"]')

    def confirm_close_button(self):
        """
        确定关闭节目单
        :return:
        """
        self.click('by_xpath,//span[text()=" 确定 "]')

    def cancel_expiry_button(self):
        """
        失效节目单弹框上面，点击取消按钮
        """
        self.click('by_xpath,//span[text()="取消"]')

    def delete_play_bill(self):
        """
        删除节目单
        """
        all_delete_locators = 'by_xpath,//img[@title="删除"]'
        all_delete_buttons = self.get_elements(all_delete_locators)
        first_delete_ele = all_delete_buttons[0]
        if first_delete_ele:
            ActionChains(self.driver).move_to_element(first_delete_ele).click(first_delete_ele).perform()

    def click_filter_status(self):
        """
        点击使用状态按钮
        """
        filter_status_locator = 'by_xpath,//span[text()="使用状态"]'
        self.click(filter_status_locator)

    def filter_temporary_storage_status(self):
        """
        过滤暂存状态
        """
        temporary_storage_locator = 'by_xpath,//li[text()="暂存"]'
        self.click(temporary_storage_locator)

    def filter_in_process_approve_status(self):
        """
        过滤审批中状态
        """
        in_process_approve_locator = 'by_xpath,//li[text()="审批中"]'
        self.click(in_process_approve_locator)

    def filter_return_modify_status(self):
        """
        过滤退回修改状态
        """
        return_modify_locator = 'by_xpath,//li[text()="退回修改"]'
        self.click(return_modify_locator)

    def filter_fail_to_approve_status(self):
        """
        过滤审批不通过状态
        """
        fail_to_approve_locator = 'by_xpath,//li[text()="审批不通过"]'
        self.click(fail_to_approve_locator)

    def filter_released_status(self):
        """
        过滤已发布状态
        """
        released_locator = 'by_xpath,//li[text()="已发布"]'
        self.click(released_locator)

    def filter_disabled_status(self):
        """
        过滤已失效状态
        """
        disabled_locator = 'by_xpath,//li[text()="已失效"]'
        self.click(disabled_locator)



