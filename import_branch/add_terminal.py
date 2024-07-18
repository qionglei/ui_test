import concurrent.futures
import json
import random
import threading
import time

import requests

# 设备名称随机生成

from login_cloud import import_login, get_env_url, read_config
from import_branch import AddShop

config = read_config()
user1 = config["test_env_username1"]
user2 = config["test_env_username2"]
user3 = config["test_env_username3"]
user4 = config["test_env_username4"]

users =[user1,user2,user3,user4]

env_url = get_env_url()


class AddTerminal:

    def __init__(self, crop_id, org_id, headers,shop_type_ids):
        self.crop_id = crop_id
        self.org_id = org_id
        self.shop_type_ids = shop_type_ids
        self.headers = headers

    def get_terminal_list(self):
        """
        获取设备列表
        :return: 返回列表list
        """

        body = {
            'cropId': self.crop_id,
            'currentPage': 1,
            'pageSize': 1000,
            'name': '',
            'orgId': self.org_id,
            'orgIds': [],
            'tagIds': []
        }
        url = f'{env_url}/cuteview/terminal/list-page/1/1000'

        print("设备列表的url是;",url)
        print("crop_id:",self.crop_id)
        print("org_id:",self.org_id)

        reponse = requests.post(url=url, data=json.dumps(body), headers=self.headers)
        print("设备列表接口：",reponse.json())

        # 拿到所有的设备id
        res = reponse.json()

        ids = [record['id'] for record in res['data']['records']]
        print("拿到的ids：", ids)
        return ids

    def delete_terminal(self, terminal_id):
        ids = self.get_terminal_list()
        body = {
            "cropId": self.crop_id,
            "name": "",
            "id": "",
            "ids": terminal_id,
            "orgId": self.org_id,
            "orgIds": [],
            "sn": "",
            "tagId": 0,
            "tagIds": []
        }
        del_url = f'{env_url}/cuteview/terminal/delete'
        resp = requests.post(url=del_url, data=json.dumps(body), headers=self.headers)
        # print("删除设备的接口响应为:", resp.json)
        # print("请求头body内容是：",resp.request.body)

    def clear_terminal(self):
        ids = self.get_terminal_list()

        # print("ids**************************************:", ids)
        for id in ids:
            data = {
                "cropId": self.crop_id,
                "name": "",
                "id": "",
                "ids": [
                    id
                ],
                "orgId": self.org_id,
                "orgIds": [],
                "sn": "",
                "tagId": 0,
                "tagIds": []
            }
            del_url = f'{env_url}/cuteview/terminal/delete'
            resp = requests.post(url=del_url, data=json.dumps(data), headers=self.headers)
            # print("删除设备的接口响应为:", resp.json())
            # print("请求头body内容是：", resp.request.body)

    def add_terminal_for_each_shop(self):
        print("添加设备：*-*-*-*-*-*-*-*-*-*-*-*/-*-**")
        add_url = f"{env_url}/cuteview/terminal/join"
        print("函数中org-id:",self.shop_type_ids)
        for shop in self.shop_type_ids:
            terminal_id = "HML" + str(random.randint(111111, 999999))
            # print("shop:",shop)
            data = {
                "cropId": self.crop_id,
                "name": terminal_id,
                "orgId": shop,
                "tagIds": [],
                "sn": terminal_id
            }
            resp = requests.post(url=add_url, headers=self.headers, data=json.dumps(data))
            print("------------------------------")
            print("添加设备中的crop",self.crop_id)
            print("添加设备中的org", shop)
            print("sn",terminal_id)
            print("添加设备的结果是:",resp.json())

        print("这个设备添加完了-------------------------")


# if __name__ == "__main__":
#         """
#         实现方式1：python 多线程代码，勿删
#         """
#     import_login1 = import_login(user1)
#     import_login2 = import_login(user2)
#     import_login3 = import_login(user3)
#     import_login4 = import_login(user4)
#     print("main函数中的user1:",user1)
#     print("main函数中的user2:", user2)
#     print("main函数中的user3:", user3)
#     print("main函数中的user4:", user4)
#
#
#
#     def thread1():
#         # ****************************前置，拿到login接口中的各种信息 **********************
#         crop_id = import_login1.crop_id()
#         org_id = import_login1.org_id()
#         headers = import_login1.headers()
#         print("main函数中拿到的crop_id", crop_id)
#         print("main函数中拿到的org_id", org_id)
#         print("线程中的user1:", user1)
#
#         # 4个sheet：悸动烧仙草   good   luckin  snow
#         sheet_index =0
#
#         print("main中的sheet_index", sheet_index)
#         add_shop = AddShop(crop_id, org_id, headers, user1,sheet_index)
#
#         _, _, shop_type_ids = add_shop.get_type_branchs()
#
#         add_terminal = AddTerminal(crop_id, org_id, headers, shop_type_ids)
#
#         # ********前置可选：清理所有的终端、清理所有的机构***********
#
#         # add_terminal.clear_terminal()  # 清理列表中所有的终端
#         # time.sleep(0.5)
#         # add_terminal_ids = add_terminal.get_terminal_list()
#         # if not add_terminal_ids:
#         #     add_terminal.clear_terminal()
#         #     print("设备没有清理干净，进行二次清理")
#         # print(" 清理全部设备成功")
#         # time.sleep(0.5)
#         #
#         # # 清理所有的机构
#         # add_shop.clear_all_org()
#         # time.sleep(2)
#         #
#         # org_ids,_,  _= add_shop.get_type_branchs()
#         # if org_ids is not []:
#         #     add_shop.clear_all_org()
#         #     print("机构没有清理干净，进行二次清理")
#         # print(" 清理全部机构成功")
#
#         # ****************************第一步：添加所有的分支***************
#         add_shop.add_each_branch()  # 添加分支
#         time.sleep(0.5)
#
#         # *****************************第二步：添加所有的门店**************
#         add_shop.add_each_shop()  # 添加门店
#
#         # ****************************第三步：为每个门店添加4个设备**********
#         _, _, shop_type_ids = add_shop.get_type_branchs()
#         add_terminal.add_terminal_for_each_shop()
#         print("添加设备成功1")
#
#     def thread2():
#         # ****************************前置，拿到login接口中的各种信息 **********************
#         crop_id = import_login2.crop_id()
#         org_id = import_login2.org_id()
#         headers = import_login2.headers()
#         print("main函数中拿到的crop_id", crop_id)
#         print("main函数中拿到的org_id", org_id)
#         print("线程中的user2:", user2)
#
#
#         # 4个sheet：悸动烧仙草   good   luckin  snow
#         sheet_index =1
#
#         print("main中的sheet_index", sheet_index)
#
#         add_shop = AddShop(crop_id, org_id, headers, user2,sheet_index)
#
#         _, _, shop_type_ids = add_shop.get_type_branchs()
#
#         add_terminal = AddTerminal(crop_id, org_id, headers, shop_type_ids)
#
#         # # # ********前置可选：清理所有的终端、清理所有的机构***********
#         #
#         # add_terminal.clear_terminal()  # 清理列表中所有的终端
#         # time.sleep(0.5)
#         # add_terminal_ids = add_terminal.get_terminal_list()
#         # if not add_terminal_ids:
#         #     add_terminal.clear_terminal()
#         #     print("设备没有清理干净，进行二次清理")
#         # print(" 清理全部设备成功")
#         # time.sleep(0.5)
#         #
#         # # 清理所有的机构
#         # add_shop.clear_all_org()
#         # time.sleep(2)
#         #
#         # org_ids, _, _ = add_shop.get_type_branchs()
#         # if org_ids is not []:
#         #     add_shop.clear_all_org()
#         #     print("机构没有清理干净，进行二次清理")
#         # print(" 清理全部机构成功")
#         # #
#         # ****************************第一步：添加所有的分支***************
#         add_shop.add_each_branch()  # 添加分支
#         time.sleep(0.5)
#
#         # *****************************第二步：添加所有的门店**************
#         add_shop.add_each_shop()  # 添加门店
#
#         # ****************************第三步：为每个门店添加4个设备**********
#         _, _, shop_type_ids = add_shop.get_type_branchs()
#         add_terminal.add_terminal_for_each_shop()
#         print("添加设备成功2")
#
#     def thread3():
#         # ****************************前置，拿到login接口中的各种信息 **********************
#         crop_id = import_login3.crop_id()
#         org_id = import_login3.org_id()
#         headers = import_login3.headers()
#         print("main函数中拿到的crop_id", crop_id)
#         print("main函数中拿到的org_id", org_id)
#         print("线程中的user3:", user3)
#
#
#         # 4个sheet：悸动烧仙草   good   luckin  snow
#         sheet_index =2
#
#         print("main中的sheet_index", sheet_index)
#
#         add_shop = AddShop(crop_id, org_id, headers, user3,sheet_index)
#
#         _, _, shop_type_ids = add_shop.get_type_branchs()
#
#         add_terminal = AddTerminal(crop_id, org_id, headers, shop_type_ids)
#
#         # # ********前置可选：清理所有的终端、清理所有的机构***********
#         #
#         # add_terminal.clear_terminal()  # 清理列表中所有的终端
#         # time.sleep(2)
#         # add_terminal_ids = add_terminal.get_terminal_list()
#         # if not add_terminal_ids:
#         #     add_terminal.clear_terminal()
#         #     print("设备没有清理干净，进行二次清理")
#         # print(" 清理全部设备成功")
#         # time.sleep(0.5)
#         #
#         # # 清理所有的机构
#         # add_shop.clear_all_org()
#         # time.sleep(2)
#         #
#         # org_ids, _, _ = add_shop.get_type_branchs()
#         # if org_ids is not []:
#         #     add_shop.clear_all_org()
#         #     print("机构没有清理干净，进行二次清理")
#         # print(" 清理全部机构成功")
#
#         # ****************************第一步：添加所有的分支***************
#         add_shop.add_each_branch()  # 添加分支
#         time.sleep(0.5)
#
#         # *****************************第二步：添加所有的门店**************
#         add_shop.add_each_shop()  # 添加门店
#
#         #  ****************************第三步：为每个门店添加4个设备**********
#         _, _, shop_type_ids = add_shop.get_type_branchs()
#
#         add_terminal.add_terminal_for_each_shop()
#         print("添加设备成功3")
#
#     def thread4():
#         # ****************************前置，拿到login接口中的各种信息 **********************
#         crop_id = import_login4.crop_id()
#         org_id = import_login4.org_id()
#         headers = import_login4.headers()
#         print("main函数中拿到的crop_id",crop_id)
#         print("main函数中拿到的org_id", org_id)
#         print("线程中的user4:", user4)
#
#
#         # 4个sheet：悸动烧仙草   good   luckin  snow
#         sheet_index =3
#
#         print("main中的sheet_index", sheet_index)
#
#         add_shop = AddShop(crop_id, org_id,headers,user4,sheet_index)
#
#         _, _, shop_type_ids = add_shop.get_type_branchs()
#
#         add_terminal = AddTerminal(crop_id, org_id, headers,shop_type_ids)
#
#         # # ********前置可选：清理所有的终端、清理所有的机构***********
#
#         # add_terminal.clear_terminal()  # 清理列表中所有的终端
#         # time.sleep(0.5)
#         # add_terminal_ids= add_terminal.get_terminal_list()
#         # if not add_terminal_ids:
#         #     add_terminal.clear_terminal()
#         #     print("设备没有清理干净，进行二次清理")
#         # print(" 清理全部设备成功")
#         # time.sleep(0.5)
#         # #
#         # # 清理所有的机构
#         # add_shop.clear_all_org()
#         # time.sleep(0.5)
#         #
#         # org_ids, _, _ =add_shop.get_type_branchs()
#         # if org_ids is not []:
#         #     add_shop.clear_all_org()
#         #     print("机构没有清理干净，进行二次清理")
#         # print(" 清理全部机构成功")
#         #
#         # ****************************第一步：添加所有的分支***************
#         add_shop.add_each_branch()  # 添加分支
#         time.sleep(0.5)
#
#         # *****************************第二步：添加所有的门店**************
#         add_shop.add_each_shop()  # 添加门店
#
#         # ****************************第三步：为每个门店添加4个设备**********
#         _, _, shop_type_ids =add_shop.get_type_branchs()
#
#         add_terminal.add_terminal_for_each_shop()
#         print("添加设备成功4")
#
#
#     thread1 = threading.Thread(target=thread1)
#     thread2 = threading.Thread(target=thread2)
#     thread3 = threading.Thread(target=thread3)
#     thread4 = threading.Thread(target=thread4)
#
#     thread1.start()
#     print("线程1已启动")
#     thread2.start()
#     print("线程2已启动")
#     thread3.start()
#     print("线程3已启动")
#     thread4.start()
#     print("线程4已启动")
#
#     thread1.join()
#     thread2.join()
#     thread3.join()
#     thread4.join()


if __name__ == "__main__":
    """
    实现方式2：python线程池代码，勿删
    """

    def worker(user):

        # 4个sheet：悸动烧仙草   good   luckin  snow

        import_login4 = import_login(user)
        print("\nmain函数中当前登录的user:", user)
        # ****************************前置，拿到login接口中的各种信息 **********************
        crop_id = import_login4.crop_id()
        org_id = import_login4.org_id()
        headers = import_login4.headers()
        print("\nmain函数中拿到的crop_id", crop_id)
        print("\nmain函数中拿到的org_id", org_id)
        print("\n线程中的user:", user)
        sheet_index = users.index(user)


        print("main中的sheet_index", sheet_index)

        add_shop = AddShop(crop_id, org_id, headers, user4, sheet_index)

        _, _, shop_type_ids = add_shop.get_type_branchs()
        print("work中的org-id",shop_type_ids)


        add_terminal = AddTerminal(crop_id, org_id, headers, shop_type_ids)

        # # ********前置可选：清理所有的终端、清理所有的机构***********

        add_terminal.clear_terminal()  # 清理列表中所有的终端
        time.sleep(0.5)
        add_terminal_ids= add_terminal.get_terminal_list()
        if not add_terminal_ids:
            add_terminal.clear_terminal()
            print("设备没有清理干净，进行二次清理")
        print(" 清理全部设备成功")
        time.sleep(0.5)
        #
        # 清理所有的机构
        add_shop.clear_all_org()
        time.sleep(0.5)

        org_ids, _, _ =add_shop.get_type_branchs()
        if org_ids is not []:
            add_shop.clear_all_org()
            print("机构没有清理干净，进行二次清理")
        print(" 清理全部机构成功")

        # ****************************第一步：添加所有的分支***************
        add_shop.add_each_branch()  # 添加分支
        print("添加所有分支branch OK")
        time.sleep(0.5)

        # *****************************第二步：添加所有的门店**************
        add_shop.add_each_shop()  # 添加门店
        print("添加所有SHOP OK")

        # ****************************第三步：为每个门店添加4个设备**********
        _, _, shop_type_ids = add_shop.get_type_branchs()

        # for i in range(1,3):

        add_terminal = AddTerminal(crop_id, org_id, headers, shop_type_ids)
        add_terminal.add_terminal_for_each_shop()
        print("当前用户"+user+"添加全部设备成功")

    #
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # for i in range(3):
        #     executor.submit(worker,i)
        for user in users:
            executor.submit(worker, user)

    # 单线程，用来调试的,可保留
    # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     # for i in range(3):
    #     #     executor.submit(worker,i)
    #     user = users[0]
    #     executor.submit(worker, user)

