import json

import requests
from common.get_cookie import login_cookie,headers,crop_id,org_id


class PlayBill:
    cookie = login_cookie()
    headers = headers()

    def get_play_bill_ids(self):

        base_url = 'https://test.hkciot.com/cuteview/play-bill/page/1/10'

        body = {
            "cropId": crop_id(),
            "orgId": org_id(),
            "currentPage": 1,
            "pageSize": 10
        }

        reponse = requests.post(url=base_url, headers=self.headers, data=json.dumps(body))
        resp = reponse.json()

        play_bill_ids = [ids["id"] for ids in resp["data"]["records"]]
        # print("获取所有的节目单id")

        return play_bill_ids

    def clear_play_bill(self):
        clear_base_url ='https://test.hkciot.com/cuteview/play-bill/delete'
        all_ids  = self.get_play_bill_ids()
        for ids in range(0,len(all_ids)):
            id = all_ids[ids]
            body = {
                "ids": [id]
            }
            data = json.dumps(body)
            reponse = requests.post(url=clear_base_url, headers=self.headers, data=json.dumps(body))

# if __name__ == "__main__":
#     play_bill_list = PlayBill()
#     play_bill_list.get_play_bill_ids()
#     play_bill_list.clear_play_bill()
#     play_bill_list.get_play_bill_ids()