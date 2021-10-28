#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : decorator_practice.py
#@ide    : PyCharm
#@time   : 2021-10-27 16:07:05
"""

import time
import functools


def metric(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        print('start')
        result = fn(*args, **kwargs)
        print('%s executed in %.6s ms' % (fn.__name__, time.time() - start))
        print('end')
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
