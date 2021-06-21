# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 7:24 下午
# @Author  : xinquan
# @File    : numpy01.py
import numpy as np


def numpy_add():
    # mydata1 = np.random.rand(105, 20, 7000)
    # mydata1 = np.arange(48).reshape(6, 4, 2)
    mydata1 = np.arange(24).reshape(2, 3, 4)
    print(mydata1)
    print("*"*89)
    r1 = mydata1.sum(axis=1)
    print(r1)
    print(np.shape(r1))
    print("*"*89)
    r2 = mydata1.sum(axis=0)
    print(r2)
    print(np.shape(r2))
    print("*"*89)
    r3 = mydata1.sum(2)
    print(r3)
    print(np.shape(r3))


def numpy_T():
    mydata1 = np.arange(24).reshape(2, 3, 4)
    print(mydata1)
    print("*"*89)

    mydata2 = mydata1.transpose((2, 0, 1))
    print(mydata2)



def MyNeed():
    # mydata1 = np.random.rand(105, 20, 7000)
    # print(mydata1)
    # print("*"*89)
    # r1 = mydata1.sum(2)
    # print(r1)
    # print(np.shape(r1))
    mydata2 = np.ones((10, 4, 7000))
    mydata2[mydata2.any() == 1] = 1
    print(mydata2.sum(2))
    t_str = "asdsadsa"
    t_str.split()


if __name__ == '__main__':
    # numpy_add()
    # numpy_T()
    # MyNeed()
    from multiprocessing import cpu_count
    print(cpu_count())

