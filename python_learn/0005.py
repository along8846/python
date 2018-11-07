#coding=utf-8
import  os
from PIL import Image


os.getcwd()
os.chdir(r'/Users/apple/PycharmProjects/11/python_learn/image')

def resize(filename):
    img = Image.open(filename)
    out = img.resize((640,1130),Image.ANTIALIAS)
    f = filename.strip(".png")
    newname = f+"r.png"
    out.save(newname)

list = os.listdir(r'/Users/apple/PycharmProjects/11/python_learn/image')
f_list=[]
def getextension():
    for i in list:
        if os.path.splitext(i)[1]=='.png':
            f_list.append(i)

getextension()

for i in  f_list:
    resize(i)