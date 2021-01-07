# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :webAutoTest
# @File     :basepage
# @Date     :2020/12/21 18:31
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from common.utils import DriverUtil
import logging
import time
import config


class BasePage( object ):
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element_func(self, location):
        '''元素定位方法'''
        return self.driver.find_element( *location )

    # 获取属性值
    def get_Element_Attribute(self, location, name, model=None):
        # 先查找元素在去获取属性值
        ele = self.find_Element( location, model )
        # 获取元素属性值
        try:
            ele_attribute = ele.get_attribute( name )
            return ele_attribute
        except:
            raise

    # 等待元素可见
    def wait_eleVisible(self, loc, timeout=20, poll_frequency=0.5, model=None):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:None
        """
        logging.info( '{} 等待元素可见:{}'.format( model, loc ) )
        try:
            start = time.time()
            WebDriverWait( self.driver, timeout, poll_frequency ).until( EC.visibility_of_element_located( loc ) )
            end = time.time()
            logging.info( '等待时长:%.2f 秒' % (end - start) )
        except:
            logging.exception( '{} 等待元素可见失败:{}'.format( model, loc ) )
            # 截图
            self.save_webImgs( model )
            raise

    # 等待元素不可见
    def wait_eleNoVisible(self, loc, timeout=20, poll_frequency=0.5, model=None):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:None
        """
        logging.info( '{} 等待元素不可见:{}'.format( model, loc ) )
        try:
            start = time.time()
            WebDriverWait( self.driver, timeout, poll_frequency ).until_not(
                EC.visibility_of_element_located( loc ) )
            end = time.time()
            logging.info( '等待时长:%.2f 秒' % (end - start) )
        except:
            logging.exception( '{} 等待元素不可见失败:{}'.format( model, loc ) )
            # 截图
            self.save_webImgs( model )
            raise

    # 查找一个元素element
    def find_Element(self, loc, model=None):
        logging.info( '{} 查找元素 {}'.format( model, loc ) )
        try:
            return self.driver.find_element( *loc )
        except:
            logging.exception( '查找元素失败.' )
            # 截图
            self.save_webImgs( model )
            raise

    # 查找元素elements
    def find_Elements(self, loc, model=None):
        logging.info( '{} 查找元素 {}'.format( model, loc ) )
        try:
            return self.driver.find_element( *loc )
        except:
            logging.exception( '查找元素失败.' )
            # 截图
            self.save_webImgs( model )
            raise

    # 输入操作
    def input_Text(self, loc, text, model=None):
        # 查找元素
        ele = self.find_Element( loc, model )
        # 输入操作
        logging.info( '{} 在元素 {} 中输入文本: {}'.format( model, loc, text ) )
        try:
            ele.send_keys( text )
        except:
            logging.exception( '输入操作失败' )
            # 截图
            self.save_webImgs( model )
            raise

    # 清除操作
    def clear_Input_Text(self, loc, model=None):
        ele = self.find_Element( loc, model )
        # 清除操作
        logging.info( '{} 在元素 {} 中清除'.format( model, loc ) )
        try:
            ele.clear()
        except:
            logging.exception( '清除操作失败' )
            # 截图
            self.save_webImgs( model )
            raise

    # 点击操作
    def click_Element(self, loc, model=None):
        # 先查找元素在点击
        ele = self.find_Element( loc, model )
        # 点击操作
        logging.info( '{} 在元素 {} 中点击'.format( model, loc ) )
        try:
            ele.click()
        except:
            logging.exception( '点击操作失败' )
            # 截图
            self.save_webImgs( model )
            raise

    # 获取文本内容
    def get_Text(self, loc, model=None):
        # 先查找元素在获取文本内容
        ele = self.find_Element( loc, model )
        # 获取文本
        logging.info( '{} 在元素 {} 中获取文本'.format( model, loc ) )
        try:
            text = ele.text
            logging.info( '{} 元素 {} 的文本内容为 {}'.format( model, loc, text ) )
            return text
        except:
            logging.exception( '获取元素 {} 的文本内容失败,报错信息如下:'.format( loc ) )
            # 截图
            self.save_webImgs( model )
            raise

    # 获取属性值
    def get_Element_Attribute(self, loc, name, model=None):
        # 先查找元素在去获取属性值
        ele = self.find_Element( loc, model )
        # 获取元素属性值
        logging.info( '{} 在元素 {} 中获取属性值'.format( model, loc ) )
        try:
            ele_attribute = ele.get_attribute( name )
            logging.info( '{} 元素 {} 的文本内容为 {}'.format( model, loc, ele_attribute ) )
            return ele_attribute
        except:
            logging.exception( '获取元素 {} 的属性值失败,报错信息如下:'.format( loc ) )
            self.save_webImgs( model )
            raise

    # iframe 切换
    def switch_iframe(self, frame_refer, timeout=20, poll_frequency=0.5, model=None):
        # 等待 iframe 存在
        logging.info( 'iframe 切换操作:' )
        try:
            # 切换 == index\name\id\WebElement
            WebDriverWait( self.driver, timeout, poll_frequency ).until(
                EC.frame_to_be_available_and_switch_to_it( frame_refer ) )
            time.sleep( 0.5 )
            logging.info( '切换成功' )
        except:
            logging.exception( 'iframe 切换失败!!!' )
            # 截图
            self.save_webImgs( model )
            raise

    # 窗口切换 = 如果是切换到新窗口,new. 如果是回到默认的窗口,default
    def switch_window(self, name, cur_handles=None, timeout=20, poll_frequency=0.5, model=None):
        """
        调用之前要获取window_handles
        :param name: new 代表最新打开的一个窗口. default 代表第一个窗口. 其他的值表示为窗口的 handles
        :param cur_handles:
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:
        """
        try:
            if name == 'new':
                if cur_handles is not None:
                    logging.info( '切换到最新打开的窗口' )
                    WebDriverWait( self.driver, timeout, poll_frequency ).until(
                        EC.new_window_is_opened( cur_handles ) )
                    window_handles = self.driver.window_handles
                    self.driver.swich_to.window( window_handles[-1] )
                else:
                    logging.exception( '切换失败,没有要切换窗口的信息!!!' )
                    self.save_webImgs( model )
                    raise
            elif name == 'default':
                logging.info( '切换到默认页面' )
                self.driver.switch_to.default()
            else:
                logging.info( '切换到为 handles 的窗口' )
                self.driver.swich_to.window( name )
        except:
            logging.exception( '切换窗口失败!!!' )
            # 截图
            self.save_webImgs( model )
            raise

    # 截图
    def save_webImgs(self, model=None):
        # filepath = 指图片保存目录/model(页面功能名称)_当前时间到秒.png
        # 当前时间
        now_time = time.strftime( "%Y%m%d_%H%M%S" )
        # 路径
        filePath = '{}/{}_{}.png'.format( config.BASE_DIR + '/screenshot', model, now_time )
        print( filePath )
        try:
            self.driver.get_screenshot_as_file( filePath )
            logging.info( '截屏成功,图片路径为{}'.format( filePath ) )
        except:
            logging.exception( '截屏失败!' )


class BaseHandle( object ):
    '''操作层的基类'''

    def input_text(self, element, text):
        element.clear()
        element.send_keys( text )

    def clear_text(self, element, text):
        element.clear()
