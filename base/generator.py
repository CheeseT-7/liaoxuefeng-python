#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : generator.py
#@ide    : PyCharm
#@time   : 2021-10-18 16:16:39
"""


# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

def fib(_max):
    n, a, b, = 0, 0, 1
    while n < _max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'


g = fib(6)
