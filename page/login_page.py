# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :login_page
# @Date     :2020/12/23 10:37
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from base.base_page import BasePage,BaseHandle
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    '''登录页--对象库层'''
    def __init__(self):
        BasePage.__init__(self) #获取父类的浏览器对象
        self.username = (By.ID, 'username')
        self.password = (By.ID, 'plainpwd')
        self.checkcode = (By.ID, 'captcha')
        self.loginbtn = (By.ID, 'gologin')

    def find_username(self):
        return self.find_element_func(self.username)

    def find_password(self):
        return self.find_element_func(self.password)

    def find_checkcode(self):
        return self.find_element_func(self.checkcode)

    def find_loginbtn(self):
        return self.find_element_func(self.loginbtn)

class LoginHandle(BaseHandle):
    '''登录页--元素操作层'''
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, text):
        self.input_text(self.login_page.find_username(), text)

    def input_password(self, text):
        self.input_text(self.login_page.find_password(), text)

    def input_checkcode(self, text):
        self.input_text(self.login_page.find_checkcode(), text)

    def click_loginbtn(self):
       self.login_page.find_loginbtn().click()



class LoginProxy(object):
    '''登录页--业务层'''
    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, password, checkcode):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_checkcode(checkcode)
        self.login_handle.click_loginbtn()

