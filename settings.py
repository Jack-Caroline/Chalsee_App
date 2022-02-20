#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/20 17:23
LOGGING = dict(
    level="DEBUG",
    fh_level="DEBUG",
    sh_level="ERROR",
    log_name="logging.log"
)

# app的启动参数配置
DESIRED_CAP = {
    "platformName": "android",  # platformName：设备的操作系统
    "platformVersion": "7.1.2",  # platformVersion：系统的版本
    "automationName": "UiAutomator2",  # automationName：设备系统的自动化测试框架
    "deviceName": "HUAWEIP30",  # deviceName：设备名字
    "appPackage": "com.honghengisp",  # appPackage：操作的app包名
    "appActivity": "com.honghengisp.MainActivity"  # appActivity：app的启动页
}

# appium 的服务器地址
COMMAND_EXECUTOR = 'http://127.0.0.1:4723/wd/hub'