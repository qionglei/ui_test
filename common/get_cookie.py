import requests
import yaml


def read_config():
    conf_path = r"D:\git\ui_test\config.yaml"
    with open(conf_path) as f:
        env_config = yaml.load(f.read(),Loader = yaml.SafeLoader)
    return env_config



def login_cookie():
    session = requests.session()
    login_url = 'https://test.hkciot.com/cuteview/user/login'
    method = 'post'
    headers = {
        'Content-Type': 'application/json'
    }
    req_data = {
        'userIdentification': config["test_env_username"],
        'pwdOrVerifyCode': config["test_env_password"],
        'loginType': 1
    }
    reps = requests.request(method, login_url, json=req_data)
    reps_json = reps.json()
    # print('登录成功，获取的接口响应reps是:', reps_json)
    cookies = reps.cookies
    # print('拿到的cookie是', cookies)

    cookies_str = ''  # 将获取的登录cookies拼接为字符串
    for k, v in cookies.items():
        cookies_str += f'{k}={v};'  # key=value;的方式拼接
    # print(cookies_str)
    return cookies_str


def headers():
    cookie = login_cookie()
    headers = {'Content-Type': 'application/json',
               'cookie': cookie,
               'Context-Crop-Id': crop_id(),
               'Context-Org-Id': org_id()
               }
    return headers

# 通过login接口，获取userid、orgid、cropid

session = requests.session()
login_url = 'https://test.hkciot.com/cuteview/user/login'

# 用户账户和密码
config = read_config()
username = config["test_env_username"]
password = config["test_env_password"]


#
# headers = {
#     'Content-Type': 'application/json'
# }

def user_id():
    req_data = {
        'userIdentification':  username,
        'pwdOrVerifyCode':  password,
        'loginType': 1
    }

    reps = requests.post(url= login_url, json=req_data)
    reps_json = reps.json()

    user_id = [id["userId"] for id in reps_json["data"]]
    user_id = user_id[0]
    # print(user_id)
    return user_id

def crop_id() :
    req_data = {
        'userIdentification':  username,
        'pwdOrVerifyCode':  password,
        'loginType': 1
    }
    reps = requests.post(url= login_url, json=req_data)
    reps_json = reps.json()

    crop_id = [id["cropId"] for id in reps_json["data"]]
    crop_id = crop_id[0]
    # print(crop_id)
    return crop_id

def org_id():
    req_data = {
        'userIdentification': username,
        'pwdOrVerifyCode': password,
        'loginType': 1
    }
    reps = requests.post(url= login_url, json=req_data)
    reps_json = reps.json()

    org_id = [id["orgId"] for id in reps_json["data"]]
    org_id = org_id[0]
    # print(org_id)
    return org_id

# if __name__ == "__main__":
#     org_id()
#     user_id()
#     crop_id()
#     login_cookie()
#     headers()
#

