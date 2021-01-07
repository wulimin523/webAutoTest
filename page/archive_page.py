# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :archive_page
# @Date     :2020/12/25 14:56
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from multiprocessing.managers import BaseProxy

from base.base_page import BasePage, BaseHandle
from selenium.webdriver.common.by import By

class ArchivePage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

        self.add_btn = (By.CSS_SELECTOR, 'a.btn:nth-child(1)')
        self.submit_btn = (By.CSS_SELECTOR, 'input.btn:nth-child(3)')

    def find_add_btn(self):
        return self.find_element_func(self.add_btn)

    def find_submit_btn(self):
        return self.find_element_func(self.submit_btn)

class ArchiveHandle(BaseHandle):
    def __init__(self):
        self.archivepage = ArchivePage()

    def click_add_btn(self):
        self.archivepage.find_add_btn().click()

    def click_submit_btn(self):
        self.archivepage.find_submit_btn().click()

class ArchiveProxy(BaseProxy):
    def __init__(self):
        self.archivehandle = ArchiveHandle()

    def addarchive(self):
        self.archivehandle.click_add_btn()

    def submitarchive(self):
        self.archivehandle.click_submit_btn()