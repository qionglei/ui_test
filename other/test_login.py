# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# def test_login():
#     driver = webdriver.Firefox()
#     driver.get("http://www.baidu.com")
#     print(driver.title)
#     driver.close()

# def test_login():
#     driver = webdriver.Firefox()
#     driver.set_window_position(x=50, y=60)
#     driver.set_window_size(width=1366, height=700)
#     driver.get("http://www.python.org")
#     print(driver.title)
#     driver.close()

# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     driver.set_window_position(x=50,y=60)
#     driver.set_window_size(width=1366, height=700)
#     driver.get("http://www.python.org")
#     print(driver.title)
#     driver.close()
#
# import pytest
# from temp.homepage import HomePage
# from selenium import webdriver
#
# # driver = webdriver.Firefox()   #firefox驱动
# driver = webdriver.Chrome()
#
#
# @pytest.fixture(scope='class')
# def home_page(request):
#     home_page = HomePage(driver)
#     request.cls.home_page = home_page
#     yield home_page
#
#
# @pytest.mark.usefixtures('home_page')
# class TestCase:
#     def test_search_case01(self):
#         """测试用例一：查询功能"""
#         # home = HomePage(driver)
#         home_page = self.home_page
#         home_page.search_info("python")

# def test_search_case02(self):
#     """测试用例二：跳转新闻页"""
#     # home = HomePage(driver)
#     home_page = self.home_page
#     home_page.goto_news()
#
# def test_search_case03(self):
#     """测试用例三：跳转地图页"""
#     # home = HomePage(driver)
#     home_page = self.home_page
#     home_page.goto_map()
