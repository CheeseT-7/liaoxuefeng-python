#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : quadratic.py
#@ide    : PyCharm
#@time   : 2021-10-14 08:50:25
"""

# print('\u4e2d\u6587')
#
# a = '\u4e2d'.encode('utf-8')
# print(a)
#
# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
#
# print(b'abc')

import math


def quadratic(a, b, c):
    r_sqrt = math.sqrt(b ** 2 - 4 * a * c)
    r1 = (-b + r_sqrt) / (2 * a)
    r2 = (-b - r_sqrt) / (2 * a)
    return r1, r2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

