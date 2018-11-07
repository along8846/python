#coding=utf-8


import string, random

#激活码中的字符和数字
field = string.ascii_letters + string.digits

#获得四个字母和数字的随机组合
def getRandom(x=4):
    return "".join(random.sample(field,x))

#生成的每个激活码中有几组
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

#生成n组激活码,默认为2组四位密码，long对应组，
def generate(n,l=2):
    return [concatenate(l) for i in range(n)]

if __name__ == '__main__':
    lst = generate(6,4)
    print(lst)
    filename = "0001.txt"
    with open(filename,'w') as file:
        for i in lst:
            file.write(i+"\n")
