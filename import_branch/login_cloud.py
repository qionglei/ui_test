import threading

import requests
import yaml


def read_config():
    conf_path = r"D:\git\ui_test\import_branch\branch_account.yaml"
    with open(conf_path, encoding='utf-8', ) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config


# 用户账户和密码
config = read_config()
# username = config["test_env_username"]
password = config["test_env_password"]


def get_env_url():
    env_url = config["env_url"]
    return env_url


env_url = get_env_url()


class import_login:
    env_url = get_env_url()
    login_url = f'{env_url}/cuteview/user/login'
    print("登录的url是", login_url)

    def __init__(self, username):
        self.username = username

    def login_cookie(self):
        session = requests.session()
        login_url = f'{env_url}/cuteview/user/login'
        # print("登录的url是2222", login_url)
        method = 'post'
        headers = {
            'Content-Type': 'application/json'
        }
        req_data = {
            'userIdentification': self.username,
            'pwdOrVerifyCode': password,
            'loginType': 1
        }
        reps = requests.request(method, login_url, json=req_data)
        reps_json = reps.json()
        # print('登录成功，获取的接口响应reps是:', reps_json)
        cookies = reps.cookies
        # print('拿到的cookie是', cookies)
        print("当前登录接口的用户名是",self.username)

        cookies_str = ''  # 将获取的登录cookies拼接为字符串
        for k, v in cookies.items():
            cookies_str += f'{k}={v};'  # key=value;的方式拼接
        # print(cookies_str)
        return cookies_str

    def headers(self):
        cookie = self.login_cookie()
        headers = {'Content-Type': 'application/json',
                   'cookie': cookie,
                   'Context-Crop-Id': self.crop_id(),
                   'Context-Org-Id': self.org_id()
                   }
        return headers

    # 通过login接口，获取userid、orgid、cropid

    session = requests.session()

    def user_id(self):
        req_data = {
            'userIdentification': self.username,
            'pwdOrVerifyCode': password,
            'loginType': 1
        }

        reps = requests.post(url=self.login_url, json=req_data)
        reps_json = reps.json()

        user_id = [id["userId"] for id in reps_json["data"]]
        user_id = user_id[0]
        # print("user_id:", user_id)
        return user_id

    def crop_id(self):
        req_data = {
            'userIdentification': self.username,
            'pwdOrVerifyCode': password,
            'loginType': 1
        }
        reps = requests.post(url=self.login_url, json=req_data)
        reps_json = reps.json()

        crop_id = [id["cropId"] for id in reps_json["data"]]
        crop_id = crop_id[0]
        print("crop_id:", crop_id)
        return crop_id

    def org_id(self):
        req_data = {
            'userIdentification': self.username,
            'pwdOrVerifyCode': password,
            'loginType': 1
        }
        reps = requests.post(url=self.login_url, json=req_data)
        reps_json = reps.json()

        org_id = [id["orgId"] for id in reps_json["data"]]
        org_id = org_id[0]
        # print("org_id:", org_id)
        return org_id


#
# if __name__ == "__main__":
#     # 多线程跑4个账号
#     config = read_config()
#     user1 = config["test_env_username1"]
#     user2 = config["test_env_username2"]
#     user3 = config["test_env_username3"]
#     user4 = config["test_env_username4"]
#
#     user1_login = import_login(user1)
#     user2_login = import_login(user2)
#     user3_login = import_login(user3)
#     user4_login = import_login(user4)
#
#     def thread1():
#
#         user1_login.login_cookie()
#         user1_login.crop_id()
#
#     def thread2():
#         user2_login.login_cookie()
#         user2_login.crop_id()
#
#     def thread3():
#
#         user3_login.login_cookie()
#         user3_login.crop_id()
#
#     def thread4():
#         user4_login.login_cookie()
#         user4_login.crop_id()
#
#
#     thread1 = threading.Thread(target=thread1)
#     thread2 = threading.Thread(target=thread2)
#     thread3 = threading.Thread(target=thread3)
#     thread4 = threading.Thread(target=thread4)
#     thread1.start()
#     thread2.start()
#     thread3.start()
#     thread4.start()
#     print("线程1已启动")
#     print("线程2已启动")
#     print("线程3已启动")
#     print("线程4已启动")
#     thread1.join()
#     thread2.join()
#     thread3.join()
#     thread4.join()

