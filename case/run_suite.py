# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :run_suite
# @Date     :2020/12/25 18:50
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import unittest
import config
from case.test_archivequery import ArchiveQuery
from case.test_login import TestLogin
from case.test_menu import TestMenu
from case.test_addarchive import AddArchive
from common.utils import DriverUtil
from HwTestReport import HTMLTestReport


suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMenu))
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(AddArchive))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ArchiveQuery))

DriverUtil.change_auto_quit(False)

# unittest.TextTestRunner().run(suite)

print(config.BASE_DIR+'/report/addarchivereport.html')
with open(config.BASE_DIR+'/report/addarchivereport.html', 'wb') as report:
    runner = HTMLTestReport( stream=report,
                             verbosity=2,
                             title='档案新增自动化测试',
                             description='带饼图，带详情，带截图',
                             tester='吴利民',
                             images=True)
    runner.run(suite)

DriverUtil.change_auto_quit(True)

DriverUtil.quit_driver()
