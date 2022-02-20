#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/17 12:16
import pymssql


class DB:
    def __init__(self):
        """
        初始化数据库，连接数据库信息
        创建游标对象
        """
        self.con = pymssql.connect(
            host="10.251.251.101",
            user="uatlink",
            password="ABC.123"
        )
        self.cur = self.con.cursor()

    def find_data(self, sql):
        """
        查询 SQL 数据
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def updata_data(self, sql):
        """
        修改 SQL 语句
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()

    def close_data(self):
        """
        关闭资源
        :return:
        """
        self.cur.close()
        self.con.close()
