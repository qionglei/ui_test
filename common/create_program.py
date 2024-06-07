import json

import requests
from django.http import cookie

from common.get_cookie import login_cookie
from common.set_up_media_list import MediaList


class CreateProgram:
    cookie = login_cookie()
    media_list = MediaList()
    mediaIdList = media_list.get_media_list()

    headers = {'Content-Type': 'application/json',
               'cookie': cookie,
               'Context-Crop-Id': '1751805517940535298',
               'Context-Org-Id': '1751805517940535299'
               }

    def create_program(self):
        mediaIdList = self.mediaIdList
        headers =self.headers

        url = 'https://test.hkciot.com/cuteview/program/simple/create'

        body = {
            "cropId": "1751805517940535298",
            "mediaIdList": mediaIdList,
            "orgId": "1751805517940535299"
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(body))
        resp = response.json()

        program_list =[ids['id'] for ids in resp["data"]]



# if __name__ == "__main__":
#     create = CreateProgram()
#     create.create_program()
