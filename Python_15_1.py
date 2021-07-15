import sqlite3
import os

# if os.path.exists('homework_db.sqlite'):
#     os.remove('homework_db.sqlite')


homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 33, '作业数': 5},
                 {'姓名': '学员3', '年龄': 32, '作业数': 10}]

conn = sqlite3.connect('homework_db.sqlite')
cursor = conn.cursor()

cursor.execute("create table qytang_homework_info(姓名 varchar(40), 年龄 int, 作业数 int)")

for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']
    cursor.execute("insert into qytang_homework_info values ('%s', %d, %d)" % (name, age, homework))

conn.commit()

