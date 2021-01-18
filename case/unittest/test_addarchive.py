# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :test_addarchive
# @Date     :2020/12/25 15:06
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import unittest
import time
from common.utils import DriverUtil
from page.archive_page import ArchiveProxy
from page.login_page import LoginProxy
from page.menu_page import MenuProxy
from page.archivedetails_page import ArchiveDetailsProxy
from parameterized import parameterized

def build_archive_data():
    data_list = list()
    list0 = ['1','2']
    for i in list0:
        dict = ['自动化'+i,
                '1861270152'+i,
                '身份证',
                '20201225'+i,
                '图书馆',
                '员工']
        data_list.append(dict)
    return data_list


class AddArchive(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.menu = MenuProxy( ["账户管理", "档案管理", "档案新增"] )
        cls.menu.click_menu()
        # cls.loginproxy = LoginProxy()
        cls.archiveproxy = ArchiveProxy()
        cls.archivedetailsproxy = ArchiveDetailsProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def test_addarchive1(self):
        time.sleep(2)
        self.archiveproxy.addarchive()

    @parameterized.expand(build_archive_data())
    def test_addarchive2(self, name, tel, certtype, certno, dept, duty):
    # def test_addarchive2(self):
        time.sleep(1)
        # self.archivedetailsproxy.goto_savearchive('自动姓名', '18612701526', '护照', '20201225001','局机关', '员工')
        self.archivedetailsproxy.goto_savearchive(name, tel, certtype, certno, dept, duty)

if __name__ == '__main__':
    unittest.main()

