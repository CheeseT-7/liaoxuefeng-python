#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : oop_high_grade_enum.py
#@ide    : PyCharm
#@time   : 2021-11-11 10:08:38
"""

# from enum import Enum
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, ' =>', member, ',', member.value)

# from enum import Enum, unique
#
#
# @unique  # 此装饰器可以检查保证没有重复值
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
