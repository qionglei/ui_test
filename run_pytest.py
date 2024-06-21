import os
import pytest
from time import sleep
import time
import datetime

if __name__ == "__main__":
    print("==========开始main函数==============")
    """收集报告，调试时开启"""
    # pytest.main(['-vs', '--alluredir', './result'])
    # os.system('allure generate ./result -o ./report1 --clean')

    # pytest.main(["-vs"])

    """收集报告，调试时可以关闭"""
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d-%H%M%S")
    # 此处命令 --alluredir 生成了报告的原始文件
    pytest.main(["-vs", "-n 8","--dist=loadfile","--alluredir", "./Report/{}xml".format(time_str)])
    # pytest.main(["D:\\ui\\test_case\\test_release_management.py","-vs", "--alluredir", "./Report/{}xml".format(time_str)])
    print("开始收集报告=======================>")
    # 此处命令 allure generate 将前面生成的json文件转换为html的报告
    os.system("allure generate ./Report/{}xml -o ./Report/{}html --clean".format(time_str, time_str))
    print(f"产生报告的名称{time_str}")
    # 生成的报告index.html不能直接用Chrome打开，打开后看不到内容，需要用allure open打开才能渲染出样式和显示内容
    os.system("allure open ./Report/{}html".format(time_str))
