#!/user/bin/env python
# coding=utf-8
"""
@project : liaoxuefeng-python
@author  : CheeseT
#@file   : task_master.py
#@ide    : PyCharm
#@time   : 2021-12-15 01:14:03
"""

import random
import queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000，设置验证码‘abc’
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象
    # 在一台机上上进行多进程程序时，创建的Queue可以直接使用，
    # 在分布式情况下，添加到任务的Queue不可以直接对原始的task_queue进行操作，那样就会绕过manager的封装
    # 必需通过manager.get_task_queue()获得的Queue接口添加
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d' % n)
        task.put(n)
    # 从result队列读取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)  # 等待10s，若无数据获取，则抛出异常
        print('Result: %s...' % r)
    # 关闭
    manager.shutdown()
    print('master.exit')
