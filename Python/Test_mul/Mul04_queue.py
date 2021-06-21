# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 10:55 上午
# @Author  : xinquan
# @File    : Mul04_queue.py
"""
基于队列queue的多进程:
https://blog.csdn.net/qq_25171075/article/details/81871537#Process模块介绍
进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。
"""

'''
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
1:可以往队列里放任意类型的数据 2 队列：先进先出
'''

import os
import random
import time
from multiprocessing import Process, Queue


def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))


def producer(q):
    for i in range(100):
        time.sleep(random.randint(1, 3))
        res = '包子%s' % i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))


if __name__ == '__main__':
    q = Queue()
    # 生产者们:即厨师们
    p1 = Process(target=producer, args=(q,))

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q,))

    # 开始
    p1.start()
    c1.start()
    print('主')
