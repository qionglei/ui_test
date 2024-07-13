import os


class App(object):
    def __init__(self):
        self.content = ""
        self.startTime = 0

    # 启动APP
    def launch_app(self):
        cmd = 'adb shell am start -W -n org.chromium.webview_shell/.WebViewBrowserActivity'  # type: str
        self.content = os.popen(cmd)

    # 停止app
    @staticmethod
    def stop_app():
        # 冷启动停止的命令
        # cmd = 'adb shell am force-stop org.chromium.webview_shell'
        # 热启动停止的命令
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    # 获取启动时间
    def get_launched_time(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

    # 单次测试过程
    def test_process(self):
        self.app.launch_app()
        time.sleep(5)
        elapsed_time = self.app.get_launched_time()
        self.app.stop_app()
        time.sleep(3)
        current_time = self.get_current_time()
        self.all_data.append((current_time, elapsed_time))

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1

        # 单次测试过程

    def test_process(self):
        time_before_launch = int(time.time())
        self.app.launch_app()
        time_after_launch = int(time.time())
        time.sleep(5)
        # elapsed_time = self.app.get_launched_time()
        elapsed_time = time_after_launch - time_before_launch
        self.app.stop_app()
        time.sleep(3)
        current_time = self.get_current_time()
        self.all_data.append((current_time, str(elapsed_time)))

        # 多次执行测试过程

    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1

        # 单次测试过程
    def test_process(self):
        # window 下用findstr，Mac下用grep
        cmd = "adb shell dumpsys cpuinfo | findstr org.chromium.webview_shell"
        self.result = os.popen(cmd)
        cpu_value = 0
        for line in self.result.readlines():
            cpu_value = line.split("%")[0]

        current_time = self.get_current_time()
        self.all_data.append((current_time, cpu_value))

        # 单次测试过程
    def test_process(self):
        # 执行获取进程ID的指令 window 下用findstr，Mac下用grep
        cmd = "adb shell ps | findstr org.chromium.webview_shell"
        result = os.popen(cmd)
        # 获取进程ID
        pid = result.readlines()[0].split(" ")[5]

        # 获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/" + pid + "/net/dev")
        for line in traffic:
            # 第一个网卡的数据
            if "eth0" in line:
                # 将所有空行换成#
                line = "#".join(line.split())
                # 然后按#号进行拆分，获取到收到和发出的流量值
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
            # 第二个网卡的数据
            elif "eth1" in line:
                line2 = "#".join(line.split())
                # 然后按#号进行拆分，获取到收到和发出的流量值
                receive2 = line2.split("#")[1]
                transmit2 = line2.split("#")[9]

        # 计算所有流量之和
        all_traffic = string.atoi(receive) + string.atoi(transmit) + string.atoi(receive2) + string.atoi(transmit2)
        # 按KB计算流量值
        all_traffic = all_traffic / 1024
        # 获取当前时间
        current_time = self.get_current_time()
        # 将获取到的数据存到数组中
        self.all_data.append((current_time, all_traffic))

        # 单次测试过程
    def test_process(self):
        cmd = "adb shell dumpsys battery"
        result = os.popen(cmd)

        for line in result:
            if "level" in line:
                power = line.split(":")[1]

        # 获取当前时间
        current_time = self.get_current_time()
        # 将获取到的数据存到数组中
        self.all_data.append((current_time, power))

    # 多次执行测试过程
    def run(self):
        cmd = "adb shell dumpsys battery set status 1"
        os.popen(cmd)
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1
            # 每5秒采集一次数据, 真实测试场景建议在0.5-1小时
            time.sleep(5)

# 控制类
class Controller(object):
    def __init__(self):
        # 定义收集数据的数组
        self.all_data = [("id", "vss", "rss")]

    # 分析数据
    def analyze_data(self):
        content = self.read_file()
        i = 0
        for line in content:
            if "org.chromium.webview_shell" in line:
                print line
                line = "#".join(line.split())
                # 角标7和8不是固定的，要看你生成的meminfo文件里vss和rss出现的位置来确定
                vss = line.split("#")[7].strip("K")
                rss = line.split("#")[8].strip("K")

                # 将获取到的数据存到数组中
                self.all_data.append((i, vss, rss))
                i = i + 1

    # 读取数据文件
    @staticmethod
    def read_file():
        mem_info = file("meminfo", "r")
        content = mem_info.readlines()
        mem_info.close()
        return content

    # 数据的存储
    def save_data_to_csv(self):
        csv_file = file('meminfo.csv', 'wb')
        writer = csv.writer(csv_file)
        writer.writerows(self.all_data)
        csv_file.close()


if __name__ == '__main__':
    controller = Controller()
    controller.analyze_data()
    controller.save_data_to_csv()