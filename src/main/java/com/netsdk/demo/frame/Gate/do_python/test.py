# * coding:utf-8 *
"""
 # File   : test.PY
 # Time   : 2021/6/11 11:28
 # Author : Lethe
 # version: python 3.8
"""
import datetime
from builtins import print as _print
from sys import _getframe


def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno}行：'
    return _print(s, *arg, **kw)


from sqlalchemy import create_engine, MetaData, Table, update, select, text,insert


engine = create_engine('sqlite:///..\\gate.db', future=True, connect_args={'check_same_thread': False})
metadata = MetaData()
in_table = Table('InRecode', metadata, autoload=True, autoload_with=engine)
out_table = Table('OutRecode', metadata, autoload=True, autoload_with=engine)
con = engine.connect()

# sql = insert(in_table).values({"Name":'Lili', "NameId":"33333", "DATETIME": datetime.datetime.now()})
sql = insert(in_table).values(Name='LiLei', NameId="33333", DATETIME=datetime.datetime.now())
con.execute(sql)
con.commit()
print(dir(con))