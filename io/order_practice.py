#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : order_practice.py
#@ide    : PyCharm
#@time   : 2021-12-05 19:02:33
"""
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
s = json.dumps(obj, ensure_ascii=False)
print(s)
