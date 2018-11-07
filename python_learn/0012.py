#coding=utf-8
user_input = raw_input('Please say something:')
#print(user_input)

for filter_word in open('0011.txt'):
    fw = filter_word.rstrip() #去掉读取文本时候的\n
    if fw in user_input:
        fw_len = len(fw)
        print fw
        print fw_len
        user_input = user_input.replace(fw,'*'*fw_len)
else:
    print(user_input)