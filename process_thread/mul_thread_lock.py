#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : mul_thread_lock.py
#@ide    : PyCharm
#@time   : 2021-12-10 20:12:06
"""

import time
import threading


balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000000):
        change_it(n)


def run_thread_lock(n):
    for i in range(10000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


if __name__ == '__main__':
    start_time = time.time()
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    # t1 = threading.Thread(target=run_thread_lock, args=(5,))
    # t2 = threading.Thread(target=run_thread_lock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    end_time = time.time()
    print('Time: %0.2f' % (end_time - start_time))
