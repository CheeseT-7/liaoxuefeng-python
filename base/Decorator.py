#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : Decorator.py
#@ide    : PyCharm
#@time   : 2021-10-22 16:50:11
"""


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# @log
# def now():
#     print('2021-10-27')
#
#
# now()
# print(now.__name__)




import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2021-10-27')


now()
print(now.__name__)
