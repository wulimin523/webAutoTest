# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :read_excel
# @Date     :2020/12/31 18:07
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import xlrd
import config

data = xlrd.open_workbook_xls('E:\\job\\CRM系统\\data\\CRM系统_测试用例.xlsx')
table = data.sheets()[0]

rows = table.nrows()
cols = table.ncols()

print(rows)
