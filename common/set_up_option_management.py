import json
import logging

from common.get_cookie import login_cookie, headers, crop_id, org_id
import requests,json

cookie = login_cookie()
headers = headers()
crop_id =crop_id()
org_id =org_id()

print("crop_id",crop_id)
print("org_id",org_id)
class OptionManagement:


    def org_type_list(self):
        base_url = 'https://test.hkciot.com/cuteview/tag/get'
        body = {
            "cropId": crop_id,
            "orgId": org_id,
            "type": 4
        }
        print("crop_id11", crop_id)
        print("org_id111", org_id)
        resp = requests.post(url = base_url,data=json.dumps(body),headers=headers)
        resp = resp.json()
        org_type_list = [ids['id'] for ids in resp['data']]

        print(org_type_list)
        return org_type_list


    def clear_all_org_type(self):

        org_type_list = self.org_type_list()
        for org_type_id in org_type_list:
            del_url = f'https://test.hkciot.com/cuteview/tag/delete/{org_type_id}'
            print("id:",org_type_id)
            body ={
                        "id": org_type_id
                    }
            resp = requests.post(url =del_url,data=json.dumps(body),headers=headers)
            resp = resp.json()
            print(resp)

    def org_level_list(self):
        base_url = 'https://test.hkciot.com/cuteview/tag/get'
        body = {
            "cropId": crop_id,
            "orgId": org_id,
            "type": 5
        }
        print("crop_id11", crop_id)
        print("org_id111", org_id)
        resp = requests.post(url = base_url,data=json.dumps(body),headers=headers)
        resp = resp.json()
        org_type_list = [ids['id'] for ids in resp['data']]

        print(org_type_list)
        return org_type_list


    def clear_all_org_level(self):

        org_level_list = self.org_level_list()
        for org_level_id in org_level_list:
            del_url = f'https://test.hkciot.com/cuteview/tag/delete/{org_level_id}'
            print("id:",org_level_id)
            body ={
                        "id": org_level_id
                    }
            resp = requests.post(url =del_url,data=json.dumps(body),headers=headers)
            resp = resp.json()
            print(resp)

#
# if __name__ == "__main__":
#     option_class = OptionManagement()
#     option_class.org_type_list()
#     option_class.clear_all_org_type()
#     option_class.org_level_list()
#     option_class.clear_all_org_level()