#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : module_use.py
#@ide    : PyCharm
#@time   : 2021-10-28 11:10:14
"""

import sys
'a test module'

__author__ = 'CheeseT'


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello %s' % args[1])
    else:
        print('too many arguments')


if __name__ == '__main__':
    test()
