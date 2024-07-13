# coding: utf-8
import os
import time
import subprocess
import uiautomator2
import threading
import matplotlib.pyplot as plt
import numpy as np
"""性能测试脚本"""


def run_cmd(adb_cmd, text='',):
    """
    执行代码，输出结果
    :param adb_cmd: 输入的adb命令
    :param text:
    :return:
    """
    subprocess.run('adb logcat -c', shell=True) # 清除 logcat 日志缓存
    logcat_common = F'adb logcat -v time'  # 开始打印日志,增加打印时间信息
    print(F"正在执行命令：{adb_cmd}")
    ps = os.system(adb_cmd)
    if ps == 0:
        print("执行成功")
    else:
        print("执行失败")

    if text == '':
        pass
    else:
        print(F"正在执行命令:{logcat_common}")
        # 启动一个新的进程，并捕获其输出，默认为非阻塞
        # logcat_common: 要执行的命令，字符串列表
        # subprocess.PIPE ： 为子进程创建新的管道
        ps = subprocess.Popen(logcat_common, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        for line in ps.stdout:
            line = (str(line)).strip()
            if text in line:
                print(F"匹配到关键行{line}")
                return 1
            else:
                continue


def get_permission(device, package_name):
    """获取权限
    """
    u3 = uiautomator2.connect(device)
    u3.app_start(package_name)
    # u3(text='允许').click()
    u3.app_stop(package_name)


def get_mem(device, package_name,scan_result_name, test_type):
    """
    获取内存
    :param device: 设备id
    :param package_name: 包名
    :param scan_result_name: 扫描结果名称
    :param test_type: 测试类型
    :return:
    """
    if test_type == "mem":
        # adb_get_mem = F"adb -s {device} shell dumpsys meminfo {package_name}:remote"
        adb_get_mem = F"adb -s {device} shell dumpsys meminfo {package_name}"
        ps = subprocess.Popen(adb_get_mem, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        for line in ps.stdout:
            line = (str(line)).strip()
            if "Native Heap:" in line or "TOTAL PSS" in line:
                name = (line.split(":")[0].replace("b'", "").strip())
                value_num = (line.split(":")[1].strip().split(" ")[0])
                name_value_name = name + ":" + value_num
                with open(scan_result_name, "a") as f:
                    f.write(name_value_name + "\n")
    else:
        # adb_get_mem = F"adb -s {device} shell top -n 1 | grep {package_name}:remote"
        adb_get_mem = F"adb -s {device} shell top -n 1 | grep {package_name}"
        ps = subprocess.Popen(adb_get_mem, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        for line in ps.stdout:
            line = (str(line)).strip().split(" ")
            """这里需要对打印的数据做处理，获取到计算的值并写到文件里--待处理"""


def get_mem2(filename, test_type):
    """
    获取内存，多线程
    :param filename:
    :param test_type:
    :return:
    """
    i = 0
    time1 = 10
    while i < time1:
        get_mem(device, package_name, filename, test_type)
        time.sleep(1)
        if not thread2.is_alive():
            print("线程thread2已经结束")
            i = 11
        else:
            print("线程thread2还在运行")


# def cmd2(init, scanAll):
#
#     run_cmd(init)
#     time.sleep(15)
#     scan_end = run_cmd(adb_cmd=scanAll, text="virus/total:")
#     if scan_end == 1:
#         pass
#         time.sleep(30)
#     else:
#         print("扫描异常")
#
#     scan_end1 = run_cmd(adb_cmd=scanAll, text="virus/total:")
#     if scan_end1 == 1:
#         time.sleep(30)
#     else:
#         print("扫描异常")
#
#     scan_end2 = run_cmd(adb_cmd=scanAll, text="virus/total:")
#     if scan_end2 == 1:
#         time.sleep(30)
#     else:
#         print("扫描异常")

def cmd2(init, scanAll):

    run_cmd(init)
    time.sleep(15)
    scan_end = run_cmd(adb_cmd=scanAll, text="virus/total:")
    if scan_end == 1:
        pass
        time.sleep(30)
    else:
        print("扫描异常")

    scan_end1 = run_cmd(adb_cmd=scanAll, text="virus/total:")
    if scan_end1 == 1:
        time.sleep(30)
    else:
        print("扫描异常")

    scan_end2 = run_cmd(adb_cmd=scanAll, text="virus/total:")
    if scan_end2 == 1:
        time.sleep(30)
    else:
        print("扫描异常")


def data_process(filename, test_type):
    if test_type == "mem":
        native = []
        total = []
        with open(filename, 'r') as f:
            f1 = f.readlines()

        for i in f1:
            if "Native Heap:" in i:
                # i_num = (int(i.strip().split(":")[1]))/1024
                try:
                    # 假设 i 是从某处获取的字符串
                    parts = i.strip().split(":")
                    if len(parts) > 1:
                        # 尝试移除所有非数字字符并转换为整数
                        num_str = ''.join(filter(str.isdigit, parts[1]))
                        if num_str:  # 确保字符串不为空
                            i_num = int(num_str) / 1024
                        else:
                            # 处理无法转换为整数的情况
                            print(f"无法从 '{parts[1]}' 提取有效整数")
                            i_num = None  # 或者使用其他默认值
                    else:
                        # 处理没有足够部分的情况
                        print(f"数据格式错误: '{i}'")
                        i_num = None  # 或者使用其他默认值
                except ValueError as e:
                    # 处理转换过程中可能发生的其他 ValueError（尽管在这个特定情况下可能不需要）
                    print(f"转换错误: {e}")
                    i_num = None  # 或者使用其他默认值
                except IndexError as e:
                    # 实际上在这个特定的代码片段中，IndexError 不太可能发生，因为我们已经检查了长度
                    print(f"索引错误: {e}")
                    i_num = None  # 或者使用其他默认值
                native.append(i_num)
            elif "TOTAL PSS" in i:
                # y_num = (int(i.strip().split(":")[1]))/1024
                try:
                    # 假设 i 是从某处获取的字符串
                    parts = i.strip().split(":")
                    if len(parts) > 1:
                        # 尝试移除所有非数字字符并转换为整数
                        num_str = ''.join(filter(str.isdigit, parts[1]))
                        if num_str:  # 确保字符串不为空
                            y_num = int(num_str) / 1024
                        else:
                            # 处理无法转换为整数的情况
                            print(f"无法从 '{parts[1]}' 提取有效整数")
                            y_num = None  # 或者使用其他默认值
                    else:
                        # 处理没有足够部分的情况
                        print(f"数据格式错误: '{i}'")
                        y_num = None  # 或者使用其他默认值
                except ValueError as e:
                    # 处理转换过程中可能发生的其他 ValueError（尽管在这个特定情况下可能不需要）
                    print(f"转换错误: {e}")
                    y_num = None  # 或者使用其他默认值
                except IndexError as e:
                    # 实际上在这个特定的代码片段中，IndexError 不太可能发生，因为我们已经检查了长度
                    print(f"索引错误: {e}")
                    y_num = None  # 或者使用其他默认值
                total.append(y_num)

        # 计算每组数据中的最大值及其索引
        max_y1_index = np.argmax(total)
        max_y1 = total[max_y1_index]

        max_y2_index = np.argmax(native)
        max_y2 = native[max_y2_index]
        # 绘制折线图
        plt.plot(native, label='Native')
        plt.plot(total, label='Total')

        # 标记出最大值及其索引
        plt.scatter([[max_y1_index]], [max_y1], color='red', label='Total Max')
        plt.annotate('{:.2f}'.format(max_y1), (max_y1_index, max_y1), color='red')
        plt.scatter([[max_y2_index]], [max_y2], color='green', label='Native Max')
        plt.annotate('{:.2f}'.format(max_y2), (max_y2_index, max_y2), color='green')
        # 添加标题和标签

        plt.title('Memory Test')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.legend()

        # 显示图形
        png_filename = F'mem_test_{type}.png'
        plt.savefig(png_filename)
        plt.close()

    else:
        """这里需要对传过来存入的cpu文件进行处理、生成折线图"""
        pass


if __name__ == "__main__":
    device = "172.16.125.132" # 测试前这里修改测试的设备
    package_name = "com.hkc.ebox" #测试前这里修改测试的包名
    # scan_type = ["云本", "纯云", "纯本"] #测试前这里修改要测试的扫描类型
    test_type = ["mem"]
    adb_cmd_kill = F"adb -s {device} shell am force-stop {package_name}"
    adb_cmd_clear = F"adb -s {device} shell pm clear {package_name}"

    # com.hkc.ebox/com.hkc.service.main.MainActivity

    # start_server = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService" #启动服务
    # init = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 1" #初始化
    # scanAll_cloud_local = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 3" #scanAll云本扫描
    # scanAll_cloud = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 2"  # scanAll纯云扫描
    # scanAll_local = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 4"  # scanAll纯本扫描
    start_server = F"adb -s {device} shell am start {package_name}/com.hkc.service.main.MainActivity"  # 启动服务
    init = F"adb -s {device} shell am start {package_name}/com.hkc.service.main.MainActivity --ei flag 0"  # 初始化
    scanAll_cloud_local = F"adb -s {device} shell am start {package_name}/com.hkc.service.main.SplashActivity --ei flag 0"  #播放服务
    # scanAll_cloud = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.hkc.service.main.MainActivity --ei flag 2"
    # scanAll_local = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.hkc.service.main.MainActivity --ei flag 4"
    # 遍历当前目录
    for filename in os.listdir('.'):
        # 检查文件是否为.txt文件
        if filename.endswith('.txt'):
            # 删除文件
            os.remove(filename)
        elif filename.endswith('.png'):
            # 删除文件
            os.remove(filename)
    for y in range(len(test_type)):
        # for i in range(len(scan_type)):
        run_cmd(adb_cmd_clear)
        get_permission(device, package_name)
        # run_cmd(start_server)
        result_name = F"result_{test_type[y]}.txt"

        # 创建两个线程来执行方法
        thread1 = threading.Thread(target=get_mem2, args=(result_name, test_type[y]))
        thread2 = threading.Thread(target=cmd2, args=(init, scanAll_cloud_local))

        # 启动线程
        thread2.start()
        time.sleep(3)
        thread1.start()
        # 等待线程执行完毕

        thread1.join()
        thread2.join()

        data_process(filename=result_name, test_type=test_type[y])