#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : sorted_method.py
#@ide    : PyCharm
#@time   : 2021-10-21 16:04:48
"""

# print(sorted([36, 5, -12, 9, -21], key=abs))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)
