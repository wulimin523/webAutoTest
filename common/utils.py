# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :utils
# @Date     :2020/12/23 10:24
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
"""
全局工具类
"""
from selenium import webdriver
from time import sleep
import time
import config
import logging


def save_webImgs(model=None):
    # filepath = 指图片保存目录/model(页面功能名称)_当前时间到秒.png
    # 当前时间
    now_time = time.strftime( "%Y%m%d_%H%M%S" )
    # 路径
    filePath = '{}/{}_{}.png'.format( config.BASE_DIR + '/screenshot', model, now_time )
    print( filePath )
    try:
        DriverUtil.get_driver().get_screenshot_as_file( filePath )
        logging.info( '截屏成功,图片路径为{}'.format( filePath ) )
    except:
        logging.exception('截屏失败!')

class DriverUtil(object):
    '''浏览器驱动类'''

    _driver = None

    _auto_quit = True

    @classmethod
    def get_driver(self):
        if self._driver is None:
            self._driver = webdriver.Firefox()
            self._driver.get("https://shqp.dev/WEBICM/")
            self._driver.maximize_window()
            self._driver.implicitly_wait(10)
        return self._driver

    @classmethod
    def quit_driver(self):
        if self._driver and self._auto_quit:
            sleep(2)
            self._driver.quit()
            self._driver = None

    @classmethod
    def change_auto_quit(self, auto):
        self._auto_quit = auto
