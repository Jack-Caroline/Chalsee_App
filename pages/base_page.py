#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/20 16:24

import os
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from common.handle_log import log
from common.handle_path import ERROR_IMAGES_DIR


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_visibility_of_ele_located(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """
        等待元素可见
        :param loc: 元素定位
        :param loc_desc: 元素说明
        :param timeout: 等待时间
        :param poll_time: 等待轮询时间间隔
        :return:元素
        """
        pass

    def wait_presence_ele(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """
        等待元素可加载
        :param loc: 元素定位
        :param loc_desc: 元素说明
        :param timeout: 等待时间
        :param poll_time: 等待轮询时间间隔
        :return: 元素
        """
        pass

    def get_element(self):
        """
        查找元素
        :return:
        """
        pass

    def click_element(self):
        """
        点击元素
        :return:
        """
        pass

    def input_send_keys(self):
        """
        输入操作
        :return:
        """
        pass

    def get_element_text(self):
        """
        获取元素文本值
        :return:
        """
        pass

    def get_element_attr(self):
        """
        获取元素属性值
        :return:
        """
        pass

    def page_save_screenshot(self):
        """
        截图
        :return:
        """
        pass
