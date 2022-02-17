#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/17 11:57
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.handle_config import conf
from common.handle_path import LOGS_DIR


class HandleLog:

    @staticmethod
    def create_log():
        # 创建一个收集器
        log = logging.getLogger("小金_log")
        log.setLevel(conf.get("loggging", "level"))
        # 创建一个输出到文件的渠道
        fn = TimedRotatingFileHandler(os.path.join(LOGS_DIR, conf.get("loggging", "log_name")), when='d', interval=1,
                                      backupCount=7, encoding="utf-8")  # 设置文件轮转条件，文件名、单位、轮转时间、文件保存数量、编码格式
        fn.setLevel(conf.get("logging", "fn_level"))
        log.addHandler(fn)

        # 创建一个输出到控制台的渠道
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("logging", "sh_level"))
        log.addHandler(sh)

        # 设置输出日志的格式
        formatter = "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        mate = logging.Formatter(formatter)

        fn.setFormatter(mate)  # 设置日志文件输出格式
        sh.setFormatter(mate)  # 设置控制台输出格式

        return log


# 创建一个日志收集器
log = HandleLog.create_log()
