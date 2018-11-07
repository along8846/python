#coding=utf-8
import os,sys


file_lst = []
def get_files(path,lang='py'):
    ##遍历出path目录下所有文件
    file_paths = []
    for root,dirs,files in os.walk(path):  #将os.walk在元素中提取的值，分别放到root（根目录），dirs（目录名），files（文件名）中。
        for file in files:
            file_abs_path =  os.path.join(root,file)  #根目录与文件名组合，形成绝对路径。
            file_paths.append(file_abs_path)
    py_files = []
    for files in file_paths:
        if files.split('.')[-1]==lang:
            py_files.append(files)
    return py_files

def count(files):
    line_of_code, blank, comments = 0,0,0
    for filename in files:
        f = open(filename,'rb')
        for line in f:
            line = line.strip() #去除首尾空格
            line_of_code += 1
            if line=="":
                blank += 1
            elif line[0] == '#' or line[0] == '/':
                comments += 1
    return (line_of_code,blank,comments)
if __name__=='__main__':
    path = r'/Users/apple/PycharmProjects/11/python_learn'
    files = get_files(path)
    print files
    lines = count(files)
    print 'Line(s): %d, blank line(s): %d, comments line(s): %d' % (lines[0], lines[1], lines[2])