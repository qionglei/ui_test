import allure
import pytest
import os
import yaml
from selenium import webdriver

from pageobject.login_page import LoginPage

# 加载读取配置文件config.yaml
from data_clean import api_clear_data


@pytest.fixture(scope="session", autouse=True)
def env(request):
    config_path = os.path.join(request.config.rootdir, "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config


@pytest.fixture(scope="session", autouse=True)
def driver(env):
    """测试hkc登录模块"""
    driver = webdriver.Chrome()
    # ===============================创建了chrome浏览器=========================================================
    driver.implicitly_wait(20)
    # driver.maximize_window()
    print("\n setup begin============= \n")
    test_env_url = env["test_env_url"]
    driver.get(test_env_url)
    login_page = LoginPage(driver)
    login_page.success_login(env)
    global DRIVER
    DRIVER = driver
    yield driver
    api_clear_data()
    # driver.close()
    driver.quit()
    print("=============登录结束============")


def env_conf():
    # config_path = os.path.join(request.config.rootdir, "config.yaml")
    conf_path = r"D:\git\ui_test\config.yaml"
    with open(conf_path) as f:
        environment_conf = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return environment_conf


# # conftest.py 或者一个插件中
#
# def pytest_runtest_makereport(item, call):
#     if call.excinfo is not None:
#         # 如果有异常信息，则获取异常信息
#         reason = call.excinfo.type.__name__
#         if "DivisionByZero" in reason:
#             # 如果异常是除以零，则标记为跳过
#             call.excinfo.type = pytest.skip("skipping division by zero")
#
# #
# def pytest_runtest_call(item):
#     try:
#         item.runtest()
#     except Exception as e:
#         # 如果抛出了一个pytest.skip或pytest.xfail的异常，则直接处理它
#         if isinstance(e, (pytest.skip, pytest.xfail)):
#             raise e
#         # 否则，重新抛出异常
#         raise

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport():
#     outcome = yield
#     test_result = outcome.get_result()
#
#     if test_result.when in ["setup", "call"]:
#         xfail = hasattr(test_result, 'wasxfail')
#         # if test_result.failed or (test_result.skipped and xfail):
#         if test_result.failed or test_result.skipped:
#             global PAGE
#             if PAGE:
#                 allure.attach(PAGE.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)
#                 allure.attach(PAGE.content(), name='html_source', attachment_type=allure.attachment_type.HTML)
