#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : debug_pdb.py
#@ide    : PyCharm
#@time   : 2021-11-24 18:44:16
"""

import pdb

s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
