import json

import requests
from common.get_cookie import login_cookie,headers


class PlayBill:
    cookie = login_cookie()
    headers = headers()

    def get_play_bill_ids(self):

        base_url = 'https://test.hkciot.com/cuteview/play-bill/page/1/10'

        body = {
            "cropId": "1751805517940535298",
            "orgId": "1751805517940535299",
            "currentPage": 1,
            "pageSize": 10
        }

        reponse = requests.post(url=base_url, headers=self.headers, data=json.dumps(body))
        resp = reponse.json()

        play_bill_ids = [ids["name"] for ids in resp["data"]["records"]]

        return play_bill_ids

    def clear_play_bill(self):
        clear_base_url ='https://test.hkciot.com/cuteview/play-bill/delete'
        all_ids  = self.get_play_bill_ids()
        if all_ids:

            first_id = all_ids[0]
            print(first_id)

            body = {
                    'ids':first_id
            }

            reponse =requests.post(url=clear_base_url,headers=self.headers,data=json.dumps(body))

# if __name__ == "__main__":
#     play_bill_list = PlayBill()
#     play_bill_list.get_play_bill_ids()
#     play_bill_list.clear_play_bill()