#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : file_r_w.py
#@ide    : PyCharm
#@time   : 2021-12-02 01:28:23
"""


# from io import StringIO
# f = StringIO('Hello!\n')
# old_content = f.getvalue()
# f.write(old_content)
# f.write(' ')
# f.write('World!')
#
# print(f.getvalue())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
