# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :test_loaddata
# @Date     :2020/12/23 13:11
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""

import json

with open( '../../data/login_data.json', encoding='utf-8' ) as f:
    data = json.load(f)
    data_list = list()
    for k,v in data.items():
        data_list.append((v.get('username'),
                    v.get('password'),
                    v.get('checkcode')))
    print(data_list)

with open( '../../data/menu_data.json', encoding='utf-8' ) as f:
    data = json.load(f)
    data_list = list()
    # print(data)
    for k, v in data.items():
        print(v)

with open( '../../data/archive_data.json', encoding='utf-8' ) as f:
    data = json.load(f)
    data_list = list()
    for k, v in data.items():
        print(v)