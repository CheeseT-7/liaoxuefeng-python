#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : lambda_func.py
#@ide    : PyCharm
#@time   : 2021-10-22 11:33:33
"""


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

print(list(filter(lambda n: n % 2 == 1, range(1, 20))))
