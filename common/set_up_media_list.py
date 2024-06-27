import json
import logging

from common.get_cookie import login_cookie, headers, crop_id, org_id
import requests
# from config.log_config import logger


class MediaList:
    cookie = login_cookie()
    headers = headers()

    def get_media_list(self):
        global folder_ids, media_ids
        cookie = self.cookie
        headers = self.headers

        host = "https://test.hkciot.com"
        base_url = "/cuteview/media/getInPage"
        media_url = host + base_url
        body = {
            "cropId": crop_id(),
            "folderId": "0",
            "mediaId": "",
            "orgId": org_id(),
            "secType": "",
            "name": "",
            "tagIds": [],
            "type": "",
            "pageIndex": 1,
            "pageSize": 10
        }

        response = requests.post(url=media_url, headers=headers, data=json.dumps(body))
        res = response.json()
        media_is_null =res["data"]["mediaFormatDtoList"]
        if media_is_null is not None:
            media_ids = [media['id'] for media in res['data']['mediaFormatDtoList']]
            media_names = [media['name'] for media in res['data']['mediaFormatDtoList']]

        else:
            media_ids = None

        folder_is_null = res["data"]["folderList"]

        if folder_is_null is not None:
            folder_ids = [folder['id'] for folder in res['data']['folderList']]
        else:
            folder_ids = None
        print("media_ids:",media_ids)
        print("folder_ids:",folder_ids)
        return media_ids, folder_ids

    def delete_all_media(self):
        media_ids, folder_ids = self.get_media_list()
        delete_media_url = 'https://test.hkciot.com/cuteview/media/delete'
        data = {
            "folderIds": [],
            "ids": media_ids
        }
        response = requests.post(url=delete_media_url, headers=self.headers, data=json.dumps(data))
        res = response.json()
        # logger.info("success detele all medias")

    def delete_all_folder(self):
        media_ids, folder_ids = self.get_media_list()
        delete_url = "https://test.hkciot.com/cuteview/media/delete"
        body = {
            "folderIds": folder_ids,
            "ids": []
        }
        resp = requests.post(url=delete_url, data=json.dumps(body), headers=self.headers)
        # logger.info("success detele all folders")

if __name__ == "__main__":
    media_list = MediaList()
    media_list.get_media_list()
    # media_list.delete_all_folder()
    # media_list.delete_all_media()
