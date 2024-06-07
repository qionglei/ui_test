from time import sleep
from basepage.base_page import BasePage
from selenium.webdriver.common.by import By

class SelectPage(BasePage):

    '''定位页面元素'''
    #定位弹窗
    win_loc=(By.XPATH,"//div[@class='modal-body']/i")
    #定位iphone
    ip_12pro_loc=(By.XPATH,'//div[@id="collapse_1"]/div/dl[1]/dd/div/span[2]/label/span')
    # 定位iphone12 pro max
    ip_loc = (By.XPATH, "//button[@device-source='00008101-0004102C3468001E']")

    #定位品牌
    an_loc=(By.XPATH,'//div[@id="collapse_1"]/div/dl[2]/dd/div/span[3]/label/span')
    # 定位安卓魅族
    mz_loc = (By.XPATH, "//button[@device-source='864968050654030']")

    #定位上市时间
    onlin_loc=(By.XPATH,'//div[@id="collapse_1"]/div/dl[6]/dd/div/span[5]/label/span')
    # 定位上市时间的华为荣耀
    sj_loc = (By.XPATH, "//button[@device-source='7d22ebd8f913637d']")

    #定位文本框
    text_detail=(By.XPATH,'//div[@id="modal_quota_alert"]/div/div/div[2]')
    #定位取消框
    qx_but_loc=(By.XPATH,'//div[@id="modal_quota_alert"]/div/div/div[3]/button[1]')

    #点击登录按钮
    login_button=(By.ID,"submitBtn")

    #登录邮箱操作流程
    def testin_select_01_iphone(self):
        sleep(1)
        self.locate_element(self.ip_12pro_loc).click()
        sleep(1)
        self.locate_element(self.ip_loc).click()
        sleep(1)
        as_text=self.locate_element(self.text_detail).text
        '''断言信息正确'''
        assert as_text==u'您的配额已不足，是否前往购买？'
        self.locate_element(self.qx_but_loc).click()
        sleep(2)

    def testin_select_02_android(self):
        sleep(1)
        self.locate_element(self.an_loc).click()
        sleep(1)
        self.locate_element(self.mz_loc).click()
        sleep(1)
        as_text = self.locate_element(self.text_detail).text
        assert as_text == u'您的配额已不足，是否前往购买？'
        self.locate_element(self.qx_but_loc).click()
        sleep(2)

    def testin_select_03_onlin_time(self):
        sleep(1)
        self.locate_element(self.onlin_loc).click()
        sleep(1)
        self.locate_element(self.sj_loc).click()
        sleep(1)
        as_text = self.locate_element(self.text_detail).text
        assert as_text == u'您的配额已不足，是否前往购买？'
        self.locate_element(self.qx_but_loc).click()
        sleep(2)
