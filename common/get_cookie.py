import requests


def login_cookie():
    session = requests.session()
    login_url = 'https://test.hkciot.com/cuteview/user/login'
    method = 'post'
    headers = {
        'Content-Type': 'application/json'
    }
    req_data = {
        'userIdentification': 'uitest',
        'pwdOrVerifyCode': 'Aa12345678',
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
    return cookies_str


def headers():
    cookie = login_cookie()
    headers = {'Content-Type': 'application/json',
               'cookie': cookie,
               'Context-Crop-Id': '1751805517940535298',
               'Context-Org-Id': '1751805517940535299'
               }
    return headers
