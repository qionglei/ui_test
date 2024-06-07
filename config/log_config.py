import logging
import os
import yaml

# from conftest import driver

yamlPath = 'D:\\ui\config\log_donfig.yaml'


def read_yaml(yamlPath):
    """
    读取yaml文件内容realPath: 文件的真实绝对路径
    """
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
    with open(yamlPath, 'r', encoding='utf-8') as f:
        cfg = f.read()
    content = yaml.load(cfg, Loader=yaml.FullLoader)
    return content


config = read_yaml('D:\\ui\config\log_donfig.yaml')['log']
logger = logging.getLogger(__name__)

# 文件输出设置
logger.setLevel(level=config['level'])
handler = logging.FileHandler("log.txt")
handler.setLevel(config['file_handler_level'])
formatter = logging.Formatter(config['formatter'])
handler.setFormatter(formatter)

# 控制台输出设置
console = logging.StreamHandler()
console.setLevel(config['stream_handler_level'])
console.setFormatter(formatter)

# 加入到hander
logger.addHandler(handler)
logger.addHandler(console)

# 示例代码
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")
# 使用示例



from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from datetime import datetime
# import os
from conftest import driver




# # 使用示例
# # driver = webdriver.Chrome()
#     driver.get("http://www.example.com")
#
# if __name__ =="__main__":
#     # 假设有一个操作失败了，我们调用get_screenshot来保存截图
#
#     get_screenshot(driver, "failure_screenshot")
#
#     # 关闭浏览器
#     driver.quit()