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

import pytest

import config

from page.login_page import LoginProxy
from common.utils import DriverUtil
from parameterized import parameterized


def build_login_data():
    with open( '../../data/login_data.json', encoding='utf-8' ) as f:
        data = json.load(f)
        data_list = list()
        for k, v in data.items():
            data_list.append((v.get('username'),
                              v.get('password'),
                              v.get('checkcode')))
    return data_list

def build_login_rightdata():
    with open(config.BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()
        for k, v in data.items():
            if k == 'right_data':
                data_list.append((v.get('username'),
                              v.get('password'),
                              v.get('checkcode')))
    return data_list

def build_menu_data():
    with open(config.BASE_DIR + '/data/menu_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()
        for k, v in data.items():
            data_list.append(v)
    return data_list


class TestLogin():
    @classmethod
    def setup_class(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        cls.login_proxy = LoginProxy()
        # cls.menu_proxy = MenuProxy(['参数管理', '卡类别设置'])

    @classmethod
    def teardown_class(cls) -> None:
        # DriverUtil.quit_driver()
        pass

    # @parameterized.expand(build_login_data())
    # def test_login(self, username, password, checkcode):
    #     print(username, password, checkcode)
    #     self.login_proxy.login(username, password, checkcode)
    #     try:
    #         title = self.driver.title
    #         self.assertEqual('11一卡通管理平台',title)
    #     except AssertionError as e:
    #         # now_time = time.strftime("%Y%m%d_%H%M%S")
    #         # self.driver.get_screenshot_as_file(filename=(config.BASE_DIR + "/screenshot/bug_{}_{}.png").format(now_time, title))
    #         # basepage = BasePage()
    #         save_webImgs(model='登录模块')
    #         raise e
    @pytest.mark.run(order=2)
    @parameterized.expand( build_login_rightdata())
    def test_login_right(self, username, password, checkcode):
        print( username, password, checkcode )
        self.login_proxy.login( username, password, checkcode )


