#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : debug.py
#@ide    : PyCharm
#@time   : 2021-11-22 11:50:44
"""


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


main()
