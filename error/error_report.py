#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : error_report.py
#@ide    : PyCharm
#@time   : 2021-11-14 13:23:00
"""


try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error')
finally:
    print('finally...')
print('END')
