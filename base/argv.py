#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : argv.py
#@ide    : PyCharm
#@time   : 2021-10-15 17:41:19
"""

#
# def calc(*num):
#     sum_t = 0
#     for n in num:
#         sum_t = sum_t + n * n
#     return sum_t
#
#
# print(calc(*[1, 2]))


def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person('Jack', 24, city='BJ', job='Engineer')
