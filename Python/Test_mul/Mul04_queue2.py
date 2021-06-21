# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 10:55 上午
# @Author  : xinquan
# @File    : Mul04_queue.py

from multiprocessing import Process, Queue
import time

def consumer(name, queue):
    while 1:
        weapon = queue.get()  # 从队列中不断取最先放进的武器
        if not weapon:  # 取出的是生产完毕标识
            break  # 跳出死循环
        print("\033[31m%s购买了%s" % (name, weapon))
        time.sleep(3)


def producer(name, queue):
    for i in range(20):
        weapon = "\033[36m%s生产的第%s件武器\033[0m" % (name, i + 1)
        print(weapon)
        queue.put(weapon)  # 放入生产的武器
        time.sleep(2)
    queue.put(None)  # 生产完毕标识



if __name__ == '__main__':
    q = Queue(10)  # 队列最大容量10
    pro_1 = Process(target=producer, args=("torbjorn", q))
    con_1 = Process(target=consumer, args=("mccree", q))
    pro_1.start()
    con_1.start()

