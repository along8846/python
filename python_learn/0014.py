#coding=utf-8
import json
import os
from collections import OrderedDict
import xlwt

def run_1():
    with open('student.txt', 'r') as f:
        content = f.read()

        # 转化为json，注意转化后的dict的元素位置可能和转化前可能不一样，因此需要ordereddict
    # loads()方法把str对象反序列化为json对象，自定义解码器为ordereddict
    d = json.loads(content, object_pairs_hook=OrderedDict)
    print(d)
    # 初始化xls文件
    file = xlwt.Workbook()
    # 添加sheet,工作表，名字为test
    table = file.add_sheet('test')
    for row, i in enumerate(d):  # 读取所有字典，row为序号，i为字典关键字key
        table.write(row, 0, i)  # 写入（行号，列号，key)
        for col, j in enumerate(d[i]):  # col为序号，j为value,有多个，需要迭代
            table.write(row, col + 1, j)

    file.save('student.xls')


def run_2():
    with open('city.txt', 'r') as f:
        content = f.read()
    d = json.loads(content, object_pairs_hook=OrderedDict)
    file = xlwt.Workbook()
    table = file.add_sheet('test')
    for row, i in enumerate(d):  # 读取所有字典，row为序号，i为字典关键字key
        print row, i , d[i]
        table.write(row, 0, i)  # 写入（行号，列号，key)
        table.write(row,1,d[i])
    file.save('city.xls')


def run_3():
    with open('numbers.txt','r') as f:
        content = f.read()
    d = json.loads(content,object_pairs_hook=OrderedDict)
    file = xlwt.Workbook()
    table = file.add_sheet('test')
    for row ,i in enumerate(d):
        print row, i
        for col, j in enumerate(i):
            print col, j
            table.write(row,col,j)
    file.save('number.xls')

run_3()