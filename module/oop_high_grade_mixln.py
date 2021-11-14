#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : oop_high_grade_mixln.py
#@ide    : PyCharm
#@time   : 2021-11-05 14:16:58
"""


# 动作
class Runnable(object):
    def run(self):
        print('Running')


class Flyable(object):
    def fly(self):
        print('Flying')


class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


bat = Bat()
bat.fly()
