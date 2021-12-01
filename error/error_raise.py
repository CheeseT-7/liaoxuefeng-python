#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : error_raise.py
#@ide    : PyCharm
#@time   : 2021-11-22 10:56:46
"""


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
