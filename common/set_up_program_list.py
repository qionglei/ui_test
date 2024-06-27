import requests
import json
from common.get_cookie import login_cookie,headers,crop_id,org_id

class ProgramList:
    cookie = login_cookie()
    headers = headers()

    def get_program_list_ids(self):
        base_url = 'https://test.hkciot.com/cuteview/program/getInPage'

        body = {
            "cropId": crop_id(),
            "orgId": org_id(),
            "folderId": 0,
            "pageIndex": 1,
            "pageSize": 10
        }
        response = requests.post(url=base_url, headers=self.headers, data=json.dumps(body))
        resp = response.json()

        program_ids = [all_ids['id'] for all_ids in resp['data']['programBasicFormatDtoList']]

        program_folder_count = resp["data"]["folderList"]

        if program_folder_count is not None:
            program_folder_id = [folder_id['id'] for folder_id in resp["data"]["folderList"]]

            print("program_folder_id:", program_folder_id)
        else:
            program_folder_id = None

        return program_ids, program_folder_id

    def get_program_list_names(self):
        base_url = 'https://test.hkciot.com/cuteview/program/getInPage'

        body = {
            "cropId": crop_id(),
            "orgId": org_id(),
            "folderId": 0,
            "pageIndex": 1,
            "pageSize": 10
        }
        response = requests.post(url=base_url, headers=self.headers, data=json.dumps(body))
        resp = response.json()
        program_names = [all_ids['name'] for all_ids in resp['data']['programBasicFormatDtoList']]
        return program_names

    def delete_all_program(self):
        all_ids, program_folder_id = self.get_program_list_ids()
        delete_url = 'https://test.hkciot.com/cuteview/program/delete'

        body = {
            "ids": all_ids
        }

        requests.post(url=delete_url, headers=self.headers, data=json.dumps(body))
        # logger.info("success clear all program")

    def delete_all_program_folders(self):
        global folder_id
        program_ids, program_folder_id = self.get_program_list_ids()

        delete_program_folder_base_url = "https://test.hkciot.com/cuteview/folder/delete/"
        if program_folder_id:
            for folder_id in program_folder_id:
                delete_program_folder_full_url = delete_program_folder_base_url + str(folder_id)
                requests.post(url=delete_program_folder_full_url, headers=self.headers)

#
# if __name__ == "__main__":
#     programlist = ProgramList()
#     programlist.get_program_list_ids()
#     programlist.delete_all_program_folders()
#     programlist.delete_all_program()
