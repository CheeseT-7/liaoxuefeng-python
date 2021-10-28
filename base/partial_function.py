#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : partial_function.py
#@ide    : PyCharm
#@time   : 2021-10-27 16:33:36
"""


# def int2(x, base=2):
#     return int(x, base)
#
#
# print(int2('1000'))

import functools

int2 = functools.partial(int, base=10)
print(int2('1010101'))

max2 = functools.partial(max, 22)
print(max2(4, 6, 9))
