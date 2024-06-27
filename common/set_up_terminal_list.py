import json
import random
import time

import requests

from common.get_cookie import login_cookie,headers,crop_id,org_id
from common.set_up_org import OrgList

org_list = OrgList()


class Terminal_List:
    cookie = login_cookie()
    headers = headers()

    def get_terminal_list(self):
        """
        获取设备列表
        :return: 返回列表list
        """

        body = {
            'cropId': crop_id(),
            'currentPage': 1,
            'pageSize': 10,
            'name': '',
            'orgId': org_id(),
            'orgIds': [],
            'tagIds': []
        }

        # cookie = self.login_cookie()
        cookie = self.cookie
        # print('api拿到的cookie是', cookie)
        url = 'https://test.hkciot.com/cuteview/terminal/list-page/1/10'

        reponse = requests.post(url=url, data=json.dumps(body), headers=self.headers)
        # print(reponse.json())

        # 拿到所有的设备id
        res = reponse.json()

        ids = [record['id'] for record in res['data']['records']]
        # print("拿到的ids：", ids)
        return ids

    def delete_terminal(self, terminal_id):
        ids = self.get_terminal_list()
        cookie = self.cookie
        # headers = {'Content-Type': 'application/json',
        #            'cookie': cookie,
        #            'Context-Crop-Id': '1751805517940535298',
        #            'Context-Org-Id': '1751805517940535299'
        #            }
        body = {
            "cropId": crop_id(),
            "name": "",
            "id": "",
            "ids": terminal_id,
            "orgId": org_id(),
            "orgIds": [],
            "sn": "",
            "tagId": 0,
            "tagIds": []
        }
        del_url = 'https://test.hkciot.com/cuteview/terminal/delete'
        resp = requests.post(url = del_url, data=json.dumps(body), headers=headers())
        # print("删除设备的接口响应为:", resp.json)
        # print("请求头body内容是：",resp.request.body)


    def clear_terminal(self):
        ids = self.get_terminal_list()
        cookie = self.cookie
        # headers = {'Content-Type': 'application/json',
        #            'cookie': cookie,
        #            'Context-Crop-Id': '1751805517940535298',
        #            'Context-Org-Id': '1751805517940535299'
        #            }

        terminal_id = self.get_terminal_list()

        body = {
            "cropId": crop_id(),
            "name": "",
            "id": "",
            "ids": terminal_id,
            "orgId": org_id(),
            "orgIds": [],
            "sn": "",
            "tagId": 0,
            "tagIds": []
        }
        url = 'https://test.hkciot.com/cuteview/terminal/delete'
        resp = requests.post(url, data=json.dumps(body), headers=headers())
        # print("删除设备的接口响应为:", resp)
        # print("请求头body内容是：",resp.request.body)


    def get_terminal_names(self):
        """
        获取设备列表
        :return: 返回列表list
        """

        body = {
            'cropId': crop_id(),
            'currentPage': 1,
            'pageSize': 10,
            'name': '',
            'orgId': org_id(),
            'orgIds': [],
            'tagIds': []
        }

        # cookie = self.login_cookie()
        cookie = self.cookie
        # print('api拿到的cookie是', cookie)
        url = 'https://test.hkciot.com/cuteview/terminal/list-page/1/10'

        reponse = requests.post(url=url, data=json.dumps(body), headers=self.headers)
        # print(reponse.json())

        # 拿到所有的设备id
        res = reponse.json()

        names = [record['name'] for record in res['data']['records']]
        # print("拿到的ids：", ids)
        return names

    def add_terminal_api(self,sn):

        add_terminal_url ='https://test.hkciot.com/cuteview/terminal/join'

        body = {
                "cropId": crop_id(),
                "name": sn,
                "orgId": org_list.get_org_id(),
                "tagIds": [],
                "sn": sn
            }

        response =requests.post(url=add_terminal_url,data =json.dumps(body),headers=self.headers)
        # print("响应数据是：",response.json())
        # print("org_id的值是：",org_list.get_org_id())



if __name__ == '__main__':
    list_t = Terminal_List()
    get_ids = list_t.get_terminal_list()
    # print("ids:",get_ids)
    # names = list_t.get_terminal_names()
    # list_t.add_terminal_api(random.randint(1000,50000))

    # list_t.delete_terminal(get_ids)
    list_t.clear_terminal()
