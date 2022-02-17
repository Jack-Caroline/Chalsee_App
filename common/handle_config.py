#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/17 12:15
import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, filename, encoding='utf-8'):
        """
        继承父类初始化方法
        :param filename: 文件名
        :param encoding: 文件编码类型，默认 utf-8
        """
        super.__init__()
        self.read(filename, encoding=encoding)


# 创建一个配置文件解析器
conf = Config(os.path.join(CONF_DIR, "config.ini"))
