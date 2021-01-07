# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :archivequery_page
# @Date     :2020/12/25 14:56
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from multiprocessing.managers import BaseProxy

from base.base_page import BasePage, BaseHandle
from selenium.webdriver.common.by import By

class ArchiveQueryPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

        self.query_btn = (By.CSS_SELECTOR, '.btn-search')
        self.name = (By.CSS_SELECTOR, '#ACCNAME')
        self.retult_head = (By.CSS_SELECTOR, '.dataTables_scrollHeadInner > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1)')
        self.result = (By.CSS_SELECTOR, '#datatable_col_reorder > tbody:nth-child(2)')

    def find_query_btn(self):
        return self.find_element_func(self.query_btn)

    def find_name(self):
        return self.find_element_func(self.name)

    def get_result(self, name):
        self.thead = self.find_element_func(self.retult_head)
        self.ths = self.thead.find_elements_by_tag_name('th')
        index = 0
        for th in self.ths:
            if(name == th.text):
                break
            index += 1

        print(self.find_element_func(self.result))
        list = []
        self.tbody = self.find_element_func(self.result)#这个表格
        self.rows = self.tbody.find_elements_by_tag_name('tr')#所有行
        for row in self.rows:
            units = row.find_elements_by_tag_name('td')#所有列
            if len(units) == 1:
                break
            list.append(units[index].text)
        return list


class ArchiveQueryHandle(BaseHandle):
    def __init__(self):
        self.archivequerypage = ArchiveQueryPage()

    def input_name(self, name):
        self.input_text(self.archivequerypage.find_name(), name)

    def click_query_btn(self):
        self.archivequerypage.find_query_btn().click()

    def get_result(self, name):
        return self.archivequerypage.get_result(name)

class ArchiveQueryProxy(BaseProxy):
    def __init__(self):
        self.aqhandle = ArchiveQueryHandle()

    def queryarchive(self, name):
        self.aqhandle.input_name(name)
        self.aqhandle.click_query_btn()

    def viewresult(self, name):
        return self.aqhandle.get_result( name)