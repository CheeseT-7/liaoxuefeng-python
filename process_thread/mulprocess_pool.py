#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : mulprocess_pool.py
#@ide    : PyCharm
#@time   : 2021-12-08 16:58:29
"""

from multiprocessing import Pool
import os
import time
import random


def log_time_task(name):
    print('Run task %s (%s), ppid:%s...' % (name, os.getpid(), os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, end - start))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(7):
        p.apply_async(log_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
