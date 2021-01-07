# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :test_archivequery
# @Date     :2020/12/25 15:06
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import json
from config import BASE_DIR
import unittest
import time
from common.utils import DriverUtil
from page.archive_page import ArchiveProxy
from page.archivequery_page import ArchiveQueryProxy
from page.login_page import LoginProxy
from page.menu_page import MenuProxy
from page.archivedetails_page import ArchiveDetailsProxy
from parameterized import parameterized

def build_archive1_data():
    with open( BASE_DIR +'/data/archive_data.json', encoding='utf-8' ) as f:
        data = json.load( f )
        data_list = []
        for item in data.values():
            data_list.append(tuple(item.values()))
        print(data_list)
    return data_list


class ArchiveQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # cls.loginproxy = LoginProxy()
        # cls.loginproxy.login('qpadmin', 'a123456', '6666')
        cls.menu = MenuProxy(["账户管理", "档案管理", "档案查询"])
        time.sleep(2)
        cls.menu.click_menu()
        cls.aqproxy = ArchiveQueryProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    @parameterized.expand(build_archive1_data())
    def test_queryarchive(self, key_name, expect, column_name):
        self.aqproxy.queryarchive(key_name)
        time.sleep(2)
        # 无可显示数据！
        self.assertIn(expect, self.aqproxy.viewresult(column_name))

if __name__ == '__main__':
    unittest.main()

