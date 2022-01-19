# -*- coding:utf-8 -*-
# @author:Jhon
# @software: PyCharm
# @file:get_Excel.py
# @time:2022/1/10 14:38
import xlrd
import json
#可以作为自动识别用例数
def get_excelData(sheetName,caseName):
    resList = []
    excelDir = '../data/Control_excel.xls' #获取Excel表路径
    workBook = xlrd.open_workbook(excelDir,formatting_info=True) #打开 formatting_info=True  保持样式
    worksheet = workBook.sheet_by_name(sheetName) #获取某一个指定的表
    #读取一列数据
    idx = 0
    for one in worksheet.col_values(0):
        if caseName in one:
            cellData = worksheet.cell_value(idx,9)#读取单元格--返回字符串--cell(行号，列号) 从0开始
            respData = worksheet.cell_value(idx,11)#相应数据
            resList.append((json.loads(cellData),json.loads(respData)))#封装元组到一个列表
        idx += 1
    return resList