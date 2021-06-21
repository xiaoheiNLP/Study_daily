# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 5:52 下午
# @Author  : xinquan
# @File    : numpy02.py
import numpy as np


def test_max():
    t1 = np.random.rand(3)
    t2 = np.random.rand(3,)
    print(t1)
    print(t2)
    t3 = np.array([t1, t2])
    print(np.amax(t3, axis=0))

def test():
    t1 = np.random.rand(3, 2)
    print(t1)
    print()
    print(t1.max(axis=1))



if __name__ == '__main__':
    test()


