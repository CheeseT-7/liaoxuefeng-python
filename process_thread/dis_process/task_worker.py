#!/user/bin/env python
# coding=utf-8
"""
@project : dis_process
@author  : CheeseT
#@file   : task_worker.py
#@ide    : PyCharm
#@time   : 2021-12-15 01:50:16
"""

import time
import sys
import queue
from multiprocessing.managers import BaseManager


# 创建类似QueueManager的类
class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只能从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器
server_address = '127.0.0.1'
print('Connect to server %s...' % server_address)
# 端口和验证码注意与task_master.py设置的完全一致
m = QueueManager(address=(server_address, 5000), authkey=b'abc')
# 从网络连接
m.connect()
# 获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列中取任务，并将结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')

# 处理结束
print('worker exit.')



