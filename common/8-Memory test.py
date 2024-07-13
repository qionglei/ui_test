# coding: utf-8
import os
import time
import subprocess
import uiautomator2 as u2
import threading
import matplotlib.pyplot as plt
import numpy as np
"""性能测试脚本"""


def run_cmd(adb_cmd, text='',):
    subprocess.run('adb logcat -c', shell=True) # 清除 logcat 日志缓存
    logcat_common = F'adb logcat -v time'
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
        ps = subprocess.Popen(logcat_common, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        for line in ps.stdout:
            line = (str(line)).strip()
            if text in line:
                print(F"匹配到关键行{line}")
                return 1
            else:
                continue


def get_permission(device, package_name):
    """获取权限"""
    u3 = u2.connect(device)
    u3.app_start(package_name)
    u3(text='允许').click()
    u3.app_stop(package_name)


def get_mem(device, package_name,scan_result_name, test_type):
    if test_type == "mem":
        adb_get_mem = F"adb -s {device} shell dumpsys meminfo {package_name}:remote"
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
        adb_get_mem = F"adb -s {device} shell top -n 1 | grep {package_name}:remote"
        ps = subprocess.Popen(adb_get_mem, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        for line in ps.stdout:
            line = (str(line)).strip().split(" ")
            """这里需要对打印的数据做处理，获取到计算的值并写到文件里--待处理"""


def get_mem2(filename, test_type):
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


def data_process(filename,type, test_type):
    if test_type == "mem":
        native = []
        total = []
        with open(filename, 'r') as f:
            f1 = f.readlines()

        for i in f1:
            if "Native Heap:" in i:
                i_num = (int(i.strip().split(":")[1]))/1024
                native.append(i_num)
            elif "TOTAL PSS" in i:
                y_num = (int(i.strip().split(":")[1]))/1024
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
    device = "8ASX0Y8FE" # 测试前这里修改测试的设备
    package_name = "com.test" #测试前这里修改测试的包名
    scan_type = ["云本", "纯云", "纯本"] #测试前这里修改要测试的扫描类型
    test_type = ["mem"]
    adb_cmd_kill = F"adb -s {device} shell am force-stop {package_name}"
    adb_cmd_clear = F"adb -s {device} shell pm clear {package_name}"

    start_server = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService" #启动服务
    init = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 1" #初始化
    scanAll_cloud_local = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 3" #scanAll云本扫描
    scanAll_cloud = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 2"  # scanAll纯云扫描
    scanAll_local = F"adb -s {device} shell am start-foreground-service -n {package_name}/com.antiy.avltestmemory.MyService --ei flag 4"  # scanAll纯本扫描
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
        for i in range(len(scan_type)):
            run_cmd(adb_cmd_clear)
            get_permission(device, package_name)
            run_cmd(start_server)
            result_name = F"result_{test_type[y]}{scan_type[i]}.txt"
            if scan_type[i] == "云本":
                # 创建两个线程来执行方法
                thread1 = threading.Thread(target=get_mem2, args=(result_name, test_type[y]))
                thread2 = threading.Thread(target=cmd2, args=(init, scanAll_cloud_local))
            elif scan_type[i] == "纯本":
                thread1 = threading.Thread(target=get_mem2, args=(result_name, test_type[y]))
                thread2 = threading.Thread(target=cmd2, args=(init, scanAll_local))
            else:
                thread1 = threading.Thread(target=get_mem2, args=(result_name, test_type[y]))
                thread2 = threading.Thread(target=cmd2, args=(init, scanAll_cloud))

            # 启动线程
            thread2.start()
            time.sleep(3)
            thread1.start()
            # 等待线程执行完毕

            thread1.join()
            thread2.join()

            data_process(filename=result_name, type=scan_type[i], test_type=test_type[y])







