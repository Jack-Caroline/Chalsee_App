#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/18 10:07
from appium.webdriver import Remote

desired_cap = {
    "platformName": "android",  # 操作系统
    "platformVersion": "7.1.2",  # 系统版本
    "automationName": "UiAutomator2",  # 设备系统的自动化测试框架
    "deviceName": "HUAWEIP30",  # 设备名称
    "appPackage": "com.honghengisp",  # 操作的App的包名
    "appActivity": "com.honghengisp.mainactivity",  # app的启动页
    "moReset": "True"  # 是否保存APP数据，默认每次访问后会清空上一次的数据
}

# 跟appium建立连接，然后再把启动参数发过去。
driver = Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_cap)
