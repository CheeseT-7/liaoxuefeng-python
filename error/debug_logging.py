#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : debug_logging.py
#@ide    : PyCharm
#@time   : 2021-11-24 12:16:31
"""

import logging
logging.basicConfig(level=logging.INFO)


s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

