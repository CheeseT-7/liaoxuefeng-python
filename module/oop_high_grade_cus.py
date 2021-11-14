#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : oop_high_grade_cus.py
#@ide    : PyCharm
#@time   : 2021-11-05 19:05:09
"""


class Student(object):
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return 'Student object(name: %s)' % self.name

    def __repr__(self):
        return 'this is repr'


print(Student('Michael'))
s = Student('Michael')


# class Fib():
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100000:
#             raise StopIteration
#         return self.a
#
#
# for n in Fib():
#     print(n)

# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
#
# f = Fib()
# print(f[100])

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a+b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             l1 = []
#             for x in range(stop):
#                 if x >= start:
#                     l1.append(a)
#                 a, b = b, a+b
#             return l1
#
#
# f = Fib()
# print(f[:100])


# class Student(object):
#     def __init__(self):
#         self.name = 'a'
#
#     def __getattr__(self, item):
#         if item == 'age':
#             return 25
#
#
# s = Student()
# print(s.name)
# print(s.address)


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         print('My name is %s.' % self.name)
#
#
# s = Student('Michael')
# s()
