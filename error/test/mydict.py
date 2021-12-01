#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : mydict.py
#@ide    : PyCharm
#@time   : 2021-11-30 10:14:24
"""


class Dict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'." % key)

    def __setattr__(self, key, value):
        self[key] = value
