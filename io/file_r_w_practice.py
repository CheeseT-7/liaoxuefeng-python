#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : file_r_w_practice.py
#@ide    : PyCharm
#@time   : 2021-12-04 01:56:08
"""
import os
import sys

"""
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
并打印出相对路径。
"""


def search_dir(path, keyword):
    keyword_file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword in file:
                keyword_file_list.append(os.path.join(root, file))

    print(keyword_file_list)


if __name__ == '__main__':
    tar_path = r'..\module'
    file_keyword = 'oop'
    search_dir(tar_path, file_keyword)
