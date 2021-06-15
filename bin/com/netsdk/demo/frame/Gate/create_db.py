# * coding:utf-8 *
"""
 # File   : p_sqlite.PY
 # Time   : 2021/4/6 10:14
 # Author : Lethe
 # version: python 3.8
"""
from builtins import print as _print
from sys import _getframe
import sqlite3


def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno}行：'
    return _print(s, *arg, **kw)


# print(sqlite3.version)
# print(sqlite3.sqlite_version)

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('gate.db')
print("Opened database successfully")

# 创建游标
cursor = conn.cursor()

# 创建表——进门记录
sql = 'CREATE TABLE InRecode(pk integer PRIMARY KEY autoincrement, ' \
      'Name varchar(30), NameId varchar(30), DATETIME DATETIME, STATE integer DEFAULT 0);'
cursor.execute(sql)

# 创建表——出门记录
sql = 'CREATE TABLE OutRecode(pk integer PRIMARY KEY autoincrement, Name varchar(30), NameId varchar(30), DATETIME DATETIME);'
cursor.execute(sql)

# 插入数据。
# sql = "INSERT INTO InRecode (NAME,NameId,DATETIME) VALUES ('李雷',25, '2021/4/6 11:14:1')"
# cursor.execute(sql)

# 提交事物
conn.commit()
conn.close()
