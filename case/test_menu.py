# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :test_login
# @Date     :2020/12/23 11:02
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import unittest
import json
from time import sleep
from page.login_page import LoginProxy
from common.utils import DriverUtil
from parameterized import parameterized

from page.menu_page import MenuProxy


def build_menu_data():
    with open('../data/menu_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()
        for k, v in data.items():
            data_list.append(v)

        print(data_list)
    return data_list


class TestMenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(1)
        DriverUtil.quit_driver()

    @parameterized.expand(build_menu_data())
    def test_menu(self, *menus):
        sleep(2)
        self.menu_proxy = MenuProxy(menus)
        self.menu_proxy.click_menu()


if __name__ == '__main__':
    unittest.main()

