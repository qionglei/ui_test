import json

import requests
from django.http import cookie

from common.get_cookie import login_cookie, crop_id, org_id, headers
from common.set_up_media_list import MediaList

headers = headers()

print("headers:", headers)


class CreateProgram:
    cookie = login_cookie()
    media_list = MediaList()
    mediaIdList = media_list.get_media_list()
    mediaIdList = mediaIdList[0]

    def create_program(self):
        mediaIdList = self.mediaIdList

        url = 'https://test.hkciot.com/cuteview/program/simple/create'

        body = {
            "cropId": crop_id(),
            "mediaIdList": mediaIdList,
            "orgId": org_id()
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(body))
        resp = response.json()

        print(response.request.body)

        print(resp)

        program_list = [ids['id'] for ids in resp["data"]]


# if __name__ == "__main__":
#     create = CreateProgram()
#     create.create_program()
