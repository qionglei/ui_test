import allure
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#------
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from datetime import datetime
# import os
# from conftest import driver
#---------
# from config.log_config import logger


class BasePage(object):
    timeout = 10

    # def __init__(self):
    def __init__(self, driver):
        self.driver = driver
        self.t = 0.5
        # self.timeout = 0.5
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # driver = webdriver.Chrome(options=options)

    # 浏览器操作的二次封装
    def clear_cookies(self):
        """
        清除cookie
        """
        self.driver.delete_all_cookies()

    def refresh(self):
        """
        刷写当前页面
        """
        self.driver.refresh()

    def back_page(self):
        """
        返回
        """
        self.driver.back()

    def maxsize_window(self):
        """
        窗口最大化
        """
        current_window_size = self.get_window_size()
        fixed_window = (1050, 1000)
        if current_window_size < fixed_window:
            self.driver.maximize_window()
        else:
            self.set_window_size(1050,1000)

    def minimize_window(self):
        """
        窗口最小化
        """
        self.driver.minimize_window()

    def get_window_size(self):
        """
        获取窗口的大小
        """
        width = self.driver.get_window_size().get('width')
        height = self.driver.get_window_size().get('height')
        tuple_size = (width, height)

        return tuple_size

    def set_window_size(self, *size):
        """
        :param size: (1024, 768)
                    宽高是一个元组
        :return:
        """
        self.driver.set_window_size(*size)

    def go_to(self, url):
        """
        打开网页
        """
        self.driver.get(url)

    def quite_driver(self):
        """
        退出浏览器
        """
        self.driver.quit()

    def close_current_page(self):
        """
        关闭当前页面
        """
        self.driver.close()

    # def get_element(self, args):
    #     timeout = 20
    #     """
    #     获取元素，通过，区分开，类别 内容
    #     ('x,//*[@id="kw"])
    #     """
    #     if "," not in args:
    #         return self.driver.find_element(By.ID, value=args)
    #     args_by = args.split(",")[0]
    #
    #     # print("使用的定位方式是：", args_by)
    #     args_value = args.split(",")[1]
    #     # print("定位的元素是：", args_value)
    #     if args_by == "i" or args_by == "id":
    #         w_element = self.driver.find_element(By.ID, value=args_value)
    #     elif args_by == "n" or args_by == "name":
    #         w_element = self.driver.find_element(By.NAME, value=args_value)
    #     elif args_by == "c" or args_by == "class_name":
    #         w_element = self.driver.find_element(By.CLASS_NAME, value=args_value)
    #     elif args_by == "l" or args_by == "link_text":
    #         w_element = self.driver.find_element(By.LINK_TEXT, value=args_value)
    #     elif args_by == "p" or args_by == "partial_link":
    #         w_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, value=args_value)
    #     elif args_by == "t" or args_by == "tag_name":
    #         w_element = self.driver.find_element(By.TAG_NAME, value=args_value)
    #     elif args_by == "x" or args_by == "by_xpath":
    #         w_element = self.driver.find_element(By.XPATH, value=args_value)
    #         # w_element = WebDriverWait(self.driver, timeout,
    #         #                     self.t).until(EC.visibility_of_element_located(By.XPATH,args_value))  # 显示等待定位
    #         # print("定位元素{}成功".format(args_value))
    #         # # return ele
    #     elif args_by == "s" or args_by == "css_args":
    #         w_element = self.driver.find_element(By.CSS_SELECTOR, value=args_value)
    #     else:
    #         return None
    #     time.sleep(0.5)
    #     return w_element

    # def get_element(self, args):
    #     locator_type = By.XPATH
    #     timeout = 10
    #     """
    #     获取元素，通过，区分开，类别 内容
    #     ('x,//*[@id="kw"])
    #     """
    #     if "," not in args:
    #         return self.driver.find_element(By.XPATH, value=args)
    #     args_by = args.split(",")[0]
    #
    #     # print("使用的定位方式是：", args_by)
    #     args_value = args.split(",")[1]
    #     # print("定位的元素是：", args_value)
    #
    #     """
    #         简化的查找元素方法，使用LocatorType枚举和可选的超时时间
    #     """
    #     if timeout is None:
    #         timeout = timeout  # 如果未指定超时，则使用默认的超时时间
    #         print("元素超时时间，10s")
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         element = wait.until(
    #             EC.presence_of_element_located((locator_type, args_value)))
    #         return element
    #     except TimeoutException:
    #         print(f"元素查找超时: {locator_type}={args_value}")
    #         return None

    def get_element(self, selector):
        """
        这个地方为什么是根据=来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=su"
        login_lnk = "xpath = //*[@id='u1']/a[7]"  # 百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        # if "," not in args:
        #     return self.driver.find_element(By.XPATH, value=args)
        #     args_by = args.split(",")[0]
        #
        #     # print("使用的定位方式是：", args_by)
        #     args_value = args.split(",")[1]
        #
        element = ''
        if ',' not in selector:
            # 如果不是：分隔直接认为是id
            # return self.driver.find_element_by_id(selector)
            return self.driver.find_element(By.ID, value=selector)

        # selector_by = selector.split('=>')[0]  # 元素名称
        # selector_value = selector.split('=>')[1]  # 元素ID名称

        selector_by = selector.split(',')[0]  # 元素名称
        selector_value = selector.split(',')[1]  # 元素ID名称

        # print("selector_by:********",selector_by)
        # print("selector_value:*********",selector_value)

        if selector_by == "i" or selector_by == "id":
            try:
                # element = self.driver.find_element_by_id(selector_value)  # id 定位
                element = self.driver.find_element(By.ID, value=selector_value)
                # logger.info("Had find the element:  %s  successful"

                #             "by: %s via value:%s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                # logger.error("NoSuchElementException:%s" % e)
                # self.get_windows_img()
                raise e
        elif selector_by == "n" or selector_by == "name":
            # element = self.driver.find_element_by_name(selector_value)  # name 名称定位
            element =self.driver.find_element(By.NAME, value=selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            # element = self.driver.find_element_by_class_name(selector_value)  # css 样式名称定位
            element = self.driver.find_element(By.CLASS_NAME, value=selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            try:
                # element = self.driver.find_element_by_link_text(selector_value)  # 文本超链接定位
                element = self.driver.find_element(By.LINK_TEXT, value=selector_value)
                # logger.info(("Had find the element  %s  successful""by %s via value:%s" % (element.text, selector_by, selector_value)))
            except NoSuchElementException as e:
                # logger.error("NoSuchElementException:%s" % e)
                # self.get_windows_img()
                raise
        elif selector_by == "p" or selector_by == "partial_link_text":
            # element = self.driver.find_element_by_partial_link_text(selector_value)
            element =  self.driver.find_element(By.PARTIAL_LINK_TEXT, value=selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            # element = self.driver.find_element_by_tag_name(selector_value)
            element = self.driver.find_element(By.TAG_NAME, value=selector_value)
        elif selector_by == "x" or selector_by == "by_xpath":
            try:
                # element = self.driver.find_element_by_xpath(selector_value)
                element = self.driver.find_element(By.XPATH, value=selector_value)
                # logger.info("Had find the element:  %s  successful by %s via value:%s" % (element.text, selector_by, selector_value))/
            except NoSuchElementException as e:
                # logger.error("NoSuchElementException:%s" % e)
                # self.get_windows_img()
                raise
        elif selector_by == "s" or selector_by == "selector_selector":
            # element = self.driver.find_element_by_css_selector(selector_value)
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, value=selector_value)
        else:
            # logger.error("Please enter a valid type of targeting elements.")
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def get_elements(self, args):
        """
            获取元素列表，通过，区分开，类别 内容
            """
        if "," not in args:
            return self.driver.find_elements(By.ID, value=args)
        args_by = args.split(",")[0]
        args_value = args.split(",")[1]

        # if "," not in args:
        #     return self.driver.find_elements(By.ID, value=args)
        # parts = args.split(",")
        # if len(parts) < 2:
        #     # 处理错误情况，比如返回 None 或抛出异常
        #     print("参数格式不正确，应该包含至少一个逗号分隔的值")
        #     return None
        # args_by = parts[0].strip()  # 去除可能的空格
        # args_value = parts[1].strip()  # 同样去除可能的空格
        # print("args_by:",args_by)
        # print("args_value:",args_value)

        if args_by == "i" or args_by == "id":
            elements = self.driver.find_elements(By.ID, value=args_value)
        elif args_by == "n" or args_by == "name":
            elements = self.driver.find_elements(By.NAME, value=args_value)
        elif args_by == "c" or args_by == "class_name":
            elements = self.driver.find_elements(By.CLASS_NAME, value=args_value)
        elif args_by == "l" or args_by == "link_text":
            elements = self.driver.find_elements(By.LINK_TEXT, value=args_value)
        elif args_by == "p" or args_by == "partial_link":
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, value=args_value)
        elif args_by == "t" or args_by == "tag_name":
            elements = self.driver.find_elements(By.TAG_NAME, value=args_value)
        elif args_by == "x" or args_by == "by_xpath":
            elements = self.driver.find_elements(By.XPATH, value=args_value)
            # print("current elements是:",elements)
        elif args_by == "s" or args_by == "css_args":
            elements = self.driver.find_elements(By.CSS_SELECTOR, value=args_value)
        else:
            return None
        time.sleep(0.5)
        return elements


    def get_element_form_parent_by_e(self, par_e_or_pare_args, son_args):
        """
        par_e element
        son_args 文本
        "," 不包含的就默认是传进来的是id
        """
        if isinstance(par_e_or_pare_args, str):
            par_e = self.get_element(par_e_or_pare_args)
        else:
            par_e = par_e_or_pare_args
        if "," not in son_args:
            return par_e.driver.find_element(By.ID, value=son_args)
        args_by = son_args.split(",")[0]
        args_value = son_args.split(",")[1]
        if args_by == "i" or args_by == "id":
            element = par_e.driver.driver.find_element(By.ID, value=son_args)
        elif args_by == "n" or args_by == "name":
            element = par_e.driver.find_element(By.NAME, value=args_value)
        elif args_by == "c" or args_by == "class_name":
            element = par_e.driver.find_element(By.CLASS_NAME, value=args_value)
        elif args_by == "l" or args_by == "link_text":
            element = par_e.driver.find_element(By.LINK_TEXT, value=args_value)
        elif args_by == "p" or args_by == "partial_link":
            element = par_e.driver.find_element(By.PARTIAL_LINK_TEXT, value=args_value)
        elif args_by == "t" or args_by == "tag_name":
            element = par_e.driver.find_element(By.TAG_NAME, value=args_value)
        elif args_by == "x" or args_by == "by_xpath":
            element = par_e.driver.find_element(By.XPATH, value=args_value)
        elif args_by == "s" or args_by == "css_args":
            element = par_e.driver.find_element(By.CSS_SELECTOR, value=args_value)
        else:
            return None
        time.sleep(0.5)
        return element

    def get_elements_form_parent_by_e(self, par_e_or_pare_args, son_args):
        """
        通过父类去查找子元素的列表
        """
        if isinstance(par_e_or_pare_args, str):
            par_e = self.get_element(par_e_or_pare_args)
        else:
            par_e = par_e_or_pare_args
        if "," not in son_args:
            return par_e.driver.find_elements(By.ID, value=son_args)
        args_by = son_args.split(",")[0]
        args_value = son_args.split(",")[1]
        if args_by == "i" or args_by == "id":
            element_s = par_e.driver.driver.find_elements(By.ID, value=son_args)
        elif args_by == "n" or args_by == "name":
            element_s = par_e.driver.find_elementS(By.NAME, value=args_value)
        elif args_by == "c" or args_by == "class_name":
            element_s = par_e.driver.find_elementS(By.CLASS_NAME, value=args_value)
        elif args_by == "l" or args_by == "link_text":
            element_s = par_e.driver.find_elementS(By.LINK_TEXT, value=args_value)
        elif args_by == "p" or args_by == "partial_link":
            element_s = par_e.driver.find_elementS(By.PARTIAL_LINK_TEXT, value=args_value)
        elif args_by == "t" or args_by == "tag_name":
            element_s = par_e.driver.find_elementS(By.TAG_NAME, value=args_value)
        elif args_by == "x" or args_by == "by_xpath":
            element_s = par_e.driver.find_elementS(By.XPATH, value=args_value)
        elif args_by == "s" or args_by == "css_args":
            element_s = par_e.driver.find_elementS(By.CSS_SELECTOR, value=args_value)
        else:
            return None
        time.sleep(0.5)
        return element_s

    # 点击元素
    def click(self, args):
        # return self.driver.find_element(*args).click()
        # return self.get_element(*args).click()

        # e1 = self.get_element(args)
        # e1.click()

        if "," not in args:
            return self.driver.find_element(By.XPATH, value=args)
        args_by = args.split(",")[0]

        # print("使用的定位方式是：", args_by)
        args_value = args.split(",")[1]

        try:
            element_to_click = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, args_value))
            )
            element_to_click.click()
        except TimeoutException:
            print(f"等待点击元素超时: {args}")

    # 清空值
    def clear(self, args):
        self.get_element(args).clear()

    # 输入值
    def input(self, args, text):
        e1 = self.get_element(args)
        if e1 is not None:  # 检查 e1 是否为 None
            e1.clear()
            e1.send_keys(text)  # 假设你接下来要输入文本
        else:
            print(f"无法找到元素: {args}")


    # 点击按钮
    def click_button(self, args):
        # self.locater_ele(args).click()
        self.get_element(args).click()

    # 鼠标悬停
    def hover(self, args):
        # hover_ele = self.driver.find_element(*args)
        hover_ele = self.get_element(args)
        action = ActionChains(self.driver)
        action.move_to_element(hover_ele).perform()

    def element_exist(self, args):
        """
        判断元素是否存在
        """
        try:
            self.get_element(args)
            return True
        except Exception as e:
            return False

    # ---------以上是调试过的------------------------
    def input_text(self, args, text_info):
        """
        在编辑框元素输入文本，清除原有内容之后，在输入
        """
        e1 = self.get_element(args)
        e1.clear()
        e1.send_keys(text_info)

    def input_text_no_clear(self, args, text_info):
        """
        在编辑框元素输入文本，不清除原有内容
        """
        e1 = self.get_element(args)
        e1.send_keys(text_info)

    def select_by_index(self, args, index_num):
        """
        下拉框，通过index 来选择
        """
        e1 = self.get_element(args)
        Select(e1).select_by_index(index_num)

    def select_by_value(self, args, value_info):
        """
             下拉框，通过value 来选择
        """
        e1 = self.get_element(args)
        Select(e1).select_by_value(value_info)

    def get_select_value(self, args):
        """
         # 获取下拉列表的选项内容所有的
        """
        value_list = []
        e1 = self.get_element(args)
        op_list = e1.find_elements_by_tag_name("option")
        for option in op_list:
            value_s = option.get_attribute("text")
            value_list.append(value_s)
        return value_list

    def scroll_to_view(self, args):
        """
        滚动到元素
        """
        e1 = self.get_element(args)
        self.driver.execute_script('arguments[0].scrollIntoView(false);', e1)

    def get_attribute_info(self, args, attribute_kind):
        """
        获取元素的信息，
        """
        e1 = self.get_element(args)
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
        return self.driver.title

    def get_current_url(self):
        """
        获取当前页面的url
        """
        self.driver.current_url

    def switch_to_frame(self, args):
        """
        嵌套的frame ，切换到指定iframe
        """
        e1 = self.get_element(args)
        self.driver.switch_to.frame(e1)

    def switch_to_frame_by_handle(self, handle):
        """
        嵌套的frame ，通过handle
        """
        self.driver.switch_to.frame(handle)

    def switch_to_default_frame(self):
        """
        切换到默认的 frame
        """
        self.driver.switch_to.default_content()

    def switch_to_window(self, handle):
        """
        切换窗口，通过 handle
        """
        self.driver.switch_to.window(handle)

    def get_all_handles(self):
        """
        获取所有串口的handles
        """
        all_handles = self.driver.window_handles
        return all_handles

    def get_current_handle(self):
        """
        获取当前页面的handle
        """
        return self.driver.current_window_handle

    def switch_to_new_close_other(self, target_handle):
        """
        关闭当前页面的其他页面
        """
        all_handles = self.driver.window_handles
        if target_handle in all_handles:
            for one_h in all_handles:
                if one_h != target_handle:
                    self.switch_to_window(one_h)
                    self.close_brower()
                    self.switch_to_window(target_handle)

    def wait_element_appear(self, args, wait_time=10):
        """
        等待元素出现
        """
        time.sleep(1)
        flag = True
        while self.element_exist(args):
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

    def click_on_element(self, args):
        """
        点击元素
        """
        e1 = self.get_element(args)
        e1.click()

    def right_click(self, args):
        """
        鼠标右键点击
        """
        e1 = self.get_element(args)
        ActionChains(self.driver).context_click(e1).perform()

    def left_click(self, args):
        """
        鼠标左键点击
        """
        e1 = self.get_element(args)
        ActionChains(self.driver).click(e1).perform()

    def move_to_element(self, args):
        """
        鼠标移动元素上
        """
        e1 = self.get_element(args)
        ActionChains(self.driver).move_to_element(e1).perform()

    def move_mouse_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def get_page_source(self):
        """
        获取当前页面的source
        """
        html_txt = self.driver.page_source
        return html_txt

    def get_default_select_value(self, args):
        e1 = Select(self.get_element(args)).first_selected_option
        select_text = e1.get_attribute('text')
        return select_text

    def get_select_values(self, args):
        """
        获取下拉框的全部值
        """
        name_list = []
        e1_all = Select(self.get_element(args)).options
        for e1 in e1_all:
            select_txt = e1.get_attribute("text")
            name_list.append(select_txt)
        return name_list

    def take_screen_shot(self, file_name):
        """
        page 页面截图操作
        """
        self.driver.save_screenshot(file_name)

    def switch_alert(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        print(f"定位到的alert弹框是{alert}")

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

    # def get_screenshot(driver, filename):
    #     """
    #     获取当前页面的截图并保存。
    #     :param driver: WebDriver 实例
    #     :param filename: 保存截图的文件名
    #     :return: None
    #     """
    #     try:
    #         screenshot_path = f"D:\\ui\\temp\\{filename}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    #         driver.get_screenshot_as_file(screenshot_path)
    #         print(f"截图已保存至: {screenshot_path}")
    #     except WebDriverException as e:
    #         print(f"截图失败: {e}")

    # def visible(self, locator, wait_time=15, idx=1):
    #     el = self.get_element(locator)
    # try:
    #     el.wait_for(timeout=wait_time * 1000)
    #     # not found
    # except TimeoutError as e:
    #     print(f'\nNot found: {e}')
    #     return None, False

    # multiple el found
    # except Error as ee:
    #     # assert el.count() > 1, 'Expect multi elements'
    #     if el.count() > 1:
    #         print(f"\n{'=' * 18} Multiple elements found{'=' * 18}\n{ee}")
    #         curr = el.nth(idx - 1)
    #         v = curr.is_visible()
    #         return curr, v
    #     else:
    #         return None, False
    #
    # if el.is_visible():
    #     return el, True
    # else:
    #     return el, False    #
    #     # def contains(self, text: str, el_type='text'):
    #     #     _postfix = {
    #     #         'text': '',
    #     #         'input': 'input',
    #     #         'textarea': 'textarea',
    #     #         'dropdown': 'dropdown',
    #     #         'div': 'div',
    #     #         'table_cell': 'table_cell',
    #     #     }
    #     #     _pf = _postfix.get(el_type, '')
    #     #     my_path = f'//*[contains(text(), "{text}")]'
    #     #     if _pf:
    #     #         my_path = my_path + f'/following-sibling::*//{_pf}'
    #     #
    #     #     v = self.visible(my_path)
    #     #     if not v[1]:
    #     #         # self._attach(my_path)
    #     #         print(f'ElementNotFound: {text}')
    #     #         raise AssertionError('ElementNotFound')
    #     #
    #     #     return v

    # def findElements(self, locator):       ----------ones
    #     '''定位多个元素'''
    #
    # try:
    #     if isinstance(locator, list):
    #         locator = tuple(locator)
    # if not isinstance(locator, tuple):
    #     print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
    # print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0],
    #                                          locator[1]))
    # eles = WebDriverWait(self.driver, self.timeout,
    #                      self.t).until(EC.presence_of_all_elements_located(locator))
    # return eles
    # except TimeoutException as e:
    # print('未定位到元素', locator)
    # raise e

    # @allure.step('Click text - {text}')
    # def click_by_text(self, text: str):
    #     # self.driver.get_by_text(text).click()
    #     self.driver.find_element(By.LINK_TEXT, text).click()
    #
    # @allure.step('select option - {text} - {title}')
    # def select_option(self, title: str, text: str):
    #     self.driver.get_by_title(title).get_by_text(text).click()
    #
    # # @allure.step('Click button - {button}')
    # # def click_by_button(self, button: str):
    # #     self.driver.get_by_role("button", name=button).click()
    #

    # def text_assert(self,assert_type, assert_text, expected_text=None):
    #     """
    #     检查expected_text是否存在于text中
    #     使用Python内置的count方法计算text中expected_text出现的次数
    #     如果expected_text在text中出现，那么其出现次数应大于0
    #     如果expected_text不在text中，断言将失败，并抛出一个AssertionError异常。异常的错误消息将包含期望的文本和实际的文本。
    #     """
    #     self.assert_type = assert_type
    #     self.assert_text = assert_text
    #     self.expected_text = expected_text
    #
    #     if self.expected_text is not None:
    #         if self.assert_type == 'assert_text_in':
    #             assert self.assert_text.count(
    #                 self.expected_text) > 0, f"Expected text '{self.expected_text}' not found in '{self.assert_text}'"
    #
    #             print("Test passed successfully!!")
    #         elif self.assert_type == 'assert_equal':
    #             assert self.assert_text == self.expected_text, "实际值{}与期望值{}不相等".format(self.assert_text,
    #                                                                                    self.expected_text)
    #             print("Test passed successfully!")
    #         else:
    #             print("expected_text值不为空时，assert_type类型{}有误".format(self.assert_type))
    #
    #     elif self.assert_type == 'assert_not_none':
    #         assert self.assert_text, '期望值{}是None'.find(self.assert_text)
    #     else:
    #         print("expected_text值为空时，assert_type类型{}有误".format(self.assert_type))
