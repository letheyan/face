# * coding:utf-8 *
"""
 # File   : __init__.py.PY
 # Time   : 2021/4/6 16:01
 # Author : Lethe
 # version: python 3.8
"""
from builtins import print as _print
from sys import _getframe


def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno}行：'
    return _print(s, *arg, **kw)
