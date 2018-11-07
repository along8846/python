#coding=utf-8
"""
 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
import os,sys
path = r'/Users/apple/PycharmProjects/11/python_learn'

file_lst = []
def dirlist(path):
    ##遍历出path目录下所有文件
    file_paths = []
    for root,dirs,files in os.walk(path):  #将os.walk在元素中提取的值，分别放到root（根目录），dirs（目录名），files（文件名）中。
        for file in files:
            file_abs_path =  os.path.join(root,file)  #根目录与文件名组合，形成绝对路径。
            file_paths.append(file_abs_path)
    py_files = []
    for files in file_paths:
        if files.split('.')[-1]=='py':
            py_files.append(files)
    print py_files

    return file_paths
dirlist(path)

    """
           #截取文件扩展名进行刷选
            postfix = os.path.splitext(file_abs_path)[1]
            if postfix == '.py':
                with open(file_abs_path) as fp:
                    while true:
                        line = fp.readline()
                        if  line:
                            break
                        elif:
                            line.strip().startswith('#')
                            comm_lines += 1
   
    if __name__=='__main__':
    path = r'/Users/apple/PycharmProjects/11/python_learn'
    print dirlist(path)
    """