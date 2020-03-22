#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   proxls.py.py    
@Contact :   tango@163.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-03-22 16:43   tango      1.0         None
'''


from openpyxl import Workbook
from openpyxl.styles import Font

class Xlsx():
    def __init__(self):
        self.workbook = Workbook()
        self.index=1
        pass

    def add_sheet(self,sheetname="Sheet"):
        return self.workbook.create_sheet(sheetname,self.index+1)

    def add_data(self,data,sheet="Sheet"):
        '''
        :param sheet :sheet对象
        :param data: data最好是一个元组
        :return:
        '''
        if isinstance(data,tuple):
            sheet.append(data)
        else:
            sheet.append(tuple(data))


    def set_header_font(self,sheetname="Sheet"):
        '''
        格式化行头
        :param sheetname:
        :return:
        '''
        font = Font(u'宋体', size=13, bold=True, color='000000')
        for i in sheetname["1"]:
            i.font = font


    def delete_sheet(self,sheetname="Sheet"):
        '''
        删除sheet
        :param sheetname:
        :return:
        '''
        self.workbook.remove(self.workbook[sheetname])

    def save(self,filename):
        self.workbook.save(filename)