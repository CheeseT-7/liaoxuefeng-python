#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : oop_high_grade_meta.py
#@ide    : PyCharm
#@time   : 2021-11-12 22:05:40
"""


# def fn(self, name='world'):
#     print('Hello, %s.' % name)
#
#
# Hello = type('Hello', (object,), dict(hello=fn))
#
# h = Hello()
# h.hello()


# metaclass是类的模版，所以必须从‘type’类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    def add(self, param):
        pass


l1 = MyList()
l1.add(1)
print(l1)
