import json

import requests
from common.get_cookie import login_cookie, headers


# from config.log_config import logger


class OrgList:
    cookie = login_cookie()
    headers = headers()

    def get_org_ids(self):

        base_url = 'https://test.hkciot.com/cuteview/org/get'

        body = {
            "cropId": "1751805517940535298",
        }

        reponse = requests.get(url=base_url, headers=self.headers, params=body)
        resp = reponse.json()
        org_ids = [ids["id"] for ids in resp["data"]["allChildrenOrg"]]

        return org_ids

    def get_org_names(self):

        base_url = 'https://test.hkciot.com/cuteview/org/get'

        body = {
            "cropId": "1751805517940535298",
        }

        reponse = requests.get(url=base_url, headers=self.headers, params=body)
        resp = reponse.json()
        org_names = [names["name"] for names in resp["data"]["allChildrenOrg"]]

        return org_names

    def clear_all_org(self):
        body = {
            "cropId": "1751805517940535298",
        }

        global clear_base_url
        ids = self.get_org_ids()
        iter_times = len(ids)
        for id in ids:
            # print("current id:", id)
            clear_base_url = f'https://test.hkciot.com/cuteview/org/delete/{id}'
            for i in range(0, iter_times):
                requests.post(url=clear_base_url, headers=self.headers, data=json.dumps(body))
                # logger.info("success clear org")

    def add_branch(self, name="branch001"):
        org_name = self.get_org_names()
        fixed_org_name = "test门店"

        if "test门店" not in org_name:
            add_url = 'https://test.hkciot.com/cuteview/org/create'
            data = {
                "contact": "",
                "cropId": "1751805517940535298",
                "id": "",
                "level": 2,
                "name": "test门店",
                "outerCode": "",
                "parentId": "1751805517940535299",
                "phone": "",
                "type": 1,
                "businessStartTime": "",
                "businessEndTime": "",
                "orgTypeId": "",
                "orgLevelId": ""
            }
            requests.post(url=add_url, headers=self.headers, data=json.dumps(data))

# if __name__ == "__main__":
#     org_list = OrgList()
#     org_list.clear_all_org()
#     org_list.add_branch()
