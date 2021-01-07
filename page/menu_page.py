# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :menu_page
# @Date     :2020/12/25 10:44
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from multiprocessing.managers import BaseProxy

from base.base_page import BasePage, BaseHandle
from selenium.webdriver.common.by import By
from time import sleep


class MenuPage(BasePage):
    def __init__(self, menus):
        BasePage.__init__(self)
        self.menus = menus
        self.menu_level_1 = (By.XPATH, f"/html/body/aside/span/nav/ul/li[@title='{menus[0]}']")
        self.menu_level_2 = (
        By.XPATH, f"/html/body/aside/span/nav/ul/li[@title='{menus[0]}']/ul/li[@title='{menus[1]}']/a")
        if (len(self.menus) > 2):
            self.menu_level_3 = (By.XPATH,
                                 f"/html/body/aside/span/nav/ul/li[@title='{menus[0]}']/ul/li[@title='{menus[1]}']/ul/li[@title='{menus[2]}']")

    def find_first_menu(self):
        return self.find_element_func(self.menu_level_1)

    def find_second_menu(self):
        return self.find_element_func(self.menu_level_2)

    def find_third_menu(self):
        return self.find_element_func(self.menu_level_3)

class MenuHandle(BaseHandle):
    def __init__(self, menus):
        self.menupage = MenuPage(menus)

    def click_first_menu(self):
        if self.menupage.find_first_menu().get_attribute('class').find('open') == -1:
            self.menupage.find_first_menu().click()

    def click_second_menu(self):
        if self.menupage.find_second_menu().get_attribute('class').find('open') == -1:
            self.menupage.find_second_menu().click()

    def click_third_menu(self):
        self.menupage.find_third_menu().click()

class MenuProxy(BaseProxy):
    def __init__(self, menus):
        self.menuhandle = MenuHandle(menus)
        self.menus = menus

    def click_menu(self):
        self.menuhandle.click_first_menu()
        sleep(2)
        self.menuhandle.click_second_menu()
        if len(self.menus) > 2:
            self.menuhandle.click_third_menu()