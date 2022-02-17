#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/17 12:15
import os

# 获取项目根目录（当前文件的所属文件夹，再获取上层文件夹）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试数据的根目录
CASEDATAS_DIR = os.path.join(BASE_DIR, "casedatas")

# 获取公共方法的根目录
COMMON_DIR = os.path.join(BASE_DIR, "common")

# 获取配置文件根目录
CONF_DIR = os.path.join(BASE_DIR, "conf")

# 获取定位文件的根目录
LOCATOR_DIR = os.path.join(BASE_DIR, "locator")

# 获取业务分离根目录（OP模型）
PAGES_DIR = os.path.join(BASE_DIR, "pages")

# 获取截图文件存储根目录
ERROR_IMAGES_DIR = os.path.join(BASE_DIR, r"test_result\error_images")

# 获取日志文件根目录
LOGS_DIR = os.path.join(BASE_DIR, r"test_result\log")

# 获取测试报告根目录
REPORTS_DIR = os.path.join(BASE_DIR, r"test_result\reports")

# 获取测试用例根目录
CASE_DIR = os.path.join(BASE_DIR, "testcase")
