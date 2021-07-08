# -*- coding: utf-8 -*-
from xlutils.copy import copy
import xlrd
import xlwt
import os
from datetime import date, datetime


def Update_Excel(path, test):
    path = path
    b = os.listdir(path)

    for i in b:
        c = os.path.join(path, i)
        d = c[-4::1]
        if d == 'xlsx':
            path2 = c[:-1:]
            rb = xlrd.open_workbook(c)
            wb = copy(rb)
            ws = wb.get_sheet(0)
            ws.write(0, 1, test)
            os.remove(c)
            wb.save(path2)
            print('{0}文件修改成功'.format(c))
        elif d == '.xls':
            path2 = c
            rb = xlrd.open_workbook(c)
            wb = copy(rb)
            ws = wb.get_sheet(0)
            ws.write(0, 1, test)
            os.remove(c)
            wb.save(path2)
            print('{0}文件修改成功'.format(c))
        else:
            os.remove(c)
            print('{0}文件修改失败，已删除'.format(c))

    # wb = xlrd.open_workbook(path)
    # rb = xlrd.open_workbook(path)    #打开weng.xls文件
    # wb = copy(rb)                          #利用xlutils.copy下的copy函数复制
    # ws = wb.get_sheet(0)                   #获取表单0
    # ws.write(0, 0, 'changed!')             #改变（0,0）的值
    # ws.write(1, 0, label='好的')           #增加（8,0）的值
    # wb.save(path2)
if __name__ == '__main__':
    os.chdir('/Users/zongshuren/Desktop/测试批量修改Excel内容')
    excel_path = os.getcwd()
    Update_Excel(path=excel_path, test='2 word')