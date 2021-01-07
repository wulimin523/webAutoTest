# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :mock_test
# @Date     :2021/1/4 11:01
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import unittest
from unittest.mock import Mock


def add(a, b):
    pass

class MockTest(unittest.TestCase):


    def test_add(self):
        add = Mock(return_value=10)
        retult = add(1, 2)
        print(retult)
    # 扩展 模拟抛出异常
    def test_error(self):
        add = Mock(return_value=NameError("对不起，文件没找到"))
        result = add(1, 2)
        print(result)

if __name__ == '__main__':
    unittest.main()