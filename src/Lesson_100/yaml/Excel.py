#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 15:44
import xlrd

from datetime import date,datetime
def read_excel():
    #文件位置

    Excel_file=xlrd.open_workbook(r"D:\test.xlsx".encode("utf-8"),encoding_override="utf-8")
    #获取EXCEL文件的sheet名称
    print(Excel_file.sheet_by_names())
    sheet2_name=Excel_file.sheet_by_index(1)
    #sheet_name=Excel_file.sheet_by_name("TestCase")
    print(sheet2_name)
    #获取整行
        #返回由该行中所有的单元格对象组成的列表
    rows_3=sheet2_name.row(3);
        #回由该列中所有的单元格对象组成的列表
    rows_3_10=sheet2_name.row_slice(rows_3)
        #返回所有的列内容
    rows_4_10=sheet2_name.row_values(start_colx=0,end_colx=None)
    #获取整列
    #colnum 列操
    ## 作回由该列中所有的单元格对象组成的列表
    sheet_2_colnum=Excel_file.sheet_by_name("Testcase").col(start_rowx=0,end_rowx=None)
    sheet2_colnums=Excel_file.sheet_by_name("TestCase").col_slice(start_rowx=0,end_rowx=None)
    sheet2_colnums_value=Excel_file.sheet_by_name("Testcase").col_values(start_rowx=0,end_rowx=None)
    #返回单元格指定的数据
    value=Excel_file.sheet_by_name("Testcase").cell(2,5)
    value=Excel_file.sheet_by_name("Testcase").col_values(2,3)
    #解决中文编码问题
    file=filename.decode


