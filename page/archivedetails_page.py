# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :archivedetails_page
# @Date     :2020/12/25 15:22
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from multiprocessing.managers import BaseProxy

from base.base_page import BasePage, BaseHandle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class ArchiveDetailsPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

        self.name = (By.CSS_SELECTOR, 'div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
        self.tel = (By.CSS_SELECTOR, '.isPhone')
        self.certtype = (By.CSS_SELECTOR, 'div.form-group:nth-child(2) > div:nth-child(4) > select:nth-child(1)')
        self.certno = (By.CSS_SELECTOR, '#certNoInput')
        self.dept = (By.CSS_SELECTOR, '#view_DEPTID')
        self.dept0 = (By.XPATH, '/html/body/div[9]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img')
        self.duty = (By.CSS_SELECTOR, 'div.form-group:nth-child(5) > div:nth-child(4) > select:nth-child(1)')
        self.save_btn = (By.CSS_SELECTOR, '#submit')

    def find_name(self):
        return self.find_element_func(self.name)
    def find_tel(self):
        return self.find_element_func(self.tel)
    def find_certtype(self):
        return self.find_element_func(self.certtype)
    def find_certno(self):
        return self.find_element_func(self.certno)
    def find_dept(self):
        return self.find_element_func(self.dept)
    def find_dept0(self):
        return self.find_element_func(self.dept0)
    def find_dept1(self, text):
        return self.find_element_func((By.XPATH, "//span[contains(text(),'{}')]".format(text)))
    def find_duty(self):
        return self.find_element_func(self.duty)
    def find_save_btn(self):
        return self.find_element_func(self.save_btn)

class ArchiveDetailsHandle(BaseHandle):
    def __init__(self):
        self.archivedetailspage = ArchiveDetailsPage()

    def input_name(self, text):
        self.input_text(self.archivedetailspage.find_name(), text)
    def input_tel(self, text):
        self.input_text(self.archivedetailspage.find_tel(), text)
    def input_certtype(self, text):
        Select(self.archivedetailspage.find_certtype()).select_by_visible_text(text)
    def input_certno(self, text):
        self.input_text(self.archivedetailspage.find_certno(), text)
    def input_dept(self, text):
        print('-----------',self.archivedetailspage.find_dept().get_attribute('value'),text)
        if self.archivedetailspage.find_dept().get_attribute('value') != text:
            self.archivedetailspage.find_dept().click()
            sleep(2)
            if self.archivedetailspage.find_dept0().is_displayed():
                self.archivedetailspage.find_dept0().click()
            sleep(5)
            if self.archivedetailspage.find_dept1(text).is_displayed():
                self.archivedetailspage.find_dept1(text).click()

    def input_duty(self, text):
        Select(self.archivedetailspage.find_duty()).select_by_visible_text(text)

    def goto_save(self):
        self.archivedetailspage.find_save_btn().click()

class ArchiveDetailsProxy(BaseProxy):
    def __init__(self):
        self.archivedetailshandle = ArchiveDetailsHandle()

    def goto_savearchive(self, name, tel, certtype, certno, dept, duty):
        self.archivedetailshandle.input_name(name)
        self.archivedetailshandle.input_tel(tel)
        self.archivedetailshandle.input_certtype(certtype)
        self.archivedetailshandle.input_certno(certno)
        self.archivedetailshandle.input_dept(dept)
        self.archivedetailshandle.input_duty(duty)
        self.archivedetailshandle.goto_save()
