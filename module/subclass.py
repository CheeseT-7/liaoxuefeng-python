#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : subclass.py
#@ide    : PyCharm
#@time   : 2021-11-01 17:27:27
"""


# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#
#     def eat(self):
#         print('Dog is eating')
#
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running')
#
#
# dog = Dog()
# dog.run()
# dog.eat()
#
# cat = Cat()
# cat.run()


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
