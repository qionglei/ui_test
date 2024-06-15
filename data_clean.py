import pymysql.cursors

import traceback

import yaml

from common.set_up_media_list import MediaList
from common.set_up_org import OrgList
from common.set_up_play_bill import PlayBill
from common.set_up_program_list import ProgramList
from common.set_up_terminal_list import Terminal_List
# from config.log_config import logger
# from config.log_config import logger


host = 'rm-wz9vq722u8axcvo06oo.mysql.rds.aliyuncs.com'


def sql_execute():
    # 建立与MySQL的连接
    connection = pymysql.connect(host=host, port=3391, user='hkc_cv_user', password='Hkc285$$', database='hkc_cv')
    cursor = connection.cursor()

    try:
        connection.begin()
        # 定义要执行的SQL语句列表
        sql_statements = [
            "SELECT * FROM user_base WHERE phone = '13715297700'",
            "SELECT * FROM user_ext_info WHERE user_id = '1751805419424722946'",
            "DELETE FROM play_bill WHERE crop_id = '1751805517940535298'",
            "DELETE FROM `folder` WHERE crop_id = '1751805517940535298'",
            "DELETE FROM program_basic WHERE crop_id = '1751805517940535298'",
            "DELETE FROM media WHERE crop_id = '1751805517940535298'",
            "DELETE FROM terminal WHERE crop_id = '1751805517940535298'",
            "DELETE FROM busi_invoice_header WHERE crop_id = '1751805517940535298'",
            "DELETE FROM `busi_license` WHERE crop_id = '1751805517940535298'",
            "DELETE FROM `busi_order` WHERE crop_id = '1751805517940535298'",
            "DELETE FROM `busi_invoice` WHERE crop_id = '1751805517940535298'",
            "DELETE FROM `terminal` WHERE sn LIKE '824022000300645'",
            "delete from tag where crop_id ='1751805517940535298'"
        ]

        # 遍历SQL语句列表，依次执行每条语句
        for statement in sql_statements:
            cursor.execute(statement)

        # 提交事务
        connection.commit()
    except Exception as e:
        print("Error executing SQL statements: ", str(e))
    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()
        print("数据清理已完成")


def api_clear_data():
    """
    调用接口，进行数据清理工作，从而恢复环境
    """

    try:
        # 尝试导入可能产生循环导入的模块

        # 1、清理节目单
        play_bill_list = PlayBill()
        play_bill_list.get_play_bill_ids()
        play_bill_list.clear_play_bill()

        # 2、清理节目列表、节目列表下的文件夹
        programlist = ProgramList()
        programlist.get_program_list_ids()
        programlist.delete_all_program_folders()
        programlist.delete_all_program()

        # 4、清理素材列表、素材列表下的文件夹
        media_list = MediaList()
        media_list.delete_all_folder()
        media_list.delete_all_media()

        # 5、清理机器
        list_t = Terminal_List()
        ids = list_t.get_terminal_list()
        list_t.delete_terminal(ids)

        # 6、清理组织架构，且保留一个门店
        org_list = OrgList()
        org_list.clear_all_org()
        org_list.add_branch()
        print("添加门店成功")


    except Exception as e:
        traceback.print_exc()


def clear_terminal():

    conf_path = r"D:\git\ui_test\config.yaml"
    with open(conf_path) as f:
        environment_conf = yaml.load(f.read(), Loader=yaml.SafeLoader)
    real_terminal_id = environment_conf["test_terminal_id"]
    # real_terminal_name = environment_conf["test_terminal_name"]
    # 建立与MySQL的连接
    connection = pymysql.connect(host=host, port=3391, user='hkc_cv_user', password='Hkc285$$', database='hkc_cv')
    cursor = connection.cursor()

    try:
        connection.begin()
        # 定义要执行的SQL语句列表
        sql_statements = [
            f"DELETE FROM terminal WHERE sn = '{real_terminal_id}",
            "DELETE FROM terminal WHERE crop_id = '1751805517940535298'",]

        # 遍历SQL语句列表，依次执行每条语句
        for statement in sql_statements:
            cursor.execute(statement)

        # 提交事务
        connection.commit()
    except Exception as e:
        print("Error executing SQL statements: ", str(e))
    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()
        # print("终端sn清理已完成")

#
# if __name__ == "__main__":
#     api_clear_data()
