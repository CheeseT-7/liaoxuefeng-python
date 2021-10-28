#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : return_method.py
#@ide    : PyCharm
#@time   : 2021-10-22 09:22:31
"""


def create_counter():
    list1 = [0]

    def counter():
        list1[0] = list1[0] + 1
        return list1[0]
    return counter


# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
