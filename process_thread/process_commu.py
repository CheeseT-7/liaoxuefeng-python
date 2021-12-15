#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : process_commu.py
#@ide    : PyCharm
#@time   : 2021-12-09 13:23:44
"""

from multiprocessing import Process, Queue
import os
import time
import random


# 写数据
def write(_q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        _q.put(value)
        time.sleep(random.random())


# 读数据
def read(_q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = _q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程，写入对应数据：
    pw.start()
    # 启动子进程，读取相应数据
    pr.start()
    # 等待写入数据的子进程结束
    pw.join()
    # 因读取数据子进程为死循环，需要强行终止
    pr.terminate()
