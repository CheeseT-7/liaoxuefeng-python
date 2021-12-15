#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : sub_process.py
#@ide    : PyCharm
#@time   : 2021-12-09 01:56:45
"""

import subprocess

print('ping www.python.org')
r = subprocess.call(['ping', 'www.python.org'])
print('Exit code:', r)
