#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/17 11:56
import openpyxl


class Excel:
    def __init__(self, filename, sheet_name):
        """
        初始化 excel 表格
        :param filename: 文件名称
        :param sheet_name: 表单名称
        """
        self.filename = filename
        self.sheet_name = sheet_name

    def open(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_excel(self):
        pass

    def write_excel(self, row, column, value):
        self.sh.cell(row=row, column=column, value=value)

    def save_excel(self):
        self.wb.save(self.filename)
