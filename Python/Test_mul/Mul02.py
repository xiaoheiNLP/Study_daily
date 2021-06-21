# -*-coding:utf-8-*-
# @Time    : 2019/6/17 0017 16:48
# @Author   :zhuxinquan
# @File    : Mul02.py
from multiprocessing import Manager, Process, Lock
def work(d,lock):
    # with lock:      # 不加锁而操作共享的数据,肯定会出现数据错乱
    #     d['count'] += 1
    d['count'] += 1


if __name__ == '__main__':
    lock = Lock()
    with Manager() as m:
        dic = m.dict({'count': 100})
        p_l = []
        for i in range(100):
            p = Process(target=work, args=(dic, lock))
            p_l.append(p)
            p.start()
        for p in p_l:
            p.join()
        print(dic)