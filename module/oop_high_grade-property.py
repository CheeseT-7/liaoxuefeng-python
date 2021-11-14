#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : oop_high_grade-property.py
#@ide    : PyCharm
#@time   : 2021-11-05 09:57:30
"""

#
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#
# s = Student()
# s.score = 60
# print('s.score =', s.score)
# # ValueError: score must between 0 ~ 100!
# s.score = 9999


# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         print('return age')
#         return 2021 - self._birth
#
#
# s = Student()
# s.birth = 1996
# print(s.birth)
# print(s.age)
# s.age = 13


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return 786432


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
