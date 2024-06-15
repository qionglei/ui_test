import json
import time

import requests

from common.get_cookie import login_cookie,headers
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
            'cropId': '1751805517940535298',
            'currentPage': 1,
            'pageSize': 10,
            'name': '',
            'orgId': '1751805517940535299',
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
        headers = {'Content-Type': 'application/json',
                   'cookie': cookie,
                   'Context-Crop-Id': '1751805517940535298',
                   'Context-Org-Id': '1751805517940535299'
                   }
        body = {
            "cropId": "1751805517940535298",
            "name": "",
            "id": "",
            "ids": terminal_id,
            "orgId": "1751805517940535299",
            "orgIds": [],
            "sn": "",
            "tagId": 0,
            "tagIds": []
        }
        url = 'https://test.hkciot.com/cuteview/terminal/delete'
        resp = requests.post(url, data=json.dumps(body), headers=headers)
        # print("删除设备的接口响应为:", resp)

    def get_terminal_names(self):
        """
        获取设备列表
        :return: 返回列表list
        """

        body = {
            'cropId': '1751805517940535298',
            'currentPage': 1,
            'pageSize': 10,
            'name': '',
            'orgId': '1751805517940535299',
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
                "cropId": "1751805517940535298",
                "name": sn,
                "orgId": org_list.get_org_id(),
                "tagIds": [],
                "sn": sn
            }

        response =requests.post(url=add_terminal_url,data =json.dumps(body),headers=self.headers)
        print("响应数据是：",response.json())
        print("org_id的值是：",org_list.get_org_id())


#
# if __name__ == '__main__':
#     list_t = Terminal_List()
#     ids = list_t.get_terminal_list()
#     list_t.add_terminal_api("123458866865578")
