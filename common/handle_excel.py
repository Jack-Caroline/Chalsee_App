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
        """
        打开 excel 表格中文件，表单
        :return:
        """
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_excel(self):
        """
        读取表单中数据，将数据处理为可数据驱动的格式
        读取第一行表头
        依次读取其他行数据，然后和第一行表头进行 zip 打包
        :return:
        """
        self.open()
        res = list(self.sh.rows)
        title = []
        case_datas = []
        for t in res[0]:
            title.append(t.value)
        for row in res[1:]:
            data = []
            for v in row:
                data.append(v.value)
            case = dict(zip(title, data))
            case_datas.append(case)
        return case_datas

    def write_excel(self, row, column, value):
        """
        写入数据
        :param row: 行
        :param column: 列
        :param value: 数据值
        :return:
        """
        self.sh.cell(row=row, column=column, value=value)

    def save_excel(self):
        """
        保存 Excel 表格
        :return:
        """
        self.wb.save(self.filename)
