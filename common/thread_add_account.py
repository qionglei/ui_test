import json
import random
import threading
import requests

# 假设这些是从common.thread模块导入的
from common.get_cookie import org_id,crop_id,login_cookie,headers

def request_api():
    # 生成随机手机号码
    phone = '1' + random.choice(['3', '4', '5', '6', '7', '8', '9'])
    for _ in range(0, 9):
        digit = random.randint(0, 9)
        phone += str(digit)

    # print("生成的随机手机号码是：", phone)
    base_url = "https://test.hkciot.com/cuteview/userinfo/other/create"
    body = {
        "account": "",
        "accountType": "2",
        "cropId": crop_id(),
        "email": "",
        "id": "",
        "orgId": org_id(),
        "phone": phone
    }

    response = requests.post(url=base_url, json=body, headers=headers())  # 使用json参数直接发送JSON
    result = response.json()
    print(f"线程名称是：{threading.current_thread().name}, 响应是：{result}")
    return result

#
# 创建线程锁和结果列表
lock = threading.Lock()

# 定义线程数量
thread_count = 5


# 创建并启动线程
def create_and_start_threads(count):
    threads = []
    for _ in range(count):
        t = threading.Thread(target=run_thread)
        # 使用 append() 方法将线程对象添加到列表中
        threads.append(t)
        t.start()
    return threads

results = []

# 线程函数
def run_thread():
    result = request_api()
    with lock:
        results.append(result)

    # 创建并启动线程


threads = create_and_start_threads(thread_count)

# 等待所有线程完成
for t in threads:
    t.join()

# 打印结果
print("run_thread函数返回的结果：", results)

# if __name__ == "__main__":
#     # 主程序入口，不需要再调用其他函数
#     request_api()
