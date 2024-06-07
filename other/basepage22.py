import allure, os
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Base111:
    def __init__(self, page):
        self.page = page

    def clear_cookies(self):
        """
        清除cookie
        """
        self.page.delete_all_cookies()

    def refresh_page(self):
        """
        刷写当前页面
        """
        self.page.refresh()

    def back_page(self):
        """
        返回
        """
        self.page.back()

    def open_url(self, url):
        """
        打开网页
        """
        self.page.get(url)

    def quite_page(self):
        """
        退出浏览器
        """
        self.page.quit()

    def close_current_page(self):
        """
        关闭当前页面
        """
        self.page.close()

    def get_element(self, selector):
        """
        获取元素，通过，区分开，类别 内容
        ('x,//*[@id="kw"])
        """
        if "," not in selector:
            return self.page.find_element(By.ID, value=selector)
        selector_by = selector.split(",")[0]
        selector_value = selector.split(",")[1]
        if selector_by == "i" or selector_by == "id":
            w_element = self.page.find_element(By.ID, value=selector_value)
        elif selector_by == "n" or selector_by == "name":
            w_element = self.page.find_element(By.NAME, value=selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            w_element = self.page.find_element(By.CLASS_NAME, value=selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            w_element = self.page.find_element(By.LINK_TEXT, value=selector_value)
        elif selector_by == "p" or selector_by == "partial_link":
            w_element = self.page.find_element(By.PARTIAL_LINK_TEXT, value=selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            w_element = self.page.find_element(By.TAG_NAME, value=selector_value)
        elif selector_by == "x" or selector_by == "by_xpath":
            w_element = self.page.find_element(By.XPATH, value=selector_value)
        elif selector_by == "s" or selector_by == "css_selector":
            w_element = self.page.find_element(By.CSS_SELECTOR, value=selector_value)
        else:
            return None
        time.sleep(0.5)
        return w_element

    def get_elements(self, selector):
        """
        获取元素列表，通过，区分开，类别 内容
        """
        if "," not in selector:
            return self.page.find_elements(By.ID, value=selector)
        selector_by = selector.split(",")[0]
        selector_value = selector.split(",")[1]
        if selector_by == "i" or selector_by == "id":
            elements = self.page.find_elements(By.ID, value=selector_value)
        elif selector_by == "n" or selector_by == "name":
            elements = self.page.find_elements(By.NAME, value=selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            elements = self.page.find_elements(By.CLASS_NAME, value=selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            elements = self.page.find_elements(By.LINK_TEXT, value=selector_value)
        elif selector_by == "p" or selector_by == "partial_link":
            elements = self.page.find_elements(By.PARTIAL_LINK_TEXT, value=selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            elements = self.page.find_elements(By.TAG_NAME, value=selector_value)
        elif selector_by == "x" or selector_by == "by_xpath":
            elements = self.page.find_elements(By.XPATH, value=selector_value)
        elif selector_by == "s" or selector_by == "css_selector":
            elements = self.page.find_elements(By.CSS_SELECTOR, value=selector_value)
        else:
            return None
        time.sleep(0.5)
        return elements

    def get_element_form_parent_by_e(self, par_e_or_pare_selector, son_selector):
        """
        par_e element
        son_selector 文本
        "," 不包含的就默认是传进来的是id
        """
        if isinstance(par_e_or_pare_selector, str):
            par_e = self.get_element(par_e_or_pare_selector)
        else:
            par_e = par_e_or_pare_selector
        if "," not in son_selector:
            return par_e.page.find_element(By.ID, value=son_selector)
        selector_by = son_selector.split(",")[0]
        selector_value = son_selector.split(",")[1]
        if selector_by == "i" or selector_by == "id":
            element = par_e.page.page.find_element(By.ID, value=son_selector)
        elif selector_by == "n" or selector_by == "name":
            element = par_e.page.find_element(By.NAME, value=selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            element = par_e.page.find_element(By.CLASS_NAME, value=selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            element = par_e.page.find_element(By.LINK_TEXT, value=selector_value)
        elif selector_by == "p" or selector_by == "partial_link":
            element = par_e.page.find_element(By.PARTIAL_LINK_TEXT, value=selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            element = par_e.page.find_element(By.TAG_NAME, value=selector_value)
        elif selector_by == "x" or selector_by == "by_xpath":
            element = par_e.page.find_element(By.XPATH, value=selector_value)
        elif selector_by == "s" or selector_by == "css_selector":
            element = par_e.page.find_element(By.CSS_SELECTOR, value=selector_value)
        else:
            return None
        time.sleep(0.5)
        return element

    def get_elements_form_parent_by_e(self, par_e_or_pare_selector, son_selector):
        """
        通过父类去查找子元素的列表
        """
        if isinstance(par_e_or_pare_selector, str):
            par_e = self.get_element(par_e_or_pare_selector)
        else:
            par_e = par_e_or_pare_selector
        if "," not in son_selector:
            return par_e.page.find_elements(By.ID, value=son_selector)
        selector_by = son_selector.split(",")[0]
        selector_value = son_selector.split(",")[1]
        if selector_by == "i" or selector_by == "id":
            element_s = par_e.page.page.find_elements(By.ID, value=son_selector)
        elif selector_by == "n" or selector_by == "name":
            element_s = par_e.page.find_elementS(By.NAME, value=selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            element_s = par_e.page.find_elementS(By.CLASS_NAME, value=selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            element_s = par_e.page.find_elementS(By.LINK_TEXT, value=selector_value)
        elif selector_by == "p" or selector_by == "partial_link":
            element_s = par_e.page.find_elementS(By.PARTIAL_LINK_TEXT, value=selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            element_s = par_e.page.find_elementS(By.TAG_NAME, value=selector_value)
        elif selector_by == "x" or selector_by == "by_xpath":
            element_s = par_e.page.find_elementS(By.XPATH, value=selector_value)
        elif selector_by == "s" or selector_by == "css_selector":
            element_s = par_e.page.find_elementS(By.CSS_SELECTOR, value=selector_value)
        else:
            return None
        time.sleep(0.5)
        return element_s

    def element_exist(self, selector):
        """
        判断元素是否存在
        """
        try:
            self.get_element(selector)
            return True
        except Exception as e:
            return False

    def input_text(self, selector, text_info):
        """
        在编辑框元素输入文本，清除原有内容之后，在输入
        """
        e1 = self.get_element(selector)
        e1.clear()
        e1.send_keys(text_info)

    def input_text_no_clear(self, selector, text_info):
        """
        在编辑框元素输入文本，不清除原有内容
        """
        e1 = self.get_element(selector)
        e1.send_keys(text_info)

    def select_by_index(self, selector, index_num):
        """
        下拉框，通过index 来选择
        """
        e1 = self.get_element(selector)
        Select(e1).select_by_index(index_num)

    def select_by_value(self, selector, value_info):
        """
             下拉框，通过value 来选择
        """
        e1 = self.get_element(selector)
        Select(e1).select_by_value(value_info)

    def get_select_value(self, selector):
        """
         # 获取下拉列表的选项内容所有的
        """
        value_list = []
        e1 = self.get_element(selector)
        op_list = e1.find_elements_by_tag_name("option")
        for option in op_list:
            value_s = option.get_attribute("text")
            value_list.append(value_s)
        return value_list

    def scroll_to_view(self, selector):
        """
        滚动到元素
        """
        e1 = self.get_element(selector)
        self.page.execute_script('arguments[0].scrollIntoView(false);', e1)

    def get_attribute_info(self, selector, attribute_kind):
        """
        获取元素的信息，
        """
        e1 = self.get_element(selector)
        r_a = e1.get_attribute(attribute_kind)
        return r_a

    @staticmethod
    def get_element_attribute_info(element, attribute_kind):
        """
        获取元素的信息，
        """
        r_a = element.get_attribute(attribute_kind)
        return r_a

    def get_title(self):
        """
        获取当前页面的title
        """
        return self.page.title

    def get_current_url(self):
        """
        获取当前页面的url
        """
        self.page.current_url

    def switch_to_frame(self, selector):
        """
        嵌套的frame ，切换到指定iframe
        """
        e1 = self.get_element(selector)
        self.page.switch_to.frame(e1)

    def switch_to_frame_by_handle(self, handle):
        """
        嵌套的frame ，通过handle
        """
        self.page.switch_to.frame(handle)

    def switch_to_default_frame(self):
        """
        切换到默认的 frame
        """
        self.page.switch_to.default_content()

    def switch_to_window(self, handle):
        """
        切换窗口，通过 handle
        """
        self.page.switch_to.window(handle)

    def get_all_handles(self):
        """
        获取所有串口的handles
        """
        all_handles = self.page.window_handles
        return all_handles

    def get_current_handle(self):
        """
        获取当前页面的handle
        """
        return self.page.current_window_handle

    def switch_to_new_close_other(self, target_handle):
        """
        关闭当前页面的其他页面
        """
        all_handles = self.page.window_handles
        if target_handle in all_handles:
            for one_h in all_handles:
                if one_h != target_handle:
                    self.switch_to_window(one_h)
                    self.close_brower()
                    self.switch_to_window(target_handle)

    def wait_element_appear(self, selector, wait_time=10):
        """
        等待元素出现
        """
        time.sleep(1)
        flag = True
        while self.element_exist(selector):
            time.sleep(1)
            wait_time -= 1
            if wait_time == 0:
                flag = False
                break
        return flag

    def click_on_text(self, text_info):
        """
        点击文本，唯一性
        """
        e1 = self.get_element('x,//*[text="' + text_info + '"]')
        e1.click()

    def click_on_element(self, selector):
        """
        点击元素
        """
        e1 = self.get_element(selector)
        e1.click()

    def right_click(self, selector):
        """
        鼠标右键点击
        """
        e1 = self.get_element(selector)
        ActionChains(self.page).context_click(e1).perform()

    def left_click(self, selector):
        """
        鼠标左键点击
        """
        e1 = self.get_element(selector)
        ActionChains(self.page).click(e1).perform()

    def move_mouse_to_element(self, selector):
        """
        鼠标移动元素上
        """
        e1 = self.get_element(selector)
        ActionChains(self.page).move_to_element(e1).perform()

    def move_mouse_to_element(self, element):
        ActionChains(self.page).move_to_element(element).perform()

    def get_page_source(self):
        """
        获取当前页面的source
        """
        html_txt = self.page.page_source
        return html_txt

    def get_default_select_value(self, selector):
        e1 = Select(self.get_element(selector)).first_selected_option
        select_text = e1.get_attribute('text')
        return select_text

    def get_select_values(self, selector):
        """
        获取下拉框的全部值
        """
        name_list = []
        e1_all = Select(self.get_element(selector)).options
        for e1 in e1_all:
            select_txt = e1.get_attribute("text")
            name_list.append(select_txt)
        return name_list

    def take_screen_shot(self, file_name):
        """
        page 页面截图操作
        """
        self.page.save_screenshot(file_name)

    def visible(self, locator, wait_time=15, idx=1):

        el = self.page.locator(locator)

        try:
            el.wait_for(timeout=wait_time * 1000)
            # not found
        except TimeoutError as e:
            print(f'\nNot found: {e}')
            return None, False

        # multiple el found
        except Error as ee:
            # assert el.count() > 1, 'Expect multi elements'
            if el.count() > 1:
                print(f"\n{'=' * 18} Multiple elements found{'=' * 18}\n{ee}")
                curr = el.nth(idx - 1)
                v = curr.is_visible()
                return curr, v
            else:
                return None, False

        if el.is_visible():
            return el, True
        else:
            return el, False

    def contains(self, text: str, el_type='text'):
        _postfix = {
            'text': '',
            'input': 'input',
            'textarea': 'textarea',
            'dropdown': 'dropdown',
            'div': 'div',
            'table_cell': 'table_cell',
        }
        _pf = _postfix.get(el_type, '')
        my_path = f'//*[contains(text(), "{text}")]'
        if _pf:
            my_path = my_path + f'/following-sibling::*//{_pf}'

        v = self.visible(my_path)
        if not v[1]:
            # self._attach(my_path)
            print(f'ElementNotFound: {text}')
            raise AssertionError('ElementNotFound')

        return v

    def element_is_exist(self, locator, is_exist=True, wait_time=30):
        """
        断言页面是否存在元素
        :param wait_time:
        :param locator: 定位
        :param is_exist: 断言 True or False
        :return:
        """
        element, is_v = self.visible(locator, wait_time=wait_time)
        assert is_v == is_exist, AssertionError('AssertionError')

    def attach(self, png):
        """
        截图功能
        :param png: 截图文件名称
        :return:
        """
        base_path = RuntimeVars.tmp_files
        p = f'{png}-{mocks.ones_uuid()}'
        s_path = os.path.join(base_path, f'{p}.png')
        allure.attach(self.page.screenshot(path=s_path, full_page=True), p, attachment_type.PNG)


class LoggerHandler:
    # 初始化 Logger
    def __init__(self,
                 name='root',
                 logger_level='DEBUG',
                 file=None,
                 logger_format='%(asctime)s-%(message)s'
                 # logger_format = '%(asctime)s-%(filename)s-%(lineno)d-%(message)s'
                 ):
        # 1、初始化logger收集器
        logger = logging.getLogger(name)

        # 2、设置日志收集器level级别
        logger.setLevel(logger_level)

        # 5、初始化 handler 格式
        fmt = logging.Formatter(logger_format)

        # 3、初始化日志处理器

        # 如果传递了文件，就会输出到file文件中
        if file:
            file_handler = logging.FileHandler(file)
            # 4、设置 file_handler 级别
            file_handler.setLevel(logger_level)
            # 6、设置handler格式
            file_handler.setFormatter(fmt)
            # 7、添加handler
            logger.addHandler(file_handler)

        # 默认都输出到控制台
        stream_handler = logging.StreamHandler()
        # 4、设置 stream_handler 级别
        stream_handler.setLevel(logger_level)
        # 6、设置handler格式
        stream_handler.setFormatter(fmt)
        # 7、添加handler
        logger.addHandler(stream_handler)

        # 设置成实例属性
        self.logger = logger

    # 返回日志信息

    def debug(self, msg):
        return self.logger.debug(msg)

    def info(self, msg):
        return self.logger.info(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)

    def critical(self, msg):
        return self.logger.critical(msg)
