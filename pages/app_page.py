#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/20 16:24

from appium.webdriver.webdriver import WebDriver
from pages.base_page import BasePage
from time import sleep
from common.handle_log import log


class AppPage(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_devive_size(self):
        """
        获取设备大小
        :return:
        """
        pass

    def swipe_by_direction(self):
        """
        根据方向滑动屏幕 80%
        :return:
        """
        pass

    def get_toast_msg(self):
        """
        toast 处理, xpath - 等待存在
        :return:
        """
        pass

    def switch_to_webview(self):
        """
        或者应用，识别-开调试-获取所有的 contexts - 切换到 webview contexts 里-html自动化
        :return:
        """
        pass

    # 微信小程序
    # 识别-开调试-获取小程序所在的进程名称
    # 启动参数配置-微信操作进入小程序页面当中-切换操作-获取所有的窗口-进入到小程序所在的窗口
