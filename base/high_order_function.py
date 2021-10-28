#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : high_order_function.py
#@ide    : PyCharm
#@time   : 2021-10-20 15:51:39
"""

# def f(x):
#     return x ** 2
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

# from functools import reduce


# def normalize(name):
#     return name.title()
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# def prod(l1):
#     return reduce(lambda x, y: x * y, l1)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def is_odd(n):
#     return n % 2 == 1
#
#
# print(list(filter(is_odd, [0, 1, 2, 3, 4, 5, 7, 9, 11])))


# # 埃式筛法
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# def _not_divisible(n_1):
#     return lambda y: y % n_1 > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
#
# for x in primes():
#     if x < 10:
#         print(x)
#     else:
#         break


def is_palindrome(n):
    str_n = str(n)
    if str_n[:] == str_n[-1::-1]:
        return True
    else:
        return False


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')