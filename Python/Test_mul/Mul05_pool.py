# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 2:42 下午
# @Author  : xinquan
# @File    : Mul05_pool.py

from multiprocessing import Pool
import time
import os


def func(i):
    i += 1
    time.sleep(2)
    print(i, os.getpid())
    return i


if __name__ == '__main__':
    p = Pool(5)  # 创建进程池,池中有5个进程待命
    res_l = []
    for i in range(10):
        res = p.apply_async(func, args=(i,))  # 10个任务,派给5个进程,异步执行任务,5个进程同时5执行任务,那个先执行完任务就去接收下一个任务
        res_l.append(res)  # 拿到的结果是一个AsyncResult的实例obj,先将结果放入列表
    p.close()
    p.join()  # 异步执行需要join,因为异步调用的子进程都是守护进程,所以需要子进程都执行完,父进程才继续执行
    t = [i.get() for i in res_l]  # 异步机制,从AsyncResult的实例obj中get到实际结果,同步机制没有get()方法
    print(t)
    # 因为同步机制能直接拿到实际结果
    # 其实get()是阻塞等待的,也就是说,如果没有上边的close()和join()
    # 主进程一样会阻塞在get()等待进程池中给返回结果,进程池异步执行任务获取结果
    # 每次有一个进程返回结果后,就能get()一个结果,然后for循环到下一次继续阻塞,等待拿结果
