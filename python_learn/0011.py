#coding=utf-8
user_input = raw_input('Please say something:')
#print(user_input)

for filter_word in open('0011.txt'):
    if filter_word.rstrip() in user_input:
        print('Freedom!')
        break
else:
    print('Human Rights!')