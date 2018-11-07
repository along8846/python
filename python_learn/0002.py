#coding=utf-8
import pymysql


list_id = []
with open("0001.txt",'r') as file:
    files = file.readlines()
    for content in files:
        list_id.append(str(content).replace('\n', ''))
try:
    conn = pymysql.connect("localhost", "root", "88461296")
    cur = conn.cursor()
    cur.execute('create database if not exists test1')
    conn.select_db('test1')
    cur.execute('create table if not exists Activation_code(id int ,uuid varchar(50))')
    for i in range(len(list_id)):
        cur.execute('insert into Activation_code values(%s,%s)', (i + 1, list_id[i]))
    conn.commit()
    cur.close()
    conn.close()
except pymysql.Error as e:
#except ValueError as e:
    print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
finally:
    print('finally' * 20)