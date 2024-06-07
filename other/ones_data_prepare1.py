# -*- coding: utf-8 -*-
import json
import os
import requests
import yaml


def read_config():
    # 获取config.yaml变量
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("JiraMigrationTool_UITest") + len("JiraMigrationTool_UITest")]
    config_path = os.path.abspath(rootPath + '/config.yaml')

    with open(config_path) as f:
        env_info = yaml.load(f.read(), Loader=yaml.SafeLoader)
        return env_info


def prepare_data():
    # 获取配置信息
    config_env = read_config()
    # 获取ONES token、uuid、team_uuid、org_uuid
    login_url = config_env["base_url"] + "/#/login"
    login_payload = json.dumps({
        "userIdentification": config_env["config_env_user1"],
        "pwdOrVerifyCode": config_env["config_env_pwd"],
        "loginType": 1
    })
    login_headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
    }
    login_response = requests.request("POST", login_url, headers=login_headers, data=login_payload)


def get_crop_info():
    # 获取企业信息
    config_env = read_config()
    # 获取ONES token、uuid、team_uuid、org_uuid
    get_crop_url = config_env["base_url"] + "/cuteview/crop/get"
    # login_payload = json.dumps({
    #     "pwdOrVerifyCode": config_env["config_env_pwd"],
    #     "loginType": 1,
    #     "userIdentification": config_env["config_env_user1"]
    # })


    # login_response = requests.request("POST", login_url, headers=login_headers, data=login_payload)
    # token = json.loads(login_response.text)["user"]["token"]
    # uuid = json.loads(login_response.text)["user"]["uuid"]
    # team_uuid = json.loads(login_response.text)["teams"][0]["uuid"]
    # org_uuid = json.loads(login_response.text)["org"]["uuid"]
    hkc_headers = {
        'Referer': config_env["base_url"],
        'Host': config_env["base_url"],
        'Content-Type': 'application/json',
    }
    crop_info_response = requests.request("POST", get_crop_url, headers=hkc_headers)
    print(crop_info_response)
    # return team_uuid, hkc_headers

# if __name__ == "__main__":
#     get_crop_info()


# def create_custom_fields():
#     team, api_headers = get_crop_info()
#     config_env = read_config()
#     api_url = config_env["config_env_url"] + config_env["base_url"] + "/team/" + team + "/fields/add"
#     multi_choice = {"field": {
#         "name": "自定义单选菜单",
#         "type": 16,
#         "renderer": 1,
#         "filter_option": 0,
#         "search_option": 1,
#         "options": [
#             {
#                 "value": "多选001",
#                 "background_color": "#307fe2",
#                 "color": "#fff"
#             },
#             {
#                 "value": "多选002",
#                 "background_color": "#00b388",
#                 "color": "#fff"},
#             {
#                 "value": "多选003",
#                 "background_color": "#00b388",
#                 "color": "#fff"},
#             {
#                 "value": "多选004",
#                 "background_color": "#00b388",
#                 "color": "#fff"},
#             {
#                 "value": "我是超长的多选选项值呀哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈或或或或或或",
#                 "background_color": "#f1b300",
#                 "color": "#fff"}
#         ]
#     }}
#     single_line = {
#         "field": {
#             "name": "自定义单行文本",
#             "type": 2,
#             "renderer": 1,
#             "filter_option": 0,
#             "search_option": 1
#         }
#     }
#     multi_line = {
#         "field": {
#             "name": "自定义多行文本",
#             "type": 15,
#             "renderer": 1,
#             "filter_option": 0,
#             "search_option": 1
#         }
#     }
#     number_field = {
#         "field": {
#             "name": "自定义浮点数",
#             "type": 4,
#             "renderer": 1,
#             "filter_option": 0,
#             "search_option": 1
#         }
#     }
#     date_field = {
#         "field": {
#             "name": "自定义日期",
#             "type": 5,
#             "renderer": 1,
#             "filter_option": 0,
#             "search_option": 1
#         }
#     }
#     datetime_field = {
#         "field": {
#             "name": "自定义时间",
#             "type": 6,
#             "renderer": 1,
#             "filter_option": 0,
#             "search_option": 1
#         }
#     }
#     multiple_user = {
#         "field": {
#             "name": "自定义多选成员",
#             "type": 13,
#             "renderer": 1,
#             "filter_option": 0,
#             "search_option": 1
#         }
#     }
#     single_user = {
#         "field": {
#             "name": "自定义单选成员",
#             "type": 8,
#             "renderer": 1,
#             "filter_option": 0,
#             "search_option": 1
#         }
#     }
#     custom_list = [multi_choice, single_line, multi_line, number_field, date_field, datetime_field, multiple_user,
#                    single_user]
#     for field in custom_list:
#         requests.request("POST",
#                          api_url, headers=api_headers, data=json.dumps(field))
