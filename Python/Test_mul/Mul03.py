# -*-coding:utf-8-*-
# @Time    : 2019/6/17 0017 17:02
# @Author   :zhuxinquan
# @File    : Mul03.py


import multiprocessing
import threading
import time


def m_test():
    for i in range(2):
        t=threading.Thread(target=t_test)
        t.setDaemon(True)
        t.start()
        t.join()

def t_test():
    n=10
    while n>0:
        print('这是进程{0},线程{1}'.format(multiprocessing.current_process(),threading.current_thread()))
        n-=1
        print(n)
        # time.sleep(0.02)

for i in range(4):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    for i in range(2):
        pool.apply_async(m_test)
    print('第{}个进程'.format(i))
    pool.close()
    pool.join()

