#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : oop_high_grade-slots.py
#@ide    : PyCharm
#@time   : 2021-11-05 09:50:20
"""


class Father(object):
    __slots__ = ('age', 'name')


class Son(Father):
    __slots__ = ('subject', 'country')

    def __init__(self):
        pass


s = Son()
s.subject = 'Math'
s.age = '18'
